---
title:  Cloud Architecture Patterns
created: Saturday 12th April 2025 00:13
aliases: 
tags:
  - architecture
  - cloud
---
- https://distributedleo.medium.com/cloud-architecture-patterns-3a932a95691b
- Type: article
- Source: Medium · Leo Kyrpychenko · Dec 2014

---

# TL;DR

A short catalogue of cloud-native architecture patterns: scale horizontally and statelessly, decouple with queues, design for failure and latency, and accept eventual consistency.

# Summary

A cloud architecture pattern is a tested approach to problems of applications designed to run in a cloud. The essay summarises a dozen patterns: horizontal scaling of compute, queue-centric workflow, auto-scaling, eventual consistency, MapReduce, database sharding, multi-tenancy on commodity hardware, busy signal, node failure, network latency, colocation and valet key, with short guidance on each.

# Key takeaways

1. **Horizontal scaling**: keep nodes stateless (no sticky sessions) so they are interchangeable.
2. **Queue-centric workflow**: decouple web and service tiers with queues; not for read-only requests.
3. **Auto-scaling**: automate routine scaling for cost and resilience.
4. **Eventual consistency**: CAP forces a business choice between stale data and scalability.
5. **Sharding**: spread workloads over many database nodes; cross-shard operations are harder.
6. **Design for failure**: handle transient errors (busy signal), node failures and network latency (reduce perceived latency and distance).
7. **Colocate** nodes by default; **valet key** gives clients temporary storage access without proxying data.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[Cloud]] | Cloud-native application context |
| [[Architecture Patterns]] | Catalogue of patterns |
| [[AWS]] | One of the target clouds named |
| [[Big Data]] | MapReduce and Hadoop ecosystem |

# When to use

1. When **reviewing a design for cloud-readiness** (stateless, decoupled, failure-tolerant).
2. When you need a quick **list of pattern names** to search further.
3. When explaining eventual consistency trade-offs.

# Caveats

- 2014 essay with brief entries and no examples; the last patterns were cut off in the text read.

---
[[Cloud]] [[Architecture Patterns]] [[Software Architecture]]
[[The Software Architecture Handbook]]
[[De Lambda a Kappa - evolución de las arquitecturas Big Data]]
