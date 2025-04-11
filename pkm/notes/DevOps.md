---
title: DevOps
created: Sunday 23rd April 2023 16:57
aliases: 
tags:
---
DevOps is **the combination of cultural philosophies, practices, and tools that increases an organization's ability to deliver applications and services at high velocity**: evolving and improving products at a faster pace than organizations using traditional software development and infrastructure management processes.

![[devops.png]]

- [DevOps Roadmap](https://roadmap.sh/devops)
- [DevOps Newsletters](https://devopsnewsletters.com/)
- [DevOps Community](https://github.com/rohitg00/DevOpsCommunity)
- [Developer Handbook](https://github.com/apptension/developer-handbook/blob/master/Technical%20Stack/DevOps%20Developer.md)
- [DevOps Docs](https://roadmap.sh/devops)
- [DevOps Exercises](https://github.com/bregman-arie/devops-exercises)

# Continuous Integration / Continuous Delivery (CI/CD)

The term CI/CD is commonly used today to describe the overarching tools and practices that are pulling the practices of build, test, and deployment automation together to happen multiple times a day as code merges to the product’s production branch/trunk become more frequent.

- [Continuous integration](https://en.wikipedia.org/wiki/Continuous_integration?ref=hackernoon.com) is the practice of using a CI-specific server to frequently merge code branches into the mainline version of working application source code, or to flag code if a merge will cause errors. 

- [Continuous delivery](https://en.wikipedia.org/wiki/Continuous_delivery?ref=hackernoon.com) is the concept of being able to have a chain of automation that makes any new code commit result in a new, deployable version of the application with the changes included. This deployable artifact automatically goes through test automation, CI, build automation, and any other deployment preparations, such as building new containers for the application.

The four most popular CI engines (they are all language-agnostic) are [[Jenkins]], [TravisCI](https://travis-ci.org/?ref=hackernoon.com), [CircleCI](https://circleci.com/?ref=hackernoon.com), and [TeamCity](https://www.jetbrains.com/teamcity/?ref=hackernoon.com).

# Configuration Management

This category has a very broad sounding name, but in most software engineering circles it’s used as a descriptor for tools that codify individual machine definitions. These tools install and manage operating system configurations on existing servers. 

The four major configuration management tools are [Chef](https://github.com/chef/chef?ref=hackernoon.com), [Puppet](https://github.com/puppetlabs/?ref=hackernoon.com), [Ansible](https://www.ansible.com/resources/get-started?ref=hackernoon.com), and [Salt](https://docs.saltstack.com/en/latest/?ref=hackernoon.com). They were some of the first tools to codify IT infrastructure management—much in the same way that developers had codified their testing, build, and CI practices and version-controlled those files—making them the first drivers of the “infrastructure as code” and DevOps movements.

# Container / Cluster orchestrators

Container orchestrators take the benefits of containers and make it easy to scale up their deployment and management. VMs can also benefit from this approach. 

At their core, they are [cluster schedulers](https://medium.com/@copyconstruct/schedulers-kubernetes-and-nomad-b0f2e14a896?ref=hackernoon.com)—intelligent systems that optimize the usage of cloud/virtual infrastructure as if your applications were Tetris pieces. Essentially, a scheduler takes a configuration file with some rules and then goes and deploys any number of applications, services, or components (e.g. load balancers, etc) on containers or VMs in the most optimal way for a given infrastructure according to your parameters.

Orchestrators include [[Kubernetes]], which has a host of additional features, and [Nomad](https://www.nomadproject.io/?ref=hackernoon.com), which has a more focused scheduling use case.

# Development & Testing

-   Security-focused static analysis (SAST) - [SonarQube](http://www.sonarqube.org/?ref=hackernoon.com), [FindBugs](https://www.baeldung.com/intro-to-findbugs?ref=hackernoon.com), [Checkmarx](https://www.checkmarx.com/?ref=hackernoon.com)
-   Dynamic security test automation, such as DAST and penetration testing (pen testing) - [FindBugs](https://www.baeldung.com/intro-to-findbugs?ref=hackernoon.com), [Checkmarx](https://www.checkmarx.com/?ref=hackernoon.com), [OWASP ZAP](https://github.com/zaproxy/zaproxy?ref=hackernoon.com), [ThreadFix](http://www.threadfix.org/?ref=hackernoon.com)
-   Third-party component risk analysis and alerting - [Snyk](https://snyk.io/?ref=hackernoon.com), [BlackDuck](https://www.blackducksoftware.com/?ref=hackernoon.com), [WhiteSource](https://www.whitesourcesoftware.com/?ref=hackernoon.com)
-   Credential/secrets management - [[Vault |HashiCorp Vault]], [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/?ref=hackernoon.com)
# As a Code

The *“as code”* buzzwords started with *infrastructure as code* ([[IaC]]) and the [[DevOps]] movement, when IT operations/sysadmins and developers started working together to automate IT environment modifications with reusable code and then [version control](https://www.git-tower.com/learn/git/ebook/en/command-line/basics/why-use-version-control?ref=hackernoon.com) that code much like developers had been handling their application code changes for many years before.

## Architecture as code

Being able to create software architecture models as code has been possible for a while. Tools like [Structurizr](https://structurizr.com/?ref=hackernoon.com) allow you to build diagrams this way and check them into version control. But for decades developers have tried, with varied results, to do more with these application models.

The concept of [model-driven development](https://en.wikipedia.org/wiki/Model-driven_engineering?ref=hackernoon.com) was heavily discussed 10-20 years ago, but it never really took off in mainstream development. Its basic premise is that you can make models of software components using modeling languages like UML or EMF to generate entire starter applications based on the requirements you code.

## Projects as code + Scaffolding

The code generation concepts from model-driven development, however, are as old as programming itself. The compilers that turn Ruby, [[Python]], or [[Java]] into C code are all generators. Even novice frontend programmers today understand the importance of code generation, which saves you from writing blocks and blocks of the dreaded stuff we consider [boilerplate code](https://en.wikipedia.org/wiki/Boilerplate_code?ref=hackernoon.com).

There is a lot of room for novel automation in this category, and in the last few years “projects as code”—repo and delivery pipeline setup for applications—has filled in some gaps that tools coming out of the DevOps movement hadn’t addressed yet. Tools like [Yeoman](https://yeoman.io/?ref=hackernoon.com) for JavaScript projects and [JHipster](https://www.jhipster.tech/?ref=hackernoon.com) for Java projects have provided bare-bones, flexible frameworks for setting up projects using Node.js and Spring Boot+Angular respectively. [[Cloud]] vendors, such as Microsoft Azure, are creating [tools](https://azure.microsoft.com/en-us/services/devops/pipelines/?ref=hackernoon.com) that set up delivery pipelines. Another company, realMethods, [has built a tool](https://modeling-languages.com/realmethods-devops-project-generation/?ref=hackernoon.com) that takes database schema or modeled requirements and uses them to generate tech stack specific skeleton code, along with build and config files, CI/CD YAML, Docker files and images, Kubernetes cluster config, and Terraform provisioning files.

## Application environment as code

Virtual machines (VMs), containers, and other various abstractions of a software production environment have been a blessing to developers for many years as they continue to get better and easier to manage. Why try and debug 100 different things that could go wrong while manually setting up an operational environment when you can automatically spin up template environments that allow you to start coding with almost no issues?

Technologies like [Vagrant](https://www.vagrantup.com/?ref=hackernoon.com) and later [[Docker]] (and [[Container]] in general) made development environment setup a whole lot easier. Both containers and container orchestrators (such as Kubernetes or Nomad) became popular tools for deploying environments in agile, isolated, correctly configured pieces.
## Infrastructure as Code

The full promise of infrastructure as code came with provisioning tools, which—in addition to providing templates for the configuration of infrastructure components—could also boot up the infrastructure itself. This also became much easier as more organizations started using cloud infrastructure that could be spun up with the push of a button.

Provisioning systems include [CloudFormation](https://aws.amazon.com/cloudformation/?ref=hackernoon.com) for AWS only, [ARM](https://docs.microsoft.com/en-us/azure/azure-resource-manager/resource-group-overview?ref=hackernoon.com) for Azure only, and [[Terraform]], which is one of the more popular open-source options because it can provision across any major cloud provider. Because of these systems’ ability to manage the complexity of infrastructure at scale, they are becoming one of the primary interfaces that operators use to interact with their infrastructure.

## Configuration as Code

**Configuration as code** (CAC) is managing configuration resources in your source repository. You treat your application config resources as versioned artifacts. By managing your application environment in tandem with your application code, you gain the same benefits you get with your code.

The adoption of CaC offers numerous benefits, including consistency, repeatability, and faster recovery from failures. It reduces the possibility of human error in [configuration management](https://configu.com/blog/configuration-management-what-devops-teams-need-to-know/), leading to higher reliability. Moreover, since configuration is managed as code, it can be version controlled, enabling easy tracking of changes and rollback if necessary.

The [Configu Orchestrator](https://github.com/configu/configu), which is open-source software, is a powerful standalone tool designed to address this challenge by providing configuration orchestration along with Configuration-as-Code (CaC) approach.
## Policy as Code

**Policy as code** is an approach to policy management in which policies are defined, updated, shared, and enforced using code. By leveraging code-based automation instead of relying on manual processes to manage policies, policy-as-code allows teams to move more quickly and reduce the potential for mistakes due to human error.

At the same time, a policy as code approach to domains like security makes it possible to define and manage policies in ways that different types of stakeholders. Teams write out policies using some type of programming language, such as Python, YAML, or [Rego](https://www.paloaltonetworks.com/content/pan/en_US/blog/prisma-cloud/prisma-cloud-compute-open-policy-agent/).

You may also want to explore tools like [Open Policy Agent](https://www.paloaltonetworks.com/content/pan/en_US/blog/prisma-cloud/prisma-cloud-compute-open-policy-agent/), which aims to provide a common framework for applying PaC to any domain. 

---
# References

[1]: [What is Everything-as-Code?](https://hackernoon.com/everything-as-code-explained-0ibg32a3)