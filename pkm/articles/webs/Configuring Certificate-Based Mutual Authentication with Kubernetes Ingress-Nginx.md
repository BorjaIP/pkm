---
title:  Configuring Certificate-Based Mutual Authentication with Kubernetes Ingress-Nginx
created: Friday 11th April 2025 21:54
aliases: 
tags:
  - k8s
  - ssl
  - security
  - mtls
---
- https://awkwardferny.medium.com/configuring-certificate-based-mutual-authentication-with-kubernetes-ingress-nginx-20e7e38fdfca
- Type: tutorial
- Source: Medium · Fern · Nov 2018

---

# TL;DR

Create a CA, server and client certificates with [[OpenSSL]], store them in one Secret and add two annotations so Ingress-NGINX rejects any client without a valid certificate.

# Summary

Mutual (2-way) authentication means client and server verify each other's certificate through a **Certificate Authority**. The tutorial generates a self-signed CA, a server cert whose CN is the host and a client cert, puts server cert, key and `ca.crt` into one [[Kubernetes]] Secret, deploys an echo server behind a Service and an Ingress with `auth-tls-verify-client: "on"` and `auth-tls-secret`. A `curl` without a cert gets `400 No required SSL certificate was sent`; with `--cert` and `--key` it succeeds and the backend sees `ssl-client-verify=SUCCESS`.

# Key takeaways

1. **Generate three identities**: CA (`openssl req -x509 ...`), server (CN = hostname) and client (CN = user), the last two signed by the CA.
2. **Keep everything in one Secret**: `kubectl create secret generic my-certs --from-file=tls.crt --from-file=tls.key --from-file=ca.crt` (it can also be split).
3. **Turn on verification** with the annotations `nginx.ingress.kubernetes.io/auth-tls-verify-client: "on"` and `auth-tls-secret: "namespace/secret"`.
4. **Tune with extra annotations**: `auth-tls-verify-depth`, `auth-tls-error-page`, `auth-tls-pass-certificate-to-upstream`.
5. **Test both paths** with `curl -k` without and with `--cert/--key`.
6. **Troubleshoot** by grepping `ssl_client_certificate` and `ssl_verify_client` in the generated `nginx.conf` inside the controller pod, then reading its logs.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[Kubernetes]] | Secrets, Deployment, Service, Ingress |
| [[OpenSSL]] | Creates the CA and the signed certificates |
| Ingress-NGINX | Enforces client certificate verification via annotations |
| [[Security]] | Mutual authentication as an access-control layer |

# When to use

1. When **protecting an Ingress with client certificates** (mTLS) in Kubernetes.
2. When you need the **annotation names** for client-cert verification and passing the cert upstream.
3. When debugging why NGINX answers 400 for missing certificates.

# Caveats

- Self-signed certs for testing only; 2018 manifests use the removed `extensions/v1beta1` API, so adapt to current Ingress and Deployment versions.

---
[[Kubernetes]] [[OpenSSL]] [[Security]] [[Cert Manager]]
[[mTLS setup using self-signed cert in Kubernetes and NGINX]]
[[mutual TLS based on specific IP]]
[[Securing Kubernetes Cluster Networking]]
[[Securing kubernetes clusters with Istio and Keycloak]]
