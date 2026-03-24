---
title:  Improving Knowledge Graph Embedding Using Simple Constraints
created: Monday 5th February 2024 19:56
aliases:
tags:
  - knowledge-graph
  - ml
---
- https://arxiv.org/pdf/1805.02408.pdf
- Source: arxiv

---

# TL;DR

Injecting **entity type constraints** and **non-negativity constraints** into existing KG embedding models consistently improves link prediction accuracy on FB15k-237 and WN18RR with minimal added complexity.

# Summary

**Knowledge graph embedding** models like TransE and DistMult suffer from scoring invalid entity candidates during link prediction. This ACL 2018 paper injects two simple ontological constraints: **entity type constraints** that filter candidates incompatible with a relation's domain/range, and **non-negativity constraints** on entity embeddings that improve interpretability by enforcing a parts-based representation. Evaluated on FB15k-237 and WN18RR, constraint-enhanced models consistently outperform unconstrained counterparts, demonstrating that structural ontological knowledge is a low-cost, high-impact signal for **KG completion**.

# Key contributions

1. Introduces **entity type constraints** that eliminate invalid candidates during link prediction scoring using relation domain/range metadata.
2. Proposes **non-negativity constraints** on embeddings that encourage interpretable parts-based representations.
3. Demonstrates consistent improvement on **FB15k-237 and WN18RR** by applying constraints to existing models (TransE, DistMult) without architectural changes.
4. Establishes that **ontological metadata already in KGs** is a zero-cost source of inductive bias for embedding models.

# When to cite

1. When adding **type constraints** to knowledge graph embeddings as a model-agnostic quality improvement.
2. When arguing that **KG completion models routinely underuse** structured ontological metadata available in the graph.
3. When discussing **non-negativity regularization** as a technique that simultaneously improves accuracy and interpretability.
4. When motivating the use of **domain/range schema** in KG embedding to reduce the effective candidate search space.

---
[[Knowledge Graph|KG]]
[[Knowledge Graph]]
[[NLP]]
