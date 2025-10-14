---
title: "Login Nodes"
weight: 2
description: >
  Overview of DAIC login nodes and appropriate usage guidelines.
---


Login nodes act as the gateway to the DAIC cluster. They are intended for lightweight tasks such as job submission, file transfers, and compiling code (on specific nodes). They are not designed for running resource-intensive jobs, which should be submitted to the [compute nodes](/docs/system/compute-nodes).


### Specifications and usage notes

| Hostname  | CPU (Sockets x Model)                               | Total Cores | Total RAM  | Operating System      | GPU Type     | GPU Count | Usage Notes                                                   |
|-----------|-----------------------------------------------------|-------------|------------|-----------------------|--------------|-----------|---------------------------------------------------------------|
| `login1.daic.tudelft.nl`  | 1 x Intel(R) Xeon(R) CPU E5-2620 v4 @ 2.10GHz       | 8           | 15.39 GB   | OpenShift Enterprise   | Quadro K2200 | 1         | For file transfers, job submission, and lightweight tasks.   |
| `login2.daic.tudelft.nl`  | 1 x Intel(R) Xeon(R) CPU E5-2683 v3 @ 2.00GHz       | 1           | 3.70 GB    | OpenShift Enterprise   | N/A          | N/A       | Virtual server, for non-intensive tasks. **No compilation.** |
| `login3.daic.tudelft.nl`  | 2 x Intel(R) Xeon(R) CPU E5-2683 v4 @ 2.10GHz       | 32          | 503.60 GB  | RHEV                  | Quadro K2200 | 1         | For large compilation and interactive sessions.              |

{{% alert title="Login1 resource limits (effective immediately)" color="warning" %}}

Due to excessive background usage (especially from VSCode-related processes), per-user limits on `login1` have been reduced to: 1 CPU, 1 GB RAM. This helps prevent system-wide instability.  
For compiling large code or running memory-heavy tasks, please use an interactive job: [Interactive jobs on compute nodes](/docs/manual/job-submission/slurm-basics/#interactive-jobs-on-compute-nodes)
{{% /alert %}}
