---
title:  Design Patterns
created: Saturday 12th April 2025 00:31
aliases: 
tags: 
---
**Design patterns** are reusable solutions to common problems that occur during software design and development. They represent best practices evolved over time by experienced software practitioners to solve recurring design challenges.

Key characteristics of design patterns:

- **Proven Solutions**: They capture solutions that have been refined over time through practical experience.
- **Abstraction**: They address design problems at a level higher than specific code implementations.
- **Template**: They provide a template for solving problems rather than finished designs to be copied.
- **Context-Specific**: They define situations where they are applicable and explain consequences of their use.
- **Language-Independent**: While their implementation may vary, the core concepts apply across programming languages.
# Categories

## Creational Patterns

Focus on object creation mechanisms, providing flexibility in what gets created, how it's created, and who creates it:

- **Singleton**: Ensures a class has only one instance and provides global access
- **Factory Method**: Creates objects without specifying the exact class
- **Abstract Factory**: Creates families of related objects
- **Builder**: Separates complex object construction from its representation
- **Prototype**: Creates new objects by copying existing ones
## Structural Patterns

Deal with the composition of classes or objects to form larger structures:

- **Adapter**: Converts one interface to another
- **Bridge**: Separates abstraction from implementation
- **Composite**: Composes objects into tree structures
- **Decorator**: Adds responsibilities to objects dynamically
- **Façade**: Provides a simplified interface to a complex subsystem
- **Flyweight**: Minimizes memory usage by sharing common parts of objects
- **Proxy**: Provides a surrogate for another object
## Behavioral Patterns

Concerned with algorithms, communication between objects, and responsibility assignment:

- **Chain of Responsibility**: Passes requests along a chain of handlers
- **Command**: Encapsulates a request as an object
- **Iterator**: Accesses elements sequentially without exposing underlying representation
- **Mediator**: Reduces dependencies between objects
- **Memento**: Captures and restores an object's internal state
- **Observer**: Defines a one-to-many dependency between objects
- **State**: Allows an object to alter its behavior when its state changes
- **Strategy**: Defines a family of algorithms and makes them interchangeable
- **Template Method**: Defines the skeleton of an algorithm, deferring some steps to subclasses
- **Visitor**: Separates algorithms from the objects on which they operate