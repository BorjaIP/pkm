---
title:  Claude
created: Saturday 31st January 2026 23:47
aliases:
tags:
---
Claude is Anthropic's AI assistant family, available as a web/desktop chat app ([[Claude#Claude Desktop|Claude Desktop]]) and a terminal-based agentic coding tool ([[Claude#Claude Code|Claude Code]]). Models range from the fast [[Haiku]] to the balanced [[Sonnet]] and the most capable [[Opus]], each optimized for different cost/performance trade-offs.
# Claude Code

## Ecosystem

### Plugins & Extensions

| Tool                                                                         | Description                                                                                                                                                                                                   |
| ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [ccusage](https://github.com/ryoppippi/ccusage)                              | CLI tool for analyzing Claude Code usage from local JSONL files.                                                                                                                                              |
| [claude-mem](https://github.com/thedotmack/claude-mem)                       | Plugin that automatically captures everything Claude does during coding sessions and compresses it with AI.                                                                                                   |
| [claude-hud](https://github.com/jarrodwatts/claude-hud)                      | Plugin that shows in the terminal statusline: context usage, rate limits, tool activity, task progress, git status, and active agents. Updates every ~300ms.                                                  |
| [ralph](https://github.com/snarktank/ralph)                                  | Autonomous AI agent loop that runs repeatedly until all PRD items are complete.                                                                                                                               |
| [Understand-Anything](https://github.com/Lum1104/Understand-Anything)        | Plugin that turns any codebase into an interactive, queryable knowledge graph.                                                                                                                                |
| [HolyClaude](https://github.com/CoderLuii/HolyClaude)                        | Containerized AI development workstation: Claude Code + web UI (CloudCLI) + headless Chromium + 5 AI CLIs + 50+ dev tools in a single Docker image. Supports AMD64/ARM64.                                     |
| [everything-claude-code](https://github.com/affaan-m/everything-claude-code) | Anthropic hackathon winner. Performance optimization system: 28 agents, 50+ skills, 25+ slash commands, hooks, language rules, and MCP configs. Built from 10+ months of daily use.                           |
| [claudian](https://github.com/YishenTu/claudian)                             | Obsidian plugin that integrates Claude Code directly into your vault. Supports agentic file ops, bash commands, inline editing with diff previews, slash commands, skills/subagents, vision, and MCP servers. |
| [notebooklm-ai-plugin](https://github.com/proyecto26/notebooklm-ai-plugin)  | Claude Code skill that brings Google NotebookLM into the terminal: chat with notebook AI, generate 9 artifact types (slides, audio, video, mind maps, quizzes, flashcards, infographics, reports, data tables), manage sources (URLs, YouTube, files, text), and run fast/deep web research. |
### Skills & Collections

| Resource | Description |
| -------- | ----------- |
| [anthropics/skills](https://github.com/anthropics/skills) | Official Anthropic repository of Agent Skills — self-contained skill folders Claude loads dynamically for specialized tasks. |
| [obsidian-skills](https://github.com/kepano/obsidian-skills) | Agent skills (by Obsidian's CEO) for Claude Code to read, write, and navigate Obsidian vaults. |
| [impeccable](https://github.com/pbakaus/impeccable) | Design skill system for AI coding assistants; teaches typography, color, and UX anti-patterns via 20+ slash commands. |
| [awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents) | A collection of 100+ specialized Claude Code subagents covering a wide range of development use cases. |
| [awesome-claude-agents](https://github.com/vijaythecoder/awesome-claude-agents) | An orchestrated sub-agent dev team powered by Claude Code. |
| [claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | Comprehensive guide to Claude Code best practices: subagents, commands, skills, memory systems, and MCP servers. |
| [marketingskills](https://github.com/coreyhaines31/marketingskills) | 40+ marketing skills for Claude Code and other AI coding agents: conversion optimization, copywriting, SEO, paid ads, analytics, A/B testing, retention, and growth engineering. |

---

## Commands

### Slash Commands

| Command | Description |
| ------- | ----------- |
| `/clear` | Clears the conversation history and resets the context window, starting fresh without losing your work. Aliases: `/reset`, `/new`. |
| `/compact` | Summarizes the current conversation into a compressed context to free up token space while preserving key information. |
| `/context` | Displays the current context window usage as a colored grid. Shows optimization suggestions for context-heavy tools, memory bloat, and capacity warnings. |
| `/reload-plugins` | Reloads all installed plugins without restarting Claude Code. |
| `/plugin` | Lists installed plugins and manages plugin lifecycle (install, remove, enable, disable). |
| `/feedback` | Sends the full conversation history to Anthropic (encrypted). Optionally creates a public GitHub issue. |
| `/rename [name]` | Rename the current session and show the name on the prompt bar. Without a name, auto-generates one from conversation history. Pairs with `claude -n` / `claude --resume <name>`. |
| `/resume [session]` | Resume a conversation by ID or name, or open an interactive session picker. Alias: `/continue`. |
| `/rewind` | Rewind the conversation and/or code to a previous point, or summarize from a selected message. Alias: `/checkpoint`. |
| `/branch [name]` | Create a named branch of the current conversation at this point, to explore a different path. Alias: `/fork`. |
| `/export [filename]` | Export the current conversation as plain text. Without a filename, opens a dialog to copy to clipboard or save to a file. |
| `/btw <question>` | Ask a quick side question without adding to the conversation history. Runs even while Claude is working; ephemeral and answer never enters the context. |
| `/diff` | Open an interactive diff viewer showing uncommitted changes and per-turn diffs. Use arrow keys to switch between git diff and individual Claude turns. |
| `/cost` | Show token usage statistics for the current session. |
| `/stats` | Visualize daily usage, session history, streaks, and model preferences. |
| `/effort [low\|medium\|high\|max\|auto]` | Set model effort level. `low`/`medium`/`high` persist across sessions; `max` is session-only (Opus 4.6). `auto` resets to model default. |

```bash
# Start a named session (resumable by name)
claude -n "my-feature-work"

# Resume a session by name or ID
claude --resume my-feature-work

# Fork a session on resume (new ID, preserves original)
claude --resume my-feature-work --fork-session
```

### Statusline

Mix `/statusline` with [ccusage](https://github.com/ryoppippi/ccusage) to get real context usage visible in your statusline at all times.

**Context thresholds — personal rules:**

| Usage | Action |
| ----- | ------ |
| > 60% | Start thinking about summarization |
| > 80% | Compact manually using the [[Claude#Context Management\|Context Management]] technique below |

---

### Context Management

Instead of using `/compact` (which lets Claude decide what to keep), take manual control of the context by externalizing it to a Markdown file.

**Step 1 — Summarize into a file.** When the context is getting full, ask:

```
Let's summarize where we are. What have we accomplished, what's the current state, and what are our next steps? Put this in progress.md
```

**Step 2 — Clear the context.**

```
/clear
```

**Step 3 — Resume with full context.**

```
Let us continue our work @progress.md
```

> You now have full control over the context: it lives in a versioned `.md` file, survives `/clear`, and you decide when to roll it over.

### Guided Compaction

`/compact` accepts a free-text instruction telling it what to **keep in detail** and what to **summarize briefly**. This beats blind auto-compact, which treats everything equally.

```
/compact Focus on preserving our authentication refactoring discussion in detail.
The database work is complete — summarize it briefly.
```

> What matters most is preserved verbatim; finished work shrinks to a few lines.

---

### Context References

Use `@` to inject file or folder context explicitly — this avoids broad repo searches and keeps token usage low.

| Syntax | Result |
| ------ | ------ |
| `@path/to/file.md` | Injects the full content of that specific file |
| `@path/to/folder/` | Injects a **directory listing** (filenames only, not content) |

> Prefer `@folder/` over `@folder` when you only need to know what files exist. Reserve full file injection for when you actually need the content.

```
# Example: reference a specific file
Fix the bug described in @docs/known-issues.md

# Example: list available files in a folder, not their content
Pick the right migration script from @db/migrations/
```

---

### Subagent Context Isolation

Each subagent gets its own **fresh context window** — it does the deep work, returns a summary, and the main context stays clean.

Use an `Explore` subagent for research-heavy phases so the main agent never accumulates the cost of reading many files:

```
Use the Explore subagent to analyze the Authentication module in depth.
Return a summary of how it works.
```

Parallelize across multiple files or topics by spawning one subagent per item:

```
Let's review our roadmap items.
This task will require reading many files. Use a subagent for the research phase —
one for each roadmap idea in @roadmap_ideas/
```

**When to reach for this pattern:**
- Exploring a large module or unfamiliar codebase section
- Processing many files in parallel (one subagent per file/topic)
- Any research phase before writing code — offload it, get the summary, then act

---

## Plugins

### Install anthropics/skills

```bash
# Add the official Anthropic skills marketplace
/plugin marketplace add anthropics/skills
```

### Install Understand-Anything

```bash
# Install the plugin
/plugin marketplace add Lum1104/Understand-Anything
/plugin install understand-anything
```

| Command | Description |
| ------- | ----------- |
| `/understand` | Analyze the current codebase and build a knowledge graph. |
| `/understand-dashboard` | Open the interactive visualization dashboard. |
| `/understand-chat [QUERY]` | Ask questions about the codebase. |
| `/understand-diff` | Analyze the impact of changes (git diffs / PRs). |
| `/understand-explain [FILE]` | Deep-dive explanation of a specific file or function. |
| `/understand-onboard` | Generate an onboarding guide for new team members. |

### Install context-mode

```bash
# Install the plugin
/plugin marketplace add mksglu/context-mode
/plugin install context-mode@context-mode
```

Then run `/reload-plugins` and verify with `/context-mode:ctx-doctor`.

---

## Configuration

### settings.json Template

```json
{
  "env": {
    "DISABLE_TELEMETRY": "1",
    "DISABLE_ERROR_REPORTING": "1",
    "DISABLE_FEEDBACK_COMMAND": "1",
    "DISABLE_EXTRA_USAGE_COMMAND": "1",
    "CLAUDE_CODE_DISABLE_FEEDBACK_SURVEY": "1",
    "CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC": "1",
    "ENABLE_TOOL_SEARCH": "true",
    "CLAUDE_CODE_DISABLE_1M_CONTEXT": "1",
    "CLAUDE_CODE_ATTRIBUTION_HEADER": "1",
    "CLAUDE_CODE_DISABLE_TERMINAL_TITLE": "1",
    "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1" 
  },
  "feedbackSurveyRate": 0
}
```

### Environment Variables

#### Telemetry & Privacy

| Variable | Documented | Description |
| -------- | ---------- | ----------- |
| `DISABLE_TELEMETRY` | ✅ | Disables all telemetry collection (metrics, usage data). Setting this also suppresses the feedback survey. The official opt-in counterpart is `CLAUDE_CODE_ENABLE_TELEMETRY=1`. |
| `DISABLE_ERROR_REPORTING` | ✅ | Disables automatic error/crash reporting to Anthropic. Already off by default on Bedrock, Vertex, and Foundry — only active on the `claude.ai` API. |
| `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` | ✅ | Master kill-switch for **all** non-essential outbound traffic: surveys, telemetry, error reporting, bug reports. Covers the two variables above and more. [docs](https://code.claude.com/docs/en/data-usage) |

#### Feedback & Surveys

| Variable | Documented | Description |
| -------- | ---------- | ----------- |
| `CLAUDE_CODE_DISABLE_FEEDBACK_SURVEY` | ✅ | Disables the in-session *"How is Claude doing?"* pop-up. Only a numeric rating is collected (no transcripts), but this suppresses it entirely. [docs](https://code.claude.com/docs/en/data-usage) |
| `feedbackSurveyRate` | ✅ | **Top-level `settings.json` field, not an env var.** Float between `0`–`1` (probability of showing the survey). Setting to `0` is equivalent to `CLAUDE_CODE_DISABLE_FEEDBACK_SURVEY=1`. |
| `DISABLE_FEEDBACK_COMMAND` | ✅ | Disables the `/feedback` slash command, which otherwise lets users send their full conversation history to Anthropic (encrypted, optionally creates a public GitHub issue). [docs](https://code.claude.com/docs/en/data-usage) |
| `DISABLE_EXTRA_USAGE_COMMAND` | ⚠️ | Disables extra usage/stats commands exposed in the CLI. Community-discovered — not in official docs. |

#### Features & Behavior

| Variable | Documented | Description |
| -------- | ---------- | ----------- |
| `ENABLE_TOOL_SEARCH` | ✅ | Controls deferred tool search. Values: `true` (always on), `false` (off), `auto` (auto-detect by tool count), `auto:N` (custom % threshold). Requires Sonnet 4+ or Opus 4+. [docs](https://code.claude.com/docs/en/mcp) |
| `CLAUDE_CODE_DISABLE_1M_CONTEXT` | ⚠️ | Disables the 1-million-token context window when available. Useful to reduce costs or avoid memory pressure on large sessions. Community-discovered. |
| `CLAUDE_CODE_ATTRIBUTION_HEADER` | ⚠️ | Injects an attribution/user-agent header into API requests (useful for identifying Claude Code traffic in API logs). Community-discovered. |
| `CLAUDE_CODE_DISABLE_TERMINAL_TITLE` | ⚠️ | Prevents Claude Code from dynamically updating the terminal window/tab title with the current task. Useful when it conflicts with shell title management (tmux, iTerm, etc.). Community-discovered. |

### MCP Servers

#### Add an MCP via Streamable HTTP

Use `mcp-remote` to proxy any Streamable HTTP MCP endpoint into Claude Code's `mcpServers` config. This lets you connect to local or remote MCP servers that speak the HTTP transport without needing a native stdio adapter.

Add the following to `~/.claude/settings.json` (or the project-level `.claude/settings.json`):

```json
"mcpServers": {
  "mcp-local": {
    "command": "npx",
    "args": [
      "-y",
      "mcp-remote@latest",
      "http://localhost:8889/mcp"
    ]
  }
}
```

> `mcp-remote` is a zero-install bridge — `npx -y` fetches the latest version on first run and caches it. Replace `http://localhost:8889/mcp` with the actual endpoint URL of your MCP server.

---

# Claude Desktop

## Troubleshooting

### Reset MCP Cache

Kills lingering `mcp-remote` processes, wipes the auth cache, clears temp files, and relaunches the app. Run this when OAuth authorization gets stuck or MCP servers fail to connect.

```bash
echo "Clearing MCP cache..."
pkill -f "mcp-remote" 2>/dev/null
pkill -f "Claude" 2>/dev/null
rm -rf ~/.mcp-auth
find /tmp -name "*mcp*" -delete 2>/dev/null
sleep 2
echo "Restarting Claude Desktop..."
open -a "Claude"
echo "Done — authorize the OAuth flow when the browser opens"
```
