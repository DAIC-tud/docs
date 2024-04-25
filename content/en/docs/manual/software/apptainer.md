---
title: "Apptainer"
linkTitle: "Apptainer"
weight: 10
description: >
  How to use Apptainer on DAIC?
---

Apptainer is a container platform. It allows you to create and run containers that package up pieces of software in a way that is portable and reproducible. You can build a container using Apptainer on your laptop, and then run it on many on an HPC cluster. Apptainer was created to run complex applications on HPC clusters in a simple, portable, and reproducible way. This repository contains a template for building a Apptainer (former Singularity) container using `miniforge`, and `mamba` (similar to conda). The examples directory also contains examples for other setups.

### Apptainer features
- Verifiable reproducibility and security, using cryptographic signatures, an immutable container image format, and in-memory decryption.
- Integration over isolation by default. Easily make use of GPUs, high speed networks, parallel filesystems on a cluster or server by default.
- Mobility of compute. The single file SIF container format is easy to transport and share.
- A simple, effective security model. You are the same user inside a container as outside, and cannot gain additional privilege on the host system by default. Read more about Security in Apptainer.

### How to use it on the cluster with SLURM?
Here is how to use the container in a SLURM script.

```bash
#!/bin/sh
#SBATCH --job-name="my-script"
#SBATCH --account="my-account"
#SBATCH --partition="my-partition" # Request partition.
#SBATCH --time=01:00:00            # Request run time (wall-clock). Default is 1 minute
#SBATCH --nodes=1.                 # Request 1 node
#SBATCH --tasks-per-node=1         # Set one task per node
#SBATCH --cpus-per-task=4          # Request number of CPUs (threads) per task.
#SBATCH --gres=gpu:1               # Request 1 GPU
#SBATCH --mem=4GB                  # Request 4 GB of RAM in total
#SBATCH --mail-type=END            # Set mail type to 'END' to receive a mail when the job finishes. 
#SBATCH --output=slurm-%x-%j.out   # Set name of output log. %j is the Slurm jobId
#SBATCH --error=slurm-%x-%j.err    # Set name of error log. %j is the Slurm jobId

export DATASETS_ROOT="/scratch/$USER/datasets"
export APPTAINER_ROOT="/path/to/container/folder"
export APPTAINER_NAME="my-container.sif"

# If you use GPUs
## Setup environment
module load cuda/12.1

## Use this simple command to check that your sbatch 
## settings are working (it should show the GPU that you requested)
nvidia-smi

# Run script
srun apptainer exec \
  --nv \                              # Bind NVIDIA libraries from the host
  --env-file ~/.env \                 # Source additional environment variables (optional)
  -B /home/$USER:/home/$USER \        # Mount host file-sytem inside container 
  -B /projects/:/projects/ \          # (different for each cluster)
  -B /scratch/$USER:/scratch/$USER \
  $APPTAINER_ROOT/$APPTAINER_NAME \   # Path to the Apptainer container to run
  python my-script.py                 # Command to be executed inside container
```
