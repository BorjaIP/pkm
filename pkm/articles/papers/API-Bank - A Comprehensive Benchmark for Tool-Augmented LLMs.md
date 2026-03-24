---
title: API-Bank - A Comprehensive Benchmark for Tool-Augmented LLMs
created: Monday 5th February 2024 19:43
aliases:
tags:
  - llm
  - tool
---
- https://aclanthology.org/2023.emnlp-main.187.pdf
- Source: acl

---

# Summary

Tool-augmented LLMs must plan which APIs to call, retrieve them from a catalog, and execute calls correctly — yet no systematic benchmark existed for this three-stage pipeline. **API-Bank** provides 73 runnable API tools, 314 annotated dialogues with 753 API calls, and a 1,888-dialogue training set spanning 2,138 APIs across 1,000 domains. Evaluated models include **GPT-3, GPT-3.5, and GPT-4**: GPT-4 excels at planning while GPT-3.5 leads on retrieval. Fine-tuning Alpaca on the training set produces **Lynx**, which surpasses the base model by over 26 percentage points and approaches GPT-3.5 performance.

# Main points

1. Tool use requires three distinct skills: **planning, retrieval, and API call execution**.
2. **API-Bank** provides 73 runnable tools and 753 annotated API calls for systematic evaluation.
3. **GPT-4 excels at planning**; GPT-3.5 leads on retrieval — no single model dominates all dimensions.
4. Fine-tuning on the training set yields **Lynx**, outperforming Alpaca by 26+ percentage points.
5. Error analysis reveals significant gaps in **multi-step API chaining** and error recovery.

# Takeaways

1. **Planning and retrieval are separable skills** — evaluate and improve them independently when debugging tool use.
2. A 1,000-domain training set enables fine-tuned smaller models to **approach GPT-3.5** at lower cost.
3. **Runnable tools** with ground-truth calls expose failures that text-only evaluations hide entirely.
4. GPT-4's planning advantage suggests **instruction following quality** drives tool orchestration more than retrieval.
5. Multi-step API chaining remains the **hardest unsolved subproblem** for production tool-augmented systems.

---
[[LLM]]
[[Generative AI]]
[[Prompt Engineering]]
[[ART - Automatic multi-step reasoning and tool-use for large language models]]
[[An LLM Compiler for Parallel Function Calling]]
