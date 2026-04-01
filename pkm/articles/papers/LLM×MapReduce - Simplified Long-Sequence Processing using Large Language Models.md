---
title: "LLM×MapReduce: Simplified Long-Sequence Processing using Large Language Models"
created: Wednesday 1st April 2026 12:30
aliases:
tags:
  - llm
  - reasoning
  - prompt-engineering
  - multi-hop-qa
  - long-context
---
- https://arxiv.org/pdf/2410.09342
- https://github.com/thunlp/LLMxMapReduce
- Source: arxiv

---

# TL;DR

**LLM×MapReduce** is a training-free divide-and-conquer framework that processes arbitrarily long documents by splitting them into chunks, extracting structured intermediate answers with **confidence scores**, and resolving inter-chunk conflicts at aggregation time.

# Summary

Large language models struggle with documents that exceed their effective **context window**, forcing a choice between truncation and expensive retraining. LLM×MapReduce splits long texts into chunks processed in a **Map stage** (extracting structured information with a confidence score per chunk), optionally compresses results through a **Collapse stage**, then resolves contradictions in a **Reduce stage** via in-context confidence calibration. On **InfiniteBench** (>100K token inputs), Llama3-70B with LLM×MapReduce scores 68.66% average — outperforming GPT-4 (57.34%) and all open-source long-context baselines — while handling sequences up to **1.28M tokens** with lower GPU memory overhead than standard decoding.

# Key contributions

1. Proposes **LLM×MapReduce**, a training-free three-stage (Map → Collapse → Reduce) pipeline enabling any LLM to process documents that exceed its native context limit without fine-tuning.
2. Introduces a **structured information protocol** — a four-field output (Extracted Information, Rationale, Answer, Confidence Score) — that preserves **inter-chunk dependencies** across the pipeline stages.
3. Demonstrates **in-context confidence calibration**, aligning chunk-level confidence scores to a consistent standard using prompt-embedded examples, enabling principled conflict resolution without parameter updates.
4. Shows scalability to **1.28M-token sequences** on a model with only 8K native context, achieving near-perfect retrieval (99.56%) and strong mathematical reasoning (91.43%) on InfiniteBench.

# When to cite

1. When arguing that **training-free methods** can match or exceed fine-tuned long-context LLMs on document understanding benchmarks.
2. When explaining how to resolve **contradictory evidence across chunks** in a divide-and-conquer long-document pipeline.
3. When discussing **inference efficiency** strategies for very long documents that avoid repeated full-context decoding and reduce GPU memory requirements.
4. When citing work on **structured prompting formats** that preserve reasoning chains across independently processed text segments.

---
[[LLM]]
[[Prompt Engineering]]
[[A Survey of Large Language Models]]
[[REACT - SYNERGIZING REASONING AND ACTING IN LANGUAGE MODELS]]
