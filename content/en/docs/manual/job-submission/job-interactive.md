---
title: "Interactive jobs"
linkTitle: "Interactive jobs"
weight: 20
description: >
  How to submit jobs to slurm?
---


### Interactive jobs on compute nodes

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





