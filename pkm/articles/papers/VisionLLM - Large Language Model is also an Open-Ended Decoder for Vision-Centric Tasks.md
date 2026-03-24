---
title:  VisionLLM - Large Language Model is also an Open-Ended Decoder for Vision-Centric Tasks
created: Wednesday 27th September 2023 14:13
aliases:
tags:
  - llm
  - gpt
  - ml
---
- https://arxiv.org/pdf/2305.11175.pdf
- Source: arxiv

---

# TL;DR

**VisionLLM** unifies detection, segmentation, captioning, and VQA under a single LLM autoregressive decoder by expressing all tasks as natural language instructions, eliminating task-specific heads entirely.

# Summary

Vision models traditionally require separate task-specific heads for detection, segmentation, captioning, and VQA. **VisionLLM** eliminates this by routing all vision tasks through a single **LLM autoregressive decoder**, where task instructions are natural language commands and outputs — bounding box coordinates, class tokens, and text — are generated in the same decoding pass. This enables **open-ended instruction following** for vision tasks without architectural switches. On COCO detection, VisionLLM surpasses specialist models while remaining competitive on captioning, all from one unified architecture.

# Key contributions

1. Proposes using a single **LLM decoder** for heterogeneous vision tasks without any task-specific heads.
2. Introduces **natural language task instructions** as the universal interface replacing task-specific prompts and switches.
3. Demonstrates **autoregressive coordinate prediction** as a viable alternative to regression-based detection heads.
4. Shows that a unified architecture surpasses specialist models on **COCO detection** while remaining competitive on captioning.

# When to cite

1. When arguing that **LLM decoders** can generalize across heterogeneous vision output types (coordinates, classes, text).
2. When comparing unified generalist architectures against **task-specific vision heads** for detection and segmentation.
3. When discussing **open-ended instruction following** as a paradigm for multi-task vision models.
4. When looking for evidence that **autoregressive bounding box prediction** matches regression-based detection at scale.

---
[[Artificial Intelligence|AI]]
[[LLM]]
[[Machine Learning|ML]]
[[GPT]]
