---
title:  Prometheus
created: Monday 1st May 2023 15:04
aliases: 
tags: k8s
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