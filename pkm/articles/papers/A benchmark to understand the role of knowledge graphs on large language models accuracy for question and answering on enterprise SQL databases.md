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

# TL;DR

An enterprise-domain benchmark shows that adding an **ontology-based knowledge graph** layer over SQL triples GPT-4 question-answering accuracy from 16% to 54% in zero-shot settings.

# Summary

Enterprise SQL databases are hard for **LLMs** to query accurately because schemas alone carry no business semantics. This benchmark uses an insurance-domain enterprise schema paired with an **ontology-based knowledge graph** to measure how much semantic context affects accuracy. Testing **GPT-4** with zero-shot prompting, direct SQL achieves only 16% accuracy while posing the same questions over a KG representation reaches 54%, demonstrating that **semantic enrichment** is a decisive factor independent of model capability.

# Key contributions

1. Introduces a benchmark using a **real enterprise insurance schema** to evaluate LLM question-answering accuracy.
2. Demonstrates a **threefold accuracy improvement** (16% → 54%) by adding a KG layer over the same raw SQL data.
3. Shows that **ontology and R2RML mappings** alone — without fine-tuning — supply sufficient semantic context for GPT-4.
4. Establishes that popular **text-to-SQL benchmarks** underrepresent real enterprise complexity.

# When to cite

1. When arguing that **knowledge graph enrichment** is more impactful than model upgrades for enterprise Q&A accuracy.
2. When supporting claims that **schema structure alone** is insufficient context for LLM-based SQL querying.
3. When motivating the use of **ontology-to-SQL mappings** (OBDA/R2RML) as a production engineering asset.
4. When benchmarking **LLM readiness** on domain-specific enterprise data with realistic query complexity.

---
[[LLM]]
[[Knowledge Graph]]
[[Prompt Engineering]]
[[RAG]]
[[Knowledge Graph Prompting for Multi-Document Question Answering]]
[[Unifying Large Language Models and Knowledge Graphs - A Roadmap]]
