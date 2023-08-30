
---
title: "QuickStart"
linkTitle: "QuickStart"
weight: 20
menu:
  main:
    weight: 20
---


## Pre-requisits

1. Access credentials (see [Access and Accounts](../../docs/intro_daic/access_accounts#access-and-accounts)).
2. Basic familiarity with the command line (see {{< external-link "https://swcarpentry.github.io/shell-novice/" "The software carpentry's Unix shell materials">}})


## Cluster workflow
When working with HPCs in general, or DAIC in particular, the workflow of [_Fig 1_]({{< ref "fig:daic_partitions" >}}) needs to be followed, where:
1. code is developed locally (eg, in a laptop or PC), 
2. then ported to the cluster (see [Connecting to DAIC](../../docs/connecting/) and [Data transfer methods](../../docs/filesystem/#data-transfer-methods)). 
    - Possibly, software and dependencies are set up (see [Software environment](../../docs/software_environment/)).
3. Typically, code is tested in the cluster, eg in an interactive session (see [Interactive jobs on compute nodes](../../docs/job_submissions/#interactive-jobs-on-compute-nodes)), following  [Best practices](../docs/intro_daic/guidelines#best-practices), and consulting with [Support resources](../../support/).
4. If testing is successful, jobs scripts are submitted to the scheduler (see [Job submission](../../docs/job_submissions/#job-submission-and-monitoring)), and 
5. progress is monitored (see [Checking slurm jobs](../../docs/job_submissions/#checking-slurm-jobs)).
6. Finally, once all is done, intermediate files are deleted (see [How do I clean up tmp?](../../support/faqs/job_resources#how-do-i-clean-up-tmp-when-a-job-fails)), and final results are downloaded for subsequent downstream analysis.

{{< figure src="clusterWorkflow.png" caption="Cluster workflow, with key Unix* based commands for each step. Text within angle brackets `<`, `>` denote names that are chosen by the user" ref="fig:cluster_workflow">}}



## Handy commands



| Command                            | Purpose | Example |
| ---------------------------------- | ------- | ------- |
| `sinteractive` | For requesting an interactive node, typically, during testing phases.  Needed compute resources are specified as part of the command, including `mem`, `time`, and `gres`, analogously to `sbatch` directives. | Request a GPU node for 10 minutes: `sinteractive --time=00:10:00 --gres=gpu` |
| `sbatch`       | For submitting a script to slurm for queuing (in batch mode). Requested resources are specified as directives on top of the script | Submit a job in script.sh file `sbatch script.sh`
| `squeue`       | Check the status of jobs in the queue. | Check the user's jobs: `squeue -u $USER`
| `scancel`      | Cancel a job or all jobs of a user. | `scancel -u $USER` or `scancel <jobid>` |
| `slurmtop`     | DAIC-specific command to view top jobs in the queues and their resource use |
| `scontrol show job <jobid>`| Show the details and resources allocated to the job with slurm id `<jobid>`, eg, the UserId, QOS, TimeLimit, Partition, Command, WorkDir, StdErr and StdOut | `scontrol show job 1`

