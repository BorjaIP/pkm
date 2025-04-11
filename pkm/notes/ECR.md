---
title:  ECR
created: Monday 1st May 2023 17:55
aliases: 
tags: cloud, aws
---

- [Using Amazon ECR Images with Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/userguide/ecr-repositories.html)

To register in `ECR`, first you need to know the password for login using this command: 

```bash
aws ecr get-login-password --profile name | docker login --username AWS --password-stdin <url>
aws ecr get-login --registry-ids <id> --no-include-email --profile name
```
