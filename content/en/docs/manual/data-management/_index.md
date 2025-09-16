---
title: "Data management & transfer"
linkTitle: "Data management & transfer"
weight: 20
description: >
  How and where to store data on DAIC.
---

## Data Management Guidelines

DAIC login and compute nodes have direct access to standard TU Delft network storage, including your personal home folder, group storage, and project storage. It is important to use the correct storage location for your data, as each has different use cases, access rights, and quota limits.

For example, **Project Storage** (`staff-umbrella`) is the recommended location for research data, datasets, and code. In contrast, `staff-bulk` is a legacy storage area that is being phased out. For a complete overview of storage types, official guidelines, and quota limits, always consult the **TU Delft {{< external-link "https://tudelft.topdesk.net/tas/public/ssp/content/detail/service?unid=f359caaa60264f99b0084941736786ae" "Overview data storage" >}}**.

This page explains the best methods for transferring data to and from these storage locations.


## Recommended Workflow: Direct Data Download

The most efficient way to download large datasets from external sources (e.g. collaborators or public repositories) is to transfer them directly from your **local computer** to your TU Delft project storage. This avoids using the DAIC login and compute nodes, which are optimized for computation, not large data transfers, and avoids unnecessary load on the internal network.

{{% alert title="Note" color="warning" %}}
Do not connect to DAIC using sshfs! That would only (over)load the network connection to the login nodes, which would affect  the interactive work of other users. Instead, download data directly to your project storage as described below.
{{% /alert %}}


Follow these steps to download data directly to your project storage (and access it from DAIC):

### 1. Access your DAIC storage from your local computer


You can either mount the storage as a network drive or use an `SFTP` client. Mounting is often more convenient as it makes the remote storage appear like a local folder. Choose the appropriate method for your operating system:


{{< tabpane text=true right=true >}}
  {{% tab header="**Operating System**:" disabled=true /%}}

  {{% tab header="Windows" %}}
**For TU Delft-managed computers:**
- Project Data Storage is mounted automatically under `This PC` as `Project Data (U:)` or `\\tudelft.net\staff-umbrella`.

**For personal computers:**
- Connect to EduVPN first.
- Install [**WebDrive**](https://webdata.tudelft.nl/) and connect to `sftp.tudelft.nl`. Click on `staff-umbrella` (this is the Project Data Storage).

  {{% /tab %}}

  {{% tab header="MacOS" %}}

**Option 1: Using Finder**
1. Press `⌘K` or choose **Go > Connect to Server**.
2. Enter: `smb://tudelft.net/staff-umbrella/<your_project_name>` and click `Connect`.
3. (Optional) Add this address to your **Favorite Servers** for easy access later.

**Option 2: Using an SFTP client (e.g., Terminal, FileZilla, CyberDuck)**

Connect to `sftp.tudelft.nl` with your NetID and password. From the terminal, you can use:

```bash
sftp <YourNetID>@sftp.tudelft.nl
cd staff-umbrella/<your_project_name>
put data.zip  # Upload a file (data.zip) to your storage
get results.zip # Download a file (results.zip) from your storage
```

Graphical clients like [FileZilla](https://filezilla-project.org/) or [CyberDuck](https://cyberduck.io/) provide a drag-and-drop interface for the same purpose.

    {{% /tab %}}

    {{% tab header="Linux" %}}

**For TU Delft-managed computers:**
- For managed Ubuntu 22.04, [contact ICT](https://tudelft.topdesk.net/tas/public/ssp/content/serviceflow?unid=bb079374b047400382d67566e4b57597&from=cac22e81-a71b-4aaa-b268-da90e255e19a&openedFromService=true) for setting up the mount.
- For Ubuntu 18.04, storage is mounted under `/tudelft.net/staff-umbrella/`:
  - You can access it via the terminal:
    ```bash
    cd /tudelft.net/staff-umbrella/<your_project_name>
    ```
  - Or via the file manager (nautilus or dolphin): `under Other locations > Computer > tudelft.net > staff-umbrella > <your_project_name>`

**For personal computers:**
**Option 1: Mount with sshfs**
```bash
mkdir ~/storage_mount
sshfs YourNetID@sftp.tudelft.nl:/staff-umbrella/<your_project_name> ~/storage_mount
ls ~/storage_mount # Check contents of your project storage
```
And, after you are done with the mount:

```bash
fusermount -u ~/storage_mount
```

**Option 2: Use `sftp`**

```bash
sftp <YourNetID>@sftp.tudelft.nl
cd staff-umbrella/<your_project_name>
put data.zip  # Upload a file (data.zip) to your storage
get results.zip # Download a file (results.zip) from your storage
```
 {{% /tab %}}

{{< /tabpane >}}

### 2. Download the data directly to the storage location

Once you have mounted or connected to your storage, you can use standard tools like `wget`, `curl`, or your web browser to download files directly into that location.

For example, if you mounted your storage on Linux at `~/storage_mount`, you can download a large dataset into your project folder with wget:

```bash
wget -P ~/storage_mount/datasets/ https://www.robots.ox.ac.uk/~vgg/data/flowers/102/102flowers.tgz

```

The file (the [Oxford Flowers 102 Dataset](https://www.robots.ox.ac.uk/~vgg/data/flowers/102/index.html) in this example) downloads directly to your project folder in the `staff-umbrella` storage, using your local machine's network connection.



## Command-Line Transfer Tools
<!-- Your Windows Personal Storage and the Project and Group Storage are available on all TU Delft installed machines including the DAIC compute servers. If possible use one of these for files that you want to access on both your personal computer and the compute servers. Your Windows Personal Storage and the Project and Group Storage are also accessible off-campus through the TU Delft `webdata service`. See the {{< external-link "https://webdata.tudelft.nl/" "webdata page" >}} for manuals on using the service with your personal computer. -->
Both your Linux and Windows Personal Storage and the Project and Group Storage are also available world-wide via an SCP/SFTP client.

For direct transfers between your local machine and DAIC, or for scripting automated workflows, you can use command-line tools like `scp` and `rsync`.


### SCP (Secure Copy)

The `scp` command provides a simple way to copy files over a secure channel. It has the following basic syntax:


```bash
$ scp <source_file> <target_destination>       # for files
$ scp -r <source_folder> <target_destination>  # for folders
```

For example, to transfer a file from your computer to DAIC:

```bash
$ scp mylocalfile [<YourNetID>@]login.daic.tudelft.nl:~/destination_path_on_DAIC/
```

To transfer a folder (recursively) from your computer to DAIC:

```bash
$ scp -r mylocalfolder [<YourNetID>@]login.daic.tudelft.nl:~/destination_path_on_DAIC/
```

To transfer a file from DAIC to your computer:

```bash
$ scp [<YourNetID>@]login.daic.tudelft.nl:~/origin_path_on_DAIC/remotefile ./
```

To transfer a folder from DAIC to your computer:

```bash
$ scp -r [<YourNetID>@]login.daic.tudelft.nl:~/origin_path_on_DAIC/remotefolder ./
```

The above commands work from both the university network, or when using EduVPN. If a "jump" via `linux-bastion` is needed (see [Access from outside university network](/docs/manual/connecting/#access-from-outside-university-network)), modify the above commands by replacing scp with `scp -J <YourNetID>@linux-bastion.tudelft.nl` and keep the rest of the command as before:

```bash
# Transfer a local file to DAIC via the bastion host
$ scp -J [<YourNetID>@]linux-bastion.tudelft.nl <localfile> [<YourNetID>@]login.daic.tudelft.nl:/tudelft.net/staff-umbrella/<your_project_name>/

# Transfer a remote file from DAIC to your local machine via the bastion host
$ scp -J [<YourNetID>@]linux-bastion.tudelft.nl [<YourNetID>@]login.daic.tudelft.nl:/tudelft.net/staff-umbrella/<your_project_name>/<remotefile> ./

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


### rsync
`rsync` is a robust file copying and synchronization tool commonly used in Unix-like operating systems. It allows you to transfer files and directories efficiently, both locally and remotely. `rsync` supports options that enable compression, preserve file attributes, and allow for incremental updates.

#### Basic Usage

- **Copy files locally:**
    ```bash
    rsync [options] <source> <destination>
    ```

    This command copies files and directories from the `source` to the `destination`.

- **Copy files remotely:**
    ```bash
    rsync [options] <source> <user>@<remote_host>:<destination>
    ```

    This command transfers files from a local `source` to a  `destination` on a remote host.

{{% alert title="Note" color="warning" %}}
When sending data to `staff-umbrella` or `staff-bulk`, you **must** use the `--no-perms` option to avoid errors, as the underlying network filesystem does not support changing permissions.

A recommended command to use is:

```bash
$ rsync --progress -avz --no-perms <source_file> [<YourNetID>@]login.daic.tudelft.nl:<destination_umbrella_directory>
``` 

This command is effective because: 
- `--progress` shows the transfer progress. 
- `-a` (archive mode) efficiently copies directories and preserves file attributes like timestamps. 
- `-v` provides verbose output. 
- `-z` compresses data to speed up the transfer. 
- `--no-perms` prevents errors related to file permissions on the destination.

{{% /alert %}}       

#### Examples

- **Synchronize a local directory with a remote directory:**
    ```bash
    rsync -avz /path/to/local/dir user@remote_host:/path/to/remote/dir
    ```

    This synchronizes a local directory with a remote directory, using archive mode (`-a`) to preserve file attributes, verbose mode (`-v`) for detailed output, and compression (`-z`) for efficient transfer.

- **Synchronize a remote directory with a local directory:**
    ```bash
    rsync -avz user@remote_host:/path/to/remote/dir /path/to/local/dir
    ```

    This transfers files from a remote directory to a local directory, using the same options as the previous example.

- **Delete files in the destination that are not present in the source:**
    ```bash
    rsync -av --delete /path/to/source/dir /path/to/destination/dir
    ```

    This synchronizes the source and destination directories and deletes files in the destination that are not in the source.

- **Exclude certain files or directories during transfer:**
    ```bash
    rsync -av --exclude='*.tmp' /path/to/source/dir /path/to/destination/dir
    ```

    This synchronizes the source and destination directories, excluding files with the `.tmp` extension.

#### Other Options in rsync

In addition to the commonly used options, `rsync` provides several other options for more advanced control and customization during file transfers:

- `--dry-run`: Perform a trial run without making any changes. This option allows you to see what would be done without actually doing it.

- `--checksum`: Use checksums instead of file size and modification time to determine if files should be transferred. This is more precise but slower.

- `--partial`: Keep partially transferred files and resume them later. This is useful in case of an interrupted transfer.

- `--partial-dir=DIR`: Specify a directory to hold partial transfers. This option works well with `--partial`.

- `--bwlimit=KBPS`: Limit the bandwidth used by the transfer to the specified rate in kilobytes per second. Useful for managing network load.

- `--timeout=SECONDS`: Set a maximum wait time in seconds for receiving data. If the timeout is exceeded, `rsync` will exit.

- `--no-implied-dirs`: When transferring a directory, this option prevents the creation of implied directories on the destination side that exist in the source but not explicitly specified in the transfer.

- `--files-from=FILE`: Read a list of source files from the specified FILE. This can be useful when you want to transfer specific files.

- `--update`: Skip files that are newer on the destination than the source. This is useful for incremental backups.

- `--ignore-existing`: Skip files that already exist on the destination. Useful when you want to avoid overwriting existing files.

- `--inplace`: Update files in place instead of creating temporary files and renaming them later. This can save disk space and improve speed.

- `--append`: Append data to files instead of replacing them if they already exist on the destination.

- `--append-verify`: Append data and verify it with checksums to ensure integrity.

- `--backup`: Make backups of files that are overwritten or deleted during the transfer. By default, a `~` is appended to the backup filename.

- `--backup-dir=DIR`: Specify a directory to store backup files.

- `--suffix=SUFFIX`: Specify a suffix to append to backup files instead of the default `~`.

- `--progress`: Displays the progress of the transfer, including the speed and the number of bytes transferred. This is useful for monitoring long transfers and seeing how much data has been copied so far.

These options, along with others, provide additional flexibility and control over your `rsync` transfers, allowing you to fine-tune the synchronization process to meet your specific needs.


<!--
## see this example: 
* https://www.nhr.kit.edu/userdocs/horeka/filesystems/
* https://www.hrz.tu-darmstadt.de/hlr/nutzung_hlr/dateisysteme_hlr/index.en.jsp
-->