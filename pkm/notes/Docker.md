---
title:  Docker
created: Sunday 23rd April 2023 17:20
aliases: 
tags: container
---
**Docker** is an open platform for developing, shipping, and running applications. Docker enables you to separate your applications from your infrastructure so you can deliver software quickly. With Docker, you can manage your infrastructure in the same ways you manage your applications. By taking advantage of Docker's methodologies for shipping, testing, and deploying code, you can significantly reduce the delay between writing code and running it in production.

| Tool                                                                      | Description                                                   |
| ------------------------------------------------------------------------- | ------------------------------------------------------------- |
| [Lazydocker](https://github.com/jesseduffield/lazydocker)                 | The lazier way to manage everything docker                    |
| [Dive](https://github.com/wagoodman/dive)                                 | A tool for exploring each layer in a docker image             |
| [Hadolint](https://github.com/hadolint/hadolint)                          | Dockerfile linter, validate inline bash, written in Haskell   |
| [Depend on Docker {DoD}](https://github.com/datasailors/depend-on-docker) | Open-source project that helps you containerize your software |
| [Grype](https://github.com/anchore/grype)                                 | A vulnerability scanner for container images and filesystems  |
| [Trivy](https://github.com/aquasecurity/trivy)                            | Find vulnerabilities, misconfigurations, secrets              |
| [Ctop](https://github.com/bcicen/ctop)                                    | Top-like interface for container metrics                      |
| [Edgeshark](https://github.com/siemens/edgeshark)                         | Discover and capture container network                        |
| [Skopeo](https://github.com/containers/skopeo)                            | Work with remote images registries                            |
| [Dockerc](https://github.com/NilsIrl/dockerc)                             | Container image to single executable compiler                 |

Deploy multiple dockers with [[Docker Compose]]

# Articles/Talks

- [[Simple C program to allocate memory from the command-line. Useful to test programs or systems under high memory usage conditions]]
- [[One Dockerfile for Production and Development]]
- [[Fast Docker Builds With Caching (Not Only) For Python]]
- [[Alpine-machine-learning-base]]
# Installation

[get.docker](https://get.docker.com/)

```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```
# Configuration

```bash
# modify for builtkit
vim /etc/docker/daemon.json

{
	# activate buildkit by default
	"features": {"buildkit": true},
    "bip": "10.0.20.10/16",
    "dns": ["172.18.18.101", "172.18.18.102"] ,
    "dns-search": ["nameserver.com"] ,
    "live-restore": true,
    "log-opts": {"max-size": "25m", "max-file": "4"},
    "insecure-registries" : ["registry.es:5000"] ,
    "registry-mirrors": ["https://registry.es:5000"],
    # subnet
    "default-address-pools":
      [
         {"base":"10.1.0.0/16","size":24}
      ]
}
# for docker-compose add
export COMPOSE_DOCKER_CLI_BUILD=1
# Show docker configuration for Registries
cat $HOME/.docker/config.json
# SYSTEMD
sudo systemctl daemon-reload
sudo systemctl restart docker
# display docker enviroments variables
sudo systemctl show docker --property Environment
```

Configure variables for proxy in docker [daemon](https://docs.docker.com/config/daemon/systemd/)
# Commands

## Run

```bash
docker run -it --entrypoint /bin/bash image:latest
```
### Run Ubuntu

```bash
docker run -it --rm ubuntu
apt update && apt install -y curl python3 python3-pip python3-venv
```
### Run IT-tools
- https://github.com/CorentinTh/it-tools

```bash
docker run -d --name it-tools --restart unless-stopped -p 8080:80 corentinth/it-tools:latest
```
## Networking

```bash
# Attach a running container to a network
docker network connect [network] [container]
```
## Logging

```bash
docker logs ID_CONTAINER -f
```

## Inspect

```bash
# show IP Docker
docker inspect -f '{{.NetworkSettings.IPAddress}}' ID or Name
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' ID or Name
# list all containers belonging to a network by name
docker inspect -f '{{range $key, $value := .NetworkSettings.Networks}}{{$key}} {{end}}' ID or Name
#show volumes
docker inspect -f '{{json .Mounts}}' ID | jq .
```

## System 

```bash
# Show information about space used for Docker
docker system df
```
## Stats

```bash
docker stats
```
## Registry

- Add docker **Registry** [insecure](https://docs.docker.com/registry/insecure/)

```bash
"insecure-registries" : ["registry.es:5000"]
```

- Create registry

```bash
docker run -d -p 5000:5000 --name registry registry:2
docker image tag ubuntu localhost:5000/myfirstimage
docker push localhost:5000/myfirstimage
```

- Push image to Docker Registry

```bash
docker login -u <user> -p <pass> https://url
docker tag image:latest url/image:latest
docker push url/image:latest
```
## Operations
### Stop all containers

```bash
docker stop $(docker ps -q)
```
### Show process machine

```bash
docker run --net=host --ipc=host --uts=host --pid=host -it --security-opt=seccomp=unconfined --privileged ubuntu top

docker exec -it CONTAINER_ID bash top
```
### Show volume information

```bash
docker run -it --rm -v /path/on/host:/vol busybox ls -l /vol
```
## Docker delete

### Delete all

```bash
docker system prune -a
```

### Delete unused or dangling

> Images, Containers, Volumes, and Networks

```bash
docker system prune
docker volume prune
```

### Delete unused containers

```bash
docker rm $(docker ps -aq)
```

### Delete build cache

```bash
docker builder prune
```

### Delete images dangling

```bash
docker rmi $(docker images -qf "dangling=true")
docker rmi $(docker images | grep "<none>" | awk '{print $3}')

# remove last 5 images
docker rm $(docker images -q | tail -n 5)
```

