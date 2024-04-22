---
title: "Priorities and waiting times"
weight: 1
description: >
  How to submit jobs to slurm?
---

## Slurm's job scheduling and waiting times
When slurm is not configured for FIFO scheduling, jobs are prioritized in the following order:

1. Jobs that can preempt: _Not enabled in DAIC_
2. Jobs with an advanced reservation: _See {{< external-link "https://slurm.schedmd.com/reservations.html" "Slurm's Advanced Resource Reservation Guide" >}}_
3. Partition PriorityTier: _See [Priority tiers](#priority-tiers)_
4. Job priority: _See [Priority calculations](#priority-calculations) and [QoS priority](#qos-priority)_
6. Job ID


### Priority tiers
DAIC partitions are tiered: the `general` partition is in the lowest priority tier, department partitions (eg, `insy`, `st`) are in the middle priority tier, and partitions for specific groups (eg, `visionlab`, `wis`) are in the highest priority tier. Those partitions correspond to resources contributed by the respective groups or departments (see [Contributing departments](/docs/introduction)).

When resources become available, the scheduler will first look for jobs in the highest priority partition that those resources are in, and start the highest (user) priority jobs that fit within the resources (if any). When resources remain, the scheduler will check the next lower priority tier, and so on. Finally, the scheduler will try to backfill lower (user) priority jobs that fit (if any).

The partition priorities have no impact on resources that are in use, so jobs have to wait until the resources become available.

#### Where to submit jobs?
The idea behind the tiering is that you submit to all partitions, e.g. `--partition=wis,st,general`, and let the scheduler figure out where the job can start the soonest.  This should give the job the highest possible priority on the different partitions (resources) in the cluster, at no cost for yourself or others.

Resources of all partitions (eg, `st`) are also part of the `general` partition (see [Fig 1]({{< ref "fig:daic_partitions" >}})). Thus:
* submitting to the  `general` partition allows jobs to use all nodes
* submitting to group-specific partitions alone results in longer waiting times, since the `general` partition has much more resources than any of them (The bigger the resource pool, the more chances a job has to be scheduled or back-filled)
* The optimal way is to submit to both `general` and group-specific partitions when accessible. This is to skip over higher-priority jobs that would otherwise get started first on resources that are also in the specific partition.


### Priority calculations
Slurm continually calculates job priorities and schedules the execution of jobs based on its configurations. A few configuration parameters affect priority computations:

- `SchedulerType`: The type of scheduling used based on available resources, requested resources, and job priorities. On DAIC, slurm is used with `backfill` scheduling mechanism. This mechanism allows low priority jobs to _backfill_ idle resources if doing so does not delay the expected start time of any high priority job (based on resource availability).

{{% alert title="Tip" color="info" %}}
With `sched/backfil`, jobs can only be started when the resources that they request fit within the available idle resources. Thus:
- The fewer resources a job request, the higher the chance that it will fit within the available idle resources. 
- The more resources a job request, the long it will have to wait before enough resources become available to start.
To check how the cluster is configured, you may run:
```bash
$ scontrol show config | grep SchedulerType
SchedulerType           = sched/backfil
```  
More details is available in [Slurm's SchedulerType](https://slurm.schedmd.com/slurm.conf.html#OPT_SchedulerType)

{{% /alert %}}


- `PriorityType`: The way priority is computed. On DAIC, a `multifactor` computation is applied, where job priority _at any given time_ is a weighted sum of the following factors:
  - Fairshare: a measure of the amount of resources that a group (ie `account` in slurm terminology) has contributed, and the historical usage of the group and the user.
  - QOS: the quality of service associated with the job, which is specified with the slurm `--qos` directive  (see [QoS priority](#qos-priority)).

{{% alert title="Info" color="info" %}}
The whole idea behind the FairShare scheduling in DAIC is to share all the available resources fairly and efficiently with all users (instead of having strict limitations in the amount of resource use or in which hardware users can compute). The resources in the cluster are contributed in different amounts by different groups (see [Contributing departments](/docs/introduction)), and the scheduler makes sure that each group can use a _share_ of the resource relative to what the group contributed. 
To check how the cluster is configured you may run:

```bash
$ scontrol show config | grep PriorityType
PriorityType            = priority/multifactor
$ sprio --weights
          JOBID PARTITION   PRIORITY       SITE  FAIRSHARE        QOS
        Weights                               1   20000000   40000000
```
{{% /alert %}}



The following commands are useful for checking prioritization of your own jobs:

| Command | Purpose |
| ------- | ------- |
| `sprio -j <YourJobID>` | Determine the priority of your job |
| `squeue -j <YourJobID> --start` | Request your job’s estimated start time|
| `sshare -u <YourNetID>` | Determine your current fairshare value |


{{% alert title="Info" color="info" %}}
To get more complete priority configurations of a cluster, run the command:
```bash
$ scontrol show config | grep ^Priority
PriorityParameters      = (null)
PrioritySiteFactorParameters = (null)
PrioritySiteFactorPlugin = (null)
PriorityDecayHalfLife   = 2-00:00:00
PriorityCalcPeriod      = 00:05:00
PriorityFavorSmall      = No
PriorityFlags           = 
PriorityMaxAge          = 7-00:00:00
PriorityUsageResetPeriod = NONE
PriorityType            = priority/multifactor
PriorityWeightAge       = 0
PriorityWeightAssoc     = 0
PriorityWeightFairShare = 20000000
PriorityWeightJobSize   = 0
PriorityWeightPartition = 0
PriorityWeightQOS       = 40000000
PriorityWeightTRES      = (null)
```
{{% /alert %}}

### QoS priority 
The purpose of the (multiple) QoSs in DAIC is to optimize the throughput of the cluster and to reduce the waiting times for jobs:
* Long jobs block resources for a long time, thus leading to long waiting times and fragmentation of resources.
* Short jobs block resources only for short times, and can more easily fill in the gaps in the scheduling of resources (thus start sooner), and are therefore better for throughput and waiting times.

Thus, DAIC has the following policy:
* To stimulate short jobs, the `short` QoS has a higher priority, and allows you to use a larger part of all resources, than the `medium` and `long` QoS.
* To prevent long jobs from blocking all resources in the cluster for long times (thus causing long waiting times), only a certain part of all cluster resources is available to all running `long` QoS jobs (of all users) combined. 
* All running `medium` QoS jobs together can use a somewhat larger part of all resources in the cluster, and all running `short` QoS jobs combined are allowed to fill the biggest part of the cluster. 
  * These limits are called the _QoS group limits_.
  * When this limit is reached, no new jobs with this QoS can be started, until some of the running jobs with this QoS finish and release some resources. 
  * The scheduler will indicate this with the reason `QoS Group CPU/memory/GRES limit`.

* To prevent one user from single-handedly using all available resources in a certain QoS, there are also limits for the total resources that all running jobs of one user in a specific QoS can use. 
  * These are called the _QoS per-user limits_. 
  * When this limit is reached, no new jobs of this user with this QoS can be started, until some of the running jobs of this user and with this QoS finish and release some resources.
  * The scheduler will indicate this with the reason `QoS User CPU/memory/GRES limit`.

These per-group and per-user limits are set by the DAIC user board, and the scheduler strictly enforces these limits. Thus, no user can use more resources than the amount that was set by the user board. Any (perceived) imbalance in the use of resources by a certain QoS or user should not be held against a user or the scheduler, but should be discussed in the user board.

