---
title:  An Envoy-Powered, Kubernetes-Native API Gateway
created: Friday 11th April 2025 23:39
aliases: 
tags:
  - k8s
  - api-gateway
  - networking
---
- https://github.com/kgateway-dev/kgateway
- Type: repo
- Source: GitHub · kgateway-dev (formerly Gloo, by Solo.io) · Apache-2.0 · CNCF sandbox

---

# TL;DR

**kgateway** is an open-source control plane that implements the Kubernetes **Gateway API** for **Envoy**, adding authentication, authorization and rate limiting at the edge.

# What it does

Started in 2018 as Gloo and production-ready since 2019, it exposes APIs and applies policies in one place, routes to microservices, serverless functions or legacy apps (useful for gradual migration), and supports route delegation and composable policies for multiple teams. Since 2.3.0 the AI and agentic control plane moved to the separate agentgateway repository, so kgateway now centres on the Envoy API gateway.

# Key takeaways

1. **Gateway API implementation** on top of Envoy, scaling from small microgateways to large central gateways.
2. **Central policies**: authentication, authorization and rate limiting defined once.
3. **Hybrid migration**: function-level routing and discovery across services, functions and legacy apps.
4. **Multi-team tenancy** through route delegation.
5. **Governance**: CNCF sandbox project, Apache-2.0, Helm charts under `install/helm`.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[Kubernetes]] | Gateway API resources |
| Envoy | Data plane (alongside agentgateway) |
| [[Helm]] | Installation method |
| [[API]] | What the gateway exposes and protects |

# When to use

1. When choosing a **Kubernetes-native API gateway** built on Envoy.
2. When looking for the **successor of Gloo**.
3. When comparing gateways, see [[System Design Interview Basics - Difference Between API Gateway and Load Balancer]].

# Caveats

- The repository page has no install steps, and its tagline still mentions an AI gateway that the body says moved out.

---
[[Kubernetes]] [[Istio]] [[API]]
[[System Design Interview Basics - Difference Between API Gateway and Load Balancer]]
[[Apache APISIX - Gateway transcode]]
