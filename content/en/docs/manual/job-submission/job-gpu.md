---
title: "Using graphic cards"
weight: 28
description: >
  How to use the compute node's GPU?
---

### Jobs on GPU resources

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
