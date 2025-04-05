---
title:  Podman
created: Saturday 5th April 2025 13:03
aliases: 
tags: 
---
**Podman** is an open-source container engine developed by Red Hat, designed for developing, managing, and running containers and container images. It's a part of the **libpod** library, and is often seen as a drop-in replacement for [[Docker]], with some key differences.

- Podman is a **daemonless container engine** that allows you to run containers and pods (groups of containers).
- It uses the same **OCI (Open Container Initiative)** standards as Docker, meaning you can run the same container images with either.
- Podman can manage **pods** natively (like in Kubernetes), which groups containers sharing the same network namespace.
- Excellent rootless support out-of-the-box.
- Decentralized; each container runs as its own process.
- Native support for **pods**, similar to Kubernetes.