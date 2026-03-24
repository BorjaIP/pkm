---
title:  When Federated Learning Meets Blockchain - A New Distributed Learning Paradigm
created: Friday 2nd February 2024 11:17
aliases:
tags:
  - blockchain
  - fl
  - ml
---
- https://arxiv.org/pdf/2009.09338.pdf
- Source: arxiv

---

# TL;DR

This paper proposes replacing the trusted central server in federated learning with a **blockchain** aggregation layer using smart contracts, reputation-based client selection, and token incentives to achieve decentralized, Byzantine-tolerant model training.

# Summary

Standard federated learning depends on a trusted central server — a single point of failure for trust and auditability. This paper replaces it with a **blockchain** layer where **smart contracts** automate model aggregation and record updates as immutable transactions. **Reputation-based client selection** filters Byzantine participants before aggregation, and a **token incentive** mechanism encourages honest gradient contributions. Evaluated on image classification, the system matches centralized FL accuracy while adding auditability and removing the central trust assumption.

# Key contributions

1. Proposes replacing the FL central server with a **blockchain aggregation layer** using smart contracts for coordination.
2. Introduces **reputation-based client selection** as a Byzantine filtering mechanism before gradient aggregation.
3. Demonstrates a **token incentive** system that sustains honest participation in open federated networks.
4. Shows that decentralized aggregation achieves accuracy **comparable to centralized FL** on image classification benchmarks.

# When to cite

1. When proposing **trustless or decentralized federated learning** architectures for regulated or adversarial settings.
2. When discussing **smart contracts** as transparent, auditable coordination mechanisms for ML aggregation.
3. When evaluating **incentive mechanisms** for sustaining honest participation in open FL networks.
4. When comparing **reputation-based Byzantine filtering** against cryptographic Byzantine defenses in FL.

---
[[FL]]
[[PET]]
[[Blockchain]]
[[Machine Learning|ML]]
