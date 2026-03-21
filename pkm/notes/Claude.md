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