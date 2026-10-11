---
title:  Building a ML Pipeline from Scratch with Kubeflow
created: Friday 11th April 2025 22:33
aliases: 
tags:
  - kubeflow
  - mlops
  - k8s
---
- https://blogs.cisco.com/developer/machinelearningops03
- Type: tutorial
- Source: Cisco Developer blog · Flo Pachinger · Sep 2022 (MLOps part 3)

---

# TL;DR

An end-to-end [[Kubeflow]] walkthrough that turns an MNIST digit recogniser into a pipeline from data to a **KServe** inference service.

# Summary

The tutorial installs Kubeflow 1.5.1 on a Kubernetes 1.21 cluster, reaches the central dashboard through a port-forward to the [[Istio]] ingress gateway, and uses a Jupyter notebook to run the Kubeflow Pipelines SDK. MinIO, bundled with Kubeflow, stores artifacts and models. The pipeline retrieves and preprocesses data, trains the model and finishes by creating a KServe inference service that can be tested from the notebook or a small web app.

# Key takeaways

1. **Verify the platform first**: check Kubeflow pods with `kubectl` and open the dashboard through `port-forward` on the Istio gateway.
2. **Let notebooks reach the pipelines API** by applying the access manifest in your user namespace.
3. **Use the bundled MinIO**: read its credentials from a Kubernetes secret and use the `mlpipeline` bucket.
4. **Give KServe access to models** in MinIO with a dedicated secret.
5. **Define the pipeline in Python** with the KFP SDK; the last step deploys the inference service.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[Kubeflow]] | Notebooks, Pipelines and KServe |
| [[Kubernetes]] | Platform (v1.21) |
| [[Istio]] | Ingress gateway for the dashboard |
| [[Jupyter]] | Notebook where the pipeline is authored |
| MinIO | S3-compatible object store for artifacts |

# When to use

1. When you want a **hands-on Kubeflow pipeline** from notebook to served model.
2. When wiring **KServe with MinIO** model storage.
3. When recalling the steps to reach the Kubeflow dashboard locally.

# Caveats

- Versions are old (Kubeflow 1.5.x); commands may differ today.
- No accuracy results or cluster sizing; pipeline code lives in the linked repo, and the post lists default MinIO credentials that must be changed.

---
[[Kubeflow]] [[MLOps]] [[Kubernetes]] [[Istio]] [[Jupyter]]
[[An end-to-end ML pipeline on-prem - Notebooks & Kubeflow Pipelines on the new MiniKF]]
[[Distributed TensorFlow training using Kubeflow on Amazon EKS]]
[[KServe - The State and Future of Cloud-Native Model Serving]]
