---
title:  RestGPT - Connecting Large Language Models with Real-World RESTful APIs
created: Monday 22nd January 2024 09:35
aliases:
tags:
  - llm
  - gpt
  - tool-use
  - agents
---
- https://arxiv.org/pdf/2306.06624.pdf
- Source: arxiv

---

# TL;DR

**RestGPT** connects LLMs to real-world RESTful APIs through a coarse-to-fine planning loop — planner, API selector, caller, and response executor — achieving 79% task success on complex multi-step benchmarks without fine-tuning.

# Summary

Generic tool-use frameworks fail on real-world REST APIs because they lack structured planning and response parsing. RestGPT addresses this with a four-component architecture: a high-level planner decomposes goals into sub-tasks, an **API selector** identifies the correct endpoint from an OpenAPI specification, a caller constructs and executes the HTTP request, and a **response executor** maps raw API results back to task context. Evaluated on RestBench (TMDB and Spotify), it achieves 79% on **complex multi-step tasks** without any fine-tuning.

# Key contributions

1. Proposes a **coarse-to-fine planning loop** that decomposes high-level goals into concrete API call sequences.
2. Introduces a dedicated **response executor** module that translates raw API output into task-relevant context — a component generic frameworks omit.
3. Demonstrates that **OpenAPI specifications** provide sufficient context for LLMs to construct valid HTTP calls without fine-tuning.
4. Establishes **RestBench** as a benchmark for evaluating LLM agents on authentic real-world web services (TMDB, Spotify).

# When to cite

1. When designing an **LLM agent architecture** for interacting with REST APIs and needing a reference decomposition.
2. When arguing that **separating planning, selection, and execution** produces cleaner API integration than monolithic prompting.
3. When evaluating LLM agents on **multi-step real-world API tasks** rather than synthetic tool-use benchmarks.
4. When justifying the need for a dedicated **response parsing layer** in API-connected LLM systems.

---
[[LLM]]
[[GPT]]
[[API]]
