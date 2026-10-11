---
title:  How do I schedule jobs in Jenkins
created: Friday 11th April 2025 23:01
aliases: 
tags:
  - jenkins
  - ci-cd
  - devops
---
- https://stackoverflow.com/questions/12472645/how-do-i-schedule-jobs-in-jenkins
- Type: qa
- Source: Stack Overflow · asked Sep 2012 · top answer 665 votes

---

# TL;DR

"Build periodically" uses cron syntax, and the `H` (hash) symbol spreads jobs across the hour instead of firing them all at once.

# Summary

The asker used `15 13 * * *` and expected 4:20 AM; that expression means every day at 13:15. The accepted answer explains the five cron fields, and later answers add the Jenkins-specific `H` symbol, multiple schedules separated by newlines, and examples such as weekday builds. Whether a job really runs also depends on the server time zone.

# Key takeaways

1. **Fields**: MINUTE (0-59), HOUR (0-23), DAY OF MONTH (1-31), MONTH (1-12), DAY OF WEEK (0-7, both 0 and 7 are Sunday).
2. **Use `H` instead of fixed values**: it is a hash of the job name, not random, so each job gets a stable but different time (`H H * * *` runs once a day without a midnight spike).
3. **Prefer `H/5 * * * *` over `*/5 * * * *`** to spread load.
4. **Ranges with `H`**: `H(0,30) 02 01 * *` picks a stable minute between 0 and 30.
5. **Several schedules** go on separate lines, for example `H 7 * * *` and `H 16 * * 0`.
6. **Examples**: `30 08 * * 1-5` weekday 08:30; `@midnight` for midnight.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[Jenkins]] | "Build periodically" trigger |
| cron syntax | Schedule expression format |
| [[Jenkins pipeline Syntax]] | Same rules in declarative `triggers { cron(...) }` |

# When to use

1. When **writing a cron schedule for a Jenkins job** and wondering why it did not run when expected.
2. When you need to **spread many jobs** without a load spike.
3. When translating the schedule into a declarative pipeline.

# Caveats

- Community answers from 2012-2018; the official syntax lives in the Jenkins documentation.

---
[[Jenkins]] [[DevOps]]
[[Jenkins pipeline Syntax]]
[[Jenkins running multiple steps]]
