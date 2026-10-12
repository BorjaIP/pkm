#!/usr/bin/env python3
"""Suggest (and optionally add) wikilinks between existing notes.

Finds places where a page's prose mentions the exact name of a concept note
(notes/*.md and their aliases) without linking it. Dry run by default.

Usage:
  python .claude/scripts/suggest_links.py                       # summary + top suggestions
  python .claude/scripts/suggest_links.py --page "Helm"         # one page, all suggestions
  python .claude/scripts/suggest_links.py --target "Kubernetes" # where could [[Kubernetes]] be linked
  python .claude/scripts/suggest_links.py --orphans             # orphan pages + related candidates by shared tags
  python .claude/scripts/suggest_links.py --hub-gaps            # articles a hub should list but does not (--apply adds them)
  python .claude/scripts/suggest_links.py --apply --page "Helm" [--max-per-page 3]
  python .claude/scripts/suggest_links.py --apply --all [--max-per-page 3]

Rules: exact-case whole-word match; only the FIRST mention per target per page is linked; never inside
frontmatter, headings, tables, code, URLs, existing links or the page's own name. Very generic names are
skipped unless --include-generic is given.
"""
import argparse
import collections
import re
from pkmlib import VAULT, iter_pages, read_text, write_text, utf8_stdout, FM_RE

GENERIC = {"Web", "Tools", "Arch", "Awesome", "Vault", "Testing", "Security", "Cloud", "Obsidian", "Hugo",
           "Nix", "Remote Access", "Homelab", "Trading", "FOSS", "XaaS", "PaaS", "Claude"}
MASK_RE = re.compile(r"`[^`\n]*`|\[\[.*?\]\]|\[[^\]]*\]\([^)]*\)|https?://\S+|<[^>]+>")
SKIP_LINE = re.compile(r"^\s*(#|\||>|- Type:|- Source:|- https?://|!\[\[|---|\*\*Status)")


def targets(pages, include_generic):
    """name -> canonical page name, for concept notes and their aliases."""
    out = {}
    for p in pages:
        if p.area != "notes":
            continue
        for nm in [p.name] + p.aliases:
            nm = nm.strip()
            if len(nm) < 3 and not re.fullmatch(r"[A-Z0-9]{2}", nm):
                continue
            if nm in GENERIC and not include_generic:
                continue
            out[nm] = p.name
    return out


def eligible_lines(body):
    in_fence = False
    for i, ln in enumerate(body.split("\n")):
        if ln.strip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence or SKIP_LINE.match(ln):
            continue
        yield i, ln


def find_mentions(page, names, include_generic):
    """List of (target_canonical, matched_text, line_no, snippet) first mention per target."""
    linked = {l.lower() for l in page.links()}
    own = {page.name.lower()} | {a.lower() for a in page.aliases}
    found = {}
    ordered = sorted(names, key=len, reverse=True)           # longest first: "Docker Compose" before "Docker"
    for i, ln in eligible_lines(page.body):
        masked = MASK_RE.sub(lambda m: " " * len(m.group(0)), ln)
        taken = [False] * len(masked)
        for nm in ordered:
            canon = names[nm]
            if canon.lower() in linked or canon.lower() in own or nm.lower() in own or canon in found:
                continue
            m = re.search(r"(?<![\w\-/#.])" + re.escape(nm) + r"(?![\w\-/])", masked)
            if not m or any(taken[m.start():m.end()]):
                continue
            for k in range(m.start(), m.end()):
                taken[k] = True
            found[canon] = (canon, nm, i, ln.strip()[:140])
    return list(found.values())


def apply_to_page(page, mentions, max_per_page):
    lines = page.body.split("\n")
    done = []
    for canon, nm, i, _ in mentions[:max_per_page]:
        ln = lines[i]
        masked = MASK_RE.sub(lambda m: " " * len(m.group(0)), ln)
        m = re.search(r"(?<![\w\-/#.])" + re.escape(nm) + r"(?![\w\-/])", masked)
        if not m:
            continue
        link = "[[%s]]" % canon if nm == canon else "[[%s|%s]]" % (canon, nm)
        lines[i] = ln[:m.start()] + link + ln[m.end():]
        done.append((canon, nm))
    if done:
        text = read_text(page.path)
        fm = FM_RE.match(text)
        head = "---\n%s\n---\n" % fm.group(1) if fm else ""
        write_text(page.path, head + "\n".join(lines))
    return done


HUB_TAG = {"Kubernetes": "k8s", "Machine Learning": "ml", "Artificial Intelligence": "ai",
           "Deep Learning": "deep-learning", "Software Architecture": "architecture",
           "Databases": "db", "Security": "security", "Containers": "container"}


def hub_gaps(pages, apply, max_gap=15):
    """Hubs list their articles under '# Articles/Talks'. Find web/paper notes that carry the hub's
    own tag but are not linked from the hub."""
    notes = [p for p in pages if p.area == "notes"]
    articles = [p for p in pages if p.area in ("articles/webs", "articles/papers")]
    total = 0
    for hub in notes:
        key = HUB_TAG.get(hub.name) or hub.name.lower().replace(" ", "-")
        if key not in hub.tags:
            continue
        linked = {l.lower() for l in hub.links()}
        missing = [q for q in articles if key in q.tags and q.name.lower() not in linked]
        if not missing:
            continue
        if len(missing) > max_gap:
            print("%s  (tag '%s')  SKIPPED: %d missing is too broad for a hub list (use --max-gap to raise)" % (
                hub.rel, key, len(missing)))
            continue
        total += len(missing)
        print("%s  (tag '%s')  missing %d" % (hub.rel, key, len(missing)))
        for q in missing:
            print("    - [[%s]]" % q.name)
        if apply:
            text = read_text(hub.path)
            bullets = "".join("- [[%s]]\n" % q.name for q in missing)
            m = re.search(r"^# Articles/Talks[^\n]*\n(\s*\n)?", text, re.M)
            if m:
                text = text[:m.end()] + bullets + text[m.end():]
            else:
                text = text.rstrip("\n") + "\n\n# Articles/Talks\n\n" + bullets
            write_text(hub.path, text)
            print("    (added to %s)" % hub.rel)
    print("\nmissing links in total: %d" % total)


def main():
    utf8_stdout()
    ap = argparse.ArgumentParser()
    ap.add_argument("--page"); ap.add_argument("--target"); ap.add_argument("--orphans", action="store_true")
    ap.add_argument("--apply", action="store_true"); ap.add_argument("--all", action="store_true")
    ap.add_argument("--max-per-page", type=int, default=3); ap.add_argument("--include-generic", action="store_true")
    ap.add_argument("--hub-gaps", action="store_true",
                    help="web/paper notes tagged with a hub's own tag that the hub does not link (add with --apply)")
    ap.add_argument("--max-gap", type=int, default=15, help="skip hubs with more missing links than this")
    ap.add_argument("--only-targets", help="comma-separated concept notes to link, e.g. 'Docker,Kubernetes'")
    ap.add_argument("--skip-targets", help="comma-separated concept notes to never link, e.g. 'API,Linux'")
    ap.add_argument("--areas", help="comma-separated source areas: notes,papers,webs (default all)")
    a = ap.parse_args()
    only = {x.strip().lower() for x in (a.only_targets or "").split(",") if x.strip()}
    skip = {x.strip().lower() for x in (a.skip_targets or "").split(",") if x.strip()}
    areas = {x.strip().lower() for x in (a.areas or "").split(",") if x.strip()}
    area_of = {"notes": "notes", "articles/papers": "papers", "articles/webs": "webs"}

    pages = iter_pages(roots=["notes", "articles"], include_index=False)
    names = targets(pages, a.include_generic)

    if a.hub_gaps:
        hub_gaps(pages, a.apply, a.max_gap)
        return

    if a.orphans:
        inbound = collections.Counter()
        for p in pages:
            for t in set(p.links()):
                inbound[t.lower()] += 1
        by_name = {p.name.lower(): p for p in pages}
        for p in pages:
            if inbound[p.name.lower()] or not p.tags:
                continue
            ptags = set(p.tags)
            cands = []
            for q in pages:
                if q is p or q.name.lower() in {l.lower() for l in p.links()}:
                    continue
                shared = ptags & set(q.tags)
                if len(shared) >= 2 or (len(shared) == 1 and len(ptags) == 1):
                    cands.append((len(shared) + (0.5 if q.area == "notes" else 0), q, shared))
            cands.sort(key=lambda x: -x[0])
            print("ORPHAN %s  tags=%s" % (p.rel, sorted(ptags)))
            for _, q, sh in cands[:4]:
                print("    related? [[%s]] (shared: %s)" % (q.name, ", ".join(sorted(sh))))
        return

    selected = pages
    if a.page:
        selected = [p for p in pages if p.name.lower() == a.page.lower()]
        if not selected:
            raise SystemExit("page not found: " + a.page)
    elif a.apply and not a.all:
        raise SystemExit("--apply needs --page NAME or --all")

    total, per_target, rows = 0, collections.Counter(), []
    for p in selected:
        if areas and area_of.get(p.area, p.area) not in areas:
            continue
        ms = find_mentions(p, names, a.include_generic)
        if a.target:
            ms = [m for m in ms if m[0].lower() == a.target.lower()]
        if only:
            ms = [m for m in ms if m[0].lower() in only]
        if skip:
            ms = [m for m in ms if m[0].lower() not in skip]
        if not ms:
            continue
        rows.append((p, ms))
        total += len(ms)
        for m in ms:
            per_target[m[0]] += 1

    if a.apply:
        changed = 0
        for p, ms in rows:
            done = apply_to_page(p, ms, a.max_per_page)
            if done:
                changed += len(done)
                print("%s: %s" % (p.rel, ", ".join(d[0] for d in done)))
        print("\nlinks added: %d" % changed)
        return

    print("pages with suggestions: %d | total suggestions: %d" % (len(rows), total))
    print("most linkable targets:", ", ".join("%s(%d)" % kv for kv in per_target.most_common(15)))
    print()
    limit = None if (a.page or a.target) else 25
    for p, ms in sorted(rows, key=lambda r: -len(r[1]))[:limit]:
        print("%s  (%d)" % (p.rel, len(ms)))
        for canon, nm, line, snip in ms[: (None if a.page else 4)]:
            print("   -> [[%s]]  line %d: ...%s" % (canon, line, snip))


if __name__ == "__main__":
    main()
