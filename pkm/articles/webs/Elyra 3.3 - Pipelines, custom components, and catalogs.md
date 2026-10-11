---
title:  Elyra 3.3 - Pipelines, custom components, and catalogs
created: Saturday 12th April 2025 13:01
aliases: 
tags:
  - mlops
  - orchestration
  - kubeflow
---
- https://medium.com/ibm-data-ai/elyra-3-3-pipelines-custom-components-and-catalogs-74cf198fdf48
- Type: article
- Source: Medium (IBM Data Science in Practice) · Patrick Titzler · Dec 2021

---

# TL;DR

Elyra 3.3 lets the JupyterLab **Visual Pipeline Editor** build pipelines from generic notebook/script nodes plus runtime-specific **custom components** pulled from **component catalogs**.

# Summary

Elyra's pipeline editor started as a way to chain Jupyter notebooks, Python and R scripts and run them locally, on [[Kubeflow]] Pipelines or on [[Airflow]]. Version 3.3 adds custom components, black-box tasks tied to one runtime. A catalog (filesystem, web or service-based) is read through catalog connectors that feed the editor palette; the Machine Learning Exchange connector is an example. Data passes only between explicitly connected nodes.

# Key takeaways

1. **Generic components** (notebook, Python, R) run on every supported runtime and exchange data through S3-compatible storage.
2. **Custom components** are runtime specific, black boxes, managed outside Elyra and use runtime mechanisms such as Airflow XComs.
3. **Catalogs hold components**: built-in filesystem and web connectors, extra connectors for other sources.
4. **Compose by dragging** components onto the canvas, connecting them and setting properties.
5. **Data exchange is restricted** to connected nodes, so a node cannot read outputs of an unconnected one.
6. **Next steps** at the time: wider Airflow operator support (extended in 3.6).

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[Kubeflow]] | Runtime for Kubeflow Pipelines components |
| [[Airflow]] | Runtime for Airflow operators |
| [[Jupyter]] | JupyterLab hosts the editor |
| [[CLAIMED, a visual and scalable component library for Trusted AI\|CLAIMED]] | Component library built on generic components |

# When to use

1. When you need the **difference between generic and custom components** in Elyra.
2. When configuring **component catalogs** for the pipeline editor.
3. When explaining **portability** of pipelines between Kubeflow Pipelines and Airflow.

# Caveats

- Version-specific (Dec 2021); later Elyra releases changed supported runtimes and features.

---
[[Kubeflow]] [[Airflow]] [[Jupyter]] [[MLOps]]
[[Introducing Elyra pipelines with custom component support]]
[[Automate your machine learning workflow tasks using Elyra and Apache Airflow]]
[[MLOps - Task and Workflow Orchestration Tools on Kubernetes]]
