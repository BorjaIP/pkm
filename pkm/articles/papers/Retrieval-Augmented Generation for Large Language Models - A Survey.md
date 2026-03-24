---
title: Retrieval-Augmented Generation for Large Language Models - A Survey
created: Friday 9th February 2024 08:45
aliases:
tags:
  - llm
  - rag
  - survey
  - nlp
---
- https://arxiv.org/pdf/2312.10997.pdf
- Source: arxiv

---

# TL;DR

A comprehensive survey that categorizes **RAG** systems into three paradigms — Naive, **Advanced**, and **Modular RAG** — and maps the full design space from indexing through evaluation.

# Summary

Retrieval-augmented generation systems suffer from fragmented design decisions across indexing, retrieval, augmentation, and generation. This survey imposes structure by defining three evolutionary paradigms: **Naive RAG**, **Advanced RAG**, and **Modular RAG**. It covers sparse and dense retrieval, hybrid methods, chunking strategies, and augmentation techniques, then surveys evaluation frameworks including **RAGAS** and ARES. Persistent challenges such as hallucination, multi-hop reasoning degradation, and latency are analyzed alongside downstream applications in QA, code generation, and summarization.

# Key contributions

1. Proposes a **three-paradigm taxonomy** (Naive, Advanced, Modular RAG) that structures the entire RAG design space.
2. Introduces a systematic review of **indexing strategies** — chunking, metadata, hierarchical — as a first-class design axis.
3. Establishes **hybrid retrieval** (BM25 + bi-encoder) as consistently superior to either sparse or dense alone.
4. Surveys automated evaluation frameworks **RAGAS and ARES** for reference-free assessment of RAG pipelines.
5. Identifies multi-hop reasoning as the primary open challenge where current pipelines degrade with reasoning depth.

# When to cite

1. When framing a **RAG system design** and needing a taxonomy to position architectural choices.
2. When justifying the use of **hybrid retrieval** over purely sparse or dense methods.
3. When selecting an **automated evaluation framework** for a RAG pipeline without human annotation.
4. When arguing that **retrieval quality**, not generation, is the primary source of hallucination in RAG systems.

---
[[LLM]]
[[RAG]]
[[Generative AI]]
[[Prompt Engineering]]
[[ARAGOG - Advanced RAG Output Grading]]
[[RAG-Fusion - a New Take on Retrieval-Augmented Generation]]
