---
title:  What is SAGA Pattern in Microservice Architecture - Which Problem does it solve
created: Saturday 12th April 2025 00:30
aliases: 
tags:
  - architecture
  - microservices
  - event-driven
---
- https://medium.com/javarevisited/what-is-saga-pattern-in-microservice-architecture-which-problem-does-it-solve-de45d7d01d2b
- Type: article
- Source: Javarevisited (Medium) · Soma · Jan 2023 (read through an archive copy)

---

# TL;DR

The **saga** pattern keeps data consistent across microservices by splitting a long transaction into local steps, each with a **compensating action** that undoes it if a later step fails.

# Summary

In a microservice architecture one request becomes several, so some steps may succeed while others fail. Distributed atomic transactions are hard, so a saga records the steps of a business transaction and, on failure, triggers compensating transactions to return to a consistent state. The standard example is an order: payment fails, so the inventory reservation is cancelled and the order is not shipped. Sagas can be coordinated through a database, message queue or coordination service and give eventual consistency.

# Key takeaways

1. **Break the transaction** into independent local steps, one per service.
2. **Compensate, do not roll back**: if a step fails, run compensating transactions for the earlier steps.
3. **Store saga state** (in a database, queue or coordinator) to know which compensations to run.
4. **Advantages**: handles failures gracefully, avoids lost updates, adds resilience and gives a defined compensation process.
5. **Disadvantages**: hard to implement, monitor and debug; state overhead; extra latency from round trips; no standardisation across frameworks.
6. **Tooling**: no Java framework offers sagas directly; the author suggests Apache Camel or Spring Integration with [[Kafka]], event sourcing and message-driven design.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[Software Architecture]] | Microservice data consistency |
| [[Architecture Patterns]] | Saga as a pattern |
| [[Kafka]] | Event backbone for saga steps |
| [[What Is Event-Driven Microservices Architecture]] | Saga vs 2PC in an event-driven design |

# When to use

1. When a business operation **spans several services** and needs consistency.
2. When preparing **microservices interview** answers about distributed transactions.
3. When choosing between sagas and two-phase commit.

# Caveats

- Interview-style overview with promotional material; no concrete implementation or orchestration vs choreography comparison.

---
[[Software Architecture]] [[Architecture Patterns]] [[Kafka]]
[[What Is Event-Driven Microservices Architecture]]
[[System Design Interview Basics - Difference Between API Gateway and Load Balancer]]
