# AGENTS.md

Rules and project guidance for AI agents (Claude Code, Codex, etc.) working in this repository. `CLAUDE.md` imports this file, so keep all guidance here.

## Scope separation

This repository has **two instruction files** with different purposes:

| File | Scope | When to read |
|---|---|---|
| **`AGENTS.md`** (this file) | Repository infrastructure, Git rules, publishing pipeline, Docker/Quartz. | When asked to modify `quartz/`, `Dockerfile`, GitHub Actions, `.devcontainer/`, or when committing/pushing infrastructure files. |
| **`.claude/WIKI.md`** | Second Brain knowledge operations — ingest, query, lint, catalog, log, cross-references. | When asked about *knowledge in the vault* — "what do I know about X?", "ingest this paper", "compare A and B from my notes", "lint my wiki", etc. |

**`AGENTS.md` stays for infrastructure and Git discipline.**  
**`WIKI.md` is the schema that turns the agent into a disciplined wiki maintainer rather than a generic chatbot.**

### Vault first

For any technical question the vault may cover (Kubernetes, MLOps, RAG, AWS, architecture, tools, papers...), **check the vault before web search or general knowledge**: read `pkm/wiki/catalog.md` (one line and tags per page), then the matching topic digest in `pkm/wiki/queries/state-of-*.md` and the cited notes. Follow the source URL on a note when you need evidence. Go outside the vault only when it has nothing relevant or the user asks for fresh information. Details are in `.claude/WIKI.md`.

Vault maintenance scripts (Python 3, standard library only) live in `.claude/scripts/` (next to `.claude/skills/`): `lint.py` (health check), `catalog.py` (regenerates `wiki/catalog.md` and `wiki/tag-index.md`) and `suggest_links.py` (proposes new wikilinks). Run them from the repository root. They are meant to be triggered by the user through the `pkm-lint` and `pkm-link-enricher` skills; do not schedule them.

---

## Git: who commits what

This repo is synced across several machines (Windows, WSL and macOS). To keep formatting consistent, commits are split by scope:

- **Notes and vault structure (`pkm/`)** — notes, articles, templates, assets, folder structure and Obsidian settings (`pkm/.obsidian/`) are **ONLY committed and pushed from Obsidian** (obsidian-git plugin). Agents may edit these files when asked, but must **never** `git commit` or `git push` them. **Exception: Lilith** commits vault changes only through `pkm-sync.sh` (see the Lilith section); no other agent does.
- **Repository / publishing infrastructure** — anything outside the vault content: `quartz/`, `Dockerfile`, `docker-compose.yml`, `.devcontainer/`, `.github/`, `ci/`, `.gitignore`, `.gitattributes`, `README.md`, `CLAUDE.md`, `AGENTS.md`. Agents **may** commit and push these changes (stage only those files, never vault content).

If a change touches both scopes, commit only the infrastructure files and leave the vault changes for Obsidian.

## Line endings

`.gitattributes` forces LF (`* text=auto eol=lf`) on every machine. Do not change `core.autocrlf` or convert files to CRLF.

## What This Repository Is

A Personal Knowledge Management (PKM) system ("Second Brain") built on the Zettelkasten methodology. Notes are written in Obsidian and published as a static website via [Quartz v4](https://quartz.jzhao.xyz/).

**Content lives in `pkm/`** (the Obsidian vault). **Publishing infrastructure lives alongside it**: `quartz/` for Quartz customizations, `Dockerfile`, `.github/workflows/deploy.yaml`, and `.devcontainer/`.

## Lilith (Hermes) on the home server

Lilith is Borja's personal assistant: Hermes Agent running on the home-server VM `lilith`, used from Telegram. Her working directory is `/home/bis/pkm`, a clone of this repository, so this file is loaded automatically at the start of each session. For her, the **PKM and the Second Brain are the same thing**: this vault.

How to use it:

- Knowledge questions: vault first (`pkm/wiki/catalog.md`, then the matching topic digest, then the notes) and cite the note path. See "Vault first" above.
- Wiki operations (ingest, remember, query, lint, links): follow `.claude/WIKI.md`.
- Notes are written in English (see "Note Format"). Talk to Borja in Spanish.
- `pkm/private/` is never in Git. Content that arrives from Apple Notes or Reminders is not part of this repository.

What she may do:

- Create and edit notes under `pkm/`, using the templates and the territories described in `.claude/WIKI.md`.
- She does **not** run `git commit` or `git push` by hand. A systemd timer (`pkm-sync.timer`, every 15 minutes) runs `~/.local/bin/pkm-sync.sh`, which commits changes made under `pkm/` as `lilith: vault backup: YYYY-MM-DD HH:MM:SS` (Git author `lilith`), rebases onto `origin/main` and pushes straight to `main`. To publish right away, run `~/.local/bin/pkm-sync.sh`.
- Check the sync with `systemctl --user status pkm-sync.service` and `journalctl --user -u pkm-sync.service -n 20`.

What she must not do:

- A push to `main` publishes the public website (`deploy.yaml`) and the repository is public. Never write secrets, tokens, personal or private data into the vault. The script blocks obvious secrets, but it is the last guard, not the first.
- Do not edit infrastructure (`quartz/`, `.github/`, `Dockerfile`, `.claude/`, `AGENTS.md`) unless Borja asks. The script only commits `pkm/`.
- If the sync fails (rebase conflict, rejected push, possible secret), tell Borja and stop. Never force-push, `git reset --hard` or rewrite history.

## Development Commands

```bash
# Local dev with live reload (run from repo root inside the devcontainer or with Quartz installed)
npx quartz build --serve --watch --concurrency 10

# Docker build and serve (port 8080)
docker build -t quartz .
docker run --rm --name quartz -p 8080:8080 quartz:latest
```

The DevContainer (`.devcontainer/devcontainer.json`) uses `ghcr.io/jackyzha0/quartz` and forwards ports 8080 and 3001.

## Repository Structure

```
pkm/                     # Obsidian vault (the actual notes)
  notes/                 # ~149 tech/CS notes (Zettelkasten atoms)
  articles/
    papers/              # Academic paper summaries (LLMs, RAG, ML)
    webs/                # Web article references
    code/                # Code-related articles
  templates/             # Obsidian Templater templates (Note.md, Paper.md, Web.md)
  assets/                # Images and attachments
  index.md               # Vault homepage
  .obsidian/             # Obsidian config (plugins, hotkeys, appearance)
quartz/                  # Quartz customizations (config, layout, components, styles)
  quartz.config.ts       # Main Quartz config (plugins, theme, ignorePatterns)
  quartz.layout.ts       # Page layout
  custom.scss            # Custom styles
  *.tsx / *.ts           # Custom Quartz components (Breadcrumbs, RecentNotes, etc.)
.github/workflows/       # deploy.yaml → builds and deploys to GitHub Pages on push to main
                         # ci.yaml → checks on pull requests (presentation, build, deploy infra only)
.github/dependabot.yml   # keeps GitHub Actions pinned by SHA and up to date
ci/                      # CI-only: fixture content (fixture/) and output checks (check-output.sh)
odd/                     # Local agent working notes (git-ignored): never commit or push
Dockerfile               # Multi-stage: copies pkm/ → content/, runs quartz build --serve
```

## Note Format

All notes use YAML frontmatter generated by Obsidian Templater:

```yaml
---
title: Note Title
created: <date>
aliases:
tags:
---
```

- Notes **must be written in English**.
- The `draft: true` frontmatter key excludes a note from the published site (`RemoveDrafts` plugin).
- Links use Obsidian's `[[shortest path]]` resolution (`CrawlLinks` with `markdownLinkResolution: "shortest"`).
- The `private/` folder and `**/templates` are excluded from the published output (`ignorePatterns` in `quartz.config.ts`).

## Publishing Pipeline

Push to `main` → GitHub Actions (`deploy.yaml`) → Docker build → `npx quartz build` → GitHub Pages.

The Quartz config (`quartz/quartz.config.ts`) controls which plugins run, the theme, and what gets excluded. Custom components in `quartz/` override Quartz defaults and are copied into the container at build time (see `Dockerfile`).

## CI Scope

CI in this repository covers **only the site's presentation, build and deployment**: the Quartz image and its overrides (`quartz/`), `Dockerfile`, `docker-compose.yml`, `.devcontainer/`, `.github/` and `ci/`.

CI must **never** validate, lint, rewrite or gate the Obsidian notes (`pkm/`): note content, links, frontmatter, tags, assets and vault structure are out of scope. In particular:

- Checks that run on pull requests ignore notes (`paths-ignore: pkm/**`): a PR that only changes `pkm/` does not trigger them. Notes are pushed straight to `main` from Obsidian, not through PRs. A PR that mixes notes and infrastructure does run the checks, which build a fixture and never read the notes.
- CI builds use a small fixture under `ci/` instead of the real vault, so a check never depends on note content.
- `deploy.yaml` is the only workflow that runs on note changes, and only to publish them (push to `main`).
- Do not add broken-link, spell-check, frontmatter or formatting checks for notes.
