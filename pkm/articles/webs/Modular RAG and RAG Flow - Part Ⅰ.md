---
title:  Modular RAG and RAG Flow - Part Ⅰ
created: Saturday 12th April 2025 21:10
aliases: 
tags:
  - rag
  - retrieval
  - indexing
  - query-expansion
  - chunking
---
- https://medium.com/@OpenRAG/modular-rag-and-rag-flow-part-%E2%85%B0-e69b32dc13a3
- Type: article
- Source: Medium · OpenRAG (authors of the RAG survey) · Jan 2024

---

# TL;DR

Modular RAG organises a [[RAG]] system as **module types → modules → operators** (6 types, 14 modules, 40+ operators), and a concrete pipeline is a **RAG Flow** built by combining them.

# Summary

Naive and chain-style Advanced RAG no longer describe the field: RAG now covers structured data, fine-tuned retrievers, multi-round retrieval and LLM-decided retrieval. The article proposes a three-tier modular paradigm in which Advanced RAG is a modular form and Naive RAG a special case. Part I walks through the first module types, **indexing**, **pre-retrieval** and **retrieval**, listing the techniques for each. Part II (flows and industry cases) is a separate note.

# Key takeaways

1. **Indexing**: balance chunk size with **sliding window**, **small-to-big** (retrieve small, synthesise from the parent), summary indexes and **metadata attachment**; add hierarchical or knowledge-graph structure.
2. **Pre-retrieval query expansion**: multi-query, sub-query (least-to-most decomposition) and Chain-of-Verification to reduce hallucination.
3. **Pre-retrieval query transformation**: LLM **rewrite**, **HyDE** (embed a hypothetical answer instead of the query) and **step-back prompting**.
4. **Routing and construction**: metadata or semantic routers pick the pipeline; text-to-SQL and text-to-Cypher reach structured sources.
5. **Retrieval**: choose retrievers by efficiency, embedding quality and task alignment; consult the MTEB leaderboard, and keep sparse retrievers for stability.
6. **Keep the user's intent**: weight the original query more when using several queries.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[RAG]] | System being decomposed |
| [[Knowledge Graph]] | Organises documents hierarchically and consistently |
| [[Precise Zero-Shot Dense Retrieval without Relevance Labels\|HyDE paper]] | Source of the hypothetical-document idea |
| [[Knowledge Graph Prompting for Multi-Document Question Answering\|KGP]] | KG-based multi-document QA |
| LlamaIndex, Neo4j, Semantic Router | Implementations referenced |

# When to use

1. When you need a **taxonomy of RAG techniques** to pick the next improvement.
2. When choosing between **query rewriting, HyDE, step-back or sub-queries**.
3. When designing **chunking and indexing** (small-to-big, metadata, hierarchy).

# Caveats

- High-level survey style: techniques are named with references but not benchmarked here.
- Flows and industry cases are covered in [[Modular RAG and RAG Flow - Part II]].

---
[[RAG]] [[LLM]] [[Knowledge Graph]] [[VDB]]
[[LLM RAG Paradigms - Naive RAG, Advanced RAG & Modular RAG]]
[[Retrieval-Augmented Generation for Large Language Models - A Survey]]
[[Solving the out-of-context chunk problem for RAG]]
[[Forget RAG, the Future is RAG-Fusion]]
