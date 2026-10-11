---
title:  Kubernetes Network Policy Recipes
created: Friday 11th April 2025 21:51
aliases: 
tags:
  - k8s
  - networking
  - security
---
- https://github.com/ahmetb/kubernetes-network-policy-recipes
- Type: repo
- Source: GitHub · ahmetb · Apache-2.0

---

# TL;DR

A numbered set of copy-paste **NetworkPolicy** manifests for the usual [[Kubernetes]] cases: deny all, namespace isolation, external ingress, port limits and egress control.

# Summary

Each recipe is one Markdown file with a scenario, the YAML and a test, preceded by a crash course on policy semantics. Policies work at layers 3 and 4, an empty pod selector matches every pod in the namespace, pods selected by no policy allow everything, and there are no deny rules: traffic is denied by allowing only what is listed. Multiple policies on the same pod are unioned. The repo pairs with the author's article [[Securing Kubernetes Cluster Networking]].

# Key takeaways

1. **Deny first**: recipes 01 and 03 block all traffic to an app or namespace, the base for any allow-list.
2. **Allow selectively**: limit by labels (02), by namespace (04-07), by port (09) or with multiple selectors (10).
3. **Open to the outside** deliberately with recipe 08 (external clients).
4. **Control egress**: recipes 11, 12 and 14 deny outbound traffic per app, per namespace or to the outside world.
5. **Use the rules of thumb**: selectors match only the policy's namespace, policies are additive, and unselected pods are open.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[Kubernetes]] | NetworkPolicy resource |
| Google Kubernetes Engine | Suggested test environment (recipe 00) |
| [[Securing Kubernetes Cluster Networking]] | Conceptual companion article |

# When to use

1. When you need a **ready manifest** for a specific traffic rule.
2. When practising network policies for the CKAD/CKS-style exercises, see [[CKAD Exercises]].
3. When reviewing which policy pattern fits namespace isolation vs egress control.

# Caveats

- Recipe numbering skips 13 and two egress recipes are only planned; the page does not list supported CNI plugins.
- Applying policies to an existing cluster can disrupt networking; test first.

---
[[Kubernetes]] [[Security]]
[[Securing Kubernetes Cluster Networking]]
[[Securing kubernetes clusters with Istio and Keycloak]]
[[CKAD Exercises]]
