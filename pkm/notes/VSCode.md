---
title:  VSCode
created: Sunday 23rd April 2023 16:47
aliases: 
tags: tools
---

- [VS Code - You don't need that extension](https://www.roboleary.net/vscode/2020/08/05/dont-need-extensions.html)
- [VS Code Performance – How to Optimize Visual Studio Code and Choose the "Best" Extensions](https://www.freecodecamp.org/news/optimize-vscode-performance-best-extensions/)
- [Keyboard Driven VSCode](https://dev.to/waylonwalker/keyboard-driven-vscode-n0a)
- [All VSCode Shortcuts for MacOS, Linux and Windows](https://vscode-shortcuts.com/)
- [Emoji Cheat Sheet](https://www.webfx.com/tools/emoji-cheat-sheet/)

## Devcontainers

- [Deployment Containers](https://containers.dev/)
## Shortcuts

ctrl+shift+p    Execute         
ctrl+p      Search files by name
ctrl+e      Search files
ctrl+r      Abrir folder o workspace
ctrl+alt+o  Open Workspace
ctrl+0      Go to File explorer
alt+n       Create new file
alt+shift+n Create new folder

ctrl+g      Go to line

alt+up/down Move line
ctrl+alt+up/down    Multiple cursors

```bash
# Commands
# Ctrl + Shift + P 
Developer: Show Running Extensions
Developer: Startup Performance

# Show status os VSCode
code --status
```

- Add Youtube videos.

[![Blinking LEDs](http://img.youtube.com/vi/XAMVzS13HY0/0.jpg)](http://www.youtube.com/watch?v=XAMVzS13HY0 "Blinking LEDs")

- Add a Pomodoro Iframe.
    <!-- <iframe width="560" height="700" src="https://pomofocus.io/"></iframe> -->

## Remove lines

Reemplaza todo lo de dentro del la expresion regular (por ejemplo poner "" a todas las lineas)
Tienes que darle al * para ver qué expresiones regulares aplicas, para saltos de lína una `/n` o `^/n`


Find (Ctrl+F):

```bash
^(.+)$
```

Replace:

```bash
'$1'
```
