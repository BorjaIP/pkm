---
title:  Apache APISIX - Gateway transcode
created: Saturday 12th April 2025 00:01
aliases: 
tags:
  - grpc
  - api-gateway
  - networking
---
- https://apisix.apache.org/docs/apisix/plugins/grpc-transcode/
- Type: reference
- Source: Apache APISIX documentation (plugin `grpc-transcode`)

---

# TL;DR

The **grpc-transcode** plugin lets APISIX accept plain HTTP requests, call an upstream [[gRPC]] service from a registered `.proto`, and convert the reply back to HTTP.

# What it covers

Attributes, registration of the proto, route setup and error handling for HTTP-to-gRPC transcoding in the APISIX gateway.

# Key takeaways

1. **Register the proto** through the Admin API (`/apisix/admin/protos/{id}`); for imports, build a `.pb` descriptor with `protoc --include_imports --descriptor_set_out` and upload it base64-encoded.
2. **Enable on a route** with `proto_id`, `service` (for example `echo.EchoService`) and `method`, and set the upstream `scheme` to `grpc`.
3. **Call it with HTTP**: query parameters map to request message fields.
4. **Tune the encoding** with `pb_option` (`enum_as_name`, `int64_as_string`, `auto_default_values`, ...); use `int64_as_string` to avoid precision loss.
5. **Handle errors**: the response carries `grpc-status` and `grpc-message` and a matching HTTP code (for example 503 for status 14); `show_status_in_body` plus `status_detail_type` decode details.
6. **Limits**: `deadline` (ms) and `max_resp_body_size` (default 64 MiB) bound a call.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[Apache]] | APISIX is an Apache project |
| [[gRPC]] | Upstream protocol |
| [[API]] | HTTP/JSON façade over gRPC |
| protoc | Compiles descriptors for the proto resource |

# When to use

1. When exposing a **gRPC backend to HTTP/JSON clients** through APISIX.
2. When you need the **plugin attributes** and the Admin API calls.
3. When comparing with Google's mapping approach in [[Transcoding HTTP-JSON to gRPC]].

# Caveats

- Mapping is by route and query parameters; there is no `google.api.http` annotation support described on this page.

---
[[gRPC]] [[API]] [[Apache]]
[[Transcoding HTTP-JSON to gRPC]]
[[Introducing gRPC Support with NGINX]]
[[An Envoy-Powered, Kubernetes-Native API Gateway]]
