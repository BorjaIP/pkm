---
title:  Do we really need a specialized vector database
created: Monday 14th April 2025 20:59
aliases: 
tags:
  - vector-search
  - db
  - rag
  - embeddings
---
- https://archive.ph/MbAyx
- Type: article
- Source: Vendor blog · Ce Gao · Jun 2023

---

# TL;DR

Vector search is a **data type and index**, not a new kind of database, so for most [[RAG]] workloads a general-purpose database with vector support beats a separate vector store.

# Summary

[[VDB|Vector databases]] became the default "external memory" for LLMs because ten lines of code and an embedding API give you recall. The article argues the specialised system brings **data consistency** problems (syncing and deleting across two stores) and a restricted **query language and metadata filtering**. A naive benchmark of one million 256-dimensional vectors shows exact search taking about 50 ms, roughly 0.5% of a 10 s LLM call, so raw performance rarely decides the choice. Ease of operation and consistency do, where mature databases are ahead.

# Key takeaways

1. **Treat vectors as a column**: store embeddings next to your relational data and query them with SQL (an ivfflat index on a [[PostgreSQL]] table is the example).
2. **Avoid dual-write drift**: with a separate store, rows deleted in the primary database linger in the vector store.
3. **Question the performance argument**: exact Numpy search over 1M vectors costs ~50 ms against ~10 s for 7B-model inference, so retrieval latency is dwarfed by the LLM.
4. **Filter richly**: vector stores usually limit metadata types (string, number, list, boolean) and operators; SQL does not.
5. **Use ANN indexes** (e.g. HNSW) when scale demands it; trade space for time instead of O(n) scans.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[VDB]] | The specialised systems being questioned |
| [[PostgreSQL]] | General-purpose database used for the SQL vector example |
| [[Databases]] | Broader context (OLTP, OLAP, consistency) |
| Hnswlib, Numpy | Approximate vs exact search in the benchmark |
| OpenAI embeddings | Text-to-vector step in the sample code |

# When to use

1. When deciding **dedicated vector DB vs vector extension** for a RAG project.
2. When arguing about **consistency and operations cost** of an extra datastore.
3. When you need a rough **latency budget**: retrieval vs LLM inference.

# Caveats

- Vendor blog arguing for its own approach; the benchmark uses random vectors and ignores recall.
- Captured through an archive snapshot; the last section on implementing vector types in traditional databases was not read.

---
[[RAG]] [[VDB]] [[Databases]] [[PostgreSQL]] [[Elasticsearch]]
[[Better RAG results with Reciprocal Rank Fusion and Hybrid Search]]
[[SOAR - Improved Indexing for Approximate Nearest Neighbor Search]]
