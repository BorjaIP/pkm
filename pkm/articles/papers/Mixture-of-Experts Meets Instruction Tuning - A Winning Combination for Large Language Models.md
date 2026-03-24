---
title:  Mixture-of-Experts Meets Instruction Tuning - A Winning Combination for Large Language Models
created: Wednesday 6th March 2024 18:26
aliases:
tags:
  - llm
  - ml
---
- https://arxiv.org/pdf/2305.14705.pdf
- Source: arxiv

---

# TL;DR

Sparse **Mixture-of-Experts** and **instruction tuning** combine synergistically — MoE models finetuned on FLAN-style data outperform dense models of equivalent FLOPs by more than either technique achieves independently.

# Summary

Scaling dense models improves performance but at linear compute cost. Sparse **Mixture-of-Experts (MoE)** with top-2 routing increases parameter count without proportional FLOPs. When combined with **FLAN-style instruction tuning**, the gains exceed what either technique achieves independently, suggesting that MoE's per-token specialization amplifies the generalization benefits of diverse instruction data. **Chain-of-thought finetuning** further improves MoE models on reasoning tasks. Results hold across multiple model scales, confirming the combination's scaling robustness.

# Key contributions

1. Demonstrates a **synergistic interaction** between sparse MoE and instruction tuning that exceeds additive effects.
2. Shows that **top-2 expert routing** MoE models outperform FLOPs-matched dense models on FLAN benchmarks.
3. Establishes that **chain-of-thought finetuning** provides additional gains specifically for MoE models on reasoning tasks.
4. Confirms the combination's **scaling robustness** across multiple model sizes.

# When to cite

1. When justifying a **sparse MoE architecture** over a dense model under a fixed compute budget.
2. When arguing that **instruction tuning benefits are amplified** by MoE's conditional computation.
3. When designing an instruction tuning mix for MoE models and considering whether to include **chain-of-thought data**.
4. When evaluating models and needing to argue that **FLOPs-matched comparisons** are more meaningful than parameter-count comparisons.

---
[[LLM]] [[NLP]] [[Machine Learning]]
