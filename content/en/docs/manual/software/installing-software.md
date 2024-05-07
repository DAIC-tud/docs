---
title: "Installing software"
linkTitle: "Installing software"
weight: 10
description: >
  How to install unavailable software?
---

## Basic principles
- On a cluster, it's important that software is available and identical on all nodes, both _login_ and _compute_ nodes (see [Workload scheduler](/docs/system#workload-scheduler)). For self-installed software, it's easier to install the software in one shared location than installing and maintaining the same software separately on every single node. You should therefore install your software on one of the network shares (eg, your `$HOME` folder or an `umbrella` or `bulk` folder) that are accessible from all nodes (see [Storage](/docs/system#storage)).

- As a regular Linux user you don't have administrator rights. Yet, you can do your normal work, including installing software _in a personal folder_, without needing administrator rights. Consequently, you don't need (nor are you allowed) to use the `sudo` or `su` commands that are often shown in manuals. 

- DAIC provides only 8GB of storage in the `/home` directories and the project spaces (`/tudelft.net/...`) are Windows-based leading to problems installing packages with `pip` due to file permission errors.
However, `/tudelft.net/...` locations are mounted on all nodes. Therefore, the recommened way of using your own software and environments is to use containerization and to store your containers under `/tudelft.net/staff-umbrella/...`. Check out the [Apptainer tutorial](/tutorials/apptainer) for guidance. 

{{% alert title="Stop!" color="warning" %}}

Although both Linux flavors _Red Hat Enterprise Linux_ (RHEL, CentOS, Scientific Linux, Fedora) and _Debian_ (Ubuntu) can run the same Linux software, they use completely different package systems for installing software. 
The available software, packages' names and package versions might differ, and the package formats and package management tools are incompatible. This means:
- It is not possible to install Ubuntu or Debian `.deb` packages in CentOS or use `apt-get` to install software in DAIC. So when installing software, use a manual for CentOS, Red Hat or Fedora. 
- If you can only find a manual for Ubuntu, you have to substitute the CentOS versions for any Ubuntu-specific packages or commands. 
{{% /alert %}}


## Managing environments
### Conda/Mamba
Conda and Mamba are both package management and environment management tools used primarily in the data science and programming communities. Conda, developed by Anaconda, Inc., allows users to manage packages and create isolated environments for different projects, supporting multiple languages like Python and R. Mamba is a more recent alternative to Conda that offers faster performance and improved dependency solving using the same package repositories as Conda. Both tools help avoid dependency conflicts and simplify the management of software packages and environments.

#### Use module load conda
Miniconda is available as [module](../modules).

```bash
$ module load miniconda
$ which conda
/opt/insy/miniconda/3.9/condabin/conda
```

### Creating a conda environment
To create a new environment you can run `conda create`:

```bash
conda create -n env
Collecting package metadata (current_repodata.json): done
Solving environment: done

==> WARNING: A newer version of conda exists. <==
  current version: 4.10.1
  latest version: 24.3.0

Please update conda by running

    $ conda update -n base -c defaults conda

## Package Plan ##

  environment location: /home/nfs/username/.conda/envs/env
```

#### Creating a conda environment from a YAML file

Conda allows you to create environments from a YAML file that specifies the packages and their versions for the desired environment. This feature makes it easier to reproduce environments across different machines and share environment configurations with others.

```bash
conda env create -f environment.yml (-n new-name)
```

For how to create a `environment.yml` file see [Exporting environments](#exporting-environments)

### Environment variables
You can set enviromnet variables to install packages and environments in other locations:

- `CONDA_PREFIX`: This variable points to the active conda environment's root directory. When an environment is active, `CONDA_PREFIX` contains the path to that environment's root directory.

- `CONDA_ENVS_DIRS`: This variable specifies the directories where conda environments are stored. You can set it to a list of directories (separated by colons on Unix-like systems and semicolons on Windows). Conda will search for and store environments in these directories.

- `CONDA_PKGS_DIRS`: This variable specifies the directories where conda stores downloaded packages. Like `CONDA_ENVS_DIRS`, you can set it to a list of directories. Conda uses these directories as cache locations for package downloads and installations.


#### Examples
- **Set conda environments directory**:
```bash
export CONDA_ENVS_DIRS="/tudelft.net/staff-umbrella/my-project/conda/envs"
export CONDA_PKGS_DIRS="/tudelft.net/staff-umbrella/my-project/conda/pkgs"
```

A caveat is that the `/tudelft.net` mounts are windows based and therefore have compatibility issues with `pip`. When you create your conda environments there you will not be able to use `pip` to install packages. It is therefore recommeneded to keep the conda environments minimal and in your home directory, and to use [containerization](../containerization) for larger environments.

### List existing environments

You can list environments with 

```bash
conda env list
```

### Activating environments
You can activate an existing environemnt with `conda activate`, for example to install more packages:

```bash
$ conda activate env  # Activate the newly created environment
```

### Modifying environments

Sometimes you need to add/remove/change packages and libraries in existing environments. First, activate the enviroment you want to change with `conda activate` and then run `conda install package-name` or `conda remove package-name`. You can also use `pip` to install packages inside a conda environment, but for that `pip` has to be installed inside the environment. To make sure `pip` is installed in your enviroment run `conda install pip` first.

```bash
(env) $ conda install pandas  # Add a new package to the active environment
Collecting package metadata (current_repodata.json): done
Solving environment: done

==> WARNING: A newer version of conda exists. <==
  current version: 4.10.1
  latest version: 24.3.0

Please update conda by running

    $ conda update -n base -c defaults conda

## Package Plan ##

  environment location: /home/nfs/sdrwacker/.conda/envs/test

  added / updated specs:
    - pandas

The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    blas-1.0                   |              mkl           6 KB
    bottleneck-1.3.7           |  py312ha883a20_0         140 KB
    bzip2-1.0.8                |       h5eee18b_5         262 KB
    expat-2.6.2                |       h6a678d5_0         177 KB
    intel-openmp-2023.1.0      |   hdb19cb5_46306        17.2 MB
    ld_impl_linux-64-2.38      |       h1181459_1         654 KB
    libffi-3.4.4               |       h6a678d5_0         142 KB
    libuuid-1.41.5             |       h5eee18b_0          27 KB
    mkl-2023.1.0               |   h213fc3f_46344       171.5 MB
    mkl-service-2.4.0          |  py312h5eee18b_1          66 KB
    mkl_fft-1.3.8              |  py312h5eee18b_0         204 KB
    mkl_random-1.2.4           |  py312hdb19cb5_0         284 KB
    ncurses-6.4                |       h6a678d5_0         914 KB
    numexpr-2.8.7              |  py312hf827012_0         149 KB
    numpy-1.26.4               |  py312hc5e2394_0          11 KB
    numpy-base-1.26.4          |  py312h0da6c21_0         7.7 MB
    openssl-3.0.13             |       h7f8727e_0         5.2 MB
    pandas-2.2.1               |  py312h526ad5a_0        15.4 MB
    pip-23.3.1                 |  py312h06a4308_0         2.8 MB
    python-3.12.3              |       h996f2a0_0        34.8 MB
    pytz-2023.3.post1          |  py312h06a4308_0         197 KB
    readline-8.2               |       h5eee18b_0         357 KB
    setuptools-68.2.2          |  py312h06a4308_0         1.2 MB
    six-1.16.0                 |     pyhd3eb1b0_1          18 KB
    sqlite-3.41.2              |       h5eee18b_0         1.2 MB
    tbb-2021.8.0               |       hdb19cb5_0         1.6 MB
    tk-8.6.12                  |       h1ccaba5_0         3.0 MB
    tzdata-2024a               |       h04d1e81_0         116 KB
    wheel-0.41.2               |  py312h06a4308_0         131 KB
    xz-5.4.6                   |       h5eee18b_0         651 KB
    zlib-1.2.13                |       h5eee18b_0         103 KB
    ------------------------------------------------------------
                                           Total:       266.1 MB

The following NEW packages will be INSTALLED:

  _libgcc_mutex      pkgs/main/linux-64::_libgcc_mutex-0.1-main
  _openmp_mutex      pkgs/main/linux-64::_openmp_mutex-5.1-1_gnu
  blas               pkgs/main/linux-64::blas-1.0-mkl
  bottleneck         pkgs/main/linux-64::bottleneck-1.3.7-py312ha883a20_0
  bzip2              pkgs/main/linux-64::bzip2-1.0.8-h5eee18b_5
  ca-certificates    pkgs/main/linux-64::ca-certificates-2024.3.11-h06a4308_0
  expat              pkgs/main/linux-64::expat-2.6.2-h6a678d5_0
  intel-openmp       pkgs/main/linux-64::intel-openmp-2023.1.0-hdb19cb5_46306
  ld_impl_linux-64   pkgs/main/linux-64::ld_impl_linux-64-2.38-h1181459_1
  libffi             pkgs/main/linux-64::libffi-3.4.4-h6a678d5_0
  libgcc-ng          pkgs/main/linux-64::libgcc-ng-11.2.0-h1234567_1
  libgomp            pkgs/main/linux-64::libgomp-11.2.0-h1234567_1
  libstdcxx-ng       pkgs/main/linux-64::libstdcxx-ng-11.2.0-h1234567_1
  libuuid            pkgs/main/linux-64::libuuid-1.41.5-h5eee18b_0
  mkl                pkgs/main/linux-64::mkl-2023.1.0-h213fc3f_46344
  mkl-service        pkgs/main/linux-64::mkl-service-2.4.0-py312h5eee18b_1
  mkl_fft            pkgs/main/linux-64::mkl_fft-1.3.8-py312h5eee18b_0
  mkl_random         pkgs/main/linux-64::mkl_random-1.2.4-py312hdb19cb5_0
  ncurses            pkgs/main/linux-64::ncurses-6.4-h6a678d5_0
  numexpr            pkgs/main/linux-64::numexpr-2.8.7-py312hf827012_0
  numpy              pkgs/main/linux-64::numpy-1.26.4-py312hc5e2394_0
  numpy-base         pkgs/main/linux-64::numpy-base-1.26.4-py312h0da6c21_0
  openssl            pkgs/main/linux-64::openssl-3.0.13-h7f8727e_0
  pandas             pkgs/main/linux-64::pandas-2.2.1-py312h526ad5a_0
  pip                pkgs/main/linux-64::pip-23.3.1-py312h06a4308_0
  python             pkgs/main/linux-64::python-3.12.3-h996f2a0_0
  python-dateutil    pkgs/main/noarch::python-dateutil-2.8.2-pyhd3eb1b0_0
  python-tzdata      pkgs/main/noarch::python-tzdata-2023.3-pyhd3eb1b0_0
  pytz               pkgs/main/linux-64::pytz-2023.3.post1-py312h06a4308_0
  readline           pkgs/main/linux-64::readline-8.2-h5eee18b_0
  setuptools         pkgs/main/linux-64::setuptools-68.2.2-py312h06a4308_0
  six                pkgs/main/noarch::six-1.16.0-pyhd3eb1b0_1
  sqlite             pkgs/main/linux-64::sqlite-3.41.2-h5eee18b_0
  tbb                pkgs/main/linux-64::tbb-2021.8.0-hdb19cb5_0
  tk                 pkgs/main/linux-64::tk-8.6.12-h1ccaba5_0
  tzdata             pkgs/main/noarch::tzdata-2024a-h04d1e81_0
  wheel              pkgs/main/linux-64::wheel-0.41.2-py312h06a4308_0
  xz                 pkgs/main/linux-64::xz-5.4.6-h5eee18b_0
  zlib               pkgs/main/linux-64::zlib-1.2.13-h5eee18b_0


Proceed ([y]/n)? y
....
```

### Exporting environments

You can export versions of all installed packages and libaries inside a coda environment with `conda env export`.
It is good practice to keep track of all versions that you have used for a particular experiment by exporting it into a YAML file typically called `environment.yml`:

```bash
conda env export --no-builds > environment.yml
```

### Install your own mamba/conda

Sometimes the versions provided by `module` are outdated and users need their own installation of `conda` or `mamba`. 
A minimal version can be installed as demonstrated in the following:

```bash
$ alias install-miniforge='
    wget https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-Linux-x86_64.sh \
    && bash Miniforge3-Linux-x86_64.sh -b \
    && rm -f Miniforge3-Linux-x86_64.sh \
    && eval "$($HOME/miniforge3/bin/conda shell.bash hook)" \
    && conda init \
    && conda install -n base -c conda-forge mamba'

$ cd ~ && install-miniforge

(base) $  # This shows that the 'base' environment is active.
(base) $ which python
~/miniforge3/bin/python
```

This will already occupy around 500MB of your home directory totalling ~20k files.

```bash
du -h miniforge3 --max-depth=0
486M	miniforge3

find miniforge3 -type f | wc -l
20719
```

Now, you can install your own versions of libraries and programs, or create entire environments as descibed above.

{{% alert title="Stop!" color="warning" %}}
You are limited to 8GB of data in your home directoy. Installing a full development environement for PyTorch can easily exceed 12 GB; Therefore, it is recommeneded to install only tools and libraries that you really need on the login nodes via this route. Instead, use `Apptainer` to create container files containing all dependencies.
{{% /alert %}}

## Using binaries
Some programs come as precompiled binaries or are written in a scripting language such as Perl, PHP, Python or shell script. Most of these programs don't actually need to be "installed" since you can simply run these programs directly. In certain scenarios, you may need to make the program executable first using `chmod +x`: 

```bash
$ ./my-executable        # attempting to run the binary `my-executable`
-bash: ./my-executable: Permission denied

$ chmod +x program       # making `my-executable` executable, since it fails due to permissions

$ ./my-executable        # checking `my-executable` works!
Hello world!

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

