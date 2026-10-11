---
title:  Mastering the KUBECONFIG file
created: Friday 11th April 2025 21:56
aliases: 
tags:
  - k8s
  - config
  - devops
---
- https://ahmet.im/blog/mastering-kubeconfig/
- Type: article
- Source: ahmet.im · Ahmet Alp Balkan · Feb 2019

---

# TL;DR

Behind every `kubectl` command is a kubeconfig; knowing its lookup order, how to merge or extract contexts and how to avoid the wrong cluster saves real mistakes.

# Summary

[[Kubernetes]] clients resolve their configuration from `--kubeconfig`, then the `KUBECONFIG` environment variable, then `$HOME/.kube/config`. `KUBECONFIG` accepts several colon-separated files, which makes in-memory merging trivial, while `kubectl config view --merge --flatten` persists a merged file and `--minify` extracts a single context. The post also shows how to run `kubectl` with no kubeconfig at all and how to keep yourself from hitting the wrong cluster.

# Key takeaways

1. **Remember the precedence**: `--kubeconfig` flag, then `KUBECONFIG` env var, then `$HOME/.kube/config`.
2. **Merge temporarily** with `export KUBECONFIG=file1:file2`, or **persist** with `KUBECONFIG=f1:f2 kubectl config view --merge --flatten > out`; appending YAML files does not work.
3. **Extract one context**: `kubectl config view --minify --flatten --context=<name> > out`.
4. **Run without a kubeconfig** by overriding flags (`--server`, `--user`, `--client-certificate`, ...) and an empty `KUBECONFIG=`; it breaks with complex auth plugins.
5. **Avoid wrong-cluster accidents**: set `KUBECONFIG` per directory with direnv and show the context in the prompt with kube-ps1.
6. **Isolate credentials** per cluster, e.g. `KUBECONFIG=c1.yaml gcloud container clusters get-credentials cluster-1`.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[Kubernetes]] | The `kubectl` client and its config |
| kubectx | Switch contexts (author's tool) |
| direnv, kube-ps1 | Per-directory `KUBECONFIG`, context in the shell prompt |
| Krew plugins | `konfig` (merge/split/import), `config-cleanup`, `config-registry`, `view-serviceaccount-kubeconfig` |
| [[Kubetools - A Curated List of Kubernetes Tools]] | Broader catalogue of such tools |

# When to use

1. When **merging kubeconfigs** from several clusters or splitting one out.
2. When a `kubectl` command hits the wrong cluster and you want a guardrail.
3. When scripting `kubectl` without touching `~/.kube/config`.

# Caveats

- Written in 2019; the lookup order is described as undocumented but codified in client-go.

---
[[Kubernetes]] [[DevOps]]
[[Kubetools - A Curated List of Kubernetes Tools]]
[[Securing Kubernetes Cluster Networking]]
