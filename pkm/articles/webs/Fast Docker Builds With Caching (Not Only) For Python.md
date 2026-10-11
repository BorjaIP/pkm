---
title:  Fast Docker Builds With Caching (Not Only) For Python
created: Friday 11th April 2025 21:36
aliases: 
tags:
  - docker
  - python
  - devops
---
- https://towardsdatascience.com/fast-docker-builds-with-caching-for-python-533ddc3b0057/
- Type: article
- Source: Towards Data Science · Jan Michelfeit · Dec 2021

---

# TL;DR

Cache the dependency layer, build in two stages and pass credentials as **BuildKit secrets**, so [[Docker]] rebuilds only what changed, even in CI.

# Summary

Python image builds are slow because dependency installation reruns, CI systems offer little layer cache and private package indexes need credentials. The article copies dependency manifests (`pyproject.toml`, lock file) and installs before copying code, so that layer is rebuilt only when dependencies change. A build stage creates a virtualenv, the slim final stage copies it, and secrets are mounted at build time so they do not invalidate the cache.

# Key takeaways

1. **Separate the dependency layer** from application code.
2. **Use multi-stage builds**: build stage for dependencies, `3.8-slim` for the final image.
3. **Exclude dev dependencies** (`poetry install --no-dev`) to shrink the image.
4. **Copy the venv** between stages and set `PATH` and `VIRTUAL_ENV`.
5. **Pass credentials with `--secret`** (`DOCKER_BUILDKIT=1`); mounts are ignored by caching logic.
6. **Warm CI caches** by building `--target build-stage` and listing it and `latest` as cache sources, or move them with `docker save`.
7. **Harden**: run as non-root and set `PIP_NO_CACHE_DIR=1` in the build stage.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[Docker]] | Layer cache, BuildKit secrets |
| [[Python]] | Poetry-based dependency management |
| [[DevOps]] | CI/CD cache reuse |

# When to use

1. When **speeding up Python Docker builds** in CI.
2. When you need to inject **private-index credentials** without baking them in layers.
3. When reducing **final image size** with multi-stage builds.

# Caveats

- The Dockerfile and CI snippets were not captured, and the article reports no timings.

---
[[Docker]] [[Python]] [[DevOps]]
[[Using YAML Anchors and X Properties in Docker Compose]]
