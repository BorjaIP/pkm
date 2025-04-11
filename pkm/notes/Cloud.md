---
title:  Cloud
created: Sunday 23rd April 2023 17:34
aliases: 
tags: cloud
---
# Providers

- [[AWS]]
- [[Azure]]
- [[GCP]]
- [[IBM]]
# Hostings and VPS

- [OVH Cloud](https://www.ovhcloud.com/es-es/)
- [Linode](https://www.linode.com/)
# Cost Reduce

1. Cache external dependencies locally to reduce network transfer costs. For example, use pull-through Docker image registries.
2. Prefer **spot instances** for stateless workloads instead of on-demand instances.
3. Use **automated scaling solutions** to shut down development workloads during weekends when possible.
4. Filter logs, metrics, and traces before they reach your monitoring solution. Most solutions (SaaS or self-hosted) charge for storage and ingestion since the SSD/HDD space is the least expensive resource of AWS instead of RAM. 
5. Optimize your application to reduce **CPU hotspots** and **memory leaks**—this can significantly cut infrastructure costs. The same applies to **database queries** and **caching**.
6. Use a **profiler** to identify inefficiencies:
    1. [**JProfiler**](https://digma.ai/9-best-java-profilers-to-use-in-2024/) is great for finding CPU hotspots, memory leaks, and slow DB queries in Java applications.
    2. **Flamegraphs** provide similar insights across multiple languages.
7. Identify inefficient code that leads to unnecessary cloud resource consumption. Whether it’s performance bottlenecks or excessive database queries, [**Digma**](https://digma.ai/engineering-managers/) helps teams optimize before deployment, avoiding costly inefficiencies.
8. The best way to save money is by **preventing unnecessary asset creation**. Implement **asset management workflows and approval processes** to control resource allocation.
9. Plan ahead—understand the cost implications of standing up resources. Estimate **network transit costs** and other variables. Effective cost management comes from **proper planning and proactive monitoring**, not reactive billing analysis.
10. Managed services or A managed: you can use only one managed service, like a stable load balancer but keep in mind that a managed service can increase costs.