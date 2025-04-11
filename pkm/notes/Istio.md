---
title: Istio
created: Saturday 29th April 2023 16:49
aliases: 
tags:
  - k8s
---
[Istio](https://istio.io/) makes it easy to create a network of deployed services with load balancing, service-to-service authentication, monitoring, and more. You add Istio support to services by deploying a special sidecar proxy throughout your environment that intercepts all network communication between microservices, then configure and manage Istio using its control plane functionality. Was developed on top of [[Kubernetes]].

- [[How to easily setup Istio service mesh in AWS EKS]]
- [[Deploying an Istio Gateway with TLS in EKS using the AWS Load Balancer Controller]]


![[istio_architecture.png]]

# Service Mesh

[Istio service mesh](https://imesh.ai/blog/what-is-istio/) is the powerful software to enable zero trust by enabling authentication, authorization, and audit using mTLS or just encryption of [[PET#Data in Transit|data-in-transit]] and identity controls. Platform teams, cloud architects of large organizations have implemented security using Istio. To implement security, Istio involves the following components- a certificate authority (CA) for key management, API to distribute Authn/Authz policies to proxies, Policy Enforcement Points (PEPs) implemented using sidecars (Envoy proxies), and extensions to manage telemetry.

- **Secure overlay layer** (also known as **zero-trust tunnel or ztunnel**)is a L4 processing layer designed to implement TCP routing and handle zero trust security for traffic such as [mTLS](https://imesh.ai/blog/what-is-mtls-and-how-to-implement-it-with-istio/), Authentication and Authorization policies. 
-  **L7 processing layer** (also known as **waypoint proxy**) is designed to handle complex traffic management functionalities such as HTTP routing, circuit breaking, chaos engineering, reties, timeouts, rate limiting, etc, and handle granular Authn/Authz policy implementation.


![[service_mesh.png]]
# Ambient mesh

Istio ambient mesh is a **sidecar-less implementation of Istio**. It is comparatively faster, lightweight, and provides all the L4 and L7 functionality of Istio.

![[ztunnel.png]]

The connection between ztunnels happens over an HTTP tunnel, called HBONE (or HTTP-Based Overlay Network Environment), where the traffic is encrypted with mTLS. **Waypoint proxy** is basically Envoy which is deployed as a pod, not as a container. **It is deployed per namespace or service account**.

[Ztunnel](https://github.com/istio/ztunnel/) is an agent, primarily a rust-based proxy, whose responsibility is to securely connect and authenticate elements within the mesh. One can deploy ztunnel as a DaemonSet workload resource on a Kubernetes cluster. Ztunnel is a dedicated L4 technology and is deployed per node in a cluster. The idea is ztunnel will be shared among all the workloads in a node it is deployed to. The ztunnel leverages leverages Kubernetes CNI to establish connections between workloads, secure communication using mTLS, collect HTTP metrics, access logs, etc

# Components

## Service Entry

**ServiceEntry** enables adding additional entries into Istio’s internal service registry so that auto-discovered services in the mesh can access/route to these manually specified services. Istio ServiceEntry is the way to define an endpoint that doesn’t belong to the Istio Service Registry.

## Virtual Service

## Gateway

## Sidecar Proxy
# CLI

- [Cheatsheet](https://istio-cheatsheet.tetratelabs.io/istioctl)
- Display logs from proxy-config (kubeflow example)

```bash
istioctl pc log --level "rbac:debug" profiles-kfam-*.kubeflow
```