---
title: Herdr
created: Tuesday 3rd November 2026 12:00
aliases:
tags:
  - ai
  - agents
  - tools
  - terminal
part_of:
  - "[[AI Agents]]"
---
**Herdr** is an open-source (Apache 2.0) native application built as an agent-centric development environment for coding agents such as [[Claude#Claude Code|Claude Code]] and Codex. Its tagline is *"Made for your agents. Remade by them."*: the agent itself can change any part of the interface, and agents keep running in a backend server even if you close the window.

- Website: [herdr.dev](https://herdr.dev/)
- Source: [github.com/herdrdev](https://github.com/herdrdev) (app, `herdr-core` and Herdr TUI)
- Related: [[Terminal]] (terminal tools and multiplexers), [[AI Agents]] (agent tools and frameworks), [[Claude]] (Claude Code), [[Agent Skills]], [[Harness Engineering]], [[Dotfiles]] (plain-file config)

## Key Concepts

| Concept | Description |
| --- | --- |
| Spaces and tabs | Spaces group work per repository; tabs hold individual tasks/agents. |
| Status sidebar | Shows which agents are working, done, or waiting for input. |
| Persistent backend | Agents keep working after the window is closed. |
| Remote machines | Add machines over SSH (servers, VMs, cloud); their agents appear in the same sidebar. |
| Agent delegation | Agents can hand work to other agents and get reports back, e.g. `hc run --bg`. |
| Status protocol | Supports OSC 7501, an open protocol for agents to report their state. |
| Plain-file config | Layouts, sidebars, tabs, keybindings and themes are plain config files, editable by you or by an agent. |

## Installation

```bash
# macOS / Linux
curl -fsSL https://releases.herdr.dev/app/install.sh | sh
```

```powershell
# Windows
powershell -c "irm https://releases.herdr.dev/app/install.ps1 | iex"
```

## Building Your Own Setup

Herdr is customised with two kinds of building blocks. Both are shared as GitHub repos that an agent reads and applies; Herdr does **not** review community content, so the agent should read every file before adding it.

### Layouts

> [!info] Source
> [herdr.dev/layouts](https://herdr.dev/layouts/)

A **layout** is a whole window: what goes where and how it looks. Adding a shared layout puts it next to yours and leaves your own layout untouched.

Examples published by `herdrdev`: Board, Call, Chat, Code, Mission, Pasture, Threads.

**Sharing a layout** (no sign-up needed):

1. Ask your agent to write a `RECIPE.md` for the layout, a brief another agent could build it from.
2. Push to a public GitHub repo with the topic `herdr-layout`, using this structure:
   ```text
   layouts/<name>.json
   mods/...            # any mods the layout depends on
   RECIPE.md
   preview.png
   ```
3. It is listed under *Community* on the site within about an hour.

### Mods

> [!info] Source
> [herdr.dev/mods](https://herdr.dev/mods/)

A **mod** is a piece you add to the layout you already have, like a key prefix or a panel. Example: the *Tmux prefix* mod by `herdrdev`.

**Building and sharing a mod:**

1. Ask your agent for the recipe:
   > write a RECIPE.md for my `<name>` mod the way it describes: a brief another agent could build it from with an empty folder.
2. Push to a public GitHub repo with the topic `herdr-mod`:
   ```text
   mods/<name>/
   RECIPE.md
   preview.png
   keys.json           # optional keybinding snippet
   ```
   Do **not** include a `layouts/` folder; that is what separates a mod from a layout.
3. It shows up under *Community* within about an hour. Preview pictures are screened before they appear.

### Layout vs Mod

| | Layout | Mod |
| --- | --- | --- |
| Scope | Whole window | One piece (panel, key prefix...) |
| GitHub topic | `herdr-layout` | `herdr-mod` |
| Main file | `layouts/<name>.json` | `mods/<name>/` |
| `layouts/` folder | Required | Must not exist |
| Optional | Bundled mods | `keys.json` |
| Always included | `RECIPE.md`, `preview.png` | `RECIPE.md`, `preview.png` |

## Workflow to Build One

1. Tweak your Herdr setup (or ask your agent to) until it works.
2. Ask the agent to generate `RECIPE.md` so another agent can rebuild it from an empty folder.
3. Add `preview.png` and, for mods, an optional `keys.json`.
4. Push to a public repo and add the `herdr-layout` or `herdr-mod` topic.
5. Wait for it to appear under *Community*.

> [!warning]
> Community layouts and mods are unreviewed. Read every file before letting an agent apply them.
