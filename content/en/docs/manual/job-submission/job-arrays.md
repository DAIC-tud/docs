---
title: "Job arrays"
linkTitle: "Job arrays"
weight: 30
description: >
  How to submit jobs to slurm?
---


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

Please see the Frequently asked questions on [Scheduler problems ](/support/faqs/scheduler) and [Job resources](/support/faqs/job-resources)

<!--
see this example: https://www.nhr.kit.edu/userdocs/horeka/batch/
-->

