---
title:  Cross-Account Access in the AWS Management Console
created: Friday 11th April 2025 21:26
aliases: 
tags:
  - aws
  - security
---
- https://aws.amazon.com/es/blogs/aws/new-cross-account-access-in-the-aws-management-console/
- Type: article
- Source: AWS News Blog · Jeff Barr · Jan 2015

---

# TL;DR

The console's **Switch Role** option lets an [[IAM]] user or federated identity work in another account through an IAM role, without a second login.

# Summary

The feature is built on IAM roles, which are not tied to a user and give temporary credentials when assumed. After signing in, a user chooses Switch Role, enters the account and role, optionally sets a display name and menu colour, and the console assumes that role. The console generates role-switching URLs and remembers up to five roles; administrators must set up the roles and groups first.

# Key takeaways

1. **Switch without credentials**: no separate user name or password for each account.
2. **Steps**: user name menu, Switch Role, enter account and role, optional display name and colour.
3. **Switch back** by choosing the original identity.
4. **Useful for splits** such as development and production in different accounts.
5. **Limit**: the console remembers five roles; administrators prepare the IAM roles and groups.

# Tools and concepts

| Item | Role in the page |
|---|---|
| [[IAM]] | Roles and temporary credentials |
| [[AWS]] | Management Console |
| [[Security]] | Access separation between accounts |

# When to use

1. When setting up **multi-account access** for people.
2. When you need the origin of the **Switch Role** feature.
3. When connecting to EKS access, see [[Enable an IAM User or IAM Role to access an EKS cluster]].

# Caveats

- 2015 announcement; it leaves trust policies and administrator setup to a separate security post.

---
[[AWS]] [[IAM]] [[Security]]
[[Enable an IAM User or IAM Role to access an EKS cluster]]
