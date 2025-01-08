---
title: "Best practices"
linkTitle: "Best practices"
weight: 99
description: >
  What is acceptable usage of DAIC?
---

The available processing power and memory in DAIC is large, but still limited. You should use the available resources efficiently and fairly. This page lays out a few general principles and guidelines  for considerate use of DAIC.

## Using shared resources
The [computing nodes](docs/system/#compute-nodes) within DAIC are primarily meant to run large, long (non-interactive) jobs. You share these resources with other users across departments. Thus, you need to be cautious of your usage so you do not hinder other users. 

To help protect the active jobs and resources, when a [login node](docs/system/#login-nodes) becomes overloaded, new logins to this node are automatically disabled. 
This means that you will sometimes have to wait for other jobs to finish and at other times ICT may have to kill a job to create space for other users.

{{% pageinfo %}}
**_One rule:_** Respect your fellow users.

**Implication**: we reserve the right to terminate any job or process that we feel is clearly interfering with the ability of others to complete work, regardless of technical measures or its resource usage.
{{% /pageinfo %}}

### Best practices
* Connect only directly from the bastion server to the login nodes (See [Connecting to DAIC](/docs/manual/connecting/))
* Always choose the login node with the lowest use (most importantly system load and memory usage), by checking the {{< external-link "https://login.daic.tudelft.nl/" "Current resource usage page" >}} or the `servers` command for information.
  * Each login node displays a message at login. Make sure you understand it before proceeding. This message includes the current load of the node, so look at it at every login
* Only use the storage best suited to your files (See [Storage](/docs/system#storage)).

<!--
* ~~Automate your job.~~
  * ~~Prepare a script that runs all necessary steps automatically, so you don't have unnecessary delays and can rerun the job if necessary. Do the interactive pre- and post-processing, including creating and debugging the script, on your own computer as much as possible.~~
-->

* Do interactive code development, debugging and testing in your local machine, as much as possible. In the cluster, try to organize your code as scripts, instead of working interactively in the command line.

* If you need to test and debug in the cluster, for example, in a GPU node, request an interactive session and do not work in the login node itself (See [Interactive jobs on compute nodes](/docs/manual/job-submission/job-interactive)).

* Save results frequently: your job can crash, the compute node can become overloaded, or the network shares can become unavailable. 

* Write your code in a modular way, so that you can continue the job from the point where it last crashed.

<!--
* ~~(Automatically) terminate your jobs when they are done.~~ How?
  * ~~Release the used resources so other users can use them. Have the script save the final results to file and exit.~~
-->

* Actively monitor the status of your jobs:
  * Make sure your job runs normally and is not hindering other jobs. Check the following at the start of a job and thereafter at least twice a day:
    - If your job is not working correctly (or halted) because of a programming error, terminate it immediately; debug and fix the problem instead of just trying again (the result will almost certainly be exactly the same).
    - If your `screen`'s [Kerberos ticket](/docs/manual/job-submission/kerberos) has expired, renew it so your job can successfully save it's results.
    - Use the `top` program to monitor the cpu (`%CPU`) and memory (`%MEM`) usage of your code. If either is too high, kill your code so it doesn't cause problems for other users.
    - Don't leave `top` running unless your are continuously watching it; press q to quit.
    - Watch the current resource usage (see {{< external-link "https://login.daic.tudelft.nl/" "Current resource usage page" >}} or use the `servers` command), and if the node is running close to it's limits (higher than 90% load or memory, swap or disk usage), consider moving your job to a less busy node. <!-- ~~If more than half of the nodes are at their limits, consider killing one or more jobs to make some space for others. ~~ -->

### Computing on login nodes
<!--
* ~~Run only one computing or memory intensive job per login node.~~
  * ~~Leave enough resources for other users. When the number of running threads of all programs combined exceed the number of cores in the node, or the combined virtual memory used exceeds the node's memory, the efficiency of the node will be (severely) reduced.~~
-->

- You can use login nodes for basic tasks like compiling software, preparing submission scripts for the batch queue, submitting and monitoring jobs in the batch queue, analyzing results, and moving data or managing files. 

- Small-scale interactive work may  be acceptable on login nodes if your resource requirements are minimal.

<!--
{{% alert title="Note" color="info" %}}
~~Login nodes have per-user CPU and memory quotas. If you run processes on a login node that push the total usage beyond a certain amount, the limiter will begin killing the largest processes until the total  satisfies the limit. ~~
{{% /alert %}}
-->

- Please do not run production research computations on the login nodes. If necessary, request an interactive session in these cases (See [Interactive jobs on compute nodes](/docs/manual/job-submission/job-interactive)) 

{{% alert title="Note" color="info" %}}

Most multi-threaded applications (such as `Java` and `Matlab`) will automatically use all cpu cores of a node, and thus take away processing power from other jobs. If you can specify the number of threads, set it to at most 25% (¼) of the cores in that node (for a node with 16 cores, use at most 4; this leaves enough processing capacity for other users). Also see [How do I request CPUs for a multithreaded program? ](/support/faqs/job-resources#how-do-i-request-cpus-for-a-multithreaded-program)
{{% /alert %}}
