---
title:  Deploying ML Models in Production with FastAPI and Celery
created: Saturday 12th April 2025 13:01
aliases: 
tags:
  - mlops
  - python
  - serving
---
- https://towardsdatascience.com/deploying-ml-models-in-production-with-fastapi-and-celery-7063e539a5db/
- Type: tutorial
- Source: Towards Data Science · Jonathan Readshaw · Feb 2021

---

# TL;DR

Serve model predictions asynchronously: a [[FastAPI]] endpoint enqueues a Celery task, a worker loads the model once, and the client polls for the result by task ID.

# Summary

The API has a `predict` endpoint that accepts feature JSON and returns a task ID, and a `results` endpoint that reports pending or finished status. Celery workers run the inference. Instead of the plain task decorator, the task extends Celery's base `Task` class, so the saved scikit-learn pipeline (preprocessing included) is loaded only on first use and reused. The approach fits any model exposing `predict` and `predict_proba`, including Keras.

# Key takeaways

1. **Decouple request and inference** with a queue so slow predictions do not block the API.
2. **Return a task ID** from `predict` and poll `results`.
3. **Load the model once per worker** by subclassing Celery's `Task`.
4. **Package preprocessing with the model** as a single pipeline.
5. **Run the pieces**: `uvicorn app:app`, then `celery -A celery_task_app.worker worker -l info`, and test with a requests client.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[FastAPI]] | HTTP API for predict and results |
| [[Python]] | Implementation language |
| Celery | Distributed task queue running inference |
| [[MLOps]] | Serving pattern |

# When to use

1. When **inference is slow** and clients can poll.
2. When you need the **worker-side model caching** pattern in Celery.
3. When comparing serving options with [[Deploying Machine Learning Models with PyTorch, gRPC and asyncio]].

# Caveats

- Minimal example: the broker/backend is not named, error handling and Docker are left as next steps.

---
[[FastAPI]] [[Python]] [[MLOps]]
[[Deploying Machine Learning Models with PyTorch, gRPC and asyncio]]
[[KServe - The State and Future of Cloud-Native Model Serving]]
