---
title:  RAG vs Finetuning — Which Is the Best Tool to Boost Your LLM Application
created: Saturday 12th April 2025 21:01
aliases: 
tags:
  - rag
  - fine-tuning
  - llm
  - domain-adaptation
---
- https://towardsdatascience.com/rag-vs-finetuning-which-is-the-best-tool-to-boost-your-llm-application-94654b1eaba7/
- Type: article
- Source: Towards Data Science · Heiko Hotz · Aug 2023

---

# TL;DR

**RAG** adds external knowledge and **fine-tuning** changes model behaviour and style, so they solve different problems and can be combined.

# Summary

The author retracts the "try RAG first, fine-tune if it falls short" advice: the two are not points on one cost scale but tools for orthogonal needs. Two questions decide the choice: does the application need **external, changing data**, and does it need to change the model's **tone, terminology or domain behaviour**? A 15-criterion comparison (hallucinations, freshness, transparency, cost, latency, maintenance) backs the recommendations for summarization, organizational Q&A and customer support.

# Key takeaways

1. **Ask two questions first**: need for external data, and need to adapt behaviour or style. Both can be yes.
2. **Choose RAG for dynamic knowledge**: updates need no retraining, answers are grounded and **traceable** to sources, and hallucination risk drops.
3. **Choose fine-tuning for style and domain fluency**: it captures tone and vocabulary but is a static snapshot and a black box.
4. **Pick by use case**: summarization in a specialized style leans on fine-tuning; internal Q&A on RAG; customer support on a **hybrid** (brand voice plus current documents).
5. **Mind the cost profile**: RAG has high setup and maintenance cost; fine-tuning costs have fallen with parameter-efficient methods such as **QLoRA**.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[RAG]] | Retrieve snippets, let the LLM answer from them |
| [[LLM]] | The model being boosted by either approach |
| [[QLORA - Efficient Finetuning of Quantized LLMs\|QLoRA]] | Cheaper fine-tuning |
| [[RAFT - Adapting Language Model to Domain Specific RAG\|RAFT]] | Research that combines both ideas (not cited by the page) |

# When to use

1. When deciding **RAG vs fine-tuning** (or both) for a new LLM application.
2. When justifying why fine-tuning is **not** the way to add fresh knowledge.
3. When you need a checklist of comparison criteria for an architecture review.

# Caveats

- Opinion piece from 2023 with no benchmarks or measurements.

---
[[RAG]] [[LLM]] [[Generative AI]]
[[RAFT - Adapting Language Model to Domain Specific RAG]]
[[QLORA - Efficient Finetuning of Quantized LLMs]]
[[Retrieval-Augmented Generation for Large Language Models - A Survey]]
