---
title:  Obsidian
created: Wednesday 23rd April 2025 22:30
aliases: 
tags:
  - tools
---

# Commands

```bash
# Open Developer Tools
Ctrl + Shift + I
```
# Projects

inspiration for create plugins in obsidian

- https://phibr0.medium.com/how-to-create-your-own-obsidian-plugin-53f2d5d44046
- https://github.com/irbull/obsidian-ai-summary
- https://github.com/RavenWits/obsidian-ai-summarize
- https://github.com/HyeonseoNam/auto-classifier
- https://github.com/CtrlAltFocus/obsidian-plugin-auto-tag

## Tools & Templates

| Tool | Description |
| ---- | ----------- |
| [Obsidian Mind](https://github.com/breferrari/obsidian-mind) | Obsidian vault template enabling Claude Code to maintain continuous context across sessions with automatic note organization and semantic links |
| [claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | Claude Code plugin and Agent Skills that turn captured sources into a linked, cited Obsidian wiki (Karpathy LLM Wiki pattern). 15 skills, read-only helper agents, and writes checked against a SHA-256 of each note with a journal for rollback. `claude plugin marketplace add AgriciDaniel/claude-obsidian` |
| [obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain) | Persistent agent memory kept as plain Markdown in the vault, with builds for Claude Code, Codex, Hermes and others. 48 commands, a freshness rule for stored facts (OKM), optional semantic search, scheduled agents, and Crew, a shared one-line-per-job logbook. For Hermes use the skills build; do not run `hermes plugins install` on the repo URL |
| [second-brain-starter](https://github.com/coleam00/second-brain-starter) | Claude Code skill that turns a requirements template into a nine-phase plan for a proactive personal assistant: memory files, session hooks, hybrid keyword and vector search, a heartbeat, and four proactivity levels. A planning aid rather than an implementation |
| [obsidian-skills](https://github.com/kepano/obsidian-skills) | Reference skills by Obsidian's CEO for Obsidian Markdown, Bases, JSON Canvas, the CLI and Defuddle. Listed in [[Agent Skills]] |

## Second Brain patterns worth borrowing

Ideas collected from the projects above that apply to any vault an AI agent also writes to. Treat each as a candidate to test, not a feature to switch on.

- **Plain files first.** Every project keeps the vault as ordinary Markdown, so any process can read it; Obsidian is the viewer and editor. Only the official CLI needs a running Obsidian.
- **Write only if the note is unchanged.** Record a hash of each note when it is read and refuse the write if it changed meanwhile, so a replicated edit from another device is never overwritten.
- **Timeless, dated, or a pointer.** Slow-changing knowledge is stored as is; counts, versions and statuses carry an `as of` date or link to where they live, so they do not quietly go stale.
- **Measure retrieval.** Keep a list of real questions with the note that should answer each, and track recall@k before adding embeddings or a vector index.
- **Lessons need a human yes.** A shared log of agent jobs is fine, but a lesson becomes a standing rule only after the owner keeps it.
- **Say how much initiative the agent has.** Observer, advisor, assistant and partner is a useful shared vocabulary for deciding what may run unattended.
- **Keep a fixed-size identity file.** A tiny always-loaded set of facts (timezone, role, preferences) is cheaper than rediscovering them each session.
- **One writer per territory.** When several agents and a person edit the same folder, give each area a single owner.

Related: [[Agent Skills]], [[AI Agents]], [[Claude]], [[Hermes]], [[Knowledge Graph]]
