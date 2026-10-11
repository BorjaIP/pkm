---
title:  Evaluating RAG pipelines with Ragas + LangSmith
created: Saturday 12th April 2025 21:10
aliases: 
tags:
  - rag
  - evaluation
  - llm
  - retrieval
---
- https://blog.langchain.dev/evaluating-rag-pipelines-with-ragas-langsmith/
- Type: tutorial
- Source: LangChain blog (with the Ragas team) · Aug 2023

---

# TL;DR

**Ragas** scores a [[RAG]] pipeline with four LLM-based metrics, and **LangSmith** runs them over a dataset so scores are traceable and repeatable.

# Summary

Classic QA metrics such as ROUGE and BLEU correlate poorly with human judgment, and benchmarks may not transfer to production data. **Ragas** uses an LLM for reference-light evaluation and separates **retrieval** metrics from **generation** metrics. The tutorial wraps each metric in a `RagasEvaluatorChain`, stores test questions in a LangSmith dataset, runs the chain with `run_on_dataset()` and inspects per-example scores in the Feedback tab.

# Key takeaways

1. **Measure generation with two metrics**: **faithfulness** (statements supported by the context divided by all statements) and **answer relevancy** (similarity between the question and questions the answer would respond to).
2. **Measure retrieval with two metrics**: **context relevancy** (signal-to-noise of the retrieved sentences) and **context recall** (does the context cover the ground-truth answer).
3. **Aggregate with the Ragas score**, the harmonic mean of the four metrics.
4. **Evaluate on a dataset, not one query**: create a LangSmith dataset, build a fresh chain per example with `create_qa_chain(return_context=True)`, then run the evaluators.
5. **Close the loop**: push interesting production logs back into the dataset for continuous evaluation.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[RAG]] | System under evaluation (a RetrievalQA over a Wikipedia page) |
| [[LLM]] | Judge inside every Ragas metric; ChatOpenAI as the generator |
| Ragas | Open-source evaluation framework |
| LangSmith / LangChain | Datasets, evaluation runs, tracing, Feedback tab |

# When to use

1. When choosing **metrics to evaluate retrieval vs generation** separately in RAG.
2. When setting up a **repeatable evaluation loop** for a RAG chatbot.
3. When explaining why LLM-as-judge metrics replace BLEU/ROUGE for QA.

# Caveats

- Code uses 2023 LangChain APIs and will need updating.
- Tiny demo (5 questions, two reference answers flagged as wrong); the example `context_relevancy` score of ~0.075 shows the metric is harsh on long contexts.
- LLM judges are themselves biased, which the page acknowledges through a cited paper.

---
[[RAG]] [[LLM]]
[[Evaluating Large Language Model (LLM) systems - Metrics, challenges, and best practices]]
[[ARAGOG - Advanced RAG Output Grading]]
[[Retrieval-Augmented Generation for Large Language Models - A Survey]]
