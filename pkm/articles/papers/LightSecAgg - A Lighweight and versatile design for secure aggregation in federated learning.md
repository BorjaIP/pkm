---
title: LightSecAgg - A Lighweight and versatile design for secure aggregation in federated learning
created: Friday 28th July 2023 08:58
aliases:
tags:
  - fl
  - pet
  - ml
---
- https://arxiv.org/pdf/2109.14236.pdf
- Source: arxiv

---

# TL;DR

**LightSecAgg** replaces pairwise secret sharing in federated learning with a one-shot aggregate mask scheme, reducing secure aggregation overhead from O(n²) to O(n) while tolerating client dropout and Byzantine adversaries.

# Summary

Standard secure aggregation in **federated learning** requires pairwise secret sharing between all clients, causing O(n²) communication and computation overhead that limits scalability. LightSecAgg replaces this with a **one-shot encoding scheme** where each client generates a single aggregate mask that cancels at the server, preserving privacy without revealing individual updates. The scheme scales linearly O(n), tolerates both **client dropout** and Byzantine participants within configurable thresholds, and integrates with standard FL protocols without requiring architectural changes.

# Key contributions

1. Proposes **one-shot mask encoding** as a replacement for pairwise secret sharing, achieving O(n) rather than O(n²) scaling.
2. Demonstrates that **aggregate masks** that cancel at the server provide equivalent privacy to pairwise schemes.
3. Shows that **dropout tolerance** can be built natively into the one-shot encoding without post-hoc recovery mechanisms.
4. Establishes that **Byzantine resistance** is compatible with the lightweight encoding at configurable security thresholds.

# When to cite

1. When comparing **secure aggregation protocols** for federated learning and evaluating communication overhead.
2. When arguing that **O(n²) pairwise secret sharing** is a scalability bottleneck in large FL deployments.
3. When looking for a secure aggregation scheme that handles **client dropout** natively.
4. When discussing **linear-scaling cryptographic protocols** as an alternative to quadratic multi-party computation designs.

---
[[FL]]
[[PET]]
[[Machine Learning|ML]]
