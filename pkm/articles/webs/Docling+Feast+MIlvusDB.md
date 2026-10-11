---
title:  Docling+Feast+MIlvusDB
created: Saturday 12th April 2025 21:12
aliases: 
tags:
  - rag
  - retrieval
  - vector-search
  - feature-store
---
- https://github.com/feast-dev/feast/blob/master/examples/rag-docling/docling-quickstart.ipynb
- Type: repo
- Source: GitHub · Feast example notebook (`examples/rag-docling`)

---

# TL;DR

A notebook that uses **Feast** to load [[VDB|Milvus]] with Docling-parsed PDF chunks and then answers questions with a [[RAG]] prompt.

# What it does

Chunks parsed from PDFs by Docling are stored as parquet and written to Feast's online store, a local Milvus Lite database configured in `feature_store.yaml` (384-dimension embeddings, FLAT index). A query is embedded with a Sentence Transformer, the top-k chunks are retrieved with cosine distance and the formatted context goes to `gpt-4o-mini`.

# Key takeaways

1. **Register definitions**: `feast apply` creates entities and feature views and deploys the online store.
2. **Ingest**: `write_to_online_store` for a plain `FeatureView`, optionally with Docling `transform_on_write`.
3. **Retrieve**: `retrieve_online_documents_v2` with embeddings, comparing `FeatureView` against `OnDemandFeatureView`.
4. **Generate**: build a prompt from retrieved chunks and call the OpenAI chat completions API.
5. **Requirements**: Python 3.11, `feast[nlp]`, Milvus Lite, Docling and `OPENAI_API_KEY`.
6. **Example result**: asking for a paper's authors returned the four IBM Research authors.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[Feature Stores]] | Feast manages the online features and vectors |
| [[VDB]] | Milvus Lite as the vector store |
| [[RAG]] | Retrieval plus generation flow |
| [[LLM]] | OpenAI model that answers |

# When to use

1. When you want a **feature store as the RAG retrieval layer**.
2. When you need an **end-to-end example** with Docling, Feast and Milvus.
3. When comparing with a classic stack such as [[Do we really need a specialized vector database]].

# Caveats

- Some retrieved on-demand chunks were empty, which suggests the transform path needs checking; the intro text mentions city summaries but the data are research-paper chunks.

---
[[RAG]] [[Feature Stores]] [[VDB]] [[LLM]]
[[Do we really need a specialized vector database]]
[[Better RAG results with Reciprocal Rank Fusion and Hybrid Search]]
