---
title:  RAG-Fusion - a New Take on Retrieval-Augmented Generation
created: Friday 10th May 2024 11:12
aliases:
tags:
  - rag
  - retrieval
  - query-expansion
  - rank-fusion
---
- https://arxiv.org/html/2402.03367v2
- Source: arxiv

---

# TL;DR

**RAG-Fusion** generates multiple semantically diverse query variants via an LLM and merges their ranked retrieval lists using **Reciprocal Rank Fusion**, producing more robust context than single-query RAG.

# Summary

**RAG-Fusion** extends standard RAG by generating multiple semantically diverse query variants from the original user query using an LLM. Each variant retrieves its own ranked document list; the lists are then merged using **Reciprocal Rank Fusion (RRF)**, which promotes documents that rank consistently across multiple perspectives. The fused ranking surfaces more comprehensive and robust context than single-query retrieval, reducing sensitivity to query phrasing and improving downstream QA accuracy.

# Key contributions

1. Proposes **RAG-Fusion**, combining LLM-based multi-query generation with **Reciprocal Rank Fusion** to improve retrieval robustness.
2. Demonstrates that **RRF** is a parameter-free rank aggregation method that straightforwardly improves any existing retrieval pipeline.
3. Shows that **query diversification** reduces brittleness of embedding-based retrieval without requiring thesauri or domain vocabulary.
4. Establishes that multi-query retrieval outperforms **single-query RAG** on QA benchmarks with minimal additional latency.

# When to cite

1. When implementing **multi-query retrieval** strategies to reduce sensitivity to query phrasing in RAG systems.
2. When applying **Reciprocal Rank Fusion** as a parameter-free method to aggregate ranked retrieval lists.
3. When discussing **query expansion** techniques that use an LLM rather than domain-specific vocabulary resources.
4. When evaluating the **latency-quality tradeoff** of multi-query retrieval approaches before deployment.

---
[[Artificial Intelligence|AI]]
[[LLM]]
[[RAG]]
[[Prompt Engineering]]
[[Retrieval-Augmented Generation for Large Language Models - A Survey]]
