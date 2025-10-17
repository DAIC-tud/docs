---
title: 2025-10-17
# subtitle: > 
date: 2025-10-17
description: >
  _New Feature:_ Submitting Jobs from Compute Nodes
---

It's now possible to **submit Slurm jobs directly from DAIC compute nodes**.

This allows workflow managers such as **Snakemake**, **Nextflow**, or other orchestration tools to run smoothly without needing to return to the login node for each submission.

{{% alert title="Important" color="warning" %}}
Please submit jobs only through Slurm commands (`sbatch`, `srun`, `salloc`), not via background processes or recursive scripts, to ensure fair scheduling and stable operation.
{{% /alert %}}

For most users, this means that standard HPC workflows will now function more smoothly on DAIC.