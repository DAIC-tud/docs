---
title: "Submitting jobs"
linkTitle: "Submitting jobs"
weight: 20
description: >
  How to submit jobs to slurm?
---

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
