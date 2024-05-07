---
title: "Available software"
linkTitle: "Available software"
weight: 1
description: >
  How to find and work with pre-installed software?
---

## General software
Most common general software, like programming languages and libraries, is installed on the DAIC servers. 
To check if the program that you need is pre-installed, you can simply try to start it:

```bash
$ python
Python 2.7.5 (default, Jun 28 2022, 15:30:04) 
[GCC 4.8.5 20150623 (Red Hat 4.8.5-44)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> quit()
```

To find out which binary is used exactly you can use `which` command:
```bash
$ which python
/usr/bin/python
```

Alternatively, you can try to locate the program or library using the `whereis` command:

 ```bash
$ whereis python
python: /usr/bin/python3.4m-config /usr/bin/python3.6m-x86_64-config /usr/bin/python2.7 /usr/bin/python3.6-config /usr/bin/python3.4m-x86_64-config /usr/bin/python3.6m-config /usr/bin/python3.4 /usr/bin/python3.4m /usr/bin/python2.7-config /usr/bin/python3.6 /usr/bin/python3.4-config /usr/bin/python /usr/bin/python3.6m /usr/lib/python2.7 /usr/lib/python3.4 /usr/lib/python3.6 /usr/lib64/python2.7 /usr/lib64/python3.4 /usr/lib64/python3.6 /etc/python /usr/include/python2.7 /usr/include/python3.4m /usr/include/python3.6m /usr/share/man/man1/python.1.gz
```

 Or, you can check if the package is installed using the `rpm -qa` command as follows: 

 ```bash
$ rpm -q python
python-2.7.5-94.el7_9.x86_64
$ rpm -q python4
package python4 is not installed
```

You can also search with wildcards:

```bash
$ rpm -qa 'python*'
python2-wheel-0.29.0-2.el7.noarch
python2-cryptography-1.7.2-2.el7.x86_64
python34-virtualenv-15.1.0-5.el7.noarch
python-networkx-1.8.1-12.el7.noarch
python-gobject-3.22.0-1.el7_4.1.x86_64
python-gofer-2.12.5-3.el7.noarch
python-iniparse-0.4-9.el7.noarch
python-lxml-3.2.1-4.el7.x86_64
python34-3.4.10-8.el7.x86_64
python36-numpy-f2py-1.12.1-3.el7.x86_64
...
```

### Useful commands on DAIC
For a list of handy commands on DAIC have a look [here](/docs/manual/commands).