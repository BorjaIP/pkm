---
title:  A CD4ML Example Setup on AWS S3, GitLab with DVC
created: Friday 11th April 2025 22:12
aliases: 
tags:
  - mlops
  - dvc
  - ci-cd
---
- https://github.com/sbalnojan/cd4ml-example
- Type: repo
- Source: GitHub · sbalnojan

---

# TL;DR

A small repo showing CD4ML end to end: [[Dvc]] versions the data and model on S3, and GitLab CI reruns the pipeline and fails if the model does not beat the baseline.

# What it does

Using the KKBox music-recommendation data from Kaggle (downloaded manually, about 1.2-1.5 GB), the pipeline cleans data, trains a Random Forest, evaluates it against a stored baseline and promotes the model only if the score improves, then updates `baseline.txt`. Deployment is out of scope. A Makefile wraps the steps.

# Key takeaways

1. **Stages**: `preprocess_data.py` -> `train_rf.py` -> `preprocess_data_eval.py` + `evaluate_model.py`, each a DVC stage.
2. **Promotion gate**: a model that does not beat `baseline.txt` fails the pipeline.
3. **Setup**: `dvc init`, add an S3 remote, `dvc add data/` and `dvc push`, then `dvc run` and `dvc repro`.
4. **CI**: `.gitlab-ci.yml` reproduces the pipeline on each push.
5. **Suggested extras**: sanity checks on predictions, XGBoost, daily ingestion, GPU runners, TensorFlow Data Validation, MLflow.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[Dvc]] | Data and model versioning, pipeline stages |
| [[S3]] | DVC remote storage |
| [[Git]] | GitLab repository and CI |
| [[Makefile]] | Wraps pipeline commands |
| [[MLOps]] | Continuous delivery practice |

# When to use

1. When you want a **working example of CD4ML** with DVC.
2. When implementing a **baseline gate** for model promotion.
3. When pairing with the theory in [[Continuous Delivery for Machine Learning]].

# Caveats

- 19 commits and the README says the blog post was "not yet written"; some DVC commands (`dvc run`) are outdated.

---
[[Dvc]] [[MLOps]] [[S3]] [[Git]]
[[Continuous Delivery for Machine Learning]]
[Continuous Intelligence and CD4ML Workshop](https://github.com/ThoughtWorksInc/cd4ml-workshop)
[[Using DVC to create an efficient version control system for data projects]]
