---
title:  RAFT - Adapting Language Model to Domain Specific RAG
created: Thursday 18th July 2024 10:08
aliases:
tags:
  - rag
  - fine-tuning
  - llm
  - domain-adaptation
---
- https://arxiv.org/pdf/2403.10131
- Source: arxiv

---

# TL;DR

**RAFT** (Retrieval Augmented Fine-Tuning) trains LLMs to robustly ignore distractor documents in retrieved context by exposing them to mixed oracle and distractor passages with chain-of-thought rationales during supervised fine-tuning.

# Summary

Standard fine-tuning on clean documents does not prepare LLMs for the noisy context produced by real-world retrieval. RAFT closes this gap by training on mixed sets of **oracle documents** and **distractor passages**, teaching the model to identify and cite the correct source while ignoring irrelevant content. **Chain-of-thought rationales** in the training data make this reasoning explicit. RAFT outperforms both RAG-only and SFT-only baselines on domain-specific benchmarks PubMed, HotpotQA, and Gorilla, and is retriever-agnostic since only the generation stage is fine-tuned.

# Key contributions

1. Proposes **RAFT**, a fine-tuning recipe that exposes LLMs to mixed oracle and distractor documents to build robustness to noisy retrieval.
2. Introduces **chain-of-thought rationale supervision** that teaches the model to explicitly reason through which document supports the answer, providing an implicit citation mechanism.
3. Demonstrates that **standard SFT on clean documents** does not transfer to RAG settings and retrieval-context training is required.
4. Shows RAFT is **retriever-agnostic** by fine-tuning only the generation stage while leaving the retriever unchanged.

# When to cite

1. When applying **domain-specific fine-tuning** to a RAG system over a known closed corpus.
2. When arguing that models must be trained on **retrieved-context inputs** (not clean documents) to perform well with retrieval at inference.
3. When using **distractor training** to improve LLM robustness to imperfect retrieval precision.
4. When justifying **chain-of-thought supervision** as a method for improving answer attribution and interpretability in RAG.

---
[[LLM]]
[[Artificial Intelligence|AI]]
[[RAG]]
[[Generative AI]]
[[Prompt Engineering]]
