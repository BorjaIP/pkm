---
title:  Precise Zero-Shot Dense Retrieval without Relevance Labels
created: Friday 31st May 2024 19:33
aliases:
tags:
  - retrieval
  - zero-shot
  - dense-retrieval
  - embeddings
---
- https://arxiv.org/pdf/2212.10496
- Source: arxiv

---

# TL;DR

**HyDE** (Hypothetical Document Embeddings) achieves zero-shot dense retrieval competitive with supervised systems by having an LLM generate a hypothetical answer document and embedding it with **Contriever** for nearest-neighbor search.

# Summary

**HyDE** solves **zero-shot dense retrieval** by inverting the usual query-to-document matching direction. An instruction-following LLM generates a hypothetical answer document for the query — plausible in style and structure even if factually imprecise. A contrastive encoder (**Contriever**) then embeds that hypothesis into the document space, where nearest-neighbor search retrieves real passages. The hypothesis acts as a soft relevance signal that aligns query intent with document vocabulary, matching supervised dense retrieval on **BEIR** without any labeled data.

# Key contributions

1. Proposes **HyDE**, a zero-shot retrieval method that replaces query encoding with encoding of a hypothetically generated answer document.
2. Demonstrates that **factual correctness of the hypothesis is irrelevant** — only its embedding proximity to real documents matters.
3. Matches **supervised dense retrieval performance on BEIR** without any labeled relevance data.
4. Shows that larger instruction-following LLMs produce better hypotheses and improve recall, linking **generation quality to retrieval quality**.

# When to cite

1. When implementing **zero-shot dense retrieval** without labeled training data for a new domain.
2. When arguing that LLMs are useful as **retrieval preprocessors** even when they hallucinate, because factual accuracy is decoupled from embedding utility.
3. When evaluating **HyDE** as a strong baseline before investing in fine-tuned retrievers or hard-negative training.
4. When discussing **query expansion techniques** that require no thesaurus or domain-specific vocabulary resources.

---
[[Artificial Intelligence|AI]]
[[LLM]]
[[RAG]]
[[NLP]]
[[Prompt Engineering]]
