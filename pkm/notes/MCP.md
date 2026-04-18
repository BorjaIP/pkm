---
title:  MCP
created: Sunday 27th April 2025 10:46
aliases: 
tags: 
---
**Model Context Protocol (MCP)** is an open standard developed by Anthropic to facilitate seamless interaction between AI models and external tools or data sources. It standardizes the way applications provide context to large language models (LLMs), enabling structured, secure, and efficient communication.

Key features of MCP include:

- **Standardized Interface**: MCP provides a universal protocol for AI models to access external data and tools, reducing the need for custom integrations .
- **Model-Agnostic Design**: It works across various AI models, including those from OpenAI and Anthropic, ensuring broad applicability .
- **Structured Communication**: MCP utilizes JSON-RPC 2.0 for structured messaging, allowing for clear and organized interactions between AI models and external systems .
- **Security and Control**: Organizations retain full control over their data, with MCP supporting secure access protocols and authentication mechanisms .

| Tool                                                                         | Description                                                                                                                                                                                                  |
| ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [mcp-gateway](https://github.com/docker/mcp-gateway)                         | docker mcp CLI plugin / MCP Gateway                                                                                                                                                                          |
| [agentgateway](https://github.com/agentgateway/agentgateway)                 | Next Generation Agentic Proxy for AI Agents and MCP servers                                                                                                                                                  |
| [context7](https://github.com/upstash/context7)                              | MCP server that retrieves current, version-specific library documentation and injects it into prompts, eliminating outdated info and hallucinated APIs.                                                      |
| [knowledge](https://github.com/withoneai/knowledge)                          | Structured API docs for 40,000+ tools across 250+ platforms, served via CLI or REST API for MCP-compatible AI agents.                                                                                        |
| [chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) | Chrome DevTools for AI agents: browser automation, network inspection, performance tracing, console debugging, and screenshots via Puppeteer.                                                                |
| [CodeGraphContext](https://github.com/CodeGraphContext/CodeGraphContext)     | Transforms code repositories into queryable graph databases via CLI or MCP server; supports 14 languages with function call tracking, dead code detection, and complexity analysis.                          |
| [GitNexus](https://github.com/abhigyanpatwari/GitNexus)                      | Zero-server code intelligence engine that precomputes codebase knowledge graphs for AI agents (Claude Code, Cursor); supports blast radius analysis and breaking change prevention via MCP or in-browser UI. |
| [context-mode](https://github.com/mksglu/context-mode)                       | MCP server that reduces context window bloat by sandboxing tool outputs and maintaining session continuity through SQLite-backed event tracking and FTS5 search. Claims up to 98% context savings.           |
# Chrome DevTools MCP

`chrome-devtools-mcp` lets coding agents (Claude, Cursor, Copilot, …) control and inspect a live Chrome browser via [Chrome DevTools](https://github.com/ChromeDevTools/devtools-frontend) and [Puppeteer](https://github.com/puppeteer/puppeteer).

**Key capabilities**

| Category | Tools |
| -------- | ----- |
| Input automation | `click`, `fill`, `fill_form`, `drag`, `hover`, `press_key`, `type_text`, `upload_file`, `handle_dialog` |
| Navigation | `navigate_page`, `new_page`, `close_page`, `list_pages`, `select_page`, `wait_for` |
| Performance | `performance_start_trace`, `performance_stop_trace`, `performance_analyze_insight`, `take_memory_snapshot` |
| Network | `list_network_requests`, `get_network_request` |
| Debugging | `evaluate_script`, `list_console_messages`, `take_screenshot`, `take_snapshot`, `lighthouse_audit` |
| Emulation | `emulate`, `resize_page` |

## Installation

**Claude Code — as a plugin (MCP + Skills)**

```bash
/plugin marketplace add ChromeDevTools/chrome-devtools-mcp
/plugin install chrome-devtools-mcp
```

Restart Claude Code, then verify with `/skills`.

**Claude Code — MCP only**

```bash
claude mcp add chrome-devtools --scope user npx chrome-devtools-mcp@latest
```

**Generic MCP config**

```json
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": ["-y", "chrome-devtools-mcp@latest"]
    }
  }
}
```

> [!tip] Test it
> `Check the performance of https://developers.chrome.com` — the agent will open Chrome, record a trace, and return insights.

## Connect to a running Chrome instance

Useful when you need shared session state or the agent runs inside a sandbox.

```bash
# macOS — launch Chrome with remote debugging
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome \
  --remote-debugging-port=9222 \
  --user-data-dir=/tmp/chrome-profile-stable
```

```json
{
  "mcpServers": {
    "chrome-devtools": {
      "command": "npx",
      "args": ["chrome-devtools-mcp@latest", "--browser-url=http://127.0.0.1:9222"]
    }
  }
}
```

Or use `--autoConnect` (Chrome 144+) to auto-attach to the running default profile via `chrome://inspect/#remote-debugging`.

## Useful flags

| Flag | Description |
| ---- | ----------- |
| `--headless` | Run without a browser UI |
| `--slim` | Expose only 3 tools: navigate, evaluate, screenshot |
| `--isolated` | Temporary profile, wiped after session |
| `--channel=canary\|beta\|dev` | Target a specific Chrome channel |
| `--no-usage-statistics` | Opt out of Google telemetry |
| `--viewport 1280x720` | Set initial window size |

---

# Docker MCP Gateway


```cardlink
url: https://www.docker.com/blog/dynamic-mcps-stop-hardcoding-your-agents-world/
title: "Dynamic MCPs: Stop Hardcoding Your Agents’ World | Docker"
description: "Empower your agents to configure MCPs dynamically with the Docker MCP Gateway smart search and code mode tools."
host: www.docker.com
favicon: https://www.docker.com/app/uploads/2024/02/cropped-docker-logo-favicon-32x32.png
image: https://www.docker.com/app/uploads/2025/03/image.png
```


```bash [docker-compose.yaml]
services:
  gateway:
    image: docker/mcp-gateway
    ports:
      - "8080:8080"
    volumes:
      - "/var/run/docker.sock:/var/run/docker.sock"
      - "~/.docker/mcp:/mcp"
    command:
      - --catalog=/mcp/catalogs/docker-mcp.yaml
      - --config=/mcp/config.yaml
      - --registry=/mcp/registry.yaml
      - --watch=true
      - --transport=sse
      - --port=8080
```

```bash [mcp.json]
{
  "mcpServers": {
    "mcp-toolkit-gateway": {
      "command": "docker",
      "args": [
	      "run", 
	      "-i", 
	      "--rm", 
	      "-v", "/var/run/docker.sock:/var/run/docker.sock",
	      "~/.docker/mcp:/mcp",
	      "docker/mcp-gateway", 
	      "--catalog=/mcp/catalogs/docker-mcp.yaml",
	      "--catalog=/mcp/catalogs/custom.yaml",
	      "--config=/mcp/config.yaml",
	      "--registry=/mcp/registry.yaml",
	      "--tools-config=/mcp/tools.yaml",
	      "--transport=stdio"
	  ]
    }
  }
}
```

Use the Airbnb MCP server to search for listings with the following criteria:

- Location: A coruña, Spain
- Check-in: 2026-02-27
- Check-out: 2026-03-01
- Guests: 2 adults
- Price range: €50 – €80 per night
- Minimum review rating: 4.4 stars

Sorting / ordering requirements:

- Sort results by price (low to high)
- If prices are equal, order by review rating (high to low)

Output requirements:

- Return up to 20 listings
- Include for each listing:
    
    - Name
    - Price per night
    - Review rating & number of reviews
    - Location
    - Key amenities
    - Direct Airbnb listing URL