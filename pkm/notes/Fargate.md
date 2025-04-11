---
title:  Fargate
created: Monday 1st May 2023 17:48
aliases: 
tags: cloud, aws
---
[AWS Fargate](https://aws.amazon.com/fargate/) is a serverless compute engine for containers. It changes the distribution model entirely so that instead of needing to provision _servers_, you only need to think about the _applications_.

Fargate seems to be a management layer that abstracts away some of the complexity of container orchestration. However, it still needs either [[EKS]] or [[ECS]] in the background.

- Testing the solution for **optimize cost-effective**.
  
**AWS offers a custom [distributed load testing solution](https://aws.amazon.com/solutions/implementations/distributed-load-testing-on-aws/)** for AWS Fargate that can help you establish your performance requirement under load, but be aware that this solution will incur costs as it utilizes several AWS services.

- [Building Real Time AI with AWS Fargate](https://aws.amazon.com/es/blogs/architecture/building-real-time-ai-with-aws-fargate/)
- [Samsung Builds a Secure Developer Portal with Fargate and ECR](https://aws.amazon.com/es/blogs/architecture/samsung-builds-a-secure-developer-portal-with-fargate-and-ecr/)