---
title:  Reasoning best practices
created: Saturday 12th April 2025 19:40
aliases: 
tags:
  - prompt-engineering
  - reasoning
  - llm
  - co-openai
---
- https://platform.openai.com/docs/guides/reasoning-best-practices
- Type: reference
- Source: OpenAI developer documentation

---

# TL;DR

Reasoning models plan internally, so prompt them with short, goal-focused instructions and clear constraints, and do not ask them to "think step by step".

# What it covers

Guidance for OpenAI's o-series models. **Reasoning models** suit ambiguous, multi-step, high-accuracy work (planning, document analysis, code review, LLM-as-judge); **GPT models** suit fast, cheap, well-defined execution. A common pattern uses a reasoning model as the **planner** and a GPT model as the **doer**.

# Key takeaways

1. **Keep prompts simple and direct**; the models handle brief instructions well.
2. **Skip chain-of-thought prompts**: reasoning happens internally, so "think step by step" adds little and can hurt.
3. **Use delimiters** (markdown, XML tags, section titles) to separate parts of the input.
4. **Start zero-shot**, add few-shot examples only if needed and make them match the instructions closely.
5. **State constraints and success criteria** explicitly (budget, format, end goal).
6. **Use developer messages** rather than system messages from `o1-2024-12-17`; markdown is off by default, re-enable it with `Formatting re-enabled` on the first line.
7. **For agentic flows** use the Responses API, set `store` true and pass reasoning items back (via `previous_response_id`) between function calls.

# When to use

1. When **choosing between reasoning and GPT models** for a task.
2. When **rewriting prompts** that were written for non-reasoning models.
3. When building an **agent loop** that must preserve reasoning items.

# Caveats

- Vendor documentation tied to OpenAI model names and APIs of the time, and the docs have moved to a new URL.

---
[[Prompt Engineering]] [[LLM]] [[GPT]] [[AI Agents]]
[Google - Prompt Engineering](https://drive.google.com/file/d/1AbaBYbEa_EbPelsT40-vj64L-2IwUJHy/view)
[[8 Types of Prompt Engineering]]
[[Prompt-engineering-guide]]
