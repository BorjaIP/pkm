#!/usr/bin/env python3
"""Regenerate the two generated pages of the vault from its notes:

  wiki/catalog.md    one row per page: [[Page]] | one-line summary (TL;DR or first paragraph) | tags | created
  wiki/tag-index.md  every tag with how many notes use it

Usage (from the repository root):
  python .claude/scripts/catalog.py            # rewrite both files
  python .claude/scripts/catalog.py --check    # only report drift (exit code 1 if something is out of date)
"""
import collections
import datetime
import re
import sys
from pkmlib import VAULT, iter_pages, read_text, write_text, utf8_stdout, summary_of, get_scalar

SECTIONS = [
    ("Notes — Concepts (Zettelkasten)", lambda p: p.area == "notes", "concept notes", "concept note"),
    ("Articles — Papers", lambda p: p.area == "articles/papers", "paper summaries", "paper summary"),
    ("Articles — Webs", lambda p: p.area == "articles/webs", "web articles", "web article"),
    ("Articles — Code", lambda p: p.area == "articles/code", "code articles", "code article"),
    ("Wiki — Remembered (Agent territory)", lambda p: p.rel.startswith("wiki/remembered/"), "remembered entries", "remembered entry"),
    ("Wiki — Queries (Agent territory)", lambda p: p.rel.startswith("wiki/queries/"), "archived queries", "archived query"),
    ("Wiki — Lint Reports (Agent territory)", lambda p: p.rel.startswith("wiki/lint-reports/"), "lint reports", "lint report"),
    ("Wiki — Reference (Agent territory)", lambda p: p.rel == "wiki/tag-index.md", "reference pages", "reference page"),
]

TAIL = """## How to Update This Catalog

This file is **generated**. Regenerate it after any batch of changes (ingest, remember, query-archive, lint fixes), from the repository root:

```bash
python .claude/scripts/catalog.py          # rewrite wiki/catalog.md and wiki/tag-index.md
python .claude/scripts/catalog.py --check  # report drift only
```

- Summaries come from each page's `# TL;DR` (or its first prose paragraph), truncated to ~140 characters.
- To improve a summary, edit the page itself, not this file.
- Logs (`log.md` and `wiki/logs/`) and `wiki/catalog.md` itself are **not catalogued**.
"""

MEANING = {
    "llm": "Large language models", "gpt": "GPT family and ChatGPT-style models", "ml": "Machine learning",
    "deep-learning": "Deep learning, neural networks", "ai": "Artificial intelligence in general",
    "rag": "Retrieval-augmented generation", "retrieval": "Information retrieval and search",
    "k8s": "Kubernetes", "mlops": "ML operations: pipelines, serving, tracking",
    "ci-cd": "Continuous integration and delivery", "db": "Databases", "os": "Operating systems",
    "ssl": "TLS/SSL and certificates", "mtls": "Mutual TLS authentication", "iac": "Infrastructure as code",
    "etl": "Extract, transform, load and data pipelines",
    "privacy": "Privacy-enhancing technologies (PET), secure computation",
    "federated-learning": "Federated learning", "business-intelligence": "BI and reporting",
    "computer-science": "General computer science", "computer-architecture": "Hardware/computer architecture",
    "knowledge-graph": "Knowledge graphs", "vector-search": "Vector/ANN search and vector databases",
    "tool-use": "LLMs using tools and function calling", "agents": "AI agents", "multi-agent": "Multi-agent systems",
    "fine-tuning": "Fine-tuning and adaptation of models", "rlhf": "Reinforcement learning from human feedback",
    "embeddings": "Text/vector embeddings", "gpu": "GPU training and optimisation",
    "orchestration": "Workflow and pipeline orchestration", "serving": "Model serving",
    "observability": "Monitoring, metrics and tracing", "api-gateway": "API gateways and ingress",
    "grpc": "gRPC and protobuf", "networking": "Networking", "security": "Security", "tools": "Tools and utilities",
    "architecture": "Software and system architecture", "microservices": "Microservices architecture",
    "event-driven": "Event-driven architecture and messaging", "evaluation": "Evaluation of models and RAG systems",
    "hybrid-search": "Keyword plus vector search", "rank-fusion": "Merging ranked lists (RRF)",
    "query-expansion": "Rewriting or expanding queries", "chunking": "Splitting documents into chunks",
}


def cell(text):
    return text.replace("|", "\\|")


def link(p):
    if p.title and p.title != p.name:
        return "[[%s\\|%s]]" % (p.name, cell(p.title))
    return "[[%s]]" % p.name


def ordinal(d):
    return "th" if 10 <= d % 100 <= 20 else {1: "st", 2: "nd", 3: "rd"}.get(d % 10, "th")


def build_catalog(pages):
    old = read_text(VAULT / "wiki" / "catalog.md")
    head = old.split("\n## ", 1)[0]
    head = re.sub(r"(\n\s*---\s*)+$", "", head).rstrip() + "\n"   # separator is re-added below
    out = [head]
    total = 0
    for title, pred, plural, singular in SECTIONS:
        rows = sorted((p for p in pages if pred(p)), key=lambda p: p.name.lower())
        total += len(rows)
        out.append("---\n\n## %s\n" % title)
        out.append("| Page | Summary | Tags | Created |")
        out.append("|---|---|---|---|")
        for p in rows:
            out.append("| %s | %s | %s | %s |" % (
                link(p), cell(summary_of(p)), cell(", ".join(p.tags)), cell(p.created)))
        out.append("")
        out.append("*Total: %d %s*\n" % (len(rows), plural if len(rows) != 1 else singular))
    out.append("---\n")
    out.append(TAIL)
    return "\n".join(out), total


def build_tag_index(pages):
    rows = collections.defaultdict(collections.Counter)
    for p in pages:
        area = {"notes": "notes", "articles/papers": "papers", "articles/webs": "webs"}.get(p.area)
        if not area:
            continue
        for t in p.tags:
            rows[t][area] += 1
            rows[t]["total"] += 1
    target = VAULT / "wiki" / "tag-index.md"
    created = get_scalar(read_text(target), "created") if target.exists() else ""
    if not created:                                   # keep the original date so --check stays stable
        now = datetime.datetime.now()
        created = "%s %d%s %s" % (now.strftime("%A"), now.day, ordinal(now.day), now.strftime("%B %Y %H:%M"))
    order = sorted(rows.items(), key=lambda kv: (-kv[1]["total"], kv[0]))
    out = ["---", "title: Tag Index", "created: " + created, "aliases:", "tags:", "  - meta", "  - wiki", "---", "",
           "# Tag Index", "",
           "Generated list of every tag used in `notes/`, `articles/papers/` and `articles/webs/`, with how many "
           "notes use it. Tags are written in backticks on purpose so this page does not add tags itself. In "
           "Obsidian search use `tag:#name` (for example `tag:#k8s`).", "",
           "**%d tags**, sorted by number of notes. Rules: lowercase kebab-case, reuse an existing tag before "
           "creating one, prefix companies with `co-` and organizations with `org-`." % len(rows), "",
           "Regenerate with `python .claude/scripts/catalog.py` (it writes this page and the catalog).", "",
           "| Tag | Notes | notes/ | papers/ | webs/ | Meaning |", "|---|---:|---:|---:|---:|---|"]
    for t, c in order:
        out.append("| `%s` | %d | %d | %d | %d | %s |" % (t, c["total"], c["notes"], c["papers"], c["webs"], MEANING.get(t, "")))
    out += ["", "Prefixes: `co-*` = company (`co-openai`, `co-anthropic`, `co-microsoft`, `co-ibm`); "
            "`org-*` = organization or lab (`org-deepmind`).", ""]
    return "\n".join(out), len(rows)


def main():
    utf8_stdout()
    pages = [p for p in iter_pages() if p.rel not in ("wiki/catalog.md", "wiki/log.md")
             and not p.rel.startswith("wiki/logs/") and p.rel != "index.md"]
    tag_text, ntags = build_tag_index(pages)
    tag_path = VAULT / "wiki" / "tag-index.md"
    cat_path = VAULT / "wiki" / "catalog.md"
    # tag-index first: the catalog lists it as a row (with its summary and date)
    if "--check" in sys.argv:
        tag_ok = tag_path.exists() and read_text(tag_path) == tag_text
        pages_now = [p for p in pages]
        cat_text, total = build_catalog(pages_now)
        cat_ok = read_text(cat_path) == cat_text
        print("tag-index.md: %s | catalog.md: %s (%d pages, %d tags)" % (
            "up to date" if tag_ok else "OUT OF DATE", "up to date" if cat_ok else "OUT OF DATE", total, ntags))
        sys.exit(0 if (tag_ok and cat_ok) else 1)
    write_text(tag_path, tag_text)
    pages = [p for p in iter_pages() if p.rel not in ("wiki/catalog.md", "wiki/log.md")
             and not p.rel.startswith("wiki/logs/") and p.rel != "index.md"]
    cat_text, total = build_catalog(pages)
    write_text(cat_path, cat_text)
    print("tag-index.md written: %d tags | catalog.md written: %d pages" % (ntags, total))


if __name__ == "__main__":
    main()
