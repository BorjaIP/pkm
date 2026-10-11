---
title:  Continuous Delivery for Machine Learning
created: Friday 11th April 2025 22:12
aliases: 
tags:
  - mlops
  - ci-cd
  - dvc
  - ml
---
- https://martinfowler.com/articles/cd4ml.html
- Type: article
- Source: martinfowler.com · Sato, Wider, Windheuser (Thoughtworks) · Sep 2019

---

# TL;DR

**CD4ML** applies Continuous Delivery to ML systems that change along three axes (**code, model, data**), using versioned artifacts, reproducible pipelines and automated quality checks.

# Summary

ML projects stall in proofs of concept because data engineers, data scientists and engineers hand work over a wall. CD4ML treats data, models and code as versioned artifacts released in small, safe increments, with cross-functional teams and a feedback loop from production. The article walks through a sales-forecasting example (Favorita grocery data, scikit-learn) with [[Dvc]] for reproducible training, MLflow for experiments, GoCD for orchestration, Docker and [[Kubernetes]] for deployment.

# Key takeaways

1. **Version everything**: code in Git, data and models with DVC (`dvc repro`, `dvc push/pull`).
2. **Make training reproducible** as a pipeline of stages (cleaning, features, selection, tuning, evaluation).
3. **Choose a serving pattern**: embedded model, model as a service, or model as data.
4. **Test beyond code**: data validation, contract and integration tests, model quality thresholds with ratcheting, bias checks across data slices.
5. **Track experiments** with a branch per experiment plus MLflow Tracking.
6. **Orchestrate two pipelines**: ML training and application deployment, with rollback.
7. **Monitor and close the loop**: log inputs, outputs, interpretability data and final decisions (EFK stack in the example).

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[Dvc]] | Data versioning and reproducible pipelines |
| [[MLOps]] | The discipline CD4ML contributes to |
| [[Kubernetes]] / [[Docker]] | Deployment target and packaging |
| [[Elasticsearch]] | Part of the EFK monitoring stack |
| MLflow, GoCD, Seldon | Experiment tracking, orchestration, A/B testing options |

# When to use

1. When explaining **why ML needs Continuous Delivery** rather than hand-offs.
2. When designing **testing layers for ML** pipelines.
3. When choosing **model-serving patterns** and rollback strategy.

# Caveats

- 2019 tool choices (GoCD, Pachyderm alternatives) have aged; the principles are the lasting part.

---
[[MLOps]] [[Dvc]] [[Machine Learning]] [[Kubernetes]]
[[A CD4ML Example Setup on AWS S3, GitLab with DVC]]
[Continuous Intelligence and CD4ML Workshop](https://github.com/ThoughtWorksInc/cd4ml-workshop)
[[MLOps - Continuous delivery and automation pipelines in machine learning]]
