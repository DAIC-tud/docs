---
title: "Software Environment"
linkTitle: "Software Environment"
weight: 7
description: >
  How to set up your tools and/or run certain libraries
---

{{% pageinfo %}}
At present [DAIC](https://daic.pages.ewi.tudelft.nl/docs/) and [DelftBlue](https://doc.dhpc.tudelft.nl/delftblue) have different software stacks. This pertains to the operating system (CentOS 7 _vs_ Red Hat Enterprise Linux 8, respectively) and, consequently, the available software. Please refer to the respective [DelftBlue modules](https://doc.dhpc.tudelft.nl/delftblue/DHPC-modules/) and [DAIC available software](#available-software-and-libraries-loading-and-using-software-modules) documentation before commencing your experiments.
{{% /pageinfo %}}


## Operating System

DAIC runs the {{< external-link "https://en.wikipedia.org/wiki/CentOS" "CentOS" >}} 7 Linux distribution, which provides the general Linux software. Most common software, including programming languages, libraries and development files for compiling your own software, is installed on the servers. However, a not-so-common program that you need might not be installed. Similarly, if your research requires a state-of-the-art program that is not (yet) available as a package for {{< external-link "https://en.wikipedia.org/wiki/CentOS" "CentOS" >}} 7, then it is not available. See [Unavailable/Uninstalled software](#unavailableuninstalled-software) for more information on installing software in the cluster. 

## Job Scheduling Software (Slurm)

DAIC uses the {{< external-link "https://slurm.schedmd.com/" "Slurm scheduler" >}} to efficiently manage workloads. All jobs for the cluster have to be submitted as batch jobs into a queue. The scheduler then manages and prioritizes the jobs in the queue, allocates resources (CPUs, memory) for the jobs, executes the jobs and enforces the resource allocations. See [the scheduler pages](../job_submissions/_index.md) for more information.

<!-- 
## Loading and Using Software Modules


## Libraries for Specialized Hardware or Accelerators 

## Unavailable/Uninstalled software
-->

## Available software and libraries

### General software

To check if the program that you need is installed, you can simply try to start it:

```bash
$ python
Python 2.7.5 (default, Nov 16 2020, 22:23:17) 
[GCC 4.8.5 20150623 (Red Hat 4.8.5-44)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> quit()
$ python4
-bash: python4: command not found
```
 Alternatively, you can try to locate the program or library, or check if the package is installed: 

 ```bash
 $ whereis python
python: /usr/bin/python3.6 /usr/bin/python3.6m-x86_64-config /usr/bin/python /usr/bin/python3.6-config /usr/bin/python2.7-config /usr/bin/python2.7 /usr/bin/python3.6m-config /usr/bin/python3.6m /usr/lib/python3.6 /usr/lib/python2.7 /usr/lib64/python3.6 /usr/lib64/python2.7 /etc/python /usr/local/lib/python3.6 /usr/include/python2.7 /usr/include/python3.6m /usr/share/man/man1/python.1.gz
$ rpm -q python
python-2.7.5-34.el7.x86_64
$ whereis python4
python4:
$ rpm -q python4
package python4 is not installed
```

When a program is not installed you should check if a package containing the program is available: 

```bash
$ yum search python3
================= N/S matched: python3 ==================
python3.x86_64 : Version 3 of the Python programming language aka Python 3000
$ yum search python4
Warning: No matches found for: python4
No matches found
```

When a package is available you can simply request it's installation by sending an e-mail to the HPC cluster administrators. 

### Modules

Some often used third-party is installed in the cluster as modules. To see what modules are available and load them, use the module command: 

```bash
$ module use /opt/insy/modulefiles
$ module avail
---------------------------- /opt/insy/modulefiles -----------------------------
   cuda/11.0       cudnn/11.0-8.0.3.33       devtoolset/6       devtoolset/9 (D)
   cuda/11.1       cudnn/11.1-8.0.5.39       devtoolset/7       matlab/R2020a
   cuda/11.2 (D)   cudnn/11.2-8.1.1.33 (D)   devtoolset/8       matlab/R2020b (D)

  Where:
   D:  Default Module

$ module whatis cudnn
cudnn/11.2-8.1.1.33 : cuDNN 8.1.1.33 for CUDA 11.2
cudnn/11.2-8.1.1.33 : NVIDIA CUDA Deep Neural Network library (cuDNN) is a GPU-accelerated library of primitives for deep neural networks.

$ module load cuda/11.2 cudnn/11.2-8.1.1.33
$ module list

Currently Loaded Modules:
   1) cuda/11.2   2) cudnn/11.2-8.1.1.33

$ module load matlab/R2020b
$ matlab

                              < M A T L A B (R) >
                    Copyright 1984-2020 The MathWorks, Inc.
                    R2020b (9.9.0.1495850) 64-bit (glnxa64)
                              September 30, 2020
```

For more information about using the module system, run module help. 

### Environment modules

Third-party software (CUDA, cuDNN, Matlab) is available through the module system; to use them, enable the HPC software collection:


```bash
$ module use /opt/insy/modulefiles
```

To see all available packages and versions:

```bash
$ module avail
---------------------- /opt/insy/modulefiles -----------------------
  cuda/11.0    cudnn/11.0-8.0.3.33    devtoolset/8    matlab/R2020a
  cuda/11.2    cudnn/11.2-8.1.1.33    devtoolset/10   matlab/R2020b
  ...
$ module whatis cudnn
cudnn/11.2-8.1.1.33 : cuDNN 8.1.1.33 for CUDA 11.2
cudnn/11.2-8.1.1.33 : NVIDIA CUDA Deep Neural Network library (cuDNN) is a GPU-accelerated library of primitives for deep neural networks.
```

To use a package, load it:


```bash
$ module load cuda/11.2 cudnn/11.2-8.1.1.33
$ module list
Currently Loaded Modules:
   1) cuda/11.2   2) cudnn/11.2-8.1.1.33
```

## Installing software

### Basic principles

- On a cluster, it's important that software is available and identical on all nodes, both login and compute. For self-installed software, it's easier to install the software in one shared location than installing and maintaining the same software separately on every single node. You should therefore install your software on one of the network shares (eg, your `$HOME` folder or an `umbrella` or `bulk` folder) that are accessible from all nodes (see [File system overview](../filesystem/_index.md#file-system-overview)).


- As a regular Linux user you don't have administrator rights. Yet, you can do your normal work, including installing software _in a personal folder_, without needing administrator rights. Consequently, you don't need (nor are you allowed) to use the `sudo` or `su` commands that are often shown in manuals. 

{{% alert title="Stop!" color="warning" %}}

Although both Linux flavors _Red Hat Enterprise Linux_ (RHEL, CentOS, Scientific Linux, Fedora) and _Debian_ (Ubuntu) can run the same Linux software, they use completely different package systems for installing software. 
The available software, packages names and package versions might differ, and the package formats and package management tools are incompatible. This means:
- It is not possible to install Ubuntu or Debian `.deb` packages in CentOS or use `apt-get` to install software. So when installing software, use a manual for CentOS, Red Hat or Fedora. 
- If you can only find a manual for Ubuntu, you have to substitute the CentOS versions for any Ubuntu-specific packages or commands. 
{{% /alert %}}



### Installing binaries when possible

Some programs come as precompiled binaries or are written in a scripting language such as Perl, PHP, Python or shell script. Most of these programs don't actually need to be "installed" since you can simply run these programs directly (you may need to make the program executable first): 

```bash
$ ./program
-bash: ./program: Permission denied
$ chmod +x program
$ ./program
Hello world!
```

### Installing from source

When a package for your software is not available, you'll have to install the software yourself from the source. This is not too difficult following the recipe below. 

#### Installation environment

When you are installing software for the very first time, you need to set up your environment. If you have already done this before , you can skip this and go directly to the installation instructions below.

To set up your environment, run:

```bash
$ curl -s https://wiki.tudelft.nl/pub/Research/InsyCluster/InstallingSoftware/bash_profile.txt >> ~/.bash_profile
$ source ~/.bash_profile
$ mkdir -p "$PREFIX"
```

This appends the following lines [( download)](bash_profile.txt) to your ~/.bash_profile: 

```bash
# .bash_profile

# Get the aliases and functions
if [ -f ~/.bashrc ]; then
   . ~/.bashrc
fi

# User specific environment and startup programs

export PREFIX="$HOME/.local"
export ACLOCAL_PATH="$PREFIX/share/aclocal${ACLOCAL_PATH:+:$ACLOCAL_PATH}"
export CPATH="$PREFIX/include${CPATH:+:$CPATH}"
export LD_LIBRARY_PATH="$PREFIX/lib64:$PREFIX/lib${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
export LIBRARY_PATH="$PREFIX/lib64:$PREFIX/lib${LIBRARY_PATH:+:$LIBRARY_PATH}"
export MANPATH="$PREFIX/share/man${MANPATH:+:$MANPATH}"
export PATH="$HOME/bin:$PREFIX/bin:$PATH"
export PERL5LIB="$PREFIX/lib64/perl5:$PREFIX/share/perl5${PERL5LIB:+:$PERL5LIB}"
export PKG_CONFIG_PATH="$PREFIX/lib64/pkgconfig:$PREFIX/share/pkgconfig${PKG_CONFIG_PATH:+:$PKG_CONFIG_PATH}"
export PYTHONPATH="$PREFIX/lib/python2.7/site-packages${PYTHONPATH:+:$PYTHONPATH}"
```

{{< alert title="Note!" color="info"  >}}
1.  if you already have some of these settings in your `~/.bash_profile` (or elsewhere), you should combine them so they don't duplicate the paths. 
2.  if you want to use `python3.6` instead of `python2.7`, you need to set the `PYTHONPATH` to `python3.6`. 
{{< /alert >}}


The line `export PREFIX="$HOME/.local"` sets your software installation directory to `/home/nfs/netid/.local` (which is the default and accessible on all nodes). This is in your personal home directory where you have a space quota of 8GB. However, for software for your research project, you should instead use a project share, for example: 

```bash
export PREFIX="/tudelft.net/staff-umbrella/project/software"
```

The other variables will let you use your self-installed programs. You are now ready to install your software! 


#### Installation recipe

Software installation _usually_ just requires you to follow the general installation recipe described below, but you always need to consult the documentation for your software.

1. Place the source of the software in a folder under `/tmp`:

```bash
$ mkdir /tmp/$USER
$ cd /tmp/$USER
$ wget http://host/path/software.tar.gz
$ tar -xzf software.tar.gz
          Or from github: git clone https://github.com/software
$ cd software
```

{{< alert title="Note" color="info" >}}

Note: `.tgz` is the same as `.tar.gz`, for `.tar.bz2` files use tar `-xjf software.tar.bz2`. 

{{< /alert >}}

1. If the software provides a `configure` script, run it:

```bash
$ ./configure --prefix="$PREFIX" 
```

If `configure` complains about missing software, you'll either have to install that software, tell `configure` where it is (`--with-feature _path_=`) or disable the feature (`--disable-feature`).

If your software provides a `CMakeLists.txt` file, run `cmake` (note: the trailing two dots on the last line are needed exactly as shown):

```bash
$ mkdir -p build $ cd build $ cmake -DCMAKE_INSTALL_PREFIX="$PREFIX" .. 
```

Again, if `cmake` complains about missing software, you'll either have to install that software or tell `cmake` where it is (`-DCMAKE_SYSTEM_PREFIX_PATH="/usr/local;/usr;$PREFIX;path"`).

If neither is provided, consult the documentation for dependencies and configuration (specifically for the installation directory).

There is no point in continuing until all reported problems have been fixed.

2. Compile the software:

```bash
$ make 
```

If compilation is aborted due to an error, {{< external-link "https://www.google.com/" "Google" >}} the error for possible solutions. Again, there is no point in continuing until all reported problems have been fixed.



3. Install the software. When you used configure or cmake, you can simply run:

```bash
$ make install 
```


When you used neither, you need to use:
```bash
$ make prefix="$PREFIX" install 
```

4. Your software should now be ready to use, so check it:

```bash
$ cd $ _program_ 
```


5. When the program works, clean up `/tmp/netid`:

```bash
$ rm -r /tmp/$USER 
```

#### Python modules

After setting up the installation environment (above) you are also able to install Python modules by yourself, by using the `--user` option. The easiest way is when the module is available through `pip2` (for Python 2) or `pip3` (for Python 3):

```bash
$ pip2 search module
$ pip2 install --user module
```


When you only have the source code for the module, follow the installation instructions for the module, but make sure to use --user in the installation step:

```bash
$ python setup.py install --user
```

<!--
### Virtualization: conda, virtualenv, mamba, 

### Containerization: docker, udocker, singularity, Apptainer

## Software Licensing and Restrictions

## Examples and Tutorials demonstrating the usage of specific software or libraries (eg, AI frameworks like TensorFlow or PyTorrch, R scripts, .. etc) on different computing resources 

-->

