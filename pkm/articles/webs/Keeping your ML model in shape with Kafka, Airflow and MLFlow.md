---
title:  Keeping your ML model in shape with Kafka, Airflow and MLFlow
created: Saturday 12th April 2025 12:59
aliases: 
tags:
  - mlops
  - orchestration
  - ml
---
- https://medium.com/vantageai/keeping-your-ml-model-in-shape-with-kafka-airflow-and-mlflow-143d20024ba6
- Type: tutorial
- Source: Medium (VantageAI) · Mike Kraus · Nov 2019

---

# TL;DR

Update a served model incrementally as streaming data arrives: [[Kafka]] collects data, [[Airflow]] retrains and promotes the better model, and MLflow logs each run.

# Summary

A repo simulates the loop with five Docker containers: Airflow with a data-science toolkit, PostgreSQL for Airflow metadata, Kafka, Zookeeper and MLflow, started with [[Docker Compose]]. A first DAG downloads MNIST, splits train, test and streaming sets and trains a Keras CNN. Streaming data is published to Kafka; a recurring DAG pulls batches, updates the model, compares it with the current one and keeps the winner, while MLflow records parameters, results and sample characteristics.

# Key takeaways

1. **Three roles**: Kafka for streaming, Airflow for orchestration, MLflow for tracking.
2. **Container layout**: Airflow + toolkit, PostgreSQL, Kafka, Zookeeper, MLflow, wired by Docker Compose.
3. **Folder structure**: `dags/`, `data/to_use_for_training` and `used_for_training`, `models/current_model` and `archive`.
4. **One-off DAG** trains the initial model; a **periodic DAG** retrains on new batches.
5. **Promote only on improvement** against the held-out test set, archiving superseded models.
6. **Goal**: reduce model drift with incremental updates and minimal manual work.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[Kafka]] | Streaming feed of new training data |
| [[Airflow]] | Schedules and orchestrates update DAGs |
| [[Docker Compose]] | Spins up the five-container environment |
| [[MLOps]] | Continuous training pattern |
| MLflow | Experiment tracking |

# When to use

1. When designing **incremental model updates** from a stream.
2. When looking for a **local, containerised MLOps sandbox**.
3. When comparing with managed approaches in [[MLOps - Continuous delivery and automation pipelines in machine learning]].

# Caveats

- 2019 setup on MNIST; the second half of the post (update DAG details) was only partly read here.

---
[[MLOps]] [[Airflow]] [[Kafka]] [[Docker Compose]]
[[MLOps - Continuous delivery and automation pipelines in machine learning]]
[[Automate your machine learning workflow tasks using Elyra and Apache Airflow]]
