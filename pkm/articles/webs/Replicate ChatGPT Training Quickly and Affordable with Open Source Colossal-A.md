---
title:  Replicate ChatGPT Training Quickly and Affordable with Open Source Colossal-A
created: Monday 14th April 2025 20:50
aliases: 
tags:
  - llm
  - rlhf
  - gpu
---
- https://company.hpc-ai.com/blog/colossal-ai-chatgpt
- Type: article
- Source: HPC-AI Tech blog · Feb 2023

---

# TL;DR

Colossal-AI's first ChatGPT-style RLHF code claims **7.73x faster training** and **10.3x larger single-GPU models** than plain PyTorch, with all three RLHF stages open source.

# Summary

The post introduces the open-source ChatGPT application in [[ColossalAI]]. It implements the InstructGPT pipeline: supervised fine-tuning, a reward model trained on ranked outputs, and PPO reinforcement learning. It supports Hugging Face GPT, OPT and BLOOM models and uses ZeRO and Gemini memory management with CPU offload to fit more parameters per GPU.

# Key takeaways

1. **Three stages implemented**: SFT, reward model, PPO, with the RL stage being the most complex.
2. **Claimed speed**: 7.73x training on a single multi-GPU server and 1.42x inference on one GPU, versus PyTorch.
3. **Claimed capacity**: up to 8B parameters on one GPU instead of about 780M (10.3x) on an A100 80GB; 120M models need about 1.62 GB.
4. **Hardware**: the 175B setup is claimed to need about half the 64 A100 80GB GPUs of the original approach.
5. **Usage**: create `ColossalAIStrategy(stage=3, placement_policy='cuda')`, build actor, critic and reward models in its init context, then `PPOTrainer(...).fit(prompts)`.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[ColossalAI]] | Framework implementing the pipeline |
| [[Nvidia]] | A100 and RTX 3080 benchmarks |
| [[LLM]] | GPT, OPT and BLOOM base models |
| ZeRO, Gemini | Memory optimisation and offload strategies |

# When to use

1. When you want the **first Colossal-AI RLHF setup** and its claimed efficiency.
2. When comparing memory strategies for **fine-tuning on limited GPUs**.
3. When reading the follow-up in [[ColossalChat - An Open-Source Solution for Cloning ChatGPT With a Complete RLHF Pipeline]].

# Caveats

- Vendor benchmark numbers from the framework's authors; licence is not stated on the page.

---
[[ColossalAI]] [[LLM]] [[Nvidia]]
[[ColossalChat - An Open-Source Solution for Cloning ChatGPT With a Complete RLHF Pipeline]]
[[Large Scale Distributed Model Training with Colossal AI and Lightning AI]]
[[On Efficient Training of Large-Scale Deep Learning Models - A Literature Review]]
