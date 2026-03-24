---
title:  Attention Is All You Need
created: Saturday 12th April 2025 18:00
aliases:
tags:
  - llm
  - ml
  - dl
---
- https://arxiv.org/pdf/1706.03762
- Source: arxiv

---

# TL;DR

The **Transformer** replaces recurrence and convolutions entirely with stacked **self-attention** layers, enabling full sequence parallelization and setting new state-of-the-art on machine translation.

# Summary

Sequence-to-sequence models relying on RNNs suffer from sequential computation that blocks parallelization and degrades on long-range dependencies. The Transformer architecture addresses this with **multi-head self-attention**: queries, keys, and values are projected into multiple subspaces and attended in parallel. **Positional encodings** (sinusoidal) preserve sequence order without recurrent state. An encoder-decoder structure with **cross-attention** links source and target. Trained on WMT14, it reached 28.4 BLEU (EN-DE) and 41.0 BLEU (EN-FR) at a fraction of prior compute cost.

# Key contributions

1. Introduces the **Transformer** — a sequence model built purely from attention and feedforward layers, with no recurrence or convolutions.
2. Proposes **multi-head attention** as the core building block, attending to multiple representation subspaces simultaneously.
3. Establishes **sinusoidal positional encoding** as a parameter-free way to inject sequence order into attention-based models.
4. Demonstrates that **full parallelization over sequence positions** reduces training time by orders of magnitude versus RNN baselines.
5. Shows state-of-the-art **BLEU scores** on WMT14 EN-DE and EN-FR with lower computational cost than all prior models.

# When to cite

1. When explaining the architectural foundation of any modern **LLM** (GPT, BERT, T5, and all descendants).
2. When arguing why **self-attention** is preferable to RNNs for capturing long-range dependencies.
3. When discussing **training efficiency** and why large-scale pretraining became feasible.
4. When introducing **multi-head attention** or **positional encoding** as concepts in a technical explanation.

---
[[LLM]] [[Artificial Intelligence|AI]] [[Generative AI]] [[Deep Learning]]
