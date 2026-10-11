---
title:  The Practical Guides for Large Language Models
created: Monday 14th April 2025 21:03
aliases: 
tags:
  - llm
  - nlp
  - survey
  - fine-tuning
---
- https://github.com/Mooler0410/LLMsPracticalGuide
- Type: repo
- Source: GitHub · Mooler0410 · companion to arXiv:2304.13712

---

# TL;DR

A curated, updated resource list accompanying the survey *Harnessing the Power of LLMs in Practice*, with a decision flow for choosing between an LLM and a fine-tuned model.

# What it does

It organises model families (encoder-only, encoder-decoder, decoder-only), pretraining, fine-tuning and test data, NLP task categories, efficiency, trustworthiness, alignment, and a table of licences and commercial-use limits. Two figures are central: the **evolutionary tree** of language models and a **decision flow** for whether an LLM or a fine-tuned model fits an NLP application.

# Key takeaways

1. **Know the three families**: BERT-style encoder-only, encoder-decoder and GPT-style decoder-only models.
2. **Use the decision flow** to judge whether the task suits an LLM or a fine-tuned smaller model.
3. **Check task categories**: traditional NLU, generation, knowledge-intensive tasks, emergent abilities and real-world tasks.
4. **Consider efficiency**: cost, latency and parameter-efficient fine-tuning such as LoRA.
5. **Check licences** of models and training data before commercial use.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[LLM]] | Subject of the guide |
| [[NLP]] | Task taxonomy |
| [[Transformers]] | Underlying architecture of all three families |
| [[A Survey of Large Language Models]] | Companion survey in the vault |

# When to use

1. When deciding **LLM vs fine-tuned model** for an NLP task.
2. When you need the **license status** of an open model.
3. When looking for a map of the LLM landscape.

# Caveats

- The decision flow and tree are images; the page gives no explicit findings, only navigation.
- The repo is from 2023 and its model lists age quickly.

---
[[LLM]] [[NLP]] [[Transformers]]
[[A Survey of Large Language Models]]
[[RAG vs Finetuning — Which Is the Best Tool to Boost Your LLM Application]]
[[QLORA - Efficient Finetuning of Quantized LLMs]]
