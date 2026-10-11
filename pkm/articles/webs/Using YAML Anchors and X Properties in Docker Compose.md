---
title:  Using YAML Anchors and X Properties in Docker Compose
created: Friday 11th April 2025 21:39
aliases: 
tags:
  - docker
  - config
  - devops
---
- https://nickjanetakis.com/blog/docker-tip-82-using-yaml-anchors-and-x-properties-in-docker-compose
- Type: tutorial
- Source: nickjanetakis.com · Nick Janetakis · updated May 2019

---

# TL;DR

Define shared service settings once under a top-level `x-` key with a YAML **anchor**, then reuse them in each service with `<<: *anchor`.

# Summary

Compose files often repeat the same build, env, volume and restart settings across services such as `web` and `worker`. An **anchor** (`&name`) marks a YAML block, an **alias** (`*name`) reuses it, and the **merge key** (`<<:`) pulls it into a service. Top-level keys prefixed `x-` are Compose **extension fields**, a safe place to declare the anchor. Keys placed after the merge override the shared values for that service only.

# Key takeaways

1. **Declare once**: `x-app: &default-app` followed by the shared settings.
2. **Reuse with the merge key**: `<<: *default-app` inside each service.
3. **Override per service** by writing the key after the merge, e.g. `stop_grace_period: "10s"` on the worker.
4. **Name the extension field freely**: any valid YAML key starting with `x-` works; matching the anchor name is only a convention.
5. **Avoid over-abstraction**: extracting just two shared properties is rarely worth it.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[Docker Compose]] | Extension fields (`x-`) are ignored by Compose, so they host anchors |
| [[Docker]] | Services and images being configured |
| YAML anchors, aliases, merge key | The deduplication mechanism |

# When to use

1. When a Compose file **repeats the same settings** across services.
2. When you need to **override a single value** while inheriting a shared block.
3. When explaining what an `x-` top-level key is for.

# Caveats

- Examples are excerpts using Compose file format 3.4; no minimum Compose version is stated.

---
[[Docker Compose]] [[Docker]] [[DevOps]]
