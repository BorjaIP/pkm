---
title:  Hermes
created: Wednesday 14th October 2026 19:43
aliases:
  - Hermes Agent
tags:
  - ai
  - agents
part_of:
  - "[[AI Agents]]"
---
**Hermes Agent** is the open-source, self-hosted personal AI agent built by [Nous Research](https://nousresearch.com). Its defining trait is a built-in learning loop: it curates its own memory, auto-generates skills after complex tasks, improves those skills during use and searches its own past conversations. It runs the same agent core across a CLI, a messaging gateway, a TUI and an Electron desktop app, and it is extended through **plugins and skills** rather than by growing the core.

## Architecture

- **One agent core, many surfaces.** The `AIAgent` turn loop (`run_agent.py` plus `agent/turn_*.py`) is the synchronous orchestration engine; the CLI, the messaging gateway, the TUI and the desktop app are front ends over it.
- **Gateway.** A single process bridges Telegram, Discord, Slack, WhatsApp, Signal, Email and CLI, with cross-platform conversation continuity and voice-memo transcription.
- **Narrow waist, wide edges.** Every model tool is sent on every API call, so new capability arrives as a CLI command plus skill, a service-gated tool or a plugin, never as new core surface.
- **State.** SQLite session store with FTS5 full-text search (`hermes_state.py`); settings in `~/.hermes/config.yaml`, secrets only in `.env`.
- **Profiles.** Several isolated profiles can coexist (`hermes profile create`), each with its own home, config and skills.
- **Scheduling.** A built-in cron scheduler runs natural-language jobs and delivers them to any platform.
- **Delegation.** Isolated subagents with their own conversations and terminals, plus Python RPC scripts that collapse multi-step pipelines into zero-context-cost turns.
- **Terminal backends.** Local, Docker, SSH, Singularity, Modal, Daytona and Vercel Sandbox; the serverless ones hibernate when idle and wake on demand.
- **ACP.** An Agent Communication Protocol adapter lets external tools such as code editors talk to the agent.

## Installation

Linux, macOS and WSL2:

```bash
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash
```

Windows (native, PowerShell — no WSL required):

```powershell
iex (irm https://hermes-agent.nousresearch.com/install.ps1)
```

Android/Termux has its own signed APT repository with `stable` and `canary` channels. Linux, macOS and WSL2 install under `~/.hermes`; native Windows installs under `%LOCALAPPDATA%\hermes`.

## CLI

| Command | Description |
| ------- | ----------- |
| `hermes` | Interactive CLI / TUI, starts a conversation |
| `hermes setup` | Full setup wizard, configures everything at once |
| `hermes model` | Choose the LLM provider and model |
| `hermes tools` | Configure which tools are enabled |
| `hermes config set` / `hermes config get` | Set or print individual config values |
| `hermes gateway` | Start the messaging gateway (Telegram, Discord, ...) |
| `hermes skills list` | List installed skills |
| `hermes update` | Update to the latest version |
| `hermes doctor` | Diagnose any issues |
| `hermes claw migrate` | Migrate a configuration from [[OpenClaw]] |

## Models and providers

`hermes model` switches provider with no code changes and no lock-in: Nous Portal, OpenRouter, OpenAI, or a self-hosted endpoint.

## Memory and sessions

- Agent-curated memory with periodic nudges to persist knowledge.
- FTS5 session search plus LLM summarization for cross-session recall.
- [Honcho](https://github.com/plastic-labs/honcho) dialectic user modeling.
- Autonomous skill creation after complex tasks, and skills that improve while in use.

## Skills

| Skill                                                     | Description                                                                                | Install                                                                                                                                                                                  |
| --------------------------------------------------------- | ------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Agent Reach](https://github.com/Panniantong/Agent-Reach) | Give your AI agent read-only access to platform content through one CLI.               | `uv tool install 'https://github.com/Panniantong/Agent-Reach/archive/main.zip'`, then `agent-reach setup --text`; link the generated skill to the target agent and verify with `agent-reach doctor --text` |
| [Humanizer](https://github.com/blader/humanizer)          | Agent skill that removes signs of AI-generated writing from text.                          | `hermes skills install https://raw.githubusercontent.com/blader/humanizer/main/SKILL.md`                                                                                                 |
| [Defuddle](https://github.com/kepano/defuddle)            | Get the main content of any page as Markdown. Not an Agent Skill — a Node library and CLI. | `npm install -g defuddle`, then `defuddle parse <url> --markdown` (or wrap it in your own skill with `/learn`)                                                                           |
| [unbroker](https://github.com/NousResearch/hermes-agent/tree/main/optional-skills/security/unbroker) | Finds a consenting person's exposed data on people-search sites and requests deletion. Install: `hermes skills install official/security/unbroker` |

Jev-based skills (model routing, memory, compaction) are collected in [[Jev]].

### How these three fit Hermes

- **Agent Reach uses a shared cross-agent skill directory.** The current registration flow links the skill from `~/.agents/skills/` into the target agents. Point Hermes at the shared directory so one copy serves every agent:

  ```yaml
  skills:
    external_dirs:
      - ~/.agents/skills
  ```

- **Agent Reach is read-only and channel-dependent.** Check `agent-reach help` before using older installation commands: current releases expose `setup`, `skill`, `doctor` and `check`. It selects a backend per platform and keeps fallbacks where available — web, YouTube, RSS, GitHub, X/Twitter, Reddit, Bilibili, Facebook, Instagram, Xiaohongshu, LinkedIn, V2EX, Xueqiu and Xiaoyuzhou — with `agent-reach doctor --text` reporting the current state. Cookies and tokens stay local and are opt-in; the current Hermes installation has not configured any.
- **Humanizer is a heavy skill.** One `SKILL.md` of roughly 32 KB that `skill_view` loads whole, so invoking it costs that much context for the rest of the session. Load it deliberately, when a text is actually being rewritten. It works from Wikipedia's *Signs of AI writing*: it flags all 26 tells strongest first, drafts a rewrite, critiques its own draft and returns the final version, and on a file it edits only prose — code, data, frontmatter and link targets stay untouched. It asks rather than inventing a missing fact. Its upstream cross-agent path is `npx skills add blader/humanizer --global --agent '*'`.
- **Defuddle is a tool for skills, not a skill.** It needs Node.js and takes a URL, a file or HTML on stdin, which makes it a natural `/learn` subject or a manual fallback when `web_extract` returns clutter. It outputs HTML, Markdown (`--markdown`) or JSON (`--json`), can prepend YAML frontmatter (`--frontmatter`) and ships site-specific extractors for GitHub, Reddit, Hacker News, Medium, Substack, Twitter/X, YouTube and Wikipedia. It was built for the Obsidian Web Clipper, and its README states the project is still a work in progress.
- **Compatibility.** All three target Claude Code, Codex, OpenClaw or Cursor first. The portable part is the `SKILL.md` standard that Hermes implements through agentskills.io; CLI-backed skills let Hermes delegate through its terminal toolset. For a repository that bundles several skills, `hermes skills tap add <owner>/<repo>` adds it as a searchable source instead of installing one file.

### Delegate work to external coding harnesses

Hermes' Claude Code and Codex skills are orchestration instructions, not imported connectors. They teach Hermes to invoke the corresponding CLI through its terminal tool, so the harness performs the task using its own CLI session, authentication, configuration and available tools. This is distinct from selecting Claude or Codex as Hermes' model provider: model selection changes who reasons in the Hermes turn, while CLI delegation starts a separate harness process.

For example, the Claude Code skill uses `claude -p` for one-shot tasks and supports interactive sessions for multi-turn work. Avoid `--bare` when the goal is to use Claude Code's configured MCP servers, because that flag explicitly skips MCP discovery and plugin loading. The Codex skill invokes Codex CLI (`codex exec` for one-shot work); its own configuration and authentication are distinct from Hermes' provider credentials. In either case, which connected tools are available depends on the harness CLI's own session/configuration and organizational policy. A Hermes skill does not make those tools appear individually in Hermes' tool list.

This delegation path differs from configuring the harness itself as an MCP server. Hermes documents `codex mcp-server` as a Codex MCP preset, and Claude Code provides `claude mcp serve`; those expose a harness interface over MCP rather than Hermes invoking its CLI through the terminal. Cursor's CLI documentation describes MCP consumption and ACP as the client interface to Cursor CLI; it does not document the same MCP-server command in the cited material.

The harness path is not a policy bypass: retain the harness's approvals and respect the Owner's authorization requirements for underlying services. Delegate only tasks and tool use that the relevant account and organization permit.

For ticket creation, the user's preferred harness order is Claude Code, then Cursor Agent, then Codex CLI. This is a priority/fallback sequence, not round-robin: begin with Claude for each request and move on only if the harness or an authorized ticket integration is unavailable. Never switch harnesses to evade an explicit permission denial, organizational policy or required Owner approval. Verify a created ticket by reading it back before reporting success. The detailed procedure is in the `ticket-harness-routing` Hermes skill.

### Cross-session instructions and profiles

For behavior that should carry across sessions in one Hermes instance, distinguish the loaded context layers:

- `SOUL.md` is always loaded from the active `HERMES_HOME`, but it is intended for identity, voice and communication style, not detailed workflows.
- `USER.md` and `MEMORY.md` are injected from the active profile's memory at session start. Use them for stable user preferences and compact operational facts; changes become prompt context on the next session.
- Skills are reusable procedures, loaded when relevant. Keep repeatable Second Brain capture/curation steps in a skill rather than duplicating a long checklist in `SOUL.md`.
- Project context such as `AGENTS.md` is discovered from the session's working directory and applies to that project, not every session globally.

A Hermes Bot is a profile, not a shared global assistant. Profiles isolate their own `SOUL.md`, memories, skills, configuration and sessions. Therefore a preference recorded in the default profile does not automatically propagate to a Bot or another profile. To make a procedure available across profiles, install or share the skill with each profile (for example, configure a shared external skill directory where appropriate); still keep profile-specific memory and credentials separate. A dedicated Bot is useful for a distinct role or isolated context, not as the mechanism for a rule that should govern the default agent's everyday sessions.

For a general preference that future sessions should document durable outcomes in this Second Brain, keep a concise preference in the active profile's memory and the detailed workflow in a relevant skill; keep this note as the knowledge source. For this vault, follow `AGENTS.md` and `.claude/WIKI.md` rather than assuming the PKM rules are loaded in every unrelated working directory.

Sources: [Hermes context files](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files), [Hermes SOUL.md](https://hermes-agent.nousresearch.com/docs/guides/use-soul-with-hermes), [Hermes file guide](https://hermes-agent.nousresearch.com/docs/user-guide/which-file-does-what), [Hermes profiles](https://hermes-agent.nousresearch.com/docs/user-guide/profiles), [Hermes Bot Mode](https://hermes-agent.nousresearch.com/docs/user-guide/bot-mode).

Sources: [Claude Code skill in Hermes](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-claude-code), [Codex skill in Hermes](https://hermes-agent.nousresearch.com/docs/user-guide/skills/bundled/autonomous-ai-agents/autonomous-ai-agents-codex), [Hermes MCP](https://hermes-agent.nousresearch.com/docs/user-guide/features/mcp), [Claude Code MCP](https://code.claude.com/docs/en/mcp), [Codex MCP server](https://developers.openai.com/codex/mcp-server), [Cursor CLI MCP and ACP](https://cursor.com/docs/cli/mcp).

## Things to Check Out

- [Credential Pools — Hermes](https://hermes-agent.nousresearch.com/docs/user-guide/features/credential-pools)
- [Fallback Providers — Hermes](https://hermes-agent.nousresearch.com/docs/user-guide/features/fallback-providers)
- [Provider Routing — Hermes](https://hermes-agent.nousresearch.com/docs/user-guide/features/provider-routing)
- [Jev Routing — personal plugin README](https://github.com/apoapostolov/hermes-agent-awesome-plugins/blob/main/personal/hermes-jev-routing/README.md)

## Plugins

Hermes grows through **plugins and skills, not core changes**. A plugin is a directory with a `plugin.yaml` manifest plus an optional `__init__.py` (`register(ctx)`) and an optional dashboard/desktop UI; it is installed from the curated catalog (`hermes plugins search`, `hermes plugins install <name> --enable`), from a Git URL or from `owner/repo`. Two kinds matter in practice:

- **Capability plugins** add tools, hooks or middleware to the agent loop, so they cost context on every call (e.g. `advanced-delegation`, `hermes-jev`). They must be enabled in `plugins.enabled`; the dashboard never imports backend code from a plugin that is not on that allow-list.
- **Surface plugins** add UI only — a dashboard tab, a Desktop page — and declare no tools, hooks or environment variables, so they cost nothing per turn.

| Plugin | Surface | What it adds |
| ------ | ------- | ------------ |
| [Memory Wiki](https://github.com/NousResearch/hermes-official-plugins/tree/main/memory-wiki) | dashboard tab + opt-in Desktop page | Browsable session-history wiki (subject pages and daily logs derived from `state.db`) plus a read-only `MEMORY.md` / `USER.md` audit panel |

### Memory Wiki

An official Nous plugin (`hermes-memory-wiki` in the catalog, formerly the standalone `NousResearch/hermes-memory-wiki` repo) that answers "what has this agent been doing, and what does it carry into every session?" without spending a token:

- **Deterministic, not generated.** Subject pages and daily logs are derived from `state.db` rows, not written by an LLM, so they are reproducible and free to open.
- **Read-only by design.** It opens `state.db` through the public `hermes_state.SessionDB` API and only reads memory files; editing memory stays with the `memory` tool, which keeps prompt caching intact.
- **Backend routes** are mounted at `/api/plugins/memory-wiki/`: `/overview`, `/subjects?q=`, `/subjects/{slug}`, `/days` and `/days/{date}`.
- **Two halves, two machines.** The dashboard backend goes on the machine running the gateway; the native Desktop page (`desktop/plugin.js`) is installed on the client and ships disabled, so a remote-gateway user enables both separately.
- **Restart or Rescan.** Dashboard manifests are discovered at server start, so a freshly installed tab needs *Rescan* in the Plugins page (or a dashboard restart); the backend router itself is hot-mounted on the first authenticated request.

## Hermes versus OpenClaw

Both are open-source and self-hosted, and both put messaging apps in front of a persistent agent; Hermes even ships `hermes claw migrate` for OpenClaw users. The architectural difference is where the intelligence is organised: [[OpenClaw]] is built around a central Gateway that coordinates everything, while Hermes makes the agent loop itself the core and treats platforms, tools and skills as edges around it.

---
Related: [[AI Agents]], [[Agent Skills]], [[Claude]], [[MCP]], [[OpenClaw]]
