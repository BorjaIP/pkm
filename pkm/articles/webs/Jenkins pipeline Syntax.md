---
title:  Jenkins pipeline Syntax
created: Friday 11th April 2025 23:01
aliases: 
tags:
  - jenkins
  - ci-cd
  - devops
---
- https://www.jenkins.io/doc/book/pipeline/syntax/
- Type: reference
- Source: jenkins.io official documentation

---

# TL;DR

Official reference for [[Jenkins]] **Declarative** and **Scripted** pipeline syntax: sections, directives, `post` conditions, `when` rules, parallel/matrix stages and the traps that go with them.

# What it covers

**Declarative** is the structured, opinionated form wrapped in `pipeline { }`; **Scripted** is Groovy running top to bottom inside `node { }`. Both share the same engine and steps. A declarative pipeline is built from sections (`agent`, `stages`, `steps`, `post`) and directives (`environment`, `options`, `parameters`, `triggers`, `tools`, `input`, `when`).

# Key takeaways

1. **Pick the agent** per pipeline or stage: `any`, `none`, `label`, `docker`, `dockerfile` or `kubernetes`.
2. **Inject secrets safely** with `environment { KEY = credentials('id') }`; username/password credentials also expose `_USR` and `_PSW`.
3. **React to results in `post`**: `always`, `changed`, `fixed`, `regression`, `success`, `failure`, `unstable`, `aborted`, `cleanup` (runs last).
4. **Gate stages with `when`**: `branch`, `tag`, `changeset`, `environment`, `expression`, combined with `not`, `allOf`, `anyOf`; add `beforeAgent true` to skip agent allocation.
5. **Compose stages**: nested sequential `stages`, `parallel` (with `failFast true`), or `matrix` with `axes` and `excludes`; a stage holds exactly one of `steps`, `stages`, `parallel` or `matrix`, and parallel cannot nest in parallel.
6. **Schedule with `triggers`**: `cron('H */4 * * 1-5')`; use `H` to spread load.
7. **Avoid the classic traps**: no semicolons, a top-level `timeout` excludes agent wait time but a stage one includes it, and a `when` expression returning the string `"false"` is still true.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[Jenkins]] | The CI server whose Pipeline DSL is described |
| Declarative vs Scripted | The two syntaxes, same engine |
| Shared Libraries | Place for large `script {}` blocks because of the declarative size limit |
| [[Docker]] | Agent option for containerised builds |

# When to use

1. When **writing or debugging a Jenkinsfile** and you need the exact directive or option name.
2. When deciding **declarative vs scripted** for a pipeline.
3. When running **parallel or sequential stages**, see the specific questions in [[Sequential stages within parallel pipeline in Jenkins]].

# Caveats

- Reference, not a tutorial: examples are minimal and the page has no dedicated security section.

---
[[Jenkins]] [[DevOps]] [[Docker]]
[[Sequential stages within parallel pipeline in Jenkins]]
[[How to run multiple stages on the same node with declarative Jenkins pipeline]]
[[Continue Jenkins pipeline past failed stage]]
[[How do I schedule jobs in Jenkins]]
