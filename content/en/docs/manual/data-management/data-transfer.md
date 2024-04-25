---
title: "Data transfer"
linkTitle: "Data transfer"
weight: 58
description: >
  How to move data to DAIC.
---

## Data Transfer Methods

### Between TU Delft installed machines 

Your Windows Personal Storage and the Project and Group Storage are available on all TU Delft installed machines including the DAIC compute servers. If possible use one of these for files that you want to access on both your personal computer and the compute servers. 

### Using webdata

Your Windows Personal Storage and the Project and Group Storage are also accessible off-campus through the TU Delft `webdata service`. See the {{< external-link "https://webdata.tudelft.nl/" "webdata page" >}} for manuals on using the service with your personal computer.

### Using SCP/SFTP

Both your Linux and Windows Personal Storage and the Project and Group Storage are also available world-wide via an SCP/SFTP client. This is the simplest transfer method via the `scp` command, which has the following basic syntax:

```bash
$ scp <source_file> <target_destination>       # for files
$ scp -r <source_folder> <target_destination>  # for folders
```

For example, to transfer a file from your computer to DAIC:

```bash
$ scp mylocalfile [<netid>@]login.daic.tudelft.nl:~/destination_path_on_DAIC/
```

To transfer a folder (recursively) from your computer to DAIC:

```bash
$ scp -r mylocalfolder [<netid>@]login.daic.tudelft.nl:~/destination_path_on_DAIC/
```

To transfer a file from DAIC to your computer:

```bash
$ scp [<netid>@]login.daic.tudelft.nl:~/origin_path_on_DAIC/remotefile ./
```

To transfer a folder from DAIC to your computer:

```bash
$ scp -r [<netid>@]login.daic.tudelft.nl:~/origin_path_on_DAIC/remotefolder ./
```

The above commands will work from either the university network, or when using EduVPN. If a "jump" via `linux-bastion` is needed (see [Access from outside university network](/docs/manual/connecting/#access-from-outside-university-network)), modify the above commands by replacing scp with `scp -J <netid>@linux-bastion.tudelft.nl` and keep the rest of the command as before:

```bash
$ scp <local_file> [<netid>@]linux-bastion.tudelft.nl:<remote_destination>
$ scp -r <local_folder> [<netid>@]linux-bastion.tudelft.nl:<remote_destination>
$ scp [<netid>@]linux-bastion.tudelft.nl:<remote_file> <local_destination> 
$ scp -r [<netid>@]linux-bastion.tudelft.nl:<remote_folder> <local_destination>

$ sftp [<netid>@]linux-bastion.tudelft.nl
```

Where:
*  Case is important.
* Items between < > brackets are user-supplied values (so replace with your own NetID, file or folder name).
* Items between [ ] brackets are optional: when your username on your local computer is the same as your NetID username, you don't have to specify it.
* When you specify your NetID username, don't forget the @ character between the username and the computer name. 


{{% alert title="Note for students" color="warning" %}}
Please use `student-linux.tudelft.nl` instead of `linux-bastion.tudelft.nl` as an intermediate server!
{{% /alert %}}

{{% alert title="Hint" color="info" %}}
Use quotes when file or folder names contain spaces or special characters. 
{{% /alert %}} 

### SCP alternatives

More powerful alternatives to scp exist, like `rsync` for synchronizing source and destination, and `sshfs` for mounting folders to your linux computer. See {{< external-link "https://doc.dhpc.tudelft.nl/delftblue/Data-transfer-to-DelftBlue/#rsync" "DelftBlue file transfer" >}}  documentation for use of these tools, and use the proper DAIC addresses instead.


### To or from local storage

For files that you want to transfer to or from local storage, first transfer them to Project or Scratch Storage. Then in your job script, copy the files to the local storage, run your work, and afterwards delete your files from local storage. 



<!--
## see this example: 
* https://www.nhr.kit.edu/userdocs/horeka/filesystems/
* https://www.hrz.tu-darmstadt.de/hlr/nutzung_hlr/dateisysteme_hlr/index.en.jsp
-->