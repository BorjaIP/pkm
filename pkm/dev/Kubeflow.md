---
title:  Kubeflow
created: Sunday 30th April 2023 20:09
aliases: 
tags: k8s
---
Kubeflow is an open-source platform for [[machine learning]] and MLOps on [[Kubernetes]] introduced by Google. The different stages in a typical machine learning lifecycle are represented with different software components in Kubeflow, including **model development, model training, model serving, and automated machine learning.**

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
|[Yatai](https://github.com/bentoml/yatai)|Model Deployment at Scale on Kubernetes|

- [Building a Complete AI Based Search Engine with Elasticsearch, Kubeflow and Katib](https://towardsdatascience.com/building-a-complete-ai-based-search-engine-with-elasticsearch-kubeflow-and-katib-590c7b27eb8f)
- [Search system on top of Elasticsearch, Kubeflow and Katib](https://github.com/WillianFuks/pySearchML)
- [An end-to-end ML pipeline on-prem:  Notebooks & Kubeflow Pipelines on the new MiniKF](https://medium.com/kubeflow/an-end-to-end-ml-pipeline-on-prem-notebooks-kubeflow-pipelines-on-the-new-minikf-33b7d8e9a836)
- [Distributed TensorFlow training using Kubeflow on Amazon EKS](https://aws.amazon.com/es/blogs/opensource/distributed-tensorflow-training-using-kubeflow-on-amazon-eks/)
- [Building a ML Pipeline from Scratch with Kubeflow](https://blogs.cisco.com/developer/machinelearningops03)
- [Train and Serve TensorFlow Models at Scale with Kubernetes and Kubeflow on Azure](https://github.com/Azure/kubeflow-labs)

<iframe width="560" height="315" src="https://www.youtube.com/embed/lu5zHvpQeSI" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

<iframe width="560" height="315" src="https://www.youtube.com/embed/VDINH5WkBhA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

## KServe

- [Deploy Custom Python Serving Runtime with InferenceService[¶](https://kserve.github.io/website/0.10/modelserving/v1beta1/custom/custom_model/#deploy-custom-python-serving-runtime-with-inferenceservice "Permanent link")](https://kserve.github.io/website/0.10/modelserving/v1beta1/custom/custom_model/)
- [Open Inference Protocol (V2 Inference Protocol)](https://kserve.github.io/website/0.10/modelserving/data_plane/v2_protocol/)
- [Your next KServe ML service: gRPC vs JSON-REST](https://medium.com/bumble-tech/your-next-kserve-ml-service-grpc-vs-json-rest-2e3a512fba9e)