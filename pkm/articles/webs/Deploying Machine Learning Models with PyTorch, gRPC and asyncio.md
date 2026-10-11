---
title:  Deploying Machine Learning Models with PyTorch, gRPC and asyncio
created: Friday 11th April 2025 23:59
aliases: 
tags:
  - grpc
  - mlops
  - python
  - serving
---
- https://github.com/roboflow/deploy-models-with-grpc-pytorch-asyncio
- Type: repo
- Source: GitHub · Roboflow · MIT

---

# TL;DR

Serve a PyTorch image classifier over [[gRPC]] with Python asyncio: a `.proto` contract, an async server and an async client.

# What it does

Companion code to an article: a ResNet-34 (ImageNet weights from torchvision) behind an `InferenceServer` service whose `inference` RPC takes repeated image bytes and returns repeated `uint32` class IDs. Four files in `src/`: `inference.proto`, `inference.py` (transforms and batched `no_grad` inference), `server.py` (`grpc.aio.server()` on `[::]:50052`) and `client.py` (async client printing predictions and latency).

# Key takeaways

1. **Define the contract in a proto** and generate stubs with `grpcio-tools`.
2. **Use `grpc.aio`** to serve concurrent requests with asyncio.
3. **Send images as bytes** in a repeated field to batch several images per call.
4. **Reported timings** (single machine): about 86 ms for one image, about 208 ms for three in one call.
5. **Claimed benefits** of gRPC over REST: binary Protocol Buffers, typed code in many languages (not benchmarked in the repo).

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[gRPC]] | RPC framework and contract |
| [[Python]] | asyncio server and client |
| PyTorch, torchvision | Model and transforms |
| [[MLOps]] | Model serving pattern |

# When to use

1. When serving a **model over gRPC** instead of REST.
2. When you need a **minimal async gRPC example** in Python.
3. When comparing with [[Deploying ML Models in Production with FastAPI and Celery]].

# Caveats

- Insecure channels (no TLS), single-run timings and a trailing space in the client address string; for local experiments only.

---
[[gRPC]] [[Python]] [[MLOps]]
[[Deploying ML Models in Production with FastAPI and Celery]]
[Open Inference Protocol (V2 Inference Protocol)](https://kserve.github.io/website/0.10/modelserving/data_plane/v2_protocol/)
[[Introducing gRPC Support with NGINX]]
