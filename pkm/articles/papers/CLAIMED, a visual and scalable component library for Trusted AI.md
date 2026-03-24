---
title:  CLAIMED, a visual and scalable component library for Trusted AI
created: Monday 24th April 2023 20:51
aliases:
tags:
  - ml
  - dl
---
- https://arxiv.org/pdf/2103.03281.pdf
- Source: arxiv

---

# TL;DR

**CLAIMED** is an open-source visual component library that wraps Jupyter notebooks into reusable pipeline building blocks deployable on Apache Airflow or Kubeflow Pipelines, making reproducibility and lineage tracking first-class properties of AI workflows.

# Summary

The gap between experimental Jupyter notebooks and production AI pipelines is wide, and bridging it typically requires significant orchestration engineering. **CLAIMED** closes this by wrapping notebooks into reusable pipeline components that deploy on **Apache Airflow**, **Kubeflow Pipelines**, or locally without requiring the data scientist to write orchestration code. Built-in **lineage tracking** enables auditability of pipeline runs. The system treats **reproducibility** and transparency as design goals, not afterthoughts, targeting practitioners who need production-grade ML workflows from existing notebook-based work.

# Key contributions

1. Proposes **CLAIMED**, a component library that converts Jupyter notebooks into portable, reusable pipeline building blocks.
2. Introduces built-in **lineage tracking** at the component level to enable auditability without retrofitting.
3. Demonstrates deployment across multiple orchestration backends (**Apache Airflow, Kubeflow Pipelines**) without infrastructure lock-in.
4. Shows that **low-code pipeline composition** reduces the engineering barrier between experimental notebooks and production AI.

# When to cite

1. When discussing tools that bridge the **notebook-to-production gap** for data scientists without DevOps expertise.
2. When evaluating **MLOps frameworks** that prioritize reproducibility and lineage tracking as first-class features.
3. When comparing **low-code pipeline orchestration** approaches that support multiple backends (Airflow, Kubeflow).
4. When arguing for treating **reproducibility** as a design constraint rather than a post-hoc addition in ML systems.

---
[[Kubeflow]]
[[Jupyter]]
[[Artificial Intelligence|AI]]
[[Machine Learning|ML]]
