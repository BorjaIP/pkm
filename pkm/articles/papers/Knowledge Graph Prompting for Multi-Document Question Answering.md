---
title:  Knowledge Graph Prompting for Multi-Document Question Answering
created: Friday 10th May 2024 11:53
aliases:
tags:
  - knowledge-graph
  - multi-hop-qa
  - retrieval
  - llm
---
- https://arxiv.org/pdf/2308.11730
- Source: arxiv

---

# TL;DR

**KGP (Knowledge Graph Prompting)** constructs a document-level knowledge graph from input passages and uses graph traversal to select minimal relevant subgraphs as structured LLM context, outperforming flat retrieve-then-read baselines on multi-hop QA.

# Summary

Flat retrieval fragments the reasoning chains needed for multi-hop questions by returning disconnected chunks. KGP addresses this by building a **document-level knowledge graph** offline, linking named entities, co-references, and discourse relations across all passages. At query time, **graph traversal** selects the minimal relevant subgraph, which is serialized and passed to an LLM graph-reader as structured context. This approach outperforms flat retrieve-then-read baselines on MuSiQue, 2WikiMultiHopQA, and **HotpotQA**, with the largest gains on questions requiring cross-document reasoning chains.

# Key contributions

1. Proposes **KGP**, a document-level KG construction method that links entities, co-references, and discourse relations across passages for multi-hop QA.
2. Introduces **graph traversal as a retrieval mechanism** that enforces logical connectivity between evidence pieces, replacing unstructured chunk retrieval.
3. Demonstrates superior performance over retrieve-then-read baselines on **MuSiQue, 2WikiMultiHopQA, and HotpotQA**.
4. Shows that **discourse relation extraction** during indexing pays dividends when queries require cross-document reasoning.

# When to cite

1. When building a **multi-hop QA system** and arguing that graph-based retrieval outperforms flat dense retrieval.
2. When justifying **document-level KG construction** as a preprocessing step for long-document RAG.
3. When using a **knowledge graph as a structured intermediate representation** for LLM context rather than a specialized model input.
4. When arguing that **cross-document reasoning chains** are better assembled by graph traversal than by dense chunk retrieval.

---
[[Artificial Intelligence|AI]]
[[LLM]]
[[RAG]]
[[Knowledge Graph|KG]]
[[Knowledge Graph]]
[[NLP]]
[[A benchmark to understand the role of knowledge graphs on large language models accuracy for question and answering on enterprise SQL databases]]
