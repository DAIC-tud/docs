---
title: "Container images"
weight: 1
---

## Containerization Technology

_Containerization_ is a convenient means to deploy libraries and applications to different environments in a reproducible manner. A _container image_, typically a `*.sif` file, is a self-contained file with all necessary components to run an application, including code, runtime libraries, and dependencies. 

DAIC supports [Apptainer (previously Singularity)](https://apptainer.org/docs/user/main/introduction.html), an open-source container platform, designed to run complex applications on HPC clusters. Apptainer makes it possible to use docker images natively  at a higher level of security and isolation. (see [Pulling images](#pulling-images))


Generally, to launch a container image, your commands look as follows:

```bash
$ apptainer shell <container> # OR
$ apptainer exec  <container> <command>
$ apptainer run   <container>
```

where: 
* `<container>` is the path to a container image, typically, a `*.sif` file
* `<command>` is the command you like to run from inside the container, eg, `hostname`
*  Both `shell` and `exec` can be used to launch container images. The difference is that `shell` allows you to work inside the container image interactively; while `exec` executes the `<command>` inside the image and exits. Of course, by using something like `/bin/bash` as the `<command>`, `exec` behaves exactly like `shell`. 
* `run` also launches a container image, but runs the default action defined in the container image. See an example use case in [Building images ](/tutorials/singularity/#building-images)


The question is now: where to get the `<container>` file from? You can either: 
1) use a pre-built image by pulling from a repository (see [Pulling images](#pulling-images)), or, 
2) build your own container image and use it accordingly (see [Building images](#building-images)). 
The following sections give examples to both options.

<!-- 
Add workflow for how to work with containers:
- pull image
- dependent
- building
-->

{{% alert title="Note" color="info" %}}
If you intend to extensively work/test your image interactively, it is best to first submit an interactive SLURM job with the needed resources, eg, memory, gpus, ... etc:
```bash
$ hostname  # To check this is DAIC. login[1-3] are the login nodes
login1.hpc.tudelft.nl 
$ sinteractive # Default resources: --time=01:00:00 --cpus-per-task = 2 --mem=1024 
Note: interactive sessions are automatically terminated when they reach their time limit (1 hour)!
srun: job 8543393 queued and waiting for resources
srun: job 8543393 has been allocated resources
 13:35:30 up 5 days,  3:41,  0 users,  load average: 8,79, 7,60, 7,11
$ hostname # To check we are on a compute node
grs3.hpc.tudelft.nl 
```
{{% /alert %}} 



## Pulling images

Many repositories exist where container images are hosted. Apptainer allows pulling and using images from repositories like [DockerHub](https://hub.docker.com/), [BioContainers](https://biocontainers.pro/registry) and [NVIDIA GPU Cloud (NGC)](https://ngc.nvidia.com/catalog/containers). 

### Pulling from DockerHub

For example, to obtain the latest Ubuntu image from DockerHub:


```bash
$ hostname # check this is DAIC
login1.hpc.tudelft.nl
$ cd && mkdir containers && cd containers # as convenience, use this directory
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

```bash
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

$ ls /.singularity.d/ # container-specific directory should not be found on host
ls: cannot access /.singularity.d/: No such file or directory

$ apptainer shell ubuntu_latest.sif # launch container interactively
Apptainer>
Apptainer> hostname
login1.hpc.tudelft.nl
Apptainer> ls
ubuntu_latest.sif
Apptainer> ls /.singularity.d/ 
Singularity  actions  env  labels.json  libs  runscript  startscript
Apptainer> exit
```

In the above snippet, note:
* The command prompt changes within the container to `Apptainer>`
* The container seamlessly interacts with the host system. For example, it inherits its `hostname` (the DAIC login node in this case). The container also inherits the `$HOME` variable, and is able to edit/delete files from there.
* The container has its own file system, which is distinct from the host. The presence of a directory like `/.singularity.d` is another feature of the specific to the container.

{{% alert title="Warning" color="warning"%}}
To isolate files in your system (ie, your local machine or DAIC) from the files inside the container (and thus, avoid possible erroneous deletes/edits), it is recommended to add a `-c` or `-C` flags to your apptainer commands
```bash
$ apptainer shell -C ubuntu_latest.sif
```
{{% /alert %}}

### Pulling from NVIDIA GPU cloud (NGC)

This is a specialized registry provided by NVIDIA for GPU accelerated applications or GPU software development tools. These images are large, and one is recommended to download them locally, and only send the downloaded image to DAIC. For this, Apptainer needs to be installed on your machine first.

{{% alert title="Tip" color="info" %}}
- To install Apptainer in your machine, follow the official [Installing Apptainer instructions](https://apptainer.org/docs/admin/main/installation.html). If you are a Mac user, you can use [Lima](https://github.com/lima-vm/lima) to install both a Linux virtual machine and Apptainer.
{{% /alert %}}


{{% alert title="Warning" color="warning" %}}
 By default, Apptainer images are saved to `~/.singularity`. Ideally, to avoid quota issues, you'd set the environment variable `SINGULARITY_CACHEDIR` to a different location. At present, both the `bulk` and `umbrella` filesystems do not support pulling images, so you are advised to pull these to your local machine and then copy over the image file to DAIC.
{{% /alert %}} 

```bash
$ hostname #check this is your own PC/laptop
$ apptainer pull docker://nvcr.io/nvidia/pytorch:23.05-py3
$ scp pytorch_23.05-py3.sif  hpc-login:/tudelft.net/staff-umbrella/...<YourDirectory>/apptainer
```

Now, to check this particular image on DAIC:

```bash
$ hostname # check this is DAIC not your own PC/laptop
login1.hpc.tudelft.nl
$ cd /tudelft.net/staff-umbrella/...<YourDirectory>/apptainer # path where you put images
$ apptainer shell -C --nv pytorch_23.05-py3.sif  #--nv to use NVIDIA GPU and have CUDA support
Apptainer>
Apptainer> hostname
login1.hpc.tudelft.nl # hostname inherited
Apptainer> ls /.singularity.d/ # verify this is the image
Singularity  actions  env  labels.json  libs  runscript  startscript
```

## Building images

If you prefer (or need) to have a custom container image, then you can build your own container image from a _recipe_ file, typically `*.def` file, that sets up the image with your custom dependencies. __The only requirement for building is to be in a machine (eg, your local laptop/pc) where you have sudo/root privileges. In other words, you can **not** build images on DAIC directly: First, you must build the image locally, and then send it to DAIC to run there.__

{{% alert title="Reminder" color="info" %}}
Always build the image first in your local machine. To send the built image, `YourImage.sif` to DAIC, do the following:
```bash
$ hostname # check this is your machine
$ scp YourImage.sif <YourNetID>@login.hpc.tudelft.nl:/tudelft.net/staff-umbrella/../<YourDirectory>/apptainer # send the image to DAIC
```
{{% /alert %}}

{{% alert title="Tip" color="info" %}}
- To install Apptainer in your machine, follow the official [Installing Apptainer instructions](https://apptainer.org/docs/admin/main/installation.html). If you are a Mac user, you can use [Lima](https://github.com/lima-vm/lima) to install both a  Linux virtual machine and Apptainer.
{{% /alert %}}

An example _recipe_ file, `cuda_based_recipe.def`, for a cuda-enabled container may look as follows:

```bash
$ cat cuda_based_recipe.def
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
```

where:
* The _header_, the first 2 lines of this example, specify the source of a base image, (eg, `Bootstrap: docker`), and the base image (`From: nvidia/cuda:12.1.1-devel-ubuntu22.04`) 
 to be pulled from this source. The container image will be built on top of this base image. In this example, the base image will be built from Ubuntu 22.04 OS with the CUDA toolkit 12.1 pre-installed. 
* The rest of the file are optional _data blobs_ or _sections_. In this example, the following blobs are used:
  * `%post` blob: the steps to download, configure and install needed custom software and libraries on the base image. In this example, the steps install git, clone a repo, and install a package via `make`
  * `%runscript` blob: the scripts or commands to execute when the container image is run. That is, this code is the entry point to the container with the `run` command. In this example, the `deviceQuery` is executed once the container is run.
  * Other blobs may be present in the `def` file. See [Definition files documentation](https://apptainer.org/docs/user/main/definition_files.html#definition-files) for more details and examples.



And now, build this image and send it over to DAIC:

```bash
$ hostname #check this is your machine
$ sudo apptainer build cuda_based_image.sif cuda_based_recipe.def # building may take ~ 2-5 min, depending on your internet
INFO:    Starting build...
Getting image source signatures
Copying blob d5d706ce7b29 [=>------------------------------------] 29.2MiB / 702.5MiB
...
INFO:    Adding runscript
INFO:    Creating SIF file...
INFO:    Build complete: cuda_based_image.sif  
$
$ scp cuda_based_image.sif  hpc-login:/tudelft.net/staff-umbrella/...<YourDirectory>/apptainer # send to DAIC
```

On DAIC, check the image:

```bash
$ hostname # check you are on DAIC
login1.hpc.tudelft.nl 
$ sinteractive --cpus-per-task=2 --mem=1024 --gres=gpu --time=00:05:00
$ hostname # check you are on a compute node
insy13.hpc.tudelft.nl

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

{{% alert title="Warning" color="warning"%}}
Always pass `--nv` to apptainer to run GPU-accelerated applications or libraries inside the container. Note that you also need **1)** your host system must have NVIDIA GPU drivers installed and compatible with the version of Singularity you are using, and **2)** the container you are running should have the necessary dependencies and configurations to support GPU acceleration.

```bash
$ apptainer shell --nv -C cuda_based_image.sif
```
{{% /alert %}}


{{% alert title="Note" color="info"%}}
Building container images from a recipe file is recommended to ensure the reproducibility of the resulting container image. However, there can be cases of complex dependencies where it is not clear upfront how the software installations and dependencies should be set up. In such cases, it is possible to interactively develop the image by building it in `writable sandbox` mode first. In such cases, take note of all installation commands used in the sandbox, so you can include them in a recipe file. See [Apptainer Sandbox Directories](https://apptainer.org/docs/user/main/quick_start.html#sandbox-directories) for more details.
{{% /alert %}}



### Building from local image file


During software development, it is common to incrementally build code and go through many iterations of debugging and testing. A development container may be used in this process. 
In such scenarios, re-building the container from the base image with each debugging or testing iteration becomes taxing very quickly, due to dependencies and installations involved. 
Instead, the `Bootstrap: localimage` and `From:<path/to/local/image>` header can be used to base the development container on some local image.


As an example, assume it is desirable to develop some code on the basis of the `cuda_based_recipe.sif` image created in the [Building images](#building-images) section.  Building from the original `cuda_based_recipe.def` file can take ~ 4 minutes. 
However, if the `*.sif` file is already available, building on top of it, via a `dev_on_cuda_based_recipe.def` file as below, takes ~ 2 minutes. This is already a time saving  factor of 2 in this case.

```bash
$ hostname # check this is your machine
$ cat dev_on_cuda_based_recipe.def # def file for an image based on localimage
# Header
Bootstrap: localimage
From: cuda_based_recipe.sif

# (Optional) Sections/ data blobs
%runscript
    echo "Arguments received: $*"
    exec echo "$@"

$
$ sudo apptainer build dev_image.sif # build the image
INFO:    Starting build...
INFO:    Verifying bootstrap image cuda_based_recipe.sif
WARNING: integrity: signature not found for object group 1
WARNING: Bootstrap image could not be verified, but build will continue.
INFO:    Adding runscript
INFO:    Creating SIF file...
INFO:    Build complete: dev_image.sif
$
$ apptainer run  dev_image.sif "hello world" # check runscript of the new def file is executed
INFO:    gocryptfs not found, will not be able to use gocryptfs
Arguments received: hello world
hello world
$
$ apptainer shell  dev_image.sif # further look inside the image
Apptainer> 
Apptainer> ls /cuda-samples/Samples/1_Utilities/deviceQuery/deviceQuery # commands installed in the original image are available
/cuda-samples/Samples/1_Utilities/deviceQuery/deviceQuery

Apptainer>
Apptainer> cat /.singularity.d/bootstrap_history/Apptainer0 # The original def file is also preserved 
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


### Deploying conda in a container 

There might be situations where you have a certain conda environment in your local machine that you need to set up in DAIC to commence your analysis. In such cases, deploying your conda environment in a container and sending this container to DAIC does the job for you. 

As an example, let's create a simple demo environment, `demo-env` in our local machine, 

```bash
$ hostname # check this is your machine
$ conda create -n demo-env python=3.10 # create an environment containing python3.8
$ conda activate demo-env
$ conda install numpy # install some conda libraries
$ pip install matplotlib # install some pip libraries
$ conda env export --from-history > demo-env.yml # flag added to avoid unnecessary dependencies
$ # You may manually remove the Prefix line from this file
$ cat demo-env.yml # check the environment file
name: demo-env
channels:
  - defaults
dependencies:
  - python=3.10
  - numpy
$ # Notice pip-installed libraries are not included in this file
```

Now, it is time to create the container image. One option is to base the image on `condaforge/mambaforge`, which is a minimal Ubuntu installation with `conda` preinstalled at `/opt/conda`:


```bash
$ cat demo-env-recipe.def
Bootstrap: docker
From: condaforge/mambaforge

%files
    demo-env.yml /opt

%post
    conda env create -f /opt/demo-env.yml # create environment from  yml file
    conda clean -afy # remove unused packages and caches
    exec /opt/conda/envs/demo-env/bin/pip install matplotlib # install PyPI libraries
```

This file is similar to the file in the [Building images](/tutorials/singularity/#building-images), with the addition of `%files` area. `%files` specifies the files in the host system (ie, your machine) that need to be copied to the container image, and optionally, where should they be available. In the previous example, the `demo-env.yml` file will be available in `/opt/` in the container.

Now, time to build and check the image:

```bash
$ sudo apptainer build demo-env-image.sif demo-env-recipe.def
INFO:    Starting build...
Getting image source signatures
...
INFO:    Creating SIF file...       
INFO:    Build complete: demo-env-image.sif
$
$ apptainer shell -C demo-env-image.sif 
Apptainer> 
Apptainer> source activate /opt/conda/envs/demo-env/ # activate the environment
(demo-env) Apptainer> python                         # run python and check imports
Python 3.10.11 (main, May 16 2023, 00:28:57) [GCC 11.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import numpy
>>> import matplotlib
>>> exit()
Apptainer> exit
$ scp demo-env-image.sif hpc-login:/tudelft.net/staff-umbrella/...<YourDirectory>/apptainer
```

Now, to use the environment in this image to run code in a file, `analysis.py`, which uses some data to generate a plot:

```bash
$ cat analysis.py # check python code
#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

plt.plot(x, y)
plt.title('Sine Wave')
plt.savefig('sine_wave.png')
$ 
$ apptainer exec demo-env-image.sif /bin/bash -c "source activate /opt/conda/envs/demo-env && python analysis.py"
$ ls # check the image file was created
sine_wave.png
```

{{% alert title="Warning" color="warning" %}}
In the last example, the container read and wrote a file to the host system directly. This behavior is risky. You are strongly recommended to expose only the desired host directories to the container. See [Exposing host directories](daicdocumentation/tutorials/singularity/#exposing-host-directories)
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

<!-- 

## Containers and VScode

- (bonus) attach vscode (or other ide) and apptainer
- how to connect via vscode

See this link https://stackoverflow.com/questions/63604427/launching-a-singularity-container-remotely-using-visual-studio-code
-->
