---
title:  grpc
created: Tuesday 20th June 2023 19:36
aliases: 
tags: 
---
In [gRPC](https://github.com/grpc/grpc), a client application can directly call a method on a server application on a different machine as if it were a local object, making it easier for you to create distributed applications and services. As in many RPC systems, gRPC is based around the idea of defining a service, specifying the methods that can be called remotely with their parameters and return types. On the server side, the server implements this interface and runs a gRPC server to handle client calls. On the client side, the client has a stub (referred to as just a client in some languages) that provides the same methods as the server.

![[grpc.svg]]




| Tool/Framework                       | Description                                    |
| ------------------------------------ | ---------------------------------------------- |
| [ghz](https://github.com/bojand/ghz) | Simple gRPC benchmarking and load testing tool |
# Articles/Talks

- [gRPC-Gateway](https://github.com/grpc-ecosystem/grpc-gateway) - The gRPC-Gateway is a plugin of the Google protocol buffers compiler [protoc](https://github.com/protocolbuffers/protobuf). It reads protobuf service definitions and generates a reverse-proxy server which translates a RESTful HTTP API into gRPC.
- [[Deploying Machine Learning Models with PyTorch, gRPC and asyncio]]
# Transcode to REST

- [[Introducing gRPC Support with NGINX]]
- [[Transcoding HTTP/JSON to gRPC]]
- [[Apache APISIX - Gateway transcode]]
- [[Load balancing gRPC service with Nginx]]