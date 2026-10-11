---
title:  A Practical Introduction to Grid Search, Random Search, and Bayes Search
created: Saturday 12th April 2025 12:57
aliases: 
tags:
  - ml
  - hyperparameter-tuning
  - python
---
- https://archive.ph/5vmrX
- Type: tutorial
- Source: Towards Data Science · B. Chen · Sep 2021

---

# TL;DR

Three scikit-learn ways to tune an SVC: exhaustive `GridSearchCV`, sampled `RandomizedSearchCV` and Bayesian `BayesSearchCV` from scikit-optimize.

# Summary

Hyperparameters are set before training; here `C` (regularisation) and `gamma` (RBF kernel width) of a Support Vector Classifier are tuned on the breast-cancer dataset with a 70/30 split. Grid search tries every combination from a dictionary; random search samples a fixed number of draws from distributions; Bayes search uses past results to pick the next candidates. All three expose `best_params_` and `best_estimator_`.

# Key takeaways

1. **Grid search**: `GridSearchCV(SVC(), param_grid, refit=True)`; cost grows with the number of combinations (here 25).
2. **Random search**: `RandomizedSearchCV` with distributions (`uniform`, `loguniform`) and `n_iter=20`.
3. **Bayes search**: `BayesSearchCV` with `Real(...)` search spaces and `cv=5`, modelling the space to converge faster.
4. **Pick by budget**: use grid for small spaces, random or Bayes as the number of combinations grows.
5. **Evaluate afterwards** with predictions, classification report and confusion matrix on the test set.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[Machine Learning]] | Hyperparameter tuning |
| [[Python]] | scikit-learn and scikit-optimize |
| [[Algorithms for Hyper-Parameter Optimization]] | Paper behind the Bayesian approach |
| [[Tuning Hyperparameters with Reproducible Experiments]] | Same ideas run as DVC experiments |

# When to use

1. When you need **copy-paste examples** of the three search strategies.
2. When choosing a search method by **budget**.
3. When pairing tuning with experiment tracking.

# Caveats

- Archive copy of a member-only post; the conclusion was truncated and the results were not compared quantitatively.

---
[[Machine Learning]] [[Python]]
[[Tuning Hyperparameters with Reproducible Experiments]]
[[Algorithms for Hyper-Parameter Optimization]]
