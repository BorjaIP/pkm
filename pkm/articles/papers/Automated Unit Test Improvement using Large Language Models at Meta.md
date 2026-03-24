---
title:  Automated Unit Test Improvement using Large Language Models at Meta
created: Wednesday 6th March 2024 18:24
aliases:
tags:
  - llm
  - software-testing
  - code-generation
---
- https://arxiv.org/pdf/2402.09171.pdf
- Source: arxiv

---

# TL;DR

**TestGen-LLM** improves existing human-written unit tests by proposing LLM-generated enhancements that pass a build-and-run validation pipeline, retaining only changes that compile, pass, and measurably increase code coverage.

# Summary

Generating unit test suites from scratch is brittle for production codebases; improving existing tests is more tractable. TestGen-LLM takes a method under test and its current **test suite** as input and uses an LLM to propose improvements — extended coverage, corrected assertions, added edge cases. A **build-and-run validation pipeline** filters out suggestions that fail to compile, fail to pass, or do not increase **code coverage**. Deployed at Meta on real production codebases, the system delivered meaningful coverage gains at scale.

# Key contributions

1. Proposes **TestGen-LLM**, a system that improves existing tests rather than generating suites from scratch, making LLM-assisted testing tractable for production code.
2. Introduces a **build-and-run validation pipeline** that filters LLM suggestions to only those that compile, pass, and measurably increase code coverage.
3. Demonstrates **coverage-gated acceptance** as the mechanism aligning LLM output with engineering quality standards.
4. Shows industrial-scale deployment at **Meta** on real production codebases with measurable coverage gains.

# When to cite

1. When arguing that **improving existing tests** is more tractable than full test generation for production systems.
2. When designing an **automated validation pipeline** for LLM-generated test code to prevent regressions.
3. When justifying **coverage-gated filtering** as a quality gate for LLM-assisted testing.
4. When citing evidence that **LLM-assisted testing scales** to heterogeneous real-world production codebases.

---
[[LLM]]
