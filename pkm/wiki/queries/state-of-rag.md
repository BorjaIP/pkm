---
title: State of RAG
created: Monday 12th October 2026 18:40
aliases:
tags:
  - archived
  - agent
  - rag
status: active
source: digest
query: What do I know about building and improving RAG systems?
---

> **Status: active** | Source: digest of vault notes
>
> Synthesis of what the vault says about RAG. Each claim cites the note it comes from; open the note for details and the original URL.

# Question

What do I know about building and improving RAG systems?

# Answer

**Shape of the pipeline.** [[RAG]] retrieves chunks and lets an LLM answer from them. The field moved from a linear Naive pipeline to optimised Advanced RAG (pre-retrieval, retrieval, post-retrieval) and to composable Modular RAG ([[LLM RAG Paradigms - Naive RAG, Advanced RAG & Modular RAG]], [[Modular RAG and RAG Flow - Part Ⅰ]], [[Modular RAG and RAG Flow - Part II]], survey: [[Retrieval-Augmented Generation for Large Language Models - A Survey]]).

**Indexing and chunking.** Chunks lose meaning without context; contextual headers and returning merged segments help ([[Solving the out-of-context chunk problem for RAG]]). Small-to-big and metadata attachment are the standard levers ([[Modular RAG and RAG Flow - Part Ⅰ]]).

**Retrieval.** Pure vector search misses exact identifiers, so hybrid keyword plus vector search is the common fix, with a tunable weight ([[Hybrid Search a method to Optimize RAG implementation]]) or rank-based fusion that avoids incomparable scores ([[Better RAG results with Reciprocal Rank Fusion and Hybrid Search]]). Multi-query plus RRF is RAG-Fusion ([[Forget RAG, the Future is RAG-Fusion]], [[RAG-Fusion - a New Take on Retrieval-Augmented Generation]]). Late-interaction retrievers are covered by [[ColBERT - Efficient and Effective Passage Search via Contextualized Late Interaction over BERT]] and [[PLAID - An Efficient Engine for Late Interaction Retrieval]]; query-to-answer bridging by [[Precise Zero-Shot Dense Retrieval without Relevance Labels]].

**Storage debate.** A dedicated vector database is not obviously required: consistency and filtering favour vectors inside a general database ([[Do we really need a specialized vector database]]), while vendor series argue embeddings are costly and brittle ([[Understanding the Fundamental Limitations of Vector-Based Retrieval for Building LLM-Powered Chatbots— Part 1-3]], [[Neural Databases - A Next Generation Context Retrieval System for Building Specialized AI-Agents with ChatGPT — Part 2-3]]). Both are vendor-written, so treat the numbers cautiously.

**RAG vs fine-tuning.** They solve different problems (knowledge vs behaviour) and combine well ([[RAG vs Finetuning — Which Is the Best Tool to Boost Your LLM Application]], [[RAFT - Adapting Language Model to Domain Specific RAG]]).

**Evaluation.** Measure retrieval and generation separately (faithfulness, answer relevancy, context relevancy, context recall) ([[Evaluating RAG pipelines with Ragas + LangSmith]]); system-level practices in [[Evaluating Large Language Model (LLM) systems - Metrics, challenges, and best practices]]; benchmark work in [[ARAGOG - Advanced RAG Output Grading]].

**Reference stacks.** Local: [[How to create a private ChatGPT that interacts with your local documents]]. Cloud: [[ChatGPT + Enterprise data with Azure OpenAI and AI Search]]. Feature store as retrieval layer: [[Docling+Feast+MIlvusDB]].

# Pages Consulted

[[RAG]], the web and paper notes cited above.

# Sources Cited

Original URLs are on each cited web note and paper note.
