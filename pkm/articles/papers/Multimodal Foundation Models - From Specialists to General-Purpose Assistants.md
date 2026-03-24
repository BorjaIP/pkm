---
title:  Multimodal Foundation Models - From Specialists to General-Purpose Assistants
created: Wednesday 27th September 2023 13:39
aliases:
tags:
  - llm
  - gpt
  - ml
---
- https://arxiv.org/pdf/2309.10020.pdf
- Source: arxiv

---

# TL;DR

This survey traces the evolution of multimodal AI from task-specific specialists to **general-purpose multimodal assistants**, organizing models by modality pairing and training strategy across vision-language, audio-language, and video-language systems.

# Summary

Multimodal AI has evolved from narrow specialists (OCR, captioning, VQA) toward unified systems that handle understanding, generation, and grounding across modalities. Models are organized by modality pairing (vision-language, audio-language, video-language) and by training strategy: **contrastive learning**, **generative pre-training**, and **instruction tuning**. Key architectural milestones — Flamingo, **BLIP-2**, and GPT-4V — illustrate how cross-modal generalization has advanced. Grounding and video-language understanding remain the most challenging capability gaps.

# Key contributions

1. Introduces a taxonomy organizing **multimodal models** by modality pairing and capability (understanding, generation, grounding).
2. Surveys the role of **instruction tuning** as the critical strategy enabling open-ended multimodal dialogue.
3. Analyzes BLIP-2's **Q-Former** as a lightweight bridge between frozen vision and language models.
4. Maps benchmark landscapes across modalities and identifies gaps in **fine-grained grounding** evaluation.
5. Demonstrates that **audio-visual alignment** requires modality-specific architectural design beyond scaling alone.

# When to cite

1. When looking for a comprehensive overview of **multimodal foundation model** architectures and training strategies.
2. When justifying the use of **instruction tuning** to enable open-ended vision-language interaction.
3. When discussing why **video-language understanding** lags behind image-language models.
4. When comparing lightweight bridging designs like **Q-Former** for connecting frozen encoders.

---
[[Artificial Intelligence|AI]]
[[LLM]]
[[Machine Learning|ML]]
[[GPT]]
