---
title:  Reducing Cloud Costs on Kubernetes Dev Envs
created: Friday 11th April 2025 21:58
aliases: 
tags:
  - k8s
  - devops
  - cloud
---
- https://www.raftt.io/post/reducing-cloud-costs-on-kubernetes-dev-envs
- Type: article
- Source: Raftt blog · Gahl Saraf · Jul 2023

---

# TL;DR

Share one cluster, scale it down when idle, use spot nodes and trim replicas and requests: the author models a more than 50x cost cut per [[Kubernetes]] dev environment.

# Summary

A full copy of production per developer is expensive: an EKS cluster costs about $100 per month before compute, and dev environments sit idle most of the time. The article layers infrastructure savings (shared cluster with a namespace per environment, autoscaling off-hours, smaller nodes, Karpenter with spot) and application savings (one replica, lower requests, partial environments). The worked example brings a $1,045 per month production footprint of 15 microservices to roughly $18.70 per environment for 10 environments.

# Key takeaways

1. **Use one shared cluster** with a namespace per environment instead of a cluster each.
2. **Scale to working hours**: only about a quarter of the year is actually needed.
3. **Use spot instances** via Karpenter with on-demand fallback; the author saw about 60% lower EC2 cost.
4. **Reduce replicas to one** and requests to idle levels (for example ~1-5 mCPU and 50 MiB), watching memory spikes.
5. **Start partial environments** with only the needed services; worthwhile above roughly 20 services.
6. **Order the work**: declarative IaC first, then orchestration, infrastructure savings before application changes, and verify in Cost Explorer.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[Kubernetes]] | Namespaces, replicas, requests |
| [[EKS]] | Cluster cost baseline |
| [[Terraform]] | IaC option listed (with CloudFormation, CDK, Pulumi) |
| Karpenter, cluster-autoscaler | Node autoscaling and spot |
| ArgoCD, Flux, [[Helm]], [[Kustomize]] | Environment orchestration and packaging |

# When to use

1. When **budgeting per-developer environments** on Kubernetes.
2. When deciding between **shared cluster and cluster-per-environment**.
3. When tuning **requests, replicas and spot usage** in non-production.

# Caveats

- Vendor article (Raftt sells dev-environment tooling); figures are the author's estimate and omit EBS and extra CloudWatch costs.

---
[[Kubernetes]] [[EKS]] [[DevOps]] [[Cloud]]
[[Using Telepresence to intercept microservices on a Kubernetes cluster]]
