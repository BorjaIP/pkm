---
title: "Ask, and it shall be given: On the Turing completeness of prompting"
created: Tuesday 1st April 2026 14:00
aliases:
tags:
  - llm
  - prompt-engineering
  - reasoning
  - transformer
  - theory
---
- https://arxiv.org/abs/2411.01992
- Source: arxiv

---

# TL;DR

A single **finite-size Transformer** is provably **Turing-complete under prompting**: for every computable function there exists a prompt that causes it to compute that function.

# Summary

Despite the enormous empirical success of the **LLM prompting paradigm** — one model, many tasks — no prior work had provided a theoretical foundation for it. This paper proves that prompting is **Turing-complete**: there exists a finite-size Transformer Γ such that for any computable function, a finite prompt encodes the function and Γ computes it on any input. Crucially, Γ is task-agnostic (fixed independently of the function) and the prompt is input-agnostic (fixed independently of the test input). The constructive proof goes through a novel intermediate model called **2-PTMs**, which are Turing-complete and encode compactly into prompts. The result further shows that this single Transformer matches, up to a log factor, the **CoT (chain-of-thought) complexity** and exactly matches the **precision complexity** of the entire class of unbounded-size Transformers — establishing efficient universality.

# Key contributions

1. **Proves Turing-completeness of prompting** — for every computable function ϕ, a finite prompt πϕ exists such that a fixed finite-size Transformer Γ computes ϕ(x) on all inputs x.
2. Introduces **2-PTMs** (a new computational model) that are Turing-complete and can be encoded into a finite alphabet prompt, bridging computation theory and prompt design.
3. Establishes **near-optimal CoT complexity**: Γ computes any TIME(t(n)) function in O(t(n) log t(n)) chain-of-thought steps, matching the class of all Transformers up to a log factor.
4. Shows **exact precision complexity parity**: Γ requires only O(log(n + t(n))) bits of precision — the same bound as the full class of Transformers, implying that any **P language** is decidable within log-precision by a single Transformer.
5. Provides a **simple constructive proof** (not just an existence argument) using ReLU activation, layer normalization, and causal attention in a decoder-only architecture.

# When to cite

1. When arguing theoretically **why prompt engineering works** — this paper provides the formal grounding that prompts can express any computable task.
2. When discussing the **expressivity and limits of Transformers** and why a single pretrained model can generalize to novel tasks zero-shot.
3. When comparing **one-model-many-tasks vs. one-model-one-task** paradigms and the computational power difference they imply.
4. When reasoning about **chain-of-thought length requirements** for a given computational class — the O(t(n) log t(n)) bound is a concrete theoretical baseline.

---
[[Attention Is All You Need]]
[[Prompting Frameworks for Large Language Models - A Survey]]
[[A Survey of Large Language Models]]
[[REACT - SYNERGIZING REASONING AND ACTING IN LANGUAGE MODELS]]
