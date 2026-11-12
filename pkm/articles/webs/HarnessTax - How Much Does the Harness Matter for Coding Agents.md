---
title:  HarnessTax - How Much Does the Harness Matter for Coding Agents
created: Thursday 12th November 2026 12:00
aliases:
tags:
  - agents
  - llm
  - evaluation
  - code-generation
---
- https://harnesstax.github.io/
- Type: article
- Source: UC Berkeley (Pan, Yang, Arabzadeh, Chiang, Stoica, Zaharia) · 2026

---

# TL;DR

Across 21 model–harness pairs, the harness barely changes a coding agent's success rate but can change its cost by up to 5×.

# Summary

Choosing a coding agent means choosing a model and a **harness**, the system that manages tools, context and task execution, yet the effect of the harness is rarely measured. The study runs seven models in three harnesses (Claude Code, Codex CLI and Pi) on SWE-bench Lite and Terminal-Bench 2.0. Average harness effect on success stays within about ±2% and ±5% respectively, while cost differs widely; the authors call the extra spend a **harness tax**. A minimal harness is competitive, and models often do well outside their own provider's harness.

# Key takeaways

1. **Compare cost, not just success**: the same model reaches similar success at up to 5× the cost; Claude Code costs about 2.0× Pi and 1.6× Codex on SWE-bench Lite (geometric mean).
2. **Check the default harness**: Fable 5 solves 97.8% in Claude Code, 96.7% in Codex and 96.7% in Pi, at $1.33 versus $0.67 for Claude Code and Pi.
3. **Try a minimal harness**: Pi, with four tools (read, write, edit, bash), reaches the cost–success Pareto frontier on both benchmarks; Claude Code's first-call context is over 10× Pi's.
4. **Don't assume provider lock-in**: an alternative harness gives the best success rate in 9 of 12 model–benchmark comparisons; GPT-5.6 Sol scores 83.3% in Pi versus 78.9% in Codex at about half the cost.
5. **Treat harness complexity as a trade-off**: richer scaffolding may help harder tasks, other models or interactive settings, but is not needed by default.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[AI Agents]] | Coding agents whose harness is evaluated |
| [[Claude]] | Claude Code harness and Claude models |
| SWE-bench Lite, Terminal-Bench 2.0 | Benchmarks (30 random tasks, 3 repetitions per pair) |
| Pi, Codex CLI | Alternative harnesses |

# When to use

1. When choosing a coding agent or deciding whether to pair a model with a different harness.
2. When arguing that cost per solved task should be reported next to success rate.
3. When designing a minimal agent harness and wondering what tools it really needs.

# Caveats

- Only two open-source benchmarks that models may have seen in training; the authors say results may differ elsewhere.
- Small sample (30 tasks, 3 repetitions per point); cost depends on caching and pricing at the time.
- The page is a project blog, not a peer-reviewed paper; traces are promised but not checked here.

---
[[AI Agents]] [[Claude]] [[LLM]] [[SWE-CI Evaluating Agent Capabilities in Maintaining Codebases via Continuous Integration]] [[The End of Software Engineering - How AI Agents Are Fundamentally Restructuring the Software Paradigm]]
