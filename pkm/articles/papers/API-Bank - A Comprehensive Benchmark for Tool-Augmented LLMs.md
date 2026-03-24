---
title: API-Bank - A Comprehensive Benchmark for Tool-Augmented LLMs
created: Monday 5th February 2024 19:43
aliases:
tags:
  - llm
  - tool
---
- https://aclanthology.org/2023.emnlp-main.187.pdf
- Source: acl

---

# TL;DR

**API-Bank** is the first comprehensive benchmark for tool-augmented LLMs, covering 73 runnable APIs across three skill dimensions — planning, retrieval, and execution — with a fine-tuned **Lynx** model surpassing Alpaca by over 26 points.

# Summary

Tool-augmented LLMs must plan which APIs to call, retrieve them from a catalog, and execute calls correctly — yet no systematic benchmark existed for this three-stage pipeline. **API-Bank** provides 73 runnable API tools, 314 annotated dialogues with 753 API calls, and a 1,888-dialogue training set spanning 2,138 APIs across 1,000 domains. GPT-4 excels at planning while GPT-3.5 leads on retrieval. Fine-tuning Alpaca on the training set produces **Lynx**, which surpasses the base model by over 26 percentage points and approaches GPT-3.5 performance.

# Key contributions

1. Introduces **API-Bank**, the first benchmark decomposing tool use into three evaluable skills: planning, retrieval, and API call execution.
2. Provides **73 runnable tools** with ground-truth API calls, enabling execution-level evaluation beyond text matching.
3. Shows that **GPT-4 and GPT-3.5 specialize differently** — no single model dominates all three tool-use dimensions.
4. Produces **Lynx** via fine-tuning, demonstrating that a 1,000-domain training set enables smaller models to approach GPT-3.5.
5. Identifies **multi-step API chaining** as the hardest unsolved subproblem for production tool-augmented systems.

# When to cite

1. When evaluating or benchmarking **LLM tool use** across the planning, retrieval, and execution dimensions.
2. When arguing that **planning and retrieval are separable skills** that should be improved independently.
3. When citing evidence that **fine-tuning on tool-use data** enables smaller models to approach large-model performance.
4. When discussing the difficulty of **multi-step API chaining** and error recovery in agentic LLM systems.

---
[[LLM]]
[[Generative AI]]
[[Prompt Engineering]]
[[ART - Automatic multi-step reasoning and tool-use for large language models]]
[[An LLM Compiler for Parallel Function Calling]]
