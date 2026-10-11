---
title:  Introducing Elyra pipelines with custom component support
created: Saturday 12th April 2025 12:59
aliases: 
tags:
  - mlops
  - orchestration
  - kubeflow
---
- https://medium.com/ibm-data-ai/introducing-elyra-pipelines-with-custom-component-support-ae6b616910b5
- Type: article
- Source: Medium (IBM Data Science in Practice) · Patrick Titzler · Aug 2021 (updated Oct 2021)

---

# TL;DR

Elyra 3.0 adds experimental **runtime-specific custom components** to its visual pipelines, alongside the generic notebook and script component that works everywhere.

# Summary

A pipeline is a graph of nodes, each implemented by a component. Elyra's single **generic component** runs Jupyter notebooks, Python or R scripts on JupyterLab, [[Kubeflow]] Pipelines and [[Airflow]], so a pipeline of only generic nodes is portable. Custom components implement one task (load data, train, send email) but only for Kubeflow Pipelines or Airflow, and are listed in a local registry shown in the palette. Pipelines using them are runtime specific.

# Key takeaways

1. **Nodes are components**, configured with properties such as file name and container image.
2. **Generic pipelines are portable**; runtime-specific pipelines cannot move between Kubeflow Pipelines and Airflow.
3. **Palette categories**: generic components and custom ones (for Airflow, for example `BashOperator`, `SimpleHttpOperator`).
4. **Registry stores references**, not specifications; in 3.2 it reads from the local filesystem and public web resources.
5. **Missing then**: data exchange between Airflow custom components and between generic and custom ones; remote component repositories.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[Kubeflow]] | Pipelines runtime with custom components |
| [[Airflow]] | Runtime exposing operators as components |
| [[Jupyter]] | JupyterLab with the Elyra extension |
| [[MLOps]] | Pipeline automation context |

# When to use

1. When you want the **concept of generic vs custom components** in one place.
2. When deciding whether a pipeline **must stay portable** across runtimes.
3. When reading the history before [[Elyra 3.3 - Pipelines, custom components, and catalogs]].

# Caveats

- Feature status is from 2021 and "experimental" at the time.

---
[[Kubeflow]] [[Airflow]] [[Jupyter]]
[[Elyra 3.3 - Pipelines, custom components, and catalogs]]
[[Automate your machine learning workflow tasks using Elyra and Apache Airflow]]
