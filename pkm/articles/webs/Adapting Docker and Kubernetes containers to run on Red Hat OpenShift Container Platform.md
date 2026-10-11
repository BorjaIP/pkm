---
title:  Adapting Docker and Kubernetes containers to run on Red Hat OpenShift Container Platform
created: Friday 11th April 2025 21:49
aliases: 
tags:
  - container
  - k8s
  - openshift
---
- https://developers.redhat.com/blog/2020/10/26/adapting-docker-and-kubernetes-containers-to-run-on-red-hat-openshift-container-platform#
- Type: article
- Source: Red Hat Developer · Michael Greenberg · Oct 2020 (updated Apr 2022)

---

# TL;DR

OpenShift runs containers with an **arbitrary non-root UID**, so images must grant the root group (GID 0) the same rights as the owner and avoid privileged ports.

# Summary

Containers that work on Docker or [[Kubernetes]] often fail on [[RedHat]] OpenShift because Security Context Constraints block root, ports below 1024 are privileged, and the assigned UID has no `/etc/passwd` entry. The fix is to prepare the image so one build runs on all three platforms.

# Key takeaways

1. **Set group ownership to root (GID 0)** and give the group the owner's permissions (`chgrp` and `chmod g=u`).
2. **Use a non-root `USER`** that also works on plain Kubernetes.
3. **Grant execute bits** to owner and group, since arbitrary UIDs rely on group permissions.
4. **Use ports above 1023.**
5. **Volumes** are root-owned and restricted: create files inside the mount rather than changing its ownership.
6. **Handle username lookups** with an entrypoint script that adds a `/etc/passwd` entry for the assigned UID.
7. **Remove `runAsUser`/`runAsGroup`** from deployments and Helm charts; initContainers run under the same arbitrary UID.
8. **Debug** with `oc get events -w`, `oc logs -f <pod> --all-containers`, `oc rsh` and a temporary long `sleep` entrypoint.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[RedHat]] | OpenShift Container Platform |
| [[Docker]] | Image build rules |
| [[Containers]] | Runtime constraints |
| [[Kubernetes]] | Baseline platform with less restrictive defaults |
| [[Starting containers in order on Kubernetes with InitContainers]] | InitContainers behave differently here |

# When to use

1. When a **container fails on OpenShift** but works elsewhere.
2. When writing **portable Dockerfiles** for Kubernetes and OpenShift.
3. When reviewing **Pod security** assumptions in Helm charts.

# Caveats

- Does not mention Source-to-Image; the advice targets image preparation, not cluster configuration.

---
[[RedHat]] [[Kubernetes]] [[Docker]] [[Containers]] [[Security]]
[[Starting containers in order on Kubernetes with InitContainers]]
[[Hacking an AWS hosted Kubernetes backed product, and failing]]
