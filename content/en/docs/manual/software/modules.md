---
title: "Modules"
weight: 2
description: >
  How to find and work with pre-installed software?
---

In the context of Unix-like operating systems, the `module` command is part of the environment modules system, a tool that provides a dynamic approach to managing the user environment. This system allows users to load and unload different software packages or environments on demand. Some often used third-party software (e.g., CUDA, cuDNN, MATLAB) is pre-installed on the cluster as {{< external-link "https://modules.readthedocs.io/en/latest/index.html" "environment modules" >}}. 

### Usage
To see or use the available modules, first, enable the software collection:

```bash
$ module use /opt/insy/modulefiles
```

Now, to see all available packages and versions:

```bash
$ module avail
---------------------------------------------------------------------------------------------- /opt/insy/modulefiles ----------------------------------------------------------------------------------------------
   albacore/2.2.7-Python-3.4        cuda/11.8                 cudnn/11.5-8.3.0.98        devtoolset/6    devtoolset/10        intel/oneapi  (D)    matlab/R2021b (D)    miniconda/3.9             (D)
   comsol/5.5                       cuda/12.0                 cudnn/12-8.9.1.23   (D)    devtoolset/7    devtoolset/11 (D)    intel/2017u4         miniconda/2.7        nccl/11.5-2.11.4
   comsol/5.6                (D)    cuda/12.1          (D)    cwp-su/43R8                devtoolset/8    diplib/3.2           matlab/R2020a        miniconda/3.7        openmpi/4.0.1
   cuda/11.5                        cudnn/11-8.6.0.163        cwp-su/44R1         (D)    devtoolset/9    :
   ...
```

- **D** is a label for the default module in case multiple versions are available. E.g. `module load cuda` will load `cuda/12.1`
- **L** means a module is currently loaded

To check the description of a specific module:

```bash
$ module whatis cudnn
cudnn/12-8.9.1.23   : cuDNN 8.9.1.23 for CUDA 12
cudnn/12-8.9.1.23   : NVIDIA CUDA Deep Neural Network library (cuDNN) is a GPU-accelerated library of primitives for deep neural networks.
```

And to use the module or package, load it as follows:

```bash
$ module load cuda/11.2 cudnn/11.2-8.1.1.33 # load the module

$ module list                               # check the loaded modules

Currently Loaded Modules:
   1) cuda/11.2   2) cudnn/11.2-8.1.1.33

```

{{< alert title="Note" color="info" >}}
For more information about using the module system, run `module help`. 
{{< /alert >}}

### Compilers and Development Tools

The cluster provides several compilers and development tools. The following table lists the available compilers and development tools. These are available in the `devtoolset` module:

```shell-session
$ module use /opt/insy/modulefiles
$ module avail devtoolset

---------------------------------------------------------------------------------------------- /opt/insy/modulefiles ----------------------------------------------------------------------------------------------
   devtoolset/6    devtoolset/7    devtoolset/8    devtoolset/9    devtoolset/10    devtoolset/11 (L,D)

  Where:
   L:  Module is loaded
   D:  Default Module

If the avail list is too long consider trying:

"module --default avail" or "ml -d av" to just list the default modules.
"module overview" or "ml ov" to display the number of modules for each name.

Use "module spider" to find all possible modules and extensions.
Use "module keyword key1 key2 ..." to search for all possible modules matching any of the "keys".

$ module whatis devtoolset
devtoolset/11       : Developer Toolset 11 Software Collection
devtoolset/11       : GNU Compiler Collection, GNU Debugger, and other development, debugging, and performance monitoring tools.

$ module load devtoolset/11
$ gcc --version
gcc (GCC) 11.2.1 20220127 (Red Hat 11.2.1-9)
Copyright (C) 2021 Free Software Foundation, Inc.
This is free software; see the source for copying conditions.  There is NO
warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

```