---
title:  PeaTMOSS - Mining Pre-Trained Models in Open-Source Software
created: Tuesday 31st October 2023 10:34
aliases:
tags:
  - ml
  - dl
---
- https://arxiv.org/pdf/2310.03620.pdf
- Source: arxiv

---

# TL;DR

**PeaTMOSS** mines 281,638 open-source GitHub projects linked to 14,296 HuggingFace models and finds that PTM adoption is widespread but dependency management is critically poor, with rampant version drift and missing reproducibility metadata.

# Summary

Pre-trained models are now software dependencies, yet their management practices lag far behind traditional libraries. **PeaTMOSS** constructs a dataset linking **281,638 open-source projects** to 14,296 HuggingFace models and analyzes adoption patterns, task distribution, **version drift**, and maintenance practices. Adoption is concentrated in a small set of popular models, many projects pin outdated versions without tracking, and **reproducibility metadata** is frequently absent — creating silent failures for downstream users and exposing AI supply chain risks at ecosystem scale.

# Key contributions

1. Constructs **PeaTMOSS**, a dataset linking 281,638 open-source projects to 14,296 HuggingFace pre-trained models.
2. Demonstrates that **version drift** is the norm: most projects pin outdated PTM versions without explicit tracking.
3. Shows that **reproducibility metadata** is systematically absent from PTM-dependent open-source projects.
4. Establishes empirical evidence that **PTM dependency management** practices lag far behind traditional software engineering norms.
5. Introduces the framing of **AI supply chain** risk through the lens of PTM ecosystem concentration and poor maintenance.

# When to cite

1. When arguing that **pre-trained models should be treated as versioned software dependencies** requiring explicit management.
2. When discussing **AI supply chain risks** arising from ecosystem concentration around a small set of popular models.
3. When motivating the need for **reproducibility standards** and dependency manifests in ML projects.
4. When providing empirical data on **PTM adoption patterns** in open-source software at ecosystem scale.

---
[[Artificial Intelligence|AI]]
[[Deep Learning]]
[[Machine Learning|ML]]
