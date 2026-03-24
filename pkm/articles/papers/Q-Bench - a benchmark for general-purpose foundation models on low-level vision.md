---
title:  Q-Bench - a benchmark for general-purpose foundation models on low-level vision
created: Wednesday 27th September 2023 14:11
aliases:
tags:
  - llm
  - gpt
  - ml
---
- https://arxiv.org/pdf/2309.14181.pdf
- Source: arxiv

---

# TL;DR

**Q-Bench** introduces two datasets — LLVisionQA and LLDescribe — that expose a systematic gap between current multimodal LLMs and human performance on low-level visual quality perception and distortion reasoning.

# Summary

Multimodal LLMs perform well on high-level semantic tasks but struggle with **low-level visual perception**: quality assessment, distortion recognition, and comparative quality judgment. Q-Bench introduces **LLVisionQA** (2,990 images with open-ended and yes/no questions) and **LLDescribe** (499 images for quality description generation) to evaluate this capability. Evaluated MLLMs score substantially below **human performance** on fine-grained perceptual tasks, revealing that high benchmark scores on semantic understanding do not imply competence in **perceptual quality reasoning**.

# Key contributions

1. Introduces **LLVisionQA**, a 2,990-image dataset targeting low-level quality perception with open-ended and binary questions.
2. Introduces **LLDescribe**, a 499-image dataset for evaluating quality-aware descriptive caption generation.
3. Demonstrates a systematic gap between current MLLMs and **human performance** on low-level perceptual tasks.
4. Establishes **distortion recognition** and comparative quality judgment as underexplored MLLM capability dimensions.

# When to cite

1. When evaluating **multimodal LLMs** on perceptual quality tasks rather than semantic understanding.
2. When arguing that existing vision benchmarks fail to capture **low-level visual perception** capabilities.
3. When discussing the need for **quality-aware training supervision** to improve MLLM perceptual reasoning.
4. When benchmarking foundation models on **image quality assessment** or distortion recognition tasks.

---
[[Artificial Intelligence|AI]]
[[LLM]]
[[Machine Learning|ML]]
[[GPT]]
