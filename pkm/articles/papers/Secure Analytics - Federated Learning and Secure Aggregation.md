---
title:  Secure Analytics - Federated Learning and Secure Aggregation
created: Friday 28th July 2023 08:56
aliases:
tags:
  - fl
  - pet
---
- https://inst.eecs.berkeley.edu/~cs261/fa18/scribe/10_15.pdf
- Source: berkeley

---

# TL;DR

These lecture notes establish **Shamir secret sharing** as the foundational primitive for secure aggregation in federated learning under an honest-but-curious server threat model, covering the tradeoffs between communication overhead, dropout tolerance, and cryptographic security.

# Summary

Federated learning requires aggregating model gradients from many clients without the server learning individual updates. These notes introduce **Shamir secret sharing** as the core mechanism: each client splits its gradient into shares distributed across peers, allowing the server to reconstruct only the **aggregate gradient**. The honest-but-curious server threat model defines the security boundary. Coverage includes the inherent tension between **dropout tolerance** (which requires a minimum share threshold) and security strength, plus communication overhead as a function of client count and sharing degree.

# Key contributions

1. Establishes the **honest-but-curious server** threat model as the standard baseline for secure aggregation analysis.
2. Introduces **Shamir secret sharing** as the foundational primitive enabling private gradient aggregation in FL.
3. Shows that **dropout tolerance** requires a minimum reconstruction threshold that trades off directly with security strength.
4. Analyzes **communication overhead** as a function of client count and secret sharing degree, providing a scaling reference.

# When to cite

1. When introducing **Shamir secret sharing** as the basis for understanding secure aggregation protocols.
2. When explaining the **honest-but-curious threat model** and its limitations for adversarial FL settings.
3. When discussing the fundamental tradeoff between **dropout tolerance and security guarantees** in secret sharing.
4. When establishing baseline communication cost for **secure aggregation** before comparing optimized protocols.

---
[[FL]]
[[PET]]
[[Machine Learning|ML]]
