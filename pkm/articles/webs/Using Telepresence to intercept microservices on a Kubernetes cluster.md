---
title:  Using Telepresence to intercept microservices on a Kubernetes cluster
created: Friday 11th April 2025 23:09
aliases: 
tags:
  - k8s
  - devops
  - microservices
---
- https://medium.com/@backin200ms/using-telepresence-to-intercept-microservices-on-a-kubernetes-cluster-ebaa0691fc0f
- Type: tutorial
- Source: Medium · vjay baskr

---

# TL;DR

**Telepresence** intercepts a service in a [[Kubernetes]] cluster and redirects its traffic to a process on your laptop, so you debug one microservice locally while the rest runs remotely.

# Summary

The tutorial builds a Spring Petclinic microservices demo on a local kind cluster: install the services, three MySQL databases (Bitnami Helm chart) and the app with a deploy script. With no ingress, access goes through Telepresence. After `telepresence connect`, `telepresence list` shows interceptable workloads, and `telepresence intercept <svc> --port local:remote` installs a traffic agent and routes the service's traffic to `127.0.0.1`. The services are then run locally with `mvn spring-boot:run` and tested through the cluster IP of the API gateway.

# Key takeaways

1. **Connect first**: `telepresence connect` joins your machine to the cluster network.
2. **List targets** with `telepresence list --namespace <ns>`.
3. **Intercept a workload** with `telepresence intercept customers-service --port 8081:8080 --namespace <ns>`; all its TCP connections go to your local port.
4. **Run the service locally** (IDE or debug mode) and exercise the full app through the cluster.
5. **Clean up** the intercepts when finished.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[Kubernetes]] | kind cluster hosting the demo |
| [[Helm]] | Installs the MySQL databases |
| [[Skaffold]] | Alternative inner-loop tool for the same goal |
| Telepresence | Traffic agent and intercept mechanism |

# When to use

1. When **debugging one microservice locally** against a real cluster.
2. When you need the **intercept command syntax** and sequence.

# Caveats

- The demo prints a volume-mount warning because `sshfs` is missing locally; remote volumes are not mounted.
- Versions are not stated, and Telepresence's CLI has evolved, so check current docs.

---
[[Kubernetes]] [[Skaffold]] [[Helm]] [[DevOps]]
[[Reducing Cloud Costs on Kubernetes Dev Envs]]
