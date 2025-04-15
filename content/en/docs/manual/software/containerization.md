---
title: "Containerization"
weight: 30
description: >
  How to use Apptainer on DAIC?
---

## Apptainer
Apptainer is a container platform. It allows you to create and run containers that package up pieces of software in a way that is portable and reproducible. You can build a container using Apptainer on your laptop, and then run it on many on an HPC cluster. Apptainer was created to run complex applications on HPC clusters in a simple, portable, and reproducible way. This repository contains a template for building a Apptainer (former Singularity) container using `miniforge`, and `mamba` (similar to conda). The examples directory also contains examples for other setups.

### Apptainer features
- Verifiable reproducibility and security, using cryptographic signatures, an immutable container image format, and in-memory decryption.
- Integration over isolation by default. Easily make use of GPUs, high speed networks, parallel filesystems on a cluster or server by default.
- Mobility of compute. The single file SIF container format is easy to transport and share.
- A simple, effective security model. You are the same user inside a container as outside, and cannot gain additional privilege on the host system by default. Read more about Security in Apptainer.

### Template
The [Apptainer template](https://gitlab.ewi.tudelft.nl/reit/apptainer-template) repository maintained by the [Research Engineering and Infrastructure Team](https://reit.tudelft.nl) is a good starting point to create your own apptainers.

### How to use Apptainer on the cluster with SLURM?
Here is an example how to use the container in a SLURM script.

```bash
#!/bin/sh
#SBATCH --job-name="apptainer-job"
#SBATCH --account="my-account"
#SBATCH --partition="general"      # Request partition.
#SBATCH --time=01:00:00            # Request run time (wall-clock). Default is 1 minute
#SBATCH --nodes=1.                 # Request 1 node
#SBATCH --tasks-per-node=1         # Set one task per node
#SBATCH --cpus-per-task=4          # Request number of CPUs (threads) per task.
#SBATCH --gres=gpu:1               # Request 1 GPU
#SBATCH --mem=4GB                  # Request 4 GB of RAM in total
#SBATCH --mail-type=END            # Set mail type to 'END' to receive a mail when the job finishes. 
#SBATCH --output=slurm-%x-%j.out   # Set name of output log. %j is the Slurm jobId
#SBATCH --error=slurm-%x-%j.err    # Set name of error log. %j is the Slurm jobId

export APPTAINER_IMAGE="/path/to/my-container.sif"

# If you use GPUs
module use /opt/insy/modulefiles
module load cuda/12.1

# Run script
srun apptainer exec \
  --nv \
  --env-file ~/.env \                 
  -B $HOME:$HOME \
  -B /tudelft.net/:/tudelft.net/ \
  $APPTAINER_IMAGE \
  python script.py

# --nv binds NVIDIA libraries from the host (only if you use CUDA)
# --env-file source additional environment variables from e.g. .env file (optional)
# -B /$HOME:/$HOME/ mounts host file-sytem inside container
# The home folder should be mounted by default, but sometimes it is not
# -B can be used several times, change this to match your cluster file-system
# APPTAINER_IMAGE is the full path to the container.sif file
# python script.py is the command that you want to use inside the container

```

### Tutorial

See the [Apptainer tutorial](/tutorials/apptainer).

