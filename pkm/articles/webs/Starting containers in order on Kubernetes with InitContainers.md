---
title:  Starting containers in order on Kubernetes with InitContainers
created: Friday 11th April 2025 21:48
aliases: 
tags:
  - k8s
  - container
  - devops
---
- https://medium.com/@xcoulon/initializing-containers-in-order-with-kubernetes-18173b9cc222
- Type: tutorial
- Source: Medium · Xavier Coulon · Dec 2017

---

# TL;DR

An **InitContainer** blocks a pod's app containers until a precondition (e.g. the database accepts connections) is met, replacing noisy `CrashLoopBackOff` restarts.

# Summary

Without ordering, a web app deployed before its database exits on a fatal connection error, and the kubelet restarts it with exponential back-off until the database appears. [[Kubernetes]] **InitContainers** run in sequence to completion before the application containers start, and they can use tools missing from the app image. The example adds an InitContainer based on the `postgres` image that loops on `pg_isready` until [[PostgreSQL]] responds; the pod waits in `Init:0/1` instead of crashing.

# Key takeaways

1. **Gate startup with an InitContainer**: it must finish successfully before app containers run; on failure the pod's `restartPolicy` applies.
2. **Use a different image for the check**: `postgres` provides `pg_isready` even though the app image does not.
3. **Loop until ready**: `until pg_isready -h postgres -p 5432 -U postgres; do echo waiting for database; sleep 2; done`.
4. **Recognise the status** `Init:0/1`, meaning "waiting on the first InitContainer".
5. **Debug per container** with `kubectl logs -f <pod> -c <init-container>` and `kubectl describe pod`.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[Kubernetes]] | Pod lifecycle, restart policy, `CrashLoopBackOff` |
| [[PostgreSQL]] | The dependency being waited for (`pg_isready` exit codes 0-3) |
| `kubectl logs -c` | Reads logs of a specific (init) container |

# When to use

1. When a service **must wait for a dependency** (database, queue) before starting.
2. When you need a **setup step with extra tooling** that should not live in the app image.
3. When explaining why a pod is stuck in `Init:0/1`.

# Caveats

- 2017 article: output formats and image versions are dated, and the deployment manifest was embedded and not captured here; check current Kubernetes docs.

---
[[Kubernetes]] [[Containers]] [[PostgreSQL]] [[DevOps]]
