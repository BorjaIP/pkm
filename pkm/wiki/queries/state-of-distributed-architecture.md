---
title: State of distributed systems architecture
created: Monday 12th October 2026 18:44
aliases:
tags:
  - archived
  - agent
  - architecture
status: active
source: digest
query: What do I know about architecture patterns for distributed and cloud systems?
---

> **Status: active** | Source: digest of vault notes
>
> Synthesis of what the vault says. Each claim cites the note it comes from.

# Question

What do I know about architecture patterns for distributed and cloud systems?

# Answer

**Orientation.** Start from the decision map (system design, code structure, hosting) and the advice to begin with a monolith ([[The Software Architecture Handbook]]); document at several zoom levels with [[The C4 model for visualizing software architecture]]. Hubs: [[Software Architecture]], [[Architecture Patterns]], [[System Design]].

**Cloud-native patterns.** Stateless horizontal scaling, queue-centric workflows, auto-scaling, eventual consistency, sharding, designing for node failure and latency ([[Cloud Architecture Patterns]]).

**Services and messaging.** Microservices decouple teams and deployment but make synchronous chains fragile; event-driven designs with a broker (Kafka) invert dependencies and enable event sourcing and CQRS ([[What Is Event-Driven Microservices Architecture]]). Consistency across services is handled with sagas and compensating steps ([[What is SAGA Pattern in Microservice Architecture - Which Problem does it solve]]).

**Entry points.** An API gateway routes and applies cross-cutting policies; a load balancer distributes traffic across replicas ([[System Design Interview Basics - Difference Between API Gateway and Load Balancer]]).

**Data architecture.** Lambda (batch plus speed layers) versus Kappa (everything is a replayable stream) ([[De Lambda a Kappa - evolución de las arquitecturas Big Data]]). Databases: tiers and normalization ([[Concepts of Database Architecture]]) and the internals of a SQL engine ([[Relational Database Management System (RDBMS)Architecture]]).

**Where it connects.** Kubernetes-level implementations of these ideas are in [[state-of-kubernetes-networking-security]]; data pipelines for ML in [[state-of-mlops]].

# Pages Consulted

[[Software Architecture]], [[Architecture Patterns]], [[System Design]], [[Databases]] and the web notes cited above.

# Sources Cited

Original URLs are on each cited web note.
