---
title: "CPUs"
linkTitle: "CPUs"
weight: 20
description: >
  What CPU units are available?
---

All nodes have multiple Central Processing Units (CPUs) that perform the operations. Each CPU can process one thread (i.e. a separate string of computer code) at a time. A computer program consists of one or multiple threads, and thus needs one or multiple CPUs simultaneously to do its computations (see {{< external-link "https://en.wikipedia.org/wiki/Central_processing_unit" "wikipedia's CPU page" >}} ).


{{% alert title="Note" color="info" %}}
Most programs use a fixed number of threads. Requesting more CPUs for a program than its number of threads will not make it any faster because it won't know how to use the extra CPUs. When a program has less CPUs available than its number of threads, the threads will have to time-share the available CPUs (i.e. each thread only gets part-time use of a CPU), and, as a result, the program will run slower (And even slower because of the added overhead of the switching of the threads). So it's always necessary to match the number of CPUs to the number of threads, or the other way around. See [submitting jobs](../../../manual/job-submission/job-scripts) for setting resources for batch jobs.
{{% /alert %}}

The number of threads running simultaneously determines the load of a server. If the number of running threads is equal to the number of available CPUs, the server is loaded 100% (or 1.00). When the number of threads that want to run exceed the number of available CPUs, the load rises above 100%.

The CPU functionality is provided by the hardware cores in the processor chips in the machines. Traditionally, one physical core contained one logical CPU, thus the CPUs operated completely independent. Most current chips feature hyper-threading: one core contains two (or more) logical CPUs. These CPUs share parts of the core and the cache, so one CPU may have to wait when a shared resource is in use by the other CPU. Therefore these CPUs are always allocated in pairs by the job scheduler. 


