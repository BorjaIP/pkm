---
title: Vault-First Query Workflow
created: Sunday 25th October 2026 12:34
aliases:
  - Second Brain query workflow
tags:
  - remembered
  - agent
  - wiki
  - workflow
status: active
source: remembered
scope: general
---

> **Status: active** | Source: remembered | Scope: general
> Captured by agent on Sunday 25th October 2026 from conversation.

# Summary

For technical questions, consult Borja's Second Brain before web search or general knowledge, and make the retrieval process transparent.

# Context

Use the repository's documented wiki workflow: read `pkm/wiki/catalog.md` first, identify matching topics and synonyms, open a topic digest when one exists, search the relevant vault text, and read the selected notes. The public vault content under `pkm/` is written in English because it is published as a website; communicate with Borja in Spanish. A future or existing `pkm/private/` area is private, may be read when relevant, and may be cross-referenced with public notes, but private content must never be copied into public notes, `wiki/`, generated catalogues, commits, or the published site. Answer with citations to the relevant note paths or wikilinks. Use external sources only when the vault has no relevant material or Borja explicitly asks for current/external information. Log the query audit in `pkm/wiki/log.md` with the tier and pages actually read.

The repository `.gitignore` excludes `pkm/private/*`; verify that protection before storing sensitive material and never weaken it casually.

Do not attempt to load the entire repository into chat memory. Treat the catalog and topic digests as the working index, then retrieve only relevant notes. Keep durable workflow rules in the wiki and compact global preferences in persistent memory.

For new external knowledge, follow `.claude/WIKI.md`: security-scan source text, triage as New/Update/Disputed/No material, create or update the appropriate note, cross-link only existing pages, regenerate the catalog, and append the operation to the log. Do not commit or push vault changes manually.

# Related

- [[Homelab]]
- [[Proxmox]]
- [[Docker]]
- [[Prometheus]]
