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

## Install Kubernetes on Proxmox

Resources for setting up a Kubernetes cluster on Proxmox, using Terraform for VM provisioning and Ansible for cluster configuration.

### Guides & References

- [Install Kubernetes Cluster on Proxmox](https://computingforgeeks.com/install-kubernetes-cluster-proxmox/) — Step-by-step guide to deploying a K8s cluster on Proxmox VMs.
- [Deploying Kubernetes VMs in Proxmox with Terraform](https://austinsnerdythings.com/2021/09/23/deploying-kubernetes-vms-in-proxmox-with-terraform/) — Uses Terraform to provision the VMs before bootstrapping K8s.

### Terraform Repos

- [khanh-ph/proxmox-kubernetes](https://github.com/khanh-ph/proxmox-kubernetes/tree/develop) — Terraform modules to deploy a Kubernetes cluster on Proxmox.
- [omidiyanto/terraform-ansible-kubernetes-proxmox](https://github.com/omidiyanto/terraform-ansible-kubernetes-proxmox/tree/master) — Full Terraform + Ansible pipeline: provisions VMs on Proxmox and configures the K8s cluster end-to-end.