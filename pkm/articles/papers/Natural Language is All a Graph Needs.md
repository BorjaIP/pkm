---
title:  Natural Language is All a Graph Needs
created: Monday 5th February 2024 19:50
aliases:
tags:
  - llm
  - knowledge-graph
---
- https://arxiv.org/pdf/2308.07134.pdf
- Source: arxiv

---

# TL;DR

**InstructGLM** serializes graph topology and node features as natural language instructions, unifying node classification, link prediction, and graph classification under a single LLM and matching or exceeding GNN baselines in zero-shot and few-shot settings.

# Summary

Graph machine learning tasks are typically solved with **graph neural networks** requiring task-specific architectures. **InstructGLM** serializes graph topology and node features as natural language instructions, reformulating all graph tasks as text generation problems solvable by a single **LLM**. On Cora, CiteSeer, and ogbn-arxiv benchmarks, InstructGLM matches or exceeds GNN baselines in zero-shot and few-shot regimes, demonstrating that **language models** can serve as general-purpose graph reasoners without graph-specific inductive bias.

# Key contributions

1. Proposes **InstructGLM**, which serializes graph structure and node features as natural language for LLM-based graph task solving.
2. Unifies **node classification, link prediction, and graph classification** under a single text-generation framework without task-specific architectures.
3. Demonstrates zero-shot and few-shot performance that **matches or exceeds GNN baselines** on standard benchmarks including ogbn-arxiv.
4. Shows that **instruction tuning** enables zero-shot transfer across graph task types without retraining.

# When to cite

1. When arguing that **LLMs can replace graph-specific architectures** when topology is serialized as natural language.
2. When discussing the use of **foundation models** to reduce specialized graph ML engineering across downstream tasks.
3. When citing evidence of **zero-shot transfer** from instruction-tuned LLMs to graph reasoning tasks.
4. When exploring the limits of **context-length** as the primary bottleneck for LLM-based graph processing at scale.

---
[[LLM]]
[[Knowledge Graph|KG]]
[[Knowledge Graph]]
[[NLP]]
