---
title:  Software Architecture
created: Saturday 12th April 2025 00:26
aliases: 
tags: 
---
**Software architecture** is the high-level structure of a software system that defines its organization, components, relationships, and principles governing its design and evolution. It serves as the blueprint for both the system and the project developing it, addressing both functional and quality requirements.

Key aspects of software architecture include:

- **Structure**: The organization of software components, their interfaces, and the relationships between them.
- **Architectural Decisions**: Fundamental choices that shape the system and constrain its design, often reflecting trade-offs between competing quality attributes.
- **Quality Attributes**: Non-functional requirements like scalability, performance, security, maintainability, and reliability that the architecture must support.
- **Patterns and Styles**: Reusable architectural approaches (like microservices, layered, event-driven) that solve recurring design problems.
- **Documentation**: Models, diagrams, and textual descriptions that communicate the architecture to stakeholders.
- **Governance**: Processes ensuring that implementation adheres to architectural principles and constraints.

| Tool                                    | Description                                                                  |
| --------------------------------------- | ---------------------------------------------------------------------------- |
| [Archi](https://www.archimatetool.com/) | The Open Source modelling toolkit for creating ArchiMate models and sketches |

- [[The C4 model for visualizing software architecture]]
- [[The Software Architecture Handbook]]
- [[What Is Event-Driven Microservices Architecture]]
- [[What is SAGA Pattern in Microservice Architecture - Which Problem does it solve]]
- [[System Design Interview Basics - Difference Between API Gateway and Load Balancer]]

# Architecture Patterns

- **Client-Server**: Separates functionality between service providers (servers) and service requesters (clients).
- **Layered Architecture**: Organizes components into horizontal layers, each providing services to the layer above it.
- **Microservices**: Structures an application as a collection of loosely coupled, independently deployable services.
- **Event-Driven Architecture**: Components produce and consume events asynchronously.
- **Model-View-Controller (MVC)**: Separates application concerns into data model, presentation view, and control logic.
- **Service-Oriented Architecture (SOA)**: Organizes functionality as a set of interoperable services.
- **Serverless Architecture**: Runs application functions in stateless containers managed by a third party

# Layered Architecture

# Microservices
## MVC

- **Model**: The backend that contains all the data logic
- **View**: The frontend or graphical user interface (GUI)
- **Controller**: The brains of the application that controls how data is displayed

![[mvc.png]]

![[mvc_diagram.png]]

