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

# Summary

Detecting AI-generated text without model access is the central challenge this paper solves. A random **"green list"** of tokens is selected before each generation step and softly promoted during sampling; a **statistical hypothesis test** on the proportion of green tokens then detects the watermark with interpretable p-values — no API access or model weights required. Tested on the **OPT model family**, the method produces negligible quality degradation while remaining robust to moderate text edits. Published at ICML 2023 with open-source code.

# Main points

1. A **green token list** is randomly selected per step and softly promoted during **sampling**.
2. Detection uses a **statistical test on green-token proportion**, requiring no model internals.
3. Evaluated on **OPT multi-billion parameter models** with negligible text quality impact.
4. Watermark is robust to moderate paraphrasing but can be defeated by **targeted rewriting attacks**.
5. Framework outputs **interpretable p-values**, enabling transparent and auditable detection.

# Takeaways

1. **No model access is needed** for detection — any third party with the secret key can verify output.
2. Soft promotion keeps generation quality intact — **watermarking and quality are not in tension**.
3. Robustness is bounded: aggressive paraphrasing **can strip watermarks**, limiting forensic guarantees.
4. The statistical test is **tunable** — strength of detectability can be traded against quality impact.
5. Practical deployment requires **key management** for the green-list randomness, a new operational concern for LLM providers.

---
[[LLM]]
[[GPT]]
[[On the Reliability of Watermarks for Large Language Models]]
