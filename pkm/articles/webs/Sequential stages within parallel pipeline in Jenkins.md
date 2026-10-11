---
title:  Sequential stages within parallel pipeline in Jenkins
created: Friday 11th April 2025 23:03
aliases: 
tags:
  - jenkins
  - ci-cd
  - devops
---
- https://stackoverflow.com/questions/59688963/sequential-stages-within-parallel-pipeline-in-jenkins
- Type: qa
- Source: Stack Overflow · asked Jan 2020

---

# TL;DR

In a dynamic pipeline, build each parallel branch as a closure that opens a named `stage` containing nested stages, then run them with `parallel`.

# Summary

With a scripted pipeline, serial stages inside parallel branches collapse into one visual stage. The accepted answer switches to a **declarative pipeline with a `script` block** that fills a map of closures returned from a helper function `prepareStage(name)`; each closure wraps `stage(name) { stage("1") {...} stage("2") {...} }`, and a final `parallel stepsToRun` executes them. This gives a visible sub-stage per branch.

# Key takeaways

1. **Create branches dynamically** in a loop and store them in a map for `parallel`.
2. **Return closures from a function** so each branch has its own stage structure.
3. **Nest stages** inside the branch stage to show serial steps in the UI.
4. **Allocate nodes explicitly**: the stages in the example have no node, so wrap them in `node {}` when needed.
5. **Restart limits**: Blue Ocean can restart only top-level stages, not these nested ones.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[Jenkins]] | Scripted vs declarative pipelines |
| [[Jenkins pipeline Syntax]] | `parallel`, nested `stages` rules |
| Groovy closures | Used to build branches dynamically |

# When to use

1. When generating **parallel branches from a list** and wanting serial sub-stages in the UI.
2. When the **scripted version shows only one stage** per branch.
3. When a static `parallel` block is too limited.

# Caveats

- One accepted answer, no mention of Jenkins version beyond 2020-era behaviour.

---
[[Jenkins]] [[DevOps]]
[[Jenkins pipeline Syntax]]
[[How to run multiple stages on the same node with declarative Jenkins pipeline]]
