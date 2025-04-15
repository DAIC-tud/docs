---
title: "Policies & Usage guidelines"
linkTitle: "Policies & usage guidelines"
weight: 10
description: >
  What is required to access DAIC, usage policies, and how to acknowledge DAIC in your publication.
---

## User agreement
This user agreement is intended to establish the expectations between all users and administrators of the cluster with respect to fair-use and fair-share of cluster resources. By using the DAIC cluster you agree to these terms and conditions.

### Defintions
- **Cluster structure:** The DAIC cluster is made up of shared resources contributed by different labs and groups. The pooling of resources from different groups is beneficial for everyone: it enables larger, parallelized computations and more efficient use of resources with less idle time.
- **Basic principles:** Regardless of the specific details, cluster use is always based on basic principles of fair-use and fair-share (through priority) of resources, and all users are expected to take care at all times that their cluster use is not hindering other users.
- **Policies:** Cluster policies are decided by the user board and enforced by various automated and non-automated actions, for example by the job scheduler based on [QoS limits](/docs/manual/job-submission/priorities/#quality-of-service-qos) and the administrators for ensuring the stability and performance of the cluster.
- **Support:** 
  * _Cluster administrators_ offer, __during office hours__, different levels of support, which include (in order of priority): ensuring the stability and performance of the cluster, providing generic software, helping with cluster-specific questions and problems, and providing information (via e-mails and during the board meeting) about cluster updates.
  * _Contact persons_  from participating groups add and manage users at the level of their respective groups, communicate needs and updates between their groups and system administrators, and may help with cluster-specific questions and problems.
  * _HPC Engineers_, in CS@Delft, provide support to (CS) students, researchers and staff members to efficiently use DAIC resources. This includes: maintaining updated documentation resources, running onboarding and advanced training courses on cluster usage, organizing workshops to assess compute needs, plan infrastructure upgrades, and may collaborate with researchers on individual projects as fits.
- **More information:** Please see the [Terms of service](#terms-of-service) and [What to do in case of problems](#what-to-do-in-case-of-problems) sections on where to find more information about cluster use.
- **Cluster workflow:** 
  * The typical steps for running a job on the cluster are: Test → Determine resources → Submit → Monitor job → Repeat until results are obtained. See [Quickstart](/quickstart/)
  * You can use the logins nodes for testing your code, determining the required resources and submitting jobs (see [Computing on login nodes](/docs/manual/best-practices#computing-on-login-nodes)).
  * For testing jobs which require larger resources (more than 4 CPUs and/or more than 4 GB of memory and/or one or more powerful GPUs), start an interactive job (see [Interactive jobs](/docs/manual/job-submission/slurm-basics/#interactive-jobs-on-compute-nodes)).
  * For determining resources of larger jobs, you can submit a single (short) test job (see [Submitting jobs](/docs/manual/job-submission/))
- **QoS:** 
  * A Quality of Service (QoS) is a set of limits that controls what resources a job can use and determines the priority level of a job. DAIC adopts multiple QoSs 
   to optimize the throughput of job scheduling and to reduce the waiting times in the cluster (see [Quality of Service](/docs/manual/job-submission/priorities/#quality-of-service-qos)).
  * The DAIC QoS limits are set by the DAIC user board, and the scheduler strictly enforces these limits. Thus, no user can use more resources than the amount that was set by the user board. 
   * Any (perceived) imbalance in the use of resources by a certain QoS or user should not be hold against a user or the scheduler, but should be discussed in the user board.

### Access and accounts
- DAIC is a cluster dedicated for TU Delft _researchers_ (eg, PhD students, postdocs, .. etc) _from participating groups_ (see [Contributing departments](/docs/introduction/contributors-funders)). 

{{% alert title="Needing access to DAIC?" color="primary" %}}
To access DAIC resources, eligible candidates from these groups can request an account via the [DAIC request Access form](https://tudelft.topdesk.net/tas/public/ssp/content/detail/service?unid=c6d0e44564b946eaa049898ffd4e6938&from=d75e860b-7825-4711-8225-8754895b3507). 
{{% /alert %}}


- Additionally, requests for resources reservations can also be accommodated (see [Terms of service](#terms-of-service)).    

### Terms of service
1. You may use cluster resources for your research within the QoS restrictions of your domain user and user group. Depending on your user group, you might be eligible to use specific partitions, giving higher priorities on certain nodes. See [Priority tiers](/docs/manual/job-submission/priorities), and please check this with your lab.
2. Depending on your user group, you might be eligible to get priorities on certain nodes. For example, you might have access to a specialized partition or limited-time node reservation for your group or department (for example before a conference deadline). Please check this with your lab and try to use these in your `*.sbatch` file, your jobs should then start faster! See [Resources Reservations](/docs/manual/job-submission/priorities/#resources-reservations) for more information.
3. In general, you will be informed about standard administrative actions on the cluster. All official DAIC cluster e-mails are sent to your official TU Delft mailbox, so it is advised to check it regularly.
	  1. You will receive e-mails about downtimes relating to scheduled maintenance.
    2. You, or your supervisor, will receive e-mails about scheduled cluster user board meetings where any updates and changes to the cluster structure, software, or hardware will be announced. Please check with your lab or feel free to join the cluster board meetings if you want to be up-to-date about any changes.
	  3. You will receive _automated_ e-mails regarding the efficiency of your jobs. The cluster monitors the use of resources of all jobs. When certain specific inefficiencies are detected for a significant number of jobs in the same day, an _automated_ efficiency mail is sent to inform you about these problems with your resource use, to help you optimize your jobs. These mails will not lead to automatic cancellations or bans. To avoid spamming, limited inefficient use will not trigger a mail.
	  4. You will receive an e-mail when your jobs are canceled or you receive a cluster ban (see the [Expectations from cluster users](#expectations-from-cluster-users) and [Consequences of irresponsible usage](#consequences-of-irresponsible-usage) sections). You will be informed about why your jobs were canceled or why you were banned from the cluster (often before the bans take place). If the problem is still not clear to you from the e-mails you already received, please follow the steps detailed in the [What to do in case of problems](#what-to-do-in-case-of-problems) section.
    5. You are <ins>not</ins> entitled to receive personalized help on how to debug your code via e-mail. It is your responsibility to solve technical problems stemming from your code. Please first consult with your lab for a solution to a technical problem (see [What to do in case of problems](#what-to-do-in-case-of-problems)). However, admins might offer help, advice and solutions along with information regarding a job cancellation or ban. Please listen to such advice, it might help you solve your problem and improve fair use of the cluster.
4. You may join cluster user board meetings. In the meetings you will be informed of any new developments, hardware and software updates and can suggest changes and improvements. These meetings take place roughly every 3 months and will be announced by e-mail and on the [MatterMost channel](https://mattermost.tudelft.nl/signup_user_complete/?id=cb1k3t6ytpfjbf7r397395axyc&md=link&sbr=su).

### Expectations from cluster users
1. You are responsible for your jobs not interfering with other users' cluster usage. Please try to always keep in mind that cluster resources are limited and shared between all users, and that fair use benefits everyone.
2. You are not allowed to use the cluster for reasons unrelated to your studies and research.
3. If your jobs are destructive to other users' jobs or are threatening cluster integrity, your jobs might be canceled. You have the responsibility at all times to avoid behavior which interferes negatively with other users' cluster usage. See [Consequences of irresponsible usage](#consequences-of-irresponsible-usage).
4. If the destructive behavior of your jobs does not change over time or you are unresponsive to e-mails from system admins requesting information or requiring immediate action regarding your cluster use, you might receive a ban from the cluster. See [Consequences of irresponsible usage](#consequences-of-irresponsible-usage).
5. You are expected to **cite and acknowledge DAIC** in your scientific publications using the format specified in the [Citation and Acknowledgement](/docs/introduction/advisors-impact#citation-and-acknowledgement) section. Additionally, please remember to post any scientific output based-off work performed on DAIC to the [ScientificOutput MatterMost channel](https://mattermost.tudelft.nl/daic/channels/scientificoutput).

### Responsible cluster usage
You are responsible that your jobs run efficiently:
  1. Please keep an eye on your jobs and the automated efficiency e-mails to check for unexpected behavior.
  2. Sometimes many jobs from the same user, or from student groups, will be running on many nodes at the same time. While this may seem like one user, or user group, is blocking the cluster for everyone else, please keep in mind that the scheduler operates on a set of predetermined rules based on the QoS and priority settings. We do not want idle resources. Therefore, at the time that those jobs were started, the resources were idle, no higher priority jobs were in the queue and the jobs did not exceed the QoS limits. If you repeatedly observe pending jobs, please bring it up in the user board meeting.
  3. Short job efficiency: If you are running many (hundreds or thousands of) very short jobs (duration of a few minutes), you may want to consider that starting and individually loading the same modules for each job may create overheads. When reasonably possible, it might save computation time to instead group some jobs together. The jobs can still be submitted to the `short` queue if the runtime is less than 4 hours.
  4. GPU job efficiency: If you are running multi-GPU jobs (for example due to GPU memory limitations), you may want to consider that the communications between the GPUs and other CPU processes (for example data loaders) may create overheads. It might be useful to consider running jobs on less GPUs with more GPU memory each, or taking advantage of specialized libraries optimized for multi-GPU computing in your code.

### Consequences of irresponsible usage
1. Your jobs might be **canceled** if:
    1. The node your jobs are running on becomes unresponsive and the node is automatically restarted.
    2. The job is overloading the node (for example overloading the network communication of the node).
    3. The job is adversely affecting the execution of other jobs (jobs that are not using all requested resources (effectively) and thus unfairly block waiting jobs from running may also be canceled).
    4. The jobs ignore the directions from the administrators (for example if a job is (still) affected by the same problem that the administrators informed you about before, and asked you to fix and test before resubmitting).
    5. The job is showing clear signs of a problem (like hanging, or being idle, or using only 1 CPU of the multiple CPUs requested, or not using a GPU that was requested).
2. You might receive a cluster access **ban** for:
    1. Disallowed use of the cluster, including disallowed use of computing time, purposefully ignoring directions, guidelines, fair-use principles and/or (trying to gain) unauthorized access and/or causing disruptions to the cluster or parts thereof (even if unintentional).
    2. Unresponsiveness to e-mails from system admins requesting information or requiring immediate action regarding your cluster use.
    3. Repeated problems caused by your cluster use which go unsolved even after attempts to resolve the issue.
    4. Your cluster use privileges will be returned when all parties are confident that you understand the problem and it won't reoccur.
3. Your jobs **won't be canceled** for:
    1. Scheduled maintenance. This is planned in advance and jobs that would run during scheduled maintenance times won't start until the end of maintenance.


### What to do in case of problems?
When you encounter problems, please follow the subsequent steps, in the indicated order:
  1. First, please contact your colleagues and fellow cluster users in your lab, concerning problems with your code, job performance and efficiency. They may be running similar jobs and potentially have solutions for your problem.
  2. You can also ask questions to fellow users on the [MatterMost channel](https://mattermost.tudelft.nl/signup_user_complete/?id=cb1k3t6ytpfjbf7r397395axyc&md=link&sbr=su). 
  3. For prolonged problems, your initial contact point is your supervisor/PI.
  4. As a final step, you can contact the cluster administrators for technical sysadmin problems or persistent efficiency problems, or for more information if you are not sure why you are banned from the cluster. You can do this by reporting your question, through the {{< external-link "https://tudelft.topdesk.net/tas/public/ssp/" "Self Service Portal" >}}, to the Service Desk. In your question, refer to the ‘DAIC cluster’.
  5. For severe recurring problems, complaints and suggestions for policy changes, or issues affecting multiple users, you can contact the [DAIC advisory board](/docs/introduction/advisors-impact/) to bring it up as an agenda point in the next user board meeting.




## Usage guidelines

The available processing power and memory in DAIC is large, but still limited. You should use the available resources efficiently and fairly. This page lays out a few general principles and guidelines  for considerate use of DAIC.

### Using shared resources
The computing servers within DAIC are primarily meant to run large, long (non-interactive) jobs. You share these resources with other users across departments. Thus, you need to be cautious of your usage so you do not hinder other users. 

To help protect the active jobs and resources, when a login server becomes overloaded, new logins to this server are automatically disabled. 
This means that you will sometimes have to wait for other jobs to finish and at other times ICT may have to kill a job to create space for other users.

{{% pageinfo %}}
**_One rule:_** Respect your fellow users.

**Implication**: we reserve the right to terminate any job or process that we feel is clearly interfering with the ability of others to complete work, regardless of technical measures or its resource usage.
{{% /pageinfo %}}

### Recommendations
* Always choose the login server with the lowest use (most importantly system load and memory usage), by checking the {{< external-link "https://login.daic.tudelft.nl/" "Current resource usage page" >}} or the `servers` command for information.
  * Each server displays a message at login. Make sure you understand it before proceeding. This message includes the current load of the server, so look at it at every login
* Only use the storage best suited to your files (See [Storage](/docs/system#storage)).

<!--
* ~~Automate your job.~~
  * ~~Prepare a script that runs all necessary steps automatically, so you don't have unnecessary delays and can rerun the job if necessary. Do the interactive pre- and post-processing, including creating and debugging the script, on your own computer as much as possible.~~
-->

* Do interactive code development, debugging and testing in your local machine, as much as possible. In the cluster, try to organize your code as scripts, instead of working interactively in the command line.

* If you need to test and debug in the cluster, for example, in a GPU node, request an interactive session and do not work in the login node itself (See [Interactive jobs on compute nodes](/docs/manual/job-submission/job-interactive)).

* Save results frequently: your job can crash, the server can become overloaded, or the network shares can become unavailable. 

* Write your code in a modular way, so that you can continue the job from the point where it last crashed.

<!--
* ~~(Automatically) terminate your jobs when they are done.~~ How?
  * ~~Release the used resources so other users can use them. Have the script save the final results to file and exit.~~
-->

* Actively monitor the status of your jobs and the loads of the servers.
  * Make sure your job runs normally and is not hindering other jobs. Check the following at the start of a job and thereafter at least twice a day:
    - If your job is not working correctly (or halted) because of a programming error, terminate it immediately; debug and fix the problem instead of just trying again (the result will almost certainly be exactly the same).
    - If your `screen`'s [Kerberos ticket](/docs/manual/job-submission/kerberos) has expired, renew it so your job can successfully save it's results.
    - Use the `top` program to monitor the cpu (`%CPU`) and memory (`%MEM`) usage of your code. If either is too high, kill your code so it doesn't cause problems for other users.
    - Don't leave `top` running unless your are continuously watching it; press q to quit.
    - Watch the current resource usage (see {{< external-link "https://login.daic.tudelft.nl/" "Current resource usage page" >}} or use the `servers` command), and if the server is running close to it's limits (higher than 90% server load or memory, swap or disk usage), consider moving your job to a less busy server. <!-- ~~If more than half of the servers are at their limits, consider killing one or more jobs to make some space for others. ~~ -->

### Computing on login nodes
<!--
* ~~Run only one computing or memory intensive job per login server.~~
  * ~~Leave enough resources for other users. When the number of running threads of all programs combined exceed the number of cores in the server, or the combined virtual memory used exceeds the server's memory, the efficiency of the server will be (severely) reduced.~~
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

Most multi-threaded applications (such as `Java` and `Matlab`) will automatically use all cpu cores of a server, and thus take away processing power from other jobs. If you can specify the number of threads, set it to at most 25% (¼) of the cores in that server (for a server with 16 cores, use at most 4; this leaves enough processing capacity for other users). Also see [How do I request CPUs for a multithreaded program? ](/support/faqs/job-resources#how-do-i-request-cpus-for-a-multithreaded-program)
{{% /alert %}}
