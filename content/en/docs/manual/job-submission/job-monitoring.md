---
title: "Monitoring jobs"
linkTitle: "Monitoring jobs"
weight: 25
description: >
  How to cancel/stop scheduled or running jobs?
---

* To check your job has actually been submitted:
```bash
$ squeue -u SomeNetID  # Replace SomeNetId with your NetID 
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
                 2   general  jobscip SomeNetI  R       0:01      1 insy15
```

* And to check the log of your job, use an editor or viewer of choice (eg, `vi`, `nano` or simply `cat`) to view the log:

```bash
$ cat slurm-2.out
JobId=2 JobName=jobscript.sbatch
   UserId=SomeNetId(123) GroupId=domain users(100513) MCS_label=N/A
   Priority=23909774 Nice=0 Account=ewi-insy QOS=short
   JobState=RUNNING Reason=None Dependency=(null)
   Requeue=0 Restarts=0 BatchFlag=1 Reboot=0 ExitCode=0:0
   DerivedExitCode=0:0
   RunTime=00:00:00 TimeLimit=00:01:00 TimeMin=N/A
   SubmitTime=2015-06-30T14:00:00 EligibleTime=2015-06-30T14:00:00
   AccrueTime=2015-06-30T14:00:00
   StartTime=2015-06-30T14:00:01 EndTime=2015-06-30T14:01:01 Deadline=N/A
   SuspendTime=None SecsPreSuspend=0 LastSchedEval=2015-06-30T14:01:01  Scheduler=Main
   Partition=general AllocNode:Sid=login1:2220
   ReqNodeList=(null) ExcNodeList=(null)
   NodeList=insy15
   BatchHost=insy15
   NumNodes=1 NumCPUs=2 NumTasks=1 CPUs/Task=2 ReqB:S:C:T=0:0:*:*
   TRES=cpu=2,mem=1G,node=1,billing=1
   Socks/Node=* NtasksPerN:B:S:C=0:0:*:* CoreSpec=*
   JOB_GRES=(null)
     Nodes=insy15 CPU_IDs=26-27 Mem=1024 GRES=
   MinCPUsNode=2 MinMemoryNode=1G MinTmpDiskNode=50M
   Features=(null) DelayBoot=00:00:00
   OverSubscribe=OK Contiguous=0 Licenses=(null) Network=(null)
   Command=/home/nfs/SomeNetId/jobscript.sbatch
   WorkDir=/home/nfs/SomeNetId
   StdErr=/home/nfs/SomeNetId/slurm_2.err
   StdIn=/dev/null
   StdOut=/home/nfs/SomeNetId/slurm_2.out
   Power=
   MailUser=SomeNetId@tudelft.nl MailType=END
```

## Checking slurm jobs

Sometimes, it may be desirable to inspect slurm jobs beyond their status in the queue. For example, to check which script was submitted, or how the resources were requested and allocated. Below are a few useful commands for this purpose:

* See job definition
```bash
$  scontrol show job 8580148
JobId=8580148 JobName=jobscript.sbatch
   UserId=SomeNetID(123) GroupId=domain users(100513) MCS_label=N/A
   Priority=23721804 Nice=0 Account=ewi-insy QOS=short
   JobState=RUNNING Reason=None Dependency=(null)
   Requeue=0 Restarts=0 BatchFlag=1 Reboot=0 ExitCode=0:0
   RunTime=00:00:12 TimeLimit=00:01:00 TimeMin=N/A
   SubmitTime=2023-07-10T06:41:57 EligibleTime=2023-07-10T06:41:57
   AccrueTime=2023-07-10T06:41:57
   StartTime=2023-07-10T06:41:58 EndTime=2023-07-10T06:42:58 Deadline=N/A
   SuspendTime=None SecsPreSuspend=0 LastSchedEval=2023-07-10T06:41:58 Scheduler=Main
   Partition=general AllocNode:Sid=login1:19162
   ReqNodeList=(null) ExcNodeList=(null)
   NodeList=awi18
   BatchHost=awi18
   NumNodes=1 NumCPUs=2 NumTasks=1 CPUs/Task=2 ReqB:S:C:T=0:0:*:*
   TRES=cpu=2,mem=1G,node=1,billing=1
   Socks/Node=* NtasksPerN:B:S:C=0:0:*:* CoreSpec=*
   MinCPUsNode=2 MinMemoryNode=1G MinTmpDiskNode=50M
   Features=(null) DelayBoot=00:00:00
   OverSubscribe=OK Contiguous=0 Licenses=(null) Network=(null)
   Command=/home/nfs/SomeNetID/jobscript.sbatch
   WorkDir=/home/nfs/SomeNetID
   StdErr=/home/nfs/SomeNetID/slurm_8580148.err
   StdIn=/dev/null
   StdOut=/home/nfs/SomeNetID/slurm_8580148.out
   Power=
   MailUser=SomeNetId@tudelft.nl MailType=END
   


```

* See statistics of a running job
```bash
$ sstat 1
  JobID  AveRSS  AveCPU  NTasks  AveDiskRead AveDiskWrite
------- ------- ------- ------- ------------ ------------
1.0        426K 00:00.0       1        0.52M        0.01M
```

* See accounting information of a finished job (also see --long option)
```bash
$ sacct -j 8580148
JobID           JobName  Partition    Account  AllocCPUS      State ExitCode 
------------ ---------- ---------- ---------- ---------- ---------- -------- 
8580148      jobscript+    general   ewi-insy          2  COMPLETED      0:0 
8580148.bat+      batch              ewi-insy          2  COMPLETED      0:0 
```
See overall job efficiency of a finished job

```bash
$ seff 8580148
Job ID: 8580148
Cluster: insy
User/Group: SomeNetID/domain users
State: COMPLETED (exit code 0)
Nodes: 1
Cores per node: 2
CPU Utilized: 00:00:00
CPU Efficiency: 0.00% of 00:01:00 core-walltime
Job Wall-clock time: 00:00:30
Memory Utilized: 340.00 KB
Memory Efficiency: 0.03% of 1.00 GB
```
