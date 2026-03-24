---
title:  DiT - Self-supervised Pre-training for Document Image Transformer
created: Saturday 12th April 2025 13:04
aliases:
tags:
  - ml
  - dl
---
- https://arxiv.org/pdf/2203.02378
- Source: arxiv

---

# TL;DR

**DiT** applies BEiT-style masked image modeling to document images, achieving state-of-the-art on document classification, layout analysis, and table detection through domain-specific self-supervised pre-training on 42M unlabeled document images.

# Summary

General vision transformers underperform on document understanding because natural-image pre-training doesn't capture document-specific structure: fonts, tables, and dense layout. DiT addresses this by adapting **masked image modeling** (BEiT) to pre-train on the IIT-CDIP corpus of **42M document images** without labels. The result is a single model that achieves state-of-the-art on **RVL-CDIP classification**, **PubLayNet layout analysis**, and table detection, demonstrating that domain-specific pre-training data matters more than scale on natural images.

# Key contributions

1. Proposes **DiT**, the first document-domain self-supervised vision transformer pre-trained exclusively on document images.
2. Introduces adaptation of **BEiT masked image modeling** to the document domain, showing it transfers beyond natural images.
3. Demonstrates that **IIT-CDIP** (42M images) provides sufficient domain signal to outperform general vision baselines without labels.
4. Establishes state-of-the-art results on three distinct document tasks from a single pre-trained model: classification, layout analysis, and table detection.

# When to cite

1. When justifying why a **document understanding model** should use domain-specific rather than general vision pre-training.
2. When comparing **self-supervised pre-training strategies** for structured or domain-specific image corpora.
3. When looking for a backbone for **document layout analysis** or table detection tasks.
4. When arguing that **masked image modeling** generalizes effectively beyond natural image domains.

---
[[Machine Learning|ML]]
[[Artificial Intelligence|AI]]
[[articles/webs/DiT - Self-supervised Pre-training for Document Image Transformer|DiT - Self-supervised Pre-training for Document Image Transformer]]
