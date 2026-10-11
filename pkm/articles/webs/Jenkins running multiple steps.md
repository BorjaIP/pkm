---
title:  Jenkins running multiple steps
created: Friday 11th April 2025 23:00
aliases: 
tags:
  - jenkins
  - ci-cd
  - devops
---
- https://www.jenkins.io/doc/pipeline/tour/running-multiple-steps/#running-multiple-steps
- Type: tutorial
- Source: jenkins.io Pipeline tour

---

# TL;DR

A [[Jenkins]] stage can run many steps in order: `sh`/`bat` for commands, `retry` and `timeout` as wrappers, and `post` for cleanup and notifications.

# Summary

A pipeline is made of steps; each succeeds and moves on, or fails and fails the pipeline. Use `sh` on Linux/macOS and `bat` on Windows, with triple quotes for multiline scripts. Wrapper steps change behaviour: `retry(n)` repeats and `timeout(time, unit)` stops runaway steps, and they nest. The `post` section runs outcome-based actions, with a scripted equivalent based on `try`/`catch`/`finally`.

# Key takeaways

1. **Command steps**: `sh '...'` (Unix) and `bat '...'` (Windows); `'''` for multiline.
2. **Fail fast**: any failed step fails the pipeline.
3. **Wrap flaky steps**: `timeout(time: 3, unit: 'MINUTES') { retry(5) { sh './flakey-deploy.sh' } }` caps total retry time.
4. **Post conditions**: `always`, `success`, `failure`, `unstable`, `changed`.
5. **Scripted equivalent** uses `try/catch/finally` and `currentBuild.result`; rethrow the exception after reporting.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[Jenkins]] | Pipeline steps and wrappers |
| [[Jenkins pipeline Syntax]] | Full reference for the same constructs |
| [[Linux]] | `sh` runs shell commands on Unix agents |

# When to use

1. When writing your **first multi-step stage**.
2. When you need **retry plus timeout** for a flaky step.
3. When translating `post` conditions to scripted pipelines.

# Caveats

- Introductory tour page; deeper options are in the syntax reference.

---
[[Jenkins]] [[DevOps]]
[[Jenkins pipeline Syntax]]
[[How do I schedule jobs in Jenkins]]
[[Jenkins SSH Pipeline Steps]]
