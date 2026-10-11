---
title:  Ingress controller Annotations
created: Friday 11th April 2025 21:54
aliases: 
tags:
  - k8s
  - nginx
  - networking
---
- https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/annotations/
- Type: reference
- Source: ingress-nginx official documentation

---

# TL;DR

Reference for the `nginx.ingress.kubernetes.io/*` annotations that tune the ingress-nginx controller per Ingress: rewrites, TLS, auth, rate limits, canaries, proxy settings and more.

# What it covers

All annotation values are strings, so numbers and booleans must be quoted. The page groups annotations by purpose and ends with notes on security and limits.

# Key takeaways

1. **Rewrites and redirects**: `rewrite-target`, `app-root`, `ssl-redirect` (turn off per Ingress) and `force-ssl-redirect` (force HTTPS behind an external load balancer).
2. **Authentication**: basic/digest with `auth-type`, `auth-secret`, `auth-realm`; external auth with `auth-url`.
3. **Client certificates (mTLS)**: `auth-tls-secret`, `auth-tls-verify-client`, `auth-tls-pass-certificate-to-upstream`.
4. **Traffic control**: `limit-rps`, `limit-rpm`, `limit-connections` (per client IP, per replica), `canary` with `canary-weight`, header or cookie rules, and `whitelist-source-range`.
5. **Upstream tuning**: `proxy-body-size`, `proxy-read-timeout`, `proxy-buffering`, `proxy-http-version`, `backend-protocol` (HTTP, HTTPS, GRPC, GRPCS, FCGI, AUTO_HTTP).
6. **Other**: `enable-cors` with `cors-allow-origin`, session stickiness with `affinity: cookie`.
7. **Snippets are risky**: `configuration-snippet` and similar inject raw NGINX config and can expose secrets in multi-tenant clusters (CVE-2021-25742); the docs recommend disabling them.
8. **Limits**: only one canary per Ingress rule, canaries ignore most other annotations, and SSL passthrough (off by default) disables layer 7 annotations.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[Kubernetes]] | Ingress resources |
| NGINX ingress | Controller implementing the annotations |
| [[Security]] | Snippet restrictions and auth |
| [[gRPC]] | `backend-protocol: GRPC` option |

# When to use

1. When you need the **exact annotation name** for TLS, auth, rewrites or limits.
2. When setting up **mTLS** on an Ingress, see [[Configuring Certificate-Based Mutual Authentication with Kubernetes Ingress-Nginx]].
3. When reviewing the **security impact of snippet annotations**.

# Caveats

- Controller-specific, versions differ; check the docs for your release.

---
[[Kubernetes]] [[Security]] [[gRPC]]
[[Configuring Certificate-Based Mutual Authentication with Kubernetes Ingress-Nginx]]
[[mTLS setup using self-signed cert in Kubernetes and NGINX]]
[[mutual TLS based on specific IP]]
