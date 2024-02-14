---
title:  grpc
created: Tuesday 20th June 2023 19:36
aliases: 
tags: 
---
In [gRPC](https://github.com/grpc/grpc), a client application can directly call a method on a server application on a different machine as if it were a local object, making it easier for you to create distributed applications and services. As in many RPC systems, gRPC is based around the idea of defining a service, specifying the methods that can be called remotely with their parameters and return types. On the server side, the server implements this interface and runs a gRPC server to handle client calls. On the client side, the client has a stub (referred to as just a client in some languages) that provides the same methods as the server.

![[grpc.svg]]


- [gRPC-Gateway](https://github.com/grpc-ecosystem/grpc-gateway) - The gRPC-Gateway is a plugin of the Google protocol buffers compiler [protoc](https://github.com/protocolbuffers/protobuf). It reads protobuf service definitions and generates a reverse-proxy server which translates a RESTful HTTP API into gRPC.
- [Deploying Machine Learning Models with PyTorch, gRPC and asyncio](https://github.com/roboflow/deploy-models-with-grpc-pytorch-asyncio)

### Transcode to REST

- [gRPC Support with NGINX](https://www.nginx.com/blog/nginx-1-13-10-grpc/)
- [Transcoding HTTP/JSON to gRPC](https://cloud.google.com/endpoints/docs/grpc/transcoding)
- [Gateway transcode](https://apisix.apache.org/docs/apisix/plugins/grpc-transcode/)
- [Load Balancing grpc with Nginx](https://dev.to/techschoolguru/load-balancing-grpc-service-with-nginx-3fio)