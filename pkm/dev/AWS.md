---
title:  AWS
created: Monday 1st May 2023 14:59
aliases: aws
tags: cloud, aws
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
## Compute

- [[Fargate]]
- [[EC2]]
- Elastic Beanstalk
## Storage

- [[S3]]
- EBS
- EFS
- FSx
- Storage Gateway
## Databases

- RDS
- DynamoDB
- Redshift
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

## AIM

Identity and Access Management (IAM) provides fine-grained access control across all of AWS. With IAM, you can control access to services and resources under specific conditions. Use IAM policies to manage permissions for your workforce and systems to ensure [least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege). 
### Tips

- The root account is the email address you used to sign up for AWS. The **root account** has **full administrative access** to AWS. For this reason, it is important to secure this account.
- Always create an **MFA** for good security.
- Create an **admin** group and add users to the group.
- If for some reason you are stuck in a scenario where you have policies mapped against you that have both of the effect’s for the same resource, the **Deny will always win**.
- The least privilege model is a common security suggest to **only grant the access level required to perform the necessary function, and no more**.
- **IAM is Universal**: it does not apply to regions at this time.
- **The Root Account**: this is the account created when you first set up your AWS account and it has complete admin access. Secure it as soon as possible and **do not** use it to log in day to day.
- **New Users**: no permissions when first created.
- **Access key ID and secret key are not the same as username and pass.**
- You only get to **view these one** (Access and secret key).
- **Always set up password rotations**.
- **IAM Federation**: you can combine your existing user with AWS. (LDAP)
- **Identity Federation**: uses SAML standard, which is Active Directory.
### Usage
#### Resources

**Resources** are the entities that you create in AWS. This can include thing’s like an S3 bucket, an S3 Object, or a DynamoDB tables. All resources in AWS are represented by something called an **ARN** or **Amazon Resource Name**. You’ve probably seen one of these identifiers before, they look a little like this: `arn:aws:s3:::test-website-awssimplified`.
#### Actions

**Actions** are the operations that users attempt to perform on resources. For example, if I created a lambda function, I may want to update its configuration. In order to do that, I need to use an API called `lambda:UpdateFunctionConfiguration`.
#### Policy / Policy Document

The heart of AWS IAM is the **Policy**. IAM policies refer specific JSON documents that define user permissions to access a resource. In other words, authorization to perform an **Action** is determined by whether or not the user has the appropriate **Policy Document** with associated permissions.
### Control

#### Groups

IAM **groups** are simply a collection of AWS Users. They are an important organizational toolkit to help you assign similar permissions to a collection of users at once. Using groups, you can associate users added to the group with a default IAM policy. Check out the documentation [here](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_groups.html).
#### Roles

**Roles** are similar to users in the sense that we can attach IAM policies to them. However, unlike Users, Roles are meant to **grant short term access to resources**. In other words, if I want to grant short term access to a user to provide a certain job function, say as an administrator, I may grant them the ability to **assume** a specific role. In doing so, the user will have all permissions defined under the assumed rule’s policy document. Roles can be used by many different users and at once if necessary.

Roles can be assumed by both users and other AWS services. For instance, when creating a Lambda function, we need to specify a **Role** that the Lambda function will use. If our function needs to access DynamoDB for example, I will need to add DynamoDB specific **Actions** to the role’s policy document.

#### Trust Relationships

**Trust Relationships** are not so much a core concept of IAM, but they are a source of problems that many developers run into which is why I think they’re worth discussing.

**Trust Relationships** allow us to create **Roles** that enable users from a DIFFERENT AWS account to temporarily gain access to it. For instance, consider an example like we have one account with a DynamoDB table, and a user from a different account wanting to get access to it.

- [Enabling IAM principal access to your cluster](https://docs.aws.amazon.com/eks/latest/userguide/add-user-role.html)
- [Cross-Account Access in the AWS Management Console](https://aws.amazon.com/es/blogs/aws/new-cross-account-access-in-the-aws-management-console/)

## Infrastructure as Code

- [[Cloud Formation]]

## Container orchestration

- [[ECS |Elastic Container Service]]
- [[EKS |Elastic Kubernetes Service]]
- [[ECR |Elastic Container Registry]]

## CLI

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

# EBS

- General Purpose SSD (gp2) Volumes: General Purpose SSD (gp2) volumes are the most common volume type. They were designed to be a **cost-effective storage** option for a wide variety of workloads. Gp2 volumes cover system volumes, dev and test environments, and various low-latency apps. They have a decent IOPS (starting from 100 and going all the way to 16000 IOPS) and a maximum throughput of 250MiB/s. You can combine multiple EBS volume types in a RAID to achieve even higher performance on a single instance.

- Provisioned IOPS SSD (io1) Volumes: Provisioned IOPS SSD (io1) EBS volume types are a special type of volume created to fulfill the needs of **very intensive I/O workloads** that require very high throughput. They are useful for cases which are latency-sensitive, like **large database** workloads (e.g., MySQL, Cassandra, MongoDB, and Oracle) and critical business applications that need the kind of sustained performance gp2 volumes can’t achieve.

- Throughput Optimized HDD (st1) Volumes: Throughput Optimized HDD (st1) volumes are a type of volume that offers **low-cost storage** while fulfilling the need for sequential workloads that require more throughput than IOPS. When working with **data warehouses**, log processing, **ETL** (extract, transform, load) or AWS EMR, this is a volume type to look into. Keep in mind that this volume type **cannot be used as a boot volume**.

### What is an IOPS AWS?

IOPS is an acronym for **input/output operations per second** and is a popular performance metric used to distinguish one storage type from another. Similar to device makers, AWS associates IOPS values to the volume component backing the storage option. Provisioned IOPS are an AWS EBS volume type designed to deliver predictable, high-level performance for I/O intensive workloads such as database applications.

IOPS usage can be simply calculated by knowing the total read and write throughputs (ops) of your disk divided by the time in seconds within that period.

> **_NOTE:_** IOPS Usage = (Total Read + Write Throughputs) / Time (in Seconds)

Example: IOPS = ( 15000 + 100 ) / 300 = 

# ACM

AWS Certificate Manager ([ACM](https://aws.amazon.com/certificate-manager/))

- [Managing TLS keys and certs in Istio using Amazon’s ACM](https://faun.pub/managing-tls-keys-and-certs-in-istio-using-amazons-acm-8ff9a0b99033)

# EKS

aws eks --region eu-west-1 update-kubeconfig --profile name