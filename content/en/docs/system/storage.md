---
title: "Storage"
weight: 4
description: >
  What are the foundational components of DAIC?
---

## Storage
{{% pageinfo %}}
DAIC compute nodes have direct access to the TU Delft [home](#personal-storage-aka-home-folder), [group](#group-storage) and [project](#project-storage) storage. You can use your TU Delft installed machine or an SCP or SFTP client to transfer files to and from these storage areas and others (see [data transfer](/docs/manual/data-management/)) , as is demonstrated throughout this page.
{{% /pageinfo %}}

### File System Overview
Unlike TU Delft's {{< external-link "https://doc.dhpc.tudelft.nl/delftblue/DHPC-hardware/#description-of-the-delftblue-system" "DelftBlue" >}}, DAIC does not have a dedicated storage filesystem. This means no `/scratch` space for storing temporary files (see DelftBlue's {{< external-link "https://doc.dhpc.tudelft.nl/delftblue/DHPC-hardware/#description-of-the-delftblue-system" "Storage description" >}} and {{< external-link "https://doc.dhpc.tudelft.nl/delftblue/DHPC-Policies/#disk-quota-and-scratch-space" "Disk quota and scratch space" >}}). Instead, DAIC relies on direct connection to the TU Delft network storage filesystem (see {{< external-link "https://tudelft.topdesk.net/tas/public/ssp/content/detail/service?unid=f359caaa60264f99b0084941736786ae" "Overview data storage">}}) from all its nodes, and offers the following types of storage areas:

### Personal storage (aka home folder)
The Personal Storage is private and is meant to store personal files (program settings, bookmarks).  A backup service protects your home files from both hardware failures and user error (you can restore previous versions of files from up to two weeks ago). The available space is limited by a quota (see [Quotas](#checking-quota-limits)) and is not intended for storing research data.

You have two (separate) home folders: one for Linux and one for Windows (because Linux and Windows store program settings differently). You can access these home folders from a machine (running Linux or Windows OS) using a command line interface or a browser via {{< external-link "https://webdata.tudelft.nl/" "TU Delft's webdata" >}}. For example, Windows home has a `My Documents` folder. `My documents` can be found on a Linux machine under `/winhome/<YourNetID>/My Documents` 

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
    <td>only accessible using an scp/sftp client (see <a href="https://doc.daic.tudelft.nl/docs/manual/connecting#ssh-access">SSH access</a>)</td>
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
 To see your disk usage, run something like: 
 ```bash
 du -h '</path/to/folder>' | sort -h | tail
 ```
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

Project leaders (or supervisors) can request a Project Storage location via the {{< external-link "https://tudelft.topdesk.net/tas/public/ssp/content/detail/service?unid=846ebb16181c43b5836c063a917dd199&from=03aa10b9-c5aa-4e0a-80b1-28ee7ab383df" "Self-Service Portal or the Service Desk" >}}.

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

{{% alert title="Tip" color="info" %}}

Data deleted from project storage, `staff-umbrella`, remains in a hidden `.snapshot` folder. If accidently deleted, you can recover such data by copying it from the (hidden)`.snapshot` folder in your storage.
{{% /alert %}}

### Local Storage 
Local storage is meant for temporary storage of (large amounts of) data with fast access on a single computer. You can create your own personal folder inside the local storage. Unlike the network storage above, local storage is only accessible on that computer, not on other computers or through network file servers or webdata. There is no backup service nor quota. The available space is large but fixed, so leave enough space for other users. Files under `/tmp` that have not been accessed for 10 days are automatically removed. A process that has a file opened can access the data until the file is closed, even when the file is deleted. When the file is deleted, the file entry will be removed but the data will not be removed until the file is closed. Therefore, files that are kept open by a process can be used for longer. Additionally, files that are being accessed (read, written) multiple times within one day won't be deleted.

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

### Memory Storage
{{% alert title="Warning" color="danger" %}}
Using `/dev/shm` is very risky, and should only be done when you understand all implications. Consider using the [local storage](#local-storage) (`/tmp`) as a safer alternative. 

**Cluster-wide Risk**: When memory storage fills up, it can cause memory exhaustion that kills running jobs. The scheduler cannot identify the cause, so it continues launching new jobs that will also fail, potentially making the whole cluster unusable.

**Clean up policy**: Users must always clean up '/dev/shm' after using it, even when jobs fail or are stopped via the scheduler.
{{% /alert %}}

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

{{% alert title="Info" color="info" %}}
Use this only when using other storage makes your job or the whole computer slow. Files in `/dev/shm/` use system memory directly and do not count toward your job's memory allocation. Request enough memory to cover both your job's processing needs and any files stored in memory storage. Never exceed your allocated memory, not even for one second. 
{{% /alert %}}

### Checking quota limits

The different storage areas accessible on DAIC have quotas (or usage limits). It’s important to regularly check your usage to avoid job failures and ensure smooth workflows.

Helpful commands

- For `/home`:

```bash
$ quota -s -f ~
Disk quotas for user netid (uid 000000): 
     Filesystem   space   quota   limit   grace   files   quota   limit   grace
svm111.storage.tudelft.net:/staff_homes_linux/n/netid
                 12872M  24576M  30720M           19671   4295m   4295m  
```
- For project space:
  You can use either:

```bash
$ du -hs /tudelft.net/staff-umbrella/my-cool-project
37G	/tudelft.net/staff-umbrella/my-cool-project
```
  Or:

```bash
$ df -h /tudelft.net/staff-umbrella/my-cool-project
Filesystem                                       Size  Used Avail Use% Mounted on
svm107.storage.tudelft.net:/staff_umbrella_my-cool-project  1,0T   38G  987G   4% /tudelft.net/staff-umbrella/my-cool-project
```

Note that the difference is due to snapshots, which can stay for up to 2 weeks
