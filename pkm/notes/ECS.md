---
title:  ECS
created: Monday 1st May 2023 17:45
aliases: 
tags: cloud, aws
---

![ecs](assets/ecs.png)


> With AWS ECS pricing, you only pay for the underlying resources your containers use.

The primary service for running Docker containers on AWS is ECS. Other container offerings like AWS Fargate and AWS Batch add automated container orchestration on top of ECS.

You can also choose the **AWS EC2 launch type**, which will be familiar to many AWS users. Under this model, you pay for the AWS [[EC2]] instances and **attached EBS volumes that you select to run your containers**. You can get bigger discounts with this model, but because instances are a fixed size, you have to be relatively certain about the requirements of your containers and avoid choosing an EC2 instance that’s too large or small.

- Image (Container)
- Task Definition: you need to define a Task Definition (JSON file) to describe one or more Containers (up to 10) to define all parameters, CPU, Docker image and so on.
- Cluster: the main component is the cluster being a group of EC2 to have HA. Each instance has to have a Container Agent that is the one in charge of Attaching the intancy to the Cluster. ECS optimcize AIM that come with everything needed to run Docker inside.
- Service: allows you to run a number of tasks within the cluster.
- Capacity provider: for the Auto Scaling Group to have how many EC2 intances I can have in the cluster.
- [Network Mode](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html) 
- Logging driver

Mandatory use a Load Balancer for deploying, see [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html)

- [Using ECS tasks on AWS Fargate to replace Lambda functions](https://www.gravitywell.co.uk/insights/using-ecs-tasks-on-aws-fargate-to-replace-lambda-functions/)
- [Deploying Django to AWS ECS with Terraform](https://testdriven.io/blog/deploying-django-to-ecs-with-terraform/)
- [ECSClusterWithTerraform](https://github.com/ptokito/ECSClusterWithTerraform)