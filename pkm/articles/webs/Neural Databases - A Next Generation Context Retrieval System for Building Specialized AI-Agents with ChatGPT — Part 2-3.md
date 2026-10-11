---
title: Neural Databases - A Next Generation Context Retrieval System for Building Specialized AI-Agents with ChatGPT — Part 2-3
created: Monday 14th April 2025 20:47
aliases: 
tags:
  - vector-search
  - retrieval
  - rag
  - db
---
- https://medium.com/thirdai-blog/neural-database-next-generation-context-retrieval-system-for-building-specialized-ai-agents-with-861ffa0516e7
- Type: article
- Source: ThirdAI blog (Medium) · Anshu · Jun 2023 (part 2 of 3)

---

# TL;DR

A **neural database** replaces embeddings plus ANN search with a network trained to predict hash-bucket keys for text, giving hash-map insertion and deletion and a much smaller index.

# Summary

For a PubMed-sized corpus (100M chunks of ~250 tokens) embeddings are heavy objects: about 600 GB at 1,500 dimensions, against 200 GB of raw text, and graph-based ANN indexes such as HNSW are slow to update and hard to debug. The proposed alternative treats retrieval as a learned prediction problem: a neural network maps text to discrete keys ("buckets"), chunks are stored in a key-value table, and a query returns the top buckets' chunk IDs, ranked and passed to the LLM. The author claims a 2.5B-parameter model indexes PubMed in under 20 GB.

# Key takeaways

1. **Embeddings are expensive**: storage can exceed the raw text, and high-dimensional ANN is slow or inaccurate (curse of dimensionality).
2. **Updates and deletes are painful** in HNSW-style graph indexes, so incremental changes are fragile.
3. **Retrieval failures are hard to diagnose**: missing chunk, poor embeddings or ANN misses look the same.
4. **Learn the index end to end**: train a network on semantically related text pairs with cross-entropy to predict bucket keys; index size scales logarithmically with the number of chunks.
5. **Operate it like a normal DB**: insertion, deletion and sharding are plain key-value operations, with claimed 10-100x faster retrieval on CPUs.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[VDB]] | The embedding-based approach being criticised |
| [[RAG]] | Retrieval stage that gets replaced |
| [[GPT]] | Consumer of the retrieved chunks |
| HNSW / ANN | Approximate neighbour indexes whose limits are discussed |

# When to use

1. When arguing the **trade-offs of embedding-free retrieval**.
2. When estimating **embedding storage** for large corpora.
3. When explaining why **updates and deletes** are hard in vector indexes.

# Caveats

- Vendor claims (compression, speed) come without independent benchmarks.
- Part 3 describing the product is not covered here.

---
[[VDB]] [[RAG]] [[GPT]]
[[Understanding the Fundamental Limitations of Vector-Based Retrieval for Building LLM-Powered Chatbots— Part 1-3]]
[[Do we really need a specialized vector database]]
