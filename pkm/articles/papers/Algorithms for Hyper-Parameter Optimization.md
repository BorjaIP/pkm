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

# Summary

Hyperparameter tuning is a major bottleneck in training high-performing neural networks, typically left to human intuition or grid search. This NeurIPS 2011 paper proposes two **sequential model-based optimization** (SMBO) algorithms — one using a Gaussian process and one using **Tree-structured Parzen Estimators (TPE)** — that outperform random search on deep belief network benchmarks. The key insight is modeling the **conditional structure** of hyperparameter spaces to identify irrelevant dimensions, enabling more efficient exploration. TPE achieves results that surpass previously published **human-tuned configurations** on challenging classification tasks.

# Main points

1. **Random search** is a strong baseline for neural networks but unreliable for deep belief networks.
2. **TPE** models p(x|y) rather than p(y|x), enabling efficient conditional hyperparameter search.
3. **Response surface modeling** identifies and skips irrelevant hyperparameter combinations.
4. Both SMBO methods outperform the best previously reported **human-tuned results** on DBN benchmarks.
5. Scope is limited to **moderate-dimensionality spaces**; very high-dimensional search remains challenging.

# Takeaways

1. **TPE** remains widely used today (it powers Optuna) — understanding its mechanics helps diagnose tuning failures.
2. Modeling hyperparameter **conditional structure**, not just marginals, is key to efficient search.
3. Random search is not naive — it is a **competitive baseline** that should always run before heavier methods.
4. Human-tuned configurations can be **systematically outperformed** with sufficient compute and a surrogate model.
5. The **expected improvement** criterion is a practical proxy for sample-efficient black-box optimization beyond ML.

---
[[Machine Learning]]
[[Deep Learning]]
[[Artificial Intelligence|AI]]
