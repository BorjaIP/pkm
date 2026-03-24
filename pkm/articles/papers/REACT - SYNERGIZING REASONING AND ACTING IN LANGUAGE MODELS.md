---
title:  REACT - SYNERGIZING REASONING AND ACTING IN LANGUAGE MODELS
created: Monday 5th February 2024 19:46
aliases:
tags:
  - llm
  - reasoning
  - agents
---
- https://arxiv.org/pdf/2210.03629.pdf
- Source: arxiv

---

# TL;DR

**ReAct** interleaves verbal reasoning traces and action steps in a single LLM forward pass, enabling grounded, interpretable agent behavior that outperforms chain-of-thought and action-only baselines.

# Summary

Separating reasoning from acting in LLM agents leads to ungrounded thoughts or blind actions. ReAct solves this by having the model produce a **reasoning trace** before each action and then incorporating the action's output into the next reasoning step. This dynamic loop outperforms **chain-of-thought** and action-only baselines on HotpotQA, FEVER, ALFWorld, and WebShop. The interpretable trace structure also enables practical **human-in-the-loop** correction mid-task, without any fine-tuning.

# Key contributions

1. Proposes the **ReAct prompting paradigm** that interleaves reasoning traces and actions in a unified LLM output.
2. Demonstrates that grounding reasoning in **observed action results** reduces hallucination compared to chain-of-thought alone.
3. Shows that **few-shot ReAct prompts** are sufficient for strong performance across both knowledge retrieval and embodied decision tasks.
4. Introduces interpretable agent traces as an **audit log** enabling human inspection and mid-task correction.

# When to cite

1. When building an **LLM agent** that needs to alternate between reasoning and tool/environment interaction.
2. When justifying why **interleaved reasoning and acting** outperforms either in isolation.
3. When arguing for interpretable agent architectures that support **human-in-the-loop** oversight.
4. When choosing a baseline prompting strategy for **knowledge-intensive QA** or interactive decision tasks.

---
[[LLM]]
[[Prompt Engineering]]
