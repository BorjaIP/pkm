---
title:  An LLM Compiler for Parallel Function Calling
created: Monday 13th May 2024 11:44
aliases:
tags:
  - llm
  - tool
---
- https://arxiv.org/pdf/2312.04511
- https://github.com/SqueezeAILab/LLMCompiler
- Source: arxiv

---

# TL;DR

**LLMCompiler** applies compiler design principles — dependency analysis, parallel scheduling — to LLM tool calls, achieving up to 3.7x latency and 6.7x cost reductions over sequential ReAct execution.

# Summary

LLMs calling external tools sequentially waste latency and tokens even when tasks are fully independent. Inspired by classical compiler design, **LLMCompiler** introduces a three-stage pipeline — a **Function Calling Planner**, a **Task Fetching Unit**, and an **Executor** — that identifies inter-task dependencies and dispatches independent calls in parallel. Benchmarked against **ReAct**, it achieves up to 3.7x latency reduction, 6.7x cost reduction, and ~9% accuracy improvement. The architecture is model-agnostic and was published at ICML 2024.

# Key contributions

1. Proposes **LLMCompiler**, a three-stage planner-fetcher-executor pipeline for dependency-aware parallel tool dispatch.
2. Achieves **3.7x latency reduction** and **6.7x cost reduction** versus sequential ReAct on function-calling benchmarks.
3. Shows that **parallel execution reduces error propagation** from sequential misorderings, improving accuracy by ~9%.
4. Demonstrates a **model-agnostic architecture** compatible with both open-source and proprietary LLMs.

# When to cite

1. When arguing that **orchestration design** can matter more than model choice for cost and latency in agentic systems.
2. When applying **compiler concepts** (dependency graphs, parallelism) to LLM tool-calling pipelines.
3. When looking for evidence that **parallel tool execution** improves both efficiency and accuracy over sequential approaches.
4. When evaluating alternatives to **ReAct** for multi-tool LLM agent frameworks.

---
[[LLM]]
[[Prompt Engineering]]
[[Computer Architecture]]
[[ART - Automatic multi-step reasoning and tool-use for large language models]]
