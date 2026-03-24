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

# Summary

RAG system performance varies dramatically across retrieval strategies, yet direct experimental comparisons are scarce. ARAGOG benchmarks seven advanced techniques — **HyDE**, **LLM reranking**, **Sentence Window Retrieval**, **MMR**, Cohere Rerank, Multi-query, and Document Summary Index — against naive RAG using retrieval precision and answer similarity as metrics. **Sentence Window Retrieval** achieves the highest retrieval precision overall, while **HyDE and LLM reranking** significantly boost both metrics. MMR and Cohere Rerank show no meaningful advantage over the naive baseline, contradicting common assumptions.

# Main points

1. **Sentence Window Retrieval** achieves the best overall retrieval precision among all tested methods.
2. **HyDE and LLM reranking** significantly improve both retrieval precision and answer similarity.
3. **MMR and Cohere Rerank** show no measurable advantage over the naive RAG baseline.
4. **Multi-query approaches** underperform expectations across both evaluation metrics.
5. Both **retrieval precision and answer similarity** are necessary — optimizing one does not guarantee the other.

# Takeaways

1. **LLM reranking** is one of the highest-ROI improvements available for existing RAG pipelines.
2. Commonly recommended techniques like **MMR** may not justify their added complexity — always benchmark first.
3. **HyDE** (generating a hypothetical answer before retrieval) consistently earns its overhead across evaluations.
4. Retrieval precision and answer similarity **can diverge** — a system can retrieve well but still answer poorly.
5. Running a structured comparison on your own data is **more valuable** than trusting published rankings from different domains.

---
[[LLM]]
[[RAG]]
[[Generative AI]]
[[RAG-Fusion - a New Take on Retrieval-Augmented Generation]]
[[Retrieval-Augmented Generation for Large Language Models - A Survey]]
[[Precise Zero-Shot Dense Retrieval without Relevance Labels]]
