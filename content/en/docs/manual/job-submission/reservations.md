---
title: "Reservations"
linkTitle: "Reservations"
weight: 50
description: >
  How to submit jobs to slurm?
---

## Resources reservations
Slurm gives the possibility to reserve one or more compute nodes _exclusively_ for a specific user or group of users. A reservation ensures that the designated node (or nodes) are dedicated solely to the reservation holder's tasks and are not shared with other users during the reserved period. This feature allows users to plan the execution of future workloads, and accommodates cluster users with special needs beyond the batch system (eg latency measurement scenarios).

{{% alert title="Note" color="warning" %}}
Using reservations is in line with the [General cluster usage clauses](/docs/policies#general-cluster-usage) of DAIC users' agreement. However, please be mindful that reservations are intended to facilitate special needs that cannot be satisfied by the batch system, and should not be requested to guarantee fast throughput for production runs.
{{% /alert %}}

### Using reservations
Once your reservation request is approved and a reservation is placed on the system, you can run your jobs in the reservation by specifying  `--qos=reservation` along with the following directives to your slurm commands: `--reservation=<name>` and `--partition=<partition>`. For example, to submit the job `job.sbatch` to a reservation named `icra_iv` on the `cor1` node on the `cor` partition use:

```bash
$ sbatch --qos=reservation --reservation=icra_iv --partition=cor job.sbatch
```

Alternatively, it is possible to add the following lines to the `job.sbatch` file, and submitting this file as usual:

```bash
#SBATCH --qos=reservation
#SBATCH --reservation=icra_iv
#SBATCH --partition=cor
```


{{% alert title="Note" color="info" %}}
It is possible to submit jobs to a reservation once it is created. Jobs will start immediately when the reservation is available, but already running jobs on resources will not be canceled for the reservation to start.
{{% /alert %}}


{{% alert title="Note" color="warning" %}}
When a reservation is used to run your jobs, remember to also pass the reservation parameters to your srun steps:

```bash
$ srun --qos=reservation --reservation=<reservation_name> --partition=<partition_name> <some_script.sh>
```
{{% /alert%}}

To make use of an existing reservation you have to specify `--qos=reservation` and `--reservation=<reservation-name>` in your `sbatch` script.

### Requesting a Reservation
To request a reservation for nodes, please use to the [Request Reservation form](/docs/policies#access-accounts). You can request a reservation for an entire compute node (or a group of nodes)  **if you have contributed this (or these) nodes to the cluster and you have special needs that needs to be accommodated**.

General guidelines for reservations' requests:
* You can be granted a reservation *only* on nodes from a partition that is contributed by your group (See [Partitions](/docs/manual/job-submission/partitions) to check the name of the partition contributed by your group, and [System specifications](/docs/system/) for a listing of available nodes and their features).
* Please ask for the least amount of resources you need as to minimize impact on other users.
* _Plan ahead and request your reservation as soon as possible_: Reservations usually ignore running jobs, so any running job on the machine(s) you request will continue to run when the reservation starts. While jobs from other users will not start on the reserved node(s), the resources in use by an already running job at the start time of the reservation will not be available in the reservation until this running job ends. The earlier ahead you request resources, the easier it is to allocate the requested resources.

### Viewing reservations
To view all active and future reservations run the `scontrol` command as follows:

```bash
$ scontrol show reservations
ReservationName=icra_iv StartTime=2023-09-09T00:00:00 EndTime=2023-09-16T00:00:00 Duration=7-00:00:00
   Nodes=cor1 NodeCnt=1 CoreCnt=32 Features=(null) PartitionName=cor Flags=
   TRES=cpu=64
   Users=(null) Groups=(null) Accounts=3me-cor Licenses=(null) State=ACTIVE BurstBuffer=(null) Watts=n/a
   MaxStartDelay=(null)

ReservationName=maintenance weekend 2023-10-14 StartTime=2023-10-13T20:00:00 EndTime=2023-10-16T09:00:00 Duration=2-13:00:00
   Nodes=3dgi[1-2],100plus,awi[01-26],cor1,gpu[01-11],grs[1-4],influ[1-6],insy[11-12,14-16],tbm5,wis1 NodeCnt=58 CoreCnt=2000 Features=(null) PartitionName=(null) Flags=MAINT,IGNORE_JOBS,SPEC_NODES,ALL_NODES
   TRES=cpu=4000
   Users=root Groups=(null) Accounts=(null) Licenses=(null) State=INACTIVE BurstBuffer=(null) Watts=n/a
   MaxStartDelay=(null)
```

{{%alert title="Note" color="info"%}}
* Jobs can run on a reservation only if explicitly requested as shown in the [Requesting a reservation section](#requesting-a-reservation).
* Only jobs from the `Users` or `Accounts` associated with the reservation (as shown in the `scontrol show reservations` output) will be run on the reservation
* `STATE` of a reservation will show as `ACTIVE` (instead of `INACTIVE`) during the reservation window.
{{%/alert%}}


<!--

### Ending a reservation¶

All running jobs under a reservation will be terminated when the reservation ends. There are two ways to end a reservation earlier than scheduled:

    When requesting the reservation, you can ask us to activate a setting that will terminate the reservation a few minutes after all jobs in the reservation queue have completed.

    If your reservation does not have the above setting and you complete all planned computations before the reservation ends, please call NERSC operations at 1-800-666-3772 (or 1-510-486-8600) menu option 1 to cancel the reservation.

-->

