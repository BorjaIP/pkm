---
title:  PaLI-3 Vision Language Models - Smaller, Faster, Stronger
created: Tuesday 31st October 2023 10:35
aliases:
tags:
  - llm
  - ml
---
- https://arxiv.org/abs/2310.09199
- Source: arxiv

---

# TL;DR

**PaLI-3** shows that independently applying contrastive pre-training to a ViT-G vision encoder before joint vision-language training produces state-of-the-art results on TextVQA and DocVQA at 5B parameters, outperforming models up to 10x larger.

# Summary

Scaling vision-language models is expensive, but **PaLI-3** demonstrates that encoder pre-training strategy matters more than parameter count. A ViT-G vision encoder is first trained with **contrastive pre-training** independently, then combined with a UL2 language model for joint vision-language training. At **5B parameters**, this approach achieves state-of-the-art on **TextVQA**, **DocVQA**, COCO captioning, and chart understanding, outperforming competing systems up to 10x larger and establishing that visual grounding improves substantially when the encoder already understands semantic alignment.

# Key contributions

1. Proposes **two-phase training**: contrastive vision encoder pre-training followed by joint vision-language training.
2. Demonstrates that **contrastive pre-training** of the vision encoder outperforms supervised-only initialization for grounding tasks.
3. Shows a **5B-parameter model** can surpass systems up to 10x larger through better training design.
4. Establishes state-of-the-art on **DocVQA and TextVQA**, confirming contrastive vision pre-training benefits OCR-heavy tasks.

# When to cite

1. When arguing that **encoder pre-training strategy** has more impact than model scale for vision-language tasks.
2. When justifying **contrastive pre-training** of a vision encoder before joint multimodal fine-tuning.
3. When benchmarking efficient **vision-language models** on document and text-heavy visual QA tasks.
4. When discussing how **visual grounding** quality can be improved without increasing parameter count.

---
[[Artificial Intelligence|AI]]
[[LLM]]
[[Machine Learning|ML]]
