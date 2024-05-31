---
title:  Winget
created: Sunday 23rd April 2023 15:02
aliases: 
tags: 
---
[Winget](https://github.com/microsoft/winget-cli) is the Windows Package Manager. This project includes a CLI, PowerShell modules, and a COM (Component Object Model) API .

- List of [packages](https://winget.run/) for install in [[Windows]].
# Windows preferred packages

```bash
# install git
winget install -e --id Git.Git
# udpate all packages
winget upgrade -h --all
# install packages for custom terminal
winget install -e --id stedolan.jq Git.git libjpeg-turbo.libjpeg-turbo.GCC Neovim.Neovim gerardog.gsudo
winget install -e --id junegunn.fzf
# install apps
winget install -e --id Microsoft.VisualStudioCode Kubernetes.kubectl MuhammedKalkan.OpenLens Hashicorp.Vagrant dbeaver.dbeaver Starship.Starship KeePassXCTeam.KeePassXC ShareX.ShareX
# optional packages
winget install -e --id Mobatek.MobaXterm
```

# Folders
## Temporary folder

- Remove all unnecessary downloaders `C:\Users\%USERNAME%\AppData\Local\Temp\WinGet`