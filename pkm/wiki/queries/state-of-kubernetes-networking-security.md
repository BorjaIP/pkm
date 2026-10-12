---
title: State of Kubernetes networking and security
created: Monday 12th October 2026 18:42
aliases:
tags:
  - archived
  - agent
  - k8s
status: active
source: digest
query: What do I know about Kubernetes networking, mTLS, gateways and cluster security?
---

> **Status: active** | Source: digest of vault notes
>
> Synthesis of what the vault says. Each claim cites the note it comes from.

# Question

What do I know about Kubernetes networking, mTLS, gateways and cluster security?

# Answer

**Pod-level traffic.** By default every pod reaches every pod. NetworkPolicies add label-based firewalling but need a plugin that enforces them; start from default-deny and add allows ([[Securing Kubernetes Cluster Networking]], recipes: [[Kubernetes Network Policy Recipes]]).

**Client certificates (mTLS) at the ingress.** Create a CA, server and client certificates, put them in one Secret and set `auth-tls-verify-client` and `auth-tls-secret` ([[Configuring Certificate-Based Mutual Authentication with Kubernetes Ingress-Nginx]], short version: [[mTLS setup using self-signed cert in Kubernetes and NGINX]]). Requiring mTLS only for some IPs does not work as annotations and defeats the purpose ([[mutual TLS based on specific IP]]). Annotation reference and the snippet risk: [[Ingress controller Annotations]].

**Service mesh.** [[Istio]] adds mesh-level mTLS and JWT validation, shown with Keycloak ([[Securing kubernetes clusters with Istio and Keycloak]]); installation on EKS with Terraform and Helm ([[How to easily setup Istio service mesh in AWS EKS]]); TLS and HTTP-to-HTTPS redirect through an ALB ([[Deploying an Istio Gateway with TLS in EKS using the AWS Load Balancer Controller]]).

**Gateways and gRPC.** API gateway vs load balancer: [[System Design Interview Basics - Difference Between API Gateway and Load Balancer]]. Envoy-based gateway: [[An Envoy-Powered, Kubernetes-Native API Gateway]]. gRPC through NGINX and transcoding to HTTP/JSON: [[Introducing gRPC Support with NGINX]], [[Transcoding HTTP-JSON to gRPC]], [[Apache APISIX - Gateway transcode]].

**Cluster access and hardening.** IAM principals other than the creator need an `aws-auth` mapping ([[Enable an IAM User or IAM Role to access an EKS cluster]]); cross-account console access ([[Cross-Account Access in the AWS Management Console]]). A pentest post-mortem shows how least-privilege roles, RBAC, namespace isolation and security groups stop a pod compromise from spreading ([[Hacking an AWS hosted Kubernetes backed product, and failing]]). OpenShift's arbitrary-UID rules: [[Adapting Docker and Kubernetes containers to run on Red Hat OpenShift Container Platform]].

**Developer experience.** Local debugging against a cluster: [[Using Telepresence to intercept microservices on a Kubernetes cluster]]; cost control for dev environments: [[Reducing Cloud Costs on Kubernetes Dev Envs]].

**Caveat.** Several sources are 2017-2022 (old Ingress and Istio APIs); the concepts remain valid, the manifests need updating.

# Pages Consulted

[[Kubernetes]], [[Istio]], [[gRPC]] and the web notes cited above.

# Sources Cited

Original URLs are on each cited web note.
