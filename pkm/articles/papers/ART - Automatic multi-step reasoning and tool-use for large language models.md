---
title: ART - Automatic multi-step reasoning and tool-use for large language models
created: Monday 5th February 2024 19:45
aliases:
tags:
  - llm
  - tool-use
  - reasoning
---
- https://arxiv.org/pdf/2303.09014.pdf
- Source: arxiv

---

# TL;DR

**ART** augments frozen LLMs with a **task library** of few-shot demonstrations that embed tool-use calls, enabling automatic interleaving of reasoning and tool execution without any gradient updates.

# Summary

Frozen **LLMs** are augmented with a **task library** of few-shot demonstrations that embed tool-use calls such as search and code execution. At inference time, ART retrieves the most relevant demonstrations for a new task and interleaves reasoning steps with **tool calls** automatically, without gradient updates. The approach generalizes to unseen tasks via simple task descriptions, outperforming zero-shot GPT-3 and **chain-of-thought** prompting on BigBench and MMLU benchmarks.

# Key contributions

1. Proposes **ART**, a framework that automatically interleaves multi-step reasoning and tool-use calls in frozen LLMs via retrieved demonstrations.
2. Introduces a **task library** of few-shot examples with embedded tool calls, enabling modular and updatable tool knowledge.
3. Demonstrates **zero-shot generalization** to new tasks through task descriptions alone, without per-task prompt engineering.
4. Shows outperformance over **chain-of-thought prompting** and zero-shot GPT-3 on BigBench and MMLU.

# When to cite

1. When discussing **automatic tool-use interleaving** in LLMs without fine-tuning or gradient updates.
2. When citing retrieval-based approaches to **few-shot demonstration selection** for multi-step reasoning tasks.
3. When arguing that a **task library** decouples tool knowledge from the base model, enabling modular updates.
4. When comparing **ART** to ReAct or other reasoning-plus-action frameworks for tool-augmented LLMs.

---
[[LLM]]
[[Prompt Engineering]]
