---
title: "Software questions"
linkTitle: "Software questions"
weight: 2
---

### My program requires a newer version of CMake
 Use `cmake3`.

### How can I run a Docker container?
Using `apptainer`. See the [Apptainer tutorial](/tutorials/apptainer) for more information.

### My program requires a newer version of GCC
Newer versions of GCC are available through the {{< external-link "https://developers.redhat.com/products/developertoolset/overview" "devtoolset" >}} modules. See the [Modules](/docs/manual/software/modules#environment-modules) for information on using modules.

### I want to use R
There are a few options:
* You can use the pre-installed R
* You can {{< external-link "https://docs.anaconda.com/anaconda/user-guide/tasks/using-r-language/#creating-a-new-environment-with-r" "install R using Conda" >}}. Conda is available via the `miniconda` module.
* You can {{< external-link "https://rviews.rstudio.com/2017/03/29/r-and-singularity/" "use R from a container" >}}. Containers can be run using `Apptainer` on DAIC, as explained in this [Apptainer tutorial](/tutorials/apptainer). 

### How to use TensorBoard on the DAIC cluster?
* TensorBoard is very insecure: anybody can connect to it, without authentication (i.e. when you run TensorBoard on the DAIC cluster, any TU Delft user can connect to it). And this is actually {{< external-link "https://github.com/tensorflow/tensorboard/issues/267"  "on purpose">}}, because making it secure and being able to guarantee that would require too much effort. **So you can't run TensorBoard directly on the DAIC cluster!**
* The most secure way to run TensorBoard is to run it on your personal computer (with a proper firewall). When you put your TensorFlow log files on a network folder, you can access them directly on your personal computer so you can use TensorBoard in the same way as you do in the DAIC cluster. (You can also download the log files if you find that easier.)

### My Snakemake rules seem to be working properly, but it's telling me that it can't set marker

- This comes with an error `Failed to set marker file for job started ([Errno 1] Operation not permitted. Please ensure write permissions for the directory {self.workflow.persistence.path}`. This makes it so that it's only able to run a single rule before it can't keep track of the metadata anymore. 
- The known solution is to edit the source code. In Snakemake's `jobs.py` file, you can search the error message and simply change `raise WorkflowError` to `logger.warning`

### python & conda segmentation fault error

**Issue:** Sometimes, running python within a conda environment causes an unexplainable `segmentation fault` in the prompt,
while submitting job scripts seem to work fine.

**Solution:** pin down `libgcc-ng` dependencies explicitly in the environment, eg, 
`conda create --prefix <your umbrella or bulk path> python=3.10 libgcc-ng=9.3.0`

