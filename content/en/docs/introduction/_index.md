---
title: "Introduction"
weight: 1
description: >
  What are the foundational components of DAIC?
---

### What is an HPC cluster?
A High Performance Computing (HPC) cluster, is a collection of (large) computing resources, like Processors (CPUs), Graphics processors (GPUs), Memory and Storage, that are shared among a group of users. Using multiple computers as such makes it possible to perform lengthy and resource-intense computations beyond the capabilities of a single computer, and is especially handy for modern scientific computing applications where datasets are typically large in size, models are big in parameters' size and complexity, and computations need specialized hardware (like GPUs and FPGAs). 


### What is DAIC?

The Delft AI Cluster (DAIC), formerly known as INSY-HPC or just plainly HPC, is a TU Delft High Performance Computing (HPC) cluster consisting of Linux [compute nodes (ie servers)](docs/system/#compute-nodes) with a lot of processing power and memory for running large, long or GPU-enabled jobs. 

From a CS only cluster in 2015, DAIC has grown in time to serve researchers across many TU Delft departments but maintained the needs of CS and AI in each expansion phase. Today, DAIC nodes are organized as [partitions](/docs/manual/job-submission/partitions/) that correspond to the groups contributing these resources. (See [Contributing departments](/docs/introduction/contributors-funders/#contributing-departments) and [TU Delft clusters comparison](/docs/introduction/tud-clusters/)). 


{{< figure src="/img/DAIC_partitions.png" caption="DAIC partitions and access/usage best practices" ref="fig:daic_partitions" width="750px">}}
