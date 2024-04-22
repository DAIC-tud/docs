---
title: "General questions"
linkTitle: "General questions"
weight: 1
---


### SSH: <code>The authenticity of host 'login<em>X</em>' can't be established.</code>

When connecting to a login node for the first time, you must **not continue** when the key fingerprint reported by your ssh connection does **not match** one of the fingerprints shown here:
  * For `login1.hpc.tudelft.nl` and `login2.hpc.tudelft.nl`:
      * `2iPjH/j/Tf5JZU4OJyLpASA/GZ40eCqvcQnSSa++3nQ (ECDSA)`
      * `MURg8IQL8oG5o2KsUwx1nXXgCJmDwHbttCJ9ljC9bFM (ED25519)`
      * `mKgxUQvmOVM74XvFNhWt0ODsRvfnmwIgZWcw8uPJ68o (RSA)`
      * `05:24:a0:b4:83:27:05:32:4b:83:78:2a:20:99:f8:5c (ECDSA)`
      * `C5:21:46:cb:73:cd:72:e6:18:04:d6:67:2a:67:90:75 (ED25519)`
      * `05:17:84:7f:9f:18:e3:71:b4:df:5e:c0:12:db:e8:fc (RSA)`
  * For `login3.hpc.tudelft.nl`:
      * `IaBwyYiZi1Etj7yBDtdv7sByHzH+hedW69QA8UxGUqk (ECDSA)`
      * `O3AjQQjCfcrwJQ4Ix4dyGaUoYiIv/U+isMT5+sfeA5Q (ED25519)`
      * `fslv0RnC9zkVBf34i3g1BPKaYBcsTgKqu8+PMKLTEvw (RSA)`
      * `5e:9a:69:30:75:d3:b5:75:29:b3:32:fc:48:ab:b2:f9 (ECDSA)`
      * `31:eb:cd:95:8f:d1:78:29:e1:70:f9:8b:b0:cd:56:5c (ED25519)`
      * `ba:b9:92:4b:1a:00:8c:f1:aa:49:09:53:fa:b6:79:5f (RSA)`
When the key fingerprint matches, you can safely continue.
When in the future your ssh connection tells you that the key has changed, and it doesn’t match one of the fingerprints above, contact the [DAIC support team](../../#support--contact).


### SSH: `Permission denied, please try again.`

* The DAIC cluster is not freely accessible. It is facilitated by several departments and groups within the university for their research/education.
* If you have access, this message indicates that either your access expired (in case an end date was set), or your account was (temporarily) disabled due to problems with your use of the login nodes, or there is a problem with your NetID account/password.


### `-bash: cd: /home/nfs/<NetID>: Key has expired`

* This means your Kerberos ticket has expired. Your need to renew it, either by running `kinit`, or by logging out then logging in again (using your password!). Also see [Kerberos authentication](/docs/manual/job-submission/kerberos).
* Please log out when you’re not using the cluster (so you don’t hit this problem, and so you don’t block resources on the login node).


### `Disk quota exceeded`

* The size of the data in this storage has reached the maximum allowed size (also known as _quota limit_). For `$HOME` folders (see [Personal storage](/docs/introduction/system/storage#personal-storage-aka-home-folder)) the maximum allowed amount of data is 8 GB, for project storage (see [Project storage](/docs/introduction/system/storage#project-storage)) the quota limit can be up to 5TB of data.
* To see how much space your `$HOME` files are using, run `du -h ~ | sort -h`. (When you have many files or folders, this can take a long time!)
* To make space available, you'll either need to clean up some files (like installation archives and caches), or move some of your files somewhere else. 

{{% alert title="Note" color="info" %}}

Your home folder is for storing settings and installing small software packages, not for storing data or large software installations. You need to store those in project storage. Your project leader/supervisor can request project storage for you via the [Self Service Portal (TOPdesk)](https://tudelft.topdesk.net/tas/public/ssp/).

{{% /alert %}}

### `The system load on login_X_ is too high! Please use another node if you can.`


* This message is mainly a warning for the person that is causing the high load. If that is you, you should either do the work as a cluster job, or limit the number of threads or memory that you use. If you're not the one running heavy tasks, you can choose to ignore it.


### staff-umbrella: `Operation not permitted`


* The network filesystem for the bulk, groups and project storage (staff-bulk, staff-groups, staff-umbrella) does not support `chmod` (changing permissions) or `chown` (changing owner or group) operations:
  - When you run these operations, you will receive an `Operation not permitted` error. This has nothing to do with your personal rights, it’s just not supported.
  - It's also not necessary to change these, since the _default permissions are correct for normal use_. So, you can **safely** skip these operations or **ignore** these errors in many situations.
* For `rsync` operations , use `rsync -a --no-perms`.
* If all else fails, a workaround is to (temporarily!) use the `/tmp` folder: move your folder that gives the error to `/tmp`, create a symbolic link from the folder in `/tmp` to the original location, rerun the commands that gave the error as before, then move your folder back from `/tmp` to the original location. For example, when you get an error in folder `<foldername>`, do:
    ```
    mkdir /tmp/${USER}
    mv <foldername> /tmp/${USER}/<foldername>
    ln -s /tmp/${USER}/<foldername> <foldername>
    :
    : #<rerun command(s) that gave the error>
    :
    rm <foldername>
    mv /tmp/${USER}/<foldername> <foldername>
    rmdir /tmp/${USER}
    ```
