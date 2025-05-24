---
title:  Proxmox
created: Wednesday 7th May 2025 16:58
aliases: 
tags: 
---
- List all VM IDs on the node using the following command

```bash
cat /etc/pve/.vmlist
```

- vm options

```bash
qm shutdown [vmid]
qm stop [vmid]
qm destroy [vmid]
```

- lxc options

```bash
lxc-ls --fancy
lxc-destroy -n [lxcid]

pct list
pct destroy [vmid]
pct enter 206
```