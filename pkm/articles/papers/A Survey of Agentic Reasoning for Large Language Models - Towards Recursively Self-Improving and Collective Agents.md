---
title:  A Survey of Agentic Reasoning for Large Language Models - Towards Recursively Self-Improving and Collective Agents
created: Thursday 12th November 2026 13:00
aliases:
tags:
  - agents
  - llm
  - reasoning
  - survey
  - self-improvement
---
- https://arxiv.org/pdf/2601.12538
- https://github.com/weitianxin/Awesome-Agentic-Reasoning
- Source: arxiv

---

# TL;DR

Organizes **agentic reasoning** into three layers (foundational, self-evolving, collective) and two optimization modes (in-context vs post-training).

# Summary

LLMs reason well in closed settings like math and code, but their reasoning is **static and short-horizon**, so they struggle in open-ended, changing environments. The survey recasts LLMs as autonomous agents that plan, act and learn through interaction. It maps existing work to **foundational** skills (planning, tool use, search), **self-evolving** agents (feedback, memory, adaptation) and **collective multi-agent** reasoning (roles, communication, shared memory), each studied under **in-context orchestration** or **post-training** with RL and supervised fine-tuning. It reports no new experiments.

# Key contributions

1. Proposes a **three-layer framing** of agentic reasoning, from single-agent skills up to multi-agent collaboration.
2. Introduces a **two-mode lens** that contrasts in-context orchestration (no parameter updates) with post-training through **RL, GRPO and fine-tuning**.
3. Formalizes the setting with a **POMDP** view of "think, then act", a **Dec-POMDP** view of multi-agent systems and a meta-update rule for self-evolution, distinguishing verbal, procedural (skill libraries) and structural (code) evolution.
4. Compiles **comparison tables** of planning and tool-use methods, plus applications (math and coding, science, embodied agents, healthcare, web research) and benchmarks.
5. Outlines **open challenges**: personalization, long-horizon interaction, world modeling, scalable multi-agent training and governance.

# When to cite

1. When positioning an agent method as foundational, self-evolving or collective.
2. When contrasting **in-context** reasoning with **post-training** (RL or fine-tuning) as ways to build agent ability.
3. When arguing that agents need **self-improvement** through feedback, memory and skill libraries.
4. When listing open problems in agentic reasoning such as long-horizon interaction and multi-agent training.

Caveat: scope is work up to 2025, the taxonomy is the authors' own and its layers overlap; I read only the first part of the HTML version.

---
[[AI Agents]] [[LLM]] [[Memory in the Age of AI Agents]] [[WikiSkill - Compiling Agent Experience into Persistent Knowledge for Skill Evolution]] [[REACT - SYNERGIZING REASONING AND ACTING IN LANGUAGE MODELS]] [[ART - Automatic multi-step reasoning and tool-use for large language models]]
