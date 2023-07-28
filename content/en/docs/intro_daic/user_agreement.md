---
title: "User agreement"
linkTitle: "User agreement"
weight: 4
description: >
  What are the terms of conditions of using DAIC?
---

This user agreement is intended to establish the expectations between all users and administrators of the cluster with respect to fair-use and fair-share of cluster resources. By using the DAIC cluster you agree to these terms and conditions.


## General information about the DAIC cluster

- **Cluster structure:** The DAIC cluster is made up of shared resources contributed by different labs and groups. The pooling of resources from different groups is beneficial for everyone: it enables larger, parallelized computations and more efficient use of resources with less idle time.

- **Basic principles:** ~~Best practices of cluster usage are detailed below.~~ Regardless of the specific details, cluster use is always based on basic principles of fair-use and fair-share (through priority) of resources, and all users are expected to take care at all times that their cluster use is not hindering other users.

- **Policies:** Cluster policies are decided by the user board and enforced by various automated and non-automated actions, for example by the job scheduler based on [QoS limits](../job_submissions/_index.md#partitions-and-quality-of-service) and the administrators for ensuring the stability and performance of the cluster.

- **Support:** 
  * _Cluster administrators_ offer, __during office hours__, different levels of support, which include (in order of priority): ensuring the stability and performance of the cluster, providing generic software, helping with cluster-specific questions and problems, and providing information (via e-mails and during the board meeting) about cluster updates.
  * [New!] ~~_Contact persons_  from participating groups add and manage users at the level of their respective groups, communicate needs and updates between their groups and system administrators, and may help with cluster-specific questions and problems~~.
  * [New!] ~~HPC Engineers, in CS@Delft, provide support to (CS) students, researchers and staff members to efficiently use DAIC resources. This includes: maintaining updated documentation resources, running onboarding and advanced training courses on cluster usage, organizing workshops to assess compute needs, plan infrastructure upgrades, and may collaborate with researchers on individual projects as fits.~~

- **More information:** Please see the [General cluster usage](#general-cluster-usage) and [What to do in case of problems](#what-to-do-in-case-of-problems) sections on where to find more information about cluster use.

- **Cluster workflow:** 
  * The typical steps for running a job on the cluster are: Test → Determine resources → Submit → Monitor job → Repeat until results are obtained. See [Quick start](../../quickstart/_index.md#quick-start)
  * You can use the logins nodes for testing your code, determining the required resources and submitting jobs. See [Computing on login nodes](policies.md#computing-on-login-nodes)
  * For testing jobs which require larger resources (more than 4 CPUs and/or more than 4 GB of memory and/or one or more powerful GPUs), ~~you can~~ start an interactive job. See [Interactive jobs on compute nodes](../job_submissions/_index.md#interactive-jobs-on-compute-nodes).
  * For determining resources of larger jobs, you can submit a single (short) test job. See [Job submission](../job_submissions/_index.md#job-submission)

- **QoS:** 
  * A Quality of Service (QoS) is a set of limits that controls what resources a job can use and determines the priority level of a job. DAIC adopts multiple QoSs 
  ~~* The purpose of the (multiple) QoSs is~~ to optimize the throughput of job scheduling and to reduce the waiting times in the cluster (see [QoS priority](../job_submissions/_index.md#qos-priority)).
    * ~~Long jobs block resources for a long time, thus leading to long waiting times and fragmentation of resources.~~
    * ~~Short jobs block resources only for short times, and can more easily fill in the gaps in the scheduling of resources (thus start sooner), and are therefore better for throughput and waiting times.~~
    * ~~To stimulate short jobs, the `short` QoS has a higher priority, and allows users to use a larger part of all resources, than the `medium` and long `QoS`.~~
    
    * ~~To prevent long jobs from blocking all resources in the cluster for long times (thus causing long waiting times), only a certain part of all cluster resources is available to all running `long` QoS jobs (of all users) combined. All running `medium` QoS jobs together can use a somewhat larger part of all resources in the cluster, and all running `short` QoS jobs combined are allowed to fill the biggest part of the cluster. These limits are called the **QoS group ** limits. When this limit is reached, no new jobs with this QoS can be started, until some of the running jobs with this QoS finish and release some resources. The scheduler will indicate this with the reason `QoS Group CPU/memory/GRES limit`.~~

  * ~~To prevent one user from single-handedly using all available resources in a certain QoS, there are also limits for the total resources that all running jobs of one user in a specific QoS can use. These are called the QoS per-user limits. When this limit is reached, no new jobs of this user with this QoS can be started, until some of the running jobs of this user and with this QoS finish and release some resources. The scheduler will indicate this with the reason ‘QoS User CPU/memory/GRES limit’.~~
    * The DAIC QoS limits are set by the DAIC user board, and the scheduler strictly enforces these limits. Thus, no user can use more resources than the amount that was set by the user board. 
    * Any (perceived) imbalance in the use of resources by a certain QoS or user should not be hold against a user or the scheduler, but should be discussed in the user board.

## General cluster usage

1. You may use cluster resources for your research within the QoS restrictions of your domain user and user group.
    1. ~~You can find the QoS limits for the 'general' partition on https://login.daic.tudelft.nl/ under "Getting started (slides)".~~
    2. Depending on your user group, you might be eligible to use specific partitions, giving higher priorities on certain nodes. Please check this with your lab.

2. Depending on your user group, you might be eligible to get priorities on certain nodes. For example, you might have access to a specialized partition or limited-time node reservation for your group or department (for example before a conference deadline). Please check this with your lab and try to use these in your `.sbatch` file, your jobs should then start faster!

3. In general, you will be informed about standard administrative actions on the cluster. All official DAIC cluster e-mails are sent to your official TU Delft mailbox, so it is advised to check it regularly.
	  1. You will receive e-mails about downtimes relating to scheduled maintenance.
    2. You, or your supervisor, will receive e-mails about scheduled cluster user board meetings where any updates and changes to the cluster structure, software, or hardware will be announced. Please check with your lab or feel free to join the cluster board meetings if you want to be up-to-date about any changes.
	  3. You will receive _automated_ e-mails regarding the efficiency of your jobs. The cluster monitors the use of resources of all jobs. When certain specific inefficiencies are detected for a significant number of jobs in the same day, an _automated_ efficiency mail is sent to inform you about these problems with your resource use, to help you optimize your jobs. These mails will not lead to automatic cancellations or bans. To avoid spamming, limited inefficient use will not trigger a mail.
	  4. You will receive an e-mail when your jobs are canceled or you receive a cluster ban (see the [Expectations from cluster users](#expectations-from-cluster-users) and [Regulations](#regulations) sections). You will be informed about why your jobs were canceled or why you were banned from the cluster (often before the bans take place). If the problem is still not clear to you from the e-mails you already received, please follow the steps detailed in the [What to do in case of problems](#what-to-do-in-case-of-problems) section.
    5. You are <ins>not</ins> entitled to receive personalized help on how to debug your code via e-mail. It is your responsibility to solve technical problems stemming from your code. Please first consult with your lab for a solution to a technical problem (see [What to do in case of problems](#what-to-do-in-case-of-problems)). However, admins might offer help, advice and solutions along with information regarding a job cancellation or ban. Please listen to such advice, it might help you solve your problem and improve fair use of the cluster.

4. You may join cluster user board meetings. In the meetings you will be informed of any new developments, hardware and software updates and can suggest changes and improvements. These meetings take place roughly every 3 months and will be announced by e-mail and on the ~~[MS Teams channel](https://teams.microsoft.com/l/channel/19%3ad5501f1d3a6e4b7394d7cee89d5b2d1c%40thread.tacv2/General?groupId=f73478dd-163d-4e49-8f75-cdfe56e20bbc&tenantId=096e524d-6929-4030-8cd3-8ab42de0887b)~~.



## Expectations from cluster users

1. You are responsible for your jobs not interfering with other users' cluster usage. Please try to always keep in mind that cluster resources are limited and shared between all users, and that fair use benefits everyone.

2. You are not allowed to use the cluster for reasons unrelated to your studies and research.

3. If your jobs are destructive to other users' jobs or are threatening cluster integrity, your jobs might be canceled. You have the responsibility at all times to avoid behavior which interferes negatively with other users' cluster usage. See DAIC [Regulations](#regulations)

4. If the destructive behavior of your jobs does not change over time or you are unresponsive to e-mails from system admins requesting information or requiring immediate action regarding your cluster use, you might receive a ban from the cluster. See DAIC [Regulations](#regulations)

## Regulations

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


## What to do in case of problems
When you encounter problems, please follow the subsequent steps, in the indicated order ~~starting from 1.,~~:
  1. First, please contact your colleagues and fellow cluster users in your lab, concerning problems with your code, job performance and efficiency. They may be running similar jobs and potentially have solutions for your problem.
  2. You can also ask questions to fellow users on the [MS Teams channel](https://teams.microsoft.com/l/channel/19%3ad5501f1d3a6e4b7394d7cee89d5b2d1c%40thread.tacv2/General?groupId=f73478dd-163d-4e49-8f75-cdfe56e20bbc&tenantId=096e524d-6929-4030-8cd3-8ab42de0887b). 
  3. For prolonged problems, your initial contact point is your supervisor/PI.
  4. As a final step, you can contact the cluster administrators for technical sysadmin problems or persistent efficiency problems, or for more information if you are not sure why you are banned from the cluster. You can do this by reporting your question, through the [Self Service Portal](https://tudelft.topdesk.net/tas/public/ssp/), to the Service Desk. In your question, refer to the ‘DAIC cluster’.
  5. For severe recurring problems, complaints and suggestions for policy changes, you can contact [Thomas Abeel](mailto:T.Abeel@tudelft.nl). If you encounter policy problems affecting multiple users, please contact Thomas to bring it up as an agenda point in the next user board meeting.

## Responsible cluster usage

1. You are responsible that your jobs run efficiently.
    1. Please keep an eye on your jobs and the automated efficiency e-mails to check for unexpected behavior.
	  2. Sometimes many jobs from the same user, or from student groups, will be running on many nodes at the same time. While this may seem like one user, or user group, is blocking the cluster for everyone else, please keep in mind that the scheduler operates on a set of predetermined rules based on the QoS and priority settings. We do not want idle resources. Therefore, at the time that those jobs were started, the resources were idle, no higher priority jobs were in the queue and the jobs did not exceed the QoS limits. If you repeatedly observe pending jobs, please bring it up in the user board meeting.
	  3. Short job efficiency: If you are running many (hundreds or thousands of) very short jobs (duration of a few minutes), you may want to consider that starting and individually loading the same modules for each job may create overheads. When reasonably possible, it might save computation time to instead group some jobs together. The jobs can still be submitted to the `short` queue if the runtime is less than 4 hours.
	  4. GPU job efficiency: If you are running multi-GPU jobs (for example due to GPU memory limitations), you may want to consider that the communications between the GPUs and other CPU processes (for example data loaders) may create overheads. It might be useful to consider running jobs on less GPUs with more GPU memory each, or taking advantage of specialized libraries optimized for multi-GPU computing in your code.


## Feedback and Suggestions

1. If you have suggestions for policy changes (changes to QoS, scheduler priorities, and similar), please join the cluster board meetings as stated in [General cluster usage](#general-cluster-usage) and [What to do in case of problems](#what-to-do-in-case-of-problems).