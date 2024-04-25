---
title: "Apptainer"
linkTitle: "Apptainer"
weight: 10
description: >
  How to use Apptainer on DAIC?
---

# REIT Apptainer Template
Apptainer is a container platform. It allows you to create and run containers that package up pieces of software in a way that is portable and reproducible. You can build a container using Apptainer on your laptop, and then run it on many on an HPC cluster. Apptainer was created to run complex applications on HPC clusters in a simple, portable, and reproducible way. This repository contains a template for building a Apptainer (former Singularity) container using `miniforge`, and `mamba` (similar to conda). The examples directory also contains examples for other setups.

### Apptainer features
- Verifiable reproducibility and security, using cryptographic signatures, an immutable container image format, and in-memory decryption.
- Integration over isolation by default. Easily make use of GPUs, high speed networks, parallel filesystems on a cluster or server by default.
- Mobility of compute. The single file SIF container format is easy to transport and share.
- A simple, effective security model. You are the same user inside a container as outside, and cannot gain additional privilege on the host system by default. Read more about Security in Apptainer.

## Template
### Template structure
- `environment.yaml`: Conda environment file specifying the Python and library dependencies.
- `requirements.txt`: Python library requirements file for pip-installable packages.
- `Apptainer.def`: Apptainer definition file specifying the environment setup and dependencies.
- `build.sh`: Bash script to build the container using Apptainer.
- `test.sh`: Bash script to test if the container loads the environment properly.
- `deploy.sh`: Bash script to deploy the built container to the desired location(s).

Adjust the files according to your needs.

### Usage
1. Modify the `Apptainer.def`, `environment.yaml`, and `requirements.txt` files to include your desired environment setup and dependencies.
2. Modify `build.sh`, `test.sh`, and `deploy.sh` to match your setup.
3. Especially, change the name of the container consistently in all files.
3. Run `build.sh` to build the Apptainer container.
3. Use `test.sh` to verify if the container loads the environment correctly.
4. Run `deploy.sh` to deploy the built Apptainer container to the appropriate location(s).

## FAQ

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

### How to install Apptainer without sudo?
This explains how to install Apptainer on Linux (Debian) systems without sudo.

    sudo apt-get install -y rpm2cpio  # well, you still need some sudo
    curl -s https://raw.githubusercontent.com/apptainer/apptainer/main/tools/install-unprivileged.sh | bash -s - /my/installation/directory

### How to use Apptainer on MacBook?
On MacBook with M1/2/3 processors you have to run `apptainer` inside a VM. You can use `lima` for that.
First, you have to install `lima`

> **Warning**: You might not be able to use a container build on a MacBook on DAIC or DelftBlue due to CPU architecture incompabilities. Start with a minimal container to test your setup.

#### 1. Install lima
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
brew install qemu lima
```

#### 2. Create the VM
```
limactl create --name=apptainer template://apptainer
```

#### 3. Make home directory writeable
To be able to build containers, you need to grant `lima` write permissions to your home directory.

```
vi ~/.lima/apptainer/lima.yml
```

and change

```
mounts:
  - location: "~"
  - location: "/tmp/lima"
    writable: true
```

to

```
mounts:
  - location: "~"
    writeable: true
  - location: "/tmp/lima"
    writable: true
```

#### 4. Start the VM
```
limactl start apptainer
```

#### 5. Enter the VM
```
limactl shell apptainer
```

#### 6. Inside the VM you can run `apptainer` normally.
```
apptainer
>>>
Usage:
  apptainer [global options...] <command>

Available Commands:
  build       Build an Apptainer image
  cache       Manage the local cache
  capability  Manage Linux capabilities for users and groups
  checkpoint  Manage container checkpoint state (experimental)
  completion  Generate the autocompletion script for the specified shell
  config      Manage various apptainer configuration (root user only)
  delete      Deletes requested image from the library
  exec        Run a command within a container
  inspect     Show metadata for an image
  instance    Manage containers running as services
  key         Manage OpenPGP keys
  keyserver   Manage apptainer keyservers
  oci         Manage OCI containers
  overlay     Manage an EXT3 writable overlay image
  plugin      Manage Apptainer plugins
  pull        Pull an image from a URI
  push        Upload image to the provided URI
  registry    Manage authentication to OCI/Docker registries
  remote      Manage apptainer remote endpoints
  run         Run the user-defined default command within a container
  run-help    Show the user-defined help for an image
  search      Search a Container Library for images
  shell       Run a shell within a container
  sif         Manipulate Singularity Image Format (SIF) images
  sign        Add digital signature(s) to an image
  test        Run the user-defined tests within a container
  verify      Verify digital signature(s) within an image
  version     Show the version for Apptainer

Run 'apptainer --help' for more detailed usage information.
```

## References
- [Apptainer](https://apptainer.org/docs/user/latest/introduction.html) (formerly Singularity) simplifies the creation and execution of containers, ensuring software components are encapsulated for portability and reproducibility.
- [Lima](https://lima-vm.io/docs/) launches Linux virtual machines with automatic file sharing and port forwarding (similar to WSL2).
