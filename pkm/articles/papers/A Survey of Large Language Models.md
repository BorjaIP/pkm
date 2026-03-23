---
title:  A Survey of Large Language Models
created: Monday 24th April 2023 19:20
aliases:
tags:
  - llm
  - ml
  - dl
  - gpt
---
- https://arxiv.org/pdf/2303.18223.pdf
- Source: arxiv

---

# Summary

Beyond a critical parameter scale, language models exhibit **emergent capabilities** absent in smaller counterparts — qualitatively better reasoning, instruction following, and few-shot generalization. This 144-page survey maps the full LLM lifecycle: **pre-training** (data curation, architecture choices, training recipes), **adaptation tuning** (instruction tuning, RLHF, parameter-efficient methods), **utilization** (in-context learning, chain-of-thought prompting), and **capacity evaluation** across standard benchmarks. It catalogs publicly available resources, analyzes **ChatGPT's** impact on the field, and closes with a structured discussion of open research challenges including hallucination, alignment, and efficiency.

# Main points

1. **Emergent capabilities** arise only past a parameter threshold, making scale a qualitative, not just quantitative, factor.
2. **Instruction tuning** and **RLHF** are the primary techniques for turning a pre-trained model into a usable assistant.
3. **In-context learning** and **chain-of-thought prompting** are the dominant utilization strategies requiring no gradient updates.
4. Survey covers over 1,000 references across pre-training, tuning, utilization, and evaluation as of early 2023.
5. Open challenges — **hallucination**, alignment, interpretability, and inference cost — remain largely unsolved.

# Takeaways

1. Scaling laws alone do not produce safe or helpful models — **alignment techniques** (RLHF, instruction tuning) are non-optional.
2. **In-context learning** is a first-class design primitive: structure prompts carefully before reaching for fine-tuning.
3. Benchmark scores are upper bounds; teams should run **domain-specific evaluations** to measure real-world performance gaps.
4. **Data quality for pre-training** has disproportionate downstream impact — filtering and curation matter more than raw volume.
5. The emergent-abilities framing implies smaller models **cannot substitute** for large ones on complex reasoning tasks regardless of prompting tricks.

---
[[LLM]]
[[GPT]]
[[Deep Learning]]
[[Machine Learning]]
[[Generative AI]]
[[Prompt Engineering]]
[[Retrieval-Augmented Generation for Large Language Models - A Survey]]
[[Prompting Frameworks for Large Language Models - A Survey]]
