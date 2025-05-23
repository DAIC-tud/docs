---
title: "Handy commands on DAIC"
linkTitle: "Handy commands on DAIC"
weight: 100
description: >
  Brief description of useful commandline tools.
---

## BASH commands
BASH (Bourne Again SHell) is an open-source Unix shell and command language. It is the default shell on many Linux distributions and macOS, and it's available on Windows via the Windows Subsystem for Linux, Git BASH, and other emulators. BASH is widely used for scripting and automating tasks in a computing environment. Below are some fundamental BASH commands with examples and brief explanations, aiding users in effective navigation and task execution. Remember to use these commands carefully, especially those that can modify or delete files and directories. They are fundamental tools for interacting with BASH and managing your tasks effectively.

### man

The `man` command is a tool for displaying the manual pages (documentation) of various commands and utilities available on Unix-like operating systems. It is an essential resource for users seeking detailed information about a specific command, program, or configuration file.

#### Basic Usage

**Display the manual page for a command:**
```bash
man <command>
```

This displays the manual page for the specified command.

#### Examples

**Show the manual page for the `ls` command:**
```bash
man ls
```

**Show the manual page for the `man` command:**
```bash
man man
```

### echo
Used for displaying a line of text/string that is passed as an argument. This is a fundamental command for displaying output in shell scripts.

Example: Display "Hello, World!".
```bash
echo "Hello, World!"
```

### cd
Changes the current directory to another directory. It's a basic command to navigate through the filesystem.

Example: Change to the home directory.
```bash
cd ~
```

### ls
Lists the contents of a directory. It's a key command to view files and directories.

Example: List all files and directories in the current directory, including hidden files.
```bash
ls -a
```

### tree

The `tree` command is a utility that displays the directory structure of a path in a tree-like format. It provides a visual representation of the hierarchy of files and directories, making it easier to understand the organization of a file system.

#### Basic Usage

- **Display the directory tree structure:**
    ```bash
    tree [path]
    ```

    This command displays the directory structure starting from the specified path or the current directory if no path is specified.

#### Options

- `-a`: Display all files and directories, including hidden ones (those starting with a dot).
- `-d`: Display only directories, omitting files.
- `-L level`: Limit the depth of the tree to the specified level.
- `--noreport`: Suppress the file and directory count summary at the end of the output.
- `-H baseHREF`: Create an HTML output starting with the specified base URL.
- `-o filename`: Output the tree structure to a file with the specified name.
- `--charset encoding`: Use the specified character encoding (e.g., `UTF-8`).
- `-P pattern`: Only display files matching the specified pattern (e.g., `*.txt`).
- `-I pattern`: Exclude files and directories matching the specified pattern (e.g., `*.bak`).

#### Examples

- **Display the directory tree structure starting from the current directory:**
    ```bash
    tree
    ```

- **Display the directory tree structure from a specific path:**
    ```bash
    tree /path/to/start
    ```

- **Display only directories in the tree structure:**
    ```bash
    tree -d
    ```

- **Display the tree structure and limit the depth to 2 levels:**
    ```bash
    tree -L 2
    ```

- **Display the tree structure and output it to a file:**
    ```bash
    tree -o output.txt
    ```

- **Display all files and directories, including hidden ones:**
    ```bash
    tree -a
    ```

The `tree` command is a helpful tool for quickly understanding the layout of a directory and its contents. It is especially useful for navigating complex file systems and identifying the location of files and directories within a hierarchy.

### which

The `which` command shows the full path of a command's executable file by searching the directories listed in the `PATH` environment variable.

#### Basic Usage

- **Find the path of a command:**
    ```bash
    which command
    ```

    This displays the full path of the specified command's executable file.

#### Examples

- **Find the path of the `ls` command:**
    ```bash
    which ls
    ```

- **Find the path of the `python` command:**
    ```bash
    which python
    ```

### whereis

The `whereis` command locates not only the executable file but also the source and manual page files of a command, if available.

#### Basic Usage

- **Locate a command:**
    ```bash
    whereis command
    ```

    This displays the paths to the executable, source, and manual page files of the specified command, if they exist.

#### Options

- `-b`: Search only for binaries (executable files).
- `-m`: Search only for manual pages.
- `-s`: Search only for source files.
- `-u`: Search for any missing information (binaries, source, or manual) and report it.
- `-B path`: Add a directory to the search path for binaries.
- `-M path`: Add a directory to the search path for manual pages.
- `-S path`: Add a directory to the search path for source files.

#### Examples

- **Locate the `ls` command:**
    ```bash
    whereis ls
    ```

- **Locate the `gcc` command and its source files:**
    ```bash
    whereis -s gcc
    ```

### cat
Concatenates and displays file contents. It's commonly used to view the contents of a file.

Example: Display the contents of a file named `example.txt`.
```bash
cat example.txt
```

### grep
Searches for patterns in files. It's a powerful tool for searching text using patterns.

Example: Search for the word "example" in `file.txt`.
```bash
grep "example" file.txt
```

### find
Searches for files in a directory hierarchy. This command is essential for locating files and directories.

Example: Find all .txt files in the current directory.
```bash
find . -name "*.txt"
```

### mkdir
Creates a new directory.

Example: Create a directory named `new_directory`.
```bash
mkdir new_directory
```

### rm
Removes files or directories. It's a critical command for file management.

Example 1: Remove a file named `example.txt`.
```bash
rm example.txt
```

Example 2: Remove a directory and its contents (recursively).
```bash
rm -r directory_name
```

**Warning:** Be extremely cautious with `rm -r`, especially when used with `.` (current directory) or `..` (parent directory), as this can lead to irreversible deletion of files. Never use `rm -r .` in a directory unless you are absolutely sure about deleting all its contents.


### cp
Copies files and directories.

Example: Copy `file1.txt` to `file2.txt`.
```bash
cp file1.txt file2.txt
```

### mv
Moves or renames files and directories.

Example: Rename `oldname.txt` to `newname.txt`.
```bash
mv oldname.txt newname.txt
```

### for, do, done
A for loop in Bash allows you to iterate over a list of items, such as an array, a set of files, or even a range of numbers. Below, I will provide you with a few examples of how you can use a for loop in Bash.

#### Iterating over a list of strings
In this example, the for loop iterates over a list of strings and prints each one:

```bash
# List of items
items=("apple" "banana" "cherry")

# Loop through each item
for item in "${items[@]}"; do
    echo "Item: $item"
done
```

### if, (else), then

The `if` statement in Bash scripting is used to execute a block of code conditionally based on whether an expression evaluates to true or false. Below are examples of how you can use an if statement in Bash:

```bash
filepath="/path/to/file.txt"

if [ -f "$filepath" ]; then
    echo "The file exists."
else
    echo "The file does not exist."
fi
```

### alias
In Bash, an `alias` is a shortcut for a command. You can define an alias to simplify the execution of commonly used commands or to add default options to commands you frequently use. Here are some examples of how to create and use aliases in Bash:

#### Creating a simple alias
You can create an alias by using the alias command followed by the alias name and the command it represents. Here's an example of a simple alias:

```bash
alias ll="ls -l"
```

Another commonly used alias is `md` as a shortcut for `mkdir`:

```bash
alias md="mkdir"
```

You can add these instructions to your `.bashrc` file in order to load them when logging in to the cluster.

## Slurm commands
SLURM (Simple Linux Utility for Resource Management) is an open-source job scheduler used on many of the world's supercomputers and compute clusters. It allows users to efficiently manage computing resources and queue their computational jobs for execution. Below are some essential SLURM commands with examples and brief explanations, helping users navigate and utilize these resources effectively. Remember to replace `<jobid>` with your specific job ID where necessary. These commands are vital tools for interacting with SLURM and managing your compute tasks effectively.

### sinteractive
For requesting an interactive node, typically during testing phases. Compute resources such as memory, time, and GPUs are specified as part of the command, similar to `sbatch` directives.

Example: Request a 10-minute GPU node session.
```bash
sinteractive --time=00:10:00 --gres=gpu
```

### sbatch
Used for submitting a script to SLURM for queuing in batch mode. The script includes directives at the top to specify required resources.

Example: Submit a job using a script named `script.sh`.
```bash
sbatch script.sh
```

### squeue
Checks the status of jobs in the SLURM queue. Useful for tracking your job's status and understanding the queue's state, and to find a specific `jobid` of a particular job.

Example: Check the status of all your queued jobs.
```bash
squeue -u $USER
```

### scancel
Cancels a job or all jobs of a user. Vital for managing jobs that are no longer needed or were submitted in error.

Example 1: Cancel a specific job with job ID `<jobid>`.
```bash
scancel <jobid>
```

Example 2: Cancel all jobs for the current user.
```bash
scancel -u $USER
```

### slurmtop
A DAIC-specific command to view the top jobs in the queues and their resource usage.

Example:

```bash
slurmtop
```

### scontrol
Shows detailed information and resources allocated to the job with the specified SLURM job ID.

Example: Show details of a job with job ID `jobid`.
```bash
scontrol show job <jobid>
```

### sinfo
Displays information about SLURM nodes and partitions. Key command for understanding the state of the cluster.


Example: Display information about all nodes and partitions.
```bash
sinfo
```

### sacct
Displays accounting data for all jobs and job steps. Useful for tracking resource usage and performance metrics.
Example: Display accounting data for all jobs.
```bash
sacct --format=JobID,JobName%30,State,Elapsed,Timelimit,AllocNodes,Priority,Start,NodeList
```

## Other
### module

In the context of Unix-like operating systems, the `module` command is part of the environment modules system, a tool that provides a dynamic approach to managing the user environment. This system allows users to load and unload different software packages or environments on demand.

#### Basic Usage

- **Load a module:**
    ```bash
    module load module-name
    ```

    This command loads the specified module, setting up the environment variables and paths needed for the software package.

- **Unload a module:**
    ```bash
    module unload module-name
    ```

    This command unloads the specified module, removing any environment variables and paths associated with it.

For a more detailed description of `module` see [Modules](/docs/manual/software/modules).