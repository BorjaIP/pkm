---
title:  LLMs Will Always Hallucinate, and We Need to Live With This
created: Saturday 12th October 2024 17:51
aliases:
tags:
  - llm
  - ml
---
- https://arxiv.org/pdf/2409.05746
- Source: arxiv

---

# TL;DR

This position paper proves that **hallucination** is a mathematically inevitable property of any sufficiently expressive generative model trained on finite data, and advocates for hallucination-aware deployment over elimination strategies.

# Summary

Hallucination in LLMs is widely treated as a correctable bug, but this paper argues it is an inherent mathematical property. Any sufficiently expressive generative model trained on finite data must produce hallucinations on **out-of-distribution inputs** — this is proven, not merely claimed. **RAG** and fine-tuning reduce frequency but cannot eliminate the phenomenon. The paper advocates for **hallucination-aware deployment**: uncertainty quantification, graceful degradation, and user interfaces that surface model confidence rather than projecting false certainty.

# Key contributions

1. Establishes a **formal proof** that hallucination is mathematically inevitable in any expressive generative model trained on finite data.
2. Demonstrates that **RAG and fine-tuning** reduce hallucination frequency but cannot provide formal elimination guarantees.
3. Proposes **uncertainty quantification** as a practical and necessary mitigation for surfacing unreliable outputs in production.
4. Argues for **hallucination-aware UI design** that communicates model confidence to enable informed user decisions.

# When to cite

1. When arguing that **hallucination cannot be fully eliminated** and must be managed rather than solved.
2. When justifying the inclusion of **uncertainty quantification** as a standard component of production LLM systems.
3. When warning that **RAG should not be presented as a hallucination-free solution** despite reducing frequency.
4. When motivating research into **formal theoretical bounds** on hallucination rates.

---
[[LLM]]
[[RAG]]
[[Machine Learning|ML]]
