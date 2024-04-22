---
title: "Nodes"
linkTitle: "Nodes"
weight: 10
description: >
  An overview over all compute nodes available.
---


## Nodes

DAIC compute nodes are all multi CPU servers, with large memories, and some with GPUs. The nodes in the cluster are heterogeneous, i.e. they have different types of hardware (processors, memory, GPUs), different functionality (some more advanced than others) and different performance characteristics. If a program requires specific features, you need to specifically request those for that job (see [Submitting jobs](../../../manual/job-submission/job-scripts)). 


{{% alert title="Note" color="info" %}}
All servers have [Advanced Vector Extensions](https://en.wikipedia.org/wiki/Advanced_Vector_Extensions) 1 and 2 (AVX, AVX2) support, and hyper-threading (`ht`) processors (two CPUs per core, always allocated in pairs).
{{% /alert %}}

{{% alert title="Note" color="info" %}}
You can use Slurm's `sinfo` command to get various information about cluster nodes. For example, to get an overview of compute nodes on DAIC, you can use the command:

```bash
$ sinfo --all --format="%P %N %c %m %G %b" --hide -S P,N -a | grep -v "general" | awk 'NR==1 {print; next} {match($5, /gpu:[^,]+:[0-9]+/); if (RSTART) print $1, $2, $3, $4, substr($5, RSTART, RLENGTH), $6; else print $1, $2, $3, $4, "-", $6  }'  
```
Check out the [Slurm's sinfo page](https://slurm.schedmd.com/sinfo.html) and  [wikipedia's awk page](https://en.wikipedia.org/wiki/AWK) for more info on these commands.

{{% /alert %}}

## List of all nodes

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
    <td></td>
    <td>16</td>
    <td>64</td>
    <td></td>
    <td>1500 GB</td>
    <td>Tesla V100 SXM2 16GB</td>
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