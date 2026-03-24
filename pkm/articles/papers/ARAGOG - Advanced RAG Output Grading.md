---
title:  ARAGOG - Advanced RAG Output Grading
created: Tuesday 14th May 2024 17:22
aliases:
tags:
  - llm
  - rag
  - ml
---
- https://arxiv.org/pdf/2404.01037
- https://github.com/predlico/ARAGOG
- Source: arxiv

---

# TL;DR

**ARAGOG** benchmarks seven advanced RAG retrieval techniques head-to-head, finding that **Sentence Window Retrieval** achieves the best precision and that MMR and Cohere Rerank offer no advantage over naive RAG.

# Summary

RAG system performance varies dramatically across retrieval strategies, yet direct experimental comparisons are scarce. ARAGOG benchmarks seven advanced techniques — **HyDE**, **LLM reranking**, **Sentence Window Retrieval**, MMR, Cohere Rerank, Multi-query, and Document Summary Index — against naive RAG using retrieval precision and answer similarity as metrics. Sentence Window Retrieval achieves the highest retrieval precision overall, while **HyDE and LLM reranking** significantly boost both metrics. MMR and Cohere Rerank show no meaningful advantage over the naive baseline, contradicting common assumptions.

# Key contributions

1. Provides the first **head-to-head controlled comparison** of seven advanced RAG retrieval strategies under identical conditions.
2. Demonstrates that **Sentence Window Retrieval** achieves the highest overall retrieval precision among tested methods.
3. Establishes that **HyDE and LLM reranking** are among the highest-ROI improvements for existing RAG pipelines.
4. Shows that **MMR and Cohere Rerank** offer no measurable advantage over the naive RAG baseline, contradicting widespread assumptions.
5. Introduces dual evaluation using both **retrieval precision and answer similarity**, showing the two metrics can diverge.

# When to cite

1. When choosing which **advanced RAG technique** to prioritize for a new or existing pipeline.
2. When arguing that commonly recommended techniques like **MMR** may not justify their added complexity without empirical validation.
3. When supporting the use of **LLM reranking or HyDE** as high-value RAG enhancements with experimental backing.
4. When motivating **controlled benchmarking** of retrieval strategies on domain-specific data before deployment.

---
[[LLM]]
[[RAG]]
[[Generative AI]]
[[RAG-Fusion - a New Take on Retrieval-Augmented Generation]]
[[Retrieval-Augmented Generation for Large Language Models - A Survey]]
[[Precise Zero-Shot Dense Retrieval without Relevance Labels]]
