---
title: "Software Environment"
linkTitle: "Software Environment"
weight: 7
description: >
  How to set up your tools and/or run certain libraries
---

{{% pageinfo %}}
At present [DAIC](https://daic.pages.ewi.tudelft.nl/docs/) and [DelftBlue](https://doc.dhpc.tudelft.nl/delftblue) have different software stacks. This pertains to the operating system (CentOS 7 _vs_ Red Hat Enterprise Linux 8, respectively) and, consequently, the available software. Please refer to the respective [DelftBlue modules](https://doc.dhpc.tudelft.nl/delftblue/DHPC-modules/) and [DAIC available software](#available-software-and-libraries-loading-and-using-software-modules) documentation before commencing your experiments.
{{% /pageinfo %}}


## Operating System

DAIC runs the {{< external-link "https://en.wikipedia.org/wiki/CentOS" "CentOS" >}} 7 Linux distribution, which provides the general Linux software. Most common software, including programming languages, libraries and development files for compiling your own software, is installed on the servers (see [Available software and libraries](available_software)). However, a not-so-common program that you need might not be installed. Similarly, if your research requires a state-of-the-art program that is not (yet) available as a package for {{< external-link "https://en.wikipedia.org/wiki/CentOS" "CentOS" >}} 7, then it is not available. See [Installing software](installing_software) for more information. 

## Job Scheduling Software (Slurm)

DAIC uses the {{< external-link "https://slurm.schedmd.com/" "Slurm scheduler" >}} to efficiently manage workloads. All jobs for the cluster have to be submitted as batch jobs into a queue. The scheduler then manages and prioritizes the jobs in the queue, allocates resources (CPUs, memory) for the jobs, executes the jobs and enforces the resource allocations. See [the scheduler pages](../job_submissions) for more information.

<!-- 

## Libraries for Specialized Hardware or Accelerators 

## Software Licensing and Restrictions

## Examples and Tutorials demonstrating the usage of specific software or libraries (eg, AI frameworks like TensorFlow or PyTorch, R scripts, .. etc) on different computing resources 
-->

