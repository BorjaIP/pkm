---
title:  Modular RAG and RAG Flow - Part II
created: Saturday 12th April 2025 21:10
aliases: 
tags:
  - rag
  - retrieval
  - fine-tuning
  - llm
---
- https://medium.com/@OpenRAG/modular-rag-and-rag-flow-part-ii-77b62bf8a5d3
- Type: article
- Source: Medium · OpenRAG (authors of the RAG survey) · Jan 2024

---

# TL;DR

Part II turns the Modular RAG modules into concrete **RAG Flows**: 3 fine-tuning patterns, 4 inference patterns (sequential, conditional, branching, loop) and 3 industry examples.

# Summary

With modules and operators defined in [[Modular RAG and RAG Flow - Part Ⅰ]], any [[RAG]] system can be described as a flow of operators. The tuning stage has retriever, generator and dual fine-tuning (RA-DIT). The inference stage has sequential flows (Naive and Advanced RAG, Rewrite-Retrieve-Read), conditional flows driven by a router, branching flows (multi-query before retrieval, parallel generation after, REPLUG) and loops (iterative ITER-RETGEN, recursive ToC, adaptive FLARE and Self-RAG). OpenAI, Baichuan and Databricks illustrate real stacks.

# Key takeaways

1. **Retriever fine-tuning**: direct tuning of a dense retriever, adapter modules when the embedding API is closed, LM-supervised retrieval, and RL with LLM reward.
2. **Generator fine-tuning**: direct tuning on domain data and formats, GPT-4 distillation into open models, and RLHF or LLM-judge feedback.
3. **Dual fine-tuning** coordinates retriever and generator together (RA-DIT).
4. **Sequential flows** are the most common: query rewrite or HyDE before retrieval and rerank after.
5. **Conditional flows** use a router (for example Semantic Router) to pick different pipelines by question type.
6. **Branching flows** run parallel branches before retrieval (multi-query) or after (one query, parallel generation, REPLUG).
7. **Loop flows**: iterative (fixed rounds), recursive (each step deepens the query) and adaptive, where the model decides when to retrieve (prompt-based FLARE, tuning-based Self-RAG with special tokens).
8. **OpenAI demo**: accuracy rose from 45% to 65% by tuning chunking and embeddings, 85% with reranking and question-type handling, and 98% with prompt engineering and query expansion (as reported by the authors, not an official OpenAI result).
9. **Baichuan**: decomposes queries, runs hybrid sparse and dense retrieval with a reranker, adds self-critique; **Databricks** adds a structured-data pipeline to the usual unstructured one.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[RAG]] | Systems described as flows |
| [[Toolformer - Language Models Can Teach Themselves to Use Tools\|Toolformer]] | Origin of tuning-based special tokens |
| [[RAFT - Adapting Language Model to Domain Specific RAG\|RAFT]] | Related joint adaptation work |
| [[Retrieval-Augmented Generation for Large Language Models - A Survey]] | The survey behind the taxonomy |
| [[RAG-Fusion - a New Take on Retrieval-Augmented Generation\|RAG-Fusion]] | Branching with multi-query |

# When to use

1. When you need **patterns for composing RAG pipelines** (sequential, conditional, branching, loop).
2. When deciding **what to fine-tune**: retriever, generator or both.
3. When looking for examples of **adaptive retrieval** such as FLARE and Self-RAG.

# Caveats

- The Baichuan section is partly speculative (the author says details are not public) and the OpenAI figures come from a demo-day talk.

---
[[RAG]] [[LLM]] [[Generative AI]]
[[Modular RAG and RAG Flow - Part Ⅰ]]
[[LLM RAG Paradigms - Naive RAG, Advanced RAG & Modular RAG]]
[[Retrieval-Augmented Generation for Large Language Models - A Survey]]
[[Forget RAG, the Future is RAG-Fusion]]
