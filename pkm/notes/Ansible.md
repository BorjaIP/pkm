---
title: Ansible
created: Sunday 2nd February 2026 12:17
tags:
  - automation
  - devops
  - iac
  - configuration-management
---
## Core Concepts

Ansible operates on a simple model: a **control node** (where Ansible is installed) orchestrates **managed nodes** (the target servers) without requiring any agents on them. This simplifies setup and reduces the security footprint.

### Inventory
The **inventory** is the foundational list of your managed nodes. It's a text file (INI or YAML) that groups hosts, allowing you to target specific machines for specific tasks.

```ini
# A sample inventory file
[web_servers]
host1.example.com
host2.example.com

[db_servers]
db1.example.com
```

### Playbooks
**Playbooks** are YAML files that describe the desired state of your systems. They contain a series of **plays**, and each play maps a group of hosts to a set of **tasks**. Tasks are executed sequentially by calling Ansible modules.

### Modules
A **module** is a script that performs a specific action, such as managing packages (`apt`), creating directories (`file`), or starting services (`service`). Ansible has thousands of built-in modules, and you can also write your own.

### Idempotency
This is a critical principle in Ansible. An operation is **idempotent** if running it once has the same effect as running it multiple times. Ansible modules are designed to be idempotent; they check the current state of the system and only make changes if necessary to achieve the desired state defined in the playbook.

## Code Examples

### Playbook with Variables
This playbook installs the `tree` utility on all servers in the `web_servers` group. It uses a variable to define the package name, making the playbook more reusable.

```yaml
# content of setup_tools.yml
---
- name: Install common utilities on web servers
  hosts: web_servers
  become: yes # Use 'sudo' to gain root privileges
  vars:
    package_to_install: tree

  tasks:
    - name: "Install the {{ package_to_install }} package"
      ansible.builtin.apt:
        name: "{{ package_to_install }}"
        state: present
        update_cache: yes # Good practice to update cache before installing

    - name: Verify installation by running the command
      ansible.builtin.command: "{{ package_to_install }} --version"
      register: command_output
      changed_when: false # This command doesn't change state

    - name: Display the installed version
      ansible.builtin.debug:
        msg: "{{ command_output.stdout }}"

```
> To run this playbook: `ansible-playbook -i inventory.ini setup_tools.yml`

## Related Concepts
- [[IaC]]
- [[DevOps]]
- [[Kubernetes]]
- [[Docker]]
- [[Terraform]]
- [[Python]]
- [[YAML]]

