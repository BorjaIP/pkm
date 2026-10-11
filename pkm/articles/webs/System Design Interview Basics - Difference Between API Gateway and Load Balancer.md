---
title:  System Design Interview Basics - Difference Between API Gateway and Load Balancer
created: Saturday 12th April 2025 00:30
aliases: 
tags:
  - architecture
  - api-gateway
  - networking
---
- https://levelup.gitconnected.com/system-design-interview-basics-difference-between-api-gateway-and-load-balancer-60260b568121
- Type: article
- Source: Level Up Coding (Medium) · Arslan Ahmad · Dec 2022

---

# TL;DR

An **API gateway routes** requests to the right microservice and adds cross-cutting features, while a **load balancer distributes** traffic evenly across identical backend servers.

# Summary

In a microservice system the gateway is the single entry point: it receives client requests, forwards them to the appropriate service and returns the response. A load balancer sits in front of a group of servers behind one well-known address and spreads load by health and performance. The two are often combined, and a gateway can load balance itself.

# Key takeaways

1. **Gateway = routing by URL/API** to different services; **load balancer = distribution** across replicas of one service.
2. **Gateway features**: rate limiting, caching, authentication and authorization, monitoring, transformation (XML/JSON, aggregation), request validation, circuit breaker and service discovery.
3. **Gateway can also load balance** across instances of a microservice.
4. **Load balancers** target one stable IP and pick a backend by availability and performance.
5. **Advantages of a gateway**: simpler client access, better performance via caching and routing, central security and observability.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[Software Architecture]] | Microservice entry-point patterns |
| [[ELB]] | AWS load balancer example of the second concept |
| [[System Design]] | Interview framing for both components |
| [[An Envoy-Powered, Kubernetes-Native API Gateway]] | A concrete gateway implementation |

# When to use

1. When **explaining API gateway vs load balancer** in a design review or interview.
2. When listing **gateway responsibilities** for a microservices design.
3. When choosing where to put **rate limiting and authentication**.

# Caveats

- Introductory and generic; no product comparisons or benchmarks.

---
[[Software Architecture]] [[System Design]] [[ELB]] [[API]]
[[An Envoy-Powered, Kubernetes-Native API Gateway]]
[[Apache APISIX - Gateway transcode]]
