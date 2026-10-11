---
title:  Git Custom References for ML Experiments
created: Friday 11th April 2025 22:16
aliases: 
tags:
  - dvc
  - mlops
  - git
---
- https://datachain.ai/blog/experiment-refs
- Type: article
- Source: DVC blog · Peter Rowlands · Apr 2021 (updated Nov 2025; now at dvc.org)

---

# TL;DR

DVC stores each experiment as a commit under a custom Git reference (`refs/exps/...`), so you get experiment tracking without hundreds of branches.

# Summary

[[Dvc]] 2.0's `dvc exp run` reproduces the pipeline, commits parameters and outputs, and saves the commit under a generated name such as `exp-26220`. The ref lives in the `refs/exps` namespace, a normal [[Git]] commit that works with `git diff` by SHA but stays invisible to `checkout`, branch lists and most GUIs. Experiments stay local until shared explicitly.

# Key takeaways

1. **Why not branches**: hundreds of daily experiments would clutter a repository.
2. **Custom refs** are ordinary commits stored as `refs/exps/<base-prefix>/<base-sha>/<name>`.
3. **One command** replaces `dvc repro`, `git add` and `git commit`: `dvc exp run`.
4. **Share explicitly** with `dvc exp push` and `dvc exp pull`; promote with `dvc exp branch`.
5. **Inspect**: `dvc exp show --sha`, `dvc metrics diff`, `dvc diff`.
6. **Trade-off**: experiments are hidden from standard Git tooling, so team members must use DVC commands.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[Dvc]] | Experiment management |
| [[Git]] | Custom references under `refs/` |
| [[MLOps]] | Experiment tracking practice |

# When to use

1. When explaining **how DVC experiments are stored in Git**.
2. When deciding **branches vs custom refs** for experiment tracking.
3. When sharing experiments between machines.

# Caveats

- The page does not discuss `dvc exp apply` and lists no explicit drawbacks; the trade-offs above are inferred.

---
[[Dvc]] [[Git]] [[MLOps]]
[[Tuning Hyperparameters with Reproducible Experiments]]
[[Oh Shit, Git]]
