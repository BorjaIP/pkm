---
title:  mTLS setup using self-signed cert in Kubernetes and NGINX
created: Friday 11th April 2025 21:54
aliases: 
tags:
  - k8s
  - ssl
  - mtls
  - security
---
- https://stackoverflow.com/questions/63025817/mtls-setup-using-self-signed-cert-in-kubernetes-and-nginx
- Type: qa
- Source: Stack Overflow · asked Jul 2020

---

# TL;DR

For mTLS on [[Kubernetes]] with NGINX ingress you only need a CA, a server and client certificate and two annotations; **TLS termination alone does not authenticate the client**.

# Summary

The asker on AKS wanted HTTPS with client certificates for an echo service, ending TLS at the ingress, and asked whether a Certificate Authority or cert-manager was required. The answer separates concepts: mTLS means each side authenticates the other, a CA is not cert-manager, and a self-signed CA works if the client trusts it. The ingress is told to verify clients with annotations and a Secret holding the server cert, key and CA.

# Key takeaways

1. **Enable client verification** with `nginx.ingress.kubernetes.io/auth-tls-verify-client: "on"` and `nginx.ingress.kubernetes.io/auth-tls-secret: "default/mycerts"`.
2. **Create the Secret** with `kubectl create secret generic mycerts --from-file=tls.crt=server.crt --from-file=tls.key=server.key --from-file=ca.crt=ca.crt`.
3. **Trust the CA** on clients, or requests will not be verified.
4. **No cert-manager required**: the CA and cert-manager are different things.
5. **Terminating TLS at the ingress is fine**; use a service mesh (Istio, Linkerd, Consul) for mTLS between services.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[Kubernetes]] | Secret and Ingress resources |
| [[Cert Manager]] | Optional certificate automation, not required |
| [[Istio]] | Mesh alternative for service-to-service mTLS |
| [[OpenSSL]] | Typical tool to create the CA and certificates |

# When to use

1. When you need the **minimum Kubernetes pieces** for client-certificate authentication at an NGINX ingress.
2. When explaining **mTLS vs TLS termination**.
3. When following up with the full walkthrough in [[Configuring Certificate-Based Mutual Authentication with Kubernetes Ingress-Nginx]].

# Caveats

- Short answer without a complete manifest; the linked blog contains more detail.

---
[[Kubernetes]] [[Security]] [[OpenSSL]] [[Cert Manager]] [[Istio]]
[[Configuring Certificate-Based Mutual Authentication with Kubernetes Ingress-Nginx]]
[[mutual TLS based on specific IP]]
