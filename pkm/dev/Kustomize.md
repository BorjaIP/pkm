---
title:  Kustomize
created: Sunday 30th April 2023 21:15
aliases: 
tags: k8s
---

[Kustomize](https://github.com/kubernetes-sigs/kustomize) is a standalone tool to customize [[Kubernetes]] objects through a [kustomization file](https://kubectl.docs.kubernetes.io/references/kustomize/glossary/#kustomization).

```bash
Kustomize/
├── base
│   ├── deployment.yaml
│   ├── kustomization.yaml
│   └── service.yaml
└── qa
    ├── kustomization.yaml
    └── update-replicas.yaml
```

```bash
# build kustomize for show resources before apply
kubectl kustomize path/file
# kustomize apply
kubectl apply -k path/file
```
