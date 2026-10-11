---
title:  mutual TLS based on specific IP
created: Friday 11th April 2025 21:55
aliases: 
tags:
  - k8s
  - ssl
  - mtls
  - security
---
- https://stackoverflow.com/questions/55690321/mutual-tls-based-on-specific-ip
- Type: qa
- Source: Stack Overflow · asked Apr 2019

---

# TL;DR

Requiring mTLS only for some source IPs is not possible with the NGINX ingress `auth-tls-*` annotations inside a configuration snippet, and the answer argues it defeats the purpose of mTLS anyway.

# Summary

The asker wanted client-certificate verification only for a specific remote address and tried to put `auth-tls-*` settings inside an `if ($remote_addr = ...)` block in `configuration-snippet`, but those annotation names are not NGINX directives, so the snippet fails. The accepted answer says that if everyone else can reach the service without a certificate, mTLS adds no real protection (and IPs can be spoofed), and proposes either plain TLS or mTLS for the whole service. A comment adds a legitimate case: machines from known IPs use mTLS while humans are redirected to an OIDC provider.

# Key takeaways

1. **Annotation names are not directives**: `auth-tls-verify-client` works as an annotation but not inside `configuration-snippet`.
2. **Selective mTLS by IP is weak security** because source addresses can be spoofed and others stay unauthenticated.
3. **Option A**: use regular TLS.
4. **Option B**: require mTLS on the service itself and pass the client certificate through with `backend-protocol: "https"` and `auth-tls-pass-certificate-to-upstream: "true"`.
5. **Mixed audiences** (machines and humans) need a different design, such as separate hosts or paths.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[Kubernetes]] | Ingress resource and annotations |
| NGINX ingress | `configuration-snippet`, `auth-tls-*` annotations |
| [[Security]] | Spoofable IP-based trust |

# When to use

1. When someone asks for **IP-conditional client certificates** on NGINX ingress.
2. When explaining why partial mTLS is a **weak control**.
3. When you need the pass-through annotations for a backend that terminates mTLS.

# Caveats

- 2019 answers use the old `extensions/v1beta1` Ingress API; the limitation itself still illustrates the design problem.

---
[[Kubernetes]] [[Security]]
[[mTLS setup using self-signed cert in Kubernetes and NGINX]]
[[Configuring Certificate-Based Mutual Authentication with Kubernetes Ingress-Nginx]]
