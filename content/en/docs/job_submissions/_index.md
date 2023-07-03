---
title: "Job submission and management"
linkTitle: "Job submission and management"
weight: 6
description: >
  How to submit jobs to slurm?
---


## What is Slurm?/ Batch Queuing System Overview


## Job Submission Process


## Example Job Scripts


## Job Monitoring and Status Checking

### Handy commands:

`squeue`
`scancel`
`slurmtop` (specific to DAIC)

## Job prioritization and waiting times

### Fair tree fairshare

### Priority tiers
The partitions are tiered: the general partition is in the lowest priority tier, department partitions (insy, st) are in the middle priority tier, and partitions for specific groups (visionlab, wis) are in the highest priority tier.

When resources become available, the scheduler will first look for jobs in the highest priority partition that those resources are in, and start the highest (user)priority jobs that fit within the resources (if any). When resources remain, the scheduler will check the next lower priority tier, and so on. Finally, the scheduler will try to backfill lower (user)priority jobs that fit (if any).

The partition priorities have no impact on resources that are in use, so jobs have to wait until the resources become available.

A nice thing about Slurm is that you can specify multiple partitions for your job (--partition=wis,st,general) which should give the job the highest possible priority on the different partitions (resources) in the cluster, at no cost for yourself or others.


### Where to submit jobs?

The idea behind the tiering is to submit to all partitions, e.g. `--partition=st,general`, and let the scheduler figure out were the job can start the soonest. 


Resources of all partitions (eg, `st`) are also part of the `general` partition. Thus:
1. submitting to the  `general` partition allows jobs to use all nodes
2. submitting to those partitions alone, results in longer waiting times, since the `general` partition has much more resources, and the bigger the resource pool, the more chances a job has to be scheduled or back-filled
3. The optimal way is to submit to both `general` and specific partitions. This is to skip over higher-priority jobs that would otherwise get started first on resources that are also in the specific partition.





## Parllelizing jobs- 

### Job Arrays

https://blog.ronin.cloud/slurm-job-arrays/


### Working with dependencies

sbatch --dependency=type:job_id jobfile


https://bioinformaticsworkbook.org/Appendix/HPC/SLURM/submitting-dependency-jobs-using-slurm.html#gsc.tab=0

## Troubleshooting Common Issues - _Likely contains links to the Support area_