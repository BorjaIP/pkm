---
title:  Deploying an Istio Gateway with TLS in EKS using the AWS Load Balancer Controller
created: Friday 11th April 2025 22:02
aliases: 
tags:
  - istio
  - k8s
  - aws
  - ssl
---
- https://itnext.io/deploying-an-istio-gateway-with-tls-in-eks-using-the-aws-load-balancer-controller-448812e081e5
- Type: tutorial
- Source: ITNEXT (Medium) · Grig Gheorghiu · Jan 2022 (read through an archive copy)

---

# TL;DR

Run the [[Istio]] ingress gateway as a **NodePort** service behind an **ALB** created by the AWS Load Balancer Controller, so TLS and HTTP-to-HTTPS redirect work on [[EKS]].

# Summary

TLS did not work for the author with the default Network Load Balancer. The fix is to switch `istio-ingressgateway` to NodePort and put an ALB Ingress in front of it, which needs the **AWS Load Balancer Controller** (IAM policy, OIDC provider, service account, cert-manager, controller manifest). The ALB terminates TLS with an ACM certificate and redirects port 80 to 443; inside the mesh a self-signed secret and an Istio Gateway plus VirtualService expose `httpbin`.

# Key takeaways

1. **Install Istio** with `istioctl install` (default profile, 1.12.1 at the time) and enable sidecar injection on the namespace.
2. **Install the controller** following the AWS docs: IAM policy, `eksctl utils associate-iam-oidc-provider`, `eksctl create iamserviceaccount`, cert-manager and the controller YAML with the cluster name set.
3. **Make the gateway a NodePort** service (ports 15021 status, 80 and 443 mapped to targets 8080 and 8443).
4. **Create the ALB Ingress** with annotations: `scheme: internet-facing`, `target-type: instance`, `certificate-arn`, `backend-protocol: HTTPS`, health check on `/healthz/ready` port 15021, listen ports 80 and 443 and an `ssl-redirect` action returning a 301.
5. **Tag subnets** `kubernetes.io/role/elb=1` (public) or `internal-elb` (internal) so the controller can place the ALB.
6. **Expose an app**: a TLS secret, an Istio `Gateway` (HTTPS with `credentialName`) and a `VirtualService` for `httpbin.mydomain.com`, then a Route 53 CNAME to the ALB.
7. **Verify**: `curl -I http://...` returns 301 to HTTPS and `/status/418` returns the teapot.
8. **Oddity**: the ALB listeners show "Default: returning fixed response 404" even though routing works.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[Istio]] | Ingress gateway, Gateway and VirtualService |
| [[EKS]] | Kubernetes 1.21/1.20 cluster |
| [[ELB]] | ALB created by the controller |
| [[Route 53]] | DNS CNAME to the ALB |
| [[Cert Manager]] | Prerequisite of the controller |
| [[OpenSSL]] | Self-signed certificate for the app |

# When to use

1. When you need **TLS and HTTP-to-HTTPS redirect on an Istio gateway in EKS**.
2. When an NLB-based gateway **does not terminate TLS** as you need.
3. When comparing with the simpler install in [[How to easily setup Istio service mesh in AWS EKS]].

# Caveats

- 2022 versions (Istio 1.12, AWS LB Controller 2.3.1) and `v1alpha3` Istio APIs; the author says it took about 8 hours of trial and error.

---
[[Istio]] [[EKS]] [[ELB]] [[AWS]] [[Route 53]]
[[How to easily setup Istio service mesh in AWS EKS]]
[[Securing kubernetes clusters with Istio and Keycloak]]
[[Ingress controller Annotations]]
