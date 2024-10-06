---
title: "Quality of Service (QoS)"
weight: 15
description: >
  How to submit jobs to slurm?
---

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
