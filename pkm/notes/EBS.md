---
title:  EBS
created: Thursday 29th February 2024 13:49
aliases: 
tags: 
---
**Elastic Block Store** (Amazon EBS) provides block level storage volumes for use with EC2 instances. EBS volumes behave **like raw, unformatted block devices**. You can mount these volumes as devices on your instances. EBS volumes that are attached to an instance are exposed as storage volumes that persist independently from the life of the instance. You can create a file system on top of these volumes, or use them in any way you would use a block device (such as a hard drive). You can dynamically change the configuration of a volume attached to an instance.

### What is an IOPS AWS?

IOPS is an acronym for **input/output operations per second** and is a popular performance metric used to distinguish one storage type from another. Similar to device makers, AWS associates IOPS values to the volume component backing the storage option. Provisioned IOPS are an AWS EBS volume type designed to deliver predictable, high-level performance for I/O intensive workloads such as database applications.

IOPS usage can be simply calculated by knowing the total read and write throughputs (ops) of your disk divided by the time in seconds within that period.

> **_NOTE:_** IOPS Usage = (Total Read + Write Throughputs) / Time (in Seconds)

Example: IOPS = ( 15000 + 100 ) / 300
## Types for SSD

### gp2

- Suitable for boot disks and general apps
- Up to 16000 IOPS
### gp3

-  Suitable for high performance apps
- Predictable 3000 IOPS performance and 125MB/s
### io1

- Suitable for OLTP and latency-sensitive apps
- 50 IOPS/GiB
- Up to 64000 IOPS
- High performance and most expensive
### io2

- Suitable for OLTP and latency-sensitive apps
- 500 IOPS/GiB
- Up to 64000 IOPS
- Latest generation provisioned IOPS volume

## Types for HDD

### st1

- Suitable for big data, data warehouses and ETL
- Max throughput is 500 MB/s
- Cannot be a boot volume
### sc1

- Max throughput is 250 MB/s
- Cannot be a boot volume
- Lowest cost