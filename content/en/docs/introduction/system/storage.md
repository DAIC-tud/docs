---
title: "Storage"
linkTitle: "Storage"
weight: 40
description: >
  Description of all file systems and storage locations available.
---

{{% pageinfo %}}
DAIC servers have direct access to the TU Delft [home](#personal-storage-aka-home-folder), [group](#group-storage) and [project](#project-storage) storage. You can use your TU Delft installed machine or an SCP or SFTP client to transfer files to and from these storage areas and others (see [data transfer](/docs/manual/data-management/data-transfer/)) , as is demonstrated throughout this page.
{{% /pageinfo %}}


## File System Overview

Unlike TU Delft's {{< external-link "https://doc.dhpc.tudelft.nl/delftblue/DHPC-hardware/#description-of-the-delftblue-system" "DelftBlue" >}}, DAIC does not have a dedicated storage filesystem. This means no `/scratch` space for storing temporary files (see DelftBlue's {{< external-link "https://doc.dhpc.tudelft.nl/delftblue/DHPC-hardware/#description-of-the-delftblue-system" "Storage description" >}} and {{< external-link "https://doc.dhpc.tudelft.nl/delftblue/DHPC-Policies/#disk-quota-and-scratch-space" "Disk quota and scratch space" >}}). Instead, DAIC relies on direct connection to the TU Delft network storage filesystem (see {{< external-link "https://tudelft.topdesk.net/tas/public/ssp/content/detail/service?unid=f359caaa60264f99b0084941736786ae" "Overview data storage">}}) from all its nodes, and offers the following types of storage areas:

### Personal storage (aka home folder)

 The Personal Storage is private and is meant to store personal files (program settings, bookmarks).  A backup service protects your home files from both hardware failures and user error (you can restore previous versions of files from up to two weeks ago). The available space is limited by a quota limit (since this space is not meant to be used for research data). 

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
    <td>only accessible using an scp/sftp client (see <a href="https://daic.pages.ewi.tudelft.nl/docs/docs/connecting/">SSH access</a>)</td>
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


### Local Storage 

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

### Memory Storage

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

