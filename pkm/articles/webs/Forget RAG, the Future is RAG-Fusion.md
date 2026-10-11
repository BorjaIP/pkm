---
title:  Forget RAG, the Future is RAG-Fusion
created: Saturday 12th April 2025 21:09
aliases: 
tags:
  - rag
  - rank-fusion
  - query-expansion
  - retrieval
---
- https://archive.ph/PkpOd
- Type: article
- Source: Towards Data Science · Adrian H. Raudaschl · Oct 2023

---

# TL;DR

**RAG-Fusion** has an LLM write several variants of the user's query, searches each and merges the ranked lists with **Reciprocal Rank Fusion** before generating the answer.

# Summary

Plain [[RAG]] inherits the limits of vector and lexical search and of users who write vague or typo-ridden queries. RAG-Fusion adds two steps: **multi-query generation** (different angles on the same question) and **RRF reranking** of all result lists, then prompts the LLM with the fused documents plus all queries, weighting the original query most. The author argues RRF works because it ranks by position rather than score, and that blending lexical with vector results in this way gave him a "patchwork" instead.

# Key takeaways

1. **Generate sibling queries** with an LLM prompt so each explores a different perspective of the user's intent.
2. **Fuse by rank**: `score(d) = sum(1 / (k + rank))` over lists, with `k = 60`; no dependence on engine-specific score scales.
3. **Keep the original query dominant** in the final prompt to avoid intent dilution.
4. **Gain**: richer sources, implicit spell-fixing, decomposition of complex questions and serendipitous results.
5. **Watch the costs**: verbose answers, a crowded context window, and ethics of rewriting queries (show generated queries, let users toggle the feature).

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[RAG]] | Baseline being upgraded |
| [[RAG-Fusion - a New Take on Retrieval-Augmented Generation\|RAG-Fusion paper]] | Later academic write-up of the same idea |
| [[Elasticsearch]] / [[VDB]] | Search backends suggested for retrieval |
| [[LLM]] | Query generator and answer writer |
| [[Obsidian]] | The author's "Project Ramble" searches his own Obsidian notes |

# When to use

1. When improving recall with **multi-query retrieval**.
2. When you need the **RRF formula** and the rationale for rank-based merging.
3. When discussing **UX and transparency** of query rewriting.

# Caveats

- Member-only Medium post read through an archive snapshot; the claims are qualitative with no benchmark.
- The author notes mixing lexical and vector lists with RRF disappointed him, unlike the hybrid-search framing in [[Better RAG results with Reciprocal Rank Fusion and Hybrid Search]].

---
[[RAG]] [[LLM]] [[VDB]] [[Obsidian]]
[[RAG-Fusion - a New Take on Retrieval-Augmented Generation]]
[[Better RAG results with Reciprocal Rank Fusion and Hybrid Search]]
[[Hybrid Search a method to Optimize RAG implementation]]
