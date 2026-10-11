---
title:  Hacking an AWS hosted Kubernetes backed product, and failing
created: Friday 11th April 2025 21:49
aliases: 
tags:
  - k8s
  - security
  - aws
---
- https://blog.appsecco.com/hacking-an-aws-hosted-kubernetes-backed-product-and-failing-904cbe0b7c0d
- Type: article
- Source: Appsecco blog · Appsecco team · Jun 2022 (now at appsecco.com)

---

# TL;DR

A pentest post-mortem showing that tight IAM roles, RBAC, namespace isolation and security groups on [[EKS]] stopped every infrastructure attack path, leaving only an application tenant-isolation flaw.

# Summary

The target was a SaaS on AWS EKS that imported GitHub repositories and deployed them, with one namespace per customer. Testers had remote code execution inside a pod and tried the API server, service-account tokens, the node metadata endpoint, web-identity roles, volume mounts and the VPC. None gave useful privileges. The only finding was a web-app flaw where tenant IDs allowed IDOR access to other tenants' GitHub data.

# Key takeaways

1. **Only port 443** was exposed through the AWS load balancer, giving no useful fingerprinting.
2. **Pod RCE did not equal cluster compromise**: no anonymous API access, a patched Kubernetes version and no RBAC for the service account.
3. **AWS credentials were useless**: both the web identity role and the node IAM role had no helpful permissions.
4. **Namespace isolation held** thanks to pod-level controls and network restrictions, even with root in the pod.
5. **No risky mounts** (no host filesystem) and **security groups** blocked SSH and node scans from the same VPC.
6. **Application logic was the weak point**: tenant IDs and GitHub SSO middleware allowed IDOR.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[EKS]] | Managed Kubernetes under test |
| [[IAM]] | Roles for service accounts and node instance profiles |
| [[Kubernetes]] | RBAC, namespaces, service-account tokens |
| [[AWS]] | Metadata endpoint, STS web identity, security groups |
| nmap, kubectl, AWS CLI | Tools used in the engagement |

# When to use

1. When **reviewing least-privilege settings** for EKS pods and nodes.
2. When explaining **what to harden** (RBAC, IAM, mounts, security groups) after a pod compromise.
3. When showing that **application-layer tenancy** still needs testing.

# Caveats

- Single engagement, written as a narrative; the post does not discuss SSRF or the kubelet API specifically.

---
[[Kubernetes]] [[EKS]] [[IAM]] [[AWS]] [[Security]]
[[Enable an IAM User or IAM Role to access an EKS cluster]]
[[Securing Kubernetes Cluster Networking]]
