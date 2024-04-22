---
title: "Job submission"
linkTitle: "Job submission"
weight: 20
description: >
  How to submit jobs to slurm?
---

## Slurm job's terminology: job, job step, task and CPUs

A slurm _job_ (submitted via `sbatch`) can consists of multiple _steps_ in series. Each _step_ (specified via `srun`) can run multiple _tasks (ie programs)_ in parallel. Each task gets its own set of CPUs. As an example, consider the workflow and corresponding breakdown shown in fig 2.

{{< figure src="images/slurm_job_terminology.png" caption="Slurm job's terminology" >}}

In this example, note:
* When you explicitly request 1 CPU per task (`--cpus-per-task=1`), you should also explicitly specify the number of tasks (`--ntasks`). Otherwise, `srun` may start the task twice in parallel (because CPUs are allocated in multiples of 2)
* The default slurm allocation is a single task and single CPU (ie `--ntasks=1 --cpus-per-task=1`). Thus, it is not necessary to explicitly request these to run a single task on a single CPU.
* When using multiple tasks, specify `--mem-per-cpu`.


{{% alert title="Note" color="info" %}}
DAIC is dual-threaded. It means that CPUs are automatically allocated in multiples of 2. Thus, in your job use (a multiple of) 2 threads.
{{% /alert %}} 

