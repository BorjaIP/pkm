---
title:  VPC
created: Friday 1st March 2024 09:49
aliases: 
tags: 
---
With Amazon Virtual Private Cloud (Amazon VPC), you can launch AWS resources in a logically isolated virtual network that you've defined. This virtual network closely resembles a traditional network that you'd operate in your own data center, with the benefits of using the scalable infrastructure of AWS.

![[vpc.png]]

## NAT Gateway

- If you have resources in multiple AZs and share a NAT Gateway, if NAT Gateway AZ is down, resources in others AZs lose internet access. Configure a NAT Gateway per AZs.
- **AWS Wavelength** used for 5G and mobile networks.
## Network ACLs

- **Default Network ACLs**: your VPC automatically comes with a default network ACL, and by default it allows all outbound and inbound traffic.
- **Custom Network ACLs**: you can create custom network ACLs. By default, each custom network ACL denies all inbound and outbound traffic until you add rules.
- **Subnet Associations**: each subnet in your VPC must be associated with a network ACL. If you don't explicitly associate a subnet with a network ACL, the subnet is automatically associated with the default network ACL.
- **Block IP Addresses**: block IP addresses using network ACLs, not security groups.

﻿- 1 ACL = 1 Subnet but 1 Subnet = Multiple ACLs
- Network ACLS contain a numbered list of rules that are evaluated in order, starting with the lowest numbered rule.
- Network ACLs have separate inbound and outbound rules, and each rule can either allow or deny traffic.
- Network ACLs are stateless; responses to allowed inbound traffic are subject to the rules for outbound traffic (and vice versa).
## VPC Endpoints

- Use Case: When you want to connect AWS services without leaving the Amazon internal network
- 2 Types of VPC Endpoints: Interface endpoints and gateway endpoints
- Gateway Endpoints: Support S3 and DynamoDB
## Peering

- Allows you to connect 1 VPC with another via a direct network route using private IP addresses.
- Instances behave as if they were on the same private network.
- You can peer VPCs with other AWS accounts as well as with other VPCs in the same account.
- Peering is in a star configuration (e.g., 1 central VPC peers with 4 others). No transitive peering!
- You can peer between regions.
## PrivateLink

- **AWS PrivateLink** used for tens, hundreds or thousands of customer VPCs.
- Doesn't require VPC peering, no route tables, NAT Gateway, internet gateway, etc
- Requites a NLB on the service VPC and ENI on the customer VPC
## Transit Gateway

- You can use route tables to limit how VPCs talk to one another.
- Works with Direct Connect as well as VPN connections.
- Supports IP multicast (not supported by any other AWS service).
## VPN Hub

- VPN optimization for multiple Regions/AZs.

![[vpn_hub.png]]