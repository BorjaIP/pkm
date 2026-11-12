---
title:  What Is Agent Memory - A Complete Guide
created: Wednesday 11th November 2026 12:30
aliases:
tags:
  - agents
  - llm
  - rag
---
- https://vectorize.io/what-is-agent-memory
- Type: article
- Source: Vectorize (vendor of Hindsight)

---

# TL;DR

Explains **agent memory** as retaining, recalling and reflecting on experience across sessions, and why plain [[RAG]] over stored text is not enough.

# Summary

Basic RAG used as memory cannot reason about **time**, treats all facts as equal instead of reconciling conflicts, and does not separate observed facts from inferences. The guide frames memory as a learning problem built on three operations: **retain** (extract facts, entities and temporal metadata into a graph), **recall** (fuse vector, BM25, graph and temporal retrieval under a token budget) and **reflect** (synthesize observations and update beliefs). Its main job is deciding what enters the context window. The author is open about being biased toward Hindsight.

# Key takeaways

1. **Structure data when it is written, not when it is read**, so retrieval can filter by time, entity and relationship.
2. **Combine several retrieval strategies**: semantic vectors, BM25 keywords, graph traversal and temporal filtering, then fuse, rerank and trim.
3. **Separate memory types**: world facts, experiences, observations consolidated from several data points, and user-curated mental models; procedural and episodic memory are also mentioned.
4. **Add reflection**, the step where stored memories become updated beliefs with confidence.
5. **Avoid the common mistakes**: storing everything, ignoring time, treating memory as an afterthought and skipping evaluation; measure over weeks, not single sessions.
6. **Distinguish short-term from long-term**: the context window is cleared per session, long-term memory persists in a database; multi-agent setups use private and shared memory banks.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [Hindsight](https://github.com/vectorize-io/hindsight) | Open-source memory system the guide recommends |
| [[RAG]] | Baseline the guide argues is insufficient for memory |
| Vector databases, Redis | Storage options mentioned |
| LangGraph, CrewAI | Frameworks managing short-term memory |
| LongMemEval | Benchmark mentioned |

# When to use

1. When explaining why vector search over chat history is not real agent memory.
2. When designing the write and read paths of a memory layer (retain, recall, reflect).
3. When choosing which information types to store and how to evaluate memory over time.

# Caveats

- Vendor content with no date or author; benchmark and "small context beats large dump" claims come without data.
- The applications section (healthcare, finance, education) has no supporting evidence.

---
[[AI Agents]] [[Memory in the Age of AI Agents]] [[GBrain Review - An Honest Assessment of Garry Tan's Brain]] [[RAG]] [[LLM]]
