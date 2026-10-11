---
title:  Enable an IAM User or IAM Role to access an EKS cluster
created: Friday 11th April 2025 21:25
aliases: 
tags:
  - aws
  - k8s
  - security
---
- https://www.javierinthecloud.com/enable-an-iam-user-or-iam-role-to-access-an-eks-cluster/
- Type: tutorial
- Source: Javier in the Cloud · Javier Carrera · Nov 2023

---

# TL;DR

Only the IAM principal that created an [[EKS]] cluster has admin access; to let others in, map their IAM ARN to a Kubernetes group with `eksctl create iamidentitymapping`.

# Summary

Other IAM principals see "doesn't have access to Kubernetes objects" or `Unauthorized` from kubectl. EKS authenticates through the IAM authenticator, which reads mappings in the `aws-auth` ConfigMap in `kube-system`. The cluster creator is implicitly `system:masters` outside that ConfigMap, so it can repair a broken ConfigMap. The article uses `eksctl` instead of editing the ConfigMap by hand and binds new principals to a read-only ClusterRole.

# Key takeaways

1. **Find the creator** via CloudTrail (or authenticator logs in CloudWatch) and use it to run `aws eks update-kubeconfig`.
2. **Inspect mappings** with `eksctl get iamidentitymapping` or `kubectl -n kube-system get configmaps aws-auth -o yaml`.
3. **Create RBAC**: a `cluster-viewer` ClusterRole (get/list) bound to a `cluster-viewer-group`.
4. **Grant access** with `eksctl create iamidentitymapping --arn <arn> --username ... --group ...`.
5. **Role ARNs cannot contain paths**: `role/a/b/rdsaccess` becomes `role/rdsaccess`.
6. **No overwrite**: delete the mapping with `eksctl delete iamidentitymapping`, then recreate it.
7. **Prefer federation** over IAM users for people; groups need not pre-exist.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[EKS]] | Managed Kubernetes and its aws-auth mapping |
| [[IAM]] | Users and roles being granted access |
| [[Kubernetes]] | RBAC ClusterRole and bindings |
| [[AWS]] | CloudTrail, CloudWatch, CLI |

# When to use

1. When a teammate or CI role **cannot access an EKS cluster**.
2. When you need the **aws-auth** mapping steps.
3. When explaining the **cluster-creator-is-admin** gotcha.

# Caveats

- Needs `eksctl` 0.40.0 or later to manage clusters it did not create; newer EKS access entries may supersede `aws-auth`.

---
[[EKS]] [[IAM]] [[Kubernetes]] [[AWS]] [[Security]]
[[Cross-Account Access in the AWS Management Console]]
[[Hacking an AWS hosted Kubernetes backed product, and failing]]
