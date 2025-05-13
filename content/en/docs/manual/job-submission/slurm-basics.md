---
title: "Basics of Slurm jobs"
linkTitle: "Basics of Slurm jobs"
weight: 1
description: >
  How to submit jobs to the cluster?
---

## Job script

Job scripts are text files, where the header set of directives that specify compute resources, and the remainder is the code that needs to run. All resources and scheduling are specified in the header as `#SBATCH` directives (see `man sbatch` for more information). Code could be a set of steps to run in series, or parallel tasks within these steps (see [Slurm job's terminology](/docs/manual/job-submission)).

The code snippet below is a template script that can be customized to run jobs on DAIC. 
A useful tool that can be used to streamline the debugging of such scripts is {{< external-link "https://www.shellcheck.net/" "ShellCheck" >}}.

{{< card code=true header="jobscript.sbatch" lang="bash">}}
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

#Remaining job commands go below here. For example, to run a Matlab script named "matlab_script.m", uncomment:
#module use /opt/insy/modulefiles # Use DAIC INSY software collection
#module load matlab/R2020b        # Load Matlab 2020b version
#srun matlab < matlab_script.m # Computations should be started with 'srun'.

{{< /card >}}


{{% alert title="Note" color="info" %}}
* DAIC is dual-threaded. It means that CPUs are automatically allocated in multiples of 2. Thus, in your job use (a multiple of) 2 threads.
* Do not enable mails when submitting large numbers (>20) of jobs at once
{{% /alert %}} 

### Job submission
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


### Using GPU resources

Some DAIC nodes have GPUs of different types, that can be used for various compute purposes (see [GPUs](/docs/system#gpus)).


To request a gpu for a job, use the sbatch directive `--gres=gpu[:type][:number]`, where the optional `[:type]` and `[:number]` specify the type and number of the GPUs requested, as in the examples below:

{{< figure src="/img/slurm_request_gpus.png" caption="Slurm directives to request gpus for a job" >}}



{{% alert title="Note" color="warning"%}}
For CUDA programs, first, load the needed modules (CUDA, cuDNN) before running your code (see [Available software](/docs/manual/software/available-software)).
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
login1.daic.tudelft.nl
$
$ sinteractive --cpus-per-task=1 --mem=500 --time=00:01:00 --gres=gpu:v100:1
Note: interactive sessions are automatically terminated when they reach their time limit (1 hour)!
srun: job 8607665 queued and waiting for resources
srun: job 8607665 has been allocated resources
 15:27:18 up 51 days,  3:04,  0 users,  load average: 62,09, 59,43, 44,04
SomeNetID@insy11:~$
SomeNetID@insy11:~$ hostname # check you are in one of the compute nodes
insy11.daic.tudelft.nl
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

{{% alert title="Note" color="info" %}}
To inspect a given GPU and obtain its details, you can run the following commands on an interactive session or an `sbatch` script.

```bash
$ sinteractive --cpus-per-task=2 --mem=500 --time=00:02:00 --gres=gpu
Note: interactive sessions are automatically terminated when they reach their time limit (1 hour)!
srun: job 8607783 queued and waiting for resources
srun: job 8607783 has been allocated resources
15:50:29 up 51 days,  3:26,  0 users,  load average: 60,33, 59,72, 54,65

SomeNetID@influ1:~$ nvidia-smi  --format=csv,noheader --query-gpu=name	
NVIDIA GeForce RTX 2080 Ti

SomeNetID@influ1:~$ nvidia-smi -q | grep Architecture	
Product Architecture                  : Turing                                                                     

SomeNetID@influ1:~$ nvidia-smi --query-gpu=compute_cap --format=csv,noheader
7.5	

SomeNetID@influ1:~$ apptainer run --nv  cuda_based_image.sif | grep "CUDA Cores"	 # using the apptainer image of the tutorial
(068) Multiprocessors, (064) CUDA Cores/MP:    4352 CUDA Cores

SomeNetID@influ1:~$ nvidia-smi  --format=csv,noheader --query-gpu=memory.total
11264 MiB

SomeNetID@influ1:~$ exit
```

{{% /alert %}}

## Interactive jobs on compute nodes

To work interactively on a node, e.g., to debug a running code, or test on a GPU, start an interactive session using `sinteractve <compute requirements>`. If no parameters were provided, the default are applied. `<compute requirement>` can be specified the same way as sbatch directives within an sbatch script (see [Submitting jobs](/docs/manual/job-submission/job-scripts)), as in the examples below:

```bash
$ hostname # check you are in one of the login nodes
login1.daic.tudelft.nl
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





## Monitoring slurm jobs

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

## Cancelling jobs


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