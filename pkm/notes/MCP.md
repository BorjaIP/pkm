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

| Tool                                                         | Description                                                 |
| ------------------------------------------------------------ | ----------------------------------------------------------- |
| [mcp-gateway](https://github.com/docker/mcp-gateway)         | docker mcp CLI plugin / MCP Gateway                         |
| [agentgateway](https://github.com/agentgateway/agentgateway) | Next Generation Agentic Proxy for AI Agents and MCP servers |

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