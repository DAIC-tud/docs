---
title: "Partitions"
weight: 18
description: >
  How are partitions managed on DAIC?
---

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
