---
title: Kubeflow
created: Sunday 30th April 2023 20:09
aliases: 
tags:
  - k8s
---
Kubeflow is an open-source platform for [[Machine Learning]] and MLOps on [[Kubernetes]] introduced by Google. The different stages in a typical machine learning lifecycle are represented with different software components in Kubeflow, including **model development, model training, model serving, and automated machine learning.**

| Tool                                                               | Description                                                 |
| ------------------------------------------------------------------ | ----------------------------------------------------------- |
| [Arena](https://github.com/kubeflow/arena)                         | A CLI for Kubeflow                                          |
| [Romario](https://github.com/datasailors/romario)                  | RESTful API for kick-starting a KF-Pipeline                 |
| [Training-operator](https://github.com/kubeflow/training-operator) | Training operators on Kubernetes                            |
| [Katib](https://github.com/kubeflow/katib)                         | Repository for hyperparameter tuning                        |
| [Fairing](https://github.com/kubeflow/fairing)                     | Python SDK for building, training, and deploying ML models  |
| [KServe](https://github.com/kserve/kserve)                         | Standardized Serverless ML Inference Platform on Kubernetes |
| [Kale](https://github.com/kubeflow-kale/kale)                      | Kubeflow’s superfood for Data Scientists                    |
| [BentoML](https://github.com/bentoml/BentoML)                      | Unified Model Serving Framework                             |
| [Yatai](https://github.com/bentoml/yatai)                          | Model Deployment at Scale on Kubernetes                     |
| [Bootstrap](https://github.com/treebeardtech/kubeflow-bootstrap)   | 🪐 1-click Kubeflow using ArgoCD                            |
# Articles/Talks

- [[Building a Complete AI Based Search Engine with Elasticsearch, Kubeflow and Katib]]
- [[Search system on top of Elasticsearch, Kubeflow and Katib]]
- [[An end-to-end ML pipeline on-prem - Notebooks & Kubeflow Pipelines on the new MiniKF]]
- [[Distributed TensorFlow training using Kubeflow on Amazon EKS]]
- [[Building a ML Pipeline from Scratch with Kubeflow]]
- [[Train and Serve TensorFlow Models at Scale with Kubernetes and Kubeflow on Azure]]

<iframe width="560" height="315" src="https://www.youtube.com/embed/lu5zHvpQeSI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/VDINH5WkBhA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

# Main components 

![[kubeflow_arch.png]]

## Authentication

- [Using Keycloak for Kubeflow (instead of dex)](https://medium.com/@iamestelleyu/dex-is-the-defalut-authentication-application-of-kubeflow-and-there-is-a-option-using-both-dex-and-2cea08ca76f6)
- [Using Keycloak as external OIDC provider on kubeflow](https://velog.io/@hklog/keycloak-kubeflow-dex)

Kubeflow use [ambasador-oidc](https://github.com/arrikto/oidc-authservice) call **oidc-authservice** as an authentication service with an HTTP Server in combination with [Dex](https://journal.arrikto.com/kubeflow-authentication-with-istio-dex-5eafdfac4782) as OIDC provider.
## Centraldashboard

The _Kubeflow Central Dashboard_ provides an authenticated web interface for Kubeflow and ecosystem components. It acts as a hub for your machine learning platform and tools by exposing the UIs of components running in the cluster. Access through the [Istio Gateway](https://istio.io/docs/concepts/traffic-management/#gateways) that provides access to the Kubeflow.
## Notebook

Kubeflow Notebooks provides a way to run web-based development environments inside your Kubernetes cluster by running them inside Pods. Support [[Jupyter]] and VSCode.

Kubeflow use these services for deploy and control notebooks:

- jupyter-web-app-deployment
- volumes-web-app-deployment
- notebook-controller-deployment

Deactivate secure cookies if TLS is not configured.

```bash
# change in kubernetes templates
APP_SECURE_COOKIES = false
```

## Metadata

Kubeflow Pipelines backend stores runtime information of a pipeline run in Metadata store. Runtime information includes the status of a task, availability of artifacts, custom properties associated with Execution or Artifact, etc. Learn more at [ML Metadata](https://github.com/google/ml-metadata/blob/master/g3doc/get_started.md)for using [google/ml-metadata](https://github.com/google/ml-metadata).

Kubeflow use these services:

- MySQL - store metadata
- metadata-envoy-deployment - [envoy](https://www.envoyproxy.io/) proxy 
- metadata-grpc-deployment - allows other components to interact with the metadata service
- metadata-writer - comprehensive record of the entire machine learning lifecycle

## Pipelines

## Cache

The cache server is a key-value storage system that store frequently accessed ML artifacts, such as trained models and intermediate results.

- cache-server
## Admission webhook

We need a way to inject common data (env vars, volumes) to pods (e.g. notebooks). PodPreset implementation, customize it for Kubeflow and rename it to PodDefault to avoid confusion. Use [[Kubernetes#Admission webhook|admision webhook]] and CRD to implement the functionality.

- admission-webhook-deployment

## PVCViewer

Use [filebrowser](https://github.com/filebrowser/filebrowser) for provide a file managing interface within a specified directory.

## Metacontroller

Use metacontroller as an add-on for Kubernetes that makes it easy to write and deploy  [[Kubernetes#Custom resources|custom resources]]
## Istio

## KServe

- [[KServe - The State and Future of Cloud-Native Model Serving]]
- [[Open Inference Protocol (V2 Inference Protocol)]]
### Add SSL

- Create certificate

```bash
kubectl create -n knative-serving secret tls custom-certs --key registry.key --cert registry.crt
```

- Edit deployment knative-serving

```yaml
apiVersion: apps/v1  
kind: Deployment  
metadata:  
  name: controller  
  namespace: knative-serving  
spec:  
  template:  
    spec:  
      containers:  
        - name: controller  
          volumeMounts:  
            - name: custom-certs  
              mountPath: /path-to-docker-registry-cert  # replace here.  
          env:  
            - name: SSL_CERT_FILE  
              value: /path-to-docker-registry-cert # replace here.  
            - name: GODEBUG  
              value: x509ignoreCN=0  
      volumes:  
        - name: custom-certs  
          secret:  
            secretName: custom-certs
```

## Other components


# CLI

Use [kfp](https://kubeflow-pipelines.readthedocs.io/en/stable/index.html)for interact with Kubeflow as and API for Python, the CLI version only works with [[GCP]] (Google Cloud Platform).

- You can perform all operations with the API 