---
title: Second Brain | Personal Knowledge Management
created: Tuesday 22nd April 2025 11:45
aliases: 
tags:
---

#  \o/ Context

I'm **Borja**, an AI Platform Engineer working across data, platform, and AI tooling. This is my **Second Brain** — a personal knowledge management system I use to think, learn, and operate.

This vault is one half of a two-repository setup. The other is **[`personal-os-skills`](https://github.com/borjairigoyen/personal-os-skills)** — a collection of skills that write directly into this vault: meeting notes, ops triage, runbooks, project tracking, and more. Together they form a personal OS: `personal-os-skills` acts as the **agentic write layer**, capturing and structuring operational knowledge automatically, while `pkm` is the **knowledge base** — the place where everything lands, connects, and gets published.

---

## How This Vault Is Organized

```
pkm/
├── notes/              Digital Garden — Zettelkasten atomic CS & tech notes
├── articles/
│   ├── papers/            Academic paper summaries (LLMs, RAG, ML, systems...)
│   └── webs/              Web article references & reading notes
├── meetings/           AI-enhanced meeting notes (private, not published)
│   ├── notes/             Structured records, linked to Zettelkasten concepts
│   └── transcriptions/    Raw transcription inputs
├── meridian/           Agentic project management — one folder per project
│   ├── prism/
│   ├── personal-os-skills/
│   ├── budget-app/
│   └── meridian/
├── ops/                Ops triage & runbooks (Datadog, k8s, incidents...)
│   ├── datadog/
│   ├── incidents/
│   ├── k8s/ & k8s-cost/
│   ├── runbooks/
│   └── sentry/
└── private/            Personal notes — never published
```

**Why this structure?** Each folder has a distinct capture mode and audience:

- `notes/` + `articles/` → **publish-worthy** knowledge, the public digital garden
- `meetings/` + `meridian/` + `ops/` → **operational** knowledge, private and AI-generated
- `private/` → personal scratch space, always excluded from the site

---

## Digital Garden — Notes & Articles

The public-facing half of this vault. Built on the **Zettelkasten** methodology: every concept lives in its own atomic note, linked to related ideas via `[[wikilinks]]`. Notes grow over time and connect across topics rather than living in isolated silos.

### Notes — Atomic Zettelkasten

Each file in `notes/` is a **single concept** — concise, linkable, and evergreen. Topics span computer science, distributed systems, AI/ML, infrastructure, and tooling. Notes are written to be useful both to future-me and to anyone reading the published site.

→ [[Computer Science]]

### Articles

References and summaries from external sources, organized by type:

- **`papers/`** — structured summaries of academic papers (mostly LLMs, RAG, ML systems)
- **`webs/`** — reading notes from blog posts, docs, and technical articles

Articles are linked back into the relevant Zettelkasten notes, so a concept note might reference the paper that introduced it.

---

##  AI-Powered Workflows — `personal-os-skills`

The `personal-os-skills` repo contains Claude Code skills that write directly into this vault. This is the **write path** — how operational and meeting knowledge enters the system without manual effort.

| Skill | What it creates here |
|---|---|
| `meet` | Structures raw meeting notes → `meetings/notes/` |
| `paper-summarizer` | Parses and summarizes papers → `articles/papers/` |
| `pkm-tool-adder` | Adds new tools/services → `notes/` |
| `datadog-*` / `k8s-*` | Triage reports and runbooks → `ops/` |
| `create-runbook` | Promotes triage notes into living runbooks → `ops/runbooks/` |
| `mdn-*` (Meridian) | Manages agentic project tasks → `meridian/<project>/` |

### Zettelkasten × Meetings

Meeting notes don't live in isolation. The `meet` skill structures them to **link back to existing Zettelkasten concepts** — so a meeting about a Kafka migration links to `[[Kafka]]`, a design discussion links to `[[Architecture Patterns]]`, and so on. Over time, meetings become a trace of *how* knowledge was applied, not just *what* was decided.

---

##  Quick Navigation

| Area | Link |
|---|---|
| CS knowledge base | [[Computer Science]] |
| Ops & triage index | [[ops/_index]] |
