---
title:  De Lambda a Kappa - evolución de las arquitecturas Big Data
created: Saturday 12th April 2025 00:13
aliases: 
tags:
  - architecture
  - big-data
---
- https://www.paradigmadigital.com/techbiz/de-lambda-a-kappa-evolucion-de-las-arquitecturas-big-data/
- Type: article
- Source: Paradigma Digital (in Spanish) · Jesús Domínguez · Apr 2018

---

# TL;DR

**Lambda** combines batch and speed layers over the same data, while **Kappa** drops the batch layer and treats everything as a stream that can be replayed.

# Summary

[[Big Data]] projects usually run on distributed storage such as HDFS, and Spark's in-memory processing moved the field toward real-time. Lambda (Nathan Marz, 2012) aims for fault tolerance, linear scalability and low-latency reads with three layers: batch (immutable raw data and batch views), serving (indexes the views) and speed (recent data into real-time views). Kappa (Jay Kreps, 2014) simplifies this into one stream-processing flow, recomputing views by replaying events.

# Key takeaways

1. **Lambda layers**: batch, serving and speed; queries merge batch and real-time views.
2. **Kappa pillars**: everything is a stream, source data is never modified, one processing flow, and jobs can be relaunched with new logic on the same input.
3. **Kappa requires ordered events** that are read and stored in the order they were generated.
4. **Choose Kappa** when batch and streaming do the same analysis (for example tracking movement between cell towers).
5. **Choose Lambda** when you need full dataset access or batch and streaming results differ, such as a recommender trained in batch with real-time ratings.
6. **No single answer**: the article closes with "one size does not fit all" and the need to revise architectures.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[Big Data]] | Context: HDFS, Hive, HBase, Spark |
| [[Data Engineering]] | Pipeline architecture choices |
| [[Kafka]] | Typical event log for Kappa (not mentioned in the article) |
| [[Architecture Patterns]] | Lambda and Kappa as patterns |

# When to use

1. When **choosing between Lambda and Kappa** for a data platform.
2. When explaining **batch vs streaming** and replayable event logs.
3. When designing real-time ML features alongside batch training.

# Caveats

- 2018 article in Spanish, summarised here in English; it does not detail Lambda's drawbacks or name Kafka/Flink.

---
[[Big Data]] [[Data Engineering]] [[Architecture Patterns]] [[Kafka]]
[[Keeping your ML model in shape with Kafka, Airflow and MLFlow]]
[[Cloud Architecture Patterns]]
