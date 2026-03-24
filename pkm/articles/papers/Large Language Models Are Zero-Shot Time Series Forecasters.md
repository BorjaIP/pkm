---
title:  Large Language Models Are Zero-Shot Time Series Forecasters
created: Tuesday 31st October 2023 10:37
aliases:
tags:
  - llm
  - ml
---
- https://arxiv.org/abs/2310.07820
- Source: arxiv

---

# TL;DR

**LLMTime** demonstrates that GPT-3 and LLaMA-2 perform competitive zero-shot time series forecasting purely by treating numeric sequences as text tokens, with no fine-tuning required.

# Summary

Time series forecasting typically requires task-specific models trained on domain data. **LLMTime** shows that GPT-3 and LLaMA-2, given time series values encoded as carefully formatted **decimal text tokens**, perform competitive **zero-shot forecasting** with no fine-tuning. LLMs implicitly absorb **temporal patterns** from financial reports and narrative text in their pre-training corpora, enabling extrapolation of numeric sequences. Evaluated on Darts, ETTh, and Monash benchmarks, LLMTime matches or beats task-specific baselines in many settings through pure in-context sequence continuation.

# Key contributions

1. Introduces **LLMTime**, demonstrating zero-shot time series forecasting from pre-trained LLMs without any fine-tuning.
2. Shows that **decimal token encoding** format is a critical design choice that significantly impacts forecasting accuracy.
3. Provides evidence that LLMs implicitly encode **temporal patterns** absorbed from diverse pre-training corpora.
4. Establishes competitive results against **task-specific forecasting baselines** on Darts, ETTh, and Monash benchmarks.

# When to cite

1. When arguing that **LLMs have implicit temporal reasoning** capabilities transferable to time series tasks.
2. When exploring **zero-shot forecasting** alternatives that avoid training domain-specific models.
3. When discussing how **tokenization strategy** for numeric values affects LLM performance on quantitative tasks.
4. When motivating unified models that handle both **text and time series** within a single architecture.

---
[[Artificial Intelligence|AI]]
[[LLM]]
[[Machine Learning|ML]]
