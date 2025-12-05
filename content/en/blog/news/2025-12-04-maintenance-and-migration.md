---
title: 2025-12-04
date: 2025-12-04
description: >
 Planned Maintenance and Upcoming Migration (11–17 December 2025)
---

{{% alert title="Scheduled Downtime" color="warning" %}}
As announced [earlier](2025-10-31-daic-offline.md), **DAIC will be unavailable from Thursday 11 December to Wednesday 17 December 2025** due to planned maintenance of the TU Delft datacenter.  
During this period, **no jobs can run** and **all login nodes will be offline**.
{{% /alert %}}

## Maintenance overview

As part of this maintenance:
- Six GPU nodes will be **removed from DAIC** and **migrated to a new environment** for testing.
- The new environment will form the basis of the **upcoming DAIC upgrade in Q1 2026**.


## Maintenance time line

### Before the maintenance:

- DAIC can be used normally.
- Jobs with a requested end-time after Wednesday **December 10 23:59**  will remain pending until after the maintenance.

### During the maintenance (December 11 00:00 - Wednesday December 17 23:59):

- No jobs can run; queued jobs will remain in the queue.
- All nodes, including the login nodes, will be unavailable
- All sessions on the login nodes will be lost.
- 6 GPU nodes will be removed from DAIC.

### After the maintenance:

- DAIC can be used normally again.
- All partitions and GPU types will remain available.
- Jobs that were held previously because of the maintenance will remain on hold. To release your jobs:
  1. Update your Kerberos ticket with `auks -a`, 
  2. Release the job(s) with   `scontrol release <JobID>`.

## Upcoming new environment Q1 2026

To ensure the continuity of DAIC, **DAIC will be migrated to a new environment**, (with an up-to-date OS, scheduler and software stack) in the first quarter of 2026.

The migration will be phased, to allow for an as seamless as possible transition from the old to the new environment.
The 6 GPU nodes (of different CPU & GPU types) will be migrated first, to prepare, test and fine-tune the new environment.
When the test environment is fully operational, it will allow you to modify and test your jobs in the new environment.
Then, the bulk of the DAIC nodes will be migrated to the new environment, and the old environment will be discontinued.
More details will be provided when the new environment is ready for testing.

