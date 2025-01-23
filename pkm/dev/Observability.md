---
title:  Observability
created: Tuesday 5th March 2024 14:14
aliases: 
tags: 
---
**Observability** is the ability to assess a system’s current state based on the data it produces. Typically executed by dedicated software tools, observability helps developers gain end-to-end real-time visibility of their distributed infrastructure. It enables them to **monitor key performance indicators and metrics, troubleshoot and debug applications and networks, detect anomalies, identify patterns or trends, and address issues** before they impact the bottom line.

Observability in [[DevOps]] is a technical or tooling solution that focuses on aiding IT firms to understand what procedures are going on in an app by looking at the app’s output. Observability also allows firms to know issues in the app operation by pinpointing **what, where, how, and why the app operation is malfunctioning**.

Blending [AIOps](https://middleware.io/blog/how-generative-ai-can-transform-observability/) (the practice of using [[Artificial Intelligence|AI]] and [[Machine Learning]] to enhance and automate IT operations) and Observability can optimize real user monitoring and automate the analysis of vast data streams, allowing teams to maximize their overall efficiency to a great extent

| Tool                                                            | Description                                                                                                        |
| --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| [OpenSearch](https://github.com/opensearch-project/OpenSearch)  | Open source distributed and RESTful search engine                                                                  |
| [Openobserve](https://github.com/openobserve/openobserve)       | Cloud-native observability platform built specifically for logs, metrics, traces, analytics                        |
| [Opentelemetry](https://opentelemetry.io/)                      | Use it to instrument, generate, collect, and export telemetry data                                                 |
| [Openmetrics](https://github.com/OpenObservability/OpenMetrics) | Evolving the Prometheus exposition format into a standard                                                          |
| [cAdvisor](https://github.com/google/cadvisor)                  | Analyzes resource usage and performance characteristics of running containers                                      |
| [Node exporter](https://github.com/prometheus/node_exporter)    | Exporter for machine metrics (Prometheus)                                                                          |
| [DCGM exporter](https://github.com/NVIDIA/dcgm-exporter)        | NVIDIA GPU metrics exporter for Prometheus leveraging DCGM                                                         |
| [Checkmate](https://github.com/bluewave-labs/checkmate)         | Open-source, self-hosted tool designed to track and monitor server hardware, uptime, response times, and incidents |
# Logs

[Logs](https://middleware.io/product/log-monitoring/) are records of each individual event that happens within an application during a particular period, with a timestamp to indicate when the event occurred. They help reveal unusual behaviors of components in a microservices architecture.

- Plain text: Common and unstructured.
- Structured: Formatted in JSON.
- Binary: Used for replication, recovery, and system journaling.

Cloud-native components emit these log types, leading to potential noise. Observability transforms this data into actionable information.
# Metrics

[Metrics](https://middleware.io/blog/devops-metrics-you-should-be-monitoring/) are numerical values describing service or component behavior over time. They include time stamps, names, and values, providing easy query ability and storage optimization. Metrics offer a comprehensive overview of system health and performance across your infrastructure.

However, metrics have limitations. Though they indicate breaches, they **do not shed light on underlying causes.** NO ROOT CAUSE
# Traces

[Traces](https://middleware.io/blog/what-is-distributed-tracing/) complement logs and metrics by tracing a request’s lifecycle in a distributed system.

They help analyze request flows and operations encoded with microservices data, identify services causing issues, ensure quick resolutions, and suggest areas for improvement.