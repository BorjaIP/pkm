---
title: Automate your machine learning workflow tasks using Elyra and Apache Airflow
created: Saturday 12th April 2025 13:00
aliases: 
tags:
  - mlops
  - orchestration
  - ml
---
- https://medium.com/ibm-data-ai/automate-your-machine-learning-workflow-tasks-using-elyra-and-apache-airflow-adf297adc455
- Type: tutorial
- Source: Medium (IBM Data Science in Practice) · Patrick Titzler · Mar 2021

---

# TL;DR

Build a notebook-and-script ML pipeline in Elyra's visual editor and let it **generate the Airflow DAG** for you, with no DAG code.

# Summary

[[Airflow]] workflows are DAGs of operator tasks. Running notebooks on a schedule normally needs `PythonVirtualenvOperator` or `PapermillOperator` plus custom pre- and post-processing. Elyra generates this: each node becomes a task run by a custom `NotebookOp` operator that handles artifacts and shared cloud storage. The editor packages inputs, uploads them to cloud storage, writes the DAG and pushes it to the GitHub repo Airflow watches, preconfigured to run once.

# Key takeaways

1. **Assemble visually**: drop notebooks and scripts on the canvas and connect them to set dependencies.
2. **Set node properties**: container image, CPU/GPU/RAM requests, file dependencies, environment variables and output files.
3. **Keep environments in runtime configurations**: Airflow URL, GitHub repo for DAGs and cloud storage details, outside the pipeline definition.
4. **Understand run steps**: package artifacts, upload to storage, generate the DAG, upload it to the monitored repo.
5. **Export instead of run** to customise the DAG without uploading it.
6. **Use a private DAG repository**, because runtime configuration is embedded in generated DAGs.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[Airflow]] | Scheduler running the generated DAG (Kubernetes executor, git-sync) |
| [[Jupyter]] | JupyterLab 3 with Elyra extensions |
| [[Kubeflow]] | Alternative runtime for the same pipeline |
| [[Git]] | GitHub repository holds the DAGs |

# When to use

1. When **scheduling notebooks** on Airflow without writing DAGs.
2. When you need the **prerequisites** (Airflow 1.10.8+, Kubernetes executor, git-sync).
3. When comparing visual pipelines with hand-written orchestration.

# Caveats

- Outdated (Elyra 2.1, Airflow 2 untested); later posts add custom operators.

---
[[Airflow]] [[Jupyter]] [[MLOps]] [[Data Orchestration]]
[[Introducing Elyra pipelines with custom component support]]
[[Elyra 3.3 - Pipelines, custom components, and catalogs]]
[[Keeping your ML model in shape with Kafka, Airflow and MLFlow]]
