---
title: Data Orchestration
created: Monday 4th March 2024 11:51
aliases: 
tags:
  - ETL
---
Data orchestration is an **automated process for bringing data together from multiple sources, standardizing it, and preparing it for data analysis.**

Data orchestration doesn’t require data engineers to write custom scripts but relies on **software that connects storage systems together so data analysis tools can easily access them**.

The terms “[[Workflow Orchestration]]” and “data orchestration” are often used interchangeably, but there are important differences between the two. While both workflow and data orchestration are important for businesses, they serve different purposes. Workflow orchestration is focused on the efficiency of business processes, while data orchestration is focused on the quality and accuracy of data.

The challenge of [[Big Data]] is that it is, well, BIG. It’s so big that it’s impossible to effectively use manual processes to work with it all. That’s where automated data orchestration comes in.

| Tool/Framework                                   | Description                                                                                                                                |
| ------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| [[Airflow]]                                      | A platform to programmatically author, schedule, and monitor workflows                                                                     |
| [Dagster](https://github.com/dagster-io/dagster) | An orchestration platform for the development, production, and observation of data assets                                                  |
| [DBT](https://github.com/dbt-labs/dbt-core)      | DBT enables data analysts and engineers to transform their data using the same practices that software engineers use to build applications |
