---
title:  A Watermark for Large Language Models
created: Tuesday 20th June 2023 18:29
aliases:
tags:
  - llm
  - gpt
  - ml
---
- https://arxiv.org/pdf/2301.10226.pdf
- https://github.com/jwkirchenbauer/lm-watermarking
- Source: arxiv

---

# TL;DR

A soft **green-token watermark** embedded during LLM sampling is detectable via a statistical hypothesis test with no model access required, published at ICML 2023.

# Summary

Detecting AI-generated text without model access is the central challenge this paper solves. A random **green list** of tokens is selected before each generation step and softly promoted during sampling; a **statistical hypothesis test** on the proportion of green tokens then detects the watermark with interpretable p-values — no API access or model weights required. Tested on the **OPT model family**, the method produces negligible quality degradation while remaining robust to moderate text edits.

# Key contributions

1. Proposes a **green-token watermarking scheme** that biases sampling toward a secret random token subset without requiring model retraining.
2. Introduces a **statistical detection test** based on green-token proportion that requires only the secret key, not model internals.
3. Demonstrates negligible text quality degradation on **OPT multi-billion parameter models**.
4. Establishes robustness bounds: the watermark survives moderate paraphrasing but can be defeated by **targeted rewriting attacks**.

# When to cite

1. When discussing methods for **detecting AI-generated text** without access to model weights or APIs.
2. When arguing that **watermarking and generation quality** are not fundamentally in tension.
3. When evaluating the robustness limits of **LLM output provenance** techniques against adversarial paraphrasing.
4. When comparing approaches to **LLM output attribution** that rely on statistical rather than cryptographic guarantees.

---
[[LLM]]
[[GPT]]
[[On the Reliability of Watermarks for Large Language Models]]
