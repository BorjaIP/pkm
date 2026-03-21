---
title:  Software Design Methodology
created: Saturday 21st March 2026 00:00
aliases:
tags:
---
Software design methodology based on three complementary artifacts that guide development from product vision to technical implementation decisions.

## PRD — Product Requirements Document

The PRD defines **what** will be built and **why**. It captures product goals, use cases, functional and non-functional requirements, and acceptance criteria. It is the starting point for any project and the reference document for aligning all stakeholders.

## ADR — Architecture Decision Records

ADRs document the **architecture decisions** made during development: what was decided, why, what alternatives were considered, and what the consequences are. Each significant decision has its own record, making it possible to understand the historical reasoning behind the system and avoid rehashing already-settled debates.

## System Design

System Design describes **how** the system will be built: components, interfaces, data flows, integration patterns, and technical constraints. It complements the PRD (what) and the ADRs (why) with the technical view of the solution.

## Tools

| Tool | Description |
| ---- | ----------- |
| [plan-cascade](https://github.com/Taoidle/plan-cascade) | AI-powered cascading development framework. Decomposes complex projects into parallel executable tasks with auto-generated PRDs, design docs, and multi-agent collaboration. |
| [planning-with-files](https://github.com/OthmanAdi/planning-with-files) | Claude Code skill that implements persistent markdown-based planning using a three-file pattern (task_plan.md, findings.md, progress.md) to maintain structured task tracking across context resets. |
