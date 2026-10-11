# AGENTS.md

Rules for AI agents (Claude Code, Codex, etc.) working in this repository.

## Scope separation

This repository has **two instruction files** with different purposes:

| File | Scope | When to read |
|---|---|---|
| **`AGENTS.md`** (this file) | Repository infrastructure, Git rules, publishing pipeline, Docker/Quartz. | When asked to modify `quartz/`, `Dockerfile`, GitHub Actions, `.devcontainer/`, or when committing/pushing infrastructure files. |
| **`pkm/.claude/WIKI.md`** | Second Brain knowledge operations — ingest, query, lint, catalog, log, cross-references. | When asked about *knowledge in the vault* — "what do I know about X?", "ingest this paper", "compare A and B from my notes", "lint my wiki", etc. |

**`AGENTS.md` stays for infrastructure and Git discipline.**  
**`WIKI.md` is the schema that turns the agent into a disciplined wiki maintainer rather than a generic chatbot.**

---

## Git: who commits what

This repo is synced across several machines (Windows, WSL and macOS). To keep formatting consistent, commits are split by scope:

- **Notes and vault structure (`pkm/`)** — notes, articles, templates, assets, folder structure and Obsidian settings (`pkm/.obsidian/`) are **ONLY committed and pushed from Obsidian** (obsidian-git plugin). Agents may edit these files when asked, but must **never** `git commit` or `git push` them.
- **Repository / publishing infrastructure** — anything outside the vault content: `quartz/`, `Dockerfile`, `docker-compose.yml`, `.devcontainer/`, `.github/`, `.gitignore`, `.gitattributes`, `README.md`, `CLAUDE.md`, `AGENTS.md`. Agents **may** commit and push these changes (stage only those files, never vault content).

If a change touches both scopes, commit only the infrastructure files and leave the vault changes for Obsidian.

## Line endings

`.gitattributes` forces LF (`* text=auto eol=lf`) on every machine. Do not change `core.autocrlf` or convert files to CRLF.
