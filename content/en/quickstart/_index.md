
---
title: "QuickStart"
linkTitle: "QuickStart"
weight: 20
menu:
  main:
    weight: 20
---

{{% pageinfo %}}
This is a quick getting started guide
{{% /pageinfo %}}


## Quick start
When working with HPCs in general, or DAIC in particular, the workflow of _Fig 1_ needs to be followed, where code is developed locally (eg, in a laptop or PC), then ported to the cluster for further testing (eg, in an interactive node). If successful, jobs scripts are created and submitted to slurm, and progress is monitored. Finally, once all is done, intermediate files are ideally deleted, and final results downloaded for subsequent downstream analysis.

{{< figure src="clusterWorkflow.png" caption=">Fig 1: Cluster workflow, with key Unix* based commands for each step. Text within angle brackets `<`, `>` denote names that are chosen by the user" >}}





### Handy commands:



| Command                            | Purpose | Example |
| ---------------------------------- | ------- | ------- |
| `sinteractive` | For requesting an interactive node, typically, during testing phases.  Needed compute resources are specified as part of the command, including `mem`, `time`, and `gres`, analogously to `sbatch` directives. | Request a GPU node for 10 minutes: `sinteractive --time=00:10:00 --gres=gpu` |
| `sbatch`       | For submitting a script to slurm for queuing (in batch mode). Requested resources are specified as directives on top of the script | Submit a job in script.sh file `sbatch script.sh`
| `squeue`       | Check the status of jobs in the queue. | Check the user's jobs: `squeue -u $USER`
| `scancel`      | Cancel a job or all jobs of a user. | `scancel -u $USER` or `scancel <jobid>` |
| `slurmtop`     | DAIC-specific command to view top jobs in the queues and their resource use |
| `scontrol show job <jobid>`| Show the details and resources allocated to the job with slurm id `<jobid>`, eg, the UserId, QOS, TimeLimit, Partition, Command, WorkDir, StdErr and StdOut | `scontrol show job 1`

