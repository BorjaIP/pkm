---
title:  DynamoDB
created: Thursday 29th February 2024 16:57
aliases: 
tags: 
---
**DynamoDB** is a fully managed **NoSQL** database service that provides fast and predictable performance with seamless scalability. DynamoDB lets you offload the administrative burdens of operating and scaling a distributed database so that you don't have to worry about hardware provisioning, setup and configuration, replication, software patching, or cluster scaling. DynamoDB also offers encryption at rest, which eliminates the operational burden and complexity involved in protecting sensitive data.

- Used SSD for storage.
- Spread across 3 geographically distinct data centers.

- Read types:
	- **Eventually**: consistency across all **copies of data is usually reached within a second**. Best read performance.
	- **Strongly**: a strongly consistent read **returns a result that reflects all writes** that received a successful response prior to the read.
## DynamoDB Transactions

![[acid.png]]

- Useful for ACID requirements.
- Provides ACID for 1 or more tables within a single AWS account and region.
- **All-or-nothing** transactions.

- Use cases:
	- Processing financial transactions.
	- Fulfilling and managing orders.
	- Building multiplayer game engines.
	- Coordinating actions across distributed components and services.
## Recovery

Point-in-Time Recovery (PITR)

- Protect against accidental writes or deletes
- Restore to any point in the las **35 days**
- Incremental backups
- Not enabled by default
- Lasted restorable **5 min** in the past