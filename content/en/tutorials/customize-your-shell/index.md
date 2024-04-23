---
title: "Customize your shell"
weight: 2
description: >
  After logging in to DAIC you can customize your shell.
---

## Source `.bashrc` upon login
`.bashrc` is a configuration file for the Bash shell, which is the default command-line shell on many Linux and Unix-based systems. It is a hidden file located in the user's home directory (`~/.bashrc`) and is executed every time a new interactive Bash session starts. The file contains settings that customize the shell's behavior, such as defining environment variables, setting prompt appearance, and specifying terminal options.

Edit or create the file `~/.profile` and insert the following line:

```bash
source ~/.bashrc
```
Now, your `.bashrc` will be loaded upon login.

## Customize prompt and aliases.

Aliases are custom shortcuts or abbreviations for longer commands in the shell. They allow you to define a shorter, user-friendly command that, when executed, will perform a longer or more complex command. For example, you might create an alias like `alias ll='ls -la'` in your .bashrc file to quickly list all files in a directory in long format. Aliases can help improve productivity by saving time and effort when working with the shell.

### REIT bash configuration
https://gitlab.ewi.tudelft.nl/reit/shell-config