---
title: "Job submission and management"
linkTitle: "Job submission and management"
weight: 6
description: >
  How to submit jobs to slurm?
---


## Batch Queuing System Overview

DAIC uses {{< external-link "https://slurm.schedmd.com/" "Slurm" >}} as a cluster management and job scheduling system to efficiently manage computational workloads across computing capacity. 

A slurm-based cluster is composed of a set of _login nodes_ that are used to access the cluster and submit computational jobs. A _central manager_ orchestrates computational demands across a set of _compute nodes_. These nodes are organized logically into groups called _partitions_, that defines job limits or access rights. The central manager provides fault-tolerant hierarchical communications, to ensure optimal and fair use  of available compute resources to eligible users, and make it easier to run and schedule complex jobs across compute resources (multiple nodes).


{{< figure src="DAIC_partitions.png" caption="DAIC partitions and access/usage best practices" ref="fig:daic_partitions">}}



## Partitions and Quality of Service

When you submit a job in a slurm-based system, it enters a queue waiting for resources.
The _partition_ and _Quality of Service(QoS)_ are the two job parameters slurm uses to assign resources for a job:
* The _partition_  is a set of compute nodes on which a job can be scheduled. In DAIC, the nodes contributed or funded by a certain group are lumped into a corresponding partition (see [Brief history of DAIC](../intro_daic/#brief-history-of-daic)). 
All nodes in DAIC are part of the `general` partition, but other partitions exist for prioritization purposes on select nodes (see [Priority tiers](#priority-tiers)).
* The _Quality of Service_ is a set of limits that controls what resources a job can use and, therefore, determines the priority level of a job. This includes the run time, CPU, GPU and memory limits on the given partition. Jobs that exceed these limits are automatically terminated (see [QoS priority](#qos-priority)).

 For DAIC, Table 1 shows the QoS limits on the `general` partition.

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

The priority of a job is a function of *both* QoS *and* previous usage (less is better). See [Job prioritization and waiting times ](#slurms-job-scheduling-and-waiting-times)

{{% /alert %}} 



## Slurm job's terminology: job, job step, task and CPUs

A slurm _job_ (submitted via `sbatch`) can consists of multiple _steps_ in series. Each _step_ (specified via `srun`) can run multiple _tasks (ie programs)_ in parallel. Each task gets its own set of CPUs. As an example, consider the workflow and corresponding breakdown shown in fig 2.

{{< figure src="slurm_job_terminology.png" caption="Slurm job's terminology" >}}

In this example, note:
* When you explicitly request 1 CPU per task (`--cpus-per-task=1`), you should also explicitly specify the number of tasks (`--ntasks`). Otherwise, `srun` may start the task twice in parallel (because CPUs are allocated in multiples of 2)
* The default slurm allocation is a single task and single CPU (ie `--ntasks=1 --cpus-per-task=1`). Thus, it is not necessary to explicitly request these to run a single task on a single CPU.
* When using multiple tasks, specify `--mem-per-cpu`.


{{% alert title="Note" color="info" %}}
DAIC is dual-threaded. It means that CPUs are automatically allocated in multiples of 2. Thus, in your job use (a multiple of) 2 threads.
{{% /alert %}} 


## Job Scripts

Job scripts are text files, where the header set of directives that specify compute resources, and the remainder is the code that needs to run. All resources and scheduling are specified in the header as `#SBATCH` directives (see `man sbatch` for more information). Code could be a set of steps to run in series, or parallel tasks within these steps (see [Slurm job's terminology](#slurm-jobs-terminology-job-job-step-task-and-cpus)).

The code snippet below is a template script that can be customized to run jobs on DAIC. 
A useful tool that can be used to streamline the debugging of such scripts is {{< external-link "https://www.shellcheck.net/" "ShellCheck" >}}.


```bash
#!/bin/sh
#SBATCH --partition=general # Request partition. Default is 'general' 
#SBATCH --qos=short         # Request Quality of Service. Default is 'short' (maximum run time: 4 hours)
#SBATCH --time=0:01:00      # Request run time (wall-clock). Default is 1 minute
#SBATCH --ntasks=1          # Request number of parallel tasks per job. Default is 1
#SBATCH --cpus-per-task=2   # Request number of CPUs (threads) per task. Default is 1 (note: CPUs are always allocated to jobs per 2).
#SBATCH --mem=1024          # Request memory (MB) per node. Default is 1024MB (1GB). For multiple tasks, specify --mem-per-cpu instead
#SBATCH --mail-type=END     # Set mail type to 'END' to receive a mail when the job finishes. 
#SBATCH --output=slurm_%j.out # Set name of output log. %j is the Slurm jobId
#SBATCH --error=slurm_%j.err # Set name of error log. %j is the Slurm jobId

/usr/bin/scontrol show job -d "$SLURM_JOB_ID"  # check sbatch directives are working

# Remaining job commands go below here. For example, to run a Matlab script named "matlab_script.m", uncomment:
#module use /opt/insy/modulefiles # Use DAIC INSY software collection
#module load matlab/R2020b        # Load Matlab 2020b version
#srun matlab < matlab_script.m # Computations should be started with 'srun'.

```


{{% alert title="Note" color="info" %}}
* DAIC is dual-threaded. It means that CPUs are automatically allocated in multiples of 2. Thus, in your job use (a multiple of) 2 threads.
* Do not enable mails when submitting large numbers (>20) of jobs at once
{{% /alert %}} 



### Job submission and monitoring

Once a job script (see [Job script](#job-scripts)) is ready, it is time to send it to the cluster and start computing (see [Data transfer methods](../filesystem/#data-transfer-methods)). 

{{% alert title="Hint" color="info"%}}
To check whether you are working on your machine or the cluster, observe the output of the `hostname` command. The following examples show various outputs depending on where the command was ran from:
```bash
$ hostname 
login1.hpc.tudelft.nl # You are in a DAIC login1 node
$
$ hostname 
grs1.hpc.tudelft.nl   # You are in the DAIC compute node named grs1
$
$ hostname 
<YourNetID>           # You are in your TU Delft laptop/PC
```
{{% /alert %}}

To submit a job script `jobscript.sbatch`, login to DAIC, and:

* To only test:

```bash
$ sbatch --test-only jobscript.sbatch
Job 1 to start at 2015-06-30T14:00:00 using 2 processors on nodes insy15 in partition general
```

* To actually submit the job and do the computations:

```bash
$ sbatch jobscript.sbatch
Submitted batch job 2
```

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

* And finally, to cancel a given job:

```bash
$ scancel <jobID>
```

{{% alert title="Note" color="warning"%}}
It is possible to specify the `sbatch` directives, like `--mem`, `--ntasks`, ... etc in the command line as in:
```bash
$ sbatch --time=00:02:00 jobscript.sbatch
```
This specification is generally not recommended for production, as it is less reproducible than specifying within the job script itself.
{{% /alert %}}


### Interactive jobs on compute nodes

To work interactively on a node, eg, to debug a running code, or test on a GPU, start an interactive session using `sinteractve <compute requirements>`. If no parameters were provided, the default are applied. `<compute requirement>` can be specified the same way as sbatch directives within an sbatch script (see [Job scripts](#job-scripts)), as in the examples below:

```bash
$ hostname # check you are in one of the login nodes
login1.hpc.tudelft.nl
$ sinteractive 
 16:07:20 up 12 days, 4:09, 2 users, load average: 7.06, 7.04, 7.12
$ hostname # check you are in a compute node
insy15
$ squeue -u SomeNetID  # Replace SomeNetId with your NetID 
JOBID PARTITION  NAME     USER ST  TIME  NODES NODELIST(REASON)
    2   general  bash SomeNetI  R  1:23      1 insy15  
$ logout # exit the interactive job
```

To request a node with certain compute requirements:
```bash
$ sinteractive --ntasks=1 --cpus-per-task=2 --mem=4096
 16:07:20 up 12 days, 4:09, 2 users, load average: 7.06, 7.04, 7.12
```

{{% alert title="Warning" color="warning"%}}
When you logout from an interactive session, all running processes will be terminated
{{% /alert %}}


{{% alert title="Note" color="warning"%}}
Requesting interactive sessions is subject to the same resource availability constraints as submitting an sbatch script. It means you may need to wait until resources are available as you would when you submit an sbatch script
{{% /alert %}}


### Jobs on GPU resources

Some DAIC nodes have GPUs of different types, that can be used for various compute purposes (see [DAIC GPUs](../intro_daic/hardware_infra#gpus)).


To request a gpu for a job, use the sbatch directive `--gres=gpu[:type][:number]`, where the optional `[:type]` and `[:number]` specify the type and number of the GPUs requested, as in the examples below:
{{< figure src="slurm_request_gpus.png" caption="Slurm directives to request gpus for a job" >}}



{{% alert title="Note" color="warning"%}}
For CUDA programs, first, load the needed modules (CUDA, cuDNN) before running your code. See [Environment modules](../software_environment/available_software/#environment-modules)
{{% /alert %}}


An example batch script with GPU resources

```bash
#!/bin/sh
#SBATCH --partition=general # Request partition. Default is 'general' 
#SBATCH --qos=short         # Request Quality of Service. Default is 'short' (maximum run time: 4 hours)
#SBATCH --time=0:01:00      # Request run time (wall-clock). Default is 1 minute
#SBATCH --ntasks=1          # Request number of parallel tasks per job. Default is 1
#SBATCH --cpus-per-task=2   # Request number of CPUs (threads) per task. Default is 1 (note: CPUs are always allocated to jobs per 2).
#SBATCH --mem=1024          # Request memory (MB) per node. Default is 1024MB (1GB). For multiple tasks, specify --mem-per-cpu instead
#SBATCH --mail-type=END     # Set mail type to 'END' to receive a mail when the job finishes. 
#SBATCH --output=slurm_%j.out # Set name of output log. %j is the Slurm jobId
#SBATCH --error=slurm_%j.err # Set name of error log. %j is the Slurm jobId

#SBATCH --gres=gpu:1 # Request 1 GPU

# Measure GPU usage of your job (initialization)
previous=$(/usr/bin/nvidia-smi --query-accounted-apps='gpu_utilization,mem_utilization,max_memory_usage,time' --format='csv' | /usr/bin/tail -n '+2') 

/usr/bin/nvidia-smi # Check sbatch settings are working (it should show the GPU that you requested)

# Remaining job commands go below here. For example, to run python code that makes use of GPU resources:

# Uncomment these lines and adapt them to load the software that your job requires
#module use /opt/insy/modulefiles          # Use DAIC INSY software collection
#module load cuda/11.2 cudnn/11.2-8.1.1.33 # Load certain versions of cuda and cudnn 
#srun python my_program.py # Computations should be started with 'srun'. For example:

# Measure GPU usage of your job (result)
/usr/bin/nvidia-smi --query-accounted-apps='gpu_utilization,mem_utilization,max_memory_usage,time' --format='csv' | /usr/bin/grep -v -F "$previous"

```

Similarly, to interactively work in a GPU node:
```bash
$ hostname # check you are in one of the login nodes
login1.hpc.tudelft.nl
$
$ sinteractive --cpus-per-task=1 --mem=500 --time=00:01:00 --gres=gpu:v100:1
Note: interactive sessions are automatically terminated when they reach their time limit (1 hour)!
srun: job 8607665 queued and waiting for resources
srun: job 8607665 has been allocated resources
 15:27:18 up 51 days,  3:04,  0 users,  load average: 62,09, 59,43, 44,04
SomeNetID@insy11:~$
SomeNetID@insy11:~$ hostname # check you are in one of the compute nodes
insy11.hpc.tudelft.nl
SomeNetID@insy11:~$
SomeNetID@insy11:~$ nvidia-smi # check characteristics of GPU
Mon Jul 24 15:37:01 2023       
+---------------------------------------------------------------------------------------+
| NVIDIA-SMI 530.30.02              Driver Version: 530.30.02    CUDA Version: 12.1     |
|-----------------------------------------+----------------------+----------------------+
| GPU  Name                  Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf            Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                                         |                      |               MIG M. |
|=========================================+======================+======================|
|   0  Tesla V100-SXM2-32GB            On | 00000000:88:00.0 Off |                    0 |
| N/A   32C    P0               40W / 300W|      0MiB / 32768MiB |      0%      Default |
|                                         |                      |                  N/A |
+-----------------------------------------+----------------------+----------------------+
                                                                                         
+---------------------------------------------------------------------------------------+
| Processes:                                                                            |
|  GPU   GI   CI        PID   Type   Process name                            GPU Memory |
|        ID   ID                                                             Usage      |
|=======================================================================================|
|  No running processes found                                                           |
+---------------------------------------------------------------------------------------+
SomeNetID@insy11:~$
SomeNetID@insy11:~$ exit # exit the interactive session
```


### Deploying dependent jobs (job chains)

In certain scenarios, it might be desirable to condition the execution of a certain job on the status of another job. In such cases, the sbatch directive `--dependency=<condition>:<jobID>` can be used, where `<condition>` specifies the type of dependency (See table 2), and `<jobID>` is the slurm jobID upon which dependency is based. To specify more than one dependency, the `,` separator is used to indicate that all dependencies must be specified, and, `?` is used denotes that any dependency may be satisfied.

For example, assume the slurm job scripts, `job_1.sbatch`, ... `job_3.sbatch` need to run sequentially one after the other. To start this chain, submit the first job and obtain its jobID:

```bash
$ sbatch job_1.sbatch
Submitted batch job 8580135
```

Next, submit the second job to run only if the first job is successful:

```bash
$ sbatch --dependency=afterok:8580135 job_2.sbatch
Submitted batch job 8580136
```
{{% alert title="Note" color="warning"%}}
Note that if the first job (with jobID `8580135` in the example) fails, the second job (with jobID `8580136`) will not run, but it will remain in the queue. You have to use `scancel 8580136` to cancel this job
{{% /alert %}}


And, now, to run the third job only after the first two jobs have both run successfully:

```bash
$ sbatch --dependency=afterok:8580135,8580136 job_3.sbatch
Submitted batch job 8580140
```

Alternatively, if the third job is dependent on either job running successfully:
```bash
$ sbatch --dependency=afterok:8580135?8580136 job_3.sbatch
Submitted batch job 8580141
```



{{% alert title="Warning" color="warning"%}}
* If the jobs within a chain involve copying data files to a local disk (`/tmp`) on a node, you need to make sure all jobs use the same node (`--nodelist=<node>`, for example `--nodelist=insy15`)
{{% /alert %}}


<table>
<caption> Table 2: Possible sbatch dependency conditions
</caption>
<thead>
  <tr>
    <th>Argument</th>
    <th>Description</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>after</td>
    <td>This job can begin execution after the specified jobs have begun execution</td>
  </tr>
  <tr>
    <td>afterany</td>
    <td>This job can begin execution after the specified jobs have terminated.</td>
  </tr>
  <tr>
    <td>aftercorr</td>
    <td>A task of this job array can begin execution after the corresponding task ID in the specified job has completed successfully</td>
  </tr>
  <tr>
    <td>afternotok</td>
    <td>This job can begin execution after the specified jobs have terminated in some failed state</td>
  </tr>
  <tr>
    <td>afterok</td>
    <td>This job can begin execution after the specified jobs have successfully executed</td>
  </tr>
  <tr>
    <td>singleton</td>
    <td>This job can begin execution after any previously launched jobs sharing the same job name and user have terminated</td>
  </tr>
</tbody>
</table>



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

* See partition definitions
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
* See Quality of Service definitions

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

## Slurm's job scheduling and waiting times

When slurm is not configured for FIFO scheduling, jobs are prioritized in the following order:

1. Jobs that can preempt: _Not enabled in DAIC_
2. Jobs with an advanced reservation: _See {{< external-link "https://slurm.schedmd.com/reservations.html" "Slurm's Advanced Resource Reservation Guide" >}}_
3. Partition PriorityTier: _See [Priority tiers](#priority-tiers)_
4. Job priority: _See [Priority calculations](#priority-calculations) and [QoS priority](#qos-priority)_
6. Job ID


### Priority tiers
DAIC partitions are tiered: the `general` partition is in the lowest priority tier, department partitions (eg, `insy`, `st`) are in the middle priority tier, and partitions for specific groups (eg, `visionlab`, `wis`) are in the highest priority tier. Those partitions correspond to resources contributed by the respective groups or departments (see [Brief history of DAIC](../intro_daic/#brief-history-of-daic)).

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
The whole idea behind the FairShare scheduling in DAIC is to share all the available resources fairly and efficiently with all users (instead of having strict limitations in the amount of resource use or in which hardware users can compute). The resources in the cluster are contributed in different amounts by different groups (see [Brief history of DAIC](../intro_daic/#brief-history-of-daic)), and the scheduler makes sure that each group can use a _share_ of the resource relative to what the group contributed. 
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


These per-group and per-user limits (see [Table 1](#daicPartitionsQoS)) are set by the DAIC user board, and the scheduler strictly enforces these limits. Thus, no user can use more resources than the amount that was set by the user board. Any (perceived) imbalance in the use of resources by a certain QoS or user should not be held against a user or the scheduler, but should be discussed in the user board.


## Resources reservations

Slurm gives the possibility to reserve one or more compute nodes _exclusively_ for a specific user or group of users. A reservation ensures that the designated node (or nodes) are dedicated solely to the reservation holder's tasks and are not shared with other users during the reserved period. This feature allows users to plan the execution of future workloads, and accommodates cluster users with special needs beyond the batch system (eg latency measurement scenarios).

{{% alert title="Note" color="warning" %}}
Using reservations is in line with the [General cluster usage clauses](../intro_daic/user_agreement#general-cluster-usage) of DAIC users' agreement. However, please be mindful that reservations are intended to facilitate special needs that cannot be satisfied by the batch system, and should not be requested to guarantee fast throughput for production runs.
{{% /alert %}}

### Requesting a Reservation

To request a reservation for nodes, please use to the [Request Reservation form](../intro_daic/access_accounts). You can request a reservation for an entire compute node (or a group of nodes)  **if you have contributed this (or these) nodes to the cluster and you have special needs that needs to be accommodated**.

General guidelines for reservations' requests:
* You can be granted a reservation *only* on nodes from a partition that is contributed by your group (See [DAIC partitions and contributors page](../intro_daic/#brief-history-of-daic) to check the name of the partition contributed by your group, and [the DAIC hardware page](../intro_daic/hardware_infra/) for a listing of available nodes and their features).
* Please ask for the least amount of resources you need as to minimize impact on other users.
* _Plan ahead and request your reservation as soon as possible_: Reservations usually ignore running jobs, so any running job on the machine(s) you request will continue to run when the reservation starts. While jobs from other users will not start on the reserved node(s), the resources in use by an already running job at the start time of the reservation will not be available in the reservation until this running job ends. The earlier ahead you request resources, the easier it is to allocate the requested resources .


### Using a reservation


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


## Parallelizing jobs with Job Arrays

There can be scenarios, eg in simulations or benchmarking, where a job script needs to run many times with only different parameter set each time. If done manually, keeping track of the parameter values and corresponding jobIds is cumbersome. _Job Arrays_ are a convenient mechanism for submitting and managing such jobs. 

A job array is created by adding the `--array=<indexes>` directive to an sbatch script (or in the command line), where `<indexes>` can be either a comma separated list of integers, or a range with optional step size, eg, `1-10:2`. The minimum index value is 0, and the maximum is a Slurm configuration parameter (`MaxArraySize - 1`).

Within a job array, all jobs have the same `SLURM_ARRAY_JOB_ID`, but each job will have its own environment variable `SLURM_ARRAY_TASK_ID` that corresponds to the array index value. Additionally, all jobs in the array inherit the same compute resources requirements. In the following examples, arrays of size 2 are created, but with different indexes:


```bash
$ sbatch --array=1,4 jobscript.sbatch # Indexes specified as a list, and have values 1 and 4
Submitted batch job 8580151
$
$ squeue -u SomeNetID  # Replace SomeNetId with your NetID 
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
         8580151_1   general jobscrip SomeNetID  R       0:01      1 grs4
         8580151_4   general jobscrip SomeNetID  R       0:01      1 awi18
```


```bash
$ sbatch --array=1-2 jobscript.sbatch  # Range specified with default step size = 1. Index have values 1 and 2
Submitted batch job 8580149
$
$ squeue -u SomeNetID  # Replace SomeNetId with your NetID 
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
         8580149_1   general jobscrip SomeNetID  R       0:21      1 grs4
         8580149_2   general jobscrip SomeNetID  R       0:21      1 awi18
```

{{% alert title="Note" color="info" %}}
To limit the maximum number of simultaneously running jobs in an array use the `%` separator, eg`--array=1-15%3` to run only 3 tasks at a time. 
{{% /alert %}}

### JobId and environment variables

As shown in the previous section, [Parallelizing jobs with job arrays](#parallelizing-jobs-with-job-arrays), jobs within an array are assigned special slurm variables. These variables can be exploited for various computational objectives. Among these, `SLURM_ARRAY_TASK_ID` is the index of an individual task within the array, and  `SLURM_ARRAY_JOB_ID` is the slurm jobId of the entire array job.


In the simplest case, you can use the `${SLURM_ARRAY_TASK_ID}` directly in a script to assign parameter values. For example, to run a workflow across a set of images `image_1.png` ... `image_5.png`, you can simply create an array using the sbatch directive `--array=1-5`, and then, within your sbatch script, use `image_${SLURM_ARRAY_TASK_ID}.png` to indicate the corresponding image.

In more complex scenarios, eg, when the parameters of interest are not mappable to indexes (of a job array), you can use a config file to map the parameters to the job array indexes. For example, let's assume the following parameters:

```bash
$ cat jobarray.config
i       Flower  Color   Origin  
1       Rose    Red     Worldwide
2       Jasmine  White   Asia
3       Tulip   Various Persia&Turkey
4       Orchid  Various Worldwide
5       Lily    Various Worldwide
```
Now, you can use these parameters inside a job script as follows:

```bash
$ cat jobarray.sbatch
#!/bin/bash
#SBATCH --job-name=JobArrayExample
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --array=1-5             # Arry with 5 tasks
#SBATCH --output=slurm-%A_%a.out # Set name of output log. %A is SLURM_ARRAY_JOB_ID and %a is SLURM_ARRAY_TASK_ID
#SBATCH --error=slurm-%A_%a.err  # Set name of error log. %A is SLURM_ARRAY_JOB_ID and %a is SLURM_ARRAY_TASK_ID

config=jobarray.config          # Path to config file

# Obtain parameters from config file:
flower=$(awk -v ArrayTaskID=$SLURM_ARRAY_TASK_ID '$1==ArrayTaskID {print $2}' $config)
color=$(awk -v ArrayTaskID=$SLURM_ARRAY_TASK_ID '$1==ArrayTaskID {print $3}' $config)
origin=$(awk -v ArrayTaskID=$SLURM_ARRAY_TASK_ID '$1==ArrayTaskID {print $4}' $config)

# Use the parameters, eg, print the index and parameter values to a file:
echo "Array task: ${SLURM_ARRAY_TASK_ID},  Flower: ${flower}, color: ${color}, origin: ${origin}" >> output.txt

$
$ sbatch jobArray.sbatch
Submitted batch job 8580317
$ squeue -u SomeNetID  # Replace SomeNetId with your NetID 
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
     8580317_[1-5]   general JobArray SomeNetID PD       0:00      1 (Priority)     
```

In this example, slurm created 5 jobs in a job array, each using the same settings (the name `JobArrayExample`, the `general` partition, `short` QoS, `00:01:00` time, `1` task with `1` CPU and `1G` memory, and an output and error file with both array job Id and task id). Each task looks up certain parameter values from a config file leveraging its index via the `awk` command. 


{{% alert title="Note" color="info" %}}
The command:
```bash
flower=$(awk -v ArrayTaskID=$SLURM_ARRAY_TASK_ID '$1==ArrayTaskID {print $2}' $config)
```
assigns a value to the variable `flower` by reading a configuration file (`$config`), and printing the value in the second column (`{print $2}`) where the first column matches the value of the `ArrayTaskID` variable (`$1==ArrayTaskID`). The `ArrayTaskID` is an awk variable set to the value of the SLURM environment variable `SLURM_ARRAY_TASK_ID`. 
For more on the `awk` utility, see this [awk tutorial](https://blog.jpalardy.com/posts/awk-tutorial-part-1/).
{{% /alert %}}

Jobs within a task array are run in parallel, and hence, there's no guarantee about their order of execution. This is evident looking at the output file from this example:

```bash
$ cat output.txt
Array task: 2,  Flower: Jasmine, color: White, origin: Asia
Array task: 3,  Flower: Tulip, color: Various, origin: Persia&Turkey
Array task: 1,  Flower: Rose, color: Red, origin: Worldwide
Array task: 5,  Flower: Lily, color: Various, origin: Worldwide
Array task: 4,  Flower: Orchid, color: Various, origin: Worldwide
```

Other slurm variables that are set inside a job array are shown in the following table, with values based on the preceding example:

|Slurm Environment Variable |	Description | Value in example |
| ------------------------- | ----------- | ---------------- |
| `SLURM_ARRAY_JOB_ID` | The first job ID of the array. | 8580317 |
| `SLURM_ARRAY_TASK_ID` | The job array index value. | A value in range 1-5 |
| `SLURM_ARRAY_TASK_COUNT` | The number of tasks in the job array.| 5 |
| `SLURM_ARRAY_TASK_MAX` | The highest job array index value.| 5 |
| `SLURM_ARRAY_TASK_MIN` | The lowest job array index value| 1 |

### Slurm commands and job arrays

The `squeue` command reports all submitted jobs. By default, `squeue` reports all of the tasks associated with a job array in one line and uses a regular expression to indicate the `SLURM_ARRAY_TASK_ID` values. To explicitly print one job array element per line, use the `--array` or `-r` flag. The following examples highlight the difference, using the same `jobarray.sbatch` file from the [JobId and environment variables](#jobid-and-environment-variables) section:

```bash
$ sbatch jobarray.sbatch 
Submitted batch job 8593299
$
$ squeue -u SomeNetID  # Replace SomeNetId with your NetID 
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
     8593299_[1-5]   general JobArray SomeNetID PD       0:00      1 (Priority)
$     
$ squeue -r -u SomeNetID  # Replace SomeNetId with your NetID 
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
         8593299_1   general JobArray SomeNetID PD       0:00      1 (Priority)
         8593299_2   general JobArray SomeNetID PD       0:00      1 (Priority)
         8593299_3   general JobArray SomeNetID PD       0:00      1 (Priority)
         8593299_4   general JobArray SomeNetID PD       0:00      1 (Priority)
         8593299_5   general JobArray SomeNetID PD       0:00      1 (Priority)
```


`scancel`, on the other hand, can be used to cancel an entire job array by specifying its  `SLURM_ARRAY_JOB_ID`. Alternatively, to cancel a specific task (or tasks), both its `SLURM_ARRAY_JOB_ID` and `SLURM_ARRAY_TASK_ID` must be specified, possibly with a regular expression, as shown in the following examples:

```bash
$ sbatch jobarray.sbatch
$ squeue -u SomeNetID  # Replace SomeNetId with your NetID 
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
     8593321_[1-5]   general JobArray SomeNetID PD       0:00      1 (Priority)
$     
$ scancel 8593321_4     # Cancel task with index 4 in the array
$ squeue -u SomeNetID   # Replace SomeNetId with your NetID 
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
   8593321_[1-3,5]   general JobArray SomeNetID PD       0:00      1 (Priority)
$
$ scancel 8593321_[1-3] # Cancel tasks in index range 1-3 in the array
$ squeue -u SomeNetID   # Replace SomeNetId with your NetID 
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
         8593321_5   general JobArray SomeNetID PD       0:00      1 (Priority)
$
$ scancel 8593321       # Cancel all tasks in the array
$ squeue -u SomeNetID  # Replace SomeNetId with your NetID 
             JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
$ 
```

{{% alert title="Note" color="info" %}}
For more information on job arrays, refer to [Slurm Job Array Support](https://slurm.schedmd.com/job_array.html)
{{% /alert %}}

## Troubleshooting Common Issues 

Please see the Frequently asked questions on [Scheduler problems ](../../support/faqs/scheduler/) and [Job resources](../../support/faqs/job_resources/)

<!--
see this example: https://www.nhr.kit.edu/userdocs/horeka/batch/
-->


## Kerberos Authentication


Kerberos is an authentication protocol which uses tickets to authenticate users (and computers). You automatically get a ticket when you log in with your password on a TU Delft installed computer. You can use this ticket to authenticate yourself without password when connecting to other computers or accessing your files. To protect you from misuse, the ticket expires after 10 hours or less (even when you're still logged in).

### File access

Your Linux and Windows [home ](../filesystem/#personal-storage-aka-home-folder) directories and the [Group](../filesystem/#group-storage) and [Bulk](../filesystem/#project-storage) shares are located on network fileservers, which allows you to access your files from all TU Delft installed computers. Kerberos authentication is used to enable access to, or protect, your files. Without a valid Kerberos ticket (e.g. when the ticket has expired) you will not be able to access your files but instead you will receive a `Permission denied` error.

### Lifetime of Kerberos Tickets

Kerberos tickets have a limited valid lifetime (of up to 10 hours) to reduce the risk of abuse, even when you stay logged in. If your tickets expire, you will receive a `Permission Denied` error when you try to access your files and a password prompt when you try to connect to another computer. When you want your program to be able to access your files for longer than the valid ticket lifetime, you'll have to renew your ticket (repeatedly) until your program is done. Kerberos tickets can be renewed up to a maximum renewable life period of 7 days (again to reduce the risk of abuse).

The command `klist -5` lists your cached Kerberos tickets together with their expiration time and maximum renewal time:


```bash 
$ klist -5
Ticket cache: FILE:/tmp/krb5cc_uid_random
Default principal: YourNetID@TUDELFT.NET

Valid starting     Expires            Service principal
01/01/01 00:00:00  01/01/01 10:00:00  krbtgt/TUDELFT.NET@TUDELFT.NET
        renew until 01/08/01 00:00:00
```
Where: 
* `Ticket cache`:  The Kerberos tickets that have been issued to you are stored in a ticket cache file. You can have multiple ticket cache files on the same computer (from different connections, for example) with different tickets and ticket expiration times. Some ticket cache files are automatically removed when you logout. 
{{% alert title="Tip" color="info" %}}
Make sure that you renew the tickets in the right ticket cache file (see this [`screen` example](#renewal-using-screen)).
{{% /alert %}}

* `Default principal`: Your identity. 
* `Service principal`: The identity of services that you have gotten tickets for. You always need a Kerberos ticket-granting ticket (`krbtgt`) in order to obtain other tickets for specific services like accessing files (`nfs`) or connecting to computers (`host`). 
* `Valid starting`, `Expires`: Your ticket is only valid between these times (this period is called the valid lifetime). After this time you will not be able to use the service nor automatically renew the ticket (without password). 
* `Renew until`: Your ticket can only be renewed without password up to this time. After this time you will have to obtain a new ticket using your password. 

### Renewing Kerberos tickets

If you have a valid Kerberos `krbtgt` ticket, you can renew it at any time (until it expires) by running the command `kinit -R`:

```bash
$ kinit -R
$ klist -5
Ticket cache: FILE:/tmp/krb5cc_uid_random
Default principal: YourNetID@TUDELFT.NET

Valid starting     Expires            Service principal
01/01/01 01:00:00  01/01/01 11:00:00  krbtgt/TUDELFT.NET@TUDELFT.NET
        renew until 01/08/01 00:00:00
```
{{% alert title="Note" color="info" %}}
Renewing the ticket will not change the duration of the valid lifetime, i.e. a `krbtgt` ticket with a valid lifetime of 1 hour will, after renewal, be valid for another hour.
{{% /alert %}}


When the `krbtgt` ticket has expired or reached it's renew until time, you will have to obtain a new ticket by running `kinit -r 7d` (note the difference in case for the `r`) and authenticating with your password:

```bash
$ kinit -r 7d
Password for YourNetID@TUDELFT.NET:
$ klist -5
Ticket cache: FILE:/tmp/krb5cc_uid_random
Default principal: YourNetID@TUDELFT.NET

Valid starting     Expires            Service principal
01/01/01 11:00:00  01/01/01 21:00:00  krbtgt/TUDELFT.NET@TUDELFT.NET
        renew until 01/08/01 11:00:00
```

The new ticket will have a valid lifetime of 10 hours and a renewable life of 7 days.

On the TU Delft Linux desktops your Kerberos ticket is refreshed (i.e. replaced by a new ticket) automatically every time you enter your password for unlocking the screen saver. 

{{% alert title="Tip" color="info" %}}
Do not disable the screen saver password lock.
{{% /alert %}}

On remote computers you have to manually renew your tickets before they expire.

### Slurm & Kerberos

* Slurm caches your Kerberos ticket, and uses it to execute your job
* Regularly renew the ticket in Slurm’s cache while your jobs are queued or running:

```bash
$ auks -a
Auks API request succeed
```

* To automatically renew your ticket in Slurm’s cache until you change your NetID password, run the following on the `login1` server:

```bash
$ install_keytab
Password for somebody@TUDELFT.NET:
Installed keytab.
```

You need to rerun this command whenever you change your NetID password (at least every 6 months). Otherwise, the automatic renewal will not work and you will receive a warning e-mail.

### Renewal using `screen`

On the compute servers, the `screen` program has been modified to allow jobs to run unattended for up to 7 days. It creates a private ticket cache (to prevent the cache from being destroyed at logout) and automatically renews your ticket up to the maximum renewable life. For example, start MATLAB in Screen with `screen matlab` (the order is important!).

```bash
$ screen matlab
Warning: No display specified.  You will not be able to display graphics on the screen.

                           < M A T L A B (R) >
                 Copyright 1984-2010 The MathWorks, Inc.
              Version 7.11.0.584 (R2010b) 64-bit (glnxa64)
                             August 16, 2010


  To get started, type one of these: helpwin, helpdesk, or demo.
  For product information, visit www.mathworks.com.

>>
```

For longer jobs you have to manually obtain a new ticket at least every 7 days by running `kinit -r 7d` **from within `screen`** (so you use the specific ticket cache file that `screen` is using):

1. connect to screen (`screen -r`),
1. create a new window (`Ctrl-a c`),
1. run `kinit -r 7d`,
1. exit the window (`exit`) and
1. detach from screen (`Ctrl-a d`). 

```bash
$ kinit -r 7d
Password for YourNetID@TUDELFT.NET:
$ klist -5
Ticket cache: FILE:/tmp/krb5cc_uid_private
Default principal: YourNetID@TUDELFT.NET

Valid starting     Expires            Service principal
01/08/01 09:00:00  01/08/01 19:00:00  krbtgt/TUDELFT.NET@TUDELFT.NET
        renew until 01/15/01 09:00:00
$ exit
```

{{% alert title="Tip" color="info" %}}
Use a repeating reminder (twice a week) in your agenda so you don't forget.
{{% /alert %}}

{{% alert title="Important" color="warning" %}}
When the end of the renewable life is reached, your tickets expire and your program(s) will return Permission denied errors when trying to access your files. Your program(s) will not be terminated automatically; you still have to terminate the program(s) yourself.
{{% /alert %}}

Extra functionality can be provided by the `k5start` and `krenew` programs. On most computers these are not available by default but can be installed (~~ask Robbert~~). 
