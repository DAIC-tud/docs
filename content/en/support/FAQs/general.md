---
title: "General problems"
linkTitle: "General problems"
weight: 1

---


### SSH: “<code>The authenticity of host 'login<em>X</em>' can't be established.</code>”

* When connecting to a login node for the first time, you must **not continue** when the key fingerprint reported by your ssh connection does **not match** one of the fingerprints shown here:
    * `login1.hpc.tudelft.nl` and `login2.hpc.tudelft.nl`
        * `2iPjH/j/Tf5JZU4OJyLpASA/GZ40eCqvcQnSSa++3nQ (ECDSA)`
        * `MURg8IQL8oG5o2KsUwx1nXXgCJmDwHbttCJ9ljC9bFM (ED25519)`
        * `mKgxUQvmOVM74XvFNhWt0ODsRvfnmwIgZWcw8uPJ68o (RSA)`
        * `05:24:a0:b4:83:27:05:32:4b:83:78:2a:20:99:f8:5c (ECDSA)`
        * `C5:21:46:cb:73:cd:72:e6:18:04:d6:67:2a:67:90:75 (ED25519)`
        * `05:17:84:7f:9f:18:e3:71:b4:df:5e:c0:12:db:e8:fc (RSA)`
    * `login3.hpc.tudelft.nl`
        * `IaBwyYiZi1Etj7yBDtdv7sByHzH+hedW69QA8UxGUqk (ECDSA)`
        * `O3AjQQjCfcrwJQ4Ix4dyGaUoYiIv/U+isMT5+sfeA5Q (ED25519)`
        * `fslv0RnC9zkVBf34i3g1BPKaYBcsTgKqu8+PMKLTEvw (RSA)`
        * `5e:9a:69:30:75:d3:b5:75:29:b3:32:fc:48:ab:b2:f9 (ECDSA)`
        * `31:eb:cd:95:8f:d1:78:29:e1:70:f9:8b:b0:cd:56:5c (ED25519)`
        * `ba:b9:92:4b:1a:00:8c:f1:aa:49:09:53:fa:b6:79:5f (RSA)`
* When the key fingerprint matches, you can safely continue.
* When in the future your ssh connection tells you that the key has changed, and it doesn’t match one of the fingerprints above, contact the [HPC support team](../_index.md#support--contact).


### SSH: “`Permission denied, please try again.`”

* The DAIC cluster is not freely accessible. It is facilitated by several departments and groups within the university for their research/education.
* If you have access, either your access expired (in case an end date was set), or your account was (temporarily) disabled due to problems with your use of the login nodes, or there is a problem with your NetID account/password.


### “`-bash: cd: /home/nfs/<NetID>: Key has expired`”

* Your Kerberos ticket has expired. Your need to renew it, either by running ‘`kinit`’, or by logging out then logging in again (using your password!).
* Log out when you’re not using the cluster (so you don’t hit this problem, and so you don’t block resources on the login node).


### “Disk quota exceeded”



* The size of the data in this storage has reached the maximum allowed size (also known as quota limit). For home folders the maximum allowed amount of data is 8 GB, for project storage the quota limit can be up to 5TB of data.
* To see how much space your files are using, run ‘`du -h ~ | sort -h`’. (When you have many files or folders, this can take a long time!)
* To make space available, you'll either need to clean up some files (like installation archives and caches), or move some of your files somewhere else. Note: your home folder is for storing settings and installing small software packages, not for storing data or large software installations. You need to store those in project storage. Your project leader/supervisor can request project storage for you via the [Self Service Portal (TOPdesk)](https://tudelft.topdesk.net/tas/public/ssp/).

### “The system load on login_X_ is too high! Please use another node if you can.”



    * This message is mainly a warning for the person that is causing the high load. If that is you, you should either do the work as a cluster job, or limit the number of threads or memory that you use. If you're not the one, you can choose to ignore it.


### staff-umbrella: “`Operation not permitted`”



    * The network filesystem for the bulk, groups and project storage (staff-bulk, staff-groups, staff-umbrella) does not support `chmod` (changing permissions) or `chown` (changing owner or group) operations. When you run these operations, you will receive an “Operation not permitted” error. This has nothing to do with your personal rights, it’s just not supported.
    * However, it's not necessary to change these, since the _default permissions are correct_ _for normal use_. So you can **safely** skip these operations or **ignore** these errors.
    * For `rsync`, use ‘`rsync -a --no-perms`’.
    * When the error causes problems, a workaround is to (temporarily!) use the `/tmp` folder: move your folder that gives the error to `/tmp`, create a symbolic link from the folder in /tmp to the original location, rerun the commands that gave the error as before, then move your folder back from `/tmp` to the original location. For example, when you get an error in folder <code><em><foldername></em></code>, do:

        ```
        mkdir /tmp/${USER}
        mv <foldername> /tmp/${USER}/<foldername>
        ln -s /tmp/${USER}/<foldername> <foldername>
        <rerun command(s) that gave the error>
        rm <foldername>
        mv /tmp/${USER}/<foldername> <foldername>
        rmdir /tmp/${USER}

        ```



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