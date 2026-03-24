---
title: QLORA - Efficient Finetuning of Quantized LLMs
created: Tuesday 24th October 2023 16:18
aliases:
tags:
  - llm
  - ml
  - fine-tuning
---
- https://arxiv.org/pdf/2305.14314.pdf
- Source: arxiv
- https://www.youtube.com/watch?v=pov3pLFMOPY

---

# TL;DR

**QLoRA** enables fine-tuning of 65B-parameter LLMs on a single 48GB GPU by combining a frozen 4-bit NF4 quantized base model with full-precision LoRA adapters and three memory innovations.

# Summary

Fine-tuning large LLMs requires memory far exceeding typical hardware. QLoRA solves this by freezing the base model in **4-bit NormalFloat (NF4)** quantization — information-theoretically optimal for normally distributed weights — and training only small **LoRA adapters** in BF16. Three complementary innovations manage memory: NF4 quantization, **double quantization** (quantizing the quantization constants), and **paged optimizers** to absorb gradient checkpointing memory spikes. The resulting Guanaco models, fine-tuned from LLaMA 65B, are competitive with ChatGPT on the Vicuna benchmark.

# Key contributions

1. Proposes **NF4 (4-bit NormalFloat)** quantization as information-theoretically optimal for normally distributed pretrained weights.
2. Introduces **double quantization** — quantizing the quantization constants themselves — as a low-overhead memory reduction.
3. Introduces **paged optimizers** to handle GPU memory spikes during gradient checkpointing without training crashes.
4. Demonstrates that combining frozen **4-bit base model + BF16 LoRA adapters** enables 65B-parameter fine-tuning on a single 48GB GPU.

# When to cite

1. When fine-tuning a large LLM on **limited GPU hardware** and justifying the 4-bit quantization + LoRA approach.
2. When arguing that **NF4 should be preferred over INT4** for quantizing normally distributed pretrained weights.
3. When applying **double quantization** to reduce memory overhead of quantization constants.
4. When decoupling **model scale from hardware requirements** to democratize fine-tuning of frontier models.

---
[[LLM]] [[Artificial Intelligence|AI]] [[Machine Learning]]
