---
title: Chameleon - Plug-and-Play Compositional Reasoning with Large Language Models
created: Monday 5th February 2024 19:44
aliases:
tags:
  - llm
  - tool-use
  - reasoning
---
- https://arxiv.org/pdf/2304.09842.pdf
- Source: arxiv

---

# TL;DR

**Chameleon** uses GPT-4 as a natural-language planner to compose heterogeneous tools — search, Python, vision models — plug-and-play, achieving 98.78% on TabMWP and 86.54% on ScienceQA without any task-specific fine-tuning.

# Summary

Chameleon uses **GPT-4** as a natural-language planner that synthesizes sequential programs composed of heterogeneous **tools**: search engines, Python interpreters, image captioners, and specialized models. Plans are generated in natural language and executed in order without task-specific fine-tuning. It achieves 86.54% on ScienceQA and 98.78% on **TabMWP**, surpassing prior state-of-the-art including fine-tuned models on both benchmarks.

# Key contributions

1. Proposes **Chameleon**, a plug-and-play compositional reasoning system where GPT-4 generates natural-language tool programs.
2. Introduces a **heterogeneous tool composition** approach combining search, code execution, and vision models under one planner.
3. Achieves state-of-the-art **98.78% on TabMWP** and **86.54% on ScienceQA** without any task-specific fine-tuning.
4. Demonstrates that **natural-language programs** are more interpretable than code-only tool-use pipelines and easier to extend.

# When to cite

1. When arguing that a strong **LLM planner** can coordinate heterogeneous tools without task-specific training.
2. When discussing **compositional reasoning** as a flexible alternative to monolithic end-to-end models.
3. When citing plug-and-play tool frameworks that handle **multimodal tasks** by combining vision and language tools.
4. When comparing natural-language planning approaches to code-generating tool-use systems like **ReAct or ART**.

---
[[LLM]]
[[GPT]]
[[Prompt Engineering]]
