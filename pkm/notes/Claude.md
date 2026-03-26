---
title:  Claude
created: Saturday 31st January 2026 23:47
aliases: 
tags: 
---

| Tool                                                   | Description                                                                                                                |
| ------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------- |
| [ccusage](https://github.com/ryoppippi/ccusage)        | A CLI tool for analyzing Claude Code/Codex CLI usage from local JSONL files.                                               |
| [claude-mem](https://github.com/thedotmack/claude-mem) | A Claude Code plugin that automatically captures everything Claude does during your coding sessions, compresses it with AI |
| [claude-hud](https://github.com/jarrodwatts/claude-hud) | Claude Code plugin that muestra en el statusline del terminal: uso de contexto, rate limits, actividad de herramientas, progreso de tareas, estado de git y agentes activos. Se actualiza cada ~300ms. |
| [ralph](https://github.com/snarktank/ralph) | Autonomous AI agent loop that runs repeatedly until all PRD items are complete. |
| [awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents) | A collection of 100+ specialized Claude Code subagents covering a wide range of development use cases. |
| [awesome-claude-agents](https://github.com/vijaythecoder/awesome-claude-agents) | An orchestrated sub agent dev team powered by Claude Code. |
| [claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | Comprehensive guide to Claude Code best practices: subagents, commands, skills, memory systems, and MCP servers for effective AI-assisted development workflows. |
| [claudian](https://github.com/YishenTu/claudian) | Obsidian plugin that integrates Claude Code as an AI collaborator directly into your vault. Supports agentic file ops, bash commands, inline editing with diff previews, slash commands, skills/subagents, vision, and MCP servers. Requires Claude Code CLI. |
| [HolyClaude](https://github.com/CoderLuii/HolyClaude) | Containerized AI development workstation: Claude Code + web UI (CloudCLI) + headless Chromium + 5 AI CLIs (Claude, Gemini, Codex, Cursor, TaskMaster) + 50+ dev tools in a single Docker image. Supports AMD64/ARM64. No setup required. |
| [everything-claude-code](https://github.com/affaan-m/everything-claude-code) | Anthropic hackathon winner. Performance optimization system for Claude Code: 28 agents, 50+ skills, 25+ slash commands, hooks, language rules, and MCP configs. Built from 10+ months of daily use. |

```bash
# resume old session
claude --resume
```

## Script for rest Cache in Claude Dektop

```bash
echo "🧹 Limpiando caché MCP..."
pkill -f "mcp-remote" 2>/dev/null
pkill -f "Claude" 2>/dev/null
rm -rf ~/.mcp-auth
find /tmp -name "*mcp*" -delete 2>/dev/null
sleep 2
echo "🚀 Reiniciando Claude Desktop..."
open -a "Claude"
echo "✅ Listo — autoriza el OAuth cuando aparezca el navegador"
```