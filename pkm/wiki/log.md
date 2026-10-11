---
title: Wiki Log
created: Friday 11th April 2025 12:00
aliases:
tags:
  - meta
  - agent
  - wiki
  - log
---

# Wiki Log

**Active log.** Append-only chronological record of all wiki operations.

---

## Log Rotation Policy

This file is the **current/active** log. When it grows beyond **200 lines** or **50 KB**, it is rotated into `wiki/logs/` and a fresh `wiki/log.md` is created.

**Rotation command (for agent or manual use):**
```bash
# Check current size
wc -l wiki/log.md && du -h wiki/log.md

# If > 200 lines or > 50 KB, rotate:
DATE=$(date +"%Y-%m-%d")
mv wiki/log.md wiki/logs/${DATE}-log.md
cp templates/Agent-Log.md wiki/log.md
# Fill in the created date and update the Previous/Next log links in the rotated file
```

**Rules after rotation:**
1. The rotated file gets a back-link `[[log]]` pointing to the new active log.
2. The new `log.md` starts empty except for this header (copied from `templates/Agent-Log.md`).
3. `catalog.md` is NOT updated on rotation — logs are meta, not catalogued.
4. When reading history, the agent reads the active `log.md` first, then drills into `wiki/logs/` only if the user asks for older operations.

---

## [2025-04-11 12:00] init | Wiki system bootstrap
- Disposition: Init
- Action: Created catalog.md, log.md, and WIKI.md schema
- Scope: Full vault scan — 151 notes, 63 papers, 132 webs, 0 code
- Notes: First pass. catalog.md seeded from existing vault contents. All legacy pages marked as pre-existing.

## [2025-04-11 13:00] update | Added features from gowtham0992/link
- Disposition: Update
- Source: https://github.com/gowtham0992/link (Karpathy LLM Wiki-inspired local memory system)
- Action: Extended WIKI.md with 4 new operations/concepts:
  - `remember` operation (decisions/preferences from chat, distinct from `ingest`)
  - Query budgets (micro / standard / deep tiers)
  - Memory frontmatter (`status`, `review_after`, `expires_at`)
  - Retrieval audit (log pages read per query)
  - Raw secret scan before saving any source
- Updated: WIKI.md, log.md

## [2025-04-11 13:15] update | Wiki folder structure + log rotation
- Disposition: Update
- Action: Restructured wiki operations into dedicated `wiki/` folder:
  - `wiki/logs/` — rotated log archives
  - `wiki/remembered/` — agent-captured preferences and decisions
  - `wiki/queries/` — archived query responses
  - `wiki/lint-reports/` — lint output archives
- Added agent templates: Agent-Remember.md, Agent-Archive.md, Agent-Log.md
- Log rotation policy: rotate at > 200 lines or > 50 KB
- Frontmatter format locked to Obsidian Templater standard: `dddd Do MMMM YYYY HH:mm`
- Updated: WIKI.md, wiki/log.md, wiki/catalog.md, templates/

## [2025-04-11 13:30] update | Centralized wiki/ — moved catalog.md and log.md
- Disposition: Update
- Action: Moved `catalog.md` and `log.md` into `wiki/` folder for complete agent-territory centralization.
- All WIKI.md references updated to `wiki/catalog.md` and `wiki/log.md`.
- Updated: WIKI.md, templates/Agent-Log.md

## [2025-04-11 13:45] query | What do I know about RAG?
- Tier: standard
- Pages read: [[RAG]], [[Retrieval-Augmented Generation for Large Language Models - A Survey]], [[RAG-Fusion - a New Take on Retrieval-Augmented Generation]]
- Sources cited: articles/papers/Retrieval-Augmented Generation for Large Language Models - A Survey.md, articles/papers/RAG-Fusion - a New Take on Retrieval-Augmented Generation.md
- Answer archived: —

## [2025-04-11 13:45] remember | Prefer PostgreSQL over MySQL
- Scope: general
- Expires: none
- Page: wiki/remembered/prefer-postgresql-over-mysql.md
- Catalog updated: Yes

## [2025-04-11 13:50] lint | Weekly health check
- Fixed: 0 (no auto-fixes applied)
- Flagged: 11 broken wikilinks, 31 orphan notes
- Report: wiki/lint-reports/2025-10-11-lint.md
