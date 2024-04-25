---
title:  Istio
created: Saturday 29th April 2023 16:49
aliases: 
tags: k8s
---
[Istio](https://istio.io/) makes it easy to create a network of deployed services with load balancing, service-to-service authentication, monitoring, and more. You add Istio support to services by deploying a special sidecar proxy throughout your environment that intercepts all network communication between microservices, then configure and manage Istio using its control plane functionality. Was developed on top of [[Kubernetes]].

- [How to easily setup Istio service mesh in AWS EKS](https://www.linkedin.com/pulse/how-easily-setup-istio-service-mesh-aws-eks-ihar-vauchok)
- [Deploying an Istio Gateway with TLS in EKS using the AWS Load Balancer Controller](https://itnext.io/deploying-an-istio-gateway-with-tls-in-eks-using-the-aws-load-balancer-controller-448812e081e5)


![[istio-architecture.png]]

## Components

### Service Entry

**ServiceEntry** enables adding additional entries into Istio’s internal service registry so that auto-discovered services in the mesh can access/route to these manually specified services. Istio ServiceEntry is the way to define an endpoint that doesn’t belong to the Istio Service Registry.

```yaml
apiVersion: networking.istio.io/v1beta1
kind: ServiceEntry
metadata:
  name: proxy
spec:
  hosts:
  - my-company-proxy.com # ignored
  addresses:
  - 64.103.36.135
  ports:
  - number: 80
    name: tcp
    protocol: TCP
  location: MESH_EXTERNAL
```
### Virtual Service

### Gateway

### Sidecar Proxy
## CLI

- [Cheatsheet](https://istio-cheatsheet.tetratelabs.io/istioctl)
- Display logs from proxy-config (kubeflow example)

```bash
istioctl pc log --level "rbac:debug" profiles-kfam-*.kubeflow
```