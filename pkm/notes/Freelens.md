---
title:  Freelens
created: Saturday 21st March 2026 11:01
aliases: 
tags: 
---
Config for custom NS and other options:

```bash
# Linux
~/.config/Freelens/lens-cluster-store.json

# macOS
~/Library/Application Support/Freelens/lens-cluster-store.json

# Windows
%APPDATA%\Freelens\lens-cluster-store.json
```

```json
{
  "clusters": [
    {
      "id": "abc123",
      "kubeConfigPath": "/home/user/.kube/config",
      "contextName": "mi-cluster",
      "preferences": {
        "accessibleNamespaces": [
          "namespace-1",
          "namespace-2",
          "namespace-3"
        ]
      }
    }
  ]
}
```