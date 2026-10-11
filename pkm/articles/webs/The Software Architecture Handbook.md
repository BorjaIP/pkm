---
title:  The Software Architecture Handbook
created: Saturday 12th April 2025 00:29
aliases: 
tags:
  - architecture
  - cloud
---
- https://www.freecodecamp.org/news/an-introduction-to-software-architecture-patterns/
- Type: article
- Source: freeCodeCamp · German Cocca · Jul 2022

---

# TL;DR

A beginner's map of architecture decisions: system design (monolith, microservices), code structure (layered, MVC) and infrastructure (on-premise to serverless).

# Summary

Architecture is the set of design decisions about system structure and behaviour, from folder layout to hosting. The handbook walks through client-server, monolith, microservices, Backend for Frontend, load balancing and database replication; folder patterns (all-in-one, layered, MVC); and hosting models (on-premise, rented servers, traditional, elastic and serverless cloud). Each comes with trade-offs, and the advice is to start simple.

# Key takeaways

1. **Start with a monolith** and move to microservices only when scale or complexity demands it.
2. **Microservices** scale and deploy independently but are harder to set up and manage; a **BFF** layer hides them from the front end.
3. **Scale horizontally** with a load balancer in front of identical servers; use **replicas** for reads and a source database for writes.
4. **Layered architecture**: application, routes, controllers, models, persistence, with requests flowing through each layer in order; MVC adds the view.
5. **Hosting spectrum**: on-premise, rented servers, cloud traditional, elastic and serverless (per-execution billing).
6. **Principles**: modularity, separation of concerns, loose coupling and infrastructure as code (Terraform, CloudFormation).

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[Software Architecture]] | The subject |
| [[Architecture Patterns]] | Patterns catalogued |
| [[System Design]] | Interview-style design context |
| [[Terraform]] | Infrastructure as code example |
| [[Serverless]] | Function-per-request hosting model |

# When to use

1. When you need an **overview of architectural patterns and trade-offs**.
2. When deciding **monolith vs microservices** for a new project.
3. When preparing a system-design discussion.

# Caveats

- Introductory; it does not cover event-driven or pipe-and-filter patterns and lists quality attributes only implicitly.

---
[[Software Architecture]] [[Architecture Patterns]] [[System Design]]
[[The C4 model for visualizing software architecture]]
[[System Design Interview Basics - Difference Between API Gateway and Load Balancer]]
[[Cloud Architecture Patterns]]
