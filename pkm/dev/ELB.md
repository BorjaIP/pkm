---
title:  ELB
created: Friday 1st March 2024 10:11
aliases: 
tags: 
---
**Elastic Load Balancing** automatically distributes your incoming traffic across multiple targets, such as EC2 instances, containers, and IP addresses, in one or more Availability Zones. It monitors the health of its registered targets, and routes traffic only to the healthy targets. Elastic Load Balancing scales your load balancer capacity automatically in response to changes in incoming traffic.

## Application Load Balancer (ALB)

- Use Layer 7
- ﻿**Listeners**: A listener checks for connection requests from clients, using the protocol and port you configure.
- **Rules**: Determine how the load balancer routes requests to its registered targets. Each rule consists of a priority, one or more actions, and one or more conditions.
- ﻿**Limitations**: Application Load Balancers only support **HTTP** and **HTTPS**.
- **HTTPS**: To use an HTTPS listener, you must deploy at least one **SSL/TLS server certificate** on your load balancer. The load balancer uses a server certificate to terminate the frontend connection and then decrypt requests from clients before sending them to the targets.
- You can enable **sticky sessions** for redirect to the same AWS service.

## Network Load Balancer (NLB)

- Use Layer 4
- ﻿Use where you need extreme performance.
- Other use cases are where you need protocols not supported by Application Load Balancers.
- Network Load Balancers can **decrypt traffic**, but you will need to install the certificate on the load balancer.

## Gateway Load Balancer (GLB)

- Use Layer 3

## Classic Load Balancer (CLB)

- Use Layer 4/7
- Troubleshoot the application. Is it the web server or database server?
- Need the IPv4 address of your end user? Look for the **X- Forwarded-For** header.
