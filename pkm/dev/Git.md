---
title:  Git
created: Sunday 23rd April 2023 16:46
aliases: 
tags: tool
---

| Tool                                                   | Description                                         |
| ------------------------------------------------------ | --------------------------------------------------- |
| [Gitbutler](https://github.com/gitbutlerapp/gitbutler) | The GitButler version control client, backed by Git |
- [Oh Shit, Git??](https://ohshitgit.com/)
- [GitButler](https://gitbutler.com/)
# Large files

## List the total size of HEAD

```bash
git ls-tree -r --long HEAD | awk '{sum+=$1} END {print sum}'
```

## Check the repo’s size and the number of objects

```bash
git count-objects -vH
```

## Search large files from history

Search large files 

```bash
git rev-list --objects --all \  
| git cat-file --batch-check='%(objecttype) %(objectname) %(objectsize) %(rest)' \  
| awk '/^blob/ {print substr($0,6)}' \  
| sort --numeric-sort --key=2 \  
| cut --complement --characters=13-40 \  
| numfmt --field=2 --to=iec-i --suffix=B --padding=7 --round=nearest
```

Use [bfg](https://github.com/rtyley/bfg-repo-cleaner) for use with large files.

```bash
# Find the largest files in .git:
git rev-list --objects --all | grep -f <(git verify-pack -v  .git/objects/pack/*.idx| sort -k 3 -n | cut -f 1 -d " " | tail -10)
# To remove all blobs from history, whose size is superior to 100Mb
# Execute the previous command for see the results
bfg -b 100M
# Execute this commands below for erase commits and old files
git reflog expire --expire=now --all
git gc --prune=now --aggressive
# Push changes
git push origin <your_branch_name> --force
```
