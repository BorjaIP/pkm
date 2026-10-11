---
title:  Tuning Hyperparameters with Reproducible Experiments
created: Friday 11th April 2025 22:16
aliases: 
tags:
  - dvc
  - mlops
  - hyperparameter-tuning
  - ml
---
- https://datachain.ai/blog/hyperparam-tuning
- Type: tutorial
- Source: DVC blog · Milecia McGregor · Jul 2021 (updated Nov 2025; now at dvc.org)

---

# TL;DR

Queue many [[Dvc]] experiments from a script, run them in one go and compare results with `dvc exp show` to make grid or random search reproducible.

# Summary

Hyperparameters live in `params.yaml`, so DVC tracks each change together with code and data. The tutorial adds Python scripts that call `dvc exp run --queue --set-param ...` for each configuration: a grid search over 6 values of `n_est` and 6 of `min_split` (36 runs) and a random search of 10 runs with a fixed seed. After `dvc exp run --run-all`, the experiments are compared by ROC-AUC and average precision.

# Key takeaways

1. **Keep parameters in `params.yaml`** so DVC notices changes.
2. **Queue instead of editing files**: `dvc exp run --queue --set-param train.min_split=8`.
3. **Run the queue**: `dvc exp run --run-all`.
4. **Compare**: `dvc exp show --no-timestamp --include-params train.n_est,train.min_split`.
5. **Random search can match grid search** with a similar budget because it covers the range more widely.
6. **Newer DVC (2.25+)** can run grid searches directly via `exp run --set-param`.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[Dvc]] | Experiment queue, params and comparison |
| [[Machine Learning]] | Model tuning workflow |
| [[A Practical Introduction to Grid Search, Random Search, and Bayes Search]] | Conceptual background on the search methods |
| [[Algorithms for Hyper-Parameter Optimization]] | Paper on more advanced optimisation |

# When to use

1. When running **hyperparameter searches reproducibly** with DVC.
2. When you need the **queue and compare commands**.
3. When choosing between grid and random search for a given budget.

# Caveats

- Bayesian optimisation is mentioned but not covered; CLI details have evolved since 2021.

---
[[Dvc]] [[MLOps]] [[Machine Learning]]
[[Git Custom References for ML Experiments]]
[[A Practical Introduction to Grid Search, Random Search, and Bayes Search]]
[[Using DVC to create an efficient version control system for data projects]]
