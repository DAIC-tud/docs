---
title: "Apptainer tutorial"
weight: 2
description: >
  Using Apptainer to containerize environments.
---


## What and Why containerization?

Containerization packages your software, libraries, and dependencies into a single portable unit: a *container*. This makes your application behave the same way everywhere: on your laptop, in the cloud, or on DAIC. This means:
- **Consistency:** The application runs the same way regardless of where it's executed. You can develop on one machine, test on another, and deploy on a cluster without worrying about dependency differences.  
- **Isolation:** Each container is independent from others, preventing conflicts and enhancing security and reliability.  
- **Portability:** Containers can run on different systems without modification, simplifying movement between servers, clusters, or clouds.  
- **Efficiency:** Containers share the host system's resources like the operating system, making them lightweight and fast to start compared to virtual machines.

On DAIC specifically, users often encounter issues with limited home directory space or Windows-based `/tudelft.net` mounts (see [Storage](/docs/system/storage)), which can complicate the use of `conda/mamba` and/or `pip`. Containers offer a solution by encapsulating all software and dependencies in a self-contained environment. You can, for instance, store containers on `staff-umbrella` with all required dependencies, including those installed via `pip`, and run them reliably and reproducibly without being limited by home directory size or mount compatibility.

## Containerization on DAIC: Apptainer
DAIC supports [Apptainer](https://apptainer.org/docs/user/main/introduction.html)  (previously Apptainer), an open-source container platform, designed to run on High-performance computing environments. Apptainer runs container images securely on shared clusters and allows you to use Docker images directly, without needing Docker itself.

A typical Apptainer workflow revolves around three key components:

| Component | Description |
|------------|--------------|
| *Definition file* (`*.def`) | A recipe describing how to build the container: which base image to use and which packages to install. |
| *Image* (`*.sif`) | A single portable file containing the full environment: operating system, libraries, and applications. |
| *Container* | A running instance of an image, with its own writable workspace for temporary files or intermediate data. |

Because Apptainer integrates well with Slurm, containers can be launched directly within batch jobs or interactive sessions on DAIC.  
The following sections show how to obtain, build, and run images.

## Workflow overview

The typical lifecycle for containers on DAIC is:

1. **Build** the image locally from a `.def` file.  
2. **Transfer or pull** the resulting `.sif` file onto DAIC.  
3. **Test** interactively using `sinteractive` on a compute node.  
4. **Run** in a batch job with `sbatch` or `srun` using `apptainer exec` or `apptainer run`.  
5. **Provision** bind mounts, GPU flags, and cache locations as needed.  
6. **Clean up** and manage storage (e.g., `APPTAINER_CACHEDIR`).

{{< figure src="images/apptainer-daic-workflow.png" alt="Apptainer workflow on DAIC: build → transfer → test → run" width="70%" >}}

<!-- Build locally → Transfer to DAIC → Test in `sinteractive` → Run with `sbatch`/`srun` → Maintain (cache/storage)

```mermaid
#flowchart TB
#  A["Build container locally (`apptainer build image.sif recipe.def`)"] -- B{Get image onto DAIC}
#  B --|scp image.sif| C[staff-umbrella / project dir]
#  B --|"pull from registry (DockerHub/NGC/...etc)"| C
#  C -- D["sinteractive (test on a compute node)"]
#  D -- E["Run batch job: sbatch/srun with apptainer exec/run"]
#  E -- F["Data access --bind/--mount"]
#  E -- G["GPU access --nv"]
#  E -- H["Isolation --C / -c"]
#  Z["Maintenance\nAPPTAINER_CACHEDIR → non-$HOME\nclean cache / manage storage"] -.-> A
```
-->

## How to run commands/programs inside a container?

Once you have a container image (e.g., `myimage.sif`), you can launch it in different ways depending on how you want to interact with it:

| Command | Description | Example |
|----------|--------------|----------|
| `apptainer shell <image>` | Start an interactive shell inside the container. | `apptainer shell myimage.sif` |
| `apptainer exec <image> <command>` | Run the `<command>` inside the container, then exit. | `apptainer exec myimage.sif python --version` |
| `apptainer run <image>` | Execute the container's default entrypoint (defined in its recipe). | `apptainer run myimage.sif` |


where: 
* `<image>` is the path to a container image, typically, a `*.sif` file.

**Tips:**
- Use `shell` for exploration or debugging inside the container.
- Use `exec` or `run` for automation, workflows, or Slurm batch jobs.  
- Add `-C` or `-c` to isolate the container filesystem (see [Exposing host directories](#exposing-host-directories)).


{{% alert title="Tip: Test interactively before submitting jobs" color="info" %}}
For containers that need GPUs or large memory, start an interactive session first:
```shell-session
$ hostname  # To check this is DAIC. login[1-3] are the login nodes
login1.daic.tudelft.nl 

$ sinteractive --gres=gpu:1 --mem=8G --time=01:00:00  # Request an interactive session with 1 GPU, 8GB memory, 1 hour time
Note: interactive sessions are automatically terminated when they reach their time limit (1 hour)!
srun: job 8543393 queued and waiting for resources
srun: job 8543393 has been allocated resources
 13:35:30 up 5 days,  3:41,  0 users,  load average: 8,79, 7,60, 7,11

$ hostname # To check we are on a compute node
grs3.daic.tudelft.nl 

$ apptainer exec --nv myimage.sif python script.py
```
This helps verify everything works before submitting a batch job with `sbatch` or `srun`.

{{% /alert %}} 

<!-- 
Add workflow for how to work with containers:
- pull image
- dependent
- building
-->

## How to get container files?

You can obtain container images in two main ways:

1. **Pull prebuilt images** by pulling from a container registry/repository (see [Using prebuilt images](#1-using-prebuilt-images)).
2. **Build your own** image locally using a definition file (`*.def`), then transfer the resulting `.sif` file to DAIC (see [Building images](#2-building-images)).


### 1. Using prebuilt images

Apptainer allows pulling and using images directly from repositories like [DockerHub](https://hub.docker.com/), [BioContainers](https://biocontainers.pro/registry), [NVIDIA GPU Cloud (NGC)](https://ngc.nvidia.com/catalog/containers), and others.

#### Example: Pulling from DockerHub

```shell-session
$ hostname # check this is DAIC
login1.daic.tudelft.nl

$ mkdir ~/containers && cd ~/containers # as convenience, use this directory

$ apptainer pull docker://ubuntu:latest # actually pull the image
INFO:    Converting OCI blobs to SIF format
INFO:    Starting build...
Getting image source signatures
Copying blob 837dd4791cdc done  
Copying config 1f6ddc1b25 done  
Writing manifest to image destination
Storing signatures
...
INFO:    Creating SIF file...
```

Now, to check the obtained image file:

```shell-session
$ ls  
ubuntu_latest.sif

$ apptainer exec ubuntu_latest.sif cat /etc/os-release # execute cat command and exit
PRETTY_NAME="Ubuntu 22.04.2 LTS"
NAME="Ubuntu"
VERSION_ID="22.04"
VERSION="22.04.2 LTS (Jammy Jellyfish)"
VERSION_CODENAME=jammy
ID=ubuntu
ID_LIKE=debian
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
UBUNTU_CODENAME=jammy

$ ls /.apptainer.d/ # container-specific directory should not be found on host
ls: cannot access /.apptainer.d/: No such file or directory

$ apptainer shell ubuntu_latest.sif # launch container interactively
Apptainer>
Apptainer> hostname
login1.daic.tudelft.nl
Apptainer> ls
ubuntu_latest.sif
Apptainer> ls /.apptainer.d/ 
Apptainer  actions  env  labels.json  libs  runscript  startscript
Apptainer> exit
```

Notes:
* Inside the container, the command prompt changes to `Apptainer>`
* The container inherits your environment (e.g., `$HOME`, `hostname`) but has its own internal filesystem (e.g. `/.apptainer.d`)

{{% alert title="Tip: Isolate your host filesystem" color="warning"%}}
To prevent accidental deletes/edits, add a `-c` or `-C` flags to your apptainer commands to isolate filesystems. For example:
```bash
$ apptainer shell -C ubuntu_latest.sif
```
{{% /alert %}}

#### Example: Pulling from NVIDIA GPU cloud (NGC)

NGC provides pre-built images for GPU accelerated applications. These images are large, and one is recommended to download them locally (in your machine), and then transfer to DAIC.
To install Apptainer in your machine, follow the official [Installing Apptainer instructions](https://apptainer.org/docs/admin/main/installation.html). 

{{% alert title="Important: Cache and filesystem limits" color="warning" %}}
By default, Apptainer images are saved to `~/.apptainer`. To avoid quota issues, set the environment variable `APPTAINER_CACHEDIR` to a different location.

```bash
export APPTAINER_CACHEDIR=/tudelft.net/staff-umbrella/<YourDirectory>/apptainer/cache
```

Pulling directly to `bulk` or `umbrella` is not supported, so pull large images locally, then copy the `*.sif` file to DAIC.
{{% /alert %}} 

```shell-session
$ hostname #check this is your own PC/laptop
$ apptainer pull docker://nvcr.io/nvidia/pytorch:23.05-py3
$ scp pytorch_23.05-py3.sif  hpc-login:/tudelft.net/staff-umbrella/...<YourDirectory>/apptainer
```

Test the image on DAIC:

```shell-session
$ hostname # check this is DAIC not your own PC/laptop
login1.daic.tudelft.nl

$ cd /tudelft.net/staff-umbrella/...<YourDirectory>/apptainer # path where you put images

$ sinteractive --gres=gpu:1 --time=00:05:00 # request a gpu node

$ apptainer shell -C --nv pytorch_23.05-py3.sif  #--nv to use NVIDIA GPU and have CUDA support
Apptainer> python -c "import torch; print(torch.cuda.is_available())"
True
```

### 2. Building images

If you prefer (or need) a custom container image, you can build one from a _definition_ file (`*.def`), that specifies your dependencies and setup steps.

On DAIC, you can build images directly if your current directory allows writes and sufficient quota (e.g., under `staff-umbrella`).  
For large or complex builds, it can be more convenient to build locally on your workstation and then transfer the resulting `.sif` file to DAIC.

{{% alert title="Tip: Root privileges not always required" color="info" %}}
Apptainer supports *rootless builds*.  
You only need `sudo` when:
- building from base images that require root setup (e.g., `Bootstrap: docker` on older systems), or  
- writing the resulting image to a protected location.

Otherwise, you can directly build using:
```shell-session
$ apptainer build myimage.sif myimage.def

```
{{% /alert %}}

#### Example: CUDA-enabled container

An example definion file, `cuda_based.def`, for a cuda-enabled container may look as follows:

{{< card code=true header="cuda_based.def" lang="bash" >}}
# Header
Bootstrap: docker
From: nvidia/cuda:12.1.1-devel-ubuntu22.04

# (Optional) Sections/ data blobs
%post
    apt-get update # update system
    apt-get install -y git   # install git
    git clone https://github.com/NVIDIA/cuda-samples.git  # clone target repository
    cd cuda-samples
    git fetch origin --tags && git checkout v12.1 # fetch certain repository version
    cd Samples/1_Utilities/deviceQuery && make # install certain tool

%runscript
    /cuda-samples/Samples/1_Utilities/deviceQuery/deviceQuery  
{{< /card >}}

where:
* The _header_, specifies the source (eg, `Bootstrap: docker`) and the base image (`From: nvidia/cuda:12.1.1-devel-ubuntu22.04`). Here, the container builds on _Ubuntu 22.04 with CUDA 12.1_ pre-installed. 
* The rest of the file are optional _data blobs_ or _sections_. In this example, the following blobs are used:
  * `%post`: the steps to download, configure and install needed custom software and libraries on the base image. In this example, the steps install `git`, clone a repo, and install a package via `make`
  * `%runscript`: the entry point to the container with the `apptainer run` command. In this example, the `deviceQuery` is executed once the container is run.
  * Other blobs may be present in the `def` file. See [Definition files documentation](https://apptainer.org/docs/user/main/definition_files.html#definition-files) for more details and examples.

And now, build this image and send it over to DAIC:

```shell-session
$ hostname #check this is your machine
$ apptainer build cuda_based_image.sif cuda_based.def # building may take ~ 2-5 min, depending on your internet
INFO:    Starting build...
Getting image source signatures
Copying blob d5d706ce7b29 [=>------------------------------------] 29.2MiB / 702.5MiB
...
INFO:    Adding runscript
INFO:    Creating SIF file...
INFO:    Build complete: cuda_based_image.sif  
$
$ scp cuda_based_image.sif  daic-login:/tudelft.net/staff-umbrella/...<YourDirectory>/apptainer # send to DAIC
```

On DAIC, check the image:

```shell-session
$ hostname # check you are on DAIC
login1.daic.tudelft.nl 
$ sinteractive --cpus-per-task=2 --mem=1024 --gres=gpu --time=00:05:00 # request a gpu node
$ hostname # check you are on a compute node
insy13.daic.tudelft.nl

$ apptainer run --nv -C cuda_based_image.sif # --nv to use NVIDIA GPU and have CUDA support
/cuda-samples/Samples/1_Utilities/deviceQuery/deviceQuery Starting...

 CUDA Device Query (Runtime API) version (CUDART static linking)

Detected 1 CUDA Capable device(s)

Device 0: "NVIDIA GeForce GTX 1080 Ti"
  CUDA Driver Version / Runtime Version          12.1 / 12.1
  CUDA Capability Major/Minor version number:    6.1
  Total amount of global memory:                 11172 MBytes (11714887680 bytes)
  (028) Multiprocessors, (128) CUDA Cores/MP:    3584 CUDA Cores
  GPU Max Clock rate:                            1582 MHz (1.58 GHz)
  Memory Clock rate:                             5505 Mhz
  Memory Bus Width:                              352-bit
  L2 Cache Size:                                 2883584 bytes
  Maximum Texture Dimension Size (x,y,z)         1D=(131072), 2D=(131072, 65536), 3D=(16384, 16384, 16384)
  Maximum Layered 1D Texture Size, (num) layers  1D=(32768), 2048 layers
  Maximum Layered 2D Texture Size, (num) layers  2D=(32768, 32768), 2048 layers
  Total amount of constant memory:               65536 bytes
  Total amount of shared memory per block:       49152 bytes
  Total shared memory per multiprocessor:        98304 bytes
  Total number of registers available per block: 65536
  Warp size:                                     32
  Maximum number of threads per multiprocessor:  2048
  Maximum number of threads per block:           1024
  Max dimension size of a thread block (x,y,z): (1024, 1024, 64)
  Max dimension size of a grid size    (x,y,z): (2147483647, 65535, 65535)
  Maximum memory pitch:                          2147483647 bytes
  Texture alignment:                             512 bytes
  Concurrent copy and kernel execution:          Yes with 2 copy engine(s)
  Run time limit on kernels:                     No
  Integrated GPU sharing Host Memory:            No
  Support host page-locked memory mapping:       Yes
  Alignment requirement for Surfaces:            Yes
  Device has ECC support:                        Disabled
  Device supports Unified Addressing (UVA):      Yes
  Device supports Managed Memory:                Yes
  Device supports Compute Preemption:            Yes
  Supports Cooperative Kernel Launch:            Yes
  Supports MultiDevice Co-op Kernel Launch:      Yes
  Device PCI Domain ID / Bus ID / location ID:   0 / 141 / 0
  Compute Mode:
     < Default (multiple host threads can use ::cudaSetDevice() with device simultaneously) >

deviceQuery, CUDA Driver = CUDART, CUDA Driver Version = 12.1, CUDA Runtime Version = 12.1, NumDevs = 1
Result = PASS
```

{{% alert title="Tip: Enable GPU access" color="warning"%}}
Always pass `--nv` to apptainer to run GPU-accelerated applications or libraries inside the container. Requirements:

 1) your host system must have NVIDIA GPU drivers installed and compatible with your Apptainer version, and 
 2) the container must have the necessary dependencies and configurations to support GPU acceleration.

```bash
$ apptainer shell --nv -C cuda_based_image.sif
```
{{% /alert %}}


{{% alert title="Note on reproducibility" color="info"%}}
Definition-file builds are the most reproducible approach.
However, in cases of complex dependencies, you can first prototype interactively in `writable sandbox` mode first. In such cases, take note of all installation commands used in the sandbox, so you can include them in a recipe file. See [Apptainer Sandbox Directories](https://apptainer.org/docs/user/main/quick_start.html#sandbox-directories) for more details.
{{% /alert %}}


#### Example: Extending existing images

During software development, it is common to incrementally build code and go through many iterations of debugging and testing.
To save time, you can base a new image on an existing one using the `Bootstrap: localimage` and `From:<path/to/local/image>` header.
This avoids re-installing the same dependencies with every iteration.

As an example, assume it is desirable to develop some code on the basis of the `cuda_based.sif` image created in the [Example: CUDA-enabled container](#example-cuda-enabled-container).  Building from the original `cuda_based.def` file can take ~ 4 minutes. However, if the `*.sif` file is already available, building on top of it, via a `dev_on_cuda_based.def` file as below, takes ~ 2 minutes. This is already a time saving  factor of 2.

{{< card code=true header="dev_on_cuda_based.def" lang="bash" >}}
# Header
Bootstrap: localimage
From: cuda_based.sif

# (Optional) Sections/ data blobs
%runscript
    echo "Arguments received: $*"
    exec echo "$@"
{{< /card >}}

Now, build and test:
```shell-session
$ apptainer build dev_image.sif # build the image
INFO:    Starting build...
INFO:    Verifying bootstrap image cuda_based.sif
WARNING: integrity: signature not found for object group 1
WARNING: Bootstrap image could not be verified, but build will continue.
INFO:    Adding runscript
INFO:    Creating SIF file...
INFO:    Build complete: dev_image.sif

$ apptainer run  dev_image.sif "hello world" # check runscript of the new def file is executed
INFO:    gocryptfs not found, will not be able to use gocryptfs
Arguments received: hello world
hello world

$ apptainer shell dev_image.sif # further look inside the image
Apptainer> 
Apptainer> ls /cuda-samples/Samples/1_Utilities/deviceQuery/deviceQuery # commands installed in the original image are available
/cuda-samples/Samples/1_Utilities/deviceQuery/deviceQuery

Apptainer>
Apptainer> cat /.apptainer.d/bootstrap_history/Apptainer0 # The original def file is also preserved 
bootstrap: docker
from: nvidia/cuda:12.1.1-devel-ubuntu22.04

%runscript
    /cuda-samples/Samples/1_Utilities/deviceQuery/deviceQuery  


%post
    apt-get update # update system
    apt-get install -y git   # install git
    git clone https://github.com/NVIDIA/cuda-samples.git  # clone target repository
    cd cuda-samples
    git fetch origin --tags && git checkout v12.1 # fetch certain repository version
    cd Samples/1_Utilities/deviceQuery && make # install certain tool
```

As can be seen in this example, the new def file not only preserves the dependencies of the original image, but it also preserves a complete history of all build processes while giving flexible environment that can be customized as need arises.

#### Example: Deploying conda and pip in a container

There might be situations where you have a certain conda environment in your local machine that you need to set up in DAIC to commence your analysis. In such cases, deploying your conda environment in a container and sending this container to DAIC does the job for you. 

As an example, let's create a simple demo environment, `environment.yml` in our local machine, 

```bash
name: apptainer
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.9
  - matplotlib
  - pip
  - pip:
    - -r requirements.txt
```

And everything that should be installed with pip in `requirement.txt` file:
```bash
--extra-index-url https://download.pytorch.org/whl/cu123
torch
annoy
```

Now, it is time to create the container definition file `Apptainer.def`. One option is to base the image on `condaforge/miniforge`, which is a minimal Ubuntu installation with `conda` preinstalled at `/opt/conda`:

```bash
Bootstrap: docker
From: condaforge/miniforge3:latest

%files
    environment.yml /environment.yml
    requirements.txt /requirements.txt

%post
    # Update and install necessary packages
    apt-get update && apt-get install -y tree time vim ncdu speedtest-cli build-essential

    # Create a new Conda environment using the environment files.
    mamba env create --quiet --file /environment.yml
    
    # Clean up
    apt-get clean && rm -rf /var/lib/apt/lists/*
    mamba clean --all -y

    # Now add the script to activate the Conda environment
    echo '. "/opt/conda/etc/profile.d/conda.sh"' >> $APPTAINER_ENVIRONMENT
    echo 'conda activate apptainer' >> $APPTAINER_ENVIRONMENT
```

{{% alert title="APPTAINER_ENVIRONMENT" color="secondary" %}}
The `$APPTAINER_ENVIRONMENT` variable in Apptainer refers to a special shell script that gets sourced when a container is run in shell mode. This is a key mechanism for setting up the environment for your container.

Here's what's happening in the code:

1. `echo '. "/opt/conda/etc/profile.d/conda.sh"' >> $APPTAINER_ENVIRONMENT`
   - This adds a command to source the Conda initialization script
   - The script enables the `conda` command in your shell environment

2. `echo 'conda activate apptainer' >> $APPTAINER_ENVIRONMENT`
   - This adds a command to activate the "apptainer" Conda environment
   - This ensures your container automatically starts with the right environment activated

When a user runs your container with `apptainer shell my-container.sif`, these commands will execute automatically, ensuring:

1. The conda command is available
2. The "apptainer" environment is activated
3. All the Python packages specified in your `environment.yml` are available

This approach is much cleaner than requiring users to manually activate the environment every time they run the container. It makes your container more user-friendly and ensures consistent behavior.

This file is similar to the file in the [Building images](#building-images), with the addition of `%files` area. `%files` specifies the files in the host system (ie, your machine) that need to be copied to the container image, and optionally, where should they be available. In the previous example, the `environment.yml` file will be available in `/opt/` in the container.
{{% /alert %}}


Now, time to build and check the image:

```bash
$ apptainer build demo-env-image.sif Apptainer.def
INFO:    Starting build...
Getting image source signatures
...
INFO:    Creating SIF file...       
INFO:    Build complete: Apptainer.sif
...
```

Let's verify our container setup:

```bash
$ apptainer exec demo-env-image.sif which python
/opt/conda/envs/apptainer/bin/python
```

Perfect! This confirms that our container image built successfully and the Conda environment is automatically activated. The Python executable is correctly pointing to our custom environment path, indicating that all our dependencies should be available.


We are going to use the environment inside a container together with a Python script that we store outside the container.
Create the file `analysis.py`, which generate a plot:

```python
#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

plt.plot(x, y)
plt.title('Sine Wave')
plt.savefig('sine_wave.png')
```

Now, we can run the analysis:

```bash
$ apptainer exec demo-env-image.sif python analysis.py  
$ ls # check the image file was created
sine_wave.png
```

{{% alert title="Warning" color="warning" %}}
In the last example, the container read and wrote a file to the host system directly. This behavior is risky. You are strongly recommended to expose only the desired host directories to the container. See [Exposing host directories](#exposing-host-directories)
{{% /alert %}}


## Exposing host directories
Depending on use case, it may be necessary for the container to read or write data from or to the host system. For example, to expose only files in a host directory called `ProjectDataDir` to the container image's `/mnt` directory, add the `--bind` directive with appropriate `<hostDir>:<containerDir>` mapping to the commands you use to launch the container, in conjunction with the `-C` flag eg, `shell` or `exec` as below:

```bash
$ ls  # check ProjectDataDir exists
$ ls ProjectDataDir # check contents of ProjectDataDir
raw_data.txt
$ apptainer shell -C --bind ProjectDataDir:/mnt ubuntu_latest.sif # Launch the container with ProjectDataDir bound
Apptainer> ls
Apptainer> ls /mnt # check the files are accessible inside the container
raw_data.txt
Apptainer> echo "Date: $(date)" >> raw_data.txt # edit the file
Apptainer> tail -n1 raw_data.txt # check the date was written to the file
Apptainer> exit # exit the container
$ tail -n1 ProjectDataDir/raw_data.txt # check the change persisted
```
If the desire is to expose this directory as read-only inside the container, the `--mount` directive should be used instead of `--bind`, with `ro`designation as follows:

```bash
apptainer shell -C --mount type=bind,source=ProjectDataDir,destination=/mnt,ro ubuntu_latest.sif # Launch the container with ProjectDataDir bound
Apptainer> ls /mnt # check the files are accessible inside the container
raw_data.txt
Apptainer> echo "Date: $(date)" >> /mnt/raw_data.txt # attempt to edit fails
bash: tst: Read-only file system
```

## _[Advanced:]()_ containers and (fake) native installation 
It's possible to use Apptainer to install and then use software as if it were installed natively in the host system. For example, if you are a bioinformatician, you may be using software like  [`samtools`](http://www.htslib.org/) or [`bcftools`](https://samtools.github.io/bcftools/bcftools.html) for many of your analyses, and it may be advantageous to call it directly. Let's take this as an illustrative example:


1. For hygiene, create the following file hierarchy: below a `software` directory an `exec` directory to put the container images and other executables, and a `bin` directory to contain softlinks:

```bash
$ mkdir -p software/bin/ software/exec
```

2. Create the image definition file (or pull from a repository, as appropriate) and build:

```bash
$ cd software/exec
$
$ cat bio-recipe.def
Bootstrap: docker
From: ubuntu:latest
%post
    apt-get update                       # update system
    apt-get install -y samtools bcftools # install software
    apt-get clean                        # clean up
```

```bash
$ sudo apptainer build bio-container.sif bio-recipe.def
```

3. Now, create the following wrapper script:
```bash
$ cat wrapper_bio-container.sh
#!/bin/bash
containerdir="$(dirname $(readlink -f ${BASH_SOURCE[0]}))"
cmd="$(basename $0)"
apptainer exec "${containerdir}/bio-container.sif" "$cmd" "$@"
$
$ chmod +x wrapper_bio-container.sh # make it executable
```

4. Create the softlinks:

```bash
$ cd ../bin
$ ln -s ../exec/wrapper_bio-container.sh  samtools
$ ln -s ../exec/wrapper_bio-container.sh  bcftools
```

5. Add the installation directory to your `$PATH` variable, and you will be able to call these tools 

```bash
$ export PATH=$PATH:$PWD
$
$ bcftools -v
INFO:    gocryptfs not found, will not be able to use gocryptfs
bcftools 1.13
Using htslib 1.13+ds
Copyright (C) 2021 Genome Research Ltd.
License Expat: The MIT/Expat license
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
$
$ samtools version                                  
INFO:    gocryptfs not found, will not be able to use gocryptfs                             
samtools 1.13                                                                               
Using htslib 1.13+ds                                                                        
Copyright (C) 2021 Genome Research Ltd.     
```

{{% alert title="Note" color="info" %}}
* At the end of the previous steps, you will get the following tree structure. Please be mindful of when and where commands were executed.
```bash
$ tree software/
software/
├── bin
│   ├── bcftools -> ../exec/wrapper.sh
│   └── samtools -> ../exec/wrapper.sh
└── exec
    ├── bio-container.sif
    └── wrapper.sh
```

* To permanently reflect changes to your `$PATH` variable, you may wish to add the step:
```bash
echo export PATH=$PATH:$PWD >> ~/.bash_profile
``` 
{{% /alert %}}
