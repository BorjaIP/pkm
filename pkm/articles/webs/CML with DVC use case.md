---
title:  CML with DVC use case
created: Friday 11th April 2025 22:17
aliases: 
tags:
  - mlops
  - dvc
  - ci-cd
---
- https://github.com/iterative/cml_dvc_case
- Type: repo
- Source: GitHub · iterative

---

# TL;DR

A sample showing **CML** and [[Dvc]] in GitHub Actions: each pull request trains a model on data pulled from cloud storage and gets a metrics report as a PR comment.

# What it does

On every pull request a runner starts in a CML Docker environment, DVC pulls the data, `python train.py` trains the model and CML posts a visual report with DVC metrics to the PR. The key file is `.github/workflows/cml.yaml`; the data pipeline lives in `dvc.yaml`, with `data.dvc`, `get_data.py`, `metrics.json` and `loss.csv`.

# Key takeaways

1. **Report in the PR**: model performance is visible where the code is reviewed.
2. **DVC remote on S3** configured through repository secrets (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, optional `AWS_SESSION_TOKEN`); `GITHUB_TOKEN` is automatic.
3. **Reuse in a fork**: generate the dataset, `dvc init`, add a remote, `dvc add data` and `dvc push`, add the secrets.
4. **Copy the workflow file** into a fork, since forks do not copy workflows by default.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[Dvc]] | Data versioning and metrics |
| [[S3]] | Remote storage for the dataset |
| [[Git]] | GitHub pull requests and Actions |
| [[MLOps]] | CI/CD for machine learning |

# When to use

1. When setting up **CI/CD reports for ML** in pull requests.
2. When you need a **DVC remote configured with CI secrets**.
3. When comparing with the GitLab variant in [CML basic use case](https://gitlab.com/iterative.ai/cml-base-case).

# Caveats

- The README leaves other cloud providers to the CML documentation.

---
[[Dvc]] [[MLOps]] [[S3]] [[Git]]
[CML basic use case](https://gitlab.com/iterative.ai/cml-base-case)
[[A CD4ML Example Setup on AWS S3, GitLab with DVC]]
[[Continuous Delivery for Machine Learning]]
