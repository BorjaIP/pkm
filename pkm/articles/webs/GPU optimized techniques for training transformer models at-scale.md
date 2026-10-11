---
title:  GPU optimized techniques for training transformer models at-scale
created: Saturday 12th April 2025 18:57
aliases: 
tags:
  - gpu
  - dl
  - llm
  - transformer
---
- https://github.com/NVIDIA/Megatron-LM
- Type: repo
- Source: GitHub · NVIDIA · Apache-2.0

---

# TL;DR

**Megatron-LM** and **Megatron Core** are NVIDIA's reference code and composable library for training very large [[Transformers]] with tensor, pipeline, data, expert and context parallelism.

# What it does

Megatron-LM is the reference implementation with ready training scripts; Megatron Core provides GPU-optimised building blocks for custom frameworks; Megatron Bridge converts checkpoints between Hugging Face and Megatron formats. It supports mixed precision (FP16, BF16, FP8, FP4), FSDP/DDP, overlap of communication and compute, post-training and RLHF, and models such as GPT, Mamba, hybrid and vision-language families.

# Key takeaways

1. **Parallelism toolbox**: tensor (TP), pipeline (PP), data (DP), expert (EP, for MoE) and context (CP) parallelism.
2. **Scale claims**: models from about 2B to 462B parameters, up to 47% MFU on H100 clusters, and a 462B model benchmarked on 6,144 H100s.
3. **Strong scaling**: GPT-3 (175B) from 96 to 4,608 H100s drops from 47% to 42% MFU as communication grows.
4. **Dynamic context parallelism** gives up to 1.48x speedup on variable-length sequences.
5. **Install**: `uv pip install megatron-core` or from source (limit compile jobs with `MAX_JOBS`).
6. **Entry points**: `pretrain_gpt.py`, `pretrain_mamba.py`, `pretrain_hybrid.py`, `pretrain_vlm.py`.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[Nvidia]] | Maintainer and target hardware (H100) |
| [[Transformers]] | Architecture trained at scale |
| [[Deep Learning]] | Training workloads |
| [[ColossalAI]] | Alternative large-scale training framework |
| [[On Efficient Training of Large-Scale Deep Learning Models - A Literature Review]] | Survey of the same techniques |

# When to use

1. When you need the **parallelism vocabulary** (TP/PP/DP/EP/CP) for LLM training.
2. When comparing **frameworks for large-scale pretraining**.
3. When looking up MFU figures at 100s-1000s of GPUs.

# Caveats

- Numbers come from NVIDIA's own runs, measured without training to convergence; the repo changes quickly (dev and main branches).

---
[[Nvidia]] [[Deep Learning]] [[Transformers]] [[LLM]]
[[Large Scale Distributed Model Training with Colossal AI and Lightning AI]]
[[Accelerating Large Language Models with Mixed-Precision Techniques]]
[[DiLoCo - Distributed Low-Communication Training of Language Models]]
