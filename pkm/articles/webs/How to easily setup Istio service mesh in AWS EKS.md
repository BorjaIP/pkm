---
title:  How to easily setup Istio service mesh in AWS EKS
created: Friday 11th April 2025 22:01
aliases: 
tags:
  - istio
  - aws
  - k8s
---
- https://www.linkedin.com/pulse/how-easily-setup-istio-service-mesh-aws-eks-ihar-vauchok/
- Type: tutorial
- Source: LinkedIn Pulse · Ihar Vauchok · Feb 2021

---

# TL;DR

Provision an [[EKS]] cluster with [[Terraform]], install [[Istio]] 1.8 from Helm charts, enable sidecar injection and run Bookinfo with a canary split visible in Kiali.

# Summary

The article does not use `eksctl` or `istioctl install`: Terraform (terraform-aws-eks module, four files) creates the cluster, then Helm installs `base`, `istiod` and an `istio-ingress` gateway with AWS annotations for an internet-facing NLB. Namespaces labelled `istio-injection=enabled` get an Envoy sidecar. Bookinfo services, each with a DestinationRule using `ISTIO_MUTUAL` mTLS, show `2/2` pods, and the Istio add-ons (Prometheus, Grafana, Jaeger, Zipkin, Kiali) visualise traffic.

# Key takeaways

1. **Provision the cluster** with Terraform (`init`, `plan`, `apply`, 26 resources) and save the kubeconfig output.
2. **Install Istio with Helm** in `istio-system`: `base` chart, `istiod` from `istio-discovery`, then the ingress gateway (NLB annotations for proxy protocol, idle timeout and cross-zone balancing).
3. **Enable injection** per namespace with `istio-injection=enabled`; healthy pods show `2/2`.
4. **Deploy Bookinfo** across namespaces with Service, ServiceAccount, Deployment, DestinationRule and VirtualService per app.
5. **Observe** with the sample add-ons and `istioctl dashboard kiali`.
6. **Canary** the reviews service by weighting a VirtualService 10/45/45 across v1, v2 and v3; deleting it returns to round-robin.
7. **Clean up** namespaces and run `terraform destroy` to stop AWS charges.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[Istio]] | Service mesh (1.8.2) |
| [[EKS]] | Cluster (Kubernetes 1.17) |
| [[Terraform]] | Provisioning |
| [[Helm]] | Istio installation |
| Kiali | Traffic graph |

# When to use

1. When you need a **Terraform + Helm approach** to installing Istio on EKS.
2. When looking at a **canary traffic-split example** with VirtualService weights.
3. When comparing with [[Securing kubernetes clusters with Istio and Keycloak]].

# Caveats

- Versions are old (Terraform 0.12, EKS 1.17, Istio 1.8.2) and `v1alpha3` APIs may not work today; the public NLB has no authentication, and the sizing is demo-scale.

---
[[Istio]] [[EKS]] [[Terraform]] [[Helm]] [[AWS]]
[[Securing kubernetes clusters with Istio and Keycloak]]
[[Securing Kubernetes Cluster Networking]]
