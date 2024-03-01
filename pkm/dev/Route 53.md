---
title:  Route 53
created: Friday 1st March 2024 09:53
aliases: 
tags: 
---
Amazon Route 53 is a highly available and scalable Domain Name System (DNS) web service. You can use Route 53 to perform three main functions in any combination: domain registration, DNS routing, and health checking.

- Records types:
	- SOA records
	- NS Records
	- CNAME records
	- A records
	
- Routing Policies: 
	- Simple routing: 1 record multiple IPs
	- Weighted routing: % balance traffic
	- Latency-Based routing: ms balance traffic
	- Failover routing: Active/Passive failure traffic
	- Geolocation routing: EU/US location traffic
	- Geoproximity routing: used for traffic low
	- Multivalue answer routing
## Health Checks

- You can set health checks on individual record sets.
- If a record  set fails a health check, it will be removed from Route 53 until it passes the health check.
- You can set SNS notifications to alert you about failed health checks.
## A Record VS CNAME

The [`A` record](https://support.dnsimple.com/articles/a-record) points a name to a **specific IP**. If you want `blog.dnsimple.com` to point to the server `185.31.17.133` you’ll configure:

```
blog.dnsimple.com.     A        185.31.17.133
```

The [`CNAME` record](https://support.dnsimple.com/articles/cname-record) points a name to **another name instead** of to an IP. The CNAME source represents an alias for the target name and inherits its entire resolution chain.