---
title:  Customizing your VS code setup
created: Monday 21st April 2025 20:55
aliases: 
tags:
  - vscode
  - tools
---
- https://medium.com/@uiuxwithdiptanshu/vs-code-ricing-customizing-vs-code-at-the-next-level-6a516910dcb6
- Type: tutorial
- Source: Medium · Diptanshu Mahish · Aug 2024

---

# TL;DR

"Rice" [[VSCode]] by exploiting that it is an Electron web app: a theme and icon pack, a large `settings.json` and a custom CSS file give it a minimal, personal UI.

# Summary

Because VS Code is built on Electron, its interface can be restyled with CSS (and JavaScript if needed). The tutorial picks the React Theme and Material Icon Theme, pastes a long user settings JSON that removes visual noise, and loads a CSS file that restyles the command palette, tabs, title bar and welcome watermark with the Geist Mono font. A palette command applies the CSS, and DevTools reveal class names for further tweaks.

# Key takeaways

1. **Start with theme and icons**: React Theme plus Material Icon Theme.
2. **Edit user settings (JSON)** via the command palette: Prettier formatting on save, hidden minimap, status bar and breadcrumbs, side bar on the right, wide line height, `Geist Mono, JetBrains Mono, Fira Code` fonts and ligatures.
3. **Style with CSS**: restyle `.quick-input-widget` (command palette), `.tab`, `.monaco-list-row`, title bar and the home watermark with `!important` overrides.
4. **Apply the CSS** with a command-palette action; dismiss the warning that VS Code shows after modification.
5. **Iterate** by opening Developer Tools, selecting an element and targeting its class in your CSS.
6. **No JavaScript changes** are needed for the look shown.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[VSCode]] | Editor being customised (Electron) |
| [[Tools]] | Themes and fonts used |
| [[Windows]] | The author's target platform |

# When to use

1. When you want a **personalised VS Code UI** beyond themes.
2. When you need the **CSS selectors** for the palette, tabs and title bar.
3. When looking for a sensible starter `settings.json`.

# Caveats

- Modifying VS Code's own CSS shows a "corrupt installation" style warning and may need reapplying after editor updates; the extension used to inject the CSS is shown only in screenshots.

---
[[VSCode]] [[Tools]]
