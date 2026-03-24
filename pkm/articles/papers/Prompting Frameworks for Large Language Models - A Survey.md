---
title:  Prompting Frameworks for Large Language Models - A Survey
created: Friday 10th May 2024 15:53
aliases:
tags:
  - llm
  - prompt-engineering
---
- https://arxiv.org/pdf/2311.12785
- Source: arxiv

---

# TL;DR

This survey taxonomizes prompting techniques from chain-of-thought to ReAct and reviews 30+ tooling frameworks including LangChain, DSPy, and Guidance, providing a **comparison matrix** that maps framework capabilities to use-case requirements.

# Summary

The prompting landscape has grown rapidly from basic few-shot techniques to multi-step paradigms and a fragmented ecosystem of frameworks. This survey taxonomizes techniques into single-step and multi-step categories — including **chain-of-thought**, tree-of-thought, self-consistency, and **ReAct** — and reviews 30+ frameworks (LangChain, LlamaIndex, Guidance, LMQL, DSPy). A **comparison matrix** maps framework capabilities across prompt construction, chaining, memory, and evaluation. Emerging directions include **automatic prompt optimization** (DSPy-style) and structured generation as key open frontiers.

# Key contributions

1. Introduces a taxonomy organizing prompting techniques into single-step and multi-step categories across 30+ methods.
2. Surveys and compares 30+ **prompting frameworks** using a structured comparison matrix of capabilities.
3. Establishes **ReAct** as the paradigm integrating reasoning and acting for tool-augmented LLM inference.
4. Identifies **automatic prompt optimization** (DSPy) and **structured generation** as production-ready research frontiers.

# When to cite

1. When selecting a **prompting framework** (LangChain, LlamaIndex, DSPy, Guidance) for a specific use case.
2. When comparing **chain-of-thought, tree-of-thought, and self-consistency** prompting strategies.
3. When justifying **automatic prompt optimization** over manual prompt engineering for production systems.
4. When arguing that **structured generation** (constrained decoding) is necessary for schema-conformant LLM outputs.

---
[[LLM]]
[[Generative AI|GenAI]]
[[Prompt Engineering|Prompt]]
[[Machine Learning|ML]]
