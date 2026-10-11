---
title:  Oh Shit, Git
created: Friday 11th April 2025 22:47
aliases: 
tags:
  - git
---
- https://ohshitgit.com/
- Type: reference
- Source: ohshitgit.com

---

# TL;DR

A problem-first cookbook of [[Git]] recoveries: find the symptom, copy the commands that undo it.

# What it covers

Git's own docs are hard to search when you do not know the term, so the guide is organized by mistake. The safety net is `git reflog`; rewriting history (amend, reset) is only safe for unpushed commits, while pushed commits should be undone with `git revert`. The tone is deliberately blunt and humorous, and the author notes the commands come from experience rather than exhaustive coverage.

# Key takeaways

1. **Undo almost anything** with `git reflog` to find the state before the mistake, then `git reset HEAD@{index}`.
2. **Fix the last commit** with `git commit --amend --no-edit` (content) or `git commit --amend` (message), only if unpushed.
3. **Move a commit to a new branch**: `git branch new-branch`, `git reset HEAD~ --hard`, `git checkout new-branch`.
4. **Move a commit to the right branch**: `git reset HEAD~ --soft`, `git stash`, switch branch, `git stash pop`, commit (or `git cherry-pick`).
5. **Undo an older commit** with `git revert <hash>`, and restore one file with `git checkout <hash> -- path`.
6. **Empty `git diff` after edits** means the changes are staged: use `git diff --staged`.
7. **Nuclear option**: `git fetch origin`, `git reset --hard origin/master`, `git clean -d --force`; destructive and irreversible.

# When to use

1. When you **committed to the wrong branch** or with the wrong message.
2. When you need to **recover lost work** after a bad reset or merge.
3. When deciding between `reset` and `revert` for shared history.

---
[[Git]] [[DevOps]]
