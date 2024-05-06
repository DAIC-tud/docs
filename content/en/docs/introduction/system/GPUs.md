---
title: "GPUs"
linkTitle: "GPUs"
weight: 25
description: >
  What graphical processing units are available?
---

A few types of GPUs are available in some of DAIC nodes, as shown in table 1. The total numbers of these GPUs/type and their technical specifications are shown in table 2. See [using graphic cards](/docs/manual/job-submission/job-gpu) for requesting GPUs for a computational job.

<table style="undefined;table-layout: fixed; width: 727px">
<colgroup>
<col style="width: 131px">
<col style="width: 148px">
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
    <th>GPU (slurm) type<br></th>
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
    <td>66</td>
    <td>NVIDIA A40</td>
    <td>Ampere</td>
    <td>8.6</td>
    <td>10752</td>
    <td>46068 MiB</td>
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
To inspect a given GPU and obtain the data of table 2, you can run the following commands on an interactive session or an sbatch script (see [Jobs on GPU resources](/docs/manual/job-submission/job-gpu)). The apptainer image used in this code snippet was built as demonstrated in the [containerization tutorial](/tutorials/containerization/).

```bash
$ sinteractive --cpus-per-task=2 --mem=500 --time=00:02:00 --gres=gpu
Note: interactive sessions are automatically terminated when they reach their time limit (1 hour)!
srun: job 8607783 queued and waiting for resources
srun: job 8607783 has been allocated resources
15:50:29 up 51 days,  3:26,  0 users,  load average: 60,33, 59,72, 54,65

SomeNetID@influ1:~$ nvidia-smi  --format=csv,noheader --query-gpu=name	
NVIDIA GeForce RTX 2080 Ti

SomeNetID@influ1:~$ nvidia-smi -q | grep Architecture	
Product Architecture                  : Turing                                                                     

SomeNetID@influ1:~$ nvidia-smi --query-gpu=compute_cap --format=csv,noheader
7.5	

SomeNetID@influ1:~$ apptainer run --nv  cuda_based_image.sif | grep "CUDA Cores"	 # using the apptainer image of the tutorial
(068) Multiprocessors, (064) CUDA Cores/MP:    4352 CUDA Cores

SomeNetID@influ1:~$ nvidia-smi  --format=csv,noheader --query-gpu=memory.total
11264 MiB

SomeNetID@influ1:~$ exit
```

{{% /alert %}}
