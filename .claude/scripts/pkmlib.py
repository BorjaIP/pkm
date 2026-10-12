"""Shared helpers for the PKM vault scripts (catalog.py, lint.py, suggest_links.py).

Python 3.8+, standard library only. Layout (scripts live next to the skills):

    <repo>/.claude/scripts/pkmlib.py   <- this file
    <repo>/.claude/skills/...
    <repo>/pkm/                        <- the Obsidian vault (VAULT)

Run the scripts from the repository root, e.g. `python .claude/scripts/lint.py`.
"""
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
VAULT = REPO / "pkm" if (REPO / "pkm").is_dir() else REPO
PAGE_ROOTS = ["notes", "articles", "wiki"]          # folders that hold pages
SKIP_PARTS = {".obsidian", ".claude", ".git", "odd", "private", "templates"}

FM_RE = re.compile(r"^---\n(.*?)\n---\n?(.*)$", re.S)
LINK_RE = re.compile(r"\[\[([^\]|#\\]+)(?:#[^\]|\\]*)?(?:\\?\|[^\]]*)?\]\]")
CODE_RE = re.compile(r"```.*?```|`[^`\n]*`", re.S)
CREATED_RE = re.compile(
    r"^(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday) \d{1,2}(st|nd|rd|th) "
    r"(January|February|March|April|May|June|July|August|September|October|November|December) \d{4} \d{2}:\d{2}$"
)
ASSET_EXT = (".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".pdf", ".mp4", ".canvas", ".base")


def utf8_stdout():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


def read_text(path):
    return Path(path).read_text(encoding="utf-8")


def write_text(path, text):
    """Write with LF endings (the repo enforces LF)."""
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(text)


def _block_list(lines, key_re):
    """Values of a YAML key given inline (a, b / [a, b]) or as an indented '- x' list."""
    for i, ln in enumerate(lines):
        m = re.match(key_re, ln, re.I)
        if not m:
            continue
        vals = []
        inline = m.group(1).strip()
        if inline:
            vals += [x.strip().strip('"').strip("'") for x in inline.strip("[]").split(",") if x.strip()]
        j = i + 1
        while j < len(lines) and re.match(r"^\s+-\s*(.*)$", lines[j]):
            vals.append(re.match(r"^\s+-\s*(.*)$", lines[j]).group(1).strip().strip('"').strip("'"))
            j += 1
        return [v for v in vals if v], True
    return [], False


def get_scalar(fm, key):
    m = re.search(r"^" + key + r"\s*:[ \t]*(.*)$", fm, re.I | re.M)
    return m.group(1).strip() if m else ""


class Page:
    def __init__(self, path):
        self.path = Path(path)
        self.rel = self.path.relative_to(VAULT).as_posix()
        self.name = self.path.stem
        text = read_text(self.path)
        m = FM_RE.match(text)
        self.has_fm = bool(m)
        self.fm = m.group(1) if m else ""
        self.body = m.group(2) if m else text
        lines = self.fm.split("\n")
        self.tags, self.has_tags_key = _block_list(lines, r"^tags\s*:\s*(.*)$")
        self.tags = [t.lstrip("#") for t in self.tags]
        self.aliases, _ = _block_list(lines, r"^aliases\s*:\s*(.*)$")
        self.title = get_scalar(self.fm, "title")
        self.created = get_scalar(self.fm, "created")
        self.inline_tags = bool(re.search(r"^tags\s*:[ \t]*\S", self.fm, re.I | re.M))

    @property
    def area(self):
        parts = self.path.relative_to(VAULT).parts
        if parts[0] == "articles" and len(parts) > 2:
            return "articles/" + parts[1]
        return parts[0] if len(parts) > 1 else "root"

    def links(self):
        """Wikilink targets in the body, ignoring code blocks and file embeds."""
        text = CODE_RE.sub("", self.body) + "\n" + self.fm   # frontmatter relations also count
        out = []
        for m in LINK_RE.finditer(text):
            target = m.group(1).strip()
            if "/" in target:
                target = target.rsplit("/", 1)[1]
            if target.lower().endswith(ASSET_EXT):
                continue
            out.append(target)
        return out


def iter_pages(roots=PAGE_ROOTS, include_index=True):
    pages = []
    for root in roots:
        base = VAULT / root
        if not base.exists():
            continue
        for p in sorted(base.rglob("*.md")):
            if any(part in SKIP_PARTS for part in p.relative_to(VAULT).parts):
                continue
            pages.append(Page(p))
    idx = VAULT / "index.md"
    if include_index and idx.exists():
        pages.append(Page(idx))
    return pages


def all_note_names():
    """Every markdown stem and alias in the vault, used to resolve wikilinks."""
    names = {}
    for p in VAULT.rglob("*.md"):
        if ".obsidian" in p.parts or ".git" in p.parts:
            continue
        names.setdefault(p.stem.lower(), p.stem)
    for pg in iter_pages():
        for a in pg.aliases:
            names.setdefault(a.lower(), pg.name)
    return names


def plain(text):
    """Strip simple markdown so a sentence can sit in a table cell."""
    text = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", r"\2", text)
    text = re.sub(r"\[\[([^\]]+)\]\]", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"[*_`]", "", text)
    text = re.sub(r"<[^>]+>", "", text)
    return re.sub(r"\s+", " ", text).strip()


def cut(text, n=140):
    if len(text) <= n:
        return text
    t = text[:n].rsplit(" ", 1)[0].rstrip(",;:.-")
    return t + "..."


def summary_of(page, n=140):
    """One-line summary: the TL;DR if present, else the first prose paragraph."""
    m = re.search(r"# TL;DR\s*\n\s*\n(.+?)(?:\n\s*\n|\Z)", page.body, re.S)
    if m:
        return cut(plain(m.group(1)), n)
    for block in re.split(r"\n\s*\n", page.body):
        b = block.strip()
        if not b:
            continue
        if b.startswith(("|", "!", "#", "```", ">", "---", "<", "- ", "* ", "1.", "+")):
            continue
        t = plain(b.replace("\n", " "))
        if len(t) >= 60:
            return cut(t, n)
    if page.area == "notes":
        return "Notes and references on %s." % (page.title or page.name)
    return "(no summary)"
