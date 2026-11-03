---
title:  YubiKey
created: Sunday 1st November 2026 13:00
aliases:
  - YubiKeys
  - Security key
tags:
  - security
part_of:
  - "[[Security]]"
related:
  - "[[IAM]]"
---
A **YubiKey** is a hardware security key from Yubico. It holds secrets that never leave the device and proves you are you by touch, so a stolen password or a phishing page is not enough to get into an account. One key exposes several independent applications over USB and NFC.

## Interfaces

| Application | What it is for | Phishing resistant |
| --- | --- | --- |
| FIDO2 / WebAuthn | Passkeys and security keys for websites, optionally passwordless | Yes |
| FIDO U2F | Older second factor, still accepted by many sites and by PAM | Yes |
| OATH (TOTP / HOTP) | Six-digit codes stored on the key and read with `ykman` or an authenticator app | No |
| OpenPGP | GPG keys on the card: sign Git commits, encrypt files, SSH through the GPG agent | Yes |
| PIV | Smart-card certificates for login, TLS client auth and SSH | Yes |
| Yubico OTP | One-time password typed as a keyboard | No |
| HMAC challenge-response | Secret used by tools such as KeePassXC to unlock a database | n/a |

## Setup basics

```bash
ykman info                              # model, firmware, enabled applications
ykman fido info                         # FIDO2 state
ykman fido access change-pin            # set the FIDO2 PIN
ykman fido config toggle-always-uv      # require the PIN on every use
```

- Register at least **two keys** on every account (primary plus backup) and keep the backup somewhere else.
- Change the OpenPGP defaults at once: User PIN `123456` and Admin PIN `12345678` (`ykman openpgp access change-pin` and `change-admin-pin`).
- Require touch on the card: `ykman openpgp keys set-touch sig on` (also `aut`, `enc`).

## Common uses

### Two-factor and passkeys
Add the key as a security key on the account (Google, GitHub, Microsoft...). With FIDO2 and a PIN it can replace the password.

### TOTP on the key
```bash
ykman oath accounts add <name> <secret>
ykman oath accounts code
```
Codes live on the key, so they survive a lost phone, but they can be phished unlike FIDO2.

### Signing Git commits with GPG
```bash
gpg --card-edit                          # admin, key-attr, generate
gpg --list-keys --keyid-format=long
git config --global user.signingkey <KEYID>
git config --global commit.gpgsign true
git log --show-signature -1
```
Export the public key to GitHub. Generate ed25519 (signing) and cv25519 (encryption) keys on the card so the private key is never on disk.

### Encrypting files
`gpg --encrypt --recipient <ENC_KEYID>! secret.txt`, then `gpg --decrypt secret.txt.gpg` needs the key plus a touch.

### SSH with a hardware key
```bash
ssh-keygen -t ed25519-sk                 # OpenSSH 8.2+, key bound to the YubiKey
ssh-keygen -t ed25519-sk -O resident     # discoverable, can be restored with ssh-keygen -K
```
Alternative: use the OpenPGP authentication subkey through `gpg-agent` as the SSH agent.

### KeePassXC
Program OTP slot 2 for HMAC-SHA1 with touch, then add it as a challenge-response key to the database. The secret cannot be read back, so program the same secret on the backup key.

### sudo and login (Linux)
`pamu2fcfg > ~/.config/Yubico/u2f_keys` plus `auth required pam_u2f.so` in the PAM file. Test it with a root shell open, or a misconfiguration can lock you out.

## Pitfalls

- A lost key with no backup registered means account recovery; set up the second key first.
- **macOS:** a frozen PIN prompt is fixed by removing `pinentry-mode loopback` and using `pinentry-mac` (`brew install gnupg pinentry-mac`, then set `pinentry-program` in `~/.gnupg/gpg-agent.conf`).
- After changing card state restart the daemons: `gpgconf --kill scdaemon; gpgconf --kill gpg-agent`.
- `ykman openpgp reset -f` wipes the OpenPGP keys on the card.

## Tools

| Tool | Description |
| --- | --- |
| [Yubikeys-cheatsheet](https://github.com/Opsek/Yubikeys-cheatsheet) | Practical guide (macOS and GnuPG): interfaces table, FIDO2 PIN, Git signing, file encryption, KeePassXC challenge-response, troubleshooting |
| [ykman](https://docs.yubico.com/software/yubikey/tools/ykman/) | Yubico command line to configure FIDO2, OATH, OpenPGP, PIV and OTP |

---
Related: [[Security]], [[IAM]], [[Git]], [[Vault]]
