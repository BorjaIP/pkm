---
title:  ColBERTv2 - Effective and Efficient Retrieval via Lightweight Late Interaction
created: Monday 26th August 2024 10:06
aliases:
tags:
  - retrieval
  - dense-retrieval
  - late-interaction
  - embeddings
---
- https://arxiv.org/pdf/2112.01488
- https://github.com/IntelLabs/fastRAG/blob/main/examples/plaid_colbert_pipeline.ipynb
- Source: arxiv

---

# TL;DR

**ColBERTv2** combines **late interaction** scoring via MaxSim with **residual compression** of token embeddings, outperforming dense and sparse retrievers on MS-MARCO and BEIR while making large-scale deployment practical.

# Summary

**ColBERTv2** improves over ColBERT by combining **late interaction** with **residual compression** of document embeddings. Query and document tokens are encoded independently by BERT; relevance is scored via **MaxSim** — the sum of maximum cosine similarities between each query token and all document tokens. Residual compression reduces storage by representing each embedding as a centroid index plus a quantized residual, making large-scale deployment practical. It outperforms both dense and sparse retrievers on MS-MARCO and BEIR benchmarks without sacrificing retrieval quality.

# Key contributions

1. Introduces **residual compression** that encodes token embeddings as centroid index plus quantized residual, dramatically reducing storage.
2. Demonstrates that **late interaction via MaxSim** outperforms both bi-encoder and BM25 baselines on MS-MARCO and BEIR.
3. Shows that **document encodings precomputed offline** decouple indexing cost from query latency.
4. Establishes better **cross-domain generalization** on BEIR compared to single-vector dense retrieval.

# When to cite

1. When evaluating **late interaction retrieval** as a middle ground between expensive cross-encoders and coarse bi-encoders.
2. When discussing **residual compression** as a technique to scale token-level embeddings to production corpora.
3. When citing a retrieval model that generalizes well **across domains** without domain-specific fine-tuning.
4. When architecting **RAG systems** that precompute document embeddings offline to minimize query-time latency.

---
[[Artificial Intelligence|AI]]
[[LLM]]
[[RAG]]
[[VDB]]
[[PLAID - An Efficient Engine for Late Interaction Retrieval]]
