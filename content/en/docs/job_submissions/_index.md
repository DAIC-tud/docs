---
title: "Job submission and management"
linkTitle: "Job submission and management"
weight: 6
description: >
  How to submit jobs to slurm?
---


## Batch Queuing System Overview

DAIC uses [Slurm](https://slurm.schedmd.com/) as a cluster management and job scheduling system to efficiently manage computational workloads across computing capacity. 

A slurm-based cluster is composed of a set of _login nodes_ that are used to access the cluster and submit computational jobs. A _central manager_ orchestrates computational demands across a set of _compute nodes_.  This central manager provides fault-tolerant hierarchical communications, to ensure optimal and fair use  of available compute resources, and make it easier to run and schedule complex jobs across compute resources (multiple nodes).


{{< figure src="slurm_architecture.gif" caption=">Fig 1: Slurm components- adapted from [Slurm documentation](https://slurm.schedmd.com/overview.html)" >}}


## Partitions and Quality of Service

When you submit a job in a slurm-based system, it enters a queue waiting for resources.
The _partition_ and _Quality of Service(QoS)_ are the two job parameters slurm uses to assign resources for a job:
* The _partition_  determines access to groups of different compute nodes. 
* The _Quality of Service_ determines the priority as well as the run time, CPU, GPU and memory limits on the given partition. Jobs that exceed these limits are automatically terminated.

All nodes in DAIC are part of the `general` partition, but other partitions exist for prioritization purposes on select nodes (see [Priority tiers](#priority-tiers)). Table 1 shows the QoS limits on the `general` partition
<add table>


{{% alert title="Note" color="info" %}}

The priority of a job is a function of *both* QoS *and* previous usage (less is better). 

{{% /alert %}} 


<add figure showing available partitions/ Overall hardware architecture of DAIC system, see Kindratenko et al 2020>


## Slurm job's terminology: job, job step, task and CPUs

A slurm _job_ (submitted via `sbatch`) can consists of multiple _steps_ in series. Each _step_ (specified via `srun`) can run multiple _tasks (ie programs)_ in parallel. Each task gets its own set of CPUs. As an example, consider the workflow on the left, and corresponding breakdown in the right shown in fig 1

{{< figure src="slurm_job_terminology.png" caption=">Fig 1: Slurm job's terminology" >}}

In this example, note:
* When you explicitly request 1 CPU per task (`--cpus-per-task=1`), you should also explicitly specify the number of tasks (`--ntasks`). Otherwise, `srun` may start the task twice in parallel (because CPUs are allocated in multiples of 2)
* The default slurm allocation is a single task and single CPU (ie `--ntasks=1 --cpus-per-task=1`). Thus, it is not necessary to explicitly request these to run a single task on a single CPU.
* When using multiple tasks, specify `--mem-per-cpu`.


{{% alert title="Note" color="info" %}}

DAIC is dual-threaded. It means that CPUs are automatically allocated in multiples of 2. Thus, in your job use (a multiple of) 2 threads.
{{% /alert %}} 


## Creating Job Scripts

Job scripts are text files. The top of such files is a set of directives that specify the job resources request. The remainder is the code that needs to run. It could be a set of steps to run in series, or parallel tasks within these steps (see [Slurm job's terminology](#slurm-jobs-terminology-job-job-step-task-and-cpus)).


Fig 1 provides an example slurm job that can be used in DAIC, with explanations of the directives used. If not specified the job is submitted to the `general` partition with `short` QoS for 1 minute run time, 1 task 
partition=general , qos=short, 1 minute run time, 1 task, 2 cpus, 1 Gb of memory, no usage statistics, current directory


{{< figure src="slurm_script.png" caption=">Fig 1: Example slurm job on DAIC" >}}


```bash
#!/bin/sh

# You can control the resources and scheduling with '#SBATCH' settings
# (see 'man sbatch' for more information on setting these parameters)

# The default partition is the 'general' partition
#SBATCH --partition=general

# The default Quality of Service is the 'short' QoS (maximum run time: 4 hours)
#SBATCH --qos=short

# The default run (wall-clock) time is 1 minute
#SBATCH --time=0:01:00

# The default number of parallel tasks per job is 1
#SBATCH --ntasks=1

# The default number of CPUs per task is 1 (note: CPUs are always allocated to jobs per 2)
# Request 1 CPU per active thread of your program (assume 1 unless you specifically set this)
#SBATCH --cpus-per-task=2

# The default memory per node is 1024 megabytes (1GB) (for multiple tasks, specify --mem-per-cpu instead)
#SBATCH --mem=1024

# Set mail type to 'END' to receive a mail when the job finishes
# Do not enable mails when submitting large numbers (>20) of jobs at once
#SBATCH --mail-type=END

# Use this simple command to check that your sbatch settings are working
/usr/bin/scontrol show job -d "$SLURM_JOB_ID"

# Your job commands go below here

# Uncomment these lines and adapt them to load the software that your job requires
#module use /opt/insy/modulefiles
#module load matlab/R2020b

# Computations should be started with 'srun'. For example:
#srun python my_program.py

```



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


## Parallelizing jobs-  

### Job Arrays

https://blog.ronin.cloud/slurm-job-arrays/


### Working with dependencies

sbatch --dependency=type:job_id jobfile


https://bioinformaticsworkbook.org/Appendix/HPC/SLURM/submitting-dependency-jobs-using-slurm.html#gsc.tab=0

## Troubleshooting Common Issues - _Likely contains links to the Support area_