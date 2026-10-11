---
title:  An end-to-end ML pipeline on-prem - Notebooks & Kubeflow Pipelines on the new MiniKF
created: Friday 11th April 2025 22:32
aliases: 
tags:
  - kubeflow
  - mlops
  - ml
---
- https://medium.com/kubeflow/an-end-to-end-ml-pipeline-on-prem-notebooks-kubeflow-pipelines-on-the-new-minikf-33b7d8e9a836
- Type: tutorial
- Source: Medium (Kubeflow) · Chris Pavlou (Arrikto) · May 2019, updated Aug 2020

---

# TL;DR

**MiniKF** runs [[Kubeflow]] and Kubeflow Pipelines on a laptop (via Vagrant), so a data scientist can build and run the Chicago Taxi pipeline from a notebook without Kubernetes knowledge.

# Summary

Running a Kubeflow Pipelines example normally requires `kubectl`, YAML and manual PVC handling. MiniKF bundles Kubeflow with Arrikto's **Rok** data management: you start from a notebook server with a data volume, compile the pipeline, snapshot the notebook and data with Rok, then seed the pipeline from that snapshot in the KFP UI. The tutorial uses the Taxi Cab (TFX) example that predicts trips with tips over 20% of the fare.

# Key takeaways

1. **Install** with `vagrant init arrikto/minikf` and `vagrant up`, then open `10.10.10.10` to finish setup.
2. **Create a Notebook Server** from the Kubeflow dashboard with the Kale image and an empty data volume (for example 2 GB called `data`).
3. **Fetch the notebook** with `wget`, run the cells to download the pipeline code, ingest data into the volume and compile the pipeline.
4. **Snapshot with Rok**: capture the whole JupyterLab and its volume so the pipeline can reuse the prepared data.
5. **Run from the UIs**: start the pipeline in KFP seeded by the snapshot, with no Kubernetes commands.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[Kubeflow]] | Dashboard, notebooks, Pipelines |
| [[Jupyter]] | JupyterLab notebook server |
| [[Kubernetes]] | Hidden behind the MiniKF VM |
| Rok, Kale | Snapshots and notebook-to-pipeline tooling |
| MiniKF | Single-node Kubeflow VM |

# When to use

1. When you want a **local Kubeflow Pipelines sandbox**.
2. When explaining how to **seed a pipeline from a notebook snapshot**.
3. When comparing with cluster-based walkthroughs such as [[Building a ML Pipeline from Scratch with Kubeflow]].

# Caveats

- 2019-2020 versions (Kubeflow 0.5, MiniKF v20200812) and a vendor-specific data layer (Rok); the last pipeline-run steps were truncated in the text read.

---
[[Kubeflow]] [[MLOps]] [[Jupyter]] [[Kubernetes]]
[[Building a ML Pipeline from Scratch with Kubeflow]]
[[Distributed TensorFlow training using Kubeflow on Amazon EKS]]
[[Elyra 3.3 - Pipelines, custom components, and catalogs]]
