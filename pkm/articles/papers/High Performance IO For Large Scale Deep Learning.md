---
title:  High Performance IO For Large Scale Deep Learning
created: Monday 24th April 2023 20:25
aliases:
tags:
  - ml
  - dl
---
- https://arxiv.org/ftp/arxiv/papers/2001/2001.01858.pdf
- Source: arxiv

---

# TL;DR

This paper identifies the **I/O bottleneck** as a primary cause of GPU underutilization in large-scale deep learning and proposes parallel prefetching, cache-aware sharding, and tiered storage hierarchies to achieve near-linear GPU utilization scaling.

# Summary

GPU utilization in large training clusters drops when data preprocessing and loading cannot keep pace with compute. This paper analyzes storage bandwidth requirements for ResNet, BERT, and recommendation models, demonstrating that the **I/O bottleneck** is frequently the true training bottleneck. Proposed optimizations include **parallel prefetching** to overlap loading with computation, **cache-aware data sharding** to minimize redundant cross-node reads, compression-aware formats, and **tiered storage hierarchies** (NVMe → SSD → HDD → network) matched to data access hotness. Results show near-linear GPU utilization scaling without I/O stalls on large clusters.

# Key contributions

1. Demonstrates that the **I/O bottleneck** — not compute — causes GPU underutilization in large-scale training for multiple model families.
2. Proposes **parallel prefetching** as the highest-leverage optimization for overlapping data loading with GPU computation.
3. Introduces **cache-aware data sharding** to minimize redundant cross-node reads in distributed training jobs.
4. Establishes a **tiered storage hierarchy** framework matching data hotness to storage speed for near-linear scaling.

# When to cite

1. When profiling a training pipeline and arguing that **I/O throughput** should be measured before optimizing compute.
2. When justifying **parallel prefetching** as the primary optimization for I/O-bound training workloads.
3. When designing **data sharding strategies** for distributed training to avoid redundant cross-node transfers.
4. When arguing that **storage format choice** (TFRecord, WebDataset, etc.) significantly impacts sequential read performance.

---
[[Machine Learning]] [[Deep Learning]]
