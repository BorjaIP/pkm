---
title:  ChatGPT + Enterprise data with Azure OpenAI and AI Search
created: Monday 14th April 2025 20:56
aliases: 
tags:
  - rag
  - llm
  - gpt
  - co-microsoft
---
- https://github.com/Azure-Samples/azure-search-openai-demo
- Type: repo
- Source: GitHub · Azure-Samples · MIT

---

# TL;DR

A deployable reference app that gives a ChatGPT-style chat over your own documents using [[Azure]] OpenAI for generation and Azure AI Search for retrieval.

# Summary

The sample implements a [[RAG]] chat with a fictitious company's HR and policy documents. Azure OpenAI hosts the model, Azure AI Search indexes and retrieves, and Blob Storage holds the files; the app runs on Container Apps (or App Service). Features include multi-turn chat with citations and a visible thought process, in-UI prompt settings, many document formats, optional multimodal and speech input/output, and optional Entra login with per-user data access. A Python backend is the main version, with .NET, Java and JavaScript variants.

# Key takeaways

1. **Provision with `azd up`**: it deploys the resources and builds the search index from the `./data` folder.
2. **Retrieval-grounded answers** carry citations, and the thought-process view shows what was retrieved.
3. **Optional modules**: Document Intelligence, Cosmos DB for history, AI Vision, Application Insights for tracing.
4. **Access control**: Microsoft Entra login enables per-user document access.
5. **Mind cost**: Azure AI Search is the main cost driver and charges start at creation; remove resources with `azd down`.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[Azure]] | Hosting, OpenAI, AI Search, Storage |
| [[RAG]] | Architecture pattern implemented |
| [[GPT]] | Chat model behind the answers |
| [[Elasticsearch]] | Comparable self-managed search option (not used here) |

# When to use

1. When you need a **reference architecture for enterprise RAG on Azure**.
2. When estimating **which Azure services and permissions** a RAG chat needs.
3. When comparing with a local setup such as [[How to create a private ChatGPT that interacts with your local documents]].

# Caveats

- Demo, not production-ready without extra security; deploying needs role-assignment permissions on the subscription.
- Repository is maintained actively, so model names and options in the README change often.

---
[[Azure]] [[RAG]] [[GPT]] [[LLM]]
[[How to create a private ChatGPT that interacts with your local documents]]
[[Evaluating RAG pipelines with Ragas + LangSmith]]
