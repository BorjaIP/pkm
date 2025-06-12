---
title:  Wireguard
created: Thursday 12th June 2025 17:06
aliases: 
tags: 
---
# CLI

- https://blog.scottlowe.org/2021/08/04/starting-wireguard-interfaces-automatically-launchd-macos/

```bash
wg-quick up wg0
wg-quick down wg0
```

- Generate Keys

```bash
umask 077
wg genkey | tee privatekey | wg pubkey > publickey
```

- Create `w0.conf` file in `/usr/local/etc/wireguard`

```toml
[Interface]
PrivateKey = <private-key-generated-earlier>
Address = <vpn-ip-address-for-this-interface>

[Peer]
PublicKey = <public-key-for-peer-system>
Endpoint = <public-ip-address>:51280
AllowedIPs = <vpn-ip-address-for-peer-interface>, <additional-cidrs>
PersistentKeepalive = 25
```