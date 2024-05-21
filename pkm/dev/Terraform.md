---
title: Terraform
created: Sunday 23rd April 2023 16:58
aliases:
  - opentf
tags:
---


| Tool                                                     | Description                                                          |
| -------------------------------------------------------- | -------------------------------------------------------------------- |
| [Terragrunt](https://github.com/gruntwork-io/terragrunt) | Terragrunt is a thin wrapper for Terraform that provides extra tools |
| [Terracost](https://github.com/cycloidio/terracost)      | Cloud cost estimation for Terraform in your CLI                      |
| [Infracost](https://github.com/infracost/infracost)      | Cloud cost estimates for Terraform in pull requests                  |
| [TFLint](https://github.com/terraform-linters/tflint)                                                         | Terraform Linter                                                                     |

- [Linux Academy - Using Terraform to Manage Applications and Infrastructure](https://github.com/linuxacademy/content-terraform-2021)
- [How To Structure a Terraform Project](https://www.digitalocean.com/community/tutorials/how-to-structure-a-terraform-project)
- [Creates a standalone Docker host on EC2](https://github.com/futurice/terraform-examples/tree/master/aws/aws_ec2_ebs_docker_host)
- [Terraform's Azure Provider to provision resources in Azure](https://github.com/hashicorp/terraform-provider-azurerm/tree/main/examples)
- [Docker the Terraform Way](https://joachim8675309.medium.com/docker-the-terraform-way-a7c16b5f59ed)
- [Terraform at Scale — Modualized Hierachical Layout and Continuous Delivery of Infrastructure](https://faun.pub/terraform-at-scale-modualized-hierachical-layout-cb5dbe5a368d)

## Instalation

```bash
# Download
TER_VER=`curl -s https://api.github.com/repos/hashicorp/terraform/releases/latest | grep tag_name | cut -d: -f2 | tr -d \"\,\v | awk '{$1=$1};1'`
wget https://releases.hashicorp.com/terraform/${TER_VER}/terraform_${TER_VER}_linux_amd64.zip

# Unzip
unzip terraform_${TER_VER}_linux_amd64.zip
sudo mv terraform /usr/local/bin/
```


- Display graph

```bash
export TF_VAR_rds_password=foobarbaz
terraform graph | dot -Tpng > infrastructure_graph.png
```

- Terraform destroy AWS ECS

```bash
terraform destroy -target=aws_ecs_service.backend -target=aws_ecs_task_definition.backend -target=module.vpc.aws_eip.nat -target=aws_lb.lb -target=aws_autoscaling_group.ecs-cluster
```


# OpenTF

[OpenTofu](https://github.com/opentofu/opentofu?tab=readme-ov-file) is an OSS tool for building, changing, and versioning infrastructure safely and efficiently. OpenTofu can manage existing and popular service providers as well as custom in-house solutions.