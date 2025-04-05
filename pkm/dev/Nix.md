---
title:  Nix
created: Saturday 5th April 2025 13:09
aliases: 
tags: 
---
**Nix** is a **package manager** and a **build system** that makes software deployments **deterministic**, **reproducible**, and **isolated**. It comes from the **NixOS** ecosystem but can be used on any Unix-like system.

- It uses a **purely functional approach** to package management.
- Every package and build is isolated in its own environment.
- Builds are defined with the **Nix language**, a declarative DSL.

|Component|Description|Usage|
|---|---|---|
|**Nix DSL**|Functional, declarative language to describe packages, configs, environments|Used in `.nix` files to declare builds|
|**nixpkgs**|A huge collection of pre-defined packages and functions|The standard library for Nix|
|**NixOS**|A full Linux distribution built and configured entirely using Nix|Declarative OS configuration|
|**Nix CLI**|The command-line tool to build, install, and manage packages and environments|Used with `nix`, `nix-shell`, `nix-env`, etc.|
# Environments
## 1. Nix expressions are written in `.nix` files. The DSL is:

- **Declarative** (you describe _what_ you want, not _how_ to do it)
- **Functional** (no side effects, immutable data)
- Used to define **packages**, **build environments**, **Docker images**, and more.
## 2. Using **nixpkgs** (The Nix Package Collection)

**nixpkgs** is the official repo of packages, utilities, and functions for Nix. It powers almost everything:

- You can import packages from it in your Nix expressions.
- You can search and install packages from it via CLI.
## 3. 🛠 Using **NixOS** (the Linux distro built on Nix)

NixOS is where Nix goes from **build tool** to **OS-level configuration manager**. With it, _your entire OS_ is defined in one or a few `.nix` files.

## Cachix

Cachix is a **public and private binary cache** for Nix and NixOS users. It works by storing and sharing pre-built binary packages, so you don’t need to rebuild dependencies every time you install or deploy software.

- **Binary Caching**: Instead of building everything from source every time (which can be slow), Cachix allows you to cache the results of Nix builds, so you can fetch already-built binaries instead.
- **Public & Private Caches**: You can use public caches provided by others (e.g., the official NixOS cache) or set up your own private cache, ideal for teams or organizations.
- **Integration with CI/CD**: Cachix can be integrated with continuous integration/continuous deployment (CI/CD) systems to automatically push builds to a cache.