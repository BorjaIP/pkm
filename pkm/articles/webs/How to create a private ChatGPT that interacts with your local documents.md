---
title:  How to create a private ChatGPT that interacts with your local documents
created: Saturday 12th April 2025 21:13
aliases: 
tags:
  - llm
  - rag
  - embeddings
  - gpt
---
- https://bdtechtalks.com/2023/06/01/create-privategpt-local-llm/
- Type: tutorial
- Source: TechTalks · Ben Dickson · Jun 2023

---

# TL;DR

[[PrivateGPT]] packages a local open-source LLM, an embedding model and a vector store so you can question your own documents without sending data off your machine.

# Summary

The article explains why local LLMs matter for privacy and walks through PrivateGPT's [[RAG]] pipeline. Documents are chunked, embedded with a SentenceTransformers model via LangChain and stored in a vector database; a question is embedded, similar chunks are retrieved and a local model (GPT4All-J or llama.cpp) answers with citations. Setup is a clone, `pip install`, a model download, `ingest.py` and `privateGPT.py`.

# Key takeaways

1. **Five components**: local LLM, embedding model, vector database, your documents and an interface (CLI or Streamlit).
2. **Ingest first**: chunk documents (about 500 tokens), embed and store them; new documents require updating the database.
3. **Query path**: embed the prompt, retrieve similar chunks, send prompt plus chunks to the local LLM, show the answer with sources.
4. **Run the steps**: clone the repo, install requirements, put a model in `models/`, drop files in `source_documents/`, run `python ingest.py`, then `python privateGPT.py`.
5. **Expect limits**: responses can take 20-30 seconds, models are far smaller than ChatGPT, and readers report wrong extractions.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[PrivateGPT]] | The project being explained |
| [[RAG]] | Retrieval pattern behind it |
| [[LLM]] | GPT4All-J and llama.cpp models run locally |
| [[PET]] | Local processing as a privacy-preserving approach |
| [[VDB]] | DuckDB in the project; Faiss, Qdrant, Weaviate, Milvus as alternatives |

# When to use

1. When you want a **fully local document Q&A** setup for sensitive data.
2. When explaining the **ingest and query phases** of a local RAG.
3. When comparing a local setup with [[ChatGPT + Enterprise data with Azure OpenAI and AI Search]].

# Caveats

- 2023 snapshot of an experimental project (the author's own label); file layout and defaults have likely changed.

---
[[PrivateGPT]] [[RAG]] [[LLM]] [[GPT]] [[PET]]
[[ChatGPT + Enterprise data with Azure OpenAI and AI Search]]
