---
title:  On Efficient Training of Large-Scale Deep Learning Models - A Literature Review
created: Tuesday 31st October 2023 10:42
aliases:
tags:
  - ml
  - dl
---
- https://arxiv.org/abs/2304.03589
- Source: arxiv

---

# TL;DR

A literature review that surveys efficient large-scale deep learning training across five axes — data pipelines, model architecture, training optimizations, **parallelism strategies**, and infrastructure — with Megatron-LM and DeepSpeed as the primary framework references.

# Summary

Training large-scale deep learning models efficiently requires coordinating improvements across multiple system layers. This review organizes techniques along five axes: data pipeline efficiency, model architecture efficiency, training optimizations (**mixed precision**, gradient checkpointing, activation recomputation), **parallelism strategies** (data, model, pipeline, tensor), and infrastructure (communication optimization, fault tolerance). Frameworks **Megatron-LM** and **DeepSpeed** are analyzed as the dominant implementations. The review identifies automated efficiency tooling for parallelism strategy selection as a key open gap.

# Key contributions

1. Proposes a **five-axis taxonomy** for classifying large-scale training efficiency techniques across data, architecture, optimization, parallelism, and infrastructure.
2. Establishes **3D parallelism** (data + tensor + pipeline) as the recommended combination for near-linear scaling on large clusters.
3. Reviews **Megatron-LM and DeepSpeed** as the dominant frameworks and analyzes their respective trade-offs.
4. Identifies automated **parallelism strategy selection** as a critical open gap for practitioners.

# When to cite

1. When surveying **large-scale distributed training** techniques and needing a comprehensive taxonomy.
2. When justifying the use of **mixed precision training** or **gradient checkpointing** for memory reduction.
3. When selecting between **Megatron-LM and DeepSpeed ZeRO** based on model size and cluster topology.
4. When arguing that **communication overlap** (compute-while-transferring gradients) is essential for multi-node scaling.

---
[[Artificial Intelligence|AI]] [[Machine Learning]] [[Deep Learning]]
