---
title: MacOS
created: Wednesday 4th June 2025 10:01
aliases: 
tags:
---

| Tool/Framework                                                    | Description                                                               |
| ----------------------------------------------------------------- | ------------------------------------------------------------------------- |
| [Stats](https://github.com/exelban/stats)                         | System monitor in your menu bar                                           |
| [Pearcleaner](https://github.com/alienator88/Pearcleaner)         | A free, source-available and fair-code licensed mac app cleaner           |
| [Numi](https://github.com/nikolaeu/numi)                          | Beautiful calculator app for macOS, Linux & Windows                       |
| [bottom](https://github.com/ClementTsang/bottom)                  | Yet another cross-platform graphical process/system monitor               |
| [yabai](https://github.com/koekeishiya/yabai)                     | A tiling window manager for macOS based on binary space partitioning      |
| [Amethyst](https://github.com/ianyh/Amethyst)                     | Automatic tiling window manager for macOS à la xmonad                     |
| [skhd](https://github.com/koekeishiya/skhd)                       | Simple hotkey daemon for macOS                                            |
| [Cap](https://github.com/CapSoftware/Cap)                         | Open source Loom alternative. Beautiful, shareable screen recordings      |
| [Alt-tab-macos](https://github.com/lwouis/alt-tab-macos)          | Windows alt-tab on macOS                                                  |
| [Containerization](https://github.com/apple/containerization)     | Containerization is a Swift package for running Linux containers on macOS |
| [osx-us-altgr-intl](https://github.com/xv0x7c0/osx-us-altgr-intl) | US keymap with altgr-intl variant for OSX                                 |
| [BackgroundMusic](https://github.com/kyleneideck/BackgroundMusic) | macOS audio utility: automatically pause your music, set individual apps                                                                          |

# Commands

## Network

### Lsof

```bash
sudo lsof -i -P | grep LISTEN | grep :$PORT
```

# Startup Apps

Open Finder, click **Go > Go to Folder**. Enter `/Library/LaunchAgents` or `/Library/LaunchDaemons`.

# Schedule

```bash
pmset -g sched
# add schedule on weekdays
sudo pmset repeat wakeorpoweron MTWRF 08:00:00
sudo pmset repeat poweron MTWRF 07:50:00
# remove schedule
sudo pmset repeat cancel
```

# Brew

Homebrew is a free and open-source software package management system that simplifies the installation of software on Apple's operating system, macOS, as well as Linux. The name is intended to suggest the idea of building software on the Mac depending on the user's taste.

- Install a package

```bash
brew install python@3.11
```

- Create a New `Brewfile` for having all the dependencies
```bash
brew bundle dump --no-vscode -f
```

```
brew uninstall package
brew autoremove
```
# Colima

- https://itnext.io/migrating-to-colima-from-docker-desktop-to-run-minikube-k8s-cluster-on-macos-1d491c2d75ee

```bash
colima start
# or
colima start --cpu 6 --memory 6 --disk 20
```

- display space disk

```
colima ssh -- df -h /usr/local
```

- start as a service in background
```bash
brew services start colima
```

## K8s

- Deploying K8s with more than 1 Node with Colima
- https://techexpertise.medium.com/multi-node-minikube-k8s-deployment-on-m1-mac-with-colima-and-nfs-pv-762bcf08ac08
# Raycast

- [Ente Auth](https://github.com/raycast/extensions/blob/53900f5e62a35bd4422c86e8ad3c9c1dad67bd1b/extensions/ente-auth/README.md) extension
# Ente

```bash
brew install ente-cli
ente account add
# type auth
ente account list
```