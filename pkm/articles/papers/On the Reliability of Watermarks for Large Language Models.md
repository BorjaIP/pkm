---
title:  On the Reliability of Watermarks for Large Language Models
created: Tuesday 20th June 2023 18:29
aliases:
tags:
  - llm
  - gpt
---
- https://arxiv.org/pdf/2306.04634.pdf
- Source: arxiv

---

# TL;DR

This paper stress-tests LLM watermarking schemes — including the Kirchenbauer **green-token watermark** — against practical attacks and shows that LLM-based paraphrasing reliably removes the signal below detection thresholds, exposing a fundamental robustness-quality tradeoff.

# Summary

Watermarking LLM outputs is proposed as a provenance signal, but how robust are these schemes against adversarial removal? This paper evaluates the **green-token watermark** and related schemes against paraphrasing, translation, emoji insertion, and synonym substitution. **LLM-based paraphrasing** is the most effective attack, defeating watermarks with moderate quality loss. The paper quantifies the **robustness-quality tradeoff** — stronger watermarks degrade output quality; weaker ones are easy to remove — and proposes **adversarial evaluation protocols** as a standard that watermark claims must meet to be credible.

# Key contributions

1. Demonstrates that the **green-token watermark** is fragile under LLM-based paraphrasing, which removes the signal below detection thresholds.
2. Systematically evaluates multiple attack vectors — **paraphrasing, translation, emoji insertion, synonym substitution** — against watermark detection.
3. Quantifies the fundamental **robustness-quality tradeoff** inherent to LLM watermarking schemes.
4. Proposes **adversarial evaluation protocols** as a required standard for future watermark reliability claims.

# When to cite

1. When evaluating the **robustness of LLM watermarking** schemes against realistic adversarial removal attacks.
2. When arguing that **LLM-based paraphrasing** is a low-cost, widely accessible watermark removal attack that any scheme must address.
3. When discussing the **robustness-quality tradeoff** inherent in content provenance techniques for LLM outputs.
4. When proposing or critiquing **adversarial benchmarks** for evaluating watermark reliability in the literature.

---
[[LLM]]
[[A Watermark for Large Language Models]]
