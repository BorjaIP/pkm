# AGENTS.md

Rules for AI agents (Claude Code, Codex, etc.) working in this repository.

## Git: who commits what

This repo is synced across several machines (Windows, WSL and macOS). To keep formatting consistent, commits are split by scope:

- **Notes and vault structure (`pkm/`)** — notes, articles, templates, assets, folder structure and Obsidian settings (`pkm/.obsidian/`) are **ONLY committed and pushed from Obsidian** (obsidian-git plugin). Agents may edit these files when asked, but must **never** `git commit` or `git push` them.
- **Repository / publishing infrastructure** — anything outside the vault content: `quartz/`, `Dockerfile`, `docker-compose.yml`, `.devcontainer/`, `.github/`, `ci/`, `.gitignore`, `.gitattributes`, `README.md`, `CLAUDE.md`, `AGENTS.md`. Agents **may** commit and push these changes (stage only those files, never vault content).

If a change touches both scopes, commit only the infrastructure files and leave the vault changes for Obsidian.

## Line endings

`.gitattributes` forces LF (`* text=auto eol=lf`) on every machine. Do not change `core.autocrlf` or convert files to CRLF.

## CI Scope

CI in this repository covers **only the site's presentation, build and deployment**: the Quartz image and its overrides (`quartz/`), `Dockerfile`, `docker-compose.yml`, `.devcontainer/`, `.github/` and `ci/`.

CI must **never** validate, lint, rewrite or gate the Obsidian notes (`pkm/`): note content, links, frontmatter, tags, assets and vault structure are out of scope. In particular:

- Checks that run on pull requests are path-filtered to the infrastructure paths above; changes under `pkm/` must not trigger them.
- CI builds use a small fixture under `ci/` instead of the real vault, so a check never depends on note content.
- `deploy.yaml` is the only workflow that runs on note changes, and only to publish them (push to `main`).
- Do not add broken-link, spell-check, frontmatter or formatting checks for notes.
