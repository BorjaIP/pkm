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