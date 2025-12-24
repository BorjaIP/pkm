---
title: RDBMS
created: Tuesday 21st May 2024 15:46
aliases:
  - rdb
tags:
---
RDBMS stands for Relational Database Management System used to maintain a relational database. RDBMS is the basis for all modern database systems:

- MySQL
- Microsoft SQL Server
- Oracle
- [[PostgreSQL]]
- [[AlloyDB]]

| Tool/Framework                                        | Description                         |
| ----------------------------------------------------- | ----------------------------------- |
| [Atlas](https://github.com/ariga/atlas)               | Manage your database schema as code |
| [Cloudbeaver](https://github.com/dbeaver/cloudbeaver) | Cloud Database Manager              |
# Components

## Table

Physical storage of data in the database.

## View

- **Definition:** A _saved SQL query_ that presents data from one or more tables.
- **Data:** Not stored — computed every time you query it.
- **Use case:**
    - Simplify complex queries.
    - Provide a secure "window" to data (row/column filtering).
## Materialized View (MV)

- **Definition:** Like a view, but the results are _physically stored_ (precomputed).
- **Data:** Stored, and **refreshed** periodically or on demand.
- **Use case:**
    - Speed up queries (especially aggregations).
    - Cache expensive joins/aggregations.

## Temporary Table

- **Definition:** A table that exists only during the session (or transaction).
- **Data:** Stored temporarily, dropped when session ends.
- **Use case:** Staging data in ETL pipelines.

## CTE (Common Table Expression)

- **Definition:** A _query-defined temporary view_ available only in the query.
- **Data:** Not stored, in-memory only while query executes.
- **Use case:** Break down complex queries for readability.

```sql
WITH cte_name AS (
    SELECT ...
    FROM ...
    WHERE ...
)
SELECT *
FROM cte_name
WHERE ...
```

## External Table

- **Definition:** A table that points to data stored _outside the database_ (e.g., in S3, GCS, Azure Blob).
- **Data:** Not ingested, but queried directly.
- **Use case:** Query raw files (Parquet, JSON, CSV) without loading them first.

## Aggregated Holistic Table

An **aggregated holistic table** is a **single, denormalized, summary table** that combines _multiple sources_, _multiple metrics_, or _multiple granularities_ into one unified dataset designed for **fast analytics**, **business reporting**, or **machine-learning feature extraction**.

Think of it as a _“one-stop table”_ that gives a **complete (holistic) view** of an entity or process (customer, product, transaction, session, etc.). It usually contains both:

1. **Raw identifiers / keys**
    
2. **Aggregated metrics** computed from many underlying detailed tables
    
3. **Features** derived from other dimensions or history
    
4. **Flags, scores, segments**, etc.
    

### 🔍 Why “Aggregated”?

Because it already contains **precomputed metrics** such as:

- counts
- sums
- averages
- last event timestamps
- rolling windows (7d, 30d, 90d)
- engagement scores
- revenue totals

These are **pre-aggregated** to avoid repeatedly calculating them at query time.

### 🔍 Why “Holistic”?

Because it includes **all relevant information about a business entity** in one place, instead of forcing reports or ML pipelines to JOIN dozens of tables.

It tries to answer “everything about X” in one dataset.

Examples:

- _Holistic customer table_ → everything about a customer
- _Holistic product table_ → everything about a product
- _Holistic order table_ → everything about a transaction
### 🧱 Typical Structure of an Aggregated Holistic Table

 Example: _Customer 360 Holistic Table_

Columns might include:
 
 **Identifiers**
 
- customer_id
- first_seen_date
- segment

 **Aggregated metrics**

- total_orders
- total_revenue
- avg_order_value
- last_30d_orders
- last_7d_sessions
- churn_score

 **Derived attributes**

- preferred_channel
- customer_lifetime_group
- engagement_score
 
 **Flags**

- is_active
- is_vip
- is_churned

 **Metadata**

- snapshot_date
- model_version

This table is typically refreshed daily and consumed downstream.

# SQLite

```bash
# show tables
.tables
# show squemas
.schema
```
# ORM

ORM produces a structured map that reveals the relationships between objects and tables, or data, without getting into the minutiae of the [data structure](https://builtin.com/data-science/data-structures). Objects are essentially converted into digestible parts that a database can store for future retrieval. ORM connects object-oriented programming languages ([[Python]]) or applications with a relational database, communicating any changes made to an object to the database, which then alters the data accordingly.   

Because ORM monitors and handles interface changes, developers don’t need to worry about editing code on a constant basis. This technique also enables teams to understand how a database is structured without needing to review the code, making it easier to glean insights from complex states and codes generated by object-oriented programs.
# OLTP

OLTP (online transaction processing) is a class of software programs capable of supporting **transaction** -oriented applications. In computing, a **transaction is a sequence of discrete information exchanges that are treated as a unit**. Many everyday acts involve OLTP, including online banking, online shopping and even in-store shopping when the point of sale (POS) terminal is tied to inventory management software.

OLTP systems were originally designed to handle only operational data. They process various different kinds of queries and are geared toward surface-level transactions. Today, some **in-memory databases** are able to process memory-optimized tables of transaction data stored in system memory instead of having to pull them from disk storage. This approach is called in-memory OLTP.
## Transaction

In computing, a **transaction is a set of related tasks treated as a single action**. Together the tasks form a logical unit of work in which all of them must succeed or none of them can succeed. If some tasks succeed but at least one fails, then all successful tasks are reversed, returning the system to its original state before the transaction was initiated (roll back).

A common example of a transaction is a customer's purchase through an e-commerce site. After selecting a product and entering the necessary information, the customer confirms the final sale by clicking OK or taking some other step to conclude the process. This causes the application to launch a sales transaction, which includes multiple steps, such as confirming the product's availability, validating the credit card, initiating the shipping process and placing the order with the warehouse.
## ACID

Transactions in a relational database typically adhere to the following four **ACID properties**:

- **Atomicity**. All operations within the transaction are treated as a single unit. **This means that all operations must succeed for any changes to be committed to the database**. If any operation fails, no changes are committed, and the entire transaction is rolled back.
- **Consistency**. The data remains in a consistent state throughout the transaction's execution and is left in a consistent statement at the end of the transaction. The transaction should make no changes that violate any constraints defined on the data.
- **Isolation**. Each transaction is isolated from all other transactions running concurrently against the database. A transaction should not interfere with another transaction or affect it in any way. The degree to which transactions are isolated from each other is determined by the applicable isolation levels.
- **Durability**. Any changes made by a transaction after it has been committed are persisted to the database and cannot be undone by outside circumstances, such as a hardware failure or power outage.
# OLAP

![[oltp_vs_olap.png]]