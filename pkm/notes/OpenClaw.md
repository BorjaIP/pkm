---
title:  OpenClaw
created: Sunday 15th February 2026 20:34
aliases:
tags:
---
**OpenClaw** is an open-source, locally-run personal AI assistant framework that operates as an autonomous agent integrated with messaging platforms. 

## Architecture

- WebSocket-based Gateway control plane at `ws://127.0.0.1:18789`
- Canvas system for agent-driven visual workspace interactions
- Optional sandboxing for security

## Installation

```bash
npm install -g openclaw@latest
openclaw onboard --install-daemon
```

Deployment options: Tailscale Serve/Funnel, SSH tunnels, Docker, Nix-based configuration.

## Web Search

### Tavily

```bash
openclaw configure --section web
# in your .env
TAVILY_API_KEY
# in openclaw.json
webSearch.provider: "tavily"
```

## Tools

| Tool                                                                            | Description                                                                                                                   |
| ------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| [awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills) | Curated collection of 5,400+ OpenClaw skills filtered and categorized from the official OpenClaw Skills Registry.             |
