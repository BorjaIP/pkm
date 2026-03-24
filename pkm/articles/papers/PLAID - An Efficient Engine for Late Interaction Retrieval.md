---
title:  PLAID - An Efficient Engine for Late Interaction Retrieval
created: Friday 23rd August 2024 10:47
aliases:
tags:
  - retrieval
  - late-interaction
  - serving
  - vector-search
---
- https://arxiv.org/pdf/2205.09707
- Source: arxiv

---

# TL;DR

**PLAID** is a serving engine for ColBERT that uses **centroid interaction** as a cheap pre-filter to prune irrelevant passages, achieving 4–7x latency reduction with no measurable loss in retrieval quality.

# Summary

**PLAID** (Performance-optimized Late Interaction Driver) is a serving engine for **ColBERT** that eliminates the bottleneck of full **MaxSim** computation over entire corpora. It introduces **centroid interaction** as a cheap pre-filter: query tokens are scored against cluster centroids first, pruning passages unlikely to be relevant before the expensive per-token scoring step. A subsequent candidate generation stage further narrows the set. The result is a 4–7x speedup over vanilla ColBERT with no measurable loss in retrieval quality, enabling late interaction at billion-scale.

# Key contributions

1. Introduces **centroid interaction** as a two-stage pre-filter that scores query tokens against cluster centroids before full MaxSim.
2. Achieves **4–7x latency reduction** versus vanilla ColBERT at identical recall levels on MS-MARCO.
3. Integrates directly with ColBERTv2's **residual-compressed index** without requiring reindexing.
4. Demonstrates that **late interaction retrieval** is viable at billion-scale corpora in production settings.

# When to cite

1. When discussing how to make **late interaction retrieval** practical at production scale and billion-document corpora.
2. When applying **centroid-based pruning** as a transferable pattern for speeding up multi-vector retrieval systems.
3. When arguing that **indexing and serving co-design** can unlock deployment of more expressive retrieval models.
4. When evaluating **ColBERT-based RAG pipelines** where retrieval latency is a bottleneck.

---
[[LLM]]
[[Artificial Intelligence|AI]]
[[VDB]]
[[RAG]]
[[ColBERTv2 - Effective and Efficient Retrieval via Lightweight Late Interaction]]
