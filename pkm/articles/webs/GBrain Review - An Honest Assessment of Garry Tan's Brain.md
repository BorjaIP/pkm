---
title:  GBrain Review - An Honest Assessment of Garry Tan's Brain
created: Wednesday 11th November 2026 12:30
aliases:
tags:
  - agents
  - llm
  - rag
---
- https://vectorize.io/articles/gbrain-review
- Type: article
- Source: Vectorize (vendor of Hindsight) · May 8, 2026

---

# TL;DR

Review of **GBrain**, the open-source markdown-first agent memory system by Garry Tan: the best personal brain for [[Hermes]] or [[OpenClaw]] users at single-operator scale, but young and narrow elsewhere.

# Summary

GBrain stores knowledge as **markdown in git** with Postgres-backed retrieval and a skills layer, and officially supports only OpenClaw and Hermes Agent. The review praises its **compounding mechanisms** (tiered enrichment, rule-based entity extraction with zero LLM calls, backlink-boosted ranking) and **hybrid retrieval** (HNSW vectors, full-text search, rank fusion). It also lists the limits: about v0.30 with breaking changes, single-operator design, self-host only and no multi-tenant isolation. The reviewer sells a competing product, so the alternative it recommends is biased.

# Key takeaways

1. **Keep plain text as the source of truth**: a markdown git repo can be diffed, branched and rebuilt, which is the main reason to choose GBrain.
2. **Extract entities with rules, not an LLM**: typed predicates like `works_at` or `invested_in` keep ingestion nearly free in tokens, and a fail-improve loop turns LLM fallbacks into new regex rules.
3. **Use the graph for ranking**: on its own 240-page benchmark the graph layer adds **+31.4 points of P@5** (49.1% P@5, 97.9% R@5). It is not used for multi-hop or temporal traversal.
4. **Budget the cost**: MIT licensed, OpenAI embeddings at about $0.10 per million tokens, so a personal brain runs single-digit dollars per month by the review's estimate.
5. **Check fit before adopting**: look elsewhere for other agent stacks, a managed service, multi-tenant isolation or automatic structure synthesis.

# Tools and concepts

| Item | Role in the page |
|---|---|
| GBrain | Subject: markdown, git and Postgres agent memory |
| [[Hermes]], [[OpenClaw]] | The only first-class supported agents |
| [[RAG]] | Hybrid retrieval with rank fusion, compared with vector-only RAG |
| [Hindsight](https://github.com/vectorize-io/hindsight) | Alternative recommended by the publisher |

# When to use

1. When deciding whether a markdown-first memory system fits a personal or single-operator setup.
2. When comparing agent memory systems on retrieval quality, cost and maturity.
3. When looking for design ideas to compound a knowledge base: tiered enrichment, backlinks, rule-based extraction.

# Caveats

- Vendor content: the scorecard and the recommendation of Hindsight are the author's judgment.
- Benchmarks are the project's own and not comparable with other systems' scores because the corpora differ.
- Long-term claims come from public reports, not from production use by the reviewer.

---
[[AI Agents]] [[Memory in the Age of AI Agents]] [[What Is Agent Memory - A Complete Guide]] [[Hermes]] [[OpenClaw]] [[RAG]]
