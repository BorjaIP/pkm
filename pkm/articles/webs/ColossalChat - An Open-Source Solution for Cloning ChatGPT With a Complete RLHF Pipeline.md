---
title:  ColossalChat - An Open-Source Solution for Cloning ChatGPT With a Complete RLHF Pipeline
created: Saturday 12th April 2025 21:16
aliases: 
tags:
  - llm
  - rlhf
  - fine-tuning
  - gpu
---
- https://medium.com/pytorch/colossalchat-an-open-source-solution-for-cloning-chatgpt-with-a-complete-rlhf-pipeline-5edf08fb538b
- Type: article
- Source: PyTorch blog (Medium) · Yang You · Mar 2023

---

# TL;DR

ColossalChat releases a complete open **RLHF pipeline** on top of LLaMA (SFT, reward model, PPO), plus a 104K bilingual dataset and 4-bit inference, as an open ChatGPT-style recipe.

# Summary

LLaMA lacks instruction tuning, and Alpaca-style projects stop at the supervised fine-tuning stage with English-only data. ColossalChat adds the missing alignment stages: it builds a bilingual (English-Chinese) Q&A set of about 104K pairs, expanded with self-instruct for roughly $900 of annotation, then runs **RLHF** in three stages. Models under 10B parameters reach comparable chat quality to GPT-3.5 in the authors' demos, and a 7B model can run quantized on about 4 GB of GPU memory.

# Key takeaways

1. **RLHF stage 1**: supervised instruction fine-tuning on the dataset.
2. **Stage 2**: train a reward model from human rankings of several outputs per prompt.
3. **Stage 3**: reinforcement learning with PPO, split into a "make experience" phase (SFT, actor, reward and critic models) and a parameter update.
4. **Add a PTX loss**: cross-entropy of the actor's response against pretraining-style text, summed with policy and value losses to avoid forgetting.
5. **Open assets**: demo, training code for 7B and 13B models, bilingual dataset, weights, 4-bit quantized inference needing about 4 GB.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[ColossalAI]] | Framework that provides the pipeline |
| [[LLM]] | LLaMA as base model |
| [[GPT]] | ChatGPT and GPT-3.5 as reference |
| [[QLORA - Efficient Finetuning of Quantized LLMs\|QLoRA]] | Related low-memory fine-tuning idea (not cited) |

# When to use

1. When you need the **RLHF three-stage recipe** in concrete form.
2. When comparing open ChatGPT replications, see [[Replicate ChatGPT Training Quickly and Affordable with Open Source Colossal-A]].
3. When estimating the **cost of a seed dataset** for instruction tuning.

# Caveats

- Promotional launch post: quality claims rest on demo screenshots, and the Quick Start part of the article was not read.

---
[[ColossalAI]] [[LLM]] [[GPT]] [[Deep Learning]]
[[Replicate ChatGPT Training Quickly and Affordable with Open Source Colossal-A]]
[[Large Scale Distributed Model Training with Colossal AI and Lightning AI]]
[[RAG vs Finetuning — Which Is the Best Tool to Boost Your LLM Application]]
