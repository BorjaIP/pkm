---
title:  Distributed TensorFlow training using Kubeflow on Amazon EKS
created: Friday 11th April 2025 22:33
aliases: 
tags:
  - kubeflow
  - aws
  - mlops
  - gpu
---
- https://aws.amazon.com/es/blogs/opensource/distributed-tensorflow-training-using-kubeflow-on-amazon-eks/
- Type: tutorial
- Source: AWS Open Source Blog · Ajay Vohra · Oct 2019

---

# TL;DR

Train Mask R-CNN on COCO with distributed data-parallel TensorFlow on [[EKS]] GPU nodes, launching **Horovod** workers through a [[Kubeflow]] MPI Job.

# Summary

The setup uses an EKS cluster with a P3 GPU node group created with Terraform, an MPI Operator that places launcher and worker pods, Horovod with NCCL for gradient all-reduce, [[EFS]] for the shared dataset, S3 for staging and ECR for the image. Helm charts install the MPI Job and the training job; TensorBoard shows mAP and loss over 24 epochs.

# Key takeaways

1. **Prerequisites**: GPU-optimised AMI subscription, P3 limits for at least four instances, a build instance with a 200 GB root volume.
2. **Create infrastructure** with Terraform (GPU node group), install kubectl and aws-iam-authenticator.
3. **Shared storage**: persistent volume and claim for EFS; copy COCO 2017 from S3.
4. **Containerise** the training code and push to ECR.
5. **Run** with Helm (MPI Job chart plus Mask R-CNN chart) and watch launcher and worker pods.
6. **Clean up** with `helm del --purge` and `terraform destroy`.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[Kubeflow]] | MPI Job CRD and operator |
| [[EKS]] | Kubernetes platform with GPU nodes |
| [[EFS]] / [[S3]] | Shared dataset store and staging |
| [[Terraform]] / [[Helm]] | Provisioning and deployment |
| [[Nvidia]] | P3 GPUs and NCCL |

# When to use

1. When you need a **reference for multi-node GPU training on Kubernetes**.
2. When wiring **EFS-backed datasets** for training pods.
3. When comparing with the Azure variant in [Train and Serve TensorFlow Models at Scale with Kubernetes and Kubeflow on Azure](https://github.com/Azure/kubeflow-labs).

# Caveats

- Tested on Kubernetes 1.13 and Terraform 0.12.6 in us-west-2; the post reports no speedup numbers, only TensorBoard curves.

---
[[Kubeflow]] [[EKS]] [[AWS]] [[MLOps]] [[Nvidia]]
[Train and Serve TensorFlow Models at Scale with Kubernetes and Kubeflow on Azure](https://github.com/Azure/kubeflow-labs)
[[Building a ML Pipeline from Scratch with Kubeflow]]
[[Large Scale Distributed Model Training with Colossal AI and Lightning AI]]
