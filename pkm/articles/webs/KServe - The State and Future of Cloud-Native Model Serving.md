---
title:  KServe - The State and Future of Cloud-Native Model Serving
created: Friday 11th April 2025 22:35
aliases: 
tags:
  - kubeflow
  - mlops
  - serving
---
- https://www.slideshare.net/slideshow/kubecon-2023-eu-kserve-the-state-and-future-of-cloudnative-model-serving/257510768
- Type: article
- Source: KubeCon EU 2023 slides · Dan Sun (Bloomberg), Theofilos Papapanagiotou (AWS)

---

# TL;DR

KServe 0.10 offers serverless, multi-model and graph-based inference on [[Kubernetes]] with a standard Open Inference Protocol, and its 1.0 roadmap adds LLM serving.

# Summary

The talk reviews KServe's features: serving runtimes and a custom runtime SDK, serverless autoscaling on requests per second or concurrency, **ModelMesh** for multi-model serving, **inference graphs**, explainers and drift detectors, and the **Open Inference Protocol** shared by runtimes such as MLServer, Triton and TorchServe. It then covers large-language-model serving, including BLOOM 176B on Triton FasterTransformer and BloombergGPT in production.

# Key takeaways

1. **Core**: predictor and transformer pipelines, payload logging, request batching, canary rollout and cloud or PVC storage.
2. **ModelMesh**: scale-out layer that loads many models into shared containers; the talk says IBM runs thousands in production.
3. **Inference graphs**: declarative pipelines of Sequence, Switch, Ensemble and Splitter nodes.
4. **Open Inference Protocol**: REST for ease and gRPC for performance, implemented by KServe, MLServer, Triton, TorchServe, OpenVINO and others.
5. **LLM serving** uses tensor and pipeline parallelism and sharded checkpoints; BLOOM 176B is about 360 GB, and BloombergGPT runs with BF16, TP=2 on 2 A100 80GB per replica.
6. **1.0 roadmap**: GA for core inference, SDK, ModelMesh and graphs; protocol coverage across runtimes; LLM support; observability and security.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[Kubeflow]] | KServe originated from the Kubeflow project |
| [[Kubernetes]] | Platform |
| [[Nvidia]] | Triton and FasterTransformer, A100 GPUs |
| [Open Inference Protocol (V2 Inference Protocol)](https://kserve.github.io/website/0.10/modelserving/data_plane/v2_protocol/) | Standard REST/gRPC data plane |

# When to use

1. When you need an **overview of KServe capabilities** circa 2023.
2. When comparing **model-serving options**, see [[Deploying ML Models in Production with FastAPI and Celery]].
3. When looking at **LLM serving on Kubernetes** constraints (GPU cost, load time).

# Caveats

- Slides, not a tutorial; the roadmap is from 2023 and the KEDA integration is not mentioned in the slides read.

---
[[Kubeflow]] [[MLOps]] [[Kubernetes]] [[Nvidia]]
[[Building a ML Pipeline from Scratch with Kubeflow]]
[[Deploying Machine Learning Models with PyTorch, gRPC and asyncio]]
[[Deploying ML Models in Production with FastAPI and Celery]]
