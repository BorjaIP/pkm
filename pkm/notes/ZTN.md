---
title:  ZTN
created: Friday 11th April 2025 23:24
aliases: 
tags: 
---
**Zero trust network** is a security paradigm that does not grant implicit trust to users, devices, and services, and continuously verifies their identity and authorization to access resources.

- _A Zero Trust Network (ZTN) environment where continuous authentication and authorization are enforced between microservices across multicloud_

**Zero Trust Architecture** (ZTA) is a cybersecurity model that requires strict identity verification for every user and device attempting to access resources, regardless of their location. It operates on the principle of "never trust, always verify," ensuring that no one is automatically trusted, even if they are inside the network perimeter.

[[Istio]] simplifies enforcing a ZTN environment for microservices across the cloud. Inspired by [Gartner Zero Trust Network Access](https://www.gartner.com/smarterwithgartner/new-to-zero-trust-security-start-here), we have outlined four pillars of zero trust network that can be implemented by Istio.

![[ztn.png]]

