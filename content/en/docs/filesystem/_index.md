---
title: "File systems and storage"
linkTitle: "File systems and storage"
weight: 5
description: >
  How/Where to store data
---

{{% pageinfo %}}
This aspect is different from DHPC. Comment on the difference too!
{{% /pageinfo %}}

 DAIC servers have direct access to the TU Delft home, group and bulk storage. You can use your TU Delft installed machine or an SCP or SFTP client to transfer files to and from these storage areas and others, as is demonstrated throughout this page.

## File System Overview

Unlike TU Delft's [DelftBlue](https://doc.dhpc.tudelft.nl/delftblue/DHPC-hardware/#description-of-the-delftblue-system), DAIC does not have a dedicated storage filesystem. This means no `/scratch` space for storing temporary files (see DelftBlue's [Storage description](https://doc.dhpc.tudelft.nl/delftblue/DHPC-hardware/#description-of-the-delftblue-system) and [Disk quota and scratch space](https://doc.dhpc.tudelft.nl/delftblue/DHPC-Policies/#disk-quota-and-scratch-space)). Instead, DAIC relies on direct connection to the TU Delft network storage filesystem from all its nodes, and offers the following types of storage areas:

### Personal storage (aka home folder)

 The Personal Storage is private and is meant to store personal files (program settings, bookmarks).  A backup service protects your home files from both hardware failures and user error (you can restore previous versions of files from up to two weeks ago). The available space is limited by a quota limit (since this is not meant to be used for research data). 
 
 
 You have two (separate) home folders: one for Linux and one for Windows (because Linux and Windows store program settings differently). You can access these home folders from a machine (running Linux or Windows OS) using a command line interface or a browser via [TU Delft's webdata](https://webdata.tudelft.nl/). For example, Windows home has a `My Documents` folder. `My documents` can be found on a Linux machine under `/winhome/<YourNetID>/My Documents` 

<table>
<thead>
  <tr>
    <th>Home directory</th>
    <th>Access from</th>
    <th>Storage location</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td colspan="3">Linux&nbsp;&nbsp;home folder</td>
  </tr>
  <tr>
    <td></td>
    <td>Linux </td>
    <td> <code> /home/nfs/&lt;YourNetID&gt; </code> </td>
  </tr>
  <tr>
    <td></td>
    <td>Windows </td>
    <td>only accessible using an scp/sftp client (see <a href="https://www.tablesgenerator.com/connecting/_index.md#ssh-access">SSH access</a></td>
  </tr>
  <tr>
    <td></td>
    <td>webdata</td>
    <td>not available </td>
  </tr>
  <tr>
    <td colspan="3">Windows home folder</td>
  </tr>
  <tr>
    <td></td>
    <td>Linux </td>
    <td><code>/winhome/&lt;YourNetID&gt;</code></td>
  </tr>
  <tr>
    <td></td>
    <td>Windows </td>
    <td> <code> H: </code> or <code> \\tudelft.net\staff-homes\[a-z]\&lt;YourNetID&gt; </code> </td>
  </tr>
  <tr>
    <td></td>
    <td>webdata</td>
    <td> <code> https://webdata.tudelft.nl/staff-homes/[a-z]/&lt;YourNetID&gt; </code> </td>
  </tr>
</tbody>
</table>


It's possible to access the backups yourself. In Linux the backups are located under the (hidden, read-only) `~/.snapshot/` folder. In Windows you can right-click the `H:` drive and choose `Restore previous versions`. 

{{% alert title="Note" color="info" %}}

 To see your disk usage, run something like: `du -h '</path/to/folder>' | sort -h | tail`

{{% /alert %}}

### Group storage

 The Group Storage is meant to share files (documents, educational and research data) with department/group members. The whole department or group has access to this storage, so this is not for confidential or project data. There is a backup service to protect the files, with previous versions up to two weeks ago. There is a Fair-Use policy for the used space. 

 <table>
<thead>
  <tr>
    <th>Destination</th>
    <th>Access from</th>
    <th>Storage location</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td colspan="3">Group Storage</td>
  </tr>
  <tr>
    <td rowspan="2"></td>
    <td rowspan="2">Linux </td>
    <td> <code> /tudelft.net/staff-groups/&lt;faculty&gt;/&lt;department&gt;/&lt;group&gt; </code> or</td>
  </tr>
  <tr>
    <td> <code> /tudelft.net/staff-bulk/&lt;faculty&gt;/&lt;department&gt;/&lt;group&gt;/&lt;NetID&gt; </code> </td>
  </tr>
  <tr>
    <td rowspan="2"></td>
    <td rowspan="2">Windows </td>
    <td> <code> M: </code> or <code> \\tudelft.net\staff-groups\&lt;faculty&gt;\&lt;department&gt;\&lt;group&gt; </code> or</td>
  </tr>
  <tr>
    <td> <code> L: </code> or <code> \\tudelft.net\staff-bulk\ewi\insy\&lt;group&gt;\&lt;NetID&gt; </code> </td>
  </tr>
  <tr>
    <td></td>
    <td>webdata</td>
    <td> <code> https://webdata.tudelft.nl/staff-groups/</a>&lt;faculty&gt;/&lt;department&gt;/&lt;group&gt;/ </code> </td>
  </tr>
</tbody>
</table>


### Project Storage 

The Project Storage is meant for storing (research) data (datasets, generated results, download files and programs, ...) for projects. Only the project members (including external persons) can access the data, so this is suitable for confidential data (but you may want to use encryption for highly sensitive confidential data). There is a backup service and a Fair-Use policy for the used space.

Project leaders (or supervisors) can request a Project Storage location via the [Self-Service Portal or the Service Desk](https://tudelft.topdesk.net/tas/public/ssp/content/detail/service?unid=846ebb16181c43b5836c063a917dd199&from=03aa10b9-c5aa-4e0a-80b1-28ee7ab383df).

<table>
<thead>
  <tr>
    <th>Destination</th>
    <th>Access from</th>
    <th>Storage location</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td colspan="3">Project Storage</td>
  </tr>
  <tr>
    <td></td>
    <td>Linux </td>
    <td> <code> /tudelft.net/staff-umbrella/&lt;project&gt; </code> </td>
  </tr>
  <tr>
    <td></td>
    <td>Windows </td>
    <td> <code> U: </code> or <code> \\tudelft.net\staff-umbrella\&lt;project&gt; </code> </td>
  </tr>
  <tr>
    <td></td>
    <td>webdata </td>
    <td> <code> https://webdata.tudelft.nl/staff-umbrella/&lt;project&gt; </code> or <code> <br>https://webdata.tudelft.nl/staff-bulk/&lt;faculty&gt;/&lt;department&gt;/&lt;group&gt;/&lt;NetID&gt; </code> </td>
  </tr>
</tbody>
</table>


### ~~Local Storage~~ 

 Local storage is meant for temporary storage of (large amounts of) data with fast access on a single computer. You can create your own personal folder inside the local storage. Unlike the network storage above, local storage is only accessible on that computer, not on other computers or through network file servers or webdata. There is no backup service nor quota. The available space is large but fixed, so leave enough space for other users. Files under `/tmp` that have not been accessed for 10 days are automatically removed. 

 <table>
<thead>
  <tr>
    <th>Destination</th>
    <th>Access from</th>
    <th>Storage location</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td colspan="3">Local storage</td>
  </tr>
  <tr>
    <td></td>
    <td>Linux </td>
    <td><code> /tmp/&lt;NetID&gt; </code> </td>
  </tr>
  <tr>
    <td></td>
    <td>Windows </td>
    <td>not available </td>
  </tr>
  <tr>
    <td></td>
    <td>webdata </td>
    <td>not available </td>
  </tr>
</tbody>
</table>

### ~~Memory Storage~~

 Memory storage is meant for short-term storage of limited amounts of data with very fast access on a single computer. You can create your own personal folder inside the memory storage location. Memory storage is only accessible on that computer, and there is no backup service nor quota. The available space is limited and shared with programs, so leave enough space (the computer will likely crash when you don't!). Files that have not been accessed for 1 day are automatically removed. 

<table>
<thead>
  <tr>
    <th>Destination</th>
    <th>Access from</th>
    <th>Storage location</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td colspan="3">Memory storage</td>
  </tr>
  <tr>
    <td></td>
    <td>Linux </td>
    <td> <code> /dev/shm/&lt;NetID&gt; </code> </td>
  </tr>
  <tr>
    <td></td>
    <td>Windows </td>
    <td>not available </td>
  </tr>
  <tr>
    <td></td>
    <td> webdata </td>
    <td>not available </td>
  </tr>
</tbody>
</table>

 {{% alert title="Warning" color="info" %}}
 Use this only when using other storage makes your job or the whole computer slow. 
 {{% /alert %}}


## File Management Guidelines

There are different use cases and quota limits for the different TU Delft network drives. For example, `Umbrella` (project storage), is for everybody and everything, while `bulk` needs to be cleaned up, migrated and phased out. Always check TU Delft [Overview data storage](https://tudelft.topdesk.net/tas/public/ssp/content/detail/service?unid=f359caaa60264f99b0084941736786ae) for guidelines on using network drives and quota limits.


## Data Transfer Methods

### Between TU Delft installed machines 

Your Windows Personal Storage and the Project and Group Storage are available on all TU Delft installed machines including the ~~compute servers~~. If possible use one of these for files that you want to access on both your personal computer and the compute servers. 

### Using webdata

Your Windows Personal Storage and the Project and Group Storage are also accessible off-campus through the TU Delft `webdata service`. See the [webdata page](https://webdata.tudelft.nl/) for manuals on using the service with your personal computer.


### Using SCP/SFTP

Both your Linux and Windows Personal Storage and the Project and Group Storage are also available world-wide via an SCP/SFTP client. This is the simplest transfer method via the `scp` command, which has the following basic syntax:

```bash
$ scp -p ${source} ${target}
```

For example, to transfer a file from your computer to DelftBlue:

user@laptop:~$ scp -p mylocalfile <netid>@login.delftblue.tudelft.nl:~/destination_folder_on_DelftBlue/

To transfer a folder (recursively) from your computer to DelftBlue:

user@laptop:~$ scp -pr mylocalfolder <netid>@login.delftblue.tudelft.nl:~/destination_folder_on_DelftBlue/

To transfer a file from DelftBlue to your computer:

user@laptop:~$ scp -p <netid>@login.delftblue.tudelft.nl:~/origin_folder_on_DelftBlue/remotefile ./

To transfer a folder from DelftBlue to your computer:

user@laptop:~$ scp -pr <netid>@login.delftblue.tudelft.nl:~/origin_folder_on_DelftBlue/remotefolder ./

The above commands will work from either the university network, or when using EduVPN. If a "jump" via linux-bastion is needed, modify the above commands by replacing scp with scp -J <netid>@linux-bastion.tudelft.nl and keep the rest of the command as before.

Note for students

Please use student-linux.tudelft.nl instead of linux-bastion.tudelft.nl as an intermediate server!


### SCP alternatives

More powerful alternatives to scp exist, like `rsync` for synchronizing source and destination, and `sshfs` for mounting folders to your linux computer. See [DelftBlue file transfer](https://doc.dhpc.tudelft.nl/delftblue/Data-transfer-to-DelftBlue/#rsync) documentation for use of these tools, and use the proper DAIC addresses instead.


### ~~To or from local storage~~

For files that you want to transfer to or from local storage, first transfer them to Project or Scratch Storage. Then in your job script, copy the files to the local storage, run your work, and afterwards delete your files from local storage. 




## see this example: 
* https://www.nhr.kit.edu/userdocs/horeka/filesystems/
* https://www.hrz.tu-darmstadt.de/hlr/nutzung_hlr/dateisysteme_hlr/index.en.jsp