---
title: "Handy commands on DAIC"
linkTitle: "Handy commands on DAIC"
weight: 1
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
