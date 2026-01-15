---
title:  Airflow
created: Tuesday 20th June 2023 19:48
aliases: 
tags: ETL
---
[Apache Airflow](https://airflow.apache.org/docs/apache-airflow/stable/) (or simply Airflow) is a platform to programmatically author, schedule, and monitor workflows.

When workflows are defined as code, they become more maintainable, versionable, testable, and collaborative.

Use Airflow to author workflows as directed acyclic graphs (DAGs) of tasks. The Airflow scheduler executes your tasks on an array of workers while following the specified dependencies. Rich command line utilities make performing complex surgeries on DAGs a snap. The rich user interface makes it easy to visualize pipelines running in production, monitor progress, and troubleshoot issues when needed.

- [A journey to Airflow on Kubernetes](https://towardsdatascience.com/a-journey-to-airflow-on-kubernetes-472df467f556)
- [Airflow Helm Chart (User Community)](https://github.com/airflow-helm/charts/tree/main/charts/airflow)
- [Guide to Airflow on Kubernetes](https://github.com/rolanddb/airflow-on-kubernetes)

### Fernet-key

```bash
python3 -c "from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())"
```

# CLI

```bash
# list users
airflow users list
# add role
airflow users add-role -e name@email -r Admin
airflow users list -o json 
airflow roles list -o json
```

# Achitecture

- **Workers** - Execute the assigned tasks
- **Scheduler** - Responsible for adding the necessary tasks to the queue
- **Web server** - HTTP Server provides access to DAG/task status information 
- **Database** - Contains information about the status of tasks, DAGs, Variables, connections, etc.
- **Celery** - Queue mechanism
	- **Broker** - Stores commands for execution
	- **Result backend** - Stores status of completed commands

## Logs

```bash
ssh airflow-scheduler
tail -f /opt/airflow/logs/scheduler/latest/path/file.py.log
```