---
title:  IaC
created: Saturday 29th April 2023 16:10
aliases: 
tags: 
---
**Infrastructure as Code** (IaC) is the managing and provisioning of infrastructure through code instead of through manual processes.

With IaC, configuration files are created that contain your infrastructure specifications, which makes it easier to edit and distribute configurations. It also ensures that you provision the same environment every time. By codifying and documenting your configuration specifications, IaC aids [configuration management](https://www.redhat.com/en/topics/automation/what-is-configuration-management) and helps you to avoid undocumented, ad-hoc configuration changes.

Version control is an important part of IaC, and your configuration files should be under source control just like any other software source code file. Deploying your infrastructure as code also means that you can divide your [infrastructure](https://www.ansible.com/use-cases/infrastructure) into modular components that can then be combined in different ways through automation.

| Tool                                               | Description                                                                       |
| -------------------------------------------------- | --------------------------------------------------------------------------------- |
| [Checkov](https://github.com/bridgecrewio/checkov) | Prevent cloud misconfigurations and find vulnerabilities during build-time in IaC |
| [Pyinfra](https://github.com/pyinfra-dev/pyinfra)  | Automates infrastructure using [[Python]]                                         |
# Frameworks

- [[Chef]]
- [[Ansible]]
- [[Terraform]]