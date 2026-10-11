---
title:  Securing Kubernetes Cluster Networking
created: Friday 11th April 2025 21:52
aliases: 
tags:
  - k8s
  - networking
  - security
---
- https://ahmet.im/blog/kubernetes-network-policy/
- Type: article
- Source: ahmet.im · Ahmet Alp Balkan · Aug 2017

---

# TL;DR

By default every pod can reach every pod in a [[Kubernetes]] cluster; **NetworkPolicies** add label-based pod firewalling, but only if the network plugin enforces them.

# Summary

A NetworkPolicy selects **target pods** by label and lists the **ingress sources** (pods or namespaces) allowed to connect. Pods selected by no policy stay open to everyone, and policies are connection-based, so replies on an allowed connection flow back automatically. The recommended pattern is a **default-deny** policy per namespace followed by allow rules per application, kept as manifests next to the app code. Policies are not enough on their own: add mutual TLS or a service mesh.

# Key takeaways

1. **Check plugin support first** (Calico, Weave Net): without it the API accepts policies and enforces nothing.
2. **Start from default-deny**, then allow traffic explicitly by `podSelector` labels.
3. **Remember the namespace rule**: a `podSelector` only matches pods in the policy's own namespace; cross-namespace access needs a `namespaceSelector` on the target's policy.
4. **Policies are additive and connection-based**: each `from` entry is an alternative source; the target cannot open connections back.
5. **Layer defences**: combine policies with **mutual TLS** and a service mesh such as [[Istio]] (or Linkerd) for encryption and transparent enforcement.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[Kubernetes]] | NetworkPolicy API (`networking.k8s.io/v1`) |
| [[Istio]] | Service mesh for TLS and egress policy |
| Calico, Weave Net | Network plugins that enforce policies |
| [[Kubernetes Network Policy Recipes]] | Ready-made manifests for the common cases |

# When to use

1. When **locking down pod-to-pod traffic** in a cluster.
2. When a policy "does nothing" and you suspect the CNI plugin lacks support.
3. When explaining why network policies complement, not replace, mTLS.

# Caveats

- Written for Kubernetes 1.7: egress rules were not available yet, and GKE support was alpha.

---
[[Kubernetes]] [[Istio]] [[Security]]
[[Kubernetes Network Policy Recipes]]
[[Securing kubernetes clusters with Istio and Keycloak]]
[[mTLS setup using self-signed cert in Kubernetes and NGINX]]
