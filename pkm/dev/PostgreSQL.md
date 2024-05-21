---
title:  PostgresSQL
created: Saturday 29th April 2023 17:19
aliases: 
tags: 
---
PostgreSQL is a powerful, open source object-relational database system that uses and extends the SQL language combined with many features that safely store and scale the most complicated data workloads.

- [Certificate Authentication Recipe for PostgreSQL Docker Containers](https://www.crunchydata.com/blog/ssl-certificate-authentication-postgresql-docker-containers)

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