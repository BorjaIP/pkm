---
title: Windows
created: Saturday 22nd April 2023 19:26
aliases:
  - win
tags:
  - windows
  - os
---
Windows is a desktop [[operating system]] developed by Microsoft. For the past three decades, Windows has been the most popular operating system for personal computers.
# Programs

| Programs                                                                  | Description                                                                   |
| ------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| [OpenRGB](https://openrgb.org/)                                           | Open source RGB lighting control that doesn't depend on manufacturer software |
| [NVcleanstall](https://www.techpowerup.com/nvcleanstall/)                 | Install NVIDIA Drivers                                                        |
| [Debloater](https://github.com/Sycnex/Windows10Debloater)                 | Remove all unnecesary windows applications                                    |
| [Autohotkey](https://www.autohotkey.com/)                                 | Hotkey software                                                               |
| [HotkeyD](https://github.com/HikariKnight/hotkeyD)                        | Hotkey software                                                               |
| [Trakt-scrobbler](https://github.com/iamkroot/trakt-scrobbler)            | Scrobbler for trakt.tv                                                        |
| [VIA](https://caniusevia.com/)                                            | Keyboard mapping                                                              |
| [Vial](https://get.vial.today/)                                           | Keyboard mapping                                                              |
| [QMK Fimeware](https://docs.qmk.fm/#/)                                    | Keyboard fimewares                                                            |
| [PowerToys](https://github.com/microsoft/PowerToys)                       | System utilities                                                              |
| [O&O ShutUp](https://www.oo-software.com/en/shutup10)                     | AntySpy                                                                       |
| [SumatraPDF](https://www.sumatrapdfreader.org/free-pdf-reader)            | PDF Viewer                                                                    |
| [CoreTemp](https://www.alcpu.com/CoreTemp/)                               | Monitor CPU                                                                   |
| [OpenHardware](https://openhardwaremonitor.org/)                          | Monitor tempoerature sensors                                                  |
| [PowerUP](https://www.techpowerup.com/gpuz/)                              | Information about GPU                                                         |
| [Handbraker](https://handbrake.fr/)                                       | Video transcoder                                                              |
| [ShareX](https://getsharex.com/)                                          | Screen capture                                                                |
| [DevToys](https://devtoys.app/)                                           | An offline app that helps developers in daily tasks                           |
| [ModernFlyouts](https://github.com/ModernFlyouts-Community/ModernFlyouts) | Fluent design system for windows                                              |
| [Files](https://files.community/)                                         | Building the best file manager experience for Windows                         |
| [KeepassXC](https://github.com/keepassxreboot/keepassxc)                  | Open-source password manager                                                  |
| [FanControl](https://github.com/Rem0o/FanControl.Releases)                | Highly customizable fan controlling software for Windows\|                    |
| [mRemoteNG](https://github.com/mRemoteNG/mRemoteNG)                       | Open source, tabbed, multi-protocol, remote connections manager               |
| [glazewm](https://github.com/glzr-io/glazewm)                             | GlazeWM is a tiling window manager for Windows inspired by i3wm               |
| [TranslucentTB](https://github.com/TranslucentTB/TranslucentTB)           | A lightweight utility that makes the Windows taskbar translucent/transparent  |
| [Zebar](https://github.com/glzr-io/zebar)                                 | Zebar is a tool for creating customizable and cross-platform taskbars         |
| [Flow.Launcher](https://github.com/Flow-Launcher/Flow.Launcher)           | Quick file search & app launcher for Windows with community-made plugins      |
| [ExplorerPatcher](https://github.com/valinet/ExplorerPatcher)             | This project aims to enhance the working environment on Windows               |

- [NZXT](https://nzxt.com/software/cam)
- [AMD Wraith Prism](https://landing.coolermaster.com/pages/amd-ryzen-wraith-prism-rgb-software/)
- [Trident Z RGB](https://www.gskill.com/download/1502180912/1551690847/Trident-Z-Family-(RGB,-Royal,-Neo))
- [RGB Fusion](https://www.gigabyte.com/MicroSite/512/download.html)
## Startup Programs

- Open execute window `Win+R`:

```bash
# delete all unnecesary
shell:startup
# delete all unnecesary
shell:common startup
```

- Open `regedit` and delete all unnecessary:

```bash
# For User
Computer\HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
# For Local Machine
Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
```

Open `Task scheduler` and **DISABLE** all unnecessary.

- Disable all Edge.
- Disable all Nvidia reports and updates in background.
## OpenRGB

```bash
E:\Programs\OpenRGB\OpenRGB.exe --gui --startminimized --server
```
# Variables

- System variables for configure program, appdata and user profile.

```bash
# Env variables
%PROGRAMFILES%
%APPDATA%
%LocalAppData%
%USERPROFILE%
```
# Folders

User config is in `C:\Users\Borja`, for example `.ssh`

- Hosts

```bash
C:\Windows\System32\drivers\etc
```

- Tmp

```bash
C:\Users\Borja\AppData\Local\Temp
```

- SSH

```bash
C:\Users\Borja\.ssh
```

- [Sort by 'Date Modified' but keep folders at the top?](https://answers.microsoft.com/en-us/windows/forum/all/sort-by-date-modified-but-keep-folders-at-the-top/746b8380-63fd-4d77-a568-fac11d917ad7)

# Commands

- List which process is listening in a port

```bash
Get-Process -Id (Get-NetTCPConnection -LocalPort 6443).OwningProcess
```

- List ports

```bash
netstat -abn
```

- Kill process

```bash
Stop-Process -Id 30240 -Force
```
## Install Modules

```bash
Install-Module -Name Terminal-Icons -Repository PSGallery
Install-Module -Name PSReadLine -Force
Install-Module -Name PSFzf -Force
Install-Module -Name z -Force
```

# Powershell

Personalize Windows Terminal.

1. Install windows [terminal](https://github.com/microsoft/terminal).
2. Install Powershell from Windows Store.
3. Install [Nerd Fonts](https://www.nerdfonts.com/font-downloads) for active Icons in particular [Inconsolata](https://github.com/ryanoasis/nerd-fonts/releases) from the releases and select `Inconsolata Regular Nerd Font Complete Windows Compatible.ttf`.
   - Be careful with the [issue 509](https://github.com/ryanoasis/nerd-fonts/issues/509).
4. Change color scheme to [Base 16](https://github.com/ShiromMakkad/base16-windows-terminal) Ocean.
5. Install [Startship](https://github.com/starship/starship) for custom prompt.
6. Edit Powershell profile with VScode. 

```bash
code $PROFILE
. $env:USERPROFILE\.config\powershell\profile.ps1
```

1. Create `profile.ps1` file in .config for custom configuration.
2. . Install [Terminal Icons](https://github.com/devblackops/Terminal-Icons).
3.  Install [PSReadLine](https://github.com/PowerShell/PSReadLine).
4. Install [z Directory Jumper](https://github.com/jethrokuan/z).
5. Install [fzf](https://github.com/junegunn/fzf) y [PSfzf](https://github.com/kelleyma49/PSFzf).

How to know which version of Powershell

```bash
$PSVersionTable
```

# Package manager

**A** **package** **manager** or **package**-management system is a collection of software tools that automates the process of installing, upgrading, configuring, and removing computer programs for a computer in a consistent manner. A **package** **manager** deals with **packages**, distributions of software and data in archive files.

- [[Winget]]
- [[Chocolatey]]
- [Scoop](https://scoop.sh/)

# Key

For show windows key open `regedit` and see the key:
`Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\WindowsNT\CurrentVersion\SoftwareProtectionPlatform`

# Drivers

Uninstall all GPU drivers

- [DDU](https://www.guru3d.com/files-details/display-driver-uninstaller-download.html)
# WSL

``` bash
# Link .ssh folder
sudo ln -s /mnt/c/Users/<user>/.ssh ~/.ssh
# Link .kube folder
sudo ln -s /mnt/c/Users/<user>/.kube ~/.kube
```

- [WSL-vpnkit](https://github.com/sakai135/wsl-vpnkit)
- [HyperV-fix-for-dev](https://github.com/jgregmac/hyperv-fix-for-devs)
## Network


```powershell
# Add Port Forwarding
netsh interface portproxy add v4tov4 listenport=$port connectport=$port connectaddress=$remoteaddr
# Add Firewall Rule
netsh advfirewall firewall add rule name=$port dir=in action=allow protocol=TCP localport=$port
# Delete PortForwarding
netsh interface portproxy delete v4tov4 listenport=$port
# Delete Firewall Rule
netsh advfirewall firewall delete rule name=$port
# Show PortForwardings
netsh interface portproxy show v4tov4
```

- Internet slow in terminal and in WSL2 --> https://github.com/microsoft/WSL/issues/4901#issuecomment-1933155508
- Traceroute 

```bash
tracert 8.8.8.8
```

- Restart `resolv.conf`

```bash
sudo rm /etc/resolv.conf
sudo bash -c 'echo "nameserver 8.8.8.8" > /etc/resolv.conf'
sudo bash -c 'echo "[network]" > /etc/wsl.conf'
sudo bash -c 'echo "generateResolvConf = false" >> /etc/wsl.conf'
sudo chattr +i /etc/resolv.conf
```

- Test connectivity between windows and WSL

```bash
# start server in WSL
python -m http.server --bind 0.0.0.0
# attack in windows
curl localhost:8000
```

- Add Static IP to WSL in Networking Mode = NAT. --> https://stackoverflow.com/questions/69691928/can-i-set-a-static-ip-address-for-wsl-2

Modify in regedit:

```bash
Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Lxss\NatNetwork Computer\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Lxss\NatGatewayIpAddress
# Current IP
Computer\HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Lxss
```

- Problem IPv6 with WSL --> https://github.com/microsoft/WSL/issues/11002

![[wsl_ipv6.png]]