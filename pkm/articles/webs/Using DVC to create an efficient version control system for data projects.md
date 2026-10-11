---
title:  Using DVC to create an efficient version control system for data projects
created: Friday 11th April 2025 22:16
aliases: 
tags:
  - dvc
  - mlops
  - ml
---
- https://medium.com/qonto-way/using-dvc-to-create-an-efficient-version-control-system-for-data-projects-96efd94355fe
- Type: tutorial
- Source: Medium (The Qonto Way) · Basile Guerrapin · Jul 2019

---

# TL;DR

[[Dvc]] adds a Git-like layer that versions data files through small pointer files and models a project as **stages** and pipelines tied to the code that produced each result.

# Summary

Training data of several gigabytes cannot live in Git, and keeping zips plus a metrics spreadsheet breaks as projects grow: nobody knows which data produced which result. DVC stores pointers (`.dvc` files with checksums) in Git while the files go to a local cache and a remote such as S3. Each processing step becomes a stage with dependencies, outputs and metrics; `dvc status` shows what is stale, and `git checkout` plus `dvc checkout` restores any past state. The example is VAT detection from receipts.

# Key takeaways

1. **Track data with pointers**: `dvc add data/file` ignores the file in Git and creates a small versioned `.dvc` pointer.
2. **Define stages**: `dvc run -d <deps> -o <outputs> -M <metrics> -f stage.dvc python script.py`.
3. **Chain stages into pipelines** where one stage's outputs feed the next; `dvc status` flags what to rerun.
4. **Restore any state** with `git checkout <rev>` then `dvc checkout`.
5. **Sync with remote storage** (S3 here) via `dvc push` and `dvc pull`; run `dvc gc` to prune the cache only after pushing.
6. **Mind the limit**: DVC does not see code changes unless code is a dependency, so the team used a Makefile and `--ignore-build-cache` rather than `dvc repro`.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[Dvc]] | Data and pipeline versioning |
| [[Git]] | Versions the pointers and stage files |
| [[S3]] | Remote storage for data and models |
| Makefile | Wraps long `dvc run` commands |

# When to use

1. When **versioning large data files** alongside code.
2. When you need to **reproduce an old experiment** with matching data.
3. When comparing DVC with `git-lfs`.

# Caveats

- 2019 CLI (`dvc run`) has since been replaced by `dvc stage add` and `dvc.yaml`; check current docs.

---
[[Dvc]] [[Git]] [[MLOps]] [[S3]]
[[Continuous Delivery for Machine Learning]]
[[A CD4ML Example Setup on AWS S3, GitLab with DVC]]
[[Git Custom References for ML Experiments]]
