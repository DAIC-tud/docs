---
title: "Job resource questions"
linkTitle: "Job resource questions"
weight: 3
---


### What are the limits?

* The [hard limits](/docs/manual/job-submission/qos) are in place only to protect the cluster from extreme overloads. The guiding principles of the cluster are fair-share and fair-use: all users should be able to use the cluster at the same time, and nobody should cause problems for the cluster or other users (see [Slurm's job scheduling and waiting times](/docs/manual/job-submission/priorities#slurms-job-scheduling-and-waiting-times)). So you need to make sure that your jobs do not unfairly hinder other jobs.


### What is the minimum runtime for a job?

* Submitting, scheduling and starting jobs bring along a certain overhead. To reduce the effects of the overhead, jobs need to run for at least 1 minute, but preferably 5 minutes to 1 hour. So limit the number of CPUs to at most 2 to 4 (to make the jobs easier to schedule and not finish _too quickly_) and where possible combine multiple jobs into one job (to reduce the number of jobs to at most 50 and add together the runtime of short jobs).


### How to determine the CPU load, memory use and number of active threads of your program?



* Log in on a login node (`login1` or `login3`) and run your program (`python …`).
* Log in a second time on the same login node and run `top -H -o TIME -u $USER` to see all your threads and their `%CPU` and `%MEM` use.
  - A `%CPU` of 100 corresponds to 1 CPU, 200 to 2 CPUs, and less than 75 is an indication that your program is not able to fully (optimally) use a CPU. 
  - `%MEM` is a percentage of 16 GB (`login1`) or 512 GB (`login3`); you’ll need to convert the `%MEM` to MB or GB for your job script (round up to the next GB for a little extra headroom). To determine the active threads of the program, count the threads (belonging to the program) with `%CPU` > 5 and steadily increasing `TIME+`.  (Quit top by pressing `q`.)
* For running jobs, the `CPU Load` statistics on the website is one indicator of problems (when the CPU load exceeds 100%).
* _Background:_ the system restricts a job so that it can only use the allocated CPU cores, and a CPU core can only run one thread at a time. So the actual CPU use cannot exceed the allocated number of CPU cores. When your program uses more active threads than the number of allocated CPU cores, only some threads can run, and the rest of the threads have to wait. So the CPU load, i.e. the number of active (running and waiting) threads per core, goes above 100%. Having threads waiting reduces the performance (and adds overhead).

**<span style="text-decoration:underline;">Example</span>**


Let’s assume you want to know the sum of 50 numbers. The simplest way to calculate this is to add the first two numbers, then add the third number to that, and so on. You will need to perform 49 additions, one at a time (one after the other), in one sequence, thus **1 thread**. To run this single thread, **a single CPU** is needed (to perform one addition at a time). The “time” needed to compute the sum is **49 CPU cycles** (1 addition per cycle). The **CPU load is 100%** (1 active thread per CPU) and the **CPU efficiency is 100%** (the one CPU will be active the whole time).


A simple way to speed this up would be to divide the 50 numbers in two groups of 25 numbers, and use **2 separate threads** to calculate the sums of the two groups at the same time (in parallel). Then add the sums of the two groups to get the total sum. Each thread needs its own CPU to perform the addition, so you need **2 CPUs** to be able to run the **2 threads** in parallel. Afterwards you will need to add the two sums together to get the total sum. So the time needed when using 2 threads is **25 cycles** (24 additions to sum each group, and 1 addition for the total). The average CPU load will be **98%** (1 active thread per CPU for 24 cycles, plus one final addition on only 1 CPU; the other CPU will be idle). The average CPU efficiency is also **98%** (49 additions in 50 available CPU cycles).


The **2 threads** could also have shared **1 CPU** (by first doing an addition in the first thread, temporarily storing that result, then doing an addition in the second thread, temporarily storing that result, and so on). However, because of the additional overhead, it would take _longer_ than by using _one_ thread. The average CPU load would be **_196%_** (24 additions with 2 active threads on 1 CPU, plus the final addition). The CPU efficiency would be **100%** (the one CPU will be active the whole time), but for a longer time. _In general, more than 1 active thread per CPU is less efficient._


You might have jumped to the conclusion that more threads would be even better, right? What happens when you divide the numbers in 8 groups (6 groups of 6 numbers and 2 groups of 7 numbers), and use **8 threads** (on **8 CPUs**) in parallel to sum those groups? The 6 threads that sum 6 numbers will be finished in **5** cycles, but the 2 threads that sum 7 numbers need **6** cycles. So those 6 CPUs will have to wait **idle** for one CPU cycle for the other **2 threads** to finish. Then you still have to add the sums of the 8 groups to get the total sum. If you use **1 thread** for this, you will need 7 CPU cycles. During this time, the other 7 CPUs will all be waiting **idle**!


The time needed would be **13 cycles** (_excluding any additional overhead_): 6 cycles to sum the groups and 7 cycles to calculate the total. The first 5 cycles 8 active threads run (on the 8 CPUs), the next cycle only 2 active threads remain and the final 7 cycles only 1 active thread runs. So the average CPU load is only **47%** (= (5 * (8 / 8) + (2 / 8) + 7 * (1 / 8)) / 13). In total 104 CPU cycles  (13 cycles * 8 CPUs) were available to perform the 49 additions, so the CPU efficiency is only **47%** (= 49 / 104). _In general, the more threads you use, the lower the average CPU efficiency!_


Conclusion: in this example, you can run **4** jobs with **2** threads each **_in less time_** than it takes to run **2** jobs with **8** threads each (especially considering that larger jobs often have longer waiting times). _So choose your number of threads optimally._



### How to determine the GPU use of your program?



* Log in on a login node with a GPU (`login1` or `login3`).
* Run `nvidia-smi -l`. Make sure no processes are using the GPU.
* Log in a second time _on the same login node_ and run your program (`python …`). 
* The current GPU utilization of your program is reported by `nvidia-smi` under `GPU-Util`.
* Quit your program and nvidia-smi by pressing `Ctrl+c`, and log out from the login node.


### How do I request CPUs for a multithreaded program?



* If you can specify the number of threads your program will use:
    * determine a “smart“ number of threads ( for example the number of currently available CPUs, or the number of threads needed to finish within 4 hours), **always a multiple of 2**, but **preferably no more than 8**,
    * request a cpu for each thread (`--cpus-per-task=<#threads>`), and
    * tell your program to use  the `$SLURM_CPUS_PER_TASK` variable for  threads.
        ```bash
        #/bin/sh
        #SBATCH --ntasks=1 --cpus-per-task=2
        srun ggsearch36 -t "$SLURM_CPUS_PER_TASK"
        ```

* If your program uses a fixed number (2, 4,..) of threads:
    * request a cpu for each thread (`#SBATCH --cpus-per-task=<#threads>`).
        ```bash
        #/bin/sh
        #SBATCH --ntasks=1 --cpus-per-task=2
        srun my_program
        ```
        
* If your program automatically uses as many threads as there are CPUs on a node (for example **java** programs):
    * do **not** use functions that detect the total number of CPUs of a computer (for example,  `os.cpu_count()` for Python), instead, use functions that detect the **CPU affinity** (for example, `len(os.sched_getaffinity(0))` for Python).
    * for some code you can explicitly specify the correct number of threads using an environment variable (`export <VARIABLE>=<value>`):
        ```bash
        #/bin/sh
        #SBATCH --ntasks=1 --cpus-per-task=2
        export NUMBA_NUM_THREADS="$SLURM_CPUS_PER_TASK"
        srun python script.py
        ```

    * If that is not possible, request a complete node for one task (`#SBATCH --ntasks=1 --exclusive`), and tell srun to use `"$SLURM_CPUS_ON_NODE"` threads.
    	
        ```bash
        #/bin/sh
        #SBATCH --ntasks=1 --exclusive
        srun --cpus-per-task="$SLURM_CPUS_ON_NODE" java_program
        ```

### How can I use a GPU?

* See [Jobs on GPU resources](/docs/manual/job-submission/job-gpu#jobs-on-gpu-resources)


### How can I let multiple programs use the same GPU?



* If you want to let multiple instances of your program share a GPU, you'll have to start them in parallel from the same job using `srun`.
    ```
    #!/bin/sh
    #SBATCH --gres=gpu:1
    #SBATCH --ntasks=2
    srun program
    ```


* If you want to use different programs, use the `--multi-prog` option:
    
    
    job.conf:
    ```bash
    0 <program 1>
    1 <program 2>
    ```
    
    job.sh:
    ```bash
    #!/bin/sh
    #SBATCH --gres=gpu
    #SBATCH --ntasks=2
    srun --multi-prog job.conf
    ```



### How much memory can I use?



* A task can run on a single node only. Since most jobs consist of a single task, those jobs are therefore limited to the total amount of memory in a node. However, since that would leave no memory for other jobs on the node, do not request more memory than your jobs need! (Also see [How can I see the CPU or RAM usage of a job?](#how-can-i-see-the-cpu-or-ram-usage-of-a-job)).
* There is also a per-user and per-QoS memory limit for the combined requested memory of all running jobs (of a user) in a certain QoS (see  [Quality of Service](/docs/manual/job-submission/qos#partitions-and-quality-of-service)). So, to run the most jobs at the same time, don’t request more memory than your jobs need.
* The average amount of memory that you can request when you want to run a lot of jobs is **less than 8Gb** per job (**less than 4Gb** per CPU). This will give you the most running jobs on the cluster.


### How can I see the CPU or RAM usage of a job?


* `sstat` shows specific usage information for (running) job _steps_ (i.e. when you start your program using <code>srun <em>program</em></code>), using something like this (all on one line):
    ```
    sstat --allsteps --format=JobID,NTasks,MinCPU,MaxRSS,MaxDiskRead,MaxDiskWrite <jobid>
    ```
    The `MaxRSS` field, for example, shows the maximum amount of memory used until now.
* `seff <jobid>` shows basic CPU and memory usage statistics of the whole job, including easy to understand percentages, but only for _finished_ jobs.


### How can I see the GPU usage of a job?



* See [Jobs on GPU resources](/docs/manual/job-submission/job-gpu#jobs-on-gpu-resources)


### How can I limit the number of jobs per node?



* When a job risks overloading a node (for example because it creates a large load on the network storage, or because it uses a lot of space in `/tmp`), you need to explicitly limit the number of jobs that can be run simultaneously on a node.
* One way to do this is to use the GRES (Generic consumable RESource) `jobspernode`. This allows you to limit the number of jobs per node to one, two, three or four. You do this by requesting **one** of the following GRES in your jobs (pick the one you need):
    ```bash
    #SBATCH --gres=jobspernode:one:1
    #SBATCH --gres=jobspernode:two:1
    #SBATCH --gres=jobspernode:three:1
    #SBATCH --gres=jobspernode:four:1
    ```
    When you specify one of these in your job, for example the one for four jobs per node, the scheduler will start (up to) four jobs on one node, and will then wait until a job finishes before starting another job on that node.



### Should I feel guilty about running a lot of jobs with GPU/CPU usage?



* Actually, the more jobs running and waiting in the queue, the more efficient and fair the scheduler can plan and divide the resources over the waiting jobs, so the higher the throughput and the sooner all work is finished. The scheduler will make sure that the available resources are divided fairly between the jobs of all users. This is done based on previous usage: the amount of allocated CPUs, GPUs and memory multiplied by a job’s real runtime. The higher a user’s previous usage, the lower the priority of that user’s jobs waiting in the queue. So when one user has a high previous usage, the waiting jobs of other users will be started before the jobs of that user. (The previous usage continuously decays, so when the usage stops, that user’s priority automatically goes back up again in a few days.)


### How do I clean up `/tmp` (when a job fails)



* When your job stores temporary data locally on a node, your job needs to clean up this data before it exits. So include an `rm` command at the end of your job script. (The system does not clean up this data automatically.)
* When the job fails (or is canceled or hits a timeout), the clean up requires some special code in the job script:
    ```bash
    #!/bin/sh
    #SBATCH ... # Your usual resources' specifications

    tmpdir="/tmp/${USER}/${SLURM_JOBID}" # Create local temporary folder
    mkdir --parents "$tmpdir"
    
    # You may want to uncomment this to know what to clean up when the clean up fails:
    #echo "Temporary folder: $(hostname --short):${tmpdir}"
    
    function clean_up { # Cleanup temporary folder
      rm --recursive --force "$tmpdir" && echo "Clean up of $tmpdir completed successfully."
      exit
    }
    trap 'clean_up' EXIT # Setup clean_up to run on exit

    # Your code- Make sure your program uses this "$tmpdir" location
    srun …
    ```
* If all else fails, login interactively to the node and manually clean up the files:
    ```bash
    sinteractive --nodelist=<node>
    ```


* Request a node with enough space in `/tmp` (at least twice what your script needs, because other jobs need to use `/tmp` too):

    ```bash
    #SBATCH --tmp=<size>G
    ```

