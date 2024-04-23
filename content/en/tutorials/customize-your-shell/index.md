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

Aliases are custom shortcuts or abbreviations for longer commands in the shell. They allow you to define a shorter, user-friendly command that, when executed, will perform a longer or more complex command. For example, you might create an alias like `alias ll='ls -la'` in your .bashrc file to quickly list all files in a directory in long format. Aliases can help improve productivity by saving time and effort when working with the shell. You can set these configurations permanently by editing your `~/.bashrc` file.

```bash
## Add these lines to your ~/.bashrc file to make use of these settings.

# Alias
alias ll='ls -alF'
alias la='ls -A'
alias ls='ls --color=auto'
alias l='ls -rtlh --full-time --color=auto'
alias md='mkdir'
alias ..='cd ..'
alias ...='cd ../..'
alias ....='cd ../../..'
alias src='source ~/.bashrc'

## Slurm helpers
alias interactive='srun --pty --nodes=1 --ntasks=1 --cpus-per-task=4 --mem=8G --time=1:00:00 bash'
alias st='sacct --format=JobID,JobName%30,State,Elapsed,Timelimit,AllocNodes,Priority,Start,NodeList'
alias sq="squeue -u $USER --format='%.18i %.12P %.30j %.15u %.2t %.12M %.6D %R'"
alias slurm-show-my-accounts='sacctmgr list user "$USER" withassoc format="user%-20,account%-45,maxjobs,maxsubmit,maxwall,maxtresperjob%-40"'
alias slurm-show-all-accounts='sacctmgr show account format=Account%30,Organization%30,Description%60'
alias slurm-show-nodes='sinfo -lNe'

# Shellstyle

## Assuming your shell background is black!

## Prompt setting (readable prompt colors and username@hostname:)
export PS1='\[\033[01;96m\]\u\[\033[0m\]@\[\033[01;32m\]\h\[\033[0m\]:\[\033[96m\]\w\[\033[00m\]\$ '

## ls colors (readable ls colors)
export LS_COLORS='rs=0:di=1;35:ln=01;36:mh=00:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:su=37;41:sg=30;43:ca=30;41:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arj=01;31:*.taz=01;31:*.lzh=01;31:*.lzma=01;31:*.tlz=01;31:*.txz=01;31:*.zip=01;31:*.z=01;31:*.Z=01;31:*.dz=01;31:*.gz=01;31:*.lz=01;31:*.xz=01;31:*.bz2=01;31:*.bz=01;31:*.tbz=01;31:*.tbz2=01;31:*.tz=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.war=01;31:*.ear=01;31:*.sar=01;31:*.rar=01;31:*.ace=01;31:*.zoo=01;31:*.cpio=01;31:*.7z=01;31:*.rz=01;31:*.jpg=01;35:*.jpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.svg=01;35:*.svgz=01;35:*.mng=01;35:*.pcx=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.m2v=01;35:*.mkv=01;35:*.webm=01;35:*.ogm=01;35:*.mp4=01;35:*.m4v=01;35:*.mp4v=01;35:*.vob=01;35:*.qt=01;35:*.nuv=01;35:*.wmv=01;35:*.asf=01;35:*.rm=01;35:*.rmvb=01;35:*.flc=01;35:*.avi=01;35:*.fli=01;35:*.flv=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.yuv=01;35:*.cgm=01;35:*.emf=01;35:*.axv=01;35:*.anx=01;35:*.ogv=01;35:*.ogx=01;35:*.aac=00;36:*.au=00;36:*.flac=00;36:*.mid=00;36:*.midi=00;36:*.mka=00;36:*.mp3=00;36:*.mpc=00;36:*.ogg=00;36:*.ra=00;36:*.wav=00;36:*.axa=00;36:*.oga=00;36:*.spx=00;36:*.xspf=00;36:';
```

### REIT bash configuration
An example configuration is available here: https://gitlab.ewi.tudelft.nl/reit/shell-config

