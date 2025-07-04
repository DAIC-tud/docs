---
title: "Compute nodes"
weight: 3
description: >
  The foundational hardware components of DAIC.
---

DAIC compute nodes are high-performance servers with multiple CPUs, large memory, and, on many nodes, one or more GPUs. The cluster is _heterogeneous_: nodes vary in processor types, memory sizes, GPU configurations, and performance characteristics.

If your application requires specific hardware features, you must request them explicitly in your job script (see [Submitting jobs](/docs/manual/job-submission/slurm-basics/)).



<!-- {{% alert title="Note" color="info" %}}
You can use Slurm’s `sinfo` command to view an overview of compute nodes and their characteristics. For example:

```bash
sinfo --all -N -o "%N %P %c %m %G %b"
```
This shows the node name, partition(s), number of CPUs, memory size, generic resources (e.g., GPUs), and active features.  The `--all` flag is important: without it, group-specific partitions (beyond `general`) will not be shown.

Check out the [Slurm's sinfo page](https://slurm.schedmd.com/sinfo.html) and  [wikipedia's awk page](https://en.wikipedia.org/wiki/AWK) for more  details, or explore tools like `scontrol` and sque`ue to inspect specific jobs or nodes.

{{% /alert %}} -->



### CPUs

All compute nodes have multiple CPUs (sockets), each with multiple cores. Most nodes support hyper-threading, which allows two threads per physical core. The number of cores per node is listed in the [List of all nodes](#list-of-all-nodes) section.

Request CPUs based on how many threads your program can use. Oversubscribing doesn’t improve performance and may waste resources. Undersubscribing may slow your job due to thread contention.

> To request CPUs for your jobs, see [Job scripts](docs/manual/job-submission/slurm-basics/).


### GPUs

Many nodes in DAIC include one or more NVIDIA GPUs.GPU types differ in architecture, memory size, and compute capability. The table that follows summarizes the main GPU types in DAIC. For a per-node overview, see the [List of all nodes](#list-of-all-nodes) section.

> To request GPUs in your job, use `--gres=gpu:<type>:<count>`. See [GPU jobs](/docs/manual/job-submission/slurm-basics/#using-gpu-resources) for more information.


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
<caption> Table 1: Counts and specifications of DAIC GPUs
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
    <td>l40</td>
    <td>18</td>
    <td>NVIDIA L40</td>
    <td>Ada Lovelace</td>
    <td>8.9</td>
    <td>18176</td>
    <td>49152 MiB</td>
  </tr>
  <tr>
    <td>a40</td>
    <td>84</td>
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

In table 1: the headers denote:

**Model**
: The official product name of the GPU

**Architecture**
: The hardware design used in the GPU, which defines its specifications and performance characteristics. Each architecture (e.g., Ampere, Turing, Volta) represents a different GPU generation.

**Compute capability**
: A version number indicating the features supported by the GPU, including CUDA support. Higher values offer more advanced functionality.

**CUDA cores**
: The number of processing cores available on the GPU. More CUDA cores allow more parallel operations, improving performance for parallelizable workloads.

**Memory**
: The total internal memory on the GPU. This memory is required to store data for GPU computations. If a model’s memory is insufficient, performance may be severely affected.

### Memory

Each node has a fixed amount of RAM, shown in the [List of all nodes](#list-of-all-nodes) section. Jobs may only use the memory explicitly requested using `--mem` or `--mem-per-cpu`. Exceeding the allocation may result in job failure.

Memory cannot be shared across nodes, and unused memory cannot be reallocated.

> For memory-efficient jobs, consider tuning your requested memorey to match your code's peak usage closely. Fore more information, see [Slurm basics](/docs/manual/job-submission/slurm-basics/).


{{% alert title="Note" color="info" %}}
All compute nodes support [Advanced Vector Extensions](https://en.wikipedia.org/wiki/Advanced_Vector_Extensions) 1 and 2 (AVX, AVX2), and use hyper-threading (`ht`), i.e, each physical core provides two logical CPUs. These are always allocated in pairs by the job scheduler (see [Workload Scheduler](docs/system/scheduler)).
{{% /alert %}}

### List of all nodes
The following table gives an overview of current nodes and their characteristics. Use the search bar to filter by hostname, GPU type, or any other column, and select columns to be visible. 
<!-- The "Controller" column refers to the onboard network controller. -->

{{% alert title="Note" color="info" %}}
Slurm partitions typically correspond to research groups or departments that have contributed compute resources to the cluster. Most partition names follow the format `<faculty>-<department>` or `<faculty>-<department>-<section>`. A few exceptions exist for project-specific nodes.

For more information, see the [Partitions](/docs/manual/job-submission/priorities/#partitions) section.
{{% /alert %}}






<table id="nodes-table" class="display">
<thead>
  <tr>
    <th>Hostname</th>
    <th>CPU (Sockets x Model)</th>
    <th>Cores per Socket</th>
    <th>Total Cores</th>
    <th>CPU Speed (MHz)</th>
    <th>Total RAM (GiB)</th>
    <th>Local Disk (/tmp, GiB)</th>
    <th>GPU Type</th>
    <th>GPU Count</th>
    <th>SlurmPartitions</th>
    <th>SlurmActiveFeatures</th>
  </tr></thead>
<tbody>
  <tr>
    <td>100plus</td>
    <td>2 x Intel(R) Xeon(R) CPU E5-2683 v4 @ 2.10GHz</td>
    <td>16</td>
    <td>32</td>
    <td>2097.594</td>
    <td>755</td>
    <td>3174</td>
    <td>N/A</td>
    <td>0</td>
    <td>general;ewi-insy</td>
    <td>avx;avx2;ht;10gbe;bigmem</td>
  </tr>
  <tr>
    <td>3dgi1</td>
    <td>1 x AMD EPYC 7502P 32-Core Processor</td>
    <td>32</td>
    <td>32</td>
    <td>2500.000</td>
    <td>251</td>
    <td>148</td>
    <td>N/A</td>
    <td>0</td>
    <td>general;bk-ur-uds</td>
    <td>avx;avx2;ht;10gbe;ssd</td>
  </tr>
  <tr>
    <td>3dgi2</td>
    <td>1 x AMD EPYC 7502P 32-Core Processor</td>
    <td>32</td>
    <td>32</td>
    <td>2500.000</td>
    <td>251</td>
    <td>148</td>
    <td>N/A</td>
    <td>0</td>
    <td>general;bk-ur-uds</td>
    <td>avx;avx2;ht;10gbe;ssd</td>
  </tr>
  <tr>
    <td>awi01</td>
    <td>2 x Intel(R) Xeon(R) Gold 6140 CPU @ 2.30GHz</td>
    <td>18</td>
    <td>36</td>
    <td>3494.921</td>
    <td>376</td>
    <td>393</td>
    <td>Tesla V100-PCIE-32GB</td>
    <td>1</td>
    <td>general;tnw-imphys</td>
    <td>avx;avx2;ht;10gbe;avx512;gpumem32;nvme;ssd</td>
  </tr>
  <tr>
    <td>awi02</td>
    <td>2 x Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.40GHz</td>
    <td>14</td>
    <td>28</td>
    <td>2899.951</td>
    <td>504</td>
    <td>393</td>
    <td>Tesla V100-SXM2-16GB</td>
    <td>2</td>
    <td>general;tnw-imphys</td>
    <td>avx;avx2;ht;10gbe;bigmem;ssd</td>
  </tr>
  <tr>
    <td>awi04</td>
    <td>2 x Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.40GHz</td>
    <td>14</td>
    <td>28</td>
    <td>2899.951</td>
    <td>503</td>
    <td>5529</td>
    <td>N/A</td>
    <td>0</td>
    <td>general;tnw-imphys</td>
    <td>avx;avx2;ht;ib;imphysexclusive</td>
  </tr>
  <tr>
    <td>awi08</td>
    <td>2 x Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.40GHz</td>
    <td>14</td>
    <td>28</td>
    <td>2899.951</td>
    <td>503</td>
    <td>5529</td>
    <td>N/A</td>
    <td>0</td>
    <td>general;tnw-imphys</td>
    <td>avx;avx2;ht;ib;imphysexclusive</td>
  </tr>
  <tr>
    <td>awi09</td>
    <td>2 x Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.40GHz</td>
    <td>14</td>
    <td>28</td>
    <td>2899.951</td>
    <td>503</td>
    <td>5529</td>
    <td>N/A</td>
    <td>0</td>
    <td>general;tnw-imphys</td>
    <td>avx;avx2;ht;ib;imphysexclusive</td>
  </tr>
  <tr>
    <td>awi10</td>
    <td>2 x Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.40GHz</td>
    <td>14</td>
    <td>28</td>
    <td>2899.951</td>
    <td>503</td>
    <td>5529</td>
    <td>N/A</td>
    <td>0</td>
    <td>general;tnw-imphys</td>
    <td>avx;avx2;ht;ib;imphysexclusive</td>
  </tr>
  <tr>
    <td>awi11</td>
    <td>2 x Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.40GHz</td>
    <td>14</td>
    <td>28</td>
    <td>2899.951</td>
    <td>503</td>
    <td>5529</td>
    <td>N/A</td>
    <td>0</td>
    <td>general;tnw-imphys</td>
    <td>avx;avx2;ht;ib;imphysexclusive</td>
  </tr>
  <tr>
    <td>awi12</td>
    <td>2 x Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.40GHz</td>
    <td>14</td>
    <td>28</td>
    <td>2899.951</td>
    <td>503</td>
    <td>5529</td>
    <td>N/A</td>
    <td>0</td>
    <td>general;tnw-imphys</td>
    <td>avx;avx2;ht;ib;imphysexclusive</td>
  </tr>
  <tr>
    <td>awi19</td>
    <td>2 x Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.40GHz</td>
    <td>14</td>
    <td>28</td>
    <td>2899.951</td>
    <td>251</td>
    <td>856</td>
    <td>N/A</td>
    <td>0</td>
    <td>general;tnw-imphys</td>
    <td>avx;avx2;ht;ib;ssd</td>
  </tr>
  <tr>
    <td>awi20</td>
    <td>2 x Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.40GHz</td>
    <td>14</td>
    <td>28</td>
    <td>2899.951</td>
    <td>251</td>
    <td>856</td>
    <td>N/A</td>
    <td>0</td>
    <td>general;tnw-imphys</td>
    <td>avx;avx2;ht;ib;ssd</td>
  </tr>
  <tr>
    <td>awi21</td>
    <td>2 x Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.40GHz</td>
    <td>14</td>
    <td>28</td>
    <td>2899.951</td>
    <td>251</td>
    <td>856</td>
    <td>N/A</td>
    <td>0</td>
    <td>general;tnw-imphys</td>
    <td>avx;avx2;ht;ib;ssd</td>
  </tr>
  <tr>
    <td>awi22</td>
    <td>2 x Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.40GHz</td>
    <td>14</td>
    <td>28</td>
    <td>2899.951</td>
    <td>251</td>
    <td>856</td>
    <td>N/A</td>
    <td>0</td>
    <td>general;tnw-imphys</td>
    <td>avx;avx2;ht;ib;ssd</td>
  </tr>
  <tr>
    <td>awi23</td>
    <td>2 x Intel(R) Xeon(R) Gold 6140 CPU @ 2.30GHz</td>
    <td>18</td>
    <td>36</td>
    <td>2672.149</td>
    <td>376</td>
    <td>856</td>
    <td>N/A</td>
    <td>0</td>
    <td>general;tnw-imphys</td>
    <td>avx;avx2;ht;ib;ssd</td>
  </tr>
  <tr>
    <td>awi24</td>
    <td>2 x Intel(R) Xeon(R) Gold 6140 CPU @ 2.30GHz</td>
    <td>18</td>
    <td>36</td>
    <td>3299.932</td>
    <td>376</td>
    <td>856</td>
    <td>N/A</td>
    <td>0</td>
    <td>general;tnw-imphys</td>
    <td>avx;avx2;ht;ib;ssd</td>
  </tr>
  <tr>
    <td>awi25</td>
    <td>2 x Intel(R) Xeon(R) Gold 6140 CPU @ 2.30GHz</td>
    <td>18</td>
    <td>36</td>
    <td>3542.370</td>
    <td>376</td>
    <td>856</td>
    <td>N/A</td>
    <td>0</td>
    <td>general;tnw-imphys</td>
    <td>avx;avx2;ht;ib;ssd</td>
  </tr>
  <tr>
    <td>awi26</td>
    <td>2 x Intel(R) Xeon(R) Gold 6140 CPU @ 2.30GHz</td>
    <td>18</td>
    <td>36</td>
    <td>2840.325</td>
    <td>376</td>
    <td>856</td>
    <td>N/A</td>
    <td>0</td>
    <td>general;tnw-imphys</td>
    <td>avx;avx2;ht;ib;ssd</td>
  </tr>
  <tr>
    <td>cor1</td>
    <td>2 x Intel(R) Xeon(R) Gold 6242 CPU @ 2.80GHz</td>
    <td>16</td>
    <td>32</td>
    <td>3573.315</td>
    <td>1510</td>
    <td>7168</td>
    <td>Tesla V100-SXM2-32GB</td>
    <td>8</td>
    <td>general;me-cor</td>
    <td>avx;avx2;ht;10gbe;avx512;gpumem32;ssd</td>
  </tr>
  <tr>
    <td>gpu01</td>
    <td>2 x AMD EPYC 7413 24-Core Processor</td>
    <td>24</td>
    <td>48</td>
    <td>2650.000</td>
    <td>503</td>
    <td>415</td>
    <td>NVIDIA A40</td>
    <td>3</td>
    <td>general;ewi-insy</td>
    <td>avx;avx2;10gbe;bigmem;gpumem32;ssd</td>
  </tr>
  <tr>
    <td>gpu02</td>
    <td>2 x AMD EPYC 7413 24-Core Processor</td>
    <td>24</td>
    <td>48</td>
    <td>2650.000</td>
    <td>503</td>
    <td>415</td>
    <td>NVIDIA A40</td>
    <td>3</td>
    <td>general;ewi-insy</td>
    <td>avx;avx2;10gbe;bigmem;gpumem32;ssd</td>
  </tr>
  <tr>
    <td>gpu03</td>
    <td>2 x AMD EPYC 7413 24-Core Processor</td>
    <td>24</td>
    <td>48</td>
    <td>2650.000</td>
    <td>503</td>
    <td>415</td>
    <td>NVIDIA A40</td>
    <td>3</td>
    <td>general;ewi-insy</td>
    <td>avx;avx2;10gbe;bigmem;gpumem32;ssd</td>
  </tr>
  <tr>
    <td>gpu04</td>
    <td>2 x AMD EPYC 7413 24-Core Processor</td>
    <td>24</td>
    <td>48</td>
    <td>2650.000</td>
    <td>503</td>
    <td>415</td>
    <td>NVIDIA A40</td>
    <td>3</td>
    <td>general;ewi-insy</td>
    <td>avx;avx2;10gbe;bigmem;gpumem32;ssd</td>
  </tr>
  <tr>
    <td>gpu05</td>
    <td>2 x AMD EPYC 7413 24-Core Processor</td>
    <td>24</td>
    <td>48</td>
    <td>2650.000</td>
    <td>503</td>
    <td>415</td>
    <td>NVIDIA A40</td>
    <td>3</td>
    <td>general;ewi-st</td>
    <td>avx;avx2;10gbe;bigmem;gpumem32;ssd</td>
  </tr>
  <tr>
    <td>gpu06</td>
    <td>2 x AMD EPYC 7413 24-Core Processor</td>
    <td>24</td>
    <td>48</td>
    <td>2650.000</td>
    <td>503</td>
    <td>415</td>
    <td>NVIDIA A40</td>
    <td>3</td>
    <td>general;ewi-st</td>
    <td>avx;avx2;10gbe;bigmem;gpumem32;ssd</td>
  </tr>
  <tr>
    <td>gpu07</td>
    <td>2 x AMD EPYC 7413 24-Core Processor</td>
    <td>24</td>
    <td>48</td>
    <td>2650.000</td>
    <td>503</td>
    <td>415</td>
    <td>NVIDIA A40</td>
    <td>3</td>
    <td>general;ewi-st</td>
    <td>avx;avx2;10gbe;bigmem;gpumem32;ssd</td>
  </tr>
  <tr>
    <td>gpu08</td>
    <td>2 x AMD EPYC 7413 24-Core Processor</td>
    <td>24</td>
    <td>48</td>
    <td>2650.000</td>
    <td>503</td>
    <td>415</td>
    <td>NVIDIA A40</td>
    <td>3</td>
    <td>general;ewi-st</td>
    <td>avx;avx2;10gbe;bigmem;gpumem32;ssd</td>
  </tr>
  <tr>
    <td>gpu09</td>
    <td>2 x AMD EPYC 7413 24-Core Processor</td>
    <td>24</td>
    <td>48</td>
    <td>2650.000</td>
    <td>503</td>
    <td>415</td>
    <td>NVIDIA A40</td>
    <td>3</td>
    <td>general;tnw-imphys</td>
    <td>avx;avx2;10gbe;bigmem;gpumem32;ssd</td>
  </tr>
  <tr>
    <td>gpu10</td>
    <td>2 x AMD EPYC 7413 24-Core Processor</td>
    <td>24</td>
    <td>48</td>
    <td>2650.000</td>
    <td>503</td>
    <td>415</td>
    <td>NVIDIA A40</td>
    <td>3</td>
    <td>general;tnw-imphys</td>
    <td>avx;avx2;10gbe;bigmem;gpumem32;ssd</td>
  </tr>
  <tr>
    <td>gpu11</td>
    <td>2 x AMD EPYC 7413 24-Core Processor</td>
    <td>24</td>
    <td>48</td>
    <td>2650.000</td>
    <td>503</td>
    <td>415</td>
    <td>NVIDIA A40</td>
    <td>3</td>
    <td>bk-ur-uds;general</td>
    <td>avx;avx2;10gbe;bigmem;gpumem32;ssd</td>
  </tr>
  <tr>
    <td>gpu12</td>
    <td>2 x AMD EPYC 7413 24-Core Processor</td>
    <td>24</td>
    <td>48</td>
    <td>2650.000</td>
    <td>503</td>
    <td>415</td>
    <td>NVIDIA A40</td>
    <td>3</td>
    <td>general;ewi-st</td>
    <td>avx;avx2;10gbe;bigmem;gpumem32;ssd</td>
  </tr>
  <tr>
    <td>gpu14</td>
    <td>2 x AMD EPYC 7543 32-Core Processor</td>
    <td>32</td>
    <td>64</td>
    <td>2800.000</td>
    <td>503</td>
    <td>856</td>
    <td>NVIDIA A40</td>
    <td>3</td>
    <td>general;ewi-st</td>
    <td>avx;avx2;10gbe;bigmem;gpumem32;ssd</td>
  </tr>
  <tr>
    <td>gpu15</td>
    <td>2 x AMD EPYC 7543 32-Core Processor</td>
    <td>32</td>
    <td>64</td>
    <td>2800.000</td>
    <td>503</td>
    <td>856</td>
    <td>NVIDIA A40</td>
    <td>3</td>
    <td>general;ewi-st</td>
    <td>avx;avx2;10gbe;bigmem;gpumem32;ssd</td>
  </tr>
  <tr>
    <td>gpu16</td>
    <td>2 x AMD EPYC 7543 32-Core Processor</td>
    <td>32</td>
    <td>64</td>
    <td>2800.000</td>
    <td>503</td>
    <td>856</td>
    <td>NVIDIA A40</td>
    <td>3</td>
    <td>general;ewi-st</td>
    <td>avx;avx2;10gbe;bigmem;gpumem32;ssd</td>
  </tr>
  <tr>
    <td>gpu17</td>
    <td>2 x AMD EPYC 7543 32-Core Processor</td>
    <td>32</td>
    <td>64</td>
    <td>2800.000</td>
    <td>503</td>
    <td>856</td>
    <td>NVIDIA A40</td>
    <td>3</td>
    <td>general;ewi-st</td>
    <td>avx;avx2;10gbe;bigmem;gpumem32;ssd</td>
  </tr>
  <tr>
    <td>gpu18</td>
    <td>2 x AMD EPYC 7543 32-Core Processor</td>
    <td>32</td>
    <td>64</td>
    <td>2800.000</td>
    <td>503</td>
    <td>856</td>
    <td>NVIDIA A40</td>
    <td>3</td>
    <td>general;ewi-st</td>
    <td>avx;avx2;10gbe;bigmem;gpumem32;ssd</td>
  </tr>
  <tr>
    <td>gpu19</td>
    <td>2 x AMD EPYC 7543 32-Core Processor</td>
    <td>32</td>
    <td>64</td>
    <td>2800.000</td>
    <td>503</td>
    <td>856</td>
    <td>NVIDIA A40</td>
    <td>3</td>
    <td>general;ewi-insy</td>
    <td>avx;avx2;10gbe;bigmem;gpumem32;ssd</td>
  </tr>
  <tr>
    <td>gpu20</td>
    <td>2 x AMD EPYC 7543 32-Core Processor</td>
    <td>32</td>
    <td>64</td>
    <td>2800.000</td>
    <td>1007</td>
    <td>856</td>
    <td>NVIDIA A40</td>
    <td>3</td>
    <td>general;ewi-insy</td>
    <td>avx;avx2;10gbe;bigmem;gpumem32;ssd</td>
  </tr>
  <tr>
    <td>gpu21</td>
    <td>2 x AMD EPYC 7543 32-Core Processor</td>
    <td>32</td>
    <td>64</td>
    <td>2800.000</td>
    <td>1007</td>
    <td>856</td>
    <td>NVIDIA A40</td>
    <td>3</td>
    <td>general;ewi-insy-prb;ewi-insy</td>
    <td>avx;avx2;10gbe;bigmem;gpumem32;ssd</td>
  </tr>
  <tr>
    <td>gpu22</td>
    <td>2 x AMD EPYC 7543 32-Core Processor</td>
    <td>32</td>
    <td>64</td>
    <td>2800.000</td>
    <td>1007</td>
    <td>856</td>
    <td>NVIDIA A40</td>
    <td>3</td>
    <td>general;ewi-insy</td>
    <td>avx;avx2;10gbe;bigmem;gpumem32;ssd</td>
  </tr>
  <tr>
    <td>gpu23</td>
    <td>2 x AMD EPYC 7543 32-Core Processor</td>
    <td>32</td>
    <td>64</td>
    <td>2800.000</td>
    <td>1007</td>
    <td>856</td>
    <td>NVIDIA A40</td>
    <td>3</td>
    <td>general;ewi-insy</td>
    <td>avx;avx2;10gbe;bigmem;gpumem32;ssd</td>
  </tr>
  <tr>
    <td>gpu24</td>
    <td>2 x AMD EPYC 7543 32-Core Processor</td>
    <td>32</td>
    <td>64</td>
    <td>2800.000</td>
    <td>1007</td>
    <td>856</td>
    <td>NVIDIA A40</td>
    <td>3</td>
    <td>general;ewi-insy</td>
    <td>avx;avx2;10gbe;bigmem;gpumem32;ssd</td>
  </tr>
  <tr>
    <td>gpu25</td>
    <td>2 x AMD EPYC 7543 32-Core Processor</td>
    <td>32</td>
    <td>64</td>
    <td>2800.000</td>
    <td>1007</td>
    <td>856</td>
    <td>NVIDIA A40</td>
    <td>3</td>
    <td>mmll;general;ewi-insy</td>
    <td>avx;avx2;10gbe;bigmem;gpumem32;ssd</td>
  </tr>
  <tr>
    <td>gpu26</td>
    <td>2 x AMD EPYC 7543 32-Core Processor</td>
    <td>32</td>
    <td>64</td>
    <td>2800.000</td>
    <td>1007</td>
    <td>856</td>
    <td>NVIDIA A40</td>
    <td>3</td>
    <td>lr-asm;general</td>
    <td>avx;avx2;10gbe;bigmem;gpumem32;ssd</td>
  </tr>
  <tr>
    <td>gpu27</td>
    <td>2 x AMD EPYC 7543 32-Core Processor</td>
    <td>32</td>
    <td>64</td>
    <td>2800.000</td>
    <td>503</td>
    <td>856</td>
    <td>NVIDIA A40</td>
    <td>3</td>
    <td>me-cor;general</td>
    <td>avx;avx2;10gbe;bigmem;gpumem32;ssd</td>
  </tr>
  <tr>
    <td>gpu28</td>
    <td>2 x AMD EPYC 7543 32-Core Processor</td>
    <td>32</td>
    <td>64</td>
    <td>2800.000</td>
    <td>503</td>
    <td>856</td>
    <td>NVIDIA A40</td>
    <td>3</td>
    <td>me-cor;general</td>
    <td>avx;avx2;10gbe;bigmem;gpumem32;ssd</td>
  </tr>
  <tr>
    <td>gpu29</td>
    <td>2 x AMD EPYC 7543 32-Core Processor</td>
    <td>32</td>
    <td>64</td>
    <td>2800.000</td>
    <td>503</td>
    <td>856</td>
    <td>NVIDIA A40</td>
    <td>3</td>
    <td>me-cor;general</td>
    <td>avx;avx2;10gbe;bigmem;gpumem32;ssd</td>
  </tr>
  <tr>
    <td>gpu30</td>
    <td>1 x AMD EPYC 9534 64-Core Processor</td>
    <td>64</td>
    <td>64</td>
    <td>2450.000</td>
    <td>755</td>
    <td>856</td>
    <td>NVIDIA L40</td>
    <td>3</td>
    <td>ewi-insy;general</td>
    <td>avx;avx2;10gbe;bigmem;gpumem32;ssd</td>
  </tr>
  <tr>
    <td>gpu31</td>
    <td>1 x AMD EPYC 9534 64-Core Processor</td>
    <td>64</td>
    <td>64</td>
    <td>2450.000</td>
    <td>755</td>
    <td>856</td>
    <td>NVIDIA L40</td>
    <td>3</td>
    <td>ewi-insy;general</td>
    <td>avx;avx2;10gbe;bigmem;gpumem32;ssd</td>
  </tr>
  <tr>
    <td>gpu32</td>
    <td>1 x AMD EPYC 9534 64-Core Processor</td>
    <td>64</td>
    <td>64</td>
    <td>2450.000</td>
    <td>755</td>
    <td>856</td>
    <td>NVIDIA L40</td>
    <td>3</td>
    <td>ewi-me-sps;general</td>
    <td>avx;avx2;10gbe;bigmem;gpumem32;ssd</td>
  </tr>
  <tr>
    <td>gpu33</td>
    <td>1 x AMD EPYC 9534 64-Core Processor</td>
    <td>64</td>
    <td>64</td>
    <td>2450.000</td>
    <td>755</td>
    <td>856</td>
    <td>NVIDIA L40</td>
    <td>3</td>
    <td>lr-co;general</td>
    <td>avx;avx2;10gbe;bigmem;gpumem32;ssd</td>
  </tr>
  <tr>
    <td>gpu34</td>
    <td>1 x AMD EPYC 9534 64-Core Processor</td>
    <td>64</td>
    <td>64</td>
    <td>2450.000</td>
    <td>755</td>
    <td>856</td>
    <td>NVIDIA L40</td>
    <td>3</td>
    <td>ewi-insy;general</td>
    <td>avx;avx2;10gbe;bigmem;gpumem32;ssd</td>
  </tr>
  <tr>
    <td>gpu35</td>
    <td>1 x AMD EPYC 9534 64-Core Processor</td>
    <td>64</td>
    <td>64</td>
    <td>2450.000</td>
    <td>755</td>
    <td>856</td>
    <td>NVIDIA L40</td>
    <td>3</td>
    <td>bk-ar;general</td>
    <td>avx;avx2;10gbe;bigmem;gpumem32;ssd</td>
  </tr>
  <tr>
    <td>grs1</td>
    <td>2 x Intel(R) Xeon(R) CPU E5-2667 v4 @ 3.20GHz</td>
    <td>8</td>
    <td>16</td>
    <td>3499.804</td>
    <td>251</td>
    <td>181</td>
    <td>N/A</td>
    <td>0</td>
    <td>citg-grs;general</td>
    <td>avx;avx2;ht;ib;ssd</td>
  </tr>
  <tr>
    <td>grs2</td>
    <td>2 x Intel(R) Xeon(R) CPU E5-2667 v4 @ 3.20GHz</td>
    <td>8</td>
    <td>16</td>
    <td>3499.804</td>
    <td>251</td>
    <td>181</td>
    <td>N/A</td>
    <td>0</td>
    <td>citg-grs;general</td>
    <td>avx;avx2;ht;ib;ssd</td>
  </tr>
  <tr>
    <td>grs3</td>
    <td>2 x Intel(R) Xeon(R) CPU E5-2667 v4 @ 3.20GHz</td>
    <td>8</td>
    <td>16</td>
    <td>3499.804</td>
    <td>251</td>
    <td>181</td>
    <td>N/A</td>
    <td>0</td>
    <td>citg-grs;general</td>
    <td>avx;avx2;ht;ib;ssd</td>
  </tr>
  <tr>
    <td>grs4</td>
    <td>2 x Intel(R) Xeon(R) CPU E5-2667 v4 @ 3.20GHz</td>
    <td>8</td>
    <td>16</td>
    <td>3500</td>
    <td>251</td>
    <td>181</td>
    <td>N/A</td>
    <td>0</td>
    <td>citg-grs;general</td>
    <td>avx;avx2;ht;ib;ssd</td>
  </tr>
  <tr>
    <td>influ1</td>
    <td>2 x Intel(R) Xeon(R) Gold 6130 CPU @ 2.10GHz</td>
    <td>16</td>
    <td>32</td>
    <td>3385.711</td>
    <td>376</td>
    <td>197</td>
    <td>NVIDIA GeForce RTX 2080 Ti</td>
    <td>8</td>
    <td>influence;ewi-insy;general</td>
    <td>avx;avx2;ht;10gbe;avx512;nvme;ssd</td>
  </tr>
  <tr>
    <td>influ2</td>
    <td>2 x Intel(R) Xeon(R) Gold 5218 CPU @ 2.30GHz</td>
    <td>16</td>
    <td>32</td>
    <td>2300.000</td>
    <td>187</td>
    <td>369</td>
    <td>NVIDIA GeForce RTX 2080 Ti</td>
    <td>4</td>
    <td>influence;ewi-insy;general</td>
    <td>avx;avx2;ht;10gbe;avx512;ssd</td>
  </tr>
  <tr>
    <td>influ3</td>
    <td>2 x Intel(R) Xeon(R) Gold 5218 CPU @ 2.30GHz</td>
    <td>16</td>
    <td>32</td>
    <td>2300.000</td>
    <td>187</td>
    <td>369</td>
    <td>NVIDIA GeForce RTX 2080 Ti</td>
    <td>4</td>
    <td>influence;ewi-insy;general</td>
    <td>avx;avx2;ht;10gbe;avx512;ssd</td>
  </tr>
  <tr>
    <td>influ4</td>
    <td>2 x AMD EPYC 7452 32-Core Processor</td>
    <td>32</td>
    <td>64</td>
    <td>2350.000</td>
    <td>252</td>
    <td>148</td>
    <td>N/A</td>
    <td>0</td>
    <td>influence;ewi-insy;general</td>
    <td>avx;avx2;ht;10gbe;ssd</td>
  </tr>
  <tr>
    <td>influ5</td>
    <td>2 x AMD EPYC 7452 32-Core Processor</td>
    <td>32</td>
    <td>64</td>
    <td>2350</td>
    <td>503</td>
    <td>148</td>
    <td>N/A</td>
    <td>0</td>
    <td>influence;ewi-insy;general</td>
    <td>avx;avx2;ht;10gbe;bigmem;ssd</td>
  </tr>
  <tr>
    <td>influ6</td>
    <td>2 x AMD EPYC 7452 32-Core Processor</td>
    <td>32</td>
    <td>64</td>
    <td>2350</td>
    <td>503</td>
    <td>148</td>
    <td>N/A</td>
    <td>0</td>
    <td>influence;ewi-insy;general</td>
    <td>avx;avx2;ht;10gbe;bigmem;ssd</td>
  </tr>
  <tr>
    <td>insy15</td>
    <td>2 x Intel(R) Xeon(R) Gold 5218 CPU @ 2.30GHz</td>
    <td>16</td>
    <td>32</td>
    <td>2300.000</td>
    <td>754</td>
    <td>416</td>
    <td>NVIDIA GeForce RTX 2080 Ti</td>
    <td>4</td>
    <td>ewi-insy;general</td>
    <td>avx;avx2;ht;10gbe;avx512;bigmem;ssd</td>
  </tr>
  <tr>
    <td>insy16</td>
    <td>2 x Intel(R) Xeon(R) Gold 5218 CPU @ 2.30GHz</td>
    <td>16</td>
    <td>32</td>
    <td>2300.000</td>
    <td>754</td>
    <td>416</td>
    <td>NVIDIA GeForce RTX 2080 Ti</td>
    <td>4</td>
    <td>ewi-insy;general</td>
    <td>avx;avx2;ht;10gbe;avx512;bigmem;ssd</td>
  </tr>
</tbody>
<tfoot>
  <tr>
    <td><strong>Total (66 nodes)</strong></td>
    <td></td> <!-- CPU (Sockets x Model) -->
    <td></td> <!-- Cores per Socket -->
    <td><strong>3016 cores</strong></td> <!-- Total Cores -->
    <td></td> <!-- CPU Speed (MHz) -->
    <td><strong>35.02 TiB</strong></td> <!-- Total RAM -->
    <td><strong>76.79 TiB</strong></td> <!-- Local Disk (/tmp) -->
    <td></td> <!-- GPU Type -->
    <td><strong>137 GPU</strong></td> <!-- GPU Count -->
    <td></td> <!-- SlurmPartitions -->
    <td></td> <!-- SlurmActiveFeatures -->
  </tr>
</tfoot>

</table>





<!-- ### CPUs
All nodes have multiple Central Processing Units (CPUs) that perform the operations. Each CPU can process one thread (i.e. a separate string of computer code) at a time. A computer program consists of one or multiple threads, and thus needs one or multiple CPUs simultaneously to do its computations (see {{< external-link "https://en.wikipedia.org/wiki/Central_processing_unit" "wikipedia's CPU page" >}} ).


{{% alert title="Note" color="info" %}}
Most programs use a fixed number of threads. Requesting more CPUs for a program than its number of threads will not make it any faster because it won't know how to use the extra CPUs. When a program has less CPUs available than its number of threads, the threads will have to time-share the available CPUs (i.e. each thread only gets part-time use of a CPU), and, as a result, the program will run slower (And even slower because of the added overhead of the switching of the threads). So it's always necessary to match the number of CPUs to the number of threads, or the other way around. See [submitting jobs](/docs/manual/job-submission/job-scripts) for setting resources for batch jobs.
{{% /alert %}}

The number of threads running simultaneously determines the load of a server. If the number of running threads is equal to the number of available CPUs, the server is loaded 100% (or 1.00). When the number of threads that want to run exceed the number of available CPUs, the load rises above 100%.

The CPU functionality is provided by the hardware cores in the processor chips in the machines. Traditionally, one physical core contained one logical CPU, thus the CPUs operated completely independent. Most current chips feature hyper-threading: one core contains two (or more) logical CPUs. These CPUs share parts of the core and the cache, so one CPU may have to wait when a shared resource is in use by the other CPU. Therefore these CPUs are always allocated in pairs by the job scheduler.  -->

