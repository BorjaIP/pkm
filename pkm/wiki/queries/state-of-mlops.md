---
title: State of MLOps and model serving
created: Monday 12th October 2026 18:41
aliases:
tags:
  - archived
  - agent
  - mlops
status: active
source: digest
query: What do I know about MLOps pipelines, orchestration and model serving?
---

> **Status: active** | Source: digest of vault notes
>
> Synthesis of what the vault says about MLOps. Each claim cites the note it comes from.

# Question

What do I know about MLOps pipelines, orchestration and model serving?

# Answer

**Maturity model.** Production ML is the deployment of an automated pipeline, not a model API: level 0 (manual), level 1 (pipeline automation with continuous training, validation, feature and metadata stores) and level 2 (CI/CD of the pipeline itself) ([[MLOps - Continuous delivery and automation pipelines in machine learning]], hub: [[MLOps]]). The same principles appear as CD4ML: version code, data and models, reproduce training, test data and model quality, monitor and close the loop ([[Continuous Delivery for Machine Learning]], example: [[A CD4ML Example Setup on AWS S3, GitLab with DVC]]).

**Versioning and experiments.** [[Dvc]] adds pointers to Git for data and models and defines pipeline stages ([[Using DVC to create an efficient version control system for data projects]]). Experiments live in custom Git refs ([[Git Custom References for ML Experiments]]) and hyperparameter searches can be queued and compared ([[Tuning Hyperparameters with Reproducible Experiments]], background: [[A Practical Introduction to Grid Search, Random Search, and Bayes Search]]). CI reports for models: [[CML with DVC use case]].

**Orchestration.** Choosing an orchestrator on Kubernetes is a trade-off between Kubeflow Pipelines, Argo/Tekton, Airflow, Flyte, Prefect and others ([[MLOps - Task and Workflow Orchestration Tools on Kubernetes]]). Visual layers on top: [[Elyra 3.3 - Pipelines, custom components, and catalogs]], [[Introducing Elyra pipelines with custom component support]], [[Automate your machine learning workflow tasks using Elyra and Apache Airflow]]. Continuous retraining loop with streaming data: [[Keeping your ML model in shape with Kafka, Airflow and MLFlow]].

**Kubeflow in practice.** Local sandbox: [[An end-to-end ML pipeline on-prem - Notebooks & Kubeflow Pipelines on the new MiniKF]]. Full pipeline to a served model: [[Building a ML Pipeline from Scratch with Kubeflow]]. Distributed training on GPUs: [[Distributed TensorFlow training using Kubeflow on Amazon EKS]].

**Serving options.** Asynchronous API with a queue ([[Deploying ML Models in Production with FastAPI and Celery]]), gRPC service ([[Deploying Machine Learning Models with PyTorch, gRPC and asyncio]]), or a platform: KServe with ModelMesh, inference graphs and the Open Inference Protocol ([[KServe - The State and Future of Cloud-Native Model Serving]]).

**Caveat.** Most notes are 2019-2023; tool names and APIs have moved on, the principles have not.

# Pages Consulted

[[MLOps]], [[Dvc]], [[Kubeflow]] and the web notes cited above.

# Sources Cited

Original URLs are on each cited web note.
