---
title: Prometheus
created: Monday 1st May 2023 15:04
aliases: 
tags: []
---
**Prometheus** is a free software application used for event monitoring and alerting. It records metrics in a time series database built using an HTTP pull model, with flexible queries and real-time alerting.

[[Kubernetes]], [Prometheus](https://prometheus.io/), and [Grafana](https://grafana.com/oss/grafana?pg=blog&plcmt=body-txt) are a trio of technologies that have transformed cloud native development. However, despite how powerful these three technologies are, developers still face gaps in the process of implementing a mature Kubernetes environment.

| Tool                                                         | Description                                                           |
| ------------------------------------------------------------ | --------------------------------------------------------------------- |
| [Thanos](https://github.com/thanos-io/thanos)                | Highly available Prometheus setup with long term storage capabilities |
| [Node exporter](https://github.com/prometheus/node_exporter) | Exporter for machine metrics (Prometheus)                             |
| [DCGM exporter](https://github.com/NVIDIA/dcgm-exporter)     | NVIDIA GPU metrics exporter for Prometheus leveraging DCGM            |

# Articles/Talks

- [Open source, highly available Prometheus setup with long term storage capabilities](https://thanos.io/)

# Helm

```bash
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update

helm upgrade --install kube-prometheus-stack prometheus-community/kube-prometheus-stack \
  --namespace monitoring --create-namespace
# see status
helm status kube-prometheus-stack -n monitoring
```

- Deployment note

```bash
1. Get the application URL by running these commands:
export POD_NAME=$(kubectl get pods --namespace monitoring -l "app.kubernetes.io/name=prometheus-node-exporter,app.kubernetes.io/instance=kube-prometheus-stack" -o jsonpath="{.items[0].metadata.name}")
                      echo "Visit http://127.0.0.1:9100 to use your application"
                      kubectl port-forward --namespace monitoring $POD_NAME 9100
                    kube-prometheus-stack has been installed. Check its status by running:
                      kubectl --namespace monitoring get pods -l "release=kube-prometheus-stack"
                    
                    Visit https://github.com/prometheus-operator/kube-prometheus for instructions on how to create & configure Alertmanager and Prometheus instances using the Operator.
                    
                    kube-state-metrics is a simple service that listens to the Kubernetes API server and generates metrics about the state of the objects.
                    The exposed metrics can be found here:
                    https://github.com/kubernetes/kube-state-metrics/blob/master/docs/README.md#exposed-metrics
                    
                    The metrics are exported on the HTTP endpoint /metrics on the listening port.
                    In your case, kube-prometheus-stack-kube-state-metrics.monitoring.svc.cluster.local:8080/metrics
                    
                    They are served either as plaintext or protobuf depending on the Accept header.
                    They are designed to be consumed either by Prometheus itself or by a scraper that is compatible with scraping a Prometheus client endpoint.
                    
                    1. Get your 'admin' user password by running:
                    
                       kubectl get secret --namespace monitoring kube-prometheus-stack-grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo
                    
                    
                    2. The Grafana server can be accessed via port 80 on the following DNS name from within your cluster:
                    
                       kube-prometheus-stack-grafana.monitoring.svc.cluster.local
                    
                       Get the Grafana URL to visit by running these commands in the same shell:
                         export POD_NAME=$(kubectl get pods --namespace monitoring -l "app.kubernetes.io/name=grafana,app.kubernetes.io/instance=kube-prometheus-stack" -o jsonpath="{.items[0].metadata.name}")
                         kubectl --namespace monitoring port-forward $POD_NAME 3000
                    
                    1. Login with the password from step 1 and the username: admin
                    #################################################################################
                    ######   WARNING: Persistence is disabled!!! You will lose your data when   #####
                    ######            the Grafana pod is terminated.                            #####
                    #################################################################################
```
