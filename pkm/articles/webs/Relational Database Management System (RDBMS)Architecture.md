---
title:  Relational Database Management System (RDBMS)Architecture
created: Friday 11th April 2025 20:29
aliases: 
tags:
  - db
  - sql
  - architecture
---
- https://medium.com/thedevproject/relational-database-management-system-rdbms-architecture-1-1ba5e64b190a
- Type: article
- Source: The Dev Project (Medium) · JIN · Jul 2022, part 1 (read through an archive copy)

---

# TL;DR

A relational database has five main components: client communication manager, process manager, **relational query processor**, **transactional storage manager** and shared utilities; this part covers the first three.

# Summary

Based on the *Architecture of a Database System* paper (Hellerstein, Stonebraker, Hamilton) from the Red Book. A client connects through a protocol such as JDBC, ODBC or TCP; the process model allocates a DBMS worker (a process, thread or pooled worker) and **admission control** rejects invalid or excessive requests. The query processor then parses and authorises the SQL, rewrites it, optimises it into a plan and executes it with an iterator-based engine.

# Key takeaways

1. **Five components**: client communication manager, process manager, relational query processor, transactional storage manager, shared components.
2. **Client models**: two-tier (client-database), three-tier and four-tier (adding web and application servers).
3. **Process models**: process or thread per worker, or pools multiplexing workers (Oracle, SQL Server).
4. **Admission control** protects the system from overload and unauthorised access.
5. **Query pipeline**: parse and authorise, rewrite (views, constants, predicates), optimise, execute. DML (SELECT/INSERT/UPDATE/DELETE) vs DDL (CREATE) queries.
6. **Optimizer** chooses access paths (table or index scan), join order and join type (nested loop, hash, merge); Selinger-style search reduces the plan space.
7. **Executor**: most engines use the **iterator model**, where each operator pulls from the next; it suits single-threaded execution but not parallelism.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[RDBMS]] | Subject of the article |
| [[SQL]] | Query language processed by the pipeline |
| [[Databases]] | General context |
| [[PostgreSQL]] | Example of a DBMS with this architecture |
| [[Concepts of Database Architecture]] | Tier-oriented companion |

# When to use

1. When you need the **internal pipeline of a SQL query** (parse, rewrite, optimise, execute).
2. When comparing **process-per-connection and thread-pool models**.
3. When studying why indexes and join choices matter for performance.

# Caveats

- Part 1 only: the transactional storage manager is not covered, and the text is a condensed summary with many external links.

---
[[RDBMS]] [[Databases]] [[SQL]] [[PostgreSQL]]
[[Concepts of Database Architecture]]
[[Do we really need a specialized vector database]]
