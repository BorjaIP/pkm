---
title:  Securing kubernetes clusters with Istio and Keycloak
created: Friday 11th April 2025 21:49
aliases: 
tags:
  - k8s
  - security
  - mtls
  - istio
---
- https://charnnarong.github.io/notes/kubernetes-istio-keycloak.html
- Type: tutorial
- Source: Personal notes · charnnarong.github.io

---

# TL;DR

Protect the Istio Bookinfo app by validating **Keycloak-issued JWTs** at the mesh and enabling **mTLS** between services, with an OIDC login added to the product page.

# Summary

[[Istio]] sidecars and an ingress gateway front the demo on [[Kubernetes]]. A Keycloak realm (`bookshop`) and client (`book-ui`) issue tokens; an Istio origin policy checks the JWT on `reviews`, `ratings` and `details`, while DestinationRules turn on service-to-service mTLS. The product page gets `/login`, `/callback` and `/logout` routes through authlib and forwards the access token as a Bearer header. An egress ServiceEntry and VirtualService let the mesh reach Keycloak.

# Key takeaways

1. **Install Istio 1.5.x** and label the namespace with `istio-injection=enabled`.
2. **Create the identity setup** in Keycloak: realm, client and a test user.
3. **Apply a JWT policy** (`origins.jwt` with issuer and JWKS URI, `principalBinding: USE_ORIGIN`).
4. **Enable mTLS** between services with DestinationRules.
5. **Define egress**: Istio blocks unexpected outbound traffic, so add a ServiceEntry and VirtualService for the Keycloak host.
6. **Watch the gotchas**: readiness probe 503 (fixed with `rewriteAppHTTPProbe=true`), numeric hosts rejected as domains, and reapply order after restarts.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[Istio]] | Mesh, JWT validation, mTLS |
| [[Kubernetes]] | Platform (v1.17) |
| [[Helm]] | Used for installation prerequisites |
| Keycloak | OpenID Connect identity provider |
| [[Security]] | Authentication and transport security |

# When to use

1. When wiring **OIDC/JWT authentication into an Istio mesh**.
2. When debugging **egress and probe problems** in early Istio versions.
3. When comparing mesh-level security with [[Securing Kubernetes Cluster Networking]].

# Caveats

- Uses Istio 1.5 `authentication.istio.io/v1alpha1` Policy resources, since replaced by RequestAuthentication and AuthorizationPolicy.
- The author reports Book Details still worked after sign-out and suspects a JWT/mTLS mismatch.

---
[[Istio]] [[Kubernetes]] [[Security]]
[[Securing Kubernetes Cluster Networking]]
[[Configuring Certificate-Based Mutual Authentication with Kubernetes Ingress-Nginx]]
[[mTLS setup using self-signed cert in Kubernetes and NGINX]]
