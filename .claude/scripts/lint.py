#!/usr/bin/env python3
"""Read-only health check of the vault (the 'lint' operation of WIKI.md).

Checks: broken wikilinks, orphan pages, frontmatter format, tag format, untagged pages,
web-note structure, catalog drift, expired remembered entries.

Usage:
  python .claude/scripts/lint.py            # print the report
  python .claude/scripts/lint.py --save     # also write wiki/lint-reports/YYYY-MM-DD-lint.md when long
  python .claude/scripts/lint.py --unlink-broken   # turn [[Missing]] into plain text (keeps the word)
Exit code: 0 = clean, 1 = findings.
"""
import collections
import datetime
import re
import sys
from pkmlib import (VAULT, CREATED_RE, FM_RE, iter_pages, all_note_names, read_text, write_text,
                    utf8_stdout, get_scalar)

TYPES = {"article", "tutorial", "reference", "repo", "qa"}
TAG_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")


def unlink_broken(pages, broken_by_page):
    """Replace [[Missing]] / [[Missing|Shown]] by plain text, keeping the word.
    Code blocks and spans are left alone. Returns (links changed, pages changed)."""
    links_changed = pages_changed = 0
    for p in pages:
        broken = broken_by_page.get(p.rel)
        if not broken or p.rel == "index.md":
            continue
        text = read_text(p.path)
        m = FM_RE.match(text)
        head, body = ("---\n%s\n---\n" % m.group(1), m.group(2)) if m else ("", text)
        count = 0

        def repl(mo):
            nonlocal count
            target = mo.group(1).strip()
            if target.rsplit("/", 1)[-1].lower() not in broken:
                return mo.group(0)
            shown = mo.group(2)
            count += 1
            return (shown if shown else target.rsplit("/", 1)[-1])

        pattern = re.compile(r"\[\[([^\]|#\\]+)(?:#[^\]|\\]*)?(?:\\?\|([^\]]*))?\]\]")
        pieces = re.split(r"(```.*?```|`[^`\n]*`)", body, flags=re.S)
        for i in range(0, len(pieces), 2):          # even indexes are outside code
            pieces[i] = pattern.sub(repl, pieces[i])
        if count:
            write_text(p.path, head + "".join(pieces))
            links_changed += count
            pages_changed += 1
    return links_changed, pages_changed


def main():
    utf8_stdout()
    pages = iter_pages()
    names = all_note_names()
    findings = collections.OrderedDict()

    def add(section, msg):
        findings.setdefault(section, []).append(msg)

    # generated/meta pages quote or list every page: they neither count as inbound links
    # nor are checked for broken links (a report may legitimately quote a broken link)
    META = ("wiki/catalog.md", "wiki/log.md", "wiki/tag-index.md")
    def is_meta(p):
        return p.rel in META or p.rel.startswith(("wiki/logs/", "wiki/lint-reports/"))

    inbound = collections.Counter()
    broken_by_page = collections.defaultdict(set)
    for p in pages:
        if is_meta(p):
            continue
        for target in set(p.links()):
            real = names.get(target.lower())
            if real is None:
                add("Broken wikilinks", "[[%s]] in %s" % (target, p.rel))
                broken_by_page[p.rel].add(target.lower())
            elif real != p.name:
                inbound[real.lower()] += 1

    # orphans (content pages only)
    for p in pages:
        if p.rel in ("index.md", "wiki/catalog.md", "wiki/log.md") or p.rel.startswith(("wiki/logs/", "wiki/lint-reports/")):
            continue
        if inbound[p.name.lower()] == 0:
            add("Orphan pages (no inbound wikilink)", p.rel)

    for p in pages:
        if p.rel.startswith(("wiki/logs/",)) or p.rel == "wiki/log.md":
            continue
        if not p.has_fm:
            add("Frontmatter", "%s: missing frontmatter" % p.rel)
            continue
        for key in ("title", "created", "aliases", "tags"):
            if not re.search(r"^" + key + r"\s*:", p.fm, re.I | re.M):
                add("Frontmatter", "%s: missing '%s'" % (p.rel, key))
        if p.created and not CREATED_RE.match(p.created):
            add("Frontmatter", "%s: created not in 'dddd Do MMMM YYYY HH:mm' format: %r" % (p.rel, p.created))
        if p.inline_tags:
            add("Tags", "%s: tags written inline (use a YAML list)" % p.rel)
        if not p.tags and p.rel != "index.md":
            add("Untagged pages", p.rel)
        for t in p.tags:
            if not TAG_RE.match(t):
                add("Tags", "%s: tag '%s' is not lowercase kebab-case" % (p.rel, t))
        if len(p.tags) > 6:
            add("Tags", "%s: %d tags (consider fewer)" % (p.rel, len(p.tags)))

    # web notes: structure
    for p in pages:
        if p.area != "articles/webs":
            continue
        if not re.search(r"^- https?://", p.body.lstrip("\n"), re.M):
            add("Web notes", "%s: no source URL bullet" % p.rel)
        ty = re.search(r"^- Type: (\S+)", p.body, re.M)
        if not ty or ty.group(1) not in TYPES:
            add("Web notes", "%s: missing/invalid '- Type:'" % p.rel)
        for h in ("TL;DR", "Key takeaways", "When to use"):
            if "# " + h not in p.body:
                add("Web notes", "%s: missing section '%s'" % (p.rel, h))
        if p.title and p.title != p.name:
            add("Web notes", "%s: title differs from file name (%r)" % (p.rel, p.title))

    # catalog drift
    cat = VAULT / "wiki" / "catalog.md"
    if cat.exists():
        # only real rows: lines starting with '| [[' (the header text contains example links)
        cat_links = {m.lower() for ln in read_text(cat).split("\n") if ln.startswith("| [[")
                     for m in re.findall(r"^\| \[\[([^\]|\\]+)", ln)}
        for p in pages:
            if p.rel in ("wiki/catalog.md", "wiki/log.md", "index.md") or p.rel.startswith("wiki/logs/"):
                continue
            if p.name.lower() not in cat_links:
                add("Catalog drift", "not in catalog: %s" % p.rel)
        known = {p.name.lower() for p in pages}
        for l in sorted(cat_links):
            if l not in known:
                add("Catalog drift", "catalog row without a file: [[%s]]" % l)

    # remembered entries
    today = datetime.date.today().isoformat()
    for p in pages:
        if p.rel.startswith("wiki/remembered/"):
            for key in ("expires_at", "review_after"):
                v = get_scalar(p.fm, key)
                if v and v <= today:
                    add("Remembered entries due", "%s: %s %s" % (p.rel, key, v))

    if "--unlink-broken" in sys.argv:
        fixed = unlink_broken(pages, broken_by_page)
        print("Broken links turned into plain text: %d in %d pages (index.md is never touched)\n" % fixed)

    lines = ["# Lint Report — %s" % today, "",
             "Pages checked: %d" % len(pages), ""]
    if not findings:
        lines.append("No findings.")
    for section, items in findings.items():
        lines.append("## %s (%d)" % (section, len(items)))
        lines.append("")
        lines += ["- " + i for i in items[:60]]
        if len(items) > 60:
            lines.append("- ... and %d more" % (len(items) - 60))
        lines.append("")
    report = "\n".join(lines)
    print(report)

    if "--save" in sys.argv and len(lines) > 20:
        now = datetime.datetime.now()
        d = now.day
        suf = "th" if 10 <= d % 100 <= 20 else {1: "st", 2: "nd", 3: "rd"}.get(d % 10, "th")
        created = "%s %d%s %s" % (now.strftime("%A"), d, suf, now.strftime("%B %Y %H:%M"))
        fm = "---\ntitle: Lint Report — %s\ncreated: %s\naliases:\ntags:\n  - lint\n  - agent\n  - wiki\n---\n\n" % (today, created)
        write_text(VAULT / "wiki" / "lint-reports" / ("%s-lint.md" % today), fm + report + "\n")
        print("saved wiki/lint-reports/%s-lint.md" % today)
    sys.exit(1 if findings else 0)


if __name__ == "__main__":
    main()
