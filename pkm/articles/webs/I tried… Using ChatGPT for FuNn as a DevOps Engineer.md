---
title:  I tried… Using ChatGPT for FuNn as a DevOps Engineer
created: Monday 14th April 2025 20:52
aliases: 
tags:
  - gpt
  - llm
  - devops
---
- https://ghumare64.medium.com/i-tried-using-chatgpt-for-funn-as-a-devops-engineer-8239313269d4
- Type: article
- Source: Medium · Rohit Ghumare · Jan 2023 (read through an archive copy)

---

# TL;DR

An early experiment using ChatGPT as a **work assistant** for DevOps: it drafted Terraform for a Kubernetes cluster and EFS, explained Istio and sketched an install, but its commands were not always correct.

# Summary

The author asked [[GPT]] for Terraform code to launch a Kubernetes cluster on AWS, then to add Elastic File System and NFS rules, to explain what a service mesh is and how to install Istio, to deploy the Bookinfo sample, to describe Istio Ambient Mesh and to discuss "cloud native 2.0". The results are shown as Loom videos and code. The conclusion: useful for speed and simple tasks, not production-ready code.

# Key takeaways

1. **Infrastructure drafts**: ChatGPT produced IAM roles, a launch configuration, a security group and an autoscaling group, then EFS, a mount target and NFS (TCP and UDP 2049) rules.
2. **Good explanations**: service mesh concepts and a Bookinfo install flow (Istio 1.11 demo profile, `bookinfo.yaml`, gateway).
3. **Knowledge limits**: for Ambient Mesh it gave useful context but wrong commands, and warned the project was experimental.
4. **Safety notes from the model**: always test in a development environment first.
5. **Author's verdict**: use it as an assistant to go faster on simple tasks, not as a source of production code.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[GPT]] | ChatGPT as code assistant |
| [[LLM]] | Underlying model behaviour |
| [[Terraform]] | Code requested for the cluster |
| [[Istio]] | Service mesh questions |
| [[EKS]] | Cluster target of the generated infrastructure |

# When to use

1. When showing **early use cases of LLMs for DevOps tasks**.
2. When noting the **risks of generated infrastructure code** (open SSH to 0.0.0.0/0 and broad IAM permissions appear in the sample).
3. When comparing LLM-generated infrastructure with hand-written examples such as [[Hacking an AWS hosted Kubernetes backed product, and failing]].

# Caveats

- January 2023 model behaviour; the generated Terraform has broad permissions and old resource types, so do not reuse it.

---
[[GPT]] [[LLM]] [[DevOps]] [[Terraform]] [[Istio]]
[[ChatGPT + Enterprise data with Azure OpenAI and AI Search]]
