---
title:  How to run multiple stages on the same node with declarative Jenkins pipeline
created: Friday 11th April 2025 23:03
aliases: 
tags:
  - jenkins
  - ci-cd
  - devops
---
- https://stackoverflow.com/questions/44870978/how-to-run-multiple-stages-on-the-same-node-with-declarative-jenkins-pipeline
- Type: qa
- Source: Stack Overflow · asked Jul 2017

---

# TL;DR

To keep several declarative stages on the same node, wrap them as **sequential nested stages** under one stage with a single `agent`.

# Summary

The asker used `agent none`, picked a node by label in Stage 1, stored `NODE_NAME` in a global variable and used it as the label for Stage 2, but Stage 2 still landed on a random node: the `agent { label ... }` value is evaluated before the variable is updated. Since Declarative Pipeline 1.3 the supported answer is **Sequential Stages**: put an `agent` on the parent stage and nest `stages { ... }` inside, so all children share the allocated workspace.

# Key takeaways

1. **Do not rely on a variable** set in a script block to choose the next stage's node; it is not reevaluated as expected.
2. **Use sequential stages** (declarative plugin 1.3+): parent `stage` with `agent { docker "..." }` and nested `stages` for build, test and so on.
3. **Mix agents** by grouping: one group of stages per node type (Windows vs Linux) with its own parent agent.
4. **Known limits** from the comments: nesting sequential stages inside a `parallel` stage gave syntax errors for some users, and one workaround was an environment variable set in the first sequential stage.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[Jenkins]] | Declarative pipeline and agents |
| [[Docker]] | Agent images used in the answer |
| [[Jenkins pipeline Syntax]] | Official reference for `stages`, `agent`, `parallel` |

# When to use

1. When two stages **must share a workspace or node**.
2. When you cannot use a global `agent` because groups of stages need different nodes.
3. When choosing between **scripted `node{}` blocks and nested stages**.

# Caveats

- Based on a 2018 plugin release; check current Jenkins documentation for nested and parallel constraints.

---
[[Jenkins]] [[DevOps]] [[Docker]]
[[Jenkins pipeline Syntax]]
[[Sequential stages within parallel pipeline in Jenkins]]
