---
title: AWS
created: Monday 1st May 2023 14:59
aliases:
  - aws
tags:
  - cloud
  - aws
---
Amazon Web Services is a large web of offerings from [Amazon](https://notes.nicolevanderhoeven.com/Amazon) that are centered around the creation, deployment, maintenance, and operations of web applications.

![[aws-services.png]]

| Tool                                                                  | Description                                                       |
| --------------------------------------------------------------------- | ----------------------------------------------------------------- |
| [Localstack](https://github.com/localstack/localstack)| A fully functional local AWS cloud stack |

- [Amazon Web Services — a practical guide](https://github.com/open-guides/og-aws)
- [AWS Policy Generator](https://awspolicygen.s3.amazonaws.com/policygen.html)
- [Dendron-aws-vault](https://github.com/dendronhq/dendron-aws-vault)
- [AWS Well-Architectured Framework](https://d1.awsstatic.com/whitepapers/architecture/AWS_Well-Architected_Framework.pdf)

- [[AIM]]
## Compute

- [[Fargate]]
- [[EC2]]
- Elastic Beanstalk
## Storage

- [[S3]]
- [[EBS]]
- [[EFS]]
- [[FSx]]
#### Use cases

- **S3**: used for serverless object storage
- **Glacier**: used for archiving objects
- **EFS**: NFS for Linux instances
- **FSx for Lustre**: file storage for HPC linux file systems
- **FSx for Win**: file storage for Windows instances
- **EBS Volumes**: persistent storage for EC2
- **Instance store**: Ephemeral storage for EC2
### Volumes & Snapshots

- Volumes exist on EBS, whereas snapshots exist on S3.
- Snapshots are point-in-time photographs of volume and are incremental in nature.
- You can share snapshots between AWS accounts as well as regions.
- **You can resize EBS volumes on the fly and change types**

### Encryption

- **Data in rest** is encrypted inside the volume.
- All the **data in flight** moving between the instance and the volume is encrypted.
- All snapshots are **encrypted**.
- **All volumes** created from a snapshot encrypted are encrypted.
- **Create a snapshot** of the unencrypted root device volume.
- **Create a copy** of the snapshot and select the **encrypt** option.
### Instance Store

- **Instance store volumes** are sometimes **ephemeral storage**.
- Instance store volumes **cannot be stopped**.
- EBS-backed instances can be stopped.
- You can **reboot** both EBS and instance store volumes and **not lose data**.
- By default root volumes will be **deleted on termination**.
### Backup

- **Consolidation**: use AWS Backup to back up AWS services, sush as EC2, EBS or EFS.
- **Organizations**: use AWS organizations in conjunction with AWS Backup to back up your different AWS services across multiple AWS accounts.
- **Benefits**: Backup gives you centralized control, letting you automate your backups and define lifecycle policies your data.
## Databases

- [[RDS]]
- [[Aurora]]
- [[DynamoDB]]
- Redshift

**OLTP**: processes data from transactions in real time (e.g., customer orders, banking's transactions). **Data processing** and large number of small transactions in real time.
**OLAP**: processes complex queries to analyze historical data (e.g., analyzing net profit figures from the past 3 years and sales forecasting). **Data analysis** using large amount of data.

- **Amazon Document DB** is such as MongoDB
## Networking

- VPCs
- Direct Connect
- Route 53
- API Gateway
- AWS Global Accelerator

## Availability zones and regions

- A **Region** is a physical location in the world of two or more Availability Zones (AZs)
- An **AZs** is one or more discrete data centers -each with redundant power, networking, and connectivity - housed in separate facilities
- **Edge locations** are endpoints for AWS that are used for caching content. Typically, this consists of CloudFront, Amazon's content delivery network (CDN).
## Infrastructure as Code

- [[Cloud Formation]]

## Container orchestration

- [[ECS |Elastic Container Service]]
- [[EKS |Elastic Kubernetes Service]]
- [[ECR |Elastic Container Registry]]

## CLI

First you need to create and Access Key and a Secret Key. Check more information [here](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-quickstart.html).

- **Secret Access Key**: only see once. If you lose, you cand delete and create a new one. COnfigure again the CLI.
- **Dont share key pairs**: each developer have their own access key ID.

- Configure aws for specific user

```bash
aws configure --profile profile-name
```

- User connected

```bash
aws --profile name sts get-caller-identity
```

- List EC2 instances

```bash
# EC2 
aws --profile name ec2 describe-instances --query "Reservations[].Instances[].[Tags[?Key=='Name'],InstanceId,State.Name]" --output text
aws --profile name ec2 start-instances --instance-ids ID
aws --profile name ec2 stop-instances --instance-ids ID
aws --profile name ec2 describe-instances --query "Reservations[].Instances[].[PublicIpAddress]" --output text
```

- Start RDS

```bash
aws --profile name rds stop-db-instance --db-instance-identifier name
```

- Stop RDS

```bash
aws --profile name rds start-db-instance --db-instance-identifier name
```


## Core services for Web App

<u>Static Content</u>

Amazon S3 --> For store static content files.
Amazon Cloudfront --> Chaching for access the application frontstored in S3

<u>Domain management</u>

Amazon Route 53 --> DNS Services, API Routes, Register domain.

<u>API Hosting</u>

Amazon API Gateway + AWS Lambda --> Register a function and upload Lambda and redirect to GW
Aplication Load Balancer + Amazon EC2 --> Deploy inside EC2 a redirecto to LB
Aplicacion Load Balancer + Amazon ECS --> Deploy with Docker images

<u>Database</u>

Amazon RDS --> Typicall SQL servers
Amazon Redshift (BI) --> Very heavy querys and analytics, for huge data and join columns.
Amazon DynamoDB --> NoSQL database (key,value)
Amazon ElasticCache --> Redis, Memcache for store database
Amazon Neptune --> Graph database

<u>Application Orchestration/Coordination</u>

Amazon SNS --> Connect one service to others with some restrictions or rules
Amazon SQS --> Connect one service to others with some restrictions or rules
AWS Step Functions --> Workflow processing or sequence

<u>Analytics, Big Data, ML</u>

Amazon Athnena --> Querys over S3 for analytics
Amazon Quick Sight -> Tableau or PowerBI, build dashboards(BI Tool)
Amazon EMR --> Map Reduce jobs
Amazon Sagemaker --> Build ML with Notebooks

<u>Security</u>

Amazon VPC --> Build digital Firewall around AWS resources, how to access to our applications, ports
AWS IAM --> Configure access for specific resources

<u>Monitoring</u>

Amazon CloudWatch --> Log applications, monitoring, alarms
AWS Cloudtrail --> When you have many users and need track them 


## Traffic

- **Inbound** : Data _inbound_ **to Amazon** (that is, packet data that is **destined for the Amazon** cloud servers; for example, uploads and client requests) are free. 
- **Outbound**: Data _outbound_ **from Amazon** is billed (that is, downloads from the cloud and **responses to client requests**).

![Network](assets/network.jpg)

- Calculate [Data Tansfer](https://aws.amazon.com/ec2/pricing/on-demand/#Data_Transfer) for IN/OUT and in different Regions.
# RDS

[Pricing comparing instances](https://instances.vantage.sh/rds/?region=eu-west-1)

- **RDS** Instance Types based on prices [Prices](https://aws.amazon.com/rds/instance-types/).
# ACM

AWS Certificate Manager ([ACM](https://aws.amazon.com/certificate-manager/))

- [Managing TLS keys and certs in Istio using Amazon’s ACM](https://faun.pub/managing-tls-keys-and-certs-in-istio-using-amazons-acm-8ff9a0b99033)

# EKS

aws eks --region eu-west-1 update-kubeconfig --profile name