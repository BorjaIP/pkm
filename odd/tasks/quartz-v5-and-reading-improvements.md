# Quartz v5 migration and reading improvements

Status: migration on hold (no stable v5 branch/image); reading improvements in progress on v4. Created 2026-10-10.

Decision 2026-10-10: do NOT migrate to v5 for now; stay on v4.5.2 and implement R1-R8 first.

## Objective

1. Move the PKM site from Quartz v4.5.2 (`sha-d25a6ea`, tip of the `v4` branch) to Quartz v5.
2. Afterwards, implement the reading improvements listed below.

Order matters: finish the migration first, then the improvements.

## Context (verified)

- v4 is frozen: the `v4` branch tip is `d25a6ea`, exactly the image already in use.
- v5 lives in the `v5` branch (tip `97a2d05` at the time of writing). Its Docker workflow pushes `ghcr.io/jackyzha0/quartz:sha-<short>` on every push to `v5`, but `sha-97a2d05` and `v5` tags were NOT found in ghcr; only `latest` exists. Which version `latest` points to is unverified.
- The v5 Dockerfile builds on `node:22-slim`, installs git (plugins are fetched from GitHub) and runs `npm install` plus `npx quartz plugin install`.

## What changes in v5

| Area | v4 (now) | v5 |
|---|---|---|
| Config | `quartz.config.ts` + `quartz.layout.ts` | `quartz.config.yaml`; `quartz.layout.ts` removed, layout position is a per-plugin property |
| Plugins | built in, `Plugin.X()` | standalone packages (`quartz-community` org), `npx quartz plugin add`, pinned in `quartz.lock.json`; 40+ official |
| Components | `Component.X()` in layout | `Plugin.X()` entries in YAML |
| Custom JS | edit files | `quartz.ts` override system |
| URLs | mixed case (`/notes/Harness-Engineering`) | lowercased and hyphenated; `AliasRedirects` creates redirects from old URLs |
| Node | 22 in current image | 22 or later required |
| CI | `docker build` + `quartz build` | needs a `quartz plugin install` step before the build (cache `~/.npm` and `.quartz/plugins` keyed on `quartz.lock.json`) |

## What it means for this repo

Our setup is "upstream image + COPY overrides" (see `Dockerfile`, `docker-compose.yml`). v5 migration assumes a full Quartz checkout, so the model itself has to change.

Items to port or replace:

- `quartz/quartz.config.ts` -> `quartz.config.yaml` (theme colors/fonts, `baseUrl`, ignorePatterns, plugin list).
- `quartz/quartz.layout.ts` -> per-plugin `layout` entries (left: PageTitle, Search/Darkmode/ReaderMode flex, Divider, RecentNotes, Explorer; right: Graph, ToC, Backlinks).
- `quartz/Breadcrumbs.tsx`, `RecentNotes.tsx`, `Divider.tsx`, `index.ts` -> check whether official plugins replace them; otherwise write local plugins.
- `quartz/lastmod.ts` (custom date parsing from frontmatter) -> check the v5 equivalent for created/modified dates; port `parseCustomDate` only if still needed.
- `quartz/custom.scss` -> check where custom styles go in v5 and whether our selectors (`.page > #quartz-body .sidebar.left`, `.explorer`, `.recent-notes`, `h2.page-title`) still match.
- `Dockerfile`, `docker-compose.yml`, `.devcontainer/*`, `.github/workflows/deploy.yaml` -> new build model plus plugin install step.

## Migration tasks (not started)

- [ ] M1 Decide the target: pin a `v5` commit (or a tag) and confirm how to build it (no matching ghcr image found). Resolve the open questions first.
- [ ] M2 Read the plugin reference table in the official migration guide and map each v4 plugin/component we use to its v5 equivalent.
- [ ] M3 Prototype in a branch: v5 checkout builds our `pkm/` content locally, default template only.
- [ ] M4 Port config (YAML), theme (colors, Inconsolata, `baseUrl: borjaip.github.io/pkm`) and layout.
- [ ] M5 Port or replace custom components and the lastmod transformer.
- [ ] M6 Port `custom.scss` (including the `hr { flex-shrink: 0 }` sidebar divider fix and the 18px base size).
- [ ] M7 Update Dockerfile, compose, devcontainer and the deploy workflow (plugin install, caching).
- [ ] M8 Verify in local: all 347 files build, sidebar, explorer, graph, search, dark mode, reader mode, links, and old URLs redirect.
- [ ] M9 Verify CI deploy on the branch before merging to `main` (first real CI build of the new setup).

## Open questions

- Is `latest` in ghcr v5? Is there an image or tag built from the `v5` branch, or do we have to build it ourselves?
- Do official v5 plugins cover Breadcrumbs, RecentNotes and Divider?
- Where do custom styles and transformers live in v5?
- Are URL changes acceptable (old mixed-case links already shared externally)?

## Reading improvements backlog (implement after the migration)

Evidence level in brackets. Site references are from the official showcase.

- [x] R1 (CSS served by local build; visual check pending) Line length and spacing: cap article width at about 70-80 characters and raise `line-height`; Inconsolata at 18px reads wide. [own recommendation, CSS only]
- [x] R2 (enabled; hover behavior not visually checked) Popovers: issue #890 was closed 2025-03-10 by commit 8d33608, which is an ancestor of the v4 tip (compare: ahead 197, behind 0). [verified]
- [ ] R3 Citations plugin for `articles/papers`. [Quartz feature list; fit with our note format unverified]
- [ ] R4 Sidenotes: no Quartz plugin found; try `<span class="sidenote">` plus custom CSS. [experiment, untested]
- [ ] R5 "Start here" landing: replace the flat list in `pkm/index.md` with a few curated entry notes, like The Pond (turntrout.com). [evidenced on that site]
- [x] R6 Already provided by Quartz (heading `a[role=anchor]` and a ToC are in the built HTML of a note; verified). Heading anchors and ToC for long notes, as in A Pattern Language (patternlanguage.cc). [evidenced on that site]
- [ ] R7 Evaluate Stacked pages, Bases, Canvas and encrypted pages from the Quartz feature list; check which exist in the chosen version. [unverified per version]
- [ ] R8 Check the code-block theme (`nord` in dark) against the new `#0a0a0a` background. [own recommendation]

## Sources

- Quartz what's new: https://quartz.jzhao.xyz/getting-started/whats-new
- Quartz migration guide: https://quartz.jzhao.xyz/getting-started/migrating
- Quartz features: https://quartz.jzhao.xyz/features/
- Quartz showcase: https://quartz.jzhao.xyz/showcase
- v5 branch Dockerfile and Docker workflow: https://github.com/jackyzha0/quartz/tree/v5
