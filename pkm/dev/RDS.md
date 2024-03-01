---
title:  RDS
created: Thursday 29th February 2024 16:44
aliases: 
tags: 
---
**Relational Database Service** (RDS) is a web service that makes it easier to set up, operate, and scale a relational database in the AWS Cloud. It provides cost-efficient, resizable capacity for an industry-standard relational database and manages common database administration tasks.

- [Pricing comparing instances](https://instances.vantage.sh/rds/?region=eu-west-1)
- **RDS** Instance Types based on prices [Prices](https://aws.amazon.com/rds/instance-types/).
- Table Types: SQL Server, MySQL, PostgrSQL, etc..
- RDS is for OLTP workloads
- Not suitable for OLAP workloads

## Multi-Az

- An exact copy of your production database in another AZ.
- Used for **disaster recovery**.
- In the event of failure, RDS will automatically fail over to the standby instance.
## Replicas

- A read-only copy of your primary database in the same AZ.
- Used to increase or **scale read** performance.
- Great for read-heavy workloads and rakes the load oof your primary database.