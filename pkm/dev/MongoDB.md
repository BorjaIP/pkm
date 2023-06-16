---
title:  MongoDB
created: Sunday 30th April 2023 21:17
aliases: 
tags: db
---

- Create user and pass in specific database.

```bash 
mongo admin -u admin -p admin --eval "db.getSiblingDB('dummydb').createUser({user: 'dummyuser', pwd: 'dummysecret', roles: ['readWrite']})"
```