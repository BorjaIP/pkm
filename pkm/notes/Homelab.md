---
title: Homelab
created: Friday 29th November 2024 23:43
aliases: 
tags:
  - Homelab
---

| Tool                                                            | Description                                                                                                                    |
| --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| [Immich](https://github.com/immich-app/immich)                  | High performance self-hosted photo and video management solution                                                               |
| [Flame](https://github.com/pawelmalak/flame)                    | Flame is self-hosted startpage for your server.                                                                                |
| [Swag](https://github.com/linuxserver/docker-swag)              | Nginx webserver and reverse proxy with php support and a built-in Certbot                                                      |
| [Trash-guides](https://trash-guides.info/)                      | Guides mainly for Sonarr/Radarr/Bazarr                                                                                         |
| [Linkding](https://github.com/sissbruecker/linkding)            | Self-hosted bookmark manager that is designed be to be minimal,                                                                |
| [Wallabag](https://github.com/wallabag/wallabag)                | Wallabag is a self hostable application for saving web pages                                                                   |
| [Commafeed](https://github.com/Athou/commafeed)                 | Google Reader inspired self-hosted personal RSS reader                                                                         |
| [Linkwarden](https://github.com/linkwarden/linkwarden)          | Self-hosted collaborative bookmark manager to collect, organize, and preserve webpages, articles, and documents                |
| [Memos](https://github.com/usememos/memos)                      | An open-source, lightweight note-taking solution                                                                               |
| [Maybe](https://github.com/maybe-finance/maybe)                 | The OS for your personal finances                                                                                              |
| [Actual](https://github.com/actualbudget/actual)                | A local-first personal finance app                                                                                             |
| [WG-easy](https://github.com/wg-easy/wg-easy)                   | The easiest way to run WireGuard VPN + Web-based Admin UI                                                                      |
| [Solidtime](https://github.com/solidtime-io/solidtime)          | Modern open-source time-tracking app                                                                                           |
| [Siyuan](https://github.com/siyuan-note/siyuan)                 | A privacy-first, self-hosted, fully open source personal knowledge management software (PKM)                                   |
| [Online](https://github.com/CollaboraOnline/online)             | Collabora Online is a collaborative online office suite based on LibreOffice technology                                        |
| [Paperless-ngx](https://github.com/paperless-ngx/paperless-ngx) | A community-supported supercharged version of paperless                                                                        |
| [Kavita](https://github.com/Kareadita/Kavita)                   | Kavita is a fast, feature rich, cross platform reading server.                                                                 |
| [Syncthing](https://github.com/syncthing/syncthing)             | Open Source Continuous File Synchronization                                                                                    |
| [Stirling-PDF](https://github.com/Stirling-Tools/Stirling-PDF)  | Locally hosted web application that allows you to perform various operations on PDF files                                      |
| [Firefly-iii](https://github.com/firefly-iii/firefly-iii)       | Firefly III: a personal finances manager                                                                                       |
| [pangolin](https://github.com/fosrl/pangolin)                   | Identity-aware VPN and proxy for remote access to anything, anywhere.                                                          |
| [lidify](https://github.com/Chevron7Locked/lidify)              | Lidify is built for music lovers who want the convenience of streaming services without sacrificing ownership of their library |
| [Twenty](https://github.com/twentyhq/twenty)                    | Open-source self-hosted CRM, a modern alternative to Salesforce                                                                |

## Inspiration

Resources and projects to draw ideas from — not necessarily in use, but worth studying.

| Resource                                                                    | Description                                                                         |
| --------------------------------------------------------------------------- | ----------------------------------------------------------------------------------- |
| [Deployrr](https://github.com/SimpleHomelab/Deployrr)                       | Automated Docker homelab deployer with 150+ pre-configured apps, Traefik, and auth |

## Backup Storage

### 3-2-1 Strategy

A simple, resilient backup rule that eliminates every single point of failure.

| Number | Rule | Example |
| ------ | ---- | ------- |
| **3** | Three total copies of your data | Original + 2 backups |
| **2** | Two different devices / storage media | Local NAS + external drive |
| **1** | One copy off-site | Cloud (Backblaze B2, S3…) or remote server |

Protects against: human error, drive failure, theft, ransomware, and natural disasters. [Source](https://www.backblaze.com/blog/the-3-2-1-backup-strategy/)

### Incremental Backups with `rsync`

`rsync --link-dest` creates space-efficient snapshots: unchanged files become hard links to the previous snapshot instead of new copies, so only new/modified files consume extra space. [Source](https://linuxconfig.org/how-to-create-incremental-backups-using-rsync-on-linux)

**Key flags**

| Flag | Purpose |
| ---- | ------- |
| `-a` | Archive mode — preserves permissions, timestamps, symlinks, owner, group |
| `-v` | Verbose output |
| `--delete` | Remove files from destination that no longer exist in source |
| `-e ssh` | Use SSH as transport for remote backups |
| `--link-dest=DIR` | Reference dir; unchanged files become hard links instead of copies |

**Date-stamped snapshot script**

```bash
#!/bin/bash
SOURCE=/home/user/data/
DESTBASE=/backup/data
DEST="$DESTBASE/$(date +%Y-%m-%d)"
YESTERDAY="$DESTBASE/$(date -d yesterday +%Y-%m-%d)/"

OPTS=""
[ -d "$YESTERDAY" ] && OPTS="--link-dest $YESTERDAY"

rsync -av $OPTS "$SOURCE" "$DEST"
```

Each run creates a new `YYYY-MM-DD/` directory. Only changed files are written; the rest are hard-linked from yesterday.

**7-day rolling rotation**

```bash
#!/bin/bash
rm -rf /backup/daily.7
for i in 6 5 4 3 2 1 0; do
    [ -d "/backup/daily.$i" ] && mv "/backup/daily.$i" "/backup/daily.$((i+1))"
done
rsync -a --delete --link-dest=/backup/daily.1 /home/user/data/ /backup/daily.0/
```

**Remote backup over SSH**

```bash
rsync -av -e ssh /home/user/data/ user@backup-server:/backup/data/
```

**Cron — run daily at 02:00**

```cron
0 2 * * * /usr/local/bin/backup.sh
```

### Tools

| Tool | Description |
| ---- | ----------- |
| [Duplicati](https://github.com/duplicati/duplicati) | Free backup software with encryption, deduplication, and cloud support |
| [Restic](https://github.com/restic/restic) | Fast, secure, efficient backup program with deduplication and encryption |
| [BorgBackup](https://github.com/borgbackup/borg) | Deduplicating archiver with compression and authenticated encryption |
| [Syncthing](https://github.com/syncthing/syncthing) | Continuous file sync (not a backup, but useful for the 2nd local copy) |
