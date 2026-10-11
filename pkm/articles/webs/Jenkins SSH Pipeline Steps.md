---
title:  Jenkins SSH Pipeline Steps
created: Friday 11th April 2025 22:59
aliases: 
tags:
  - jenkins
  - ci-cd
  - devops
---
- https://github.com/jenkinsci/ssh-steps-plugin
- Type: repo
- Source: GitHub · jenkinsci · Apache-2.0 (plugins.jenkins.io/ssh-steps)

---

# TL;DR

The SSH Steps plugin gives [[Jenkins]] pipelines `sshCommand`, `sshScript`, `sshPut`, `sshGet` and `sshRemove` to run commands and move files on remote hosts.

# What it does

Each step takes a `remote` map with `name`, `host`, `user` and one of `password`, `identity` or `identityFile`, plus optional `port` (default 22), `knownHosts` or `allowAnyHosts`, `timeoutSec`, `retryCount`, `fileTransfer` (`sftp` or `scp`), proxy/gateway and logging settings.

# Key takeaways

1. **Run a command**: `sshCommand` returns output and supports `sudo`, `failOnError` and `dryRun`.
2. **Run a script** from the workspace with `sshScript` (no arguments).
3. **Copy files**: `sshPut` uploads and `sshGet` downloads files or directories with optional filters; `sshRemove` deletes.
4. **Keep keys out of the script**: bind a `sshUserPrivateKey` credential with `withCredentials` into `remote.user` and `remote.identityFile`.
5. **Mind host keys**: `allowAnyHosts` skips verification, so prefer `knownHosts` in production.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[Jenkins]] | Host for the plugin |
| [[Linux]] | Typical remote targets |
| [[Security]] | Credentials binding and host-key checking |

# When to use

1. When a pipeline must **deploy or run commands over SSH**.
2. When you need the **`remote` map options** (timeouts, retries, scp vs sftp).
3. When binding private keys securely in a Jenkinsfile.

# Caveats

- The page lists no release versions; check the plugin index for the current one.

---
[[Jenkins]] [[Linux]] [[DevOps]]
[[Jenkins running multiple steps]]
[[Jenkins pipeline Syntax]]
