---
title:  Evaluating Large Language Model (LLM) systems - Metrics, challenges, and best practices
created: Monday 14th April 2025 21:07
aliases: 
tags:
  - evaluation
  - llm
  - rag
  - mlops
---
- https://medium.com/data-science-at-microsoft/evaluating-llm-systems-metrics-challenges-and-best-practices-664ac25be7e5
- Type: article
- Source: Medium (Data Science + AI at Microsoft) · Jane Huang, Kirk Li, Daniel Yehdego · Mar 2024

---

# TL;DR

Evaluating an LLM *system* is a continuous process that mixes offline golden datasets, LLM-as-judge and online metrics, with metrics chosen per application scenario.

# Summary

Benchmarks such as GLUE, HellaSwag, TruthfulQA or MMLU rate a bare model, but an LLM application also depends on prompts, retrieval and fine-tuning, so it needs its own evaluation. The article advocates an evolving evaluation dataset, scenario-specific metrics and CI/CE/CD (continuous evaluation) as part of **LLMOps**. It contrasts **offline** evaluation (cheap, automatable, pre-deployment) with **online** evaluation on real traffic, and adds Responsible AI checks.

# Key takeaways

1. **Evaluate the system, not just the model**: prompt templates, retrieval and architecture all affect output quality.
2. **Build golden datasets**, using an LLM to generate examples (LangChain `QAGenerateChain`) while keeping humans in the loop.
3. **Use LLM-as-judge with care**: few-shot scoring prompts (for example NER accuracy on a 0-1 scale) are cheap but not infallible, even with GPT-4.
4. **Combine offline and online**: offline for regression tests, online metrics and user feedback for real behaviour.
5. **Add Responsible AI test sets** per harm category (self-harm, copyright and others) and rerun them before launch.
6. **Match metrics to the task**: BLEU/METEOR for translation, precision/recall/F1 for classification and NER, dedicated sets for summarisation, Q&A and text-to-SQL.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[LLM]] | System under test and judge |
| [[RAG]] | Retrieval pipelines need component-level evaluation |
| [[MLOps]] | LLMOps extends it with continuous evaluation |
| Prompt Flow, LangSmith, W&B, DeepEval, TruEra | Evaluation frameworks listed |

# When to use

1. When **designing an evaluation plan** for an LLM application.
2. When deciding **offline vs online** evaluation.
3. When picking **metrics for a scenario** such as Q&A or summarisation.

# Caveats

- Many tables (benchmarks, frameworks, metrics) were images or links on the page and are not reproduced here.

---
[[LLM]] [[RAG]] [[MLOps]]
[[Evaluating RAG pipelines with Ragas + LangSmith]]
[[ARAGOG - Advanced RAG Output Grading]]
[[LLMs Will Always Hallucinate, and We Need to Live With This]]
