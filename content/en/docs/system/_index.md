---
title: "System specifications"
linkTitle: "System specifications"
weight: 20
description: >
  What are the foundational components of DAIC?
---

{{% pageinfo %}}
At present [DAIC](https://doc.daic.tudelft.nl/docs/) and [DelftBlue](https://doc.dhpc.tudelft.nl/delftblue) have different software stacks. This pertains to the operating system (CentOS 7 _vs_ Red Hat Enterprise Linux 8, respectively) and, consequently, the available software. Please refer to the respective [DelftBlue modules](https://doc.dhpc.tudelft.nl/delftblue/DHPC-modules/) and [Software](/docs/manual/software) section before commencing your experiments.
{{% /pageinfo %}}

<!---------------

```mermaid
---
title: DAIC Specifications
---
flowchart TD

    C[Slurm Resource Manager]
    D[Linux OS]
    subgraph Login["Login Nodes"]
      A1["login1"] 
      A2["login2 (Virtual Node)"] 
      A3["login3"] 
    end
    subgraph Compute["Compute Nodes (dummay names shown)"]
      B1[Node 1] 
      B2[Node 2]
      B3[Node 3]
      B4[...]
      B5[Node 60]
    end
    subgraph Storage
      E1["staff-bulk (not recommended)"]
      E2["staff-umbrella (recommended)"]
    end
    Login --Job Submission  -- C
    C -- Job Scheduling -- Compute
    C -- Data Management -- Storage
    D ---  C
```
----->

{{< figure src="/img/DAIC_partitions.png" caption="DAIC partitions and access/usage best practices" ref="fig:daic_partitions" width="750px">}}

## Operating System
DAIC runs the {{< external-link "https://en.wikipedia.org/wiki/Red_Hat_Enterprise_Linux" "Red Hat Enterprise Linux 7" >}}  Linux distribution, which provides the general Linux software. Most common software, including programming languages, libraries and development files for compiling your own software, is installed on the nodes (see [Available software](/docs/manual/software/available-software)). However, a not-so-common program that you need might not be installed. Similarly, if your research requires a state-of-the-art program that is not (yet) available as a package for {{< external-link "https://en.wikipedia.org/wiki/Red_Hat_Enterprise_Linux" "Red Hat" >}} 7, then it is not available. See [Installing software](/docs/manual/software/installing-software/) for more information. 

## Login Nodes

The login nodes are the gateway to the DAIC HPC cluster and are specifically designed for lightweight tasks such as job submission, file management, and compiling code (on certain nodes). These nodes are not intended for running resource-intensive jobs, which should be submitted to the [Compute Nodes](#compute-nodes).

### Specifications and usage notes

| Hostname  | CPU (Sockets x Model)                               | Total Cores | Total RAM  | Operating System      | GPU Type     | GPU Count | Usage Notes                                                   |
|-----------|-----------------------------------------------------|-------------|------------|-----------------------|--------------|-----------|---------------------------------------------------------------|
| `login1`  | 1 x Intel(R) Xeon(R) CPU E5-2620 v4 @ 2.10GHz       | 8           | 15.39 GB   | OpenShift Enterprise   | Quadro K2200 | 1         | For file transfers, job submission, and lightweight tasks.   |
| `login2`  | 1 x Intel(R) Xeon(R) CPU E5-2683 v3 @ 2.00GHz       | 1           | 3.70 GB    | OpenShift Enterprise   | N/A          | N/A       | Virtual server, for non-intensive tasks. **No compilation.** |
| `login3`  | 2 x Intel(R) Xeon(R) CPU E5-2683 v4 @ 2.10GHz       | 32          | 503.60 GB  | RHEV                  | Quadro K2200 | 1         | For large compilation and interactive sessions.              |






## Compute Nodes
DAIC compute nodes are all multi CPU servers, with large memories, and some with GPUs. The nodes in the cluster are heterogeneous, i.e. they have different types of hardware (processors, memory, GPUs), different functionality (some more advanced than others) and different performance characteristics. If a program requires specific features, you need to specifically request those for that job (see [Submitting jobs](/docs/manual/job-submission/job-scripts)). 

{{% alert title="Note" color="info" %}}
All compute nodes have [Advanced Vector Extensions](https://en.wikipedia.org/wiki/Advanced_Vector_Extensions) 1 and 2 (AVX, AVX2) support, and hyper-threading (`ht`) processors (two CPUs per core, always allocated in pairs).
{{% /alert %}}    

{{% alert title="Note" color="info" %}}
You can use Slurm's `sinfo` command to get various information about cluster nodes. For example, to get an overview of compute nodes on DAIC, you can use the command:

```bash
$ sinfo --all --format="%P %N %c %m %G %b" --hide -S P,N -a | grep -v "general" | awk 'NR==1 {print; next} {match($5, /gpu:[^,]+:[0-9]+/); if (RSTART) print $1, $2, $3, $4, substr($5, RSTART, RLENGTH), $6; else print $1, $2, $3, $4, "-", $6  }'  
```
Check out the [Slurm's sinfo page](https://slurm.schedmd.com/sinfo.html) and  [wikipedia's awk page](https://en.wikipedia.org/wiki/AWK) for more info on these commands.

{{% /alert %}}

### List of all nodes
The following table gives an overview of current nodes and their characteristics:

<table>
<thead>
  <tr>
    <th>Hostname</th>
    <th>CPU (Sockets x Model)</th>
    <th>Cores per Socket</th>
    <th>Total Cores</th>
    <th>CPU Speed (MHz)</th>
    <th>Total RAM</th>
    <th>GPU Type</th>
    <th>GPU Count</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>100plus</td>
    <td>2 x Intel(R) Xeon(R) CPU E5-2683 v4 @ 2.10GHz</td>
    <td>16</td>
    <td>32</td>
    <td>2097.488</td>
    <td>755.585 GB</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>3dgi1</td>
    <td>1 x AMD EPYC 7502P 32-Core Processor</td>
    <td>32</td>
    <td>32</td>
    <td>2500</td>
    <td>251.41 GB</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>3dgi2</td>
    <td>1 x AMD EPYC 7502P 32-Core Processor</td>
    <td>32</td>
    <td>32</td>
    <td>2500</td>
    <td>251.41 GB</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>awi01</td>
    <td>2 x Intel(R) Xeon(R) Gold 6140 CPU @ 2.30GHz</td>
    <td>18</td>
    <td>36</td>
    <td>2996.569</td>
    <td>376.384 GB</td>
    <td>Tesla V100 PCIe 32GB</td>
    <td>1</td>
  </tr>
  <tr>
    <td>awi02</td>
    <td>2 x Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.40GHz</td>
    <td>14</td>
    <td>28</td>
    <td>2900.683</td>
    <td>503.619 GB</td>
    <td>Tesla V100 SXM2 16GB</td>
    <td>2</td>
  </tr>
  <tr>
    <td>awi03</td>
    <td>2 x Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.40GHz</td>
    <td>14</td>
    <td>28</td>
    <td>2899.951</td>
    <td>503.625 GB</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>awi04</td>
    <td>2 x Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.40GHz</td>
    <td>14</td>
    <td>28</td>
    <td>3231.884</td>
    <td>503.625 GB</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>awi05</td>
    <td>2 x Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.40GHz</td>
    <td>14</td>
    <td>28</td>
    <td>3258.984</td>
    <td>503.625 GB</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>awi07</td>
    <td>2 x Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.40GHz</td>
    <td>14</td>
    <td>28</td>
    <td>2899.951</td>
    <td>503.625 GB</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>awi08</td>
    <td>2 x Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.40GHz</td>
    <td>14</td>
    <td>28</td>
    <td>2899.951</td>
    <td>503.625 GB</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>awi09</td>
    <td>2 x Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.40GHz</td>
    <td>14</td>
    <td>28</td>
    <td>2899.951</td>
    <td>503.625 GB</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>awi10</td>
    <td>2 x Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.40GHz</td>
    <td>14</td>
    <td>28</td>
    <td>2899.951</td>
    <td>503.625 GB</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>awi11</td>
    <td>2 x Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.40GHz</td>
    <td>14</td>
    <td>28</td>
    <td>2899.951</td>
    <td>503.625 GB</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>awi12</td>
    <td>2 x Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.40GHz</td>
    <td>14</td>
    <td>28</td>
    <td>2899.951</td>
    <td>503.625 GB</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>awi19</td>
    <td>2 x Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.40GHz</td>
    <td>14</td>
    <td>28</td>
    <td>2899.951</td>
    <td>251.641 GB</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>awi20</td>
    <td>2 x Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.40GHz</td>
    <td>14</td>
    <td>28</td>
    <td>2899.951</td>
    <td>251.641 GB</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>awi21</td>
    <td>2 x Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.40GHz</td>
    <td>14</td>
    <td>28</td>
    <td>2899.951</td>
    <td>251.641 GB</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>awi22</td>
    <td>2 x Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.40GHz</td>
    <td>14</td>
    <td>28</td>
    <td>2899.951</td>
    <td>251.641 GB</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>awi23</td>
    <td>2 x Intel(R) Xeon(R) Gold 6140 CPU @ 2.30GHz</td>
    <td>18</td>
    <td>36</td>
    <td>3221.038</td>
    <td>376.385 GB</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>awi24</td>
    <td>2 x Intel(R) Xeon(R) Gold 6140 CPU @ 2.30GHz</td>
    <td>18</td>
    <td>36</td>
    <td>2580.2</td>
    <td>376.385 GB</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>awi25</td>
    <td>2 x Intel(R) Xeon(R) Gold 6140 CPU @ 2.30GHz</td>
    <td>18</td>
    <td>36</td>
    <td>3399.884</td>
    <td>376.385 GB</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>awi26</td>
    <td>2 x Intel(R) Xeon(R) Gold 6140 CPU @ 2.30GHz</td>
    <td>18</td>
    <td>36</td>
    <td>3442.7</td>
    <td>376.385 GB</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>cor1</td>
    <td>2 x Intel(R) Xeon(R) Gold 6242 CPU @ 2.80GHz</td>
    <td>16</td>
    <td>64</td>
    <td>3599.975</td>
    <td>1510.33 GB</td>
    <td>Tesla V100 SXM2 32GB</td>
    <td>8</td>
  </tr>
  <tr>
    <td>gpu01</td>
    <td>2 x AMD EPYC 7413 24-Core Processor</td>
    <td>24</td>
    <td>48</td>
    <td>2650</td>
    <td>503.402 GB</td>
    <td>NVIDIA A40</td>
    <td>3</td>
  </tr>
  <tr>
    <td>gpu02</td>
    <td>2 x AMD EPYC 7413 24-Core Processor</td>
    <td>24</td>
    <td>48</td>
    <td>2650</td>
    <td>503.402 GB</td>
    <td>NVIDIA A40</td>
    <td>3</td>
  </tr>
  <tr>
    <td>gpu03</td>
    <td>2 x AMD EPYC 7413 24-Core Processor</td>
    <td>24</td>
    <td>48</td>
    <td>2650</td>
    <td>503.402 GB</td>
    <td>NVIDIA A40</td>
    <td>3</td>
  </tr>
  <tr>
    <td>gpu04</td>
    <td>2 x AMD EPYC 7413 24-Core Processor</td>
    <td>24</td>
    <td>48</td>
    <td>2650</td>
    <td>503.402 GB</td>
    <td>NVIDIA A40</td>
    <td>3</td>
  </tr>
  <tr>
    <td>gpu05</td>
    <td>2 x AMD EPYC 7413 24-Core Processor</td>
    <td>24</td>
    <td>48</td>
    <td>2650</td>
    <td>503.402 GB</td>
    <td>NVIDIA A40</td>
    <td>3</td>
  </tr>
  <tr>
    <td>gpu06</td>
    <td>2 x AMD EPYC 7413 24-Core Processor</td>
    <td>24</td>
    <td>48</td>
    <td>2650</td>
    <td>503.402 GB</td>
    <td>NVIDIA A40</td>
    <td>3</td>
  </tr>
  <tr>
    <td>gpu07</td>
    <td>2 x AMD EPYC 7413 24-Core Processor</td>
    <td>24</td>
    <td>48</td>
    <td>2650</td>
    <td>503.402 GB</td>
    <td>NVIDIA A40</td>
    <td>3</td>
  </tr>
  <tr>
    <td>gpu08</td>
    <td>2 x AMD EPYC 7413 24-Core Processor</td>
    <td>24</td>
    <td>48</td>
    <td>2650</td>
    <td>503.402 GB</td>
    <td>NVIDIA A40</td>
    <td>3</td>
  </tr>
  <tr>
    <td>gpu09</td>
    <td>2 x AMD EPYC 7413 24-Core Processor</td>
    <td>24</td>
    <td>48</td>
    <td>2650</td>
    <td>503.402 GB</td>
    <td>NVIDIA A40</td>
    <td>3</td>
  </tr>
  <tr>
    <td>gpu10</td>
    <td>2 x AMD EPYC 7413 24-Core Processor</td>
    <td>24</td>
    <td>48</td>
    <td>2650</td>
    <td>503.402 GB</td>
    <td>NVIDIA A40</td>
    <td>3</td>
  </tr>
  <tr>
    <td>gpu11</td>
    <td>2 x AMD EPYC 7413 24-Core Processor</td>
    <td>24</td>
    <td>48</td>
    <td>2650</td>
    <td>503.402 GB</td>
    <td>NVIDIA A40</td>
    <td>3</td>
  </tr>
  <tr>
    <td>gpu14</td>
    <td>2 x AMD EPYC 7543 32-Core Processor</td>
    <td>32</td>
    <td>64</td>
    <td>2794.613</td>
    <td>503.275 GB</td>
    <td>NVIDIA A40</td>
    <td>3</td>
  </tr>
  <tr>
    <td>gpu15</td>
    <td>2 x AMD EPYC 7543 32-Core Processor</td>
    <td>32</td>
    <td>64</td>
    <td>2794.938</td>
    <td>503.275 GB</td>
    <td>NVIDIA A40</td>
    <td>3</td>
  </tr>
  <tr>
    <td>gpu16</td>
    <td>2 x AMD EPYC 7543 32-Core Processor</td>
    <td>32</td>
    <td>64</td>
    <td>2794.604</td>
    <td>503.275 GB</td>
    <td>NVIDIA A40</td>
    <td>3</td>
  </tr>
  <tr>
    <td>gpu17</td>
    <td>2 x AMD EPYC 7543 32-Core Processor</td>
    <td>32</td>
    <td>64</td>
    <td>2794.878</td>
    <td>503.275 GB</td>
    <td>NVIDIA A40</td>
    <td>3</td>
  </tr>
  <tr>
    <td>gpu18</td>
    <td>2 x AMD EPYC 7543 32-Core Processor</td>
    <td>32</td>
    <td>64</td>
    <td>2794.57</td>
    <td>503.275 GB</td>
    <td>NVIDIA A40</td>
    <td>3</td>
  </tr>
  <tr>
    <td>gpu19</td>
    <td>2 x AMD EPYC 7543 32-Core Processor</td>
    <td>32</td>
    <td>64</td>
    <td>2794.682</td>
    <td>503.275 GB</td>
    <td>NVIDIA A40</td>
    <td>3</td>
  </tr>
  <tr>
    <td>gpu20</td>
    <td>2 x AMD EPYC 7543 32-Core Processor</td>
    <td>32</td>
    <td>64</td>
    <td>2794.651</td>
    <td>1007.24 GB</td>
    <td>NVIDIA A40</td>
    <td>3</td>
  </tr>
  <tr>
    <td>gpu21</td>
    <td>2 x AMD EPYC 7543 32-Core Processor</td>
    <td>32</td>
    <td>64</td>
    <td>2794.646</td>
    <td>1007.24 GB</td>
    <td>NVIDIA A40</td>
    <td>3</td>
  </tr>
  <tr>
    <td>gpu22</td>
    <td>2 x AMD EPYC 7543 32-Core Processor</td>
    <td>32</td>
    <td>64</td>
    <td>2794.963</td>
    <td>1007.24 GB</td>
    <td>NVIDIA A40</td>
    <td>3</td>
  </tr>
  <tr>
    <td>gpu23</td>
    <td>2 x AMD EPYC 7543 32-Core Processor</td>
    <td>32</td>
    <td>64</td>
    <td>2794.658</td>
    <td>1007.24 GB</td>
    <td>NVIDIA A40</td>
    <td>3</td>
  </tr>
  <tr>
    <td>gpu24</td>
    <td>2 x AMD EPYC 7543 32-Core Processor</td>
    <td>32</td>
    <td>64</td>
    <td>2794.664</td>
    <td>1007.24 GB</td>
    <td>NVIDIA A40</td>
    <td>3</td>
  </tr>
  <tr>
    <td>grs1</td>
    <td>2 x Intel(R) Xeon(R) CPU E5-2667 v4 @ 3.20GHz</td>
    <td>8</td>
    <td>16</td>
    <td>3499.804</td>
    <td>251.633 GB</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>grs2</td>
    <td>2 x Intel(R) Xeon(R) CPU E5-2667 v4 @ 3.20GHz</td>
    <td>8</td>
    <td>16</td>
    <td>3577.734</td>
    <td>251.633 GB</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>grs3</td>
    <td>2 x Intel(R) Xeon(R) CPU E5-2667 v4 @ 3.20GHz</td>
    <td>8</td>
    <td>16</td>
    <td>3499.804</td>
    <td>251.633 GB</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>grs4</td>
    <td>2 x Intel(R) Xeon(R) CPU E5-2667 v4 @ 3.20GHz</td>
    <td>8</td>
    <td>16</td>
    <td>3499.804</td>
    <td>251.633 GB</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>influ1</td>
    <td>2 x Intel(R) Xeon(R) Gold 6130 CPU @ 2.10GHz</td>
    <td>16</td>
    <td>32</td>
    <td>2955.816</td>
    <td>376.391 GB</td>
    <td>GeForce RTX 2080 Ti</td>
    <td>8</td>
  </tr>
  <tr>
    <td>influ2</td>
    <td>2 x Intel(R) Xeon(R) Gold 5218 CPU @ 2.30GHz</td>
    <td>16</td>
    <td>32</td>
    <td>2300</td>
    <td>187.232 GB</td>
    <td>GeForce RTX 2080 Ti</td>
    <td>4</td>
  </tr>
  <tr>
    <td>influ3</td>
    <td>2 x Intel(R) Xeon(R) Gold 5218 CPU @ 2.30GHz</td>
    <td>16</td>
    <td>32</td>
    <td>2300</td>
    <td>187.232 GB</td>
    <td>GeForce RTX 2080 Ti</td>
    <td>4</td>
  </tr>
  <tr>
    <td>influ4</td>
    <td>2 x AMD EPYC 7452 32-Core Processor</td>
    <td>32</td>
    <td>64</td>
    <td>1500</td>
    <td>251.626 GB</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>influ5</td>
    <td>2 x AMD EPYC 7452 32-Core Processor</td>
    <td>32</td>
    <td>64</td>
    <td>2350</td>
    <td>503.611 GB</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>influ6</td>
    <td>2 x AMD EPYC 7452 32-Core Processor</td>
    <td>32</td>
    <td>64</td>
    <td>1500</td>
    <td>503.61 GB</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>insy15</td>
    <td>2 x Intel(R) Xeon(R) Gold 5218 CPU @ 2.30GHz</td>
    <td>16</td>
    <td>32</td>
    <td>2300</td>
    <td>754.33 GB</td>
    <td>GeForce RTX 2080 Ti Rev. A</td>
    <td>4</td>
  </tr>
  <tr>
    <td>insy16</td>
    <td>2 x Intel(R) Xeon(R) Gold 5218 CPU @ 2.30GHz</td>
    <td>16</td>
    <td>32</td>
    <td>2300</td>
    <td>754.33 GB</td>
    <td>GeForce RTX 2080 Ti Rev. A</td>
    <td>4</td>
  </tr>
  <tr>
    <td><strong> Total</strong> </td>
    <td></td>
    <td><strong> 1206</strong> </td>
    <td><strong> 2380</strong> </td>
    <td></td>
    <td><strong> 28 TB</strong> </td>
    <td></td>
    <td><strong> 101</strong> </td>
  </tr>
  <tr>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</tbody>
</table>

<!--

<table>
<caption> Table 1: Overview of DAIC compute nodes </caption>
<tfoot><tr><td colspan="6"> 
<font color="gray">
<ul>
 <li> All nodes are also parts of the <code>general</code> partition. </li>
 <li> Abbreviations: 
   <code>10gbe</code>: 10 Gigabit Ethernet network connection (upgrade from the default 1 Gigabit Ethernet connection), 
   <code>ib</code> InfiniBand connection, 
   <code>ssd</code>Solid-State Disk for <code>/tmp</code> storage (instead of the default spinning disk), 
   <code>bigmem</code>: For jobs that needs a lot of memory, so remaining resources are available to others, 
   <code>imphysexclusive</code>: imphys nodes use infiband for jobs that run across a large number of nodes, and it is handy that those nodes are somewhat reserved, 
   <code>avx512</code>: extra instructions on cpu, like avx1 and avx2 only on the newer CPUs, if you have code that need them, 
   <code>gpumem32</code>: gpu memory for newer GPUs: do not use gpu types, but use this feature instead if you have a need for gpu with more memory, 
   <code>nvme</code>: Non-Volatile Memory Express for tmp storage
 </li>
</ul>:q
</font>
</td></tr></tfoot>
<thead>
  <tr>
    <th>PARTITION</th>
    <th>NODELIST</th>
    <th>CPUS</th>
    <th>MEMORY (MB)</th>
    <th>GRES</th>
    <th>ACTIVE_FEATURES</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>100plus</td>
    <td>100plus</td>
    <td>64</td>
    <td>768000</td>
    <td>-</td>
    <td>avx,avx2,ht,10gbe,bigmem</td>
  </tr>
  <tr>
    <td rowspan="2">3dgi</td>
    <td>3dgi[1-2]</td>
    <td>64</td>
    <td>256000</td>
    <td>-</td>
    <td>avx,avx2,ht,10gbe,ssd</td>
  </tr>
  <tr>
    <td>gpu11</td>
    <td>96</td>
    <td>512000</td>
    <td>gpu:a40:3</td>
    <td>avx,avx2,ht,10gbe,bigmem,gpumem32,ssd</td>
  </tr>
  <tr>
    <td>cor</td>
    <td>cor1</td>
    <td>64</td>
    <td>1536000</td>
    <td>gpu:v100:8</td>
    <td>avx,avx2,ht,10gbe,avx512,gpumem32,ssd</td>
  </tr>
  <tr>
    <td>grs</td>
    <td>grs[1-4]</td>
    <td>32</td>
    <td>256000</td>
    <td>-</td>
    <td>avx,avx2,ht,ib,ssd</td>
  </tr>
  <tr>
    <td rowspan="5">imphys</td>
    <td>awi01</td>
    <td>72</td>
    <td>384000</td>
    <td>gpu:v100:1</td>
    <td>avx,avx2,ht,10gbe,avx512,gpumem32,nvme,ssd</td>
  </tr>
  <tr>
    <td>awi02</td>
    <td>56</td>
    <td>512000</td>
    <td>gpu:v100:2</td>
    <td>avx,avx2,ht,10gbe,bigmem,ssd</td>
  </tr>
  <tr>
    <td>awi[03-14]</td>
    <td>56</td>
    <td>512000</td>
    <td>-</td>
    <td>avx,avx2,ht,ib,imphysexclusive</td>
  </tr>
  <tr>
    <td>awi[15-26]</td>
    <td>56+</td>
    <td>256000+</td>
    <td>-</td>
    <td>avx,avx2,ht,ib,ssd</td>
  </tr>
  <tr>
    <td>gpu[09-10]</td>
    <td>96</td>
    <td>512000</td>
    <td>gpu:a40:3</td>
    <td>avx,avx2,ht,10gbe,bigmem,gpumem32,ssd</td>
  </tr>
  <tr>
    <td rowspan="4">influence</td>
    <td>influ1</td>
    <td>64</td>
    <td>384000</td>
    <td>gpu:turing:8</td>
    <td>avx,avx2,ht,10gbe,avx512,nvme,ssd</td>
  </tr>
  <tr>
    <td>influ[2-3]</td>
    <td>64</td>
    <td>190000</td>
    <td>gpu:turing:4</td>
    <td>avx,avx2,ht,10gbe,avx512,ssd</td>
  </tr>
  <tr>
    <td>influ4</td>
    <td>128</td>
    <td>256000</td>
    <td>-</td>
    <td>avx,avx2,ht,10gbe,ssd</td>
  </tr>
  <tr>
    <td>influ[5-6]</td>
    <td>128</td>
    <td>512000</td>
    <td>-</td>
    <td>avx,avx2,ht,10gbe,bigmem,ssd</td>
  </tr>
  <tr>
    <td rowspan="10">insy</td>
    <td>100plus</td>
    <td>64</td>
    <td>768000</td>
    <td>-</td>
    <td>avx,avx2,ht,10gbe,bigmem</td>
  </tr>
  <tr>
    <td>gpu[01-04]</td>
    <td>96</td>
    <td>512000</td>
    <td>gpu:a40:3</td>
    <td>avx,avx2,ht,10gbe,bigmem,gpumem32,ssd</td>
  </tr>
  <tr>
    <td>influ1</td>
    <td>64</td>
    <td>384000</td>
    <td>gpu:turing:8</td>
    <td>avx,avx2,ht,10gbe,avx512,nvme,ssd</td>
  </tr>
  <tr>
    <td>influ[2-3]</td>
    <td>64</td>
    <td>190000</td>
    <td>gpu:turing:4</td>
    <td>avx,avx2,ht,10gbe,avx512,ssd</td>
  </tr>
  <tr>
    <td>influ4</td>
    <td>128</td>
    <td>256000</td>
    <td>-</td>
    <td>avx,avx2,ht,10gbe,ssd</td>
  </tr>
  <tr>
    <td>influ[5-6]</td>
    <td>128</td>
    <td>512000</td>
    <td>-</td>
    <td>avx,avx2,ht,10gbe,bigmem,ssd</td>
  </tr>
  <tr>
    <td>insy11</td>
    <td>64</td>
    <td>256000</td>
    <td>gpu:pascal:5</td>
    <td>avx,avx2,ht,10gbe</td>
  </tr>
  <tr>
    <td>insy12</td>
    <td>64</td>
    <td>256000</td>
    <td>gpu:pascal:7</td>
    <td>avx,avx2,ht,10gbe</td>
  </tr>
  <tr>
    <td>insy[13-14]</td>
    <td>64</td>
    <td>256000</td>
    <td>gpu:pascal:8</td>
    <td>avx,avx2,ht,10gbe</td>
  </tr>
  <tr>
    <td>insy[15-16]</td>
    <td>64</td>
    <td>768000</td>
    <td>gpu:turing:4</td>
    <td>avx,avx2,ht,10gbe,avx512,bigmem,ssd</td>
  </tr>
  <tr>
    <td rowspan="2">st</td>
    <td>gpu[05-08]</td>
    <td>96</td>
    <td>512000</td>
    <td>gpu:a40:3</td>
    <td>avx,avx2,ht,10gbe,bigmem,gpumem32,ssd</td>
  </tr>
  <tr>
    <td>wis1</td>
    <td>64</td>
    <td>768000</td>
    <td>gpu:p100:2</td>
    <td>avx,avx2,ht,10gbe,avx512,bigmem</td>
  </tr>
  <tr>
    <td>tbm</td>
    <td>tbm5</td>
    <td>64</td>
    <td>768000</td>
    <td>-</td>
    <td>avx,avx2,ht,10gbe,avx512,bigmem,ssd</td>
  </tr>
  <tr>
    <td rowspan="3">visionlab</td>
    <td>insy11</td>
    <td>64</td>
    <td>256000</td>
    <td>gpu:pascal:5</td>
    <td>avx,avx2,ht,10gbe</td>
  </tr>
  <tr>
    <td>insy12</td>
    <td>64</td>
    <td>256000</td>
    <td>gpu:pascal:7</td>
    <td>avx,avx2,ht,10gbe</td>
  </tr>
  <tr>
    <td>insy[13-14]</td>
    <td>64</td>
    <td>256000</td>
    <td>gpu:pascal:8</td>
    <td>avx,avx2,ht,10gbe</td>
  </tr>
  <tr>
    <td>wis</td>
    <td>wis1</td>
    <td>64</td>
    <td>768000</td>
    <td>gpu:p100:2</td>
    <td>avx,avx2,ht,10gbe,avx512,bigmem</td>
  </tr>
</tbody>
<tr>
  <td><strong>Total</strong></td>
  
  <td><strong> 59 compute nodes </strong></td>
  <td><strong>4064 cores</strong></td>
  <td><strong>25620 GB</strong></td>
  <td><strong>99 GPUs</strong></td>
</tr>
</table>

<!--->


### CPUs
All nodes have multiple Central Processing Units (CPUs) that perform the operations. Each CPU can process one thread (i.e. a separate string of computer code) at a time. A computer program consists of one or multiple threads, and thus needs one or multiple CPUs simultaneously to do its computations (see {{< external-link "https://en.wikipedia.org/wiki/Central_processing_unit" "wikipedia's CPU page" >}} ).


{{% alert title="Note" color="info" %}}
Most programs use a fixed number of threads. Requesting more CPUs for a program than its number of threads will not make it any faster because it won't know how to use the extra CPUs. When a program has less CPUs available than its number of threads, the threads will have to time-share the available CPUs (i.e. each thread only gets part-time use of a CPU), and, as a result, the program will run slower (And even slower because of the added overhead of the switching of the threads). So it's always necessary to match the number of CPUs to the number of threads, or the other way around. See [submitting jobs](/docs/manual/job-submission/job-scripts) for setting resources for batch jobs.
{{% /alert %}}

The number of threads running simultaneously determines the load of a server. If the number of running threads is equal to the number of available CPUs, the server is loaded 100% (or 1.00). When the number of threads that want to run exceed the number of available CPUs, the load rises above 100%.

The CPU functionality is provided by the hardware cores in the processor chips in the machines. Traditionally, one physical core contained one logical CPU, thus the CPUs operated completely independent. Most current chips feature hyper-threading: one core contains two (or more) logical CPUs. These CPUs share parts of the core and the cache, so one CPU may have to wait when a shared resource is in use by the other CPU. Therefore these CPUs are always allocated in pairs by the job scheduler. 



### GPUs
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
To inspect a given GPU and obtain the data of table 2, you can run the following commands on an interactive session or an sbatch script (see [Jobs on GPU resources](/docs/manual/job-submission/job-gpu)). The apptainer image used in this code snippet was built as demonstrated in the [Apptainer tutorial](/tutorials/apptainer/).

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


### Memory
All machines have large main memories for performing computations on big data sets. A job cannot use more than it's allocated amount of memory. If it needs to use more memory, it will fail or be killed. It's not possible to combine the memory from multiple nodes for a single task. 32-bit programs can only address (use) up to 3Gb (gigabytes) of memory. See [Submitting jobs](/docs/manual/job-submission/job-scripts) for setting resources for batch jobs.

## Storage
{{% pageinfo %}}
DAIC compute nodes have direct access to the TU Delft [home](#personal-storage-aka-home-folder), [group](#group-storage) and [project](#project-storage) storage. You can use your TU Delft installed machine or an SCP or SFTP client to transfer files to and from these storage areas and others (see [data transfer](/docs/manual/data-management/data-transfer/)) , as is demonstrated throughout this page.
{{% /pageinfo %}}

### File System Overview
Unlike TU Delft's {{< external-link "https://doc.dhpc.tudelft.nl/delftblue/DHPC-hardware/#description-of-the-delftblue-system" "DelftBlue" >}}, DAIC does not have a dedicated storage filesystem. This means no `/scratch` space for storing temporary files (see DelftBlue's {{< external-link "https://doc.dhpc.tudelft.nl/delftblue/DHPC-hardware/#description-of-the-delftblue-system" "Storage description" >}} and {{< external-link "https://doc.dhpc.tudelft.nl/delftblue/DHPC-Policies/#disk-quota-and-scratch-space" "Disk quota and scratch space" >}}). Instead, DAIC relies on direct connection to the TU Delft network storage filesystem (see {{< external-link "https://tudelft.topdesk.net/tas/public/ssp/content/detail/service?unid=f359caaa60264f99b0084941736786ae" "Overview data storage">}}) from all its nodes, and offers the following types of storage areas:

### Personal storage (aka home folder)
The Personal Storage is private and is meant to store personal files (program settings, bookmarks).  A backup service protects your home files from both hardware failures and user error (you can restore previous versions of files from up to two weeks ago). The available space is limited by a quota limit (since this space is not meant to be used for research data). 

You have two (separate) home folders: one for Linux and one for Windows (because Linux and Windows store program settings differently). You can access these home folders from a machine (running Linux or Windows OS) using a command line interface or a browser via {{< external-link "https://webdata.tudelft.nl/" "TU Delft's webdata" >}}. For example, Windows home has a `My Documents` folder. `My documents` can be found on a Linux machine under `/winhome/<YourNetID>/My Documents` 

<table>
<thead>
  <tr>
    <th>Home directory</th>
    <th>Access from</th>
    <th>Storage location</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td colspan="3">Linux&nbsp;&nbsp;home folder</td>
  </tr>
  <tr>
    <td></td>
    <td>Linux </td>
    <td> <code> /home/nfs/&lt;YourNetID&gt; </code> </td>
  </tr>
  <tr>
    <td></td>
    <td>Windows </td>
    <td>only accessible using an scp/sftp client (see <a href="https://doc.daic.tudelft.nl/docs/manual/connecting#ssh-access">SSH access</a>)</td>
  </tr>
  <tr>
    <td></td>
    <td>webdata</td>
    <td>not available </td>
  </tr>
  <tr>
    <td colspan="3">Windows home folder</td>
  </tr>
  <tr>
    <td></td>
    <td>Linux </td>
    <td><code>/winhome/&lt;YourNetID&gt;</code></td>
  </tr>
  <tr>
    <td></td>
    <td>Windows </td>
    <td> <code> H: </code> or <code> \\tudelft.net\staff-homes\[a-z]\&lt;YourNetID&gt; </code> </td>
  </tr>
  <tr>
    <td></td>
    <td>webdata</td>
    <td> <code> https://webdata.tudelft.nl/staff-homes/[a-z]/&lt;YourNetID&gt; </code> </td>
  </tr>
</tbody>
</table>

It's possible to access the backups yourself. In Linux the backups are located under the (hidden, read-only) `~/.snapshot/` folder. In Windows you can right-click the `H:` drive and choose `Restore previous versions`. 

{{% alert title="Note" color="info" %}}
 To see your disk usage, run something like: 
 ```bash
 du -h '</path/to/folder>' | sort -h | tail
 ```
{{% /alert %}}

### Group storage
The Group Storage is meant to share files (documents, educational and research data) with department/group members. The whole department or group has access to this storage, so this is not for confidential or project data. There is a backup service to protect the files, with previous versions up to two weeks ago. There is a Fair-Use policy for the used space. 

<table>
<thead>
  <tr>
    <th>Destination</th>
    <th>Access from</th>
    <th>Storage location</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td colspan="3">Group Storage</td>
  </tr>
  <tr>
    <td rowspan="2"></td>
    <td rowspan="2">Linux </td>
    <td> <code> /tudelft.net/staff-groups/&lt;faculty&gt;/&lt;department&gt;/&lt;group&gt; </code> or</td>
  </tr>
  <tr>
    <td> <code> /tudelft.net/staff-bulk/&lt;faculty&gt;/&lt;department&gt;/&lt;group&gt;/&lt;NetID&gt; </code> </td>
  </tr>
  <tr>
    <td rowspan="2"></td>
    <td rowspan="2">Windows </td>
    <td> <code> M: </code> or <code> \\tudelft.net\staff-groups\&lt;faculty&gt;\&lt;department&gt;\&lt;group&gt; </code> or</td>
  </tr>
  <tr>
    <td> <code> L: </code> or <code> \\tudelft.net\staff-bulk\ewi\insy\&lt;group&gt;\&lt;NetID&gt; </code> </td>
  </tr>
  <tr>
    <td></td>
    <td>webdata</td>
    <td> <code> https://webdata.tudelft.nl/staff-groups/</a>&lt;faculty&gt;/&lt;department&gt;/&lt;group&gt;/ </code> </td>
  </tr>
</tbody>
</table>

### Project Storage 
The Project Storage is meant for storing (research) data (datasets, generated results, download files and programs, ...) for projects. Only the project members (including external persons) can access the data, so this is suitable for confidential data (but you may want to use encryption for highly sensitive confidential data). There is a backup service and a Fair-Use policy for the used space.

Project leaders (or supervisors) can request a Project Storage location via the {{< external-link "https://tudelft.topdesk.net/tas/public/ssp/content/detail/service?unid=846ebb16181c43b5836c063a917dd199&from=03aa10b9-c5aa-4e0a-80b1-28ee7ab383df" "Self-Service Portal or the Service Desk" >}}.

<table>
<thead>
  <tr>
    <th>Destination</th>
    <th>Access from</th>
    <th>Storage location</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td colspan="3">Project Storage</td>
  </tr>
  <tr>
    <td></td>
    <td>Linux </td>
    <td> <code> /tudelft.net/staff-umbrella/&lt;project&gt; </code> </td>
  </tr>
  <tr>
    <td></td>
    <td>Windows </td>
    <td> <code> U: </code> or <code> \\tudelft.net\staff-umbrella\&lt;project&gt; </code> </td>
  </tr>
  <tr>
    <td></td>
    <td>webdata </td>
    <td> <code> https://webdata.tudelft.nl/staff-umbrella/&lt;project&gt; </code> or <code> <br>https://webdata.tudelft.nl/staff-bulk/&lt;faculty&gt;/&lt;department&gt;/&lt;group&gt;/&lt;NetID&gt; </code> </td>
  </tr>
</tbody>
</table>

### Local Storage 
Local storage is meant for temporary storage of (large amounts of) data with fast access on a single computer. You can create your own personal folder inside the local storage. Unlike the network storage above, local storage is only accessible on that computer, not on other computers or through network file servers or webdata. There is no backup service nor quota. The available space is large but fixed, so leave enough space for other users. Files under `/tmp` that have not been accessed for 10 days are automatically removed. 

<table>
<thead>
  <tr>
    <th>Destination</th>
    <th>Access from</th>
    <th>Storage location</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td colspan="3">Local storage</td>
  </tr>
  <tr>
    <td></td>
    <td>Linux </td>
    <td><code> /tmp/&lt;NetID&gt; </code> </td>
  </tr>
  <tr>
    <td></td>
    <td>Windows </td>
    <td>not available </td>
  </tr>
  <tr>
    <td></td>
    <td>webdata </td>
    <td>not available </td>
  </tr>
</tbody>
</table>

### Memory Storage
Memory storage is meant for short-term storage of limited amounts of data with very fast access on a single computer. You can create your own personal folder inside the memory storage location. Memory storage is only accessible on that computer, and there is no backup service nor quota. The available space is limited and shared with programs, so leave enough space (the computer will likely crash when you don't!). Files that have not been accessed for 1 day are automatically removed. 

<table>
<thead>
  <tr>
    <th>Destination</th>
    <th>Access from</th>
    <th>Storage location</th>
  </tr>
</thead>
<tbody> 
  <tr>
    <td colspan="3">Memory storage</td>
  </tr>
  <tr>
    <td></td>
    <td>Linux </td>
    <td> <code> /dev/shm/&lt;NetID&gt; </code> </td>
  </tr>
  <tr>
    <td></td>
    <td>Windows </td>
    <td>not available </td>
  </tr>
  <tr>
    <td></td>
    <td> webdata </td>
    <td>not available </td>
  </tr>
</tbody>
</table>

{{% alert title="Warning" color="info" %}}
Use this only when using other storage makes your job or the whole computer slow. 
{{% /alert %}}

## Workload scheduler
DAIC uses the {{< external-link "https://slurm.schedmd.com/" "Slurm scheduler" >}} to efficiently manage workloads. All jobs for the cluster have to be submitted as batch jobs into a queue. The scheduler then manages and prioritizes the jobs in the queue, allocates resources (CPUs, memory) for the jobs, executes the jobs and enforces the resource allocations. See [the job submission pages](/docs/manual/job-submission) for more information.

A slurm-based cluster is composed of a set of _login nodes_ that are used to access the cluster and submit computational jobs. A _central manager_ orchestrates computational demands across a set of _compute nodes_. These nodes are organized logically into groups called _partitions_, that defines job limits or access rights. The central manager provides fault-tolerant hierarchical communications, to ensure optimal and fair use  of available compute resources to eligible users, and make it easier to run and schedule complex jobs across compute resources (multiple nodes).


