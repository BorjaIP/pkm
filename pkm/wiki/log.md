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

## [2026-10-14 19:44] ingest | Hermes
- Disposition: New
- Source: https://hermes-agent.nousresearch.com/ (official docs), https://github.com/NousResearch/hermes-agent (README, AGENTS.md)
- Updated: [[Hermes]]
- Note: curated skill table pending the skill list from Borja

## [2026-10-14 19:55] update | Hermes — useful skills
- Disposition: Update
- Source: github.com/Panniantong/Agent-Reach, github.com/blader/humanizer, github.com/kepano/defuddle (1-3 of Borja's list)
- Updated: [[Hermes]]
- Note: resolved the pending skill table; catalog regenerated

## [2026-10-14 20:50] update | Raindrop "Load" collection -> 4 tools catalogued
- Disposition: Update
- Source: Raindrop collection Load (id 76095311): github.com/MakazhanAlpamys/Soup, github.com/ARahim3/DigUp, github.com/diegosouzapw/OmniRoute, github.com/wheresryan22/anatomy
- Updated: [[LLM]], [[Agent Skills]]
- Note: rows appended with pkm-tool-adder; Soup/DigUp/OmniRoute in the LLM tool table, anatomy in the Agent Skills "Design and frontend" table

## [2026-10-14 20:57] update | Raindrop "Load" emptied after cataloguing
- Disposition: Update
- Source: Raindrop bookmarks 1889819477, 1889819398, 1889819243, 1889819185 deleted (collection Load id 76095311 now empty)
- Updated: [[LLM]], [[Agent Skills]]
- Note: rows in the vault are the remaining record of these items; Raindrop Trash was not emptied and the Load collection was left in place

## [2026-10-14 22:26] update | tuxedo tool row added to [[Terminal]]
- Disposition: New
- Source: https://github.com/webstonehq/tuxedo
- Updated: [[Terminal]]
- Note: added with pkm-tool-adder; Terminal.md chosen over Tools.md because terminal TUI apps live there

## [2026-10-17 12:42] update | VoiceStudio tool row added to [[Generative AI]]
- Disposition: New
- Source: https://github.com/debpalash/VoiceStudio
- Updated: [[Generative AI]]
- Note: added with pkm-tool-adder; new "## Tools" table created under the Audio & Music Generation section (that note had no tools table; its tools were plain prose)

## [2026-10-17 18:16] update | Sim, archify and Temporal tool rows added
- Disposition: New
- Source: github.com/simstudioai/sim, github.com/tt-a1i/archify, github.com/temporalio/temporal
- Updated: [[AI Agents]], [[Agent Skills]], [[Workflow Orchestration]]
- Note: added with pkm-tool-adder; Sim in the AI Agents tools table, archify in the Agent Skills "Design and frontend" table, Temporal at the end of the Workflow Orchestration table

## [2026-10-25 12:34] remember | Vault-first query workflow
- Scope: general
- Expires: none
- Page: wiki/remembered/vault-first-query-workflow.md
- Catalog updated: Yes

## [2026-10-25 12:36] update | Public English vault and private cross-reference boundary
- Disposition: Update
- Source: Conversation with Borja; repository `.gitignore`
- Updated: wiki/remembered/vault-first-query-workflow.md
- Notes: Public notes remain in English for publication; `pkm/private/` may inform answers but must never leak into public notes, generated indexes, commits, or the site.
- Gitignore verified: `pkm/private/*`
