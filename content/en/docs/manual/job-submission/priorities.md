---
title: "Priorities, Partitions & Quality of Service"
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
DAIC partitions are tiered: 
- The `general` partition is in the _lowest priority tier_, 
- Department partitions (eg, `insy`, `st`) are in the _middle priority tier_, and 
- Partitions for specific groups (eg, `influence`, `mmll`) are in the _highest priority tier_. Those partitions correspond to resources contributed by the respective groups or departments (see [Contributing departments](/docs/introduction)).

When resources become available, the scheduler will first look for jobs in the highest priority partition that those resources are in, and start the highest (user) priority jobs that fit within the resources (if any). When resources remain, the scheduler will check the next lower priority tier, and so on. Finally, the scheduler will try to _backfill_ lower (user) priority jobs that fit (if any).

> The partition priorities have no impact on resources that are in use, so jobs have to wait until the resources become available.

#### Partition selection
The purpose of this tiering is to let you submit your jobs to _multiple partitions_ (e.g., `--partition=mml,insy,general`), allowing the scheduler to determine where the job can start the soonest. This ensures your job has the _highest possible priority_ across different partitions in the cluster, without negatively impacting your or others’ resource access.

Keep in mind that:
- Resources of all partitions (eg, `st`) are also part of the `general` partition (see [Fig 1]({{< ref "/docs/system#fig:daic_partitions" >}})). Thus:
  * Submitting to the  `general` partition _allows jobs to use all nodes_
  * Submitting to group-specific partitions _alone_ results in longer waiting times, since the `general` partition has much more resources than any of them (The bigger the resource pool, the more chances a job has to be scheduled or back-filled)
  * The _optimal strategy_ is to submit to _both_ `general` and group-specific partitions when accessible. This is to skip over higher-priority jobs that would otherwise get started first on resources that are also in the specific partition.
- You should __only submit jobs to partitions that your account has access to__. Submitting jobs to unauthorized partitions (e.g., using `--partition=insy,st` when your submitting account does not have access to both of these) will result in the job remaining in a pending state and generate excessive logging, potentially overloading the Slurm controller nodes.

{{% alert title="Warning" color="warning" %}}
Always ensure you are submitting jobs to partitions accessible by your account. You can check your account and partition permissions with the following commands- example output for a user is shown below:

```shell-session
$ sacctmgr show user "$USER" withassoc Format='DefaultAccount,Account' --parsable # Check your account(s)
Def Acct|Account|
ewi-insy-prb|ewi-st|
ewi-insy-prb|ewi-insy-prb|

$ echo "Partition   AllowAccounts"; scontrol show partition -a | \
> awk '
>     /PartitionName=/ {
>         split($1, a, "=");
>         partition = a[2]
>     } 
>     /AllowAccounts=/ {
>         split($2, b, "=");
>         print partition, b[2]
>     }
> ' | \
> grep -E 'ALL|ewi-insy-prb'      # Check paritions accessible to your *default* account
Partition   AllowAccounts
general ALL
insy ewi-insy,ewi-insy-cgv,ewi-insy-cys,ewi-insy-ii,ewi-insy-ii-influence,ewi-insy-mmc,ewi-insy-prb,ewi-insy-prb-dbl,ewi-insy-prb-prlab,ewi-insy-prb-spclab,ewi-insy-prb-visionlab,ewi-insy-reit,ewi-insy-sdm,ewi-insy-sup
```
This shows that the user can use the `ewi-insy-prb` or the `ewi-st` accounts.
The second command shows that all accounts can submit to the `general` partition and several accounts can submit to the `insy` partition.
**Replace the `ewi-insy-prb` in the grep line above to get the partition details for your specific account.**

For the example above note the following correct and incorrect examples:

{{% /alert %}}

{{< cardpane  >}}

{{< card code=true header="**Correct**: explicit _default_ account and partition specification" lang=bash >}}
#SBATCH --account=ewi-insy-prb
#SBATCH --partition=insy,general
{{< /card >}}

{{< card code=true header="**Correct**: Implicit _default_ account omitted since it has access to the specified patition" lang=bash >}}
#SBATCH --partition=insy,general
{{< /card >}}

{{< /cardpane >}}

{{< cardpane  >}}

{{< card code=true header="**Incorrect**: Multiple partitions with account mismatch" lang=bash >}}
#SBATCH --account=ewi-insy-prb
#SBATCH --partition=insy,st  
{{< /card >}}
{{< card code=true header="**Incorrect**: Specifying a wrong account for the partition" lang=bash >}}
#SBATCH --account=ewi-st
#SBATCH --partition=insy 
{{< /card >}}

{{< /cardpane >}}

{{% alert title="" color="warning" %}}
**Consequences:** Submitting jobs to unauthorized partitions may result in jobs remaining pending and could overload the system, leading to potential job cancellations without warning.
{{% /alert %}}



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

## Partitions


In SLURM, a partition is a scheduling construct that groups nodes or resources based on certain characteristics or policies. Partitions are used to organize and manage resources within a cluster, and they allow system administrators to control how jobs are allocated and executed on different nodes. 

### See partition definitions

On DAIC the `scontrol` command only shows you the general partitions. More partitions are available.

```bash
$ scontrol show partition
PartitionName=general
   AllowGroups=ALL AllowAccounts=ALL DenyQos=influence
   AllocNodes=login[1-3],oodtest Default=YES QoS=N/A
   DefaultTime=00:01:00 DisableRootJobs=NO ExclusiveUser=NO GraceTime=0 Hidden=NO
   MaxNodes=UNLIMITED MaxTime=UNLIMITED MinNodes=0 LLN=NO MaxCPUsPerNode=UNLIMITED
   Nodes=3dgi[1-2],100plus,awi[01-26],cor1,gpu[01-11],grs[1-4],influ[1-6],insy[11-16],tbm5,wis1
   PriorityJobFactor=1 PriorityTier=1 RootOnly=NO ReqResv=NO OverSubscribe=NO
   OverTimeLimit=NONE PreemptMode=OFF
   State=UP TotalCPUs=4064 TotalNodes=59 SelectTypeParameters=NONE
   JobDefaults=(null)
   DefMemPerNode=1024 MaxMemPerNode=UNLIMITED
   TRESBillingWeights=CPU=0.5,Mem=0.083333333G,GRES/gpu=16.0
```

## Quality of Service (QoS)


When you submit a job in a slurm-based system, it enters a queue waiting for resources.
The _partition_ and _Quality of Service(QoS)_ are the two job parameters slurm uses to assign resources for a job:
* The _partition_  is a set of compute nodes on which a job can be scheduled. In DAIC, the nodes contributed or funded by a certain group are lumped into a corresponding partition (see [Contributing departments](/docs/introduction#contributing-departments)). 
All nodes in DAIC are part of the `general` partition, but other partitions exist for prioritization purposes on select nodes (see [Priority tiers](/docs/manual/job-submission/priorities)).
* The _Quality of Service_ is a set of limits that controls what resources a job can use and, therefore, determines the priority level of a job. This includes the run time, CPU, GPU and memory limits on the given partition. Jobs that exceed these limits are automatically terminated (see [QoS priority](/docs/manual/job-submission/priorities#qos-priority)).

 For DAIC, Table 1 shows the QoS limits on the `general` partition.

<!------- Check that this content is true using:
sacctmgr list qos

# show every associations of every user.
# if user=username is passed, show only associations for the specific user username
# see "man sacctmgr" for more
function cri_show_assoc ()
{
    sacctmgr -p list associations $@ format=Account,User,Partition,Qos,DefaultQOS tree | column -ts'|'
}

$ cri_show_assoc user=u
Account  User  Partition  QOS            Def QOS
acc1     u     part1      q_acc1_part1     q_acc1_part1
acc1     u     part2      q_acc1_part2     q_acc1_part2
acc1     u     part3      q_acc1_part3     q_acc1_part3
acc1     u     part4      q_acc1_part4     q_acc1_part4
acc1     u     part5      q_acc1_part5     q_acc1_part5
acc1     u     part6      q_acc1_part6     q_acc1_part6
acc1     u     part7      q_acc1_part7     q_acc1_part7
acc1     u     part7      q_acc1_part7     q_acc1_part7
acc1     u     part8      q_acc1_part8     q_acc1_part8
acc1     u     part9      q_acc1_part9     q_acc1_part9
acc1     u     part10     q_acc1_part10    q_acc1_part10
acc1     u                q_acc1           q_acc1

# show every QoS definition
# if name=qosname is passed, show only the specific QoS qosname definition
# see "man sacctmgr" for more
function cri_show_qos ()
{
    sacctmgr -p list qos $@ format=Name,Priority,GraceTime,GrpTRES,GrpJobs,GrpSubmit,GrpSubmit,MaxTRES,MaxTRESPerUser,MaxJobsPU | column -ts'|'
}

$ cri_show_qos name=q_acc1
Name    Priority  GraceTime  GrpTRES  GrpJobs  GrpSubmit  MaxTRES  MaxTRESPU  MaxJobsPU
q_acc1  0         00:00:00                     2000                cpu=4200
------>

<div id=daicPartitionsQoS>
<table>
<caption> Table 1: The general partition and its operational and per-QoS per-user limits; specific groups use other partitions and QoS
</caption>
<tfoot><tr><td colspan="11"><font color="gray">
 *infinite QoS jobs will be killed when servers go down, eg, during maintenance. It is not recommended to submit jobs with this QoS.
</font></td></tr></tfoot>
<thead>
  <tr>
    <th rowspan="2">Partition</th>
    <th rowspan="2">QoS</th>
    <th rowspan="2">Priority</th>
    <th rowspan="2">Max run time</th>
    <th rowspan="2">Jobs per user</th>
    <th colspan="2">CPU limits</th>
    <th colspan="2">GPU limits</th>
    <th colspan="2">Memory limits</th>
  </tr>
  <tr>
    <th>Per QoS</th>
    <th>Per user</th>
    <th>Per QoS</th>
    <th>Per user</th>
    <th>Per QoS</th>
    <th>Per User</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td rowspan="5">general</td>
    <td>interactive</td>
    <td>high</td>
    <td>1 hour</td>
    <td>1 running</td>
    <td>-</td>
    <td>2</td>
    <td>-</td>
    <td>2</td>
    <td>-</td>
    <td>16G</td>
  </tr>
  <tr>
    <td>short</td>
    <td>normal</td>
    <td>4 hours</td>
    <td>10000</td>
    <td>3672 (85%)</td>
    <td>2160 (50%)</td>
    <td>109 (85%)</td>
    <td>64 (50%)</td>
    <td>23159G (85%)</td>
    <td>13623G (50%)</td>
  </tr>
  <tr>
    <td>medium</td>
    <td>medium</td>
    <td>1 ½ day</td>
    <td>2000</td>
    <td>3456 (80%)</td>
    <td>1512 (35%)</td>
    <td>103 (80%)</td>
    <td>45 (35%)</td>
    <td>21796G (80%)</td>
    <td>9536G (35%)</td>
  </tr>
  <tr>
    <td>long</td>
    <td>low</td>
    <td>7 days</td>
    <td>1000</td>
    <td>3240 (75%)</td>
    <td>864 (20%)</td>
    <td>96 (75%)</td>
    <td>25 (20%)</td>
    <td>20434G (75%)</td>
    <td>5449G (20%)</td>
  </tr>
  <tr>
    <td>infinite*</td>
    <td>none</td>
    <td>infinite</td>
    <td>1 running</td>
    <td>32</td>
    <td>-</td>
    <td>2</td>
    <td>-</td>
    <td>250G</td>
    <td>-</td>
  </tr>
</tbody>
</table>
</div>

{{% alert title="Note" color="info" %}}

The priority of a job is a function of *both* QoS *and* previous usage (less is better). 
Read [Priority and waiting times](/docs/manual/job-submission/priorities) for more information.

{{% /alert %}} 

### See Quality of Service definitions

On DAIC you can check the QoS policies with the `sacctmgr` command:

```bash
$ sacctmgr list qos
      Name   Priority  GraceTime    Preempt   PreemptExemptTime PreemptMode                                    Flags UsageThres UsageFactor       GrpTRES   GrpTRESMins GrpTRESRunMin GrpJobs GrpSubmit     GrpWall       MaxTRES MaxTRESPerNode   MaxTRESMins     MaxWall     MaxTRESPU MaxJobsPU MaxSubmitPU     MaxTRESPA MaxJobsPA MaxSubmitPA       MinTRES 
---------- ---------- ---------- ---------- ------------------- ----------- ---------------------------------------- ---------- ----------- ------------- ------------- ------------- ------- --------- ----------- ------------- -------------- ------------- ----------- ------------- --------- ----------- ------------- --------- ----------- ------------- 
    normal          0   00:00:00                                    cluster                              DenyOnLimit               1.000000                                                                                                                                                                                                                cpu=1 
     short         50   00:00:00                                    cluster                              DenyOnLimit               1.000000 cpu=3562,gre+                                         65536                                                           04:00:00 cpu=2096,gre+                 10000                                      cpu=1,mem=1M 
      long         25   00:00:00                                    cluster                              DenyOnLimit               1.000000 cpu=3144,gre+                                         65536                                                         7-00:00:00 cpu=838,gres+                  1000                                      cpu=1,mem=1M 
  infinite          0   00:00:00                                    cluster                              DenyOnLimit               1.000000 cpu=32,gres/+                                         65536                                                                                          1         100                                      cpu=1,mem=1M 
interacti+        100   00:00:00                                    cluster                              DenyOnLimit               2.000000                                                       65536                                                           01:00:00 cpu=2,gres/g+         1           1                                      cpu=1,mem=1M 
   student         10   00:00:00                                    cluster                              DenyOnLimit               1.000000 cpu=192,gres+                                         65536                                                           04:00:00 cpu=2,gres/g+         1         100                                      cpu=1,mem=1M 
reservati+        100   00:00:00                                    cluster          DenyOnLimit,RequiresReservation               1.000000                                                       65536                                                                                                  10000                                      cpu=1,mem=1M 
 influence        100   00:00:00                                    cluster                              DenyOnLimit               1.000000                                                       65536                                                                                                  10000                                      cpu=1,mem=1M 
guest-sho+         10   00:00:00                                    cluster                              DenyOnLimit               1.000000 cpu=200,gres+                                         65536                                                           04:00:00 cpu=128,gres+                   100                                      cpu=1,mem=1M 
guest-long          0   00:00:00                                    cluster                              DenyOnLimit               1.000000 cpu=200,gres+                                         65536                                                         7-00:00:00 cpu=128,gres+         1          10                                      cpu=1,mem=1M 
    medium         35   00:00:00                                    cluster                              DenyOnLimit               1.000000 cpu=3352,gre+                                         65536                                                         1-12:00:00 cpu=1466,gre+                  2000                                      cpu=1,mem=1M 
```

### How to use QoS in your `sbatch` scripts?

In your `sbatch.slurm` script you can specify the QoS with `#SBATCH --qos=...` option.

**Example:**
```
#!/bin/bash
#SBATCH --job-name=hello-world
#SBATCH --partition=general
#SBATCH --account=ewi-insy-reit
#SBATCH --qos=short               # This is how you specify QoS
#SBATCH --time=0:01:00     
#SBATCH --nodes=1        
#SBATCH --tasks-per-node=1        
#SBATCH --cpus-per-task=2        
#SBATCH --mem=1GB                
#SBATCH --output=slurm-%n-%j.out  
#SBATCH --error=slurm-%n-%j.err

srun echo 'Hi, from Slurm!'
sleep 30  # Wait for 30 seconds before exiting.
```

### QoS for reservations

In case you have a reservation you need to specify `--qos=reservation` and `--reservation=<reservation-name>. You can find an example [here](../reservations#using-reservations). 


## Resources reservations
Slurm gives the possibility to reserve one or more compute nodes _exclusively_ for a specific user or group of users. A reservation ensures that the designated node (or nodes) are dedicated solely to the reservation holder's tasks and are not shared with other users during the reserved period. This feature allows users to plan the execution of future workloads, and accommodates cluster users with special needs beyond the batch system (eg latency measurement scenarios).

{{% alert title="Note" color="warning" %}}
Using reservations is in line with the [General cluster usage clauses](/docs/policies#general-cluster-usage) of DAIC users' agreement. However, please be mindful that reservations are intended to facilitate special needs that cannot be satisfied by the batch system, and should not be requested to guarantee fast throughput for production runs.
{{% /alert %}}

### Requesting a Reservation
To request a reservation for nodes, please use to the [Request Reservation form](https://tudelft.topdesk.net/tas/public/ssp/content/detail/service?unid=c6d0e44564b946eaa049898ffd4e6938&from=d75e860b-7825-4711-8225-8754895b3507). You can request a reservation for an entire compute node (or a group of nodes)  **if you have contributed this (or these) nodes to the cluster and you have special needs that needs to be accommodated**.

General guidelines for reservations' requests:
* You can be granted a reservation *only* on nodes from a partition that is contributed by your group (See [Partitions](/docs/manual/job-submission/partitions) to check the name of the partition contributed by your group, and [System specifications](/docs/system/) for a listing of available nodes and their features).
* Please ask for the least amount of resources you need as to minimize impact on other users.
* _Plan ahead and request your reservation as soon as possible_: Reservations usually ignore running jobs, so any running job on the machine(s) you request will continue to run when the reservation starts. While jobs from other users will not start on the reserved node(s), the resources in use by an already running job at the start time of the reservation will not be available in the reservation until this running job ends. The earlier ahead you request resources, the easier it is to allocate the requested resources.

### Using reservations
Once your reservation request is approved and a reservation is placed on the system, you can run your jobs in the reservation by specifying  `--qos=reservation` along with the following directives to your slurm commands: `--reservation=<name>` and `--partition=<partition>`. For example, to submit the job `job.sbatch` to a reservation named `icra_iv` on the `cor1` node on the `cor` partition use:

```bash
$ sbatch --qos=reservation --reservation=icra_iv --partition=cor job.sbatch
```

Alternatively, it is possible to add the following lines to the `job.sbatch` file, and submitting this file as usual:

```bash
#SBATCH --qos=reservation
#SBATCH --reservation=icra_iv
#SBATCH --partition=cor
```


{{% alert title="Note" color="info" %}}
It is possible to submit jobs to a reservation once it is created. Jobs will start immediately when the reservation is available, but already running jobs on resources will not be canceled for the reservation to start.
{{% /alert %}}


{{% alert title="Note" color="warning" %}}
When a reservation is used to run your jobs, remember to also pass the reservation parameters to your srun steps:

```bash
$ srun --qos=reservation --reservation=<reservation_name> --partition=<partition_name> <some_script.sh>
```
{{% /alert%}}

To make use of an existing reservation you have to specify `--qos=reservation` and `--reservation=<reservation-name>` in your `sbatch` script.


### Viewing reservations
To view all active and future reservations run the `scontrol` command as follows:

```bash
$ scontrol show reservations
ReservationName=icra_iv StartTime=2023-09-09T00:00:00 EndTime=2023-09-16T00:00:00 Duration=7-00:00:00
   Nodes=cor1 NodeCnt=1 CoreCnt=32 Features=(null) PartitionName=cor Flags=
   TRES=cpu=64
   Users=(null) Groups=(null) Accounts=3me-cor Licenses=(null) State=ACTIVE BurstBuffer=(null) Watts=n/a
   MaxStartDelay=(null)

ReservationName=maintenance weekend 2023-10-14 StartTime=2023-10-13T20:00:00 EndTime=2023-10-16T09:00:00 Duration=2-13:00:00
   Nodes=3dgi[1-2],100plus,awi[01-26],cor1,gpu[01-11],grs[1-4],influ[1-6],insy[11-12,14-16],tbm5,wis1 NodeCnt=58 CoreCnt=2000 Features=(null) PartitionName=(null) Flags=MAINT,IGNORE_JOBS,SPEC_NODES,ALL_NODES
   TRES=cpu=4000
   Users=root Groups=(null) Accounts=(null) Licenses=(null) State=INACTIVE BurstBuffer=(null) Watts=n/a
   MaxStartDelay=(null)
```

{{%alert title="Note" color="info"%}}
* Jobs can run on a reservation only if explicitly requested as shown in the [Requesting a reservation section](#requesting-a-reservation).
* Only jobs from the `Users` or `Accounts` associated with the reservation (as shown in the `scontrol show reservations` output) will be run on the reservation
* `STATE` of a reservation will show as `ACTIVE` (instead of `INACTIVE`) during the reservation window.
{{%/alert%}}


<!--

### Ending a reservation¶

All running jobs under a reservation will be terminated when the reservation ends. There are two ways to end a reservation earlier than scheduled:

    When requesting the reservation, you can ask us to activate a setting that will terminate the reservation a few minutes after all jobs in the reservation queue have completed.

    If your reservation does not have the above setting and you complete all planned computations before the reservation ends, please call NERSC operations at 1-800-666-3772 (or 1-510-486-8600) menu option 1 to cancel the reservation.

-->

