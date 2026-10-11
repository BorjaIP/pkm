---
title:  Understanding the Fundamental Limitations of Vector-Based Retrieval for Building LLM-Powered Chatbots— Part 1-3
created: Monday 14th April 2025 21:06
aliases: 
tags:
  - vector-search
  - rag
  - embeddings
  - db
---
- https://medium.com/thirdai-blog/understanding-the-fundamental-limitations-of-vector-based-retrieval-for-building-llm-powered-48bb7b5a57b3
- Type: article
- Source: ThirdAI blog (Medium) · Anshu · Jun 2023 (part 1 of 3)

---

# TL;DR

The standard embedding plus vector database pipeline for domain chatbots is **costly, privacy-leaky and brittle**, because every text chunk is embedded, copied and locked to one embedding model.

# Summary

Chatbots over private corpora ground [[GPT]] answers by retrieving chunks: split the corpus, embed each chunk, store text and vector in a [[VDB|vector database]], then at query time embed the question, run approximate nearest-neighbour search and prompt the model. The author lists the weaknesses: re-indexing everything whenever the embedding model changes, two copies of all data in two services, latency that sums three stages, and heavy bills. A PubMed example (about 100M chunks) is priced at roughly $7-8k a month for the database plus about $125k per embedding run.

# Key takeaways

1. **Embeddings tie you to one model**: any change in model or dimension requires re-indexing the whole corpus.
2. **Privacy exposure**: all text goes to both the embedding provider and the vector store, creating duplicate copies.
3. **Latency is additive**: question embedding + vector search + generation.
4. **Cost scales with tokens**: PubMed-scale (35M abstracts, ~25B tokens) is estimated at about $125,000 per embedding pass plus monthly database and query fees.
5. **Prompting grounds answers** in retrieved text and limits hallucination, but the hard part is retrieving the right chunk.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[VDB]] | Stores embeddings for approximate near-neighbour search |
| [[RAG]] | The retrieve-then-generate pattern |
| [[GPT]] | Generator, limited by a 4,096-token context at the time |
| Pinecone, OpenAI embeddings | Services used in the cost estimate |

# When to use

1. When **estimating the cost** of a RAG chatbot at enterprise scale.
2. When listing the **operational weaknesses of vector databases** for an architecture review.
3. When reading the series in order: continues in [[Neural Databases - A Next Generation Context Retrieval System for Building Specialized AI-Agents with ChatGPT — Part 2-3]].

# Caveats

- Vendor series that sets up its own product as the answer; prices are 2023 estimates.
- Only part 1 is summarised here; parts 2 and 3 are separate posts.

---
[[VDB]] [[RAG]] [[LLM]]
[[Neural Databases - A Next Generation Context Retrieval System for Building Specialized AI-Agents with ChatGPT — Part 2-3]]
[[Do we really need a specialized vector database]]
