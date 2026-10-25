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
| [Agent Reach](https://github.com/Panniantong/Agent-Reach) | Give your AI agent eyes to see the entire internet — one CLI, zero API fees.               | `pipx install https://github.com/Panniantong/agent-reach/archive/main.zip`, then `agent-reach install --env=auto` (read-only check) and `--system` only after you approve system changes |
| [Humanizer](https://github.com/blader/humanizer)          | Agent skill that removes signs of AI-generated writing from text.                          | `hermes skills install https://raw.githubusercontent.com/blader/humanizer/main/SKILL.md`                                                                                                 |
| [Defuddle](https://github.com/kepano/defuddle)            | Get the main content of any page as Markdown. Not an Agent Skill — a Node library and CLI. | `npm install -g defuddle`, then `defuddle parse <url> --markdown` (or wrap it in your own skill with `/learn`)                                                                           |

### How these three fit Hermes

- **Agent Reach does not write to `~/.hermes/skills/`.** Its installer registers the skill in `~/.agents/skills/`, `~/.claude/skills/`, `~/.opencode/skill/` or `~/.openclaw/skills/`. Point Hermes at the cross-tool directory it already scans, so one copy serves every agent:

  ```yaml
  skills:
    external_dirs:
      - ~/.agents/skills
  ```

- **Agent Reach is safe by default and shell-dependent.** `agent-reach install` only inspects the machine and lists missing dependencies; it installs packages and writes configuration only with `--system`. It drives its upstream tools through shell commands, so the `terminal` toolset has to be enabled in Hermes (`hermes tools`). The repository ships `SKILL.md` with Chinese-first trigger phrases and `SKILL_en.md` as the English variant. It does not wrap those tools: it selects one backend per platform and keeps a fallback ready — web, YouTube, RSS, GitHub, X/Twitter, Reddit, Bilibili, Facebook, Instagram, Xiaohongshu, LinkedIn, V2EX, Xueqiu and Xiaoyuzhou — with `agent-reach doctor` reporting which route is live. Cookies and tokens stay in `~/.agent-reach/` on your machine; the only paid piece is a proxy if you deploy on a server.
- **Humanizer is a heavy skill.** One `SKILL.md` of roughly 32 KB that `skill_view` loads whole, so invoking it costs that much context for the rest of the session. Load it deliberately, when a text is actually being rewritten. It works from Wikipedia's *Signs of AI writing*: it flags all 26 tells strongest first, drafts a rewrite, critiques its own draft and returns the final version, and on a file it edits only prose — code, data, frontmatter and link targets stay untouched. It asks rather than inventing a missing fact. Its upstream cross-agent path is `npx skills add blader/humanizer --global --agent '*'`.
- **Defuddle is a tool for skills, not a skill.** It needs Node.js and takes a URL, a file or HTML on stdin, which makes it a natural `/learn` subject or a manual fallback when `web_extract` returns clutter. It outputs HTML, Markdown (`--markdown`) or JSON (`--json`), can prepend YAML frontmatter (`--frontmatter`) and ships site-specific extractors for GitHub, Reddit, Hacker News, Medium, Substack, Twitter/X, YouTube and Wikipedia. It was built for the Obsidian Web Clipper, and its README states the project is still a work in progress.
- **Compatibility.** All three target Claude Code, Codex, OpenClaw or Cursor first. The portable part is the `SKILL.md` standard that Hermes implements through agentskills.io; the CLI-backed ones work through the terminal toolset regardless of harness. For a repository that bundles several skills, `hermes skills tap add <owner>/<repo>` adds it as a searchable source instead of installing one file.

## Hermes versus OpenClaw

Both are open-source and self-hosted, and both put messaging apps in front of a persistent agent; Hermes even ships `hermes claw migrate` for OpenClaw users. The architectural difference is where the intelligence is organised: [[OpenClaw]] is built around a central Gateway that coordinates everything, while Hermes makes the agent loop itself the core and treats platforms, tools and skills as edges around it.

---
Related: [[AI Agents]], [[Agent Skills]], [[OpenClaw]]
