---
title:  PUMA - secure inference of LLaMa 7B in five minutes
created: Tuesday 25th July 2023 15:39
aliases:
tags:
  - llm
  - pet
  - ml
---
- https://arxiv.org/pdf/2307.12533.pdf
- Source: arxiv

---

# TL;DR

**PUMA** achieves secure two-party inference of LLaMA 7B in under five minutes by designing specialized secret-sharing protocols for transformer non-linear operations (GeLU, softmax, LayerNorm), delivering a 2-6x speedup over prior secure inference systems.

# Summary

Secure inference of large language models requires computing non-linear operations — **GeLU**, **softmax**, and **LayerNorm** — under cryptographic guarantees, which is prohibitively expensive under generic protocols. PUMA addresses this by combining **homomorphic encryption** and **secret sharing** with specialized protocols tuned to each non-linear function in transformer architectures. The result is full **LLaMA 7B** inference in under five minutes on commodity hardware, achieving a 2-6x speedup over prior secure inference systems without weakening privacy guarantees, making secure LLM serving practically feasible for sensitive applications.

# Key contributions

1. Proposes **PUMA**, a secure two-party inference system with specialized cryptographic protocols for each transformer non-linearity.
2. Introduces optimized **secret sharing protocols** for GeLU, softmax, and LayerNorm that are far more efficient than generic circuits.
3. Demonstrates full **LLaMA 7B** secure inference in under five minutes on commodity hardware.
4. Achieves **2-6x speedup** over prior secure inference systems without degrading cryptographic security guarantees.

# When to cite

1. When proposing **privacy-preserving LLM inference** and needing a practical latency baseline.
2. When discussing why **non-linear operations** (GeLU, softmax, LayerNorm) are the bottleneck in secure transformer inference.
3. When comparing **homomorphic encryption vs. secret sharing** tradeoffs for LLM inference tasks.
4. When arguing that **secure two-party inference** is now practically feasible for 7B-parameter language models.

---
[[LLM]]
[[PET]]
[[Machine Learning|ML]]
[[Artificial Intelligence|AI]]
