---
title:  LLM RAG Paradigms - Naive RAG, Advanced RAG & Modular RAG
created: Saturday 12th April 2025 21:12
aliases: 
tags:
  - rag
  - retrieval
  - embeddings
  - llm
---
- https://medium.com/@drjulija/what-are-naive-rag-advanced-rag-modular-rag-paradigms-edff410c202e
- Type: article
- Source: Medium · Dr Julija · Mar 2024 (digest of the Gao et al. 2024 survey)

---

# TL;DR

RAG systems evolved from a linear **index → retrieve → generate** pipeline (Naive) to optimized pipelines (Advanced) and finally composable modules such as search, memory, fusion and routing (Modular).

# Summary

**Naive RAG** chunks documents, embeds them into a vector store, retrieves the nearest chunks and prompts the [[LLM]]; it fails through poor retrieval, disjointed context and ungrounded answers. **Advanced RAG** adds **pre-retrieval** (data cleaning, chunking, metadata, index structure), **retrieval** (embedding fine-tuning, similarity metric) and **post-retrieval** steps (reranking, prompt compression). **Modular RAG** treats these techniques as swappable modules and adds new ones. The article summarizes [[Retrieval-Augmented Generation for Large Language Models - A Survey]].

# Key takeaways

1. **Naive RAG has three phases**: indexing (load, split, embed, store), retrieval (embed query, nearest vectors) and augmentation plus generation.
2. **Fix retrieval before generation**: clean data, tune **chunk size**, add **metadata**, and use sliding window, auto-merging or abstract embedding.
3. **Fine-tune the embedding model** on domain data (queries, corpus, relevant documents) and pick the similarity metric deliberately (cosine, L2, dot product).
4. **Post-process the context**: **rerank** chunks to keep the top-K, and compress noisy prompts with small language models.
5. **Compose modules**: search module (other sources, graphs), memory module, **fusion** (expanded queries plus reranking) and query **routing**.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[RAG]] | Overall framework, answers "what / when / how to use" retrieved data |
| [[VDB]] | ChromaDB, Pinecone and Weaviate store and search embeddings |
| [[Knowledge Graph]] | Graph indexing and a data source for the search module |
| [[RAG-Fusion - a New Take on Retrieval-Augmented Generation\|RAG-Fusion]] | The fusion module in practice |
| LlamaIndex, LangChain, Haystack | Libraries that provide rerankers |

# When to use

1. When explaining the **difference between Naive, Advanced and Modular RAG**.
2. When choosing which **pre- or post-retrieval optimization** to try first on a weak RAG.
3. When looking for a map of techniques before reading the full survey.

# Caveats

- Secondary source: a six-minute digest with no new experiments or numbers.

---
[[RAG]] [[LLM]] [[VDB]] [[Knowledge Graph]]
[[Modular RAG and RAG Flow - Part Ⅰ]] [[Modular RAG and RAG Flow - Part II]]
[[Retrieval-Augmented Generation for Large Language Models - A Survey]]
[[Better RAG results with Reciprocal Rank Fusion and Hybrid Search]]
