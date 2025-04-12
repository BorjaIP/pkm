---
title: RAG
created: Friday 10th May 2024 11:13
aliases: 
tags:
---
**Retrieval-Augmented Generation** (RAG) is the process of optimizing the output of a large language model, so it references an authoritative knowledge base outside of its training data sources before generating a response. Large Language Models ([[LLM]]) are trained on vast volumes of data and use billions of parameters to generate original output for tasks like answering questions, translating languages, and completing sentences. RAG extends the already powerful capabilities of LLMs to specific domains or an organization's internal knowledge base, all without the need to retrain the model. It is a cost-effective approach to improving LLM output so it remains relevant, accurate, and useful in various contexts.

| Tool                                                                | Description                                                                  |
| ------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| [RAGAS](https://github.com/explodinggradients/ragas)                | Evaluation framework for your Retrieval Augmented Generation (RAG) pipelines |
| [RAGEIo](https://github.com/zetaalphavector/RAGElo)                 | Tools that helps you selecting the best RAG-based                            |
| [RAGFlow](https://github.com/infiniflow/ragflow?tab=readme-ov-file) | RAG engine based on deep document understanding                              |
| [Verba](https://github.com/weaviate/Verba)                          | Retrieval Augmented Generation (RAG) chatbot powered by Weaviate             |
# Articles/Talks

- [[What is a RAG]]
- [[Modular RAG and RAG Flow - Part Ⅰ]]
- [[Modular RAG and RAG Flow - Part II]]
- [[Evaluating RAG pipelines with Ragas + LangSmith]]
- [[Hybrid Search a method to Optimize RAG implementation]]
- [[Solving the out-of-context chunk problem for RAG]]
- [[Docling+Feast+MIlvusDB]]

<iframe width="560" height="315" src="https://www.youtube.com/embed/aQ4yQXeB1Ss?si=eEbachbYQIgSClU1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
# Reciprocal Rank Fusion (RRF)

Reciprocal Rank Fusion (RRF) is a technique for combining the ranks of multiple search result lists to produce a single, unified ranking. [Developed in collaboration](https://archive.ph/o/l4PZV/https://plg.uwaterloo.ca/~gvcormac/cormacksigir09-rrf.pdf) with the University of Waterloo (CAN) and Google, RRF, in the words of its authors, “yields better results than any individual system, and better results than standard” reranking methods.

By combining ranks from different queries, we increase the chances that the most relevant documents will appear at the top of the final list. RRF is particularly effective because it doesn’t rely on the absolute scores assigned by the search engine but rather on the relative ranks, making it well-suited for combining results from queries that might have different scales or distributions of scores.

- [[Forget RAG, the Future is RAG-Fusion]]
- [[Better RAG results with Reciprocal Rank Fusion and Hybrid Search]]
# Advance  RAG

![[advance_rag.webp]]

- [[LLM RAG Paradigms - Naive RAG, Advanced RAG & Modular RAG]]
# HyDE

Enter Hypothetical Document Embeddings (HyDE), an innovative approach detailed in the paper titled [[Precise Zero-Shot Dense Retrieval without Relevance Labels]].

The core hypothesis of HyDE is simple yet profound: when conducting a document search, using hypothetical answers might yield superior results compared to using the question itself.

# RAG vs Finetuning

- [[RAG vs Finetuning — Which Is the Best Tool to Boost Your LLM Application]]

![[rag_vs_finetuning.png]]
 