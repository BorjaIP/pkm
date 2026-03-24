---
title:  SOAR - Improved Indexing for Approximate Nearest Neighbor Search
created: Thursday 13th June 2024 10:31
aliases:
tags:
  - ann
  - vector-search
  - indexing
  - embeddings
---
- https://arxiv.org/pdf/2404.00774
- Source: arxiv

---

# TL;DR

**SOAR** (Spilling with Orthogonality-Amplified Residuals) recovers recall lost at partition boundaries in ANN indices by spilling boundary queries to neighboring partitions using orthogonality-weighted residuals.

# Summary

Partition-based **Approximate Nearest Neighbor (ANN)** indices systematically miss queries that fall near partition boundaries, since only the assigned partition is searched. SOAR augments these indices with a **residual spilling** mechanism: boundary queries are forwarded to neighboring partitions using residuals amplified by their angular deviation from the partition boundary — prioritizing the most informative spills. The technique is compatible with existing IVF-style indices as an augmentation layer and achieves superior **recall-latency tradeoffs** over ScaNN and HNSW on standard ANN benchmarks at matched latency budgets.

# Key contributions

1. Identifies **partition-boundary recall loss** as a systematic failure mode in standard ANN indices and proposes a targeted solution.
2. Introduces **residual spilling** as a mechanism to forward boundary queries to neighboring partitions without full reindexing.
3. Proposes **orthogonality amplification** as a principled weighting of residuals by angular deviation from partition boundaries.
4. Demonstrates superior **recall-latency tradeoffs** over ScaNN and HNSW on standard ANN benchmarks at matched latency.

# When to cite

1. When optimizing **ANN recall at fixed latency** and seeking alternatives to brute-force multi-probe search.
2. When augmenting an existing **IVF-style vector index** to recover recall at partition boundaries.
3. When comparing **vector search index designs** and needing a reference that beats ScaNN and HNSW on recall-latency curves.
4. When arguing that **boundary handling** in partitioned indices is a distinct optimization axis from quantization.

---
[[Artificial Intelligence|AI]]
[[VDB]]
[[RAG]]
