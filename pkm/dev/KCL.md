---
title:  KCL
created: Friday 31st May 2024 18:37
aliases: 
tags: 
---
[KCL](https://github.com/kcl-lang/kcl) is an open-source configuration and policy language hosted by the Cloud Native Computing Foundation (CNCF) as a Sandbox Project. Built on a foundation of constraints and functional programming principles, KCL enhances the process of writing complex configurations, particularly in cloud-native environments. By leveraging advanced programming language techniques, KCL promotes improved modularity, scalability, and stability in configuration management. It simplifies logic writing, offers easy-to-use automation APIs, and seamlessly integrates with existing systems.

```yaml
apiVersion = "apps/v1"  
kind = "Deployment"  
metadata = {  
	name = "nginx"  
	labels.app = name  
}  
spec = {  
	replicas = 3  
	selector.matchLabels = metadata.labels  
	template.metadata.labels = metadata.labels  
	template.spec.containers = [  
		{  
		name = metadata.name  
		image = "${metadata.name}:1.14.2"  
		ports = [{ containerPort = 80 }]  
		}
	]  
}
```

We can use the KCL code to generate a Kubernetes YAML manifest.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx
  labels:
    app: nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
        - name: nginx
          image: nginx:1.14.2
          ports:
            - containerPort: 80
```