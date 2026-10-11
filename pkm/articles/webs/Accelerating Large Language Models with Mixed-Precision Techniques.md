---
title:  Accelerating Large Language Models with Mixed-Precision Techniques
created: Monday 14th April 2025 21:05
aliases: 
tags:
  - gpu
  - dl
  - llm
---
- https://lightning.ai/pages/community/tutorial/accelerating-large-language-models-with-mixed-precision-techniques/
- Type: tutorial
- Source: Lightning AI · JP Hennessy · May 2023

---

# TL;DR

Switching Lightning Fabric to `16-mixed` or `bf16-mixed` precision cut DistilBERT fine-tuning from 21.75 to 7.25 minutes and used less memory, with no accuracy loss.

# Summary

**Mixed-precision training** computes in 16-bit and updates FP32 weights. The article compares FP64/FP32 (PyTorch default), FP16 (small range, overflows past 65,504) and BF16 (wider range, less precision, needs Ampere or newer). On a single A100, DistilBERT sentiment fine-tuning shows large speed and memory wins from mixed precision, while pure FP16 diverged (NaN loss). The same idea halves memory for LLaMA inference in BF16.

# Key takeaways

1. **FP16 mixed**: 7.25 min vs 21.75 min for FP32 and 4.31 GB vs 5.37 GB, accuracy 92.15% vs 89.92%.
2. **BF16 mixed**: slightly more memory than FP16, accuracy 92.61%, and more stable than pure 16-bit.
3. **Pure FP16 failed**: 2.87 GB and the fastest run, but accuracy dropped to 50.08% as loss became NaN.
4. **Matmul precision**: `torch.set_float32_matmul_precision("high"|"medium")` gave about 2.5x speed and half the memory for FP32 models on tensor-core GPUs.
5. **Inference**: LLaMA in BF16 ran 16.7 tokens/s at 13.5 GB against 11.5 tokens/s at 27 GB in FP32.
6. **One-line change** in Lightning: `Fabric(..., precision="16-mixed")`, `"bf16-mixed"` or `"16-full"`.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[Deep Learning]] | Training and inference workloads |
| [[LLM]] | DistilBERT and LLaMA examples |
| [[Nvidia]] | A100 and BF16 support |
| [[The Era of 1-bit LLMs - All Large Language Models are in 1.58 Bits]] | Extreme end of the precision trend |
| PyTorch, Lightning Fabric | Frameworks used |

# When to use

1. When **speeding up training or inference** with lower precision.
2. When choosing **FP16 vs BF16** for a GPU generation.
3. When explaining why pure 16-bit can fail.

# Caveats

- Single model, dataset and GPU; the accuracy gain is attributed to a possible regularising effect without proof, and loss scaling is not covered.

---
[[Deep Learning]] [[LLM]] [[Nvidia]]
[[GPU optimized techniques for training transformer models at-scale]]
[[Large Scale Distributed Model Training with Colossal AI and Lightning AI]]
[[QLORA - Efficient Finetuning of Quantized LLMs]]
