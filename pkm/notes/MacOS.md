---
title: MacOS
created: Wednesday 4th June 2025 10:01
aliases: 
tags:
---
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

```bash
colima start
# or
colima start --cpu 6 --memory 6 --disk 20
```

- start as a service in background
```bash
brew services start colima
```

## K8s

- Deploying K8s with more than 1 Node with Colima
- https://techexpertise.medium.com/multi-node-minikube-k8s-deployment-on-m1-mac-with-colima-and-nfs-pv-762bcf08ac08
