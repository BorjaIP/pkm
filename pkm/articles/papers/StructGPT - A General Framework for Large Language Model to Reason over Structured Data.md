---
title: StructGPT - A General Framework for Large Language Model to Reason over Structured Data
created: Friday 9th February 2024 09:51
aliases:
tags:
  - llm
  - gpt
  - knowledge-graph
  - structured-data
---
- https://arxiv.org/pdf/2305.09645.pdf
- https://github.com/RUCAIBox/StructGPT
- Source: arxiv

---

# TL;DR

**StructGPT** introduces an Iterative Reading-then-Reasoning (IRR) framework that enables LLMs to query tables, knowledge graphs, and databases through specialized reading interfaces without any fine-tuning.

# Summary

LLMs cannot directly query structured data sources, and single-shot context stuffing loses structure and exceeds context limits. StructGPT addresses this with an **Iterative Reading-then-Reasoning (IRR)** loop: specialized **reading interfaces** extract relevant rows, triples, or schema elements from tables, KGs, or databases, which are passed as context to the LLM for a reasoning step; the loop repeats until an answer is produced. Evaluated on WikiTableQuestions, WebQSP, and BIRD, it rivals **fine-tuned baselines** across all three structured QA settings without any model fine-tuning.

# Key contributions

1. Proposes the **IRR (Iterative Reading-then-Reasoning)** loop as a unified framework for LLM reasoning over heterogeneous structured data.
2. Introduces modular **reading interfaces** specialized for tables, knowledge graphs, and SQL databases under a single architecture.
3. Demonstrates that **iterative retrieval** over structured sources rivals fine-tuned models without any gradient updates to the LLM.
4. Shows the framework generalizes across WikiTableQuestions, **WebQSP** (KG), and BIRD (database) benchmarks.

# When to cite

1. When enabling an LLM to reason over **structured data sources** (tables, KGs, databases) without fine-tuning.
2. When arguing that **iterative structured retrieval** outperforms single-shot context stuffing for complex QA.
3. When designing **modular reading interfaces** for heterogeneous data formats under a unified LLM reasoning framework.
4. When comparing zero-shot LLM approaches to **fine-tuned baselines** on structured question answering.

---
[[LLM]]
[[GPT]]
[[Knowledge Graph]]
