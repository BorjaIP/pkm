# CI checks for presentation, build and deploy

Status: in progress. Created 2026-10-10. Branch `ci/quartz-checks`, stacked on `feat/reading-improvements` (PR #3 still open).

## Objective

Add a robust CI for changes to the site's presentation, build and deployment. Never for the Obsidian notes (`pkm/`): see "CI Scope" in `AGENTS.md`.

## Scope

In: `quartz/`, `Dockerfile`, `docker-compose.yml`, `.devcontainer/`, `.github/`, `ci/`.
Out: note content, links, frontmatter, tags, assets, vault structure. Out of this change: the post-deploy smoke test (explicitly excluded by the user).

## Cost

Repository is public: GitHub-hosted standard runners are free. Existing deploys take about 2 minutes each.

## Design decisions

- PR checks are path-filtered to the in-scope paths, so note changes never trigger them. `deploy.yaml` still runs on every push to `main` (it publishes notes).
- CI builds use a fixture (`ci/fixture/`), mounted over the image's content, so no check depends on the real vault. The Docker build still copies `pkm/` as the Dockerfile does; it is never read by a check.
- Custom `tsc --noEmit` runs on the overrides inside the built image. Upstream `prettier --check` and `npm test` are not used: they validate Quartz itself, and our overrides use a different indentation.
- Actions are pinned by commit SHA with a version comment; Dependabot keeps them updated. Docker base image bumps stay manual (Quartz uses `sha-...` tags, not versions).
- Branch protection is NOT enabled: Obsidian backups and direct commits push to `main`, so requiring PRs would block them.

## Tasks

- [x] C1 Move all guidance from `CLAUDE.md` to `AGENTS.md`; `CLAUDE.md` imports it (`@AGENTS.md`). Route: inline (mechanical, two small files).
- [x] C2 Fix the 5 `tsc` unused-variable errors in `Divider.tsx`, `RecentNotes.tsx`, `lastmod.ts`. Route: inline (understood, tiny edits).
- [x] C3 Resolve and record commit SHAs for the actions used. Route: inline (`gh api` lookups).
- [x] C4 CI bundle: `ci/fixture/`, `ci/check-output.sh`, `.github/workflows/ci.yaml`, `.github/dependabot.yml`, pin actions in `deploy.yaml`. Route: delegated writer (2+ non-trivial files).
- [x] C5 Local verification: image build, fixture build, check script RED then GREEN, `tsc`, `actionlint`. Route: inline.
- [x] C6 Push, open the PR, and confirm the workflow runs green on GitHub. Route: inline.

## Testing mode

No test runner exists in this repo. `ci/check-output.sh` is the test: observe RED against an empty output directory before GREEN against a real build.

## Evidence

- C1: `CLAUDE.md` renamed to `AGENTS.md` (history kept); new `CLAUDE.md` is `@AGENTS.md`. Commit 5dfdc4a.
- C2: `tsc --noEmit` went from 5 TS6133 errors (exit 1) to exit 0 after removing the unused variables. Commit a0f790f. Note: single-file bind mounts keep the old inode after an edit, so the local container must be restarted to see edited files.
- C3: SHAs resolved with `gh api` (checkout v4.4.0, setup-buildx v3.12.0, build-push v5.4.0, upload-pages-artifact v3.0.1, deploy-pages v4.0.5).
- C4: delegated writer produced fixture, `ci/check-output.sh`, `ci.yaml`, `dependabot.yml`, pinned `deploy.yaml`. One deviation: the fixture build writes to `/out/site` because Quartz cannot remove a bind-mounted `/out` (EBUSY).
- C5 (parent re-ran everything): RED on an empty dir: exit 1, 13 FAIL. GREEN on a fixture build: exit 0, 16 PASS. `tsc --noEmit` in the built image: exit 0. `actionlint 1.7.7`: exit 0. Mutation (`openLinksInNewTab: false`): the external-link check FAILs. Run on GitHub verified in C6.
- C6: PR #4 (base `feat/reading-improvements`). First run on GitHub (run 38049653755, event `pull_request`): conclusion success; `Build site` passed in 59s and `Lint workflows` in 10s, with the SHA-pinned actions and the gha cache. Annotation (non-blocking): `actions/checkout@v4.4.0` targets Node.js 20, which GitHub already forces onto Node 24; Dependabot should propose the next major. Still unverified: the pinned `deploy.yaml`, which only runs on merge to `main`.
