---
title:  The Era of 1-bit LLMs - All Large Language Models are in 1.58 Bits
created: Wednesday 6th March 2024 18:30
aliases:
tags:
  - llm
  - ml
---
- https://arxiv.org/pdf/2402.17764.pdf
- Source: arxiv

---

# TL;DR

**BitNet b1.58** quantizes every LLM weight to {-1, 0, +1}, achieving perplexity parity with full-precision models at 3B+ parameters while eliminating all matrix multiplications from inference.

# Summary

High-precision weights have been assumed necessary for LLM quality, but BitNet b1.58 challenges this by constraining every weight to **{-1, 0, +1}** — averaging 1.58 bits per parameter. Inference kernels rely exclusively on addition and subtraction, eliminating multiplications entirely. **Perplexity parity** with FP16/BF16 baselines is achieved at the 3B parameter scale. Memory bandwidth, energy consumption, and latency are dramatically reduced, opening a viable path to deploying large models on **hardware without fast floating-point units**.

# Key contributions

1. Proposes **BitNet b1.58**, a training-time 1.58-bit quantization scheme using the {-1, 0, +1} ternary weight set.
2. Introduces **NF4-style information-theoretic justification** for the ternary constraint as optimal for normally distributed weights.
3. Demonstrates **perplexity parity** with full-precision LLMs at the 3B+ parameter scale.
4. Shows that inference requires only **addition and subtraction**, enabling deployment on multiplication-free hardware.
5. Establishes that **training-time quantization** (not post-training) is essential for preserving model quality at this precision level.

# When to cite

1. When arguing that **1-bit or ternary quantization** can match full-precision quality at sufficient scale.
2. When justifying **edge or low-power deployment** of large models without floating-point hardware.
3. When discussing the role of **implicit sparsity** (zero weights) in reducing effective inference compute.
4. When comparing **training-time versus post-training quantization** for preserving model quality.

---
[[LLM]] [[Machine Learning]]
