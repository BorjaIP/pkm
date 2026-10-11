---
title:  Better RAG results with Reciprocal Rank Fusion and Hybrid Search
created: Saturday 12th April 2025 21:08
aliases: 
tags:
  - rag
  - retrieval
  - hybrid-search
  - rank-fusion
  - vector-search
---
- https://www.assembled.com/blog/better-rag-results-with-reciprocal-rank-fusion-and-hybrid-search
- Type: article
- Source: Assembled engineering blog · May 2024

---

# TL;DR

Combining **keyword and vector search** and merging their results with **Reciprocal Rank Fusion** fixes the keyword-blind spots of vector-only [[RAG]] without per-customer score tuning.

# Summary

Vector-only retrieval in a customer-support [[RAG]] system returned marketing and overview pages for specific queries like "features in a premium plan", because exact keywords were not weighted. Adding a **keyword index** next to the [[VDB|vector store]] fixed recall, but the two score scales were incomparable, so **weighted fusion** was dropped. **Reciprocal Rank Fusion (RRF)** merges the lists by *position* instead of score, which is simple, robust and needs almost no tuning. A common `DocumentStore` interface hides the merge from callers.

# Key takeaways

1. **Run keyword and vector search in parallel** and fuse them; ensembles beat a single retriever when queries mix exact terms and semantics.
2. **Fuse by rank, not by score**: each list gives a document `1/rank`, scores are summed per document and sorted. Documents found by several retrievers rise to the top.
3. **Avoid weighted score fusion** when similarity metrics (dot product, Euclidean) and score distributions differ across datasets; weights cannot be tuned per customer at scale.
4. **Hide the hybrid logic behind one `DocumentStore` interface**: the hybrid store wraps child stores, so merging is testable on its own.
5. **Keep a separate source of truth** (PostgreSQL metadata + S3 documents), update search stores asynchronously and retry failed syncs with exponential backoff (eventual consistency).

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[RAG-Fusion - a New Take on Retrieval-Augmented Generation\|RAG-Fusion]] | Same RRF merge, but over LLM-generated query variants instead of two retrievers |
| [[VDB]] | Pinecone for vector search; Milvus considered but not adopted |
| [[Elasticsearch]] | Self-managed keyword option, rejected in favour of Algolia |
| [[PostgreSQL]] / [[S3]] | Source of truth for document metadata and files |
| HyDE, embedding fine-tuning | Suggested next steps |

# When to use

1. When choosing how to **merge keyword and vector results** in a RAG pipeline.
2. When arguing why **rank fusion beats weighted score fusion** for heterogeneous retrievers.
3. When designing a **search-store abstraction** that can sync one corpus into several indexes.

# Caveats

- No benchmarks or metrics: "outperformed more complex methods" is a claim, not evidence.
- The RRF constant `k` (60 in the original literature) and any reranking step are not described.
- Vendor-managed stack (Pinecone + Algolia); the trade-offs may not hold for self-hosted setups.

---
[[RAG]] [[LLM]] [[VDB]] [[Elasticsearch]]
[[Hybrid Search a method to Optimize RAG implementation]]
[[RAG-Fusion - a New Take on Retrieval-Augmented Generation]]
[[Retrieval-Augmented Generation for Large Language Models - A Survey]]
