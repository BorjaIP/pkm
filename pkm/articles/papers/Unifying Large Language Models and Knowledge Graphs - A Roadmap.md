---
title: Unifying Large Language Models and Knowledge Graphs - A Roadmap
created: Friday 9th February 2024 08:43
aliases:
tags:
  - llm
  - ai
  - knowledge-graph
---
- https://arxiv.org/pdf/2306.08302.pdf
- https://github.com/RManLuo/Awesome-LLM-KG
- Source: arxiv

---

# TL;DR

A roadmap survey that structures **LLM-KG integration** into three paradigms — KG-enhanced LLMs, LLM-augmented KGs, and Synergized LLM+KG — and identifies open challenges for each direction.

# Summary

LLMs suffer from hallucination and knowledge staleness; knowledge graphs are expensive to build and hard to query flexibly. This survey defines three integration paradigms: **KG-enhanced LLMs** inject structured knowledge to reduce hallucination; **LLM-augmented KGs** use language models for automated KG construction and completion; and **Synergized LLM+KG** enables bidirectional mutual enhancement. Methods, datasets, and benchmarks are reviewed for each paradigm. Open challenges include temporal knowledge drift, scalability of **symbolic grounding**, and reliable retrieval-augmented factual reasoning over large KGs.

# Key contributions

1. Proposes a **three-paradigm taxonomy** (KG-enhanced LLMs, LLM-augmented KGs, Synergized LLM+KG) as a unifying framework for the field.
2. Establishes **KG grounding** as the most practical current path to reducing LLM hallucination in factual tasks.
3. Demonstrates that **LLMs can automate KG construction** pipelines, lowering the cost of maintaining structured knowledge.
4. Identifies temporal reasoning and **multi-hop RAG over large KGs** as the weakest evaluation areas and primary open challenges.

# When to cite

1. When positioning a system that combines **LLMs and knowledge graphs** and needing a taxonomy to classify the approach.
2. When justifying **KG grounding** as a hallucination-reduction strategy for factual generation tasks.
3. When arguing that **LLMs can reduce the cost of KG construction** through automated extraction or completion.
4. When identifying gaps in **benchmark coverage** for temporal or multi-hop KG reasoning.

---
[[LLM]]
[[Knowledge Graph|KG]]
[[Knowledge Graph]]
[[NLP]]
[[RAG]]
[[Prompt Engineering]]
