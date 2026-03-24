---
title: A benchmark to understand the role of knowledge graphs on large language models accuracy for question and answering on enterprise SQL databases
created: Friday 9th February 2024 09:49
aliases:
tags:
  - llm
  - knowledge-graph
  - SQL
  - gpt
---
- https://arxiv.org/pdf/2311.07509.pdf
- Source: arxiv

---

# Summary

Enterprise SQL databases are hard for **LLMs** to query accurately because schemas alone carry no business semantics. This benchmark uses an insurance-domain enterprise schema paired with an **ontology-based knowledge graph** layer to measure how much semantic context affects accuracy. Testing **GPT-4** with zero-shot prompting, direct SQL achieves only 16% accuracy, while posing the same questions over a knowledge graph representation reaches 54% — a threefold improvement — demonstrating that **semantic enrichment** is a decisive factor, not model capability alone.

# Main points

1. Zero-shot **GPT-4 on raw enterprise SQL** achieves only 16% question-answering accuracy.
2. Adding a **knowledge graph** representation over the same data triples accuracy to 54%.
3. Benchmark covers an **insurance-domain schema** with realistic enterprise reporting queries.
4. The KG layer supplies **ontology and mappings**, not extra training data or fine-tuning.
5. Results suggest current **text-to-SQL benchmarks** underrepresent real enterprise complexity.

# Takeaways

1. Schema structure alone is insufficient context — **business ontologies** are a practical requirement for enterprise LLM Q&A.
2. Before investing in model upgrades, teams should evaluate whether **knowledge graph enrichment** closes more of the accuracy gap.
3. The 16 % baseline reveals that popular **text-to-SQL leaderboards** may be misleadingly optimistic for production settings.
4. **Ontology-to-SQL mappings** (R2RML / OBDA style) become a competitive engineering asset, not just a semantic-web artifact.
5. The benchmark methodology — isolated schema, controlled queries, measurable accuracy — is a reusable template for internal **LLM readiness assessments**.

---
[[LLM]]
[[Knowledge Graph]]
[[Prompt Engineering]]
[[RAG]]
[[Knowledge Graph Prompting for Multi-Document Question Answering]]
[[Unifying Large Language Models and Knowledge Graphs - A Roadmap]]
