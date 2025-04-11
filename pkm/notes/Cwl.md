---
title:  Cwl
created: Friday 20th October 2023 09:26
aliases: 
tags: 
---
Common Workflow Language ([CWL](https://www.commonwl.org/)) is an open standard for describing how to run command line tools and connect them to create workflows.

Tools and workflows described using CWL are portable across a variety of platforms that support the CWL standards. Using CWL, it is easy to scale complex data analysis and machine learning workflows from a single developer's laptop up to massively parallel cluster, cloud and high performance computing environments.

A standard for sharing and reusing workflows can provide a solution to describing portable,re-usable workflows while also being [[Workflow Orchestration]] and vendor-neutral. Although workflows are very popular (see our list of [existing workflow systems](https://s.apache.org/existing-workflow-systems)), prior to the CWL standards every workflow system was incompatible with every other.

| Tool                                                                 | Description                                             |
| -------------------------------------------------------------------- | ------------------------------------------------------- |
| [cwl-tool](https://github.com/common-workflow-language/cwltool)      | Common Workflow Language reference implementation       |
| [Cwl-Airflow](https://github.com/Barski-lab/cwl-airflow/tree/master) | Python package to extend Airflow functionality with CWL |

# Articles/Talks

- [SciDAP: Airflow and CWL-powered bioinformatics platform](https://airflowsummit.org/sessions/2021/scidap/)