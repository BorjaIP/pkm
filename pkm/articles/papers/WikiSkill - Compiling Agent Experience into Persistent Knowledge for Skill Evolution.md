---
title:  WikiSkill - Compiling Agent Experience into Persistent Knowledge for Skill Evolution
created: Wednesday 16th September 2026 10:15
aliases:
tags:
  - ai-agents
  - agentic-workflows
  - self-improvement
  - co-google
---
- https://arxiv.org/html/2608.27454
- Source: arxiv

---

# TL;DR

**WikiSkill** turns an agent's raw execution traces into a persistent, structured **wiki** of patterns that its skills evolve from, instead of losing that knowledge in scattered optimization histories.

# Summary

Existing skill-evolution methods refine agent behavior from run to run but discard the reasoning behind each change, so improvement doesn't compound. WikiSkill fixes this with a **three-layer architecture**: an immutable **raw layer** of execution traces, a **wiki layer** that consolidates them into structured, audited patterns, and a **skills layer** of active procedural instructions derived from that wiki. Across five benchmarks and five models, WikiSkill consistently beats prior skill-evolution baselines, and ablations show a **15-point performance drop** when the wiki is removed.

# Key contributions

1. Proposes a **three-layer memory architecture** (raw → wiki → skills) that separates immutable evidence from compounding structured knowledge and from the instructions an agent actually executes.
2. Introduces an **evolutionary loop** with distinct roles — an Inference Agent, a Wiki Maintainer, and a Skill Proposer — plus a **gating mechanism** that accepts improvements or rolls back failed skill updates while always preserving the wiki.
3. Demonstrates that **skill gains scale with model size**, showing skill evolution as complementary to (not a substitute for) raw model scaling.
4. Shows that evolved skills **transfer across models**, sometimes making a smaller model's skills outperform a larger model's self-evolved ones, depending on whether the skill encodes a general procedure or a model-specific workaround.

# When to cite

1. When explaining why **naive skill-evolution loops plateau** because they discard the reasoning behind past optimizations.
2. When arguing for a **persistent knowledge layer** (a wiki or memory store) as distinct from the active instructions an agent executes.
3. When discussing whether **skills transfer across models** and what determines transferability (general procedure vs. model-specific hack).
4. When justifying a **gating/rollback mechanism** for autonomous skill or prompt self-improvement systems.

---
[[AI Agents]] [[Knowledge Graph]]
