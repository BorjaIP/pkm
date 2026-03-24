---
title:  Foundational Models Defining a New Era in Vision - A Survey and Outlook
created: Wednesday 27th September 2023 13:40
aliases:
tags:
  - llm
  - gpt
  - ml
---
- https://arxiv.org/pdf/2307.13721.pdf
- Source: arxiv

---

# TL;DR

This survey maps the shift from task-specific computer vision models to **general-purpose vision foundation models**, covering architectures, training paradigms, and adaptation strategies across recognition, segmentation, detection, generation, and video understanding.

# Summary

Task-specific computer vision models are being superseded by **vision foundation models** that generalize across tasks via large-scale pre-training. The survey covers dominant architectures (ViT, SAM, CLIP, DINO, Florence) and three training paradigms: **contrastive learning**, **masked prediction**, and supervised pre-training. Adaptation strategies — prompting, fine-tuning, and adapters — bridge foundation models to downstream tasks. Open challenges including **open-vocabulary understanding**, efficiency, and robustness define the current research frontier.

# Key contributions

1. Provides a unified taxonomy of **vision foundation model** architectures spanning ViT, SAM, CLIP, DINO, and Florence.
2. Systematically compares three pre-training paradigms — **contrastive, masked prediction, and supervised** — across tasks and datasets.
3. Surveys adaptation strategies including **parameter-efficient fine-tuning** and prompting for downstream task transfer.
4. Identifies **open-vocabulary understanding** and robustness under distribution shift as primary unsolved challenges.
5. Extends coverage to video and multimodal tasks, exposing limits of image-only foundation approaches.

# When to cite

1. When providing background on the landscape of **vision foundation model** architectures and training paradigms.
2. When comparing **contrastive vs. masked prediction** pre-training for vision tasks.
3. When justifying the use of **adapter-based fine-tuning** over full retraining for vision models.
4. When discussing open challenges in **open-vocabulary object recognition** or distribution shift robustness.

---
[[Artificial Intelligence|AI]]
[[LLM]]
[[Machine Learning|ML]]
[[GPT]]
