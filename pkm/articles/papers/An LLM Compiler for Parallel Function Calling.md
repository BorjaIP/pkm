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

# Summary

LLMs calling external tools sequentially waste latency and tokens even when tasks are fully independent. Inspired by classical compiler design, **LLMCompiler** introduces a three-stage pipeline — a **Function Calling Planner**, a **Task Fetching Unit**, and an **Executor** — that identifies inter-task dependencies and dispatches independent calls in parallel. Benchmarked against the **ReAct** baseline, it achieves up to **3.7× latency reduction**, **6.7× cost reduction**, and ~9% accuracy improvement. Compatible with both open-source and closed-source models, published at ICML 2024.

# Main points

1. Sequential tool calls create avoidable **latency and cost bottlenecks** even for independent sub-tasks.
2. **LLMCompiler** uses a planner, fetcher, and executor for **dependency-aware parallel dispatch**.
3. Achieves up to **3.7× speedup** and **6.7× cost reduction** vs. ReAct on function-calling benchmarks.
4. Accuracy improves ~9% because parallel execution reduces **error propagation** from sequential misorderings.
5. Architecture is **model-agnostic**, compatible with open-source and proprietary LLMs.

# Takeaways

1. Compiler concepts — **dependency graphs, scheduling, parallelism** — transfer directly to LLM orchestration.
2. Audit existing tool calls for **unnecessary sequentiality** before adding more tools — this alone saves cost.
3. The 6.7× cost reduction shows that **orchestration design** can matter more than model choice for agentic workloads.
4. Parallel execution also **improves accuracy** — sequential errors compound, so order matters even for correctness.
5. Open-source release makes **LLMCompiler a drop-in option** to evaluate before building custom orchestration.

---
[[LLM]]
[[Prompt Engineering]]
[[Computer Architecture]]
[[ART - Automatic multi-step reasoning and tool-use for large language models]]
