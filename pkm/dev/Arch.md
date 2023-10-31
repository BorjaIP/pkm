---
title:  Arch
created: Saturday 22nd April 2023 21:11
aliases: 
tags: linux
---

| Tool                                        | Description                |
| ------------------------------------------- | -------------------------- |
| [Archcraft](https://archcraft.io/)          | Yet another minimal distro |
| [ArcoLinux](https://arcolinux.com/)         | Another distro             |
| [Bling](https://github.com/BlingCorp/bling) | Utilities for AwesomeWM    |
| [AwesomeWM](https://awesomewm.org/)         | Window Manager             |
|[Qtile](http://www.qtile.org/)|Tiling window manager|

- [install tar.gz???](https://bbs.archlinux.org/viewtopic.php?id=66845)
- [Offline installation of packages](https://wiki.archlinux.org/title/Offline_installation#Offline_installation_of_packages)

## Pacman

### Display information

```bash
pacman -Qii
```

### Display information by name

```bash
pacman -Qi name
```

### Packages installed

```bash
pacman -Qm
```

### All packages

```bash
pacman -Qqe
```

### Remove package

```bash
pacman -R name
```

### Remove all package from package

```bash
pacman -Rns name
```

### Remove packages your system doesn't need

```bash
pacman -Yc
```

## Java

https://rtfm.co.ua/en/arch-linux-set-a-java-version/

```bash
yay -S jdk
```

```bash
sudo archlinux-java status
```

## Certificates

Add trusted certificates:

- Move `/usr/local/share/ca-certificates/*.crt` to `/etc/ca-certificates/trust-source/anchors/`

- Do the same with all manually-added `/etc/ssl/certs/*.pem` files and rename them to *.crt

- Instead of update-ca-certificates, run `sudo trust extract-compat`

```bash
# one by one
trust anchor --store server.crt
sudo update-ca-trust
```

List all

```bash
trust list
```

Move all

```bash
sudo mv *.pem /etc/ca-certificates/trust-source/anchors/
```

```bash
sudo trust extract-compat
```

```bash
sudo update-ca-trust
```

## Errors

- Error with GPG keys

`error: failed to run: gpg --recv-keys 0D96DF4D4110E5C43FBFB17F2D347EA6AA65421D E3FF2839C048B25C084DEBE9B26995E310250568`

```bash
pacman-key --refresh-keys
```