---
title:  Graph agent - explicit reasoning agent for graphs
created: Monday 5th February 2024 19:57
aliases:
tags:
  - llm
  - knowledge-graph
  - agents
---
- https://arxiv.org/pdf/2310.16421v1.pdf
- Source: arxiv

---

# TL;DR

**Graph Agent** uses a multi-agent framework where a planner LLM decomposes complex graph questions into subgraph retrieval and reasoning sub-steps handled by specialized agents, outperforming few-shot GPT-4 on knowledge graph QA.

# Summary

Complex knowledge graph QA requires multi-hop traversal that monolithic LLM prompting cannot reliably handle. Graph Agent addresses this with a **multi-agent framework**: a **planner LLM** decomposes questions into subgraph retrieval and local reasoning sub-steps, while specialized sub-agents handle node/edge fetching independently from reasoning. The pipeline produces explicit intermediate reasoning chains, making it interpretable. On WebQSP and CWQ, it outperforms few-shot **GPT-4** and matches fine-tuned baselines using frozen models without graph-specific fine-tuning.

# Key contributions

1. Proposes a **multi-agent decomposition** framework where a planner LLM separates graph retrieval from reasoning into distinct specialized agents.
2. Demonstrates that **frozen LLMs with structured graph interfaces** can match fine-tuned baselines on knowledge graph QA.
3. Shows that **explicit intermediate reasoning steps** enable interpretable inspection and correction of graph traversal decisions.
4. Establishes that the **planner-executor pattern** from code agents transfers effectively to knowledge graph reasoning.

# When to cite

1. When building a **multi-agent system for knowledge graph QA** that requires multi-hop traversal.
2. When arguing that **separating graph retrieval from reasoning** improves precision and reduces context length.
3. When comparing **frozen LLM + graph interface** approaches against fine-tuned graph QA models.
4. When justifying **explicit intermediate steps** for interpretability in graph-based reasoning pipelines.

---
[[LLM]]
[[Knowledge Graph|KG]]
