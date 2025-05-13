---
title: "Kerberos"
linkTitle: "Kerberos"
weight: 70
description: >
  How to submit jobs to slurm?
---

## Kerberos Authentication
Kerberos is an authentication protocol which uses tickets to authenticate users (and computers). You automatically get a ticket when you log in with your password on a TU Delft installed computer. You can use this ticket to authenticate yourself without password when connecting to other computers or accessing your files. To protect you from misuse, the ticket expires after 10 hours or less (even when you're still logged in).

### File access
Your Linux and Windows [Home](/docs/system/storage/#personal-storage-aka-home-folder) directories and the [Group](/docs/system/storage/#group-storage) and [Project](/docs/system/storage/#project-storage) shares are located on network fileservers, which allows you to access your files from all TU Delft installed computers. Kerberos authentication is used to enable access to, or protect, your files. Without a valid Kerberos ticket (e.g. when the ticket has expired) you will not be able to access your files but instead you will receive a `Permission denied` error.

### Lifetime of Kerberos Tickets
Kerberos tickets have a limited valid lifetime (of up to 10 hours) to reduce the risk of abuse, even when you stay logged in. If your tickets expire, you will receive a `Permission Denied` error when you try to access your files and a password prompt when you try to connect to another computer. When you want your program to be able to access your files for longer than the valid ticket lifetime, you'll have to renew your ticket (repeatedly) until your program is done. Kerberos tickets can be renewed up to a maximum renewable life period of 7 days (again to reduce the risk of abuse).

The command `klist -5` lists your cached Kerberos tickets together with their expiration time and maximum renewal time:

```bash 
$ klist -5
Ticket cache: FILE:/tmp/krb5cc_uid_random
Default principal: YourNetID@TUDELFT.NET

Valid starting     Expires            Service principal
01/01/01 00:00:00  01/01/01 10:00:00  krbtgt/TUDELFT.NET@TUDELFT.NET
        renew until 01/08/01 00:00:00
```
Where: 
* `Ticket cache`:  The Kerberos tickets that have been issued to you are stored in a ticket cache file. You can have multiple ticket cache files on the same computer (from different connections, for example) with different tickets and ticket expiration times. Some ticket cache files are automatically removed when you logout. 
{{% alert title="Tip" color="info" %}}
Make sure that you renew the tickets in the right ticket cache file (see this [`screen` example](#renewal-using-screen)).
{{% /alert %}}

* `Default principal`: Your identity. 
* `Service principal`: The identity of services that you have gotten tickets for. You always need a Kerberos ticket-granting ticket (`krbtgt`) in order to obtain other tickets for specific services like accessing files (`nfs`) or connecting to computers (`host`). 
* `Valid starting`, `Expires`: Your ticket is only valid between these times (this period is called the valid lifetime). After this time you will not be able to use the service nor automatically renew the ticket (without password). 
* `Renew until`: Your ticket can only be renewed without password up to this time. After this time you will have to obtain a new ticket using your password. 

### Renewing Kerberos tickets
If you have a valid Kerberos `krbtgt` ticket, you can renew it at any time (until it expires) by running the command `kinit -R`:

```bash
$ kinit -R
$ klist -5
Ticket cache: FILE:/tmp/krb5cc_uid_random
Default principal: YourNetID@TUDELFT.NET

Valid starting     Expires            Service principal
01/01/01 01:00:00  01/01/01 11:00:00  krbtgt/TUDELFT.NET@TUDELFT.NET
        renew until 01/08/01 00:00:00
```
{{% alert title="Note" color="info" %}}
Renewing the ticket will not change the duration of the valid lifetime, i.e. a `krbtgt` ticket with a valid lifetime of 1 hour will, after renewal, be valid for another hour.
{{% /alert %}}


When the `krbtgt` ticket has expired or reached it's renew until time, you will have to obtain a new ticket by running `kinit -r 7d` (note the difference in case for the `r`) and authenticating with your password:

```bash
$ kinit -r 7d
Password for YourNetID@TUDELFT.NET:
$ klist -5
Ticket cache: FILE:/tmp/krb5cc_uid_random
Default principal: YourNetID@TUDELFT.NET

Valid starting     Expires            Service principal
01/01/01 11:00:00  01/01/01 21:00:00  krbtgt/TUDELFT.NET@TUDELFT.NET
        renew until 01/08/01 11:00:00
```

The new ticket will have a valid lifetime of 10 hours and a renewable life of 7 days.

On the TU Delft Linux desktops your Kerberos ticket is refreshed (i.e. replaced by a new ticket) automatically every time you enter your password for unlocking the screen saver. 

{{% alert title="Tip" color="info" %}}
Do not disable the screen saver password lock.
{{% /alert %}}

On remote computers you have to manually renew your tickets before they expire.

### Slurm & Kerberos
* Slurm caches your Kerberos ticket, and uses it to execute your job
* Regularly renew the ticket in Slurm’s cache while your jobs are queued or running:

```bash
$ auks -a
Auks API request succeed
```

* To automatically renew your ticket in Slurm’s cache until you change your NetID password, run the following on the `login1` node:

```bash
$ install_keytab
Password for somebody@TUDELFT.NET:
Installed keytab.
```

You need to rerun this command whenever you change your NetID password (at least every 6 months). Otherwise, the automatic renewal will not work and you will receive a warning e-mail.

### Renewal using `screen`
On the compute nodes, the `screen` program has been modified to allow jobs to run unattended for up to 7 days. It creates a private ticket cache (to prevent the cache from being destroyed at logout) and automatically renews your ticket up to the maximum renewable life. For example, start MATLAB in Screen with `screen matlab` (the order is important!).

```bash
$ screen matlab
Warning: No display specified.  You will not be able to display graphics on the screen.

                           < M A T L A B (R) >
                 Copyright 1984-2010 The MathWorks, Inc.
              Version 7.11.0.584 (R2010b) 64-bit (glnxa64)
                             August 16, 2010


  To get started, type one of these: helpwin, helpdesk, or demo.
  For product information, visit www.mathworks.com.

>>
```

For longer jobs you have to manually obtain a new ticket at least every 7 days by running `kinit -r 7d` **from within `screen`** (so you use the specific ticket cache file that `screen` is using):

1. connect to screen (`screen -r`),
1. create a new window (`Ctrl-a c`),
1. run `kinit -r 7d`,
1. exit the window (`exit`) and
1. detach from screen (`Ctrl-a d`). 

```bash
$ kinit -r 7d
Password for YourNetID@TUDELFT.NET:
$ klist -5
Ticket cache: FILE:/tmp/krb5cc_uid_private
Default principal: YourNetID@TUDELFT.NET

Valid starting     Expires            Service principal
01/08/01 09:00:00  01/08/01 19:00:00  krbtgt/TUDELFT.NET@TUDELFT.NET
        renew until 01/15/01 09:00:00
$ exit
```

{{% alert title="Tip" color="info" %}}
Use a repeating reminder (twice a week) in your agenda so you don't forget.
{{% /alert %}}

{{% alert title="Important" color="warning" %}}
When the end of the renewable life is reached, your tickets expire and your program(s) will return Permission denied errors when trying to access your files. Your program(s) will not be terminated automatically; you still have to terminate the program(s) yourself.
{{% /alert %}}

Extra functionality can be provided by the `k5start` and `krenew` programs. On most computers these are not available by default but can be installed. 
