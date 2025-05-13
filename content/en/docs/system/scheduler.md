---
title: "Scheduler"
weight: 5
description: >
  What are the foundational components of DAIC?
---



## Workload scheduler
DAIC uses the {{< external-link "https://slurm.schedmd.com/" "Slurm scheduler" >}} to efficiently manage workloads. All jobs for the cluster have to be submitted as batch jobs into a queue. The scheduler then manages and prioritizes the jobs in the queue, allocates resources (CPUs, memory) for the jobs, executes the jobs and enforces the resource allocations. See [the job submission pages](/docs/manual/job-submission) for more information.

A slurm-based cluster is composed of a set of _login nodes_ that are used to access the cluster and submit computational jobs. A _central manager_ orchestrates computational demands across a set of _compute nodes_. These nodes are organized logically into groups called _partitions_, that defines job limits or access rights. The central manager provides fault-tolerant hierarchical communications, to ensure optimal and fair use  of available compute resources to eligible users, and make it easier to run and schedule complex jobs across compute resources (multiple nodes).


