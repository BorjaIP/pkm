---
title:  Algorithms for Hyper-Parameter Optimization
created: Monday 24th April 2023 20:32
aliases:
tags:
  - ml
  - dl
---
- https://papers.nips.cc/paper/2011/file/86e8f7ab32cfd12577bc2619bc635690-Paper.pdf
- Source: neurips

---

# TL;DR

This NeurIPS 2011 paper proposes **Tree-structured Parzen Estimators (TPE)** and a Gaussian-process SMBO algorithm that outperform random search and previously published human-tuned configurations on deep belief network benchmarks.

# Summary

Hyperparameter tuning is a major bottleneck in training high-performing neural networks, typically left to human intuition or grid search. Two **sequential model-based optimization** (SMBO) algorithms are proposed — one using a Gaussian process and one using **Tree-structured Parzen Estimators (TPE)** — that model the conditional structure of hyperparameter spaces to identify irrelevant dimensions. Both outperform random search on deep belief network benchmarks and surpass previously published **human-tuned configurations** on challenging classification tasks.

# Key contributions

1. Proposes **TPE**, which models p(x|y) rather than p(y|x), enabling efficient conditional hyperparameter search.
2. Introduces **response surface modeling** that identifies and skips irrelevant hyperparameter combinations.
3. Demonstrates that SMBO methods outperform the best previously reported **human-tuned results** on DBN benchmarks.
4. Establishes **random search** as a strong baseline that should be run before heavier optimization methods.

# When to cite

1. When introducing **Bayesian hyperparameter optimization** or citing the origin of the TPE algorithm.
2. When arguing that **conditional hyperparameter structure** should be modeled rather than treating all dimensions as independent.
3. When claiming that **automated HPO** can systematically outperform human-tuned configurations.
4. When discussing the **expected improvement** criterion as a sample-efficient black-box optimization objective.

---
[[Machine Learning]]
[[Deep Learning]]
[[Artificial Intelligence|AI]]
