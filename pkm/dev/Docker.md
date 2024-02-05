---
title:  Docker
created: Sunday 23rd April 2023 17:20
aliases: 
tags: container
---

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
| [Skopeo](https://github.com/containers/skopeo)                                                                          | Work with remote images registries                                                              |

Deploy multiple dockers with [[Docker Compose]]

- [Awesome Docker](https://github.com/veggiemonk/awesome-docker)
- [Simple C program to allocate memory from the command line. Useful to test programs or systems under high memory usage conditions](https://github.com/julman99/eatmemory)
- [One Dockerfile for Production and Development](https://zach.codes/one-dockerfile-for-production-and-development/)
- [Fast Docker Builds With Caching (Not Only) For Python](https://towardsdatascience.com/fast-docker-builds-with-caching-for-python-533ddc3b0057)
- [Alpine-machine-learning-base](https://github.com/petronetto/alpine-machine-learning-base)

## Installation

[get.docker](https://get.docker.com/)

```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```

## Configuration

```bash
# modify for builtkit
vim /etc/docker/daemon.json

{
    "features": {"buildkit": true}
}
# for docker-compose add
export COMPOSE_DOCKER_CLI_BUILD=1
# Show docker configuration for Registries
cat $HOME/.docker/config.json
# SYSTEMD
systemctl daemon-reload
systemctl restart docker
# display docker enviroments variables
systemctl show docker --property Environment
```

Configure variables for proxy in docker [daemon](https://docs.docker.com/config/daemon/systemd/)

## Commands

### Run

```bash
docker run -it --entrypoint /bin/bash image:latest
```

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

### Logging

```bash
docker logs ID
```

### System 

```bash
# Show information about space used for Docker
docker system df
```

### Stats

```bash
docker stats
```


### Delete

#### Delete all

```bash
docker system prune -a
```

#### Delete unused or dangling

> Images, Containers, Volumes, and Networks

```bash
docker system prune
docker volume prune
```

#### Delete unused containers

```bash
docker rm $(docker ps -aq)
```

#### Delete build cache

```bash
docker builder prune
```

#### Delete images dangling

```bash
docker rmi $(docker images -qf "dangling=true")
docker rmi $(docker images | grep "<none>" | awk '{print $3}')

# remove last 5 images
docker rm $(docker images -q | tail -n 5)
```

### Docker networking

```bash
# Attach a running container to a network
docker network connect [network] [container]
```


### Docker logging

```bash
docker logs ID_CONTAINER -f
```

### Docker Inspect

```bash
# show IP Docker
docker inspect -f '{{.NetworkSettings.IPAddress}}' ID or Name
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' ID or Name
# list all containers belonging to a network by name
docker inspect -f '{{range $key, $value := .NetworkSettings.Networks}}{{$key}} {{end}}' ID or Name
#show volumes
docker inspect -f '{{json .Mounts}}' ID | jq .
```

### Docker Registry

Add docker **Registry** [insecure](https://docs.docker.com/registry/insecure/)

Create registry

```bash
docker run -d -p 5000:5000 --name registry registry:2
docker image tag ubuntu localhost:5000/myfirstimage
docker push localhost:5000/myfirstimage
```

Push image to Docker Registry

```bash
docker login -u <user> -p <pass> https://url
docker tag image:latest url/image:latest
docker push url/image:latest
```