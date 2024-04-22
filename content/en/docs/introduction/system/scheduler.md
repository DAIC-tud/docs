---
title: "Scheduler"
weight: 5
description: >
  Description of the job-scheduling system.
---

{{% pageinfo %}}
At present [DAIC](https://daic.pages.ewi.tudelft.nl/docs/) and [DelftBlue](https://doc.dhpc.tudelft.nl/delftblue) have different software stacks. This pertains to the operating system (CentOS 7 _vs_ Red Hat Enterprise Linux 8, respectively) and, consequently, the available software. Please refer to the respective [DelftBlue modules](https://doc.dhpc.tudelft.nl/delftblue/DHPC-modules/) and [DAIC Available software](../../../manual/software/available-software) documentation before commencing your experiments.
{{% /pageinfo %}}



## Slurm Workload Manager

DAIC uses the {{< external-link "https://slurm.schedmd.com/" "Slurm scheduler" >}} to efficiently manage workloads. All jobs for the cluster have to be submitted as batch jobs into a queue. The scheduler then manages and prioritizes the jobs in the queue, allocates resources (CPUs, memory) for the jobs, executes the jobs and enforces the resource allocations. See [the scheduler pages](../../../manual/job-submission) for more information.

<!-- 

## Libraries for Specialized Hardware or Accelerators 

## Software Licensing and Restrictions

## Examples and Tutorials demonstrating the usage of specific software or libraries (eg, AI frameworks like TensorFlow or PyTorch, R scripts, .. etc) on different computing resources 
-->

### Batch Queuing System Overview

DAIC uses {{< external-link "https://slurm.schedmd.com/" "Slurm" >}} as a cluster management and job scheduling system to efficiently manage computational workloads across computing capacity. 

A slurm-based cluster is composed of a set of _login nodes_ that are used to access the cluster and submit computational jobs. A _central manager_ orchestrates computational demands across a set of _compute nodes_. These nodes are organized logically into groups called _partitions_, that defines job limits or access rights. The central manager provides fault-tolerant hierarchical communications, to ensure optimal and fair use  of available compute resources to eligible users, and make it easier to run and schedule complex jobs across compute resources (multiple nodes).


{{< figure src="/img/DAIC_partitions.png" caption="DAIC partitions and access/usage best practices" ref="fig:daic_partitions" width="750px">}}
