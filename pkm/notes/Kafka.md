---
title:  Kafka
created: Saturday 12th October 2024 17:52
aliases: 
tags: Kafka
---
[[Apache]] Kafka is an open-source distributed event streaming platform used for building real-time data pipelines and streaming applications. Originally developed by LinkedIn and later donated to the Apache Software Foundation, Kafka is designed to handle high-throughput, low-latency data streams across distributed systems. It acts as a message broker, facilitating the continuous exchange of data between producers (sources of data) and consumers (applications that process data).

Kafka's key features include its ability to scale horizontally across multiple servers, fault tolerance, and the ability to retain large volumes of data for extended periods. It supports use cases such as real-time analytics, event-driven architectures, log aggregation, and streaming ETL (Extract, Transform, Load) processes. With its publish-subscribe model, Kafka has become a critical component in modern data architectures, enabling organizations to build scalable, high-performance streaming platforms.

| Tool                                                                        | Description                         |
| --------------------------------------------------------------------------- | ----------------------------------- |
| [strimzi-kafka-operator](https://github.com/strimzi/strimzi-kafka-operator) | Apache Kafka® running on Kubernetes |
# Helm chart

- Bitnamy instructions
- https://github.com/bitnami/charts/blob/main/bitnami/kafka/README.md

```bash
** Please be patient while the chart is being deployed **

Kafka can be accessed by consumers via port 9092 on the following DNS name from within your cluster:

    kafka.develop.svc.cluster.local

Each Kafka broker can be accessed by producers via port 9092 on the following DNS name(s) from within your cluster:

    kafka-controller-0.kafka-controller-headless.kafka.svc.cluster.local:9092
    kafka-controller-1.kafka-controller-headless.kafka.svc.cluster.local:9092
    kafka-controller-2.kafka-controller-headless.kafka.svc.cluster.local:9092

The CLIENT listener for Kafka client connections from within your cluster have been configured with the following security settings:
    - SASL authentication

To connect a client to your Kafka, you need to create the 'client.properties' configuration files with the content below:

security.protocol=SASL_PLAINTEXT
sasl.mechanism=SCRAM-SHA-256
sasl.jaas.config=org.apache.kafka.common.security.scram.ScramLoginModule required \
    username="user1" \
    password="$(kubectl get secret kafka-user-passwords --namespace develop -o jsonpath='{.data.client-passwords}' | base64 -d | cut -d , -f 1)";

To create a pod that you can use as a Kafka client run the following commands:

    kubectl run kafka-client --restart='Never' --image docker.io/bitnami/kafka:3.6.0-debian-11-r2 --namespace develop --command -- sleep infinity
    kubectl cp --namespace develop /path/to/client.properties kafka-client:/tmp/client.properties
    kubectl exec --tty -i kafka-client --namespace develop -- bash

    PRODUCER:
        kafka-console-producer.sh \
            --producer.config /tmp/client.properties \
            --broker-list kafka-controller-0.kafka-controller-headless.develop.svc.cluster.local:9092,kafka-controller-1.kafka-controller-headless.develop.svc.cluster.local:9092,kafka-controller-2.kafka-controller-headless.develop.svc.cluster.local:9092 \
            --topic test

    CONSUMER:
        kafka-console-consumer.sh \
            --consumer.config /tmp/client.properties \
            --bootstrap-server kafka.develop.svc.cluster.local:9092 \
            --topic test \
            --from-beginning
```