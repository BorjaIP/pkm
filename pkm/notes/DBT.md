---
title:  DBT
created: Thursday 16th October 2025 13:27
aliases: 
tags: 
---

# Structure

dbt_project.yml --> models-path: where sql logic

/dbt_packages --> where all deps live
/seeds --> for static files, a csv file for reference 
/snapshots --> for snapshots
/tests --> small tests like if a value is greater than 0
/tests/generic --> generic unit tests

- run: Models only.
- build: Models + seeds + snapshots + tests, all in graph order.

```bash
# install dependencies
dbt deps
# list all resources
dbt list
# will display the first 5 rows from the query result
dbt show
#  rebuild your model on every run
dbt run --models my_model --full-refresh
```

# Macros

```bash
# Test macro union
dbt compile --inline "{{ dbt_utils.union_relations(relations=[source('name', 'table')]) }}"
```