---
title:  Solving the out-of-context chunk problem for RAG
created: Saturday 12th April 2025 21:11
aliases: 
tags:
  - rag
  - retrieval
  - chunking
  - embeddings
---
- https://archive.ph/6fMOM
- Type: article
- Source: D-Star (d-star.ai) blog · captured Jul 2024

---

# TL;DR

Prepend **contextual chunk headers** and merge relevant neighbours into dynamic **segments** so [[RAG]] stops retrieving chunks that make no sense on their own.

# Summary

Chunks lose meaning when they use pronouns, split a thought mid-way, or only make sense inside their section. Two combined techniques fix most cases. First, an LLM splits the document into **semantically cohesive sections**, and each chunk is embedded and reranked with a header (document title, section title, optionally a summary). Second, chunk relevance scores are turned into values by subtracting a threshold and the best contiguous run is returned as a **segment**, a maximum-subarray problem. Demonstrated on Nike's 2023 10-K.

# Key takeaways

1. **Add contextual chunk headers**: embed and rerank `header + chunk` (title, section titles or a short document summary) so implicit references resolve.
2. **Section the document with an LLM**: number the lines, ask for start and end of each cohesive section (a few paragraphs to a few pages), then chunk inside sections.
3. **Return segments, not chunks**: value = relevance minus `irrelevant_chunk_penalty` (~0.2 works well); the best contiguous run maximises total value (maximum subarray).
4. **Tune segment length with the penalty**: lower values give longer segments, higher values shorter ones.
5. **Gain robustness**: low-scored chunks sandwiched between relevant ones get included, softening ranker mistakes.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[RAG]] | Pipeline whose chunking is improved |
| [[VDB]] | Holds the chunk embeddings |
| [[LLM]] | Performs semantic sectioning |
| dsRAG | Open-source retrieval engine implementing both ideas, plus a LangChain retriever |

# When to use

1. When RAG answers fail because **chunks lack context** (pronouns, mid-thought splits).
2. When choosing **chunk size** for both factoid and broad questions.
3. When designing **long-document retrieval** such as financial filings.

# Caveats

- One worked example (a single 10-K and query); no benchmark numbers.
- Sectioning with an LLM adds indexing cost and latency.

---
[[RAG]] [[LLM]] [[VDB]]
[[LLM RAG Paradigms - Naive RAG, Advanced RAG & Modular RAG]]
[[Better RAG results with Reciprocal Rank Fusion and Hybrid Search]]
[[Retrieval-Augmented Generation for Large Language Models - A Survey]]
