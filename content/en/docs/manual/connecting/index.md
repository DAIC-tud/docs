---
title: "Connecting to DAIC"
linkTitle: "Connecting to DAIC"
weight: 4
description: >
 How to connect to DAIC?
---

## SSH access

If you have a valid DAIC account (see [Access and accounts](/docs/policies#access-and-accounts)), you can access DAIC resources using an SSH client. SSH (Secure SHell) is a protocol that allows you to connect to a remote computer via a secure network connection. SSH  supports remote command-line login and remote command execution. SCP (Secure CoPy) and SFTP (Secure File Transfer Protocol) are file transfer protocols based on SSH (see {{< external-link "https://en.wikipedia.org/wiki/Secure_Shell" "wikipedia's ssh page">}}).

{{%alert title="SSH clients" color="info"%}}
Most modern operating systems like Linux, macOS, and Windows 10 include SSH, SCP, and SFTP clients (part of the OpenSSH package) by default. If not, you can install third-party programs like: {{< external-link "https://mobaxterm.mobatek.net/" MobaXterm>}} , {{< external-link "https://www.chiark.greenend.org.uk/~sgtatham/putty/" "PuTTY page" >}}, or {{< external-link "https://filezilla-project.org/" "FileZilla" >}}. 
{{%/alert%}}

{{< figure src="/img/DAIC_partitions.png" caption="Connecting to DAIC from inside and outside TU Delft network" ref="fig:daic_partitions" width="750px">}}

## Access from the TU Delft Network

To connect to DAIC _within TU Delft network_ (ie, via eduram or wired connection), open a command-line interface (prompt, or terminal, see {{< external-link "https://en.wikipedia.org/wiki/Command-line_interface" "Wikipedia's CLI page" >}}), and run the following command: 

```shell-session
$ ssh <YourNetID>@login.daic.tudelft.nl # Or
$ ssh login.daic.tudelft.nl             # If your username matches your NetID 
```

> `<YourNetID>` is your TU Delft NetID. If the username on your machine you are connecting from matches your NetID, you can omit the square brackets and their contents, `[<YourNetID>@]`.

This will log you in into DAIC's `login1.daic.tudelft.nl` node for now. Note that this setup might change in the future as the system undergoes migration, potentially reducing the number of login nodes..

{{% alert title="Note" color="info"  %}}
Currently DAIC has 3 login nodes: `login1.daic.tudelft.nl`, `login2.daic.tudelft.nl`, and `login3.daic.tudelft.nl`. You can connect to any of these nodes directly as per your needs.  For more on the choice of login nodes, see [DAIC login nodes](/docs/system/login-nodes/).
{{% /alert %}}



{{% alert title="Note" color="info" %}}
Upon first connection to an SSH server, you will be prompted to confirm the server’s identity, with a message similar to:
```bash
The authenticity of host 'login.daic.tudelft.nl (131.180.183.244)' can't be established.
ED25519 key fingerprint is SHA256:MURg8IQL8oG5o2KsUwx1nXXgCJmDwHbttCJ9ljC9bFM.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'login.daic.tudelft.nl' (ED25519) to the list of known hosts.
```
A distinct fingerprint will be shown for each login node, as below:
{{% /alert %}}

{{< tabpane  langEqualsHeader=true >}}
{{% tab header="**Fingerprints of login nodes**:" disabled=true right=false /%}}

{{< tab header="`login1`" >}}
SHA256:MURg8IQL8oG5o2KsUwx1nXXgCJmDwHbttCJ9ljC9bFM
{{< /tab >}}

{{< tab header="`login2`" >}}
SHA256:MURg8IQL8oG5o2KsUwx1nXXgCJmDwHbttCJ9ljC9bFM
{{< /tab >}}

{{< tab header="`login3`" >}}
SHA256:O3AjQQjCfcrwJQ4Ix4dyGaUoYiIv/U+isMT5+sfeA5Q
{{< /tab >}}

{{< /tabpane >}}

{{% alert title="" color="info" %}}
If you notice any discrepancy in the key fingerprint, do not proceed unless notified of legitimate changes.
{{% /alert %}}


Once identity confirmed, enter your password when prompted (nothing will be printed as you type your password):

```shell-session
The HPC cluster is restricted to authorized users only.
YourNetID@login.daic.tudelft.nl's password:
```

Next, a welcome message will be shown:

```shell-session
Last login: Mon Jul 24 18:36:23 2023 from tud262823.ws.tudelft.net
 #########################################################################
 #                                                                       #
 # Welcome to login1, login server of the HPC cluster.                   #
 #                                                                       #
 # By using this cluster you agree to the terms and conditions.          #
 #                                                                       #
 # For information about using the HPC cluster, see:                     #
 # https://login.hpc.tudelft.nl/                                         #
 #                                                                       #
 # The bulk, group and project shares are available under /tudelft.net/, #
 # your windows home share is available under /winhome/$USER/.           #
 #                                                                       #
 #########################################################################
 18:40:16 up 51 days,  6:53,  9 users,  load average: 0,82, 0,36, 0,53
```
 And, now you can now verify your environment with basic commands:

```bash
YourNetID@login1:~$ hostname  # show the current hostname
login1.hpc.tudelft.nl
YourNetID@login1:~$ echo $HOME  # show the path to your home directory
/home/nfs/YourNetID
YourNetID@login1:~$ pwd  # show current path
/home/nfs/YourNetID
YourNetID@login1:~$ exit  # exit current connection
logout
Connection to login.daic.tudelft.nl closed.
```
In this example, the user, `YourNetID`, is logged in via the login node `login1.hpc.tudelft.nl` as can be seen from the `hostname` output.  The user has landed in the `$HOME` directory, as can be seen by printing its value, and checked by the `pwd` command. Finally, the `exit` command is used to exit the cluster.


{{% alert title="Graphical applications" color="warning" %}}

We discourage running graphical applications (via `ssh -X`) on DAIC login nodes, as GUI applications are not supported on the HPC systems.

{{% /alert %}}

## Access from outside university network using a VPN
Direct access to DAIC from _outside the university network_ is blocked by a firewall. Therefore, a VPN is needed

You need to use TU Delft's EduVPN or OpenVPN (See TU Delft's {{< external-link "https://www.tudelft.nl/en/library/using-the-library/facilities-study-places/off-campus-access/access-via-vpn" "Access via VPN " >}} recommendations ) to access DAIC directly. Once connected to the VPN,  you can ssh to DAIC directly, as in [Access from the TU Delft Network](#access-from-the-tu-delft-network). 


{{% alert title="VPN access trouble?" color="warning" %}}
If you are having trouble accessing DAIC via the VPN, please report an issue via [this Self-Service link](https://tudelft.topdesk.net/tas/public/ssp/content/serviceflow?unid=5880a7704835440589808f22666f3579). 
{{%/alert%}}

{{% alert title="Using the Linux Bastion Server" color="info" %}}

As of January 16th 2025, access to TU Delft bastion hosts is only possible via a VPN. Therefore, it is now recommended to activate a TU Delft VPN and directly connect to DAIC (instead of jumping via the bastion host).

{{% /alert %}}


## Simplifying SSH with Configuration Files

To simplify SSH connections, you can store configurations in a file  _in your local machine_. The SSH configuration file can be created (or found, if already exists) in `~/.ssh/config` on Linux/Mac systems, or in `C:\Users\<YourUserName>\.ssh` on Windows.

For example, on a Linux system, you can have the following lines in the configuration file:

{{< card code=true header="**`~/.ssh/config`**" lang="bash" >}}
Host daic
  HostName login.daic.tudelft.nl # Or any other login node
  User <YourNetID>

{{< /card >}}


where:
> * The `Host` keyword starts the SSH configuration block and specifies the name (or pattern of names, like `daic` in this example) to which the configuration entries will apply. 
> * The `HostName` is the actual hostname to log into. Numeric IP addresses are also permitted (both on the command line and in HostName specifications).
> * The `User` is the login username. This is especially important when the username differs between your machine and the remote server/cluster.


You can then connect to DAIC from inside TU Delft network (or behind TU Delft VPN) by just typing the following command:

```shell-session
$ ssh daic
```







## Efficient SSH Connections with SSH Multiplexing

SSH multiplexing allows you to reuse an existing connection for multiple SSH sessions, reducing the time spent entering your password for every new connection. After the first connection is established, subsequent connections will be much faster since the existing control connection is reused.

To enable SSH multiplexing, add the following lines to your SSH configuration file. Assuming a Linux/Mac system, you can add the following lines to `~/.ssh/config`:

{{< card code=true header="**`~/.ssh/config`**" lang="bash" >}}
Host *
  ControlMaster auto
  ControlPath /tmp/ssh-%r@%h:%p
{{< /card >}}

where:
> * The `ControlPath` specifies where to store the “control socket” for the multiplexed connections. `%r` refers to the remote login name, `%h` refers to the target host name, and `%p` refers to the destination port. This ensures that SSH separates control sockets for different connections.
> * The `ControlMaster` setting activates multiplexing. With the `auto` setting, SSH will use an existing master connection if available or create a new one when necessary. This configuration helps streamline SSH connections and reduces the need to enter your password for each new session.

This setup will speed up connections after the first one and reduce the need to repeatedly enter your password for each new SSH session.

{{% alert title="Note" color="info" %}}
On Windows you may need to adjust the `ControlPath` to match a valid path for your operating system. For example, instead of `/tmp/`, you might use a path like `C:/Users/<YourUserName>/AppData/Local/Temp/`.
{{% /alert %}}


{{% alert title="Important" color="warning"%}}
SSH public key logins (passwordless login) **are not supported** on DAIC, because [Kerberos authentication](../job-submission/kerberos#kerberos-authentication) is required to access your home directory. You will need to enter your password for each session
{{% /alert %}}


