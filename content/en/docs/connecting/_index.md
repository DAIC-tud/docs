---
title: "Connecting to DAIC"
linkTitle: "Connecting to DAIC"
weight: 4
description: >
 How to connect to DAIC?
---

## SSH access

If you have a valid DAIC account (see [Access and Accounts page](../intro_daic/access_accounts)), you can access DAIC resources using an SSH client. SSH (Secure SHell) is a protocol that allows you to connect to a remote computer via a secure network connection. SSH  supports remote command-line login and remote command execution. SCP (Secure CoPy) and SFTP (Secure File Transfer Protocol) are file transfer protocols based on SSH (see {{< external-link "https://en.wikipedia.org/wiki/Secure_Shell" "wikipedia's ssh page">}}).



### Command line access

Most modern operating systems, including Linux, macOS and Windows 10, come by default with SSH, SCP and SFTP clients from OpenSSH pre-installed (but you can also use a third-party SSH or SFTP program). To connect to DAIC _within TU Delft network_ (ie, via eduram or wired connection), open a command-line interface (prompt, or terminal, see {{< external-link "https://en.wikipedia.org/wiki/Command-line_interface" "Wikipedia's CLI page" >}}), and run the following command: 

```bash
$ ssh [<YourNetID>@]login.daic.tudelft.nl
```
This command logs you in into one of the three login nodes of DAIC (`login[1-3]`), 
where `<YourNetID>` is your TU Delft's NetID. You can optionally omit the square brackets and their contents if the username on the machine you are connecting from matches your NetID.


{{% alert title="Note" color="info" %}}
 The first time that you connect to an SSH server, you will be asked to confirm the server's identity. This identity will be used in future sessions to detect (evil) server changes. If the SSH client later on detects a change, do not connect, unless you have been informed that the identity was changed legitimately. 

```bash
The authenticity of host 'login.daic.tudelft.nl (131.180.183.244)' can't be established.
ED25519 key fingerprint is SHA256:MURg8IQL8oG5o2KsUwx1nXXgCJmDwHbttCJ9ljC9bFM.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'login.daic.tudelft.nl' (ED25519) to the list of known hosts.
```
{{% /alert %}}

The server then asks you for your password, so enter it to proceed to the welcome screen. Note that the password you print will not appear:

```bash
The HPC cluster is restricted to authorized users only.

YourNetID@login.daic.tudelft.nl's password: 
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
YourNetID@login1:~$ hostname
login1.hpc.tudelft.nl
YourNetID@login1:~$
YourNetID@login1:~$
YourNetID@login1:~$ echo $HOME
/home/nfs/YourNetID
YourNetID@login1:~$
YourNetID@login1:~$ pwd
/home/nfs/YourNetID
YourNetID@login1:~$ 
YourNetID@login1:~$ 
YourNetID@login1:~$ exit
logout
Connection to login.daic.tudelft.nl closed.
```
In this example, the user, `YourNetID`, is logged in via the login node `login1.hpc.tudelft.nl` as can be seen from the `hostname` output.  The user has landed in the `$HOME` directory, as can be seen by printing its value, and checked by the `pwd` command. Finally, the `exit` command is used to exit the cluster.


Alternatively, if you like to run graphical applications on DAIC, you need to enable X11 forwarding via the `-X` option as follows:

```bash
$ ssh -X [<YourNetID>@]linux-bastion.tudelft.nl
```




## Access from outside university network 
Direct access to DAIC from _outside the university network_ is blocked by a firewall. Thus, to access DAIC, there are two options. You can either:
1. Use TU Delft's EduVPN or other recommended VPN. Once connected to a VPN, you can ssh to DAIC directly, as in [SSH access](#ssh-access). See TU Delft {{< external-link "https://www.tudelft.nl/en/library/using-the-library/facilities-study-places/off-campus-access/access-via-vpn" "Access via VPN" >}} page, or
2. Connect via Linux bastion server. In this case, first, you connect (using an SSH or SCP/SFTP client) to the bastion server, and then ssh into DAIC, as depicted in Fig 1. 

{{< figure src="connecting_to_hpc.png" caption="Connecting to DAIC from outside TU Delft network"  >}}

For the linux bastion, if you are an employee or guest, use `linux-bastion.tudelft.nl`. If you are a student (BSc or MSc), then use `student-linux.tudelft.nl` as per the following examples:

```bash
$ hostname # check this is your local machine
$ ssh YourNetID@linux-bastion.tudelft.nl
The authenticity of host 'linux-bastion.tudelft.nl (131.180.123.195)' can't be established.
ED25519 key fingerprint is SHA256:VJUFsQkIebODETsXwczkInnRrpdYYqAZDbsoKP1we+A.
This key is not known by any other names                                                                     
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes 
Warning: Permanently added 'linux-bastion.tudelft.nl' (ED25519) to the list of known hosts.
YourNetID@linux-bastion.tudelft.nl's password:                                                                
                ____  ____ _____                                         
 ___ _ ____   _|___ \|___ \___  |                                                                            
/ __| '__\ \ / / __) | __) | / /                                                                             
\__ \ |   \ V / / __/ / __/ / /                                                                              
|___/_|    \_/ |_____|_____/_/                                                                               
                                                                         
YourNetID@srv227:~$
YourNetID@srv227:~$ hostname # check you are on the bastion server
srv227.tudelft.net                      
YourNetID@srv227:~$                                                      
YourNetID@srv227:~$ ssh login.daic 
The authenticity of host 'login.daic (131.180.183.244)' can't be established.
ECDSA key fingerprint is SHA256:2iPjH/j/Tf5JZU4OJyLpASA/GZ40eCqvcQnSSa++3nQ.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added 'login.daic' (ECDSA) to the list of known hosts.
                           
The HPC cluster is restricted to authorized users only.

YourNetID@login.daic's password: 
Last login: Tue Jul 25 01:32:08 2023 from srv227.tudelft.net
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
 01:28:15 up 51 days, 13:41,  1 user,  load average: 0,10, 0,13, 0,14
YourNetID@login1:~$ 
YourNetID@login1:~$ 
YourNetID@login1:~$ hostname
login1.hpc.tudelft.nl
YourNetID@login1:~$ 
YourNetID@login1:~$ 
```




## Making OpenSSH more user-friendly 

### Configuration files

For convenience, you can place certain information about your SSH connections to a configuration file _in your local machine_. The SSH configuration file can be found in `~/.ssh/config` on Linux systems, and in `C:\Users\<YourUserName>\.ssh` on Windows.

For example, on a Linux system, you can place the following lines in the configuration file:

```bash
$ cat ~/.ssh/config
Host daic
  HostName login.daic.tudelft.nl
  User <YourNetID>
```

where:
* The `Host` keyword starts the SSH configuration block and specifies the name (or pattern of names, like `daic` in this example) to which the configuration entries will apply. 
* The `HostName` is the actual hostname to log into. Numeric IP addresses are also permitted (both on the command line and in HostName specifications).
* The `User` is the login username. This is especially important when the username differs between your machine and the remote server/cluster.
* The `Port` is the port number on the remote host. Port 22 is the default port for ssh.


You can then connect to DAIC by just typing the following command:
```bash
$ ssh daic

The HPC cluster is restricted to authorized users only.

YourNetID@login.daic.tudelft.nl's password: 
Last login: Tue Jul 25 02:24:49 2023 from srv228.tudelft.net
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
 02:24:59 up 51 days, 14:38,  1 user,  load average: 0,08, 0,10, 0,13
YourNetID@login1:~$
YourNetID@login1:~$ hostname # check you are in DAIC
login1.hpc.tudelft.nl
```

{{% alert title="Warning" color="info" %}}
This method of access applies only when connecting from within TU Delft's network. If connecting from outside the university network, it is also convenient to add `bastion` to your ssh configuration file as follows: 

```bash
Host bastion
  Hostname linux-bastion.tudelft.nl # For employees and guests. If you are student, use: student-linux.tudelft.nl instead
  User <YourNetID>
  PreferredAuthentications password
```

 You can then connect simply by:

```bash
$ hostname # check you are on your local machine
$ ssh bastion 
YourNetID@linux-bastion-ex.tudelft.nl's password: 
                ____  ____  ___                            
 ___ _ ____   _|___ \|___ \( _ )
/ __| '__\ \ / / __) | __) / _ \
\__ \ |   \ V / / __/ / __/ (_) |
|___/_|    \_/ |_____|_____\___/
                                                           

!! Attention dear users !!

=====
This server is not meant for storing large files.
It's mainly for hopping to another server and storing your ssh keys.
Your homedirectory is therefore limited in space.
If you store large files on this server anyway we reserve the right to remove them.
=====
Last login: Wed Jul 19 12:32:01 2023 from 145.90.39.240
[YourNetID@srv228 ~]$ 
[YourNetID@srv228 ~]$ hostname # check you are on the bastion server
srv228.tudelft.net
```
{{% /alert %}}



### Single Sign-On with bastion server

By default you have to enter your password for every connection (eg, first to the bastion and then to `DAIC`, for all SSH and SCP/SFTP connections from outside university network). It's much more convenient to only have to enter your password once. SSH multiplexing can be configured to reduce these logins by adding the following to the end of the configuration file:

```bash
$ cat ~/.ssh/config
Host *
  ControlMaster auto
  ControlPath /tmp/ssh-%r@%h:%p
```
where:
* The `ControlPath` specifies where to store the “control socket” for the multiplexed connections. In this case, `%r` refers to the remote login name, `%h` refers to the target host name, and `%p` refers to the destination port. Including this information in the control socket name helps SSH separate control sockets for connections to different hosts.
* The `ControlMaster` is what activates multiplexing. With the `auto` setting, SSH will try to use a master connection if one exists, but if one doesn’t exist it will create a new one (this is probably the most flexible approach, but you can refer to ssh-config(5) for more details on the other settings).



{{% alert title="Note" color="info" %}}
 Windows users may need to adapt the `ControlPath` location to match Windows. 
{{% /alert %}}


{{% alert title=Warning color="warning"%}}
SSH public key logins (passwordless login) *won't work* reliably, because Kerberos authentication is required to access your home directory
{{% /alert %}}


### ssh proxy jump support

To connect directly from your machine to a DAIC login node (when outside the university network), use the ssh _Jump Host_ option to jump the bastion server as follows:

``` bash
$ ssh -J <user@jump_host> <user@target_host>
```
  where:
  * `<user@jump_host>`: The user and hostname (or IP address) of the jump host, the intermediary server you can reach directly. 
  * `<user@target_host>`: This is the user and hostname (or IP address) of the final target host, the server you want to connect to.


Thus, to login to DAIC (when outside the university network):

```bash
$ ssh -J YourNetID@linux-bastion.tudelft.nl YourNetID@login.daic.tudelft.nl # use `student-linux.tudelft.nl` instead if you are a student
YourNetID@linux-bastion.tudelft.nl's password: 

The HPC cluster is restricted to authorized users only.

YourNetID@login.hpc.tudelft.nl's password: 
Last login: Wed Jan 17 06:37:15 2024 from srv227.tudelft.net
#########################################################################
#									#
# Welcome to login1, login server of the HPC cluster.			#
# 									#
# By using this cluster you agree to the terms and conditions.		#
#									#
# For information about using the HPC cluster, see:			#
# https://login.hpc.tudelft.nl/						#
#									#
# The bulk, group and project shares are available under /tudelft.net/,	#
# your windows home share is available under /winhome/$USER/.		#
#									#
#########################################################################
 06:39:25 up 25 days, 14:21,  4 users,  load average: 0,39, 0,26, 0,24
YourNetID@login1:~$ 
YourNetID@login1:~$ 
```

For convenience, you can also edit your ssh configuration file, `~/.ssh/config`, on your local computer as follows: 

```bash
Host daic-login
  Hostname login.daic.tudelft.nl
  User <YourNetID>
  ProxyJump linux-bastion.tudelft.nl # For employees and guests. If you are a student, use: student-linux.tudelft.nl instead
```

Where:
* `HostName`: Specifies the actual hostname or IP address of the target host (a DAIC login node in this case).
* `User`: Specifies the username to use when connecting to the target host. This is your TU Delft's NetID
*`ProxyJump`: Specifies the jump server, bastion in this case. 


{{% alert title="Note" color="info" %}}
Putting it all together, your `~/.ssh/config` file could simply be:

```bash
Host bastion
  Hostname linux-bastion.tudelft.nl # For employees and guests. If you are student, use: student-linux.tudelft.nl instead
  User <YourNetID>
  PreferredAuthentications password
Host daic-login
  Hostname login.daic.tudelft.nl
  User <YourNetID>
  ProxyJump bastion
```

{{% /alert %}}



You can then simply use: `ssh daic-login` to login. 

```bash
$ hostname # check this is your local machine
$ ssh daic-login
YourNetID@linux-bastion-ex.tudelft.nl's password: 

The HPC cluster is restricted to authorized users only.

YourNetID@login.hpc.tudelft.nl's password: 
Last login: Tue Jul 25 02:13:33 2023 from srv228.tudelft.net
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
 02:13:56 up 51 days, 14:27,  1 user,  load average: 0,02, 0,10, 0,12
YourNetID@login1:~$ 
YourNetID@login1:~$ hostname
login1.hpc.tudelft.nl
```


{{%alert title="Note" color="info" %}}
When using the _ProxyJump feature_, you will be prompted for your password twice: once for the bastion server, and then for DAIC
{{%/alert%}}


### Graphical clients

For Windows, the (free) graphical clients PuTTY (SSH) and FileZilla (SFTP) are available (see official {{< external-link "http://www.chiark.greenend.org.uk/~sgtatham/putty/" "PuTTY page" >}} and {{< external-link "http://filezilla-project.org/" "FileZilla page" >}}). On machines with a TUD-configured Windows installation, you can find PuTTY under `Start -> All Programs -> Tools -> Putty Suite -> PuTTY` and FileZilla under `Start -> All Programs -> Internet -> Filezilla FTP Client-> FileZilla`.

In Linux, you can use your default file manager (`Konqueror` or `Nautilus`) for SFTP, and just run SSH from a terminal. PuTTY (SSH) and FileZilla (SFTP) are available, but have to be installed by hand.

Machines with a TUD-configured Mac OS X installation come with Fetch (SFTP) installed in the Application folder. FileZilla (SFTP) is available, but has to be installed. For SSH, it's probably easiest to just run SSH from a terminal. 

<!--
#### ~~PuTTY settings~~

 ~~The following screen-shots show the most important settings for using PuTTY with the TU Delft linux servers. Unless otherwise specified, just use the default values.~~

#### ~~FileZilla settings~~
-->  