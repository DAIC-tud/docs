---
title: "Installing software"
linkTitle: "Installing software"
weight: 2
description: >
  How to install unavailable software?
---


## Basic principles

- On a cluster, it's important that software is available and identical on all nodes, both _login_ and _compute_ nodes (see [Batch queuing system](/docs/introduction/system/scheduler#file-system-overview)). For self-installed software, it's easier to install the software in one shared location than installing and maintaining the same software separately on every single node. You should therefore install your software on one of the network shares (eg, your `$HOME` folder or an `umbrella` or `bulk` folder) that are accessible from all nodes (see [File system overview](/docs/introduction/system/storage/#file-system-overview)).


- As a regular Linux user you don't have administrator rights. Yet, you can do your normal work, including installing software _in a personal folder_, without needing administrator rights. Consequently, you don't need (nor are you allowed) to use the `sudo` or `su` commands that are often shown in manuals. 

{{% alert title="Stop!" color="warning" %}}

Although both Linux flavors _Red Hat Enterprise Linux_ (RHEL, CentOS, Scientific Linux, Fedora) and _Debian_ (Ubuntu) can run the same Linux software, they use completely different package systems for installing software. 
The available software, packages' names and package versions might differ, and the package formats and package management tools are incompatible. This means:
- It is not possible to install Ubuntu or Debian `.deb` packages in CentOS or use `apt-get` to install software in DAIC. So when installing software, use a manual for CentOS, Red Hat or Fedora. 
- If you can only find a manual for Ubuntu, you have to substitute the CentOS versions for any Ubuntu-specific packages or commands. 
{{% /alert %}}



## Using binaries when possible

Some programs come as precompiled binaries or are written in a scripting language such as Perl, PHP, Python or shell script. Most of these programs don't actually need to be "installed" since you can simply run these programs directly. In certain scenarios, you may need to make the program executable first: 

```bash
$ ./program        # attempting to run the binary `program`
-bash: ./program: Permission denied
$ 
$ chmod +x program # making `program` executable, since it fails due to permissions
$
$ ./program        # checking `program` works!
Hello world!
$
```

## Installing from source

When a pre-made binary of your software is not available, you'll have to install the software yourself from the source. You may need to set up your [Installation environment](#installation-environment) before following this [Installation recipe](#installation-recipe).

### Installation environment

When you are installing software for the very first time, you need to set up your environment. If you have already done this before , you can skip this section and go directly to the [Installation recipe](#installation-recipe) section.

To set up your environment, first, add the following lines to your `~/.bash_profile` or, alternatively, download this ([bash_profile.txt](https://gitlab.ewi.tudelft.nl/daic/docs/-/blob/main/content/en/docs/software_environment/bash_profile.txt?ref_type=heads)) as shown in the subsequent commands:

{{< card header="bash_profile.txt" >}}
```bash
# Get the aliases and functions
if [ -f ~/.bashrc ]; then
   . ~/.bashrc
fi

# User specific environment and startup settings
export PREFIX="$HOME/.local"
export ACLOCAL_PATH="$PREFIX/share/aclocal${ACLOCAL_PATH:+:$ACLOCAL_PATH}"
export CPATH="$PREFIX/include${CPATH:+:$CPATH}"
export LD_LIBRARY_PATH="$PREFIX/lib64:$PREFIX/lib${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"
export LIBRARY_PATH="$PREFIX/lib64:$PREFIX/lib${LIBRARY_PATH:+:$LIBRARY_PATH}"
export MANPATH="$PREFIX/share/man${MANPATH:+:$MANPATH}"
export PATH="$HOME/bin:$PREFIX/bin:$PATH"
export PERL5LIB="$PREFIX/lib64/perl5:$PREFIX/share/perl5${PERL5LIB:+:$PERL5LIB}"
export PKG_CONFIG_PATH="$PREFIX/lib64/pkgconfig:$PREFIX/share/pkgconfig${PKG_CONFIG_PATH:+:$PKG_CONFIG_PATH}"
export PYTHONPATH="$PREFIX/lib/python2.7/site-packages${PYTHONPATH:+:$PYTHONPATH}"
```
{{< /card >}}




{{< alert title="Note!" color="info"  >}}
1.  if you already have some of these settings in your `~/.bash_profile` (or elsewhere), you should combine them so they don't duplicate the paths. 
2.  if you want to use `python3.6` instead of `python2.7`, you need to set the `PYTHONPATH` to `python3.6`. 
{{< /alert >}}



```bash
$ cp ~/.bash_profile ~/.bash_profile.bak # back up your file
$ curl -s https://wiki.tudelft.nl/pub/Research/InsyCluster/InstallingSoftware/bash_profile.txt >> ~/.bash_profile # download and append the lines above
$
$ # clean up any duplicate settings
$
$ source ~/.bash_profile # 
$ mkdir -p "$PREFIX"
```

The line `export PREFIX="$HOME/.local"` sets your software installation directory to `/home/nfs/<YourNetID>/.local` (which is the default and accessible on all nodes). This is in your personal home directory where you have a space quota of 8GB. However, for software for your research project, you should instead use a project share, for example: 

```bash
export PREFIX="/tudelft.net/staff-umbrella/project/software"
```

The other variables will let you use your self-installed programs. You are now ready to install your software! 


### Installation recipe

Software installation _usually_ just requires you to follow the general installation recipe described below, but you always need to consult the documentation for your software.

1. Place the source of the software in a folder under `/tmp`:

```bash
$ mkdir /tmp/$USER
$ cd /tmp/$USER
$ wget http://host/path/software.tar.gz
$ tar -xzf software.tar.gz
          Or from github: git clone https://github.com/software
$ cd software
```

{{< alert title="Note" color="info" >}}

Note: `.tgz` is the same as `.tar.gz`, for `.tar.bz2` files use tar `-xjf software.tar.bz2`. 

{{< /alert >}}

1. If the software provides a `configure` script, run it:

```bash
$ ./configure --prefix="$PREFIX" 
```

If `configure` complains about missing software, you'll either have to install that software, tell `configure` where it is (`--with-feature _path_=`) or disable the feature (`--disable-feature`).

If your software provides a `CMakeLists.txt` file, run `cmake` (note: the trailing two dots on the last line are needed exactly as shown):

```bash
$ mkdir -p build $ cd build $ cmake -DCMAKE_INSTALL_PREFIX="$PREFIX" .. 
```

Again, if `cmake` complains about missing software, you'll either have to install that software or tell `cmake` where it is (`-DCMAKE_SYSTEM_PREFIX_PATH="/usr/local;/usr;$PREFIX;path"`).

If neither is provided, consult the documentation for dependencies and configuration (specifically for the installation directory).

There is no point in continuing until all reported problems have been fixed.

2. Compile the software:

```bash
$ make 
```

If compilation is aborted due to an error, {{< external-link "https://www.google.com/" "Google" >}} the error for possible solutions. Again, there is no point in continuing until all reported problems have been fixed.



3. Install the software. When you used configure or cmake, you can simply run:

```bash
$ make install 
```


When you used neither, you need to use:
```bash
$ make prefix="$PREFIX" install 
```

4. Your software should now be ready to use, so check it:

```bash
$ cd $ _program_ 
```


5. When the program works, clean up `/tmp/netid`:

```bash
$ rm -r /tmp/$USER 
```

### Python modules

After setting up the installation environment (above) you are also able to install Python modules by yourself, by using the `--user` option. The easiest way is when the module is available through `pip2` (for Python 2) or `pip3` (for Python 3):

```bash
$ pip2 search module
$ pip2 install --user module
```


When you only have the source code for the module, follow the installation instructions for the module, but make sure to use --user in the installation step:

```bash
$ python setup.py install --user
```

<!-- 
## Virtualization: conda, virtualenv, mamba, 
-->


## Containerization

See the [Containerization tutorial](/tutorials/containerization).


