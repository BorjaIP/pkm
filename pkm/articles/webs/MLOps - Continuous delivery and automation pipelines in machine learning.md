---
title:  MLOps - Continuous delivery and automation pipelines in machine learning
created: Friday 11th April 2025 22:14
aliases: 
tags:
  - mlops
  - ci-cd
  - ml
---
- https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning
- Type: reference
- Source: Google Cloud Architecture Center · updated Aug 2024

---

# TL;DR

Production ML means deploying an **automated pipeline** that retrains and redeploys models, and maturity grows from manual (level 0) through pipeline automation (level 1) to CI/CD of the pipeline itself (level 2).

# What it covers

[[MLOps]] extends DevOps with data and model validation (CI), delivery of whole training pipelines (CD) and **continuous training (CT)**. The guide lists the ML development steps (extract, analyse, prepare, train, evaluate, validate, serve, monitor) and describes three maturity levels.

# Key takeaways

1. **Level 0 (manual)**: notebooks, hand-off of a model artifact, rare releases, no monitoring; models decay and cause **training-serving skew**.
2. **Level 1 (pipeline automation)**: same pipeline in dev and production, retraining on triggers, modular containerized components.
3. **Validate before training**: *schema skew* stops the pipeline, *data values skew* triggers retraining.
4. **Validate models offline and online**: test-set and baseline comparison, per-segment consistency, then canary or A/B.
5. **Support with infrastructure**: [[Feature Stores|feature store]], metadata store (lineage, rollback) and a pipeline orchestrator.
6. **Trigger runs** on demand, schedule, new data, performance degradation or concept drift.
7. **Level 2 (CI/CD)**: source control, build and test, model registry; six stages from experimentation to monitoring, with staged rollout (auto test, semi-auto preprod, manual prod).

# When to use

1. When assessing the **MLOps maturity** of a team or project.
2. When deciding **what triggers retraining** and what to validate in a pipeline.
3. When arguing for pipelines, not models, as the unit of deployment.

# Caveats

- Vendor guide (Google Cloud products such as TFX and Cloud Build are the examples); principles are tool-agnostic.

---
[[MLOps]] [[Machine Learning]] [[Feature Stores]] [[Kubeflow]]
[[Continuous Delivery for Machine Learning]]
[[MLOps - Task and Workflow Orchestration Tools on Kubernetes]]
[Continuous Intelligence and CD4ML Workshop](https://github.com/ThoughtWorksInc/cd4ml-workshop)
