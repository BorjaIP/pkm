---
title:  Concepts of Database Architecture
created: Friday 11th April 2025 20:26
aliases: 
tags:
  - db
  - architecture
  - sql
---
- https://medium.com/oceanize-geeks/concepts-of-database-architecture-dfdc558a93e4
- Type: article
- Source: Medium (Oceanize Lab Geeks) · Faysal Ahmed · Aug 2017

---

# TL;DR

An introductory tour of DBMS tier architectures (1, 2, 3 and n-tier) followed by database **normalization** (1NF to BCNF).

# Summary

The design of a [[Databases|DBMS]] can be centralised, decentralised or hierarchical, and single- or multi-tier. A 1-tier system keeps interface, middleware and data together; 2-tier is client-server with direct communication; **3-tier** adds an application tier between users and the database and is the most widely used; n-tier splits logic, presentation and data physically. The second half explains normalization to remove redundancy and insertion, update and deletion anomalies.

# Key takeaways

1. **1-tier**: everything in one place, simplest.
2. **2-tier**: client talks directly to the database server.
3. **3-tier**: data tier, application (middle) tier and presentation tier; end users never see the database directly.
4. **n-tier vs MVC**: n-tier layers are physical and linear through the logic tier, MVC is conceptual and triangular; they can be combined (MVC inside the presentation tier).
5. **Normalization** removes redundant data and makes dependencies logical; 1NF needs atomic values and no repeating groups, 2NF needs full functional dependence on the key.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[Databases]] | DBMS architecture context |
| [[RDBMS]] | Relational model and normalization |
| [[SQL]] | Language implied by relational design |
| [[Software Architecture]] | Tiered architecture patterns |

# When to use

1. When recalling the **difference between 2-tier and 3-tier** database architecture.
2. When reviewing **normal forms** before designing tables.
3. When contrasting n-tier with MVC.

# Caveats

- Basic 2017 introduction; the text read stops during 2NF, so 3NF and BCNF are only listed.

---
[[Databases]] [[RDBMS]] [[SQL]] [[Software Architecture]]
[[Relational Database Management System (RDBMS)Architecture]]
[[The Software Architecture Handbook]]
