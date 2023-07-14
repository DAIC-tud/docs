---
title: "Software Environment"
linkTitle: "Software Environment"
weight: 7
description: >
  How to set up your tools and/or run certain libraries
---

{{% pageinfo %}}
1. This will be split into multiple pages. Perhaps the title changed too!
2. Warn that this info only applies to HPC; and DHPC has a different software stack
{{% /pageinfo %}}

* Available Software and Libraries/ Loading and Using Software Modules
* Unavailable/Uninstalled software:
    * Installing binaries when possible
    * Compiling and Running Code
    * Virtualization: conda, virtualenv, mamba, 
    * Containerization: docker, udocker, singularity, Apptainer
* Software Licensing and Restrictions
* Examples and Tutorials demonstrating the usage of specific software or libraries (eg, AI frameworks like TensorFlow or PyTorrch, R scripts, .. etc) on different computing resources 



## Environment modules

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
