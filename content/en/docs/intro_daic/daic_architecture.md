---
title: "Hardware infrastructure"
linkTitle: "Hardware infrastructure"
weight: 3
description: >
  What are the components of the DAIC cluster?
---


## Compute Nodes: CPUs and GPUs

DAIC compute nodes are all multi CPU servers, with large memories, and some with GPUs. The nodes in the cluster are heterogeneous, i.e. they have different types of hardware (processors, memory, GPUs), different functionality (some more advanced than others) and different performance characteristics. If a program requires specific features, you need to specifically request those for that job (see [Job scripts](../job_submissions/_index.md#job-scripts)). The following table gives an overview of current nodes and their characteristics:

<table>
<caption> Table 1: Counts and types of DAIC compute nodes
</caption>
<thead>
  <tr>
    <th>Number of nodes</th>
    <th>CPUs per node</th>
    <th>Cores per node</th>
    <th>GPU type</th>
    <th>GPUs per node</th>
    <th>Memory (GB)</th>
    <th>Other features</th>
  </tr>
</thead>
<tfoot><tr><td colspan="5"> <code>10gbe</code>: 10 Gigabit Ethernet network connection (upgrade from the default 1 Gigabit Ethernet connection), <code>ib</code> InfiniBand connection, <code>ssd</code>Solid-State Disk for <code>/tmp</code> storage (instead of the default spinning disk), <code>`bigmem`</code>, <code>imphysexclusive</code>, <code>`avx512`</code>, <code>gpumem32</code>, <code>nvme</code>
</td></tr></tfoot>
<tbody>
  <tr>
    <td>4</td>
    <td>32</td>
    <td>8</td>
    <td>-</td>
    <td>-</td>
    <td>250</td>
    <td>ib,ssd</td>
  </tr>
  <tr>
    <td>1</td>
    <td>56</td>
    <td>14</td>
    <td>v100</td>
    <td>2</td>
    <td>500</td>
    <td>10gbe,bigmem,ssd</td>
  </tr>
  <tr>
    <td>12</td>
    <td>56</td>
    <td>14</td>
    <td>-</td>
    <td>-</td>
    <td>500</td>
    <td>ib,imphysexclusive</td>
  </tr>
  <tr>
    <td>8</td>
    <td>56</td>
    <td>14</td>
    <td>-</td>
    <td>-</td>
    <td>250</td>
    <td>ib,ssd</td>
  </tr>
  <tr>
    <td>1</td>
    <td>64</td>
    <td>16</td>
    <td>pascal</td>
    <td>5</td>
    <td>250</td>
    <td>10gbe</td>
  </tr>
  <tr>
    <td>3</td>
    <td>64</td>
    <td>16</td>
    <td>pascal</td>
    <td>8</td>
    <td>250</td>
    <td>10gbe</td>
  </tr>
  <tr>
    <td>1</td>
    <td>64</td>
    <td>16</td>
    <td>p100</td>
    <td>2</td>
    <td>750</td>
    <td>10gbe,avx512,bigmem</td>
  </tr>
  <tr>
    <td>2</td>
    <td>64</td>
    <td>16</td>
    <td>turing</td>
    <td>4</td>
    <td>750</td>
    <td>10gbe,avx512,bigmem,ssd</td>
  </tr>
  <tr>
    <td>1</td>
    <td>64</td>
    <td>16</td>
    <td>-</td>
    <td>-</td>
    <td>750</td>
    <td>10gbe,avx512,bigmem,ssd</td>
  </tr>
  <tr>
    <td>1</td>
    <td>64</td>
    <td>16</td>
    <td>v100</td>
    <td>8</td>
    <td>1500</td>
    <td>10gbe,avx512,gpumem32,ssd</td>
  </tr>
  <tr>
    <td>1</td>
    <td>64</td>
    <td>16</td>
    <td>turing</td>
    <td>8</td>
    <td>375</td>
    <td>10gbe,avx512,nvme,ssd</td>
  </tr>
  <tr>
    <td>2</td>
    <td>64</td>
    <td>16</td>
    <td>turing</td>
    <td>4</td>
    <td>185</td>
    <td>10gbe,avx512,ssd</td>
  </tr>
  <tr>
    <td>1</td>
    <td>64</td>
    <td>16</td>
    <td>-</td>
    <td>-</td>
    <td>750</td>
    <td>10gbe,bigmem</td>
  </tr>
  <tr>
    <td>2</td>
    <td>64</td>
    <td>32</td>
    <td>-</td>
    <td>-</td>
    <td>250</td>
    <td>10gbe,ssd</td>
  </tr>
  <tr>
    <td>1</td>
    <td>72</td>
    <td>18</td>
    <td>v100</td>
    <td>1</td>
    <td>375</td>
    <td>10gbe,avx512,gpumem32,nvme,ssd</td>
  </tr>
  <tr>
    <td>4</td>
    <td>72</td>
    <td>18</td>
    <td>-</td>
    <td>-</td>
    <td>375</td>
    <td>ib,ssd</td>
  </tr>
  <tr>
    <td>11</td>
    <td>96</td>
    <td>24</td>
    <td>a40</td>
    <td>3</td>
    <td>500</td>
    <td>10gbe,bigmem,gpumem32,ssd</td>
  </tr>
  <tr>
    <td>2</td>
    <td>128</td>
    <td>32</td>
    <td>-</td>
    <td>-</td>
    <td>500</td>
    <td>10gbe,bigmem,ssd</td>
  </tr>
  <tr>
    <td>1</td>
    <td>128</td>
    <td>32</td>
    <td>-</td>
    <td>-</td>
    <td>250</td>
    <td>10gbe,ssd</td>
  </tr>
</tbody>
</table>

{{% alert title="Note" color="info" %}}
All servers have [Advanced Vector Extensions](https://en.wikipedia.org/wiki/Advanced_Vector_Extensions) 1 and 2 (AVX, AVX2) support, and hyper-threading processors (two CPUs per core, always allocated in pairs) `ht`.
{{% /alert %}}

### CPUs

All nodes have multiple Central Processing Units (CPUs) that perform the operations. Each CPU can process one thread (i.e. a separate string of computer code) at a time. A computer program consists of one or multiple threads, and thus needs one or multiple CPUs simultaneously to do its computations(see [wikipedia's CPU page](https://en.wikipedia.org/wiki/Central_processing_unit)).


{{% alert title="Note" color="info" %}}
Most programs use a fixed number of threads. Requesting more CPUs for a program than its number of threads will not make it any faster because it won't know how to use the extra CPUs. When a program has less CPUs available than its number of threads, the threads will have to time-share the available CPUs (i.e. each thread only gets part-time use of a CPU), and, as a result, the program will run slower (And even slower because of the added overhead of the switching of the threads). So it's always necessary to match the number of CPUs to the number of threads, or the other way around. See [Job scripts](http://localhost:1313/DAICdocumentation/docs/job_submissions/#job-scripts) for setting resources for batch jobs.
{{% /alert %}}

The number of threads running simultaneously determines the load of a server. If the number of running threads is equal to the number of available CPUs, the server is loaded 100% (or 1.00). When the number of threads that want to run exceed the number of available CPUs, the load rises above 100%.

The CPU functionality is provided by the hardware cores in the processor chips in the machines. Traditionally, one physical core contained one logical CPU, thus the CPUs operated completely independent. Most current chips feature hyper-threading: one core contains two (or more) logical CPUs. These CPUs share parts of the core and the cache, so one CPU may have to wait when a shared resource is in use by the other CPU. Therefore these CPUs are always allocated in pairs by the job scheduler. 

### Memory
All machines have large main memories for performing computations on big data sets. A job cannot use more than it's allocated amount of memory. If it needs to use more memory, it will fail or be killed. It's not possible to combine the memory from multiple nodes for a single task. 32-bit programs can only address (use) up to 3Gb (gigabytes) of memory. See [Job scripts](http://localhost:1313/DAICdocumentation/docs/job_submissions/#job-scripts) for setting resources for batch jobs.

### GPUs

A few types of GPUs are available in some of DAIC nodes, as shown in table 1. The total numbers of these GPUs/type and their technical specifications are shown in table 2. See [Jobs on GPU resources](../job_submissions/_index.md#jobs-on-gpu-resources) for requesting a certain GPU for a computational job.


{{% alert title="Stop!" color="warning"%}}
It’s forbidden to use DAIC GPUs for anything other than research!
{{% /alert %}}

<table style="undefined;table-layout: fixed; width: 727px">
<colgroup>
<col style="width: 131px">
<col style="width: 48px">
<col style="width: 198px">
<col style="width: 93px">
<col style="width: 82px">
<col style="width: 97px">
<col style="width: 78px">
</colgroup>
<caption> Table 2: Counts and specifications of DAIC GPUs
</caption>
<thead>
  <tr>
    <th>GPU type<br></th>
    <th>Count</th>
    <th>Model </th>
    <th>Architecture</th>
    <th>Compute Capability </th>
    <th>CUDA cores </th>
    <th>Memory</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>a40</td>
    <td>33</td>
    <td>NVIDIA A40</td>
    <td>Ampere</td>
    <td>8.6</td>
    <td>10752</td>
    <td>46068 MiB</td>
  </tr>
  <tr>
    <td>p100</td>
    <td>2</td>
    <td>Tesla P100-PCIE-16GB</td>
    <td>Pascal</td>
    <td>6.0</td>
    <td>3584</td>
    <td>16384 MiB</td>
  </tr>
  <tr>
    <td>pascal</td>
    <td>29</td>
    <td>GeForce GTX 1080 Ti</td>
    <td>Pascal</td>
    <td>6.1</td>
    <td>3584</td>
    <td>11264 MiB</td>
  </tr>
  <tr>
    <td>turing</td>
    <td>24</td>
    <td>NVIDIA GeForce RTX 2080 Ti</td>
    <td>Turing</td>
    <td>7.5</td>
    <td>4352</td>
    <td>11264 MiB</td>
  </tr>
  <tr>
    <td>v100</td>
    <td>11</td>
    <td>Tesla V100-SXM2-32GB</td>
    <td>Volta</td>
    <td>7.0</td>
    <td>5120</td>
    <td>32768 MiB</td>
  </tr>
</tbody>
</table>

In table 2: the headers denote:
<ul>
  <li><code>Model</code>: The official product name of the GPU</li>
  <li><code>Architecture</code>: The hardware design used, and thus the hardware specifications and performance characteristics of the GPU. Each new architecture brings forward a new generation of GPUs. </li>
  <li><code>Compute capability</code>: determines the general functionality, available features and CUDA support of the GPU. A GPU with a higher capability supports more advanced functionality. </li>
  <li><code>CUDA cores</code>: The number of cores perform the computations: The more cores, the more work can be done in parallel (provided that the algorithm can make use of higher parallelization). </li>
  <li><code>Memory</code>: Total installed GPU memory. The GPUs provide their own internal (fixed-size) memory for storing data for GPU computations. All required data needs to fit in the internal memory or your computations will suffer a big performance penalty. </li>
</ul>

{{% alert title="Note" color="info" %}}
To inspect a given GPU and obtain the data of table 2, you can run the following commands on an interactive session or an sbatch script (see [Jobs on GPU resources](../job_submissions/_index.md#jobs-on-gpu-resources)). The apptainer image used in this code snippet was built as demonstrated in the [Building images tutorial](../../tutorials/container_images/_index.md#building-images).

```bash
$ sinteractive --cpus-per-task=2 --mem=500 --time=00:02:00 --gres=gpu
Note: interactive sessions are automatically terminated when they reach their time limit (1 hour)!
srun: job 8607783 queued and waiting for resources
srun: job 8607783 has been allocated resources
15:50:29 up 51 days,  3:26,  0 users,  load average: 60,33, 59,72, 54,65
SomeNetID@influ1:~$
SomeNetID@influ1:~$
SomeNetID@influ1:~$ nvidia-smi  --format=csv,noheader --query-gpu=name	
NVIDIA GeForce RTX 2080 Ti
SomeNetID@influ1:~$
SomeNetID@influ1:~$ 
SomeNetID@influ1:~$ nvidia-smi -q | grep Architecture	
Product Architecture                  : Turing                                                                     
SomeNetID@influ1:~$
SomeNetID@influ1:~$
SomeNetID@influ1:~$ nvidia-smi --query-gpu=compute_cap --format=csv,noheader
7.5	
SomeNetID@influ1:~$
SomeNetID@influ1:~$
SomeNetID@influ1:~$ apptainer run --nv  cuda_based_image.sif | grep "CUDA Cores"	 # using the apptainer image of the tutorial
(068) Multiprocessors, (064) CUDA Cores/MP:    4352 CUDA Cores
SomeNetID@influ1:~$
SomeNetID@influ1:~$
SomeNetID@influ1:~$ nvidia-smi  --format=csv,noheader --query-gpu=memory.total
11264 MiB
SomeNetID@influ1:~$
SomeNetID@influ1:~$ exit
```

{{% /alert %}}




## ~~Storage Systems~~


## ~~Networking~~


## DAIC compared with other TU Delft clusters

For an overview of other compute environments accessible to TU Delft affiliates and their collaborators, see [TU Delft clusters comparison](../../HPC_users/_index.md#tu-delft-clusters)

