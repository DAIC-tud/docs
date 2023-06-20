---
title: "Job submission and management"
linkTitle: "Job submission and management"
weight: 6
description: >
  How to submit jobs to slurm?
---

## Batch Queuing System Overview

## Job Submission Process


## Example Job Scripts


## Job Monitoring and Status Checking


## Job prioritization and waiting times

### Fair tree fairshare

### Priority tiers
The partitions are tiered: the general partition is in the lowest priority tier, department partitions (insy, st) are in the middle priority tier, and partitions for specific groups (visionlab, wis) are in the highest priority tier.

When resources become available, the scheduler will first look for jobs in the highest priority partition that those resources are in, and start the highest (user)priority jobs that fit within the resources (if any). When resources remain, the scheduler will check the next lower priority tier, and so on. Finally, the scheduler will try to backfill lower (user)priority jobs that fit (if any).

The partition priorities have no impact on resources that are in use, so jobs have to wait until the resources become available.

A nice thing about Slurm is that you can specify multiple partitions for your job (--partition=wis,st,general) which should give the job the highest possible priority on the different partitions (resources) in the cluster, at no cost for yourself or others.


### Where to submit jobs?

>  1. Yes, he is able to submit identical jobs to both `st` and `general` partition

Why submit to the one or the other instead of to both? (The idea behind the tiering is to submit to all partitions, i.e. '--partition=st,general', and let the scheduler figure out were the job can start the soonest...)

>  2. For the same requested resources, jobs submitted to the `st` partition wait longer than jobs submitted to the `general` partition

Of course, the 'general' partition has much more resources, and the bigger the resource pool, the more chances a job has to be scheduled or back-filled... (The 'st' resources are also part of the 'general' partition, so by using the 'general' partition jobs get to use both the 'st' resources nodes and all the other nodes.)

Why then specify the 'st' partition? That is to skip over higher-priority jobs that would otherwise get started first on resources that are also in the 'st' partition.

>  3. Additionally, to view all his jobs, he needs to grep for his name- ie, `squeue -u yanivoren` only shows jobs in the `general` partition. Screenshot below

He should use 'squeue --all --me'. You should use 'squeue --all --user=<username>'.

All partitions except the general partition are hidden, to simplify the idea for starting users. (This is a choice, so we can decide to make them visible by default.)



## Troubleshooting Common Issues - _Likely contains links to the Support area_