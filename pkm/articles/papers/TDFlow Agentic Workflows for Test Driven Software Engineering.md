---
title: "TDFlow: Agentic Workflows for Test Driven Software Engineering"
created: Friday 17th April 2026 16:00
aliases:
tags:
  - agents
  - code-generation
  - software-testing
  - llm
  - multi-agent
---
- https://arxiv.org/abs/2510.23761v1
- Source: arxiv

---

# TL;DR

**TDFlow** frames software repair as a test-resolution problem, using a four-agent pipeline guided by human-written tests to reach **88.8% on SWE-Bench Lite** — a 27.8% absolute improvement over prior state of the art.

# Summary

LLM-based code agents lack structured feedback signals, making reliable patch generation for real-world GitHub issues difficult. TDFlow decomposes the repair pipeline into four specialized sub-agents — patch proposer, debugger, reviser, and optional test generator — all driven by **human-written reproduction tests** as the primary execution signal. Agents iterate until tests pass, with feedback loops replacing prompt-only generation. On **SWE-Bench Verified** the system achieves 94.3% pass rate; on **SWE-Bench Lite** 88.8%. Analysis of 800 test runs found only 7 cases of test manipulation. The key finding: **test authorship**, not code generation, is the primary bottleneck to human-level autonomous software engineering.

# Key contributions

1. Proposes **TDFlow**, a test-driven agentic architecture that decomposes software repair into four specialized sub-agents, each focused on a single aspect of the repair loop
2. Achieves **88.8% on SWE-Bench Lite** and **94.3% on SWE-Bench Verified**, establishing a new state of the art at the time of publication
3. Demonstrates that framing code generation as **test resolution** — with execution feedback instead of pure LLM inference — dramatically improves patch reliability
4. Shows empirically (800 runs) that **test manipulation** is rare (0.9%), validating the integrity of the evaluation approach
5. Establishes that **writing reproduction tests**, not implementing fixes, is the primary obstacle to human-level performance, pointing toward human-in-the-loop test authorship as the next frontier

# When to cite

1. When arguing that **TDD principles** applied to LLM agents improve patch reliability over prompt-only code generation
2. When citing benchmark results for **SWE-Bench Lite** or **SWE-Bench Verified** to compare autonomous software engineering systems
3. When discussing why **test generation** is the hardest open problem in autonomous software engineering — not code generation
4. When explaining how **multi-agent decomposition** reduces cognitive load and improves performance on complex, multi-step repair tasks

---
[[LLM]]
[[Testing]]
[[Generative AI]]
[[Prompt Engineering]]
