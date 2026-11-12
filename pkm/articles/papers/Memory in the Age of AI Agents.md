---
title:  Memory in the Age of AI Agents
created: Wednesday 11th November 2026 12:00
aliases:
tags:
  - agents
  - llm
  - survey
---
- https://arxiv.org/abs/2512.13564
- Source: arxiv

---

# TL;DR

Organizes the fragmented field of **agent memory** with a **forms–functions–dynamics** taxonomy that separates it from LLM memory, RAG and context engineering.

# Summary

Research on memory for foundation-model agents is **fragmented**: papers differ in motivation, implementation and evaluation, and terms like episodic, semantic or parametric are used loosely, so the old **long/short-term** split no longer fits. The survey treats memory as a persistent, **self-evolving state** that the agent policy reads at each step. It classifies systems by **forms** (token-level, parametric, latent), **functions** (factual, experiential, working) and **dynamics** (formation, evolution, retrieval), and compiles benchmarks and open-source frameworks. It reports no new experiments.

# Key contributions

1. Proposes a **forms–functions–dynamics taxonomy**: what carries memory (token-level in 1D, 2D or 3D structures, parametric, latent), why agents need it (**factual**, **experiential**, **working**) and how it operates over time.
2. Establishes a **formal definition** of agent memory as a state updated by formation, evolution and retrieval operators, and distinguishes it from **LLM memory**, **RAG** and **context engineering**.
3. Analyzes how **memory forms and functions** align with agent objectives, including experiential memory as cases, strategies and skills.
4. Compiles **memory benchmarks and open-source frameworks** as a reference list.
5. Identifies **open frontiers**: automated memory management, **reinforcement learning** integration, multimodal memory, shared multi-agent memory, memory for world models and **trustworthiness**.

# When to cite

1. When explaining how **agent memory** differs from RAG, LLM memory or context engineering.
2. When choosing or comparing a memory design (token-level vs parametric vs latent) for an agent.
3. When arguing that **experiential memory** (cases, strategies, skills) is what lets agents improve over time.
4. When surveying **memory benchmarks and frameworks** or listing open problems in agent memory.

Caveat: it is a conceptual survey; the authors note that fast growth of the literature means some work may be missing.

---
[[AI Agents]] [[LLM]] [[RAG]] [[Harness Engineering]] [[WikiSkill - Compiling Agent Experience into Persistent Knowledge for Skill Evolution]]
