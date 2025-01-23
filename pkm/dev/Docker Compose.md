---
title:  Docker Compose
created: Sunday 23rd April 2023 17:29
aliases: 
tags: 
---
**Docker Compose** is a tool for defining and running multi-container [[Docker]] applications. Key features:

- Uses YAML files to configure application services
- Allows defining multiple containers in a single file
- Simplifies complex application deployment
- Manages container networking and volume mounting
- Enables easy scaling and environment-specific configurations

Example use case: A web application with separate containers for frontend, backend, and database, all defined and orchestrated through a single `docker-compose.yml` file.

Typical workflow involves creating a configuration file and running `docker-compose up` to start the entire application stack.

- [Docker-compose deployment - RapidMainer Documentation](https://docs.rapidminer.com/latest/deployment/docker-compose/#public_url)
- [Using YAML Anchors and X Properties in Docker Compose](https://nickjanetakis.com/blog/docker-tip-82-using-yaml-anchors-and-x-properties-in-docker-compose)
- [Compose Bridge](<- https://docs.docker.com/compose/bridge/usage/>) - Compose Bridge supplies an out-of-the box transformation for your Compose configuration file in [[Kubernetes]] files.
## Tips

- Example for create a good `docker-compose.yaml`.

```yaml
version: '3.8'
services:

  postgres:
    image: postgres:14.4
    container_name: postgres
    restart: on-failure:2
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data
    environment:
      - POSTGRES_USER=admin
      - POSTGRES_PASSWORD=password
      - POSTGRES_MULTIPLE_DATABASES=keycloak
    networks:
      - example
    healthcheck:
      test: [ "CMD", "pg_isready" ]
      interval: 30s
      timeout: 20s
      retries: 3

  keycloak:
    image: jboss/keycloak:16.1.1
    container_name: keycloak
    restart: on-failure:2
    ports:
      - "8070:8080"
    depends_on:
      - postgres
    environment:
      - KEYCLOAK_USER=admin
      - KEYCLOAK_PASSWORD=admin
      - DB_VENDOR=postgres
      - DB_ADDR=postgres
      - DB_DATABASE=keycloak
      - DB_USER=keycloak
      - DB_PASSWORD=keycloak
    networks:
      - example

networks:
  example:

volumes:
  pgdata:
```

- Build with and env file.

```bash
docker-compose build --build-args $(cat envfile)
```