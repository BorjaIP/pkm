---
title:  Aurora
created: Thursday 29th February 2024 16:52
aliases: 
tags: 
---

**Amazon Aurora** (Aurora) is a fully managed relational database engine that's **compatible with MySQL and PostgreSQL**. You already know how MySQL and PostgreSQL combine the speed and reliability of high-end commercial databases with the simplicity and cost-effectiveness of open-source databases. The code, tools, and applications you use today with your existing MySQL and PostgreSQL databases can be used with Aurora. With some workloads, Aurora can deliver up to five times the throughput of MySQL and up to three times the throughput of PostgreSQL without requiring changes to most of your existing applications.

- 2 copies in each AZ with 3 minimum AZs = 6 copies of your data
- You can share Aurora snapshots with other AWS accounts
- 3 types of replicas available
- Aurora has **automated backups** turned by default
- Useful for **serverless DB scenarios**.