---
title:  What Is Event-Driven Microservices Architecture
created: Saturday 12th April 2025 00:29
aliases: 
tags:
  - architecture
  - microservices
  - event-driven
---
- https://medium.com/fintechexplained/what-is-event-driven-microservices-architecture-278d9e5adf8a
- Type: article
- Source: FinTechExplained (Medium) · Farhad Malik · Dec 2022 (read through an archive copy)

---

# TL;DR

Combine microservices with an **event broker** such as [[Kafka]] so services publish and subscribe to events instead of calling each other, removing synchronous chains and single points of failure.

# Summary

Microservices give independent deployment, scaling and technology choice, but synchronous REST calls chain services together: a slow or failed service blocks every caller. In an event-driven design a service raises immutable events (for example `PriceTick` or `ItemCreated`) to a broker; consumers react without knowing the producer. Event sourcing stores events in order so they can be replayed, CQRS separates reads from writes, and Kafka topics, offsets and retention provide replay. Distributed transactions are the hard part, handled with two-phase commit or the saga pattern.

# Key takeaways

1. **Events are immutable facts** with a producer, a broker and consumers; they decouple services both in time and in knowledge of each other.
2. **Per-service databases** give isolation; a shared database couples release cycles.
3. **Synchronous chains do not scale**: polling only moves the problem, and one failure can cascade.
4. **Topic flow example**: Trade service publishes to a `Trade` topic, User Management checks permissions and publishes to `TradeCheck`, Calculation consumes `CalculationTopic` and publishes `CalculationResponse`.
5. **Event Sourcing** (replay events, retry from the failed step) and **CQRS** (separate read and write services).
6. **Kafka** provides brokers, topics, consumers, offsets and disk persistence, so messages can be replayed within retention.
7. **Transactions**: use 2PC for short-lived steps or **saga** with compensating steps and an Error topic for rollbacks; do not use events where you need blocking synchronous behaviour.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[Kafka]] | Broker and event store |
| [[Docker]] | Containerising each service |
| [[Architecture Patterns]] | Event-driven pattern |
| [[Software Architecture]] | Microservices benefits and drawbacks |
| [[What is SAGA Pattern in Microservice Architecture - Which Problem does it solve]] | Distributed transaction pattern |

# When to use

1. When **moving from synchronous REST chains** to asynchronous messaging.
2. When designing **event sourcing or CQRS** with Kafka.
3. When explaining **benefits and drawbacks of microservices**.

# Caveats

- Introductory and conceptual; no benchmarks or code, and the saga and 2PC sections are brief.

---
[[Software Architecture]] [[Architecture Patterns]] [[Kafka]] [[Docker]]
[[What is SAGA Pattern in Microservice Architecture - Which Problem does it solve]]
[[System Design Interview Basics - Difference Between API Gateway and Load Balancer]]
[[De Lambda a Kappa - evolución de las arquitecturas Big Data]]
