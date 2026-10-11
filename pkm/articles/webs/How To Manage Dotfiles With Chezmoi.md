---
title:  How To Manage Dotfiles With Chezmoi
created: Saturday 12th April 2025 00:04
aliases: 
tags:
  - dotfiles
  - tools
  - git
---
- https://jerrynsh.com/how-to-manage-dotfiles-with-chezmoi/
- Type: tutorial
- Source: jerrynsh.com · Jerry Ng · Feb 2022

---

# TL;DR

**chezmoi** keeps a Git-backed source copy of your dotfiles and applies it to your home directory, replacing hand-made symlinks.

# Summary

Dotfiles like `.zshrc` or `.gitconfig` are easy to lose and slow to rebuild on a new machine. The classic approach is a Git repo plus symlinks; chezmoi instead keeps a source directory at `~/.local/share/chezmoi` where files are stored with a `dot_` prefix, and `chezmoi apply` writes them to `$HOME`. You edit through chezmoi, review with `chezmoi diff`, then commit and push yourself.

# Key takeaways

1. **Install** with a package manager or `sh -c "$(curl -fsLS get.chezmoi.io)"`.
2. **Track a file**: `chezmoi init`, then `chezmoi add ~/.zshrc`.
3. **Edit safely**: `chezmoi edit <file>`, not the home copy.
4. **Preview and apply**: `chezmoi diff`, then `chezmoi apply -v`.
5. **Sync via Git**: `chezmoi cd`, commit and push; on a new machine `chezmoi init --apply <user>`; later `chezmoi update -v`.
6. **Never commit secrets** in plain text, even in a private repo.
7. **Next steps**: templates for per-machine differences and `run_once_` scripts.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[Dotfiles]] | The configuration files being managed |
| [[Git]] | Backing repository and sync |
| [[Terminal]] | Shell configuration use case |

# When to use

1. When **bootstrapping a new machine** with your configs.
2. When replacing a symlink-based dotfiles repo.
3. When you need the core chezmoi command sequence.

# Caveats

- Templates, secrets management and cross-OS differences are only mentioned as advanced topics.

---
[[Dotfiles]] [[Git]] [[Terminal]] [[Tools]]
