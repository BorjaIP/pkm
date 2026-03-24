---
title:  Toolformer - Language Models Can Teach Themselves to Use Tools
created: Monday 5th February 2024 19:46
aliases:
tags:
  - llm
  - tool-use
  - self-supervised
---
- https://arxiv.org/pdf/2302.04761.pdf
- https://github.com/lucidrains/toolformer-pytorch
- Source: arxiv

---

# TL;DR

**Toolformer** teaches language models to autonomously decide when and how to call external APIs using self-supervised learning, where only API calls that reduce next-token perplexity are retained for fine-tuning.

# Summary

Language models lack numerical, temporal, and factual precision that external tools can provide, but learning when to use tools typically requires human annotation. Toolformer eliminates this by generating candidate **API calls** — calculator, calendar, Wikipedia search, translation, QA model — inserting them into text, and retaining only those that reduce **perplexity** on subsequent tokens. Fine-tuning on this self-curated data produces a 6.7B GPT-J model that outperforms GPT-3 (175B) on several downstream benchmarks while preserving general **language modeling quality**.

# Key contributions

1. Proposes a **self-supervised data curation** method where API calls are selected by perplexity reduction on subsequent tokens — no human annotation required.
2. Demonstrates that a **6.7B model** fine-tuned with tool use surpasses GPT-3 175B on multiple downstream benchmarks.
3. Shows that fine-tuning on tool-augmented data **preserves base language modeling** capability without degradation.
4. Introduces **perplexity reduction** as a principled, task-agnostic signal for deciding when tool invocation is beneficial.

# When to cite

1. When designing a **self-supervised approach** to teaching LLMs tool use without human-labeled API call data.
2. When arguing that **small models with tool access** can outperform much larger models without tools.
3. When justifying **perplexity reduction** as a signal for selecting useful tool invocations.
4. When surveying **LLM tool-use** methods and needing the foundational self-supervised approach.

---
[[LLM]]
[[GPT]]
