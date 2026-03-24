---
title: Compositional Foundation Models for Hierarchical Planning
created: Wednesday 27th September 2023 14:05
aliases:
tags:
  - gpt
  - llm
---
- https://arxiv.org/pdf/2309.08587.pdf
- Source: arxiv

---

# TL;DR

**CFM (Compositional Foundation Models)** composes a language model, a video diffusion model, and an action diffusion model into a hierarchical planning system for long-horizon robotic manipulation without task-specific retraining.

# Summary

Long-horizon robotic manipulation requires reasoning across semantic, visual, and motor abstraction levels simultaneously — a task beyond any single foundation model. CFM addresses this by composing three specialized models hierarchically: a **language model** decomposes goals into subgoal descriptions, a **video diffusion model** imagines plausible visual subgoals conditioned on those descriptions, and an **action diffusion model** generates motor primitives conditioned on the visual subgoals. Each model operates within its training distribution. CFM outperforms monolithic baselines on long-horizon manipulation benchmarks in both success rate and **plan coherence**.

# Key contributions

1. Proposes **CFM**, a compositional inference architecture that chains language, video diffusion, and action diffusion models for hierarchical robotic planning.
2. Introduces **visual subgoal imagination via diffusion** as a bridge between language-level plans and low-level motor actions.
3. Demonstrates that **compositional inference** over specialized foundation models outperforms monolithic planning approaches on long-horizon tasks.
4. Shows that each foundation model can operate within its **training distribution** without task-specific retraining through hierarchical composition.

# When to cite

1. When designing a **multi-model hierarchical planning** system for robotics or embodied AI.
2. When arguing that **compositional inference** over specialized models outperforms a single generalist model for complex sequential tasks.
3. When using **video diffusion models** as an intermediate representation between language plans and motor control.
4. When justifying that **LLMs are most effective as planners** when grounded by lower-level perceptual or action models.

---
[[Artificial Intelligence|AI]]
[[LLM]]
[[GPT]]
