---
title: Transcoding HTTP-JSON to gRPC
created: Saturday 12th April 2025 00:00
aliases: 
tags:
  - grpc
  - api-gateway
  - api
---
- https://cloud.google.com/endpoints/docs/grpc/transcoding
- Type: reference
- Source: Google Cloud Endpoints documentation

---

# TL;DR

Annotate each RPC with `google.api.http` so Cloud Endpoints' proxy (ESP) maps REST-style HTTP/JSON requests onto [[gRPC]] methods.

# What it covers

Transcoding is on by default (`POST GRPC_SERVICE_FULL_NAME/METHOD_NAME`), but explicit mappings give a cleaner HTTP interface. The page defines the annotation syntax, field mapping rules, the descriptor needed for deployment and the usual errors.

# Key takeaways

1. **Annotate in the proto**: `option (google.api.http) = { get: "/v1/shelves/{shelf}" };` (also `post`, with `body`).
2. **Path captures fill request fields**: `{shelf}` is shorthand for `{shelf=*}`.
3. **`body: "field"`** sends the JSON body into one field; **`body: "*"`** maps all fields not bound by the path.
4. **Design resource-oriented APIs** with List, Get, Create, Update and Delete; custom methods are harder to map.
5. **Build a descriptor**: `protoc --include_imports --include_source_info --descriptor_set_out`, with the googleapis clone for `annotations.proto`, then `gcloud endpoints services deploy`.
6. **YAML alternative**: rules under `http.rules` (not supported by ESPv2).
7. **Avoid errors**: do not remap the default POST path (duplicate pattern), send valid field values only, and pass a single descriptor to `gcloud`.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[gRPC]] | Backend protocol |
| [[API]] | Resource-oriented REST surface |
| ESP / ESPv2 | Extensible Service Proxy that does the translation |
| `google.api.http` | Annotation that defines the mapping |

# When to use

1. When **adding a REST/JSON interface** to a gRPC service on Google Cloud.
2. When you need examples of **path, query and body mapping**.
3. When comparing with gateway-side transcoding in [[Apache APISIX - Gateway transcode]].

# Caveats

- Tied to Cloud Endpoints (ESP); ports and flags differ between ESPv1 and ESPv2.

---
[[gRPC]] [[API]]
[[Apache APISIX - Gateway transcode]]
[[Introducing gRPC Support with NGINX]]
