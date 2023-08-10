---
title: "Software questions"
linkTitle: "Software questions"
weight: 2

---

{{% pageinfo %}}
A compilation of FAQs is available in this [word doc](https://docs.google.com/document/d/14-jokK4MLbnJk44QaAtIH2LnxrVBooA6u3ZqI6nrPpw/edit)
{{% /pageinfo %}}



<!-- Output copied to clipboard! -->

<!-- Yay, no errors, warnings, or alerts! -->


# HPC Cluster Tips and Tricks


## Software


### My program requires a newer version of CMake



    * Use ‘`cmake3`’.


### How can I run a Docker container?



    * Using ‘`singularity`’. See the [SURFsara Singularity documentation](https://userinfo.surfsara.nl/systems/shared/software/Singularity) for information on using containers.


### My program requires a newer version of GCC



    * Newer versions of GCC are available through the [devtoolset](https://developers.redhat.com/products/developertoolset/overview) modules. See the [slides](https://docs.google.com/presentation/d/10A0_0eNRBYd87E1h1YN6bsIFaZaua5qJkfBbnBKAr6o/present#slide=id.g47bc0fe738_0_0) for information on using modules.


### I want to use R



    * You can [install R using Conda](https://docs.anaconda.com/anaconda/user-guide/tasks/using-r-language/#creating-a-new-environment-with-r). Conda is available via the ‘`miniconda`’ module.
    * You can [use R from a container](https://rviews.rstudio.com/2017/03/29/r-and-singularity/). Containers can be run using ‘`singularity`’.


### How to use TensorBoard on the HPC cluster?



    * TensorBoard is very insecure: anybody can connect to it, without authentication (i.e. when you run TensorBoard on the HPC cluster, any TU Delft user can connect to it). And this is actually [on purpose](https://github.com/tensorflow/tensorboard/issues/267), because making it secure and being able to guarantee that would require too much effort. **So you can’t run TensorBoard directly on the HPC cluster!**
    * The most secure way to run TensorBoard is to run it on your personal computer (with a proper firewall). When you put your TensorFlow log files on a network folder, you can access them directly on your personal computer so you can use TensorBoard in the same way as you do in the HPC cluster. (You can also download the log files if you find that easier.)


## Scheduler problems


### Interactive sessions hang when left for some time without input



    * This seems to be a bug. For now, use `sattach` or one of the login nodes.
    * Of course, if a session is really idle (i.e. nothing running), just close it so another job can run.


### Job pending with reason “`QOSGrpCpuLimit`”



    * Each QoS (Quality of Service) sets limits on the total number of CPUs in use for that QoS. If the total number of CPUs in use by running jobs (of the whole group of users combined) in a QoS hits the set limit, no new jobs in that QoS can be started, and jobs will stay pending with reason “QOSGrpCpuLimit”. This is not an error; when running jobs finish, the highest priority pending job will be started automatically.


### Job pending with reason “ReqNodeNotAvail”



    * Sometimes nodes are not available to start new jobs (for example when they are reserved for maintenance). When jobs can only run on those nodes, they will remain pending with the reason “ReqNodeNotAvail” until the node become available again.
    * The requested runtime of a job is an important factor here. When a reservation starts in 1 day, a job with a requested runtime of 7 days will not be able to start (since it would not be finished before the start of the reservation), but a job with a requested runtime of 4 hours can still be run normally. So when possible reduce the requested runtime.
    * The requested resources (number of CPUs, amount of memory, number or type of GPUs or specific constraints) limit the number of nodes that are suitable to run a job. So when possible reduce the requested resources and constraints, and do not request specific GPU types.


### Why does my job run on some nodes but fail on other nodes?



    * The nodes have different configurations (processor types, number of cores, memory size, GPU support, and so on). If you need a specific feature, make sure to request it in your sbatch script. Examples:

        ```
        #SBATCH --constraint=avx
        #SBATCH --constraint=avx2
        #SBATCH --gres=gpu
        ```


    * If your program uses specific processor instruction extensions (AVX/SSE/AES/…), it will crash (with an ‘Illegal instruction’ error) on processors that do not support those extensions. Either compile your program to use only standard instructions (be generic), or request nodes that have support. The login node login3 has the least advanced CPUs so if you compile your programs there they should run on all other nodes.


### Why does my job fail and is there no slurm-XXXXX.out output (or error)?



    * When your job doesn't have a valid Kerberos ticket it can't read or write files (such as the `slurm-XXXXX.out` output).

        It's best to do a fresh login to a login node when you want to submit a new job. This way you're sure your job's Kerberos ticket is valid and will remain valid for the next 7 days. If needed, you can update the Kerberos ticket for a running job by executing ‘`auks -a`’ (also from a fresh login).



### “sbatch: error: Batch job submission failed: Access/permission denied”



    * You can only submit jobs (using `sbatch`) from the login nodes (`login1, login2, login3`). When you try to submit a job from within another job (including an interactive job) you will receive this error.
    * To submit multiple jobs from a script, create a file with the submit commands:

        ```
        sbatch job1.sh
        sbatch job2.sh
        sbatch job3.sh
        …
        ```



        Then login to one of the login nodes and source the file:


        ```
        source script

        ```



### “sbatch: error: Batch job submission failed: Invalid account or account/partition combination specified”



    * Either you’re trying to use a (special) partition that you don’t have access to.
    * Or your account has been (temporarily) disabled because of problems with your jobs. The usual problems are (a combination of) of these:
        1. Your jobs are not using all of the requested resources (CPUs, GPUs, memory, runtime).
        2. Your jobs try to use more resources than requested (more active threads than the requested number of CPUs, out of memory failures, timeout failures).
        3. Too many jobs are failing or being cancelled.
        4. Failing to follow the [cluster workflow](https://docs.google.com/presentation/d/10A0_0eNRBYd87E1h1YN6bsIFaZaua5qJkfBbnBKAr6o/present#slide=id.g598656af69_0_0) as described on page 5 of the slides.

        You need to figure out the problem(s), fix them, and then send an email to the [cluster administrators](mailto:beheer-o-linux-ictfm@tudelft.nl?subject=HPC%20cluster%20job%20submission%20suspended&body=Hi,%0A%0AMy%20job%20submission%20was%20suspended%20because%20of%20the%20following%20problem:%0A<fill%20in%20your%20problem>%0A%0AI%20fixed%20the%20problem%20by%20doing%20this:%0A<fill%20in%20your%20solution%20and%20the%20way%20you%20tested%20this>%0A%0ACan%20you%20please%20re-enable%20my%20account%3F%0A%0AKind regards,%0A%0A) to explain the problem(s) and the way you fixed them.



### “srun: error: Unable to allocate resources: Invalid qos specification”



    * You can’t directly execute a jobscript, you need to submit the jobscript using `sbatch`:

        ```
        sbatch jobscript.sh

        ```



### “slurmstepd: error: Exceeded step memory limit at some point.”



    * Your program wants to use more memory than you requested. You’ll either need to limit the memory use of your program or request more memory. (Also see “How much memory can I use?” and “How can I see the CPU or RAM usage of a job?”)


### “Auks API request failed : auks cred : credential lifetime is too short” / "Auks API request failed : krb5 cred : unable to renew credential"



    * Your authentication (Kerberos ticket) expired. You get a Kerberos ticket (using your password) when you log in to the bastion server or login node. Jobs that run on a compute node also require authentication. Therefore, when you submit a job, your Kerberos ticket is stored in the Auks system so that your job can use it. However, the maximum lifetime of a Kerberos ticket is 7 days. So 7 days after you last logged in and submitted a job, the Kerberos ticket in the system expires and the job fails.
    * Therefore, for infinite jobs or long jobs that have had to wait in the queue for a couple of days, the Kerberos ticket needs to be renewed before it expires. The simple way to do this is to log in to a cluster login node and run ‘`auks -a`’.
    * When you frequently need to do this, you can (on a cluster login node) run ‘`install_keytab`’ to install an encrypted version of your password (called Kerberos keytab) for automatic Kerberos ticket renewal. _Important:_ when you change your NetID password, your Kerberos keytab becomes invalid, so you will need to rerun this command.


### What can be done about some jobs using all CPUs or memory (making it impossible for me to use other unused resources like GPUs)?



    * Resources can be used by one job at a time only, so when some resources are completely used, other jobs will have to wait until their required resources become available. The waiting is unavoidable.
    * See the answer to “Should I feel guilty about running a lot of jobs with GPU/CPU usage?” (The scheduler is already dividing the available resources fairly over all jobs based on the policies, using priorities based on previous usage. As soon as a running job finishes and it’s resources become available again, the highest priority waiting job is automatically started.)
    * The policies for the scheduler are set by the cluster users (in the cluster board meeting). To change the policies, all users must agree that the changes are necessary and fair to all users. (So the cluster administrators aren’t able to change the policies on request!)
    * You can always contact a user (nicely!😉) about the possibility to (for example) exclude a certain node. That user can decide for him-/herself if he/she wants to cooperate or not (for example in case of deadlines).

        It’s usually possible to determine a person’s initial (or first name) and last name from his/her username; if not, run: `finger <username>`

    * If you experience a real problem because of this (not being able to efficiently develop code because of the waiting, or not going to make an upcoming deadline), you should contact the cluster administrators to see if they can provide support for that specific problem.
    * It’s not desirable to reserve resources for certain types of jobs only. Since other types of jobs wouldn’t be able to use those resources even when they would be idle, this would reduce the overall cluster throughput (and recreate the exact same problem that you experience for those other jobs).
    * No type of research can make special claims regarding resources. All research that uses the cluster is equally dependent on the cluster resources: 50+ CPU jobs or jobs requiring 50GB memory can’t be run on a laptop any more than a GPU job requiring 5GB of GPU memory. When one type of resource is completely used, that is because it is required to do the same kind of research that you need the cluster for.