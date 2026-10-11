---
title:  Continue Jenkins pipeline past failed stage
created: Friday 11th April 2025 23:02
aliases: 
tags:
  - jenkins
  - ci-cd
  - devops
---
- https://stackoverflow.com/questions/40600621/continue-jenkins-pipeline-past-failed-stage
- Type: qa
- Source: Stack Overflow · asked Nov 2016 · top answer 145 votes (Jul 2019)

---

# TL;DR

Wrap the risky step in `catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE')` so the stage shows red but the pipeline keeps running.

# Summary

The asker wanted a series of quick-check stages to all run even when one fails, with the failed stage still shown as failed in the stage view. `try/catch` keeps the pipeline going but marks the stage green. The accepted answer uses the built-in `catchError` step with separate `buildResult` and `stageResult` (available since *Pipeline: Basic Steps* 2.16, May 2019); other answers use scripted flags, `post { always }`, `failFast false` in parallel stages, or shell `|| true`.

# Key takeaways

1. **Best option today**: `catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') { sh 'exit 1' }` inside `steps`; works in declarative and scripted pipelines.
2. **Choose the overall result** freely: with `buildResult: 'FAILURE', stageResult: 'FAILURE'` the build continues and fails at the end, avoiding false positives.
3. **Older scripted approach**: `try { stage(...) } catch(e) { build_ok = false }`, then set `currentBuild.result` after the last stage.
4. **Loops**: wrap each iteration in `catchError`, or record a flag and call `catchError` once to mark the stage and build `UNSTABLE`.
5. **Alternatives**: `post { always { ... } }` for cleanup, `|| true` in shell steps, or parallel stages with `failFast false`.
6. **Caveat on try/catch**: it can turn a failing stage green, hiding the failure in the stage view.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[Jenkins]] | Declarative and scripted pipelines |
| [[Jenkins pipeline Syntax]] | `post`, stages and parallel reference |
| [[Jenkins running multiple steps]] | `post` conditions and wrappers |

# When to use

1. When a pipeline should **run all checks even if one fails**.
2. When you need a failed stage to **show red without aborting** the rest.
3. When choosing between `catchError`, `try/catch` and `post`.

# Caveats

- Answers span 2016-2024; make sure your Jenkins and plugin versions support `catchError` with `stageResult`.

---
[[Jenkins]] [[DevOps]]
[[Jenkins pipeline Syntax]]
[[Jenkins running multiple steps]]
[[How to run multiple stages on the same node with declarative Jenkins pipeline]]
