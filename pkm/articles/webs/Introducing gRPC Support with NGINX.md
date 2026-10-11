---
title:  Introducing gRPC Support with NGINX
created: Friday 11th April 2025 23:59
aliases: 
tags:
  - grpc
  - nginx
  - networking
---
- https://blog.nginx.org/blog/nginx-1-13-10-grpc
- Type: article
- Source: NGINX blog · Owen Garrett · Mar 2018

---

# TL;DR

NGINX 1.13.10 can terminate, inspect and route [[gRPC]] calls natively with `grpc_pass`, so the usual HTTP controls (TLS, rate limits, load balancing, logging) now apply to gRPC services.

# Summary

Before this release NGINX could only proxy gRPC as opaque TCP. gRPC rides on HTTP/2: each call is an HTTP POST with a Protocol Buffers body and the status code travels in the trailers. With the new support NGINX listens on `http2` (cleartext) or `ssl http2`, forwards with `grpc_pass grpc://` or `grpcs://`, routes by `/package.Service` path, and balances across an `upstream` group. Failed upstreams can return a gRPC-compliant "unavailable" error.

# Key takeaways

1. **Listen with HTTP/2**: `listen ... http2` for cleartext, `listen ... ssl http2` for TLS; a cleartext port cannot serve HTTP/1.x and HTTP/2 together.
2. **Proxy with `grpc_pass`** (`grpc://` or `grpcs://` for TLS to the backend).
3. **Route by service path** with `location /package.Service`, and keep a catch-all `location /` for websites and REST on the same endpoint.
4. **Load balance** by pointing `grpc_pass` at an `upstream` (round robin, least connections); passive health checks drop failing servers.
5. **Return proper errors**: `error_page 502` to a location that answers gRPC status 14.
6. **Build requirement**: compile with `http_ssl` and `http_v2` modules if building from source.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[gRPC]] | RPC protocol over HTTP/2 being proxied |
| NGINX | Reverse proxy and load balancer gaining gRPC support |
| HTTP/2, Protocol Buffers | Transport and message format |

# When to use

1. When **putting NGINX in front of gRPC services** (TLS termination, routing, balancing).
2. When you need the **directives** `grpc_pass`, `grpcs://` and the HTTP/2 listen options.

# Caveats

- Announcement of the initial release (2018); later NGINX versions added more gRPC directives.

---
[[gRPC]] [[API]]
[[Transcoding HTTP-JSON to gRPC]]
[[Apache APISIX - Gateway transcode]]
