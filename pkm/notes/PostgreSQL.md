---
title:  PostgresSQL
created: Saturday 29th April 2023 17:19
aliases: 
tags: 
---
PostgreSQL is a powerful, open source object-relational database system that uses and extends the SQL language combined with many features that safely store and scale the most complicated data workloads.

| Tool                                                    | Description                                                                                             |
| ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| [Timescaledb](https://github.com/timescale/timescaledb) | A time-series database for high-performance real-time analytics packaged as a Postgres extension        |
| [PGVector](https://github.com/pgvector/pgvector)        | Open-source vector similarity search ([[VDB]]) for PostgreSQL.                                          |
| [Repmgr](https://github.com/EnterpriseDB/repmgr)        | A lightweight replication manager for PostgreSQL                                                        |
| [Neon](https://github.com/neondatabase/neon)            | Neon: Serverless Postgres. We separated storage and compute to offer autoscaling                        |
| [Paradedb](https://github.com/paradedb/paradedb)        | Postgres for Search and Analytics                                                                       |
| [Pgai](https://github.com/timescale/pgai)               | A suite of tools to develop RAG, semantic search, and other AI applications more easily with PostgreSQL |
# Articles/Talks

- [Certificate Authentication Recipe for PostgreSQL Docker Containers](https://www.crunchydata.com/blog/ssl-certificate-authentication-postgresql-docker-containers)
- [PostgreSQL High Availability and automatic failover using repmgr](https://medium.com/@joao_o/postgresql-high-availability-and-automatic-failover-using-repmgr-5f505dc6913a)
- [Pgpool]([https://github.com/bitnami/containers/blob/main/bitnami/pgpool/README.md](https://www.pgpool.net/docs/pgpool-II-4.2.7/en/html/example-kubernetes.html))
# WAL (Write Ahead Log)

WAL logs are the files in which various transactions are stored. These logs are written to disk before the changes are made to the database.

- Data recovery.
- Triggers for mutations.

![[postgres_wal.png]]

![[db_mutations.png]]


# Triggers

### Example data2Json 

```sql
CREATE OR REPLACE FUNCTION public.my_json_converter(
	application varchar(64),
	category varchar(64),
	customer_reference_id varchar(8),
	exception_reason varchar(128),
	event_timestamp timestamp
)
  RETURNS json 
  LANGUAGE PLPGSQL
  AS
$$
declare
	json_payload varchar(300);
BEGIN
	select json_build_object(
	'application', application ,
	'category', category ,
	'customer_reference_id', customer_reference_id ,
	'exception_reason', exception_reason ,
	'event_timestamp', event_timestamp 
	) into json_payload;

	RETURN json_payload;
END;
$$
```

- See if the trigger is apply correct

```sql
SELECT tgname, tgrelid::regclass, tgfoid::regprocedure
FROM pg_trigger
WHERE NOT tgisinternal;
```
### AWS Lambda

```sql
# install
CREATE EXTENSION IF NOT EXISTS aws_lambda CASCADE;
```

- Execute a lambda when 
```sql
CREATE OR REPLACE FUNCTION public.my_db_trigger_function()
  RETURNS TRIGGER 
  LANGUAGE PLPGSQL
  AS
$$
declare
	my_record record;
BEGIN
	raise notice 'Start my_db_trigger_function';
	SELECT * FROM aws_lambda.invoke(aws_commons.create_lambda_function_arn('arn:aws:lambda:eu-west-1: :function:my_rds_triggered_topic_writer')
,(select public.my_json_converter(
								new.application ,
								new.category ,
								new.customer_reference_id ,
								new.exception_reason ,
								new.event_timestamp 
	)
)
  , 'Event'
) into my_record;
	raise notice 'End my_db_trigger_function';						
	RETURN NEW;
END;
$$
```
# PSQL

|Command|Description|
|---|---|
|`\c <database>`|Connect to a specific database|
|`\password <user>`|Change password for a specific user|
|`\l`|List all databases|
|`\d+`|Show detailed information about various database objects|
|`\dt`|List all tables in the current database|
|`\du`|List all users|
|`\df`|List all functions|
|`\dv`|List all views|
|`\dn`|List all schemas|
|`\dp`|List all permissions|
|`\di`|List all indexes|
|`\ds`|List all sequences|
|`\d+`|Show detailed information about various database objects|
|`\q`|Quit psql|
|`\x`|Toggle expanded output|

- Access DB
```bash
	psql -h localhost -U admin -W 
psql -d postgres -U webadmin -W
# AWS
psql -U user -h hostname.rds.amazonaws.com -p 5432 database
```

- List all DB

```sql
\l
\c database;
\dn
```

- List tables

```sql
\dt 
```

- Exit

```sql
\q
```

## Backup and Restore

| Command                           | Description                    |
| --------------------------------- | ------------------------------ |
| `pg_dump <database> > backup.sql` | Backup a database to a file    |
| `psql <database> < backup.sql`    | Restore a database from a file |
# SQL

- Delete table in DB

```sql
DELETE FROM tablename;
```

- Access DB

```sql
REVOKE CONNECT ON DATABASE nova FROM PUBLIC;
GRANT  CONNECT ON DATABASE nova  TO user;
```

- Access Schema

```sql
REVOKE ALL     ON SCHEMA public FROM PUBLIC;
GRANT  USAGE   ON SCHEMA public  TO user;
```

- Access Tables

```sql
REVOKE ALL ON ALL TABLES IN SCHEMA public FROM PUBLIC ;
GRANT SELECT   ON ALL TABLES IN SCHEMA public TO read_only ;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO read_write ;
GRANT ALL ON ALL TABLES IN SCHEMA public TO admin ;
```

- Create

```sql
CREATE USER user WITH PASSWORD 'pass';
CREATE DATABASE database;
GRANT ALL PRIVILEGES ON DATABASE database TO user;
GRANT ALL PRIVILEGES ON SCHEMA database TO user;
```

- Delete all connections

```sql
SELECT
	pg_terminate_backend(pg_stat_activity.pid)
FROM
	pg_stat_activity
WHERE
	pg_stat_activity.datname = 'database_name'
	AND pid <> pg_backend_pid();
```

- Create sample data

```sql
CREATE TABLE products (
	product_name char(50),
	price int
)

INSERT INTO products (product_name, price)
VALUES
('Desktop Computer',800),
('Laptop',1200),
('Tablet',200),
('Monitor',350),
('Printer',150)
SELECT * FROM products
```

- List enums

```sql
select enum_range(null::my_enum);
```

