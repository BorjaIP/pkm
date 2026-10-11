---
title: Storage Orchestration for Kubernetes
created: Saturday 3rd May 2025 00:04
aliases: 
tags:
  - k8s
  - storage
  - devops
---
- https://medium.com/@abdulfayis/storage-orchestration-for-kubernetes-c6370f943e23
- Type: tutorial
- Source: Medium · Abdul Fayis · Feb 2024

---

# TL;DR

Two ways to give [[Kubernetes]] persistent storage: **Rook-Ceph** (block, shared filesystem and S3-style object storage) and **Longhorn** (simple replicated block volumes with a UI), each shown with install steps and a sample workload.

# Summary

Rook is an operator that deploys and manages Ceph on Kubernetes; Ceph provides object, block and file storage with replication and self-healing. Longhorn is a cloud-native distributed block storage system with snapshots, backups and cross-cluster disaster recovery. The tutorial installs the Rook operator and a Ceph cluster, checks health from the toolbox pod, and provisions block storage for WordPress and MySQL, a CephFS shared filesystem for a kube-registry, and an S3 bucket through an ObjectBucketClaim. It then installs Longhorn and persists a MySQL database across a pod deletion.

# Key takeaways

1. **Rook-Ceph needs raw storage**: raw devices or partitions, LVM volumes, encrypted or multipath devices, or block-mode PVs on the nodes.
2. **Install order**: `crds.yaml`, `common.yaml`, `operator.yaml`, then `cluster.yaml`; verify with `kubectl -n rook-ceph get pod` and `ceph status` from the toolbox.
3. **Block storage**: create a `CephBlockPool` and a `StorageClass` (`rook-ceph-block`), then reference it from PVCs (`ReadWriteOnce`).
4. **Shared filesystem**: `CephFilesystem` plus a `rook-cephfs` StorageClass gives `ReadWriteMany` volumes for multiple pods.
5. **Object storage**: a `CephObjectStore` starts the RGW service; an `ObjectBucketClaim` creates buckets, consumed with S3 clients through a user's access keys.
6. **Longhorn prerequisites**: Kubernetes 1.14+, Helm, `open-iscsi` on every node.
7. **Longhorn install**: `kubectl apply` of the release YAML or Helm into `longhorn-system`, then the UI via `kubectl port-forward` on the `longhorn-frontend` service.
8. **Persistence test**: create a MySQL database, delete the pod and confirm the data survives.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[Kubernetes]] | StorageClass, PVC and PV resources |
| Rook, Ceph | Operator and distributed storage system |
| Longhorn | Replicated block storage with a dashboard |
| [[Helm]] | Longhorn installation method |
| [[S3]] | The API exposed by Ceph object storage |
| [[Linux]] | Node prerequisites (open-iscsi) |

# When to use

1. When choosing **storage for stateful workloads on Kubernetes** (block, file or object).
2. When you need the **Rook-Ceph install sequence** and sample manifests.
3. When you want a lighter alternative such as Longhorn for replicated volumes.

# Caveats

- Hands-on notes: the sample secrets and keys printed in the article are demo values, and production sizing, upgrades and failure testing are not covered.
- Examples use MySQL 5.6 images and old API snippets; check current Rook and Longhorn docs.

---
[[Kubernetes]] [[Helm]] [[S3]] [[Linux]]
[[Kubetools - A Curated List of Kubernetes Tools]]
[[Starting containers in order on Kubernetes with InitContainers]]
