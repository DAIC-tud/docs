---
title: "Data management & transfer"
linkTitle: "Data management & transfer"
weight: 20
description: >
  How and where to store data on DAIC.
---

## Data Management Guidelines
There are different use cases and quota limits for the different TU Delft network drives. For example, `Umbrella` (project storage), is for everybody and everything, while `bulk` needs to be cleaned up, migrated and phased out. Always check TU Delft {{< external-link "https://tudelft.topdesk.net/tas/public/ssp/content/detail/service?unid=f359caaa60264f99b0084941736786ae" "Overview data storage" >}} for guidelines on using network drives and quota limits.


## Data transfer

Your Windows Personal Storage and the Project and Group Storage are available on all TU Delft installed machines including the DAIC compute servers. If possible use one of these for files that you want to access on both your personal computer and the compute servers. Your Windows Personal Storage and the Project and Group Storage are also accessible off-campus through the TU Delft `webdata service`. See the {{< external-link "https://webdata.tudelft.nl/" "webdata page" >}} for manuals on using the service with your personal computer.

### SCP

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


### rsync
`rsync` is a robust file copying and synchronization tool commonly used in Unix-like operating systems. It allows you to transfer files and directories efficiently, both locally and remotely. `rsync` supports options that enable compression, preserve file attributes, and allow for incremental updates.

#### Basic Usage

- **Copy files locally:**
    ```bash
    rsync [options] source destination
    ```

    This command copies files and directories from the source to the destination.

- **Copy files remotely:**
    ```bash
    rsync [options] source user@remote_host:destination
    ```

    This command transfers files from a local source to a remote destination.

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