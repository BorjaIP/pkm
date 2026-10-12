---
title:  MLOps - Task and Workflow Orchestration Tools on Kubernetes
created: Friday 11th April 2025 22:11
aliases: 
tags:
  - mlops
  - orchestration
  - k8s
---
- https://achernov.medium.com/mlops-task-and-workflow-orchestration-tools-on-kubernetes-adba3020d2bc
- Type: article
- Source: Medium · Anton Chernov · May 2021

---

# TL;DR

A hands-on comparison of ten workflow orchestrators for [[Kubernetes]]; the author's pick is **Flyte** or **Prefect**.

# Summary

Choosing an orchestrator shapes your dependencies, so the article sets criteria first: open source, an API for tasks and dependencies, a central scheduler, a dashboard, good Kubernetes integration, and no cloud lock-in. It then installs and runs a sample on [[Kubeflow]] Pipelines, MLflow, Metaflow, Flyte, ZenML, [[Airflow]], Argo, Tekton, Prefect and Luigi, with verdicts on each. Kubeflow Pipelines compiles Python to Argo or Tekton YAML.

# Key takeaways

1. **Define the criteria first**: scheduler, dashboard, Kubernetes integration, minimal extra concepts, no vendor lock-in.
2. **Kubeflow Pipelines** can be installed alone (via kustomize, no [[Helm]]) and sits on Argo/Tekton underneath.
3. **MLflow** excels at experiment tracking but is not a workflow engine; **Metaflow** is tightly coupled to [[AWS]].
4. **Flyte** (Lyft) is Kubernetes-native with a strong dashboard; **Prefect** has arguably the best API.
5. **Argo and Tekton** are YAML-first and interchangeable for CI/CD-style flows; Airflow is powerful but heavier; **Luigi** is the simplest, Make-like option.
6. **Dataflow engines** (Beam, Flink) and TFX are not orchestrators.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[Kubeflow]] | Python pipelines compiled to Argo/Tekton |
| [[Airflow]] | Run on Kubernetes via KubernetesPodOperator, executor or KEDA |
| [[Workflow Orchestration]] | The problem space compared |
| Argo, Tekton, Prefect, Flyte, Luigi, ZenML, Metaflow, MLflow | Candidates, each with install, example and dashboard review |

# When to use

1. When **choosing an orchestrator** for ML workflows on Kubernetes.
2. When you need a quick **mental map of Argo vs Tekton vs Kubeflow Pipelines**.
3. When justifying why MLflow is not a workflow engine.

# Caveats

- 2021 snapshot: several projects (Flyte, Prefect, ZenML) changed a lot since; opinions are the author's.

---
[[MLOps]] [[Kubeflow]] [[Airflow]] [[Workflow Orchestration]] [[Kubernetes]]
[[MLOps - Continuous delivery and automation pipelines in machine learning]]
[[Automate your machine learning workflow tasks using Elyra and Apache Airflow]]
[[Keeping your ML model in shape with Kafka, Airflow and MLFlow]]
