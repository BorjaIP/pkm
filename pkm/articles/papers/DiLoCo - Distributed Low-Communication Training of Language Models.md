---
title: "DiLoCo: Distributed Low-Communication Training of Language Models"
created: Wednesday 1st April 2026 14:00
aliases:
tags:
  - llm
  - fl
  - dl
  - org-deepmind
---
- https://arxiv.org/abs/2311.08105
- Source: arxiv

---

# TL;DR

**DiLoCo** adapts federated averaging to LLM pretraining — using **AdamW** as an inner optimizer and **Nesterov momentum** as an outer optimizer across isolated compute islands — matching synchronous data-parallel training while communicating **500× less**.

# Summary

Standard LLM training demands thousands of co-located accelerators exchanging gradients every step, making large clusters fragile and expensive to maintain. DiLoCo reframes pretraining as a federated optimization problem: each worker independently runs H=500 **AdamW** inner steps on its local data shard, then workers synchronize pseudo-gradients via a shared **Nesterov momentum** outer optimizer. On the C4 dataset, 8 workers achieve **15.02 perplexity** versus 15.30 for synchronous data parallelism at the same wall-clock time and compute — while reducing inter-worker bandwidth by **500×**. The method is robust to non-i.i.d. data partitions, mid-training changes in worker availability, and up to 50% dropped communication rounds.

# Key contributions

1. Proposes **DiLoCo**, a distributed optimizer combining H=500 **AdamW** inner steps per worker with a **Nesterov momentum** outer update — the first federated method shown to match synchronous training at transformer scale.
2. Demonstrates a **500× communication reduction** over data parallelism while matching or exceeding perplexity at equivalent compute, across 60M–400M parameter models.
3. Shows that **non-i.i.d. data distribution** across workers poses no meaningful degradation, contradicting prior conclusions that local SGD fails at scale.
4. Establishes that **adaptive compute pools** — workers dynamically joining or leaving mid-training — affect final quality only through total compute budget, enabling resilient heterogeneous cluster training.
5. Identifies DiLoCo with k=1 as equivalent to the **Lookahead optimizer**, unifying federated and single-device optimization perspectives.

# When to cite

1. When arguing that **LLM pretraining can be distributed across geographically separated or poorly-connected compute clusters**.
2. When justifying **federated averaging for large-scale language model training** and need evidence it scales to 400M+ parameters.
3. When comparing **communication efficiency** of distributed optimization strategies — DiLoCo is the key reference for 500× reduction vs. data parallelism.
4. When supporting the choice of **Nesterov momentum over Adam** as an outer optimizer in federated learning settings.

---
[[LLM]] [[Deep Learning]] [[Machine Learning]] [[ColossalAI]]
[[On Efficient Training of Large-Scale Deep Learning Models - A Literature Review]]
[[When Federated Learning Meets Blockchain - A New Distributed Learning Paradigm]]
