---
title: API
created: Saturday 29th April 2023 14:59
aliases: 
tags:
---
API stands for **Application Programming Interface**. In the context of APIs, the word Application refers to any software with a distinct function. Interface can be thought of as a contract of service between two applications. This contract defines how the two communicate with each other using requests and responses.

| Tool                                                   | Description                           |
| ------------------------------------------------------ | ------------------------------------- |
| [Hoppscotch](https://github.com/hoppscotch/hoppscotch) | Open source API development ecosystem |

## API REST

- [OpenAPI Specification](https://swagger.io/specification/)
- [[FastAPI]]
- [[gRPC]]

 - PUT means replace the entire resource with given data (so null out fields if they are not provided in the request), while PATCH means replace only specified fields

![[rest_tips.png]]

### Authentication Methods

![[rest_auth.png]]

#### JWKS

A JWKS endpoint is a designated HTTPS endpoint typically exposed at a well-known location on the authorization server (or any server managing the cryptographic keys), such as **_“https://<server_domain>/.well-known/jwks.json”_**.

![[jwks.png]]

## Performance

![[api_performance.png]]