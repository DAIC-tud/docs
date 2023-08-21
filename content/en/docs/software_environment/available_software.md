---
title: "Available software and libraries"
linkTitle: "Available software and libraries"
weight: 1
description: >
  How to find and work with pre-installed software?
---


## General software

Most common general software, like programming languages and libraries, is installed on the DAIC servers. 

To check if the program that you need is pre-installed, you can simply try to start it:

```bash
$ python
Python 2.7.5 (default, Jun 28 2022, 15:30:04) 
[GCC 4.8.5 20150623 (Red Hat 4.8.5-44)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> 
>>> quit()
$ 
$ python4
-bash: python4: command not found 
```

 Alternatively, you can try to locate the program or library using the `whereis` command:

 ```bash
 $ whereis python
python: /usr/bin/python3.4m-config /usr/bin/python3.6m-x86_64-config /usr/bin/python2.7 /usr/bin/python3.6-config /usr/bin/python3.4m-x86_64-config /usr/bin/python3.6m-config /usr/bin/python3.4 /usr/bin/python3.4m /usr/bin/python2.7-config /usr/bin/python3.6 /usr/bin/python3.4-config /usr/bin/python /usr/bin/python3.6m /usr/lib/python2.7 /usr/lib/python3.4 /usr/lib/python3.6 /usr/lib64/python2.7 /usr/lib64/python3.4 /usr/lib64/python3.6 /etc/python /usr/include/python2.7 /usr/include/python3.4m /usr/include/python3.6m /usr/share/man/man1/python.1.gz
$ 
$ whereis python4
python4:$ 
```

 Or, you can check if the package is installed using the `rpm -qa` command as follows: 

 ```bash
 $ rpm -qa python
python-2.7.5-92.el7_9.x86_64
$ 
$ rpm -qa python4
$
```
 


<!--
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

-->



## Environment modules

Some often used third-party software (eg, CUDA, cuDNN, Matlab) is installed in the cluster as {{< external-link "https://modules.readthedocs.io/en/latest/index.html" "environment modules" >}}. 


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
   :
   : # Output omitted for brevity
```

And to check the description of a specific module:

```bash
$ $ module whatis cudnn
cudnn/12-8.9.1.23   : cuDNN 8.9.1.23 for CUDA 12
cudnn/12-8.9.1.23   : NVIDIA CUDA Deep Neural Network library (cuDNN) is a GPU-accelerated library of primitives for deep neural networks.

```

And to use the module or package, load it as follows:

```bash
$ module load cuda/11.2 cudnn/11.2-8.1.1.33 # load the module
$
$ module list                               # check the loaded modules

Currently Loaded Modules:
   1) cuda/11.2   2) cudnn/11.2-8.1.1.33

```


{{< alert title="Note" color="info" >}}
For more information about using the module system, run `module help`. 

{{< /alert >}}