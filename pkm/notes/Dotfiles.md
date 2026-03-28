---
title:  Dotfiles
created: Monday 1st May 2023 16:33
aliases: 
tags: 
---
**Dotfiles** are configuration files used to customize the settings of your applications and development environment on a computer. They typically start with a dot (.) in their filename and can be tracked using version control systems like Git to synchronize settings across different devices.

| Tool                                             | Description                                                                  |
| ------------------------------------------------ | ---------------------------------------------------------------------------- |
| [Chezmoi](https://www.chezmoi.io/)               | Manage your dotfiles across multiple diverse machines, securely              |
| [Yadm](https://yadm.io/)                         | Yet Another Dotfiles Manager                                                 |
| [GNU Stow](https://www.gnu.org/software/stow/)   | Symlink farm manager                                                         |
| [Pure](https://github.com/sindresorhus/pure)     | Pretty, minimal and fast ZSH prompt                                          |
| [Starship](https://github.com/starship/starship) | The minimal, blazing-fast, and infinitely customizable prompt for any shell! |
# Shell

## ZSH

The **Z shell** is a Unix shell that can be used as an interactive login shell and as a command interpreter for shell scripting.

- [Oh my ZSH](https://ohmyz.sh/)
## FISH

The **friendly interactive shell** is a Unix shell that attempts to be more interactive and user-friendly than those with a longer history or those formulated as function-compatible replacements for the aforementioned.
# Terminal

- [[Terminal]]
# Chezmoi

- [[How To Manage Dotfiles With Chezmoi]]

```bash
# edit source file
chezmoi edit .config/zsh/.zshrc

# apply changes to your original file
chezmoi -v apply

# see diferences between tracker and local
chezmoi diff

# update new files
chezmoi git -- add .
chezmoi git -- commit -m "Update readme"
chezmoi git -- push
```