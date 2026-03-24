---
title: UniKGQA - Unified retrieval and reasoning for solving multi-hop question answering over knowledge graph
created: Friday 9th February 2024 09:52
aliases:
tags:
  - ai
  - llm
  - knowledge-graph
---
- https://arxiv.org/pdf/2212.00959.pdf
- https://github.com/RUCAIBox/UniKGQA
- Source: arxiv

---

# TL;DR

**UniKGQA** collapses KG subgraph retrieval and answer reasoning into a single **UniModel** with shared PLM parameters, outperforming pipeline baselines on WebQSP, CWQ, and MetaQA through joint end-to-end training.

# Summary

Multi-hop **knowledge graph question answering** (KGQA) traditionally separates subgraph retrieval and answer reasoning into a pipeline, causing error propagation between stages. **UniKGQA** collapses both into a single **UniModel** built on a pretrained language model that shares parameters across retrieval (finding relevant KG paths) and reasoning (reading paths to produce answers). Joint end-to-end training allows retrieval signals to inform reasoning and vice versa. On WebQSP, CWQ, and MetaQA benchmarks, UniKGQA outperforms pipeline and retrieval-only baselines, confirming that **joint optimization** of retrieval and reasoning is superior to staged approaches.

# Key contributions

1. Proposes **UniModel**, a single PLM-based model that shares parameters across subgraph retrieval and answer reasoning for KGQA.
2. Eliminates **error propagation** between retrieval and reasoning stages through joint end-to-end training.
3. Frames **subgraph retrieval as path scoring**, enabling differentiable integration with the reasoning component.
4. Outperforms pipeline baselines on **WebQSP, CWQ, and MetaQA** multi-hop benchmarks with a smaller overall model footprint.

# When to cite

1. When arguing that **unified retrieve-and-reason models** outperform modular pipelines for multi-hop KGQA.
2. When discussing **joint training** as preferable to staged approaches when retrieval and reasoning have complementary supervision signals.
3. When citing evidence that **KG path scoring** can be formulated as a sequence task compatible with PLM fine-tuning.
4. When designing systems where **multi-hop reasoning** benefits from retrieving full reasoning chains rather than individual KG triples.

---
[[LLM]]
[[Knowledge Graph|KG]]
[[Knowledge Graph]]
[[RAG]]
