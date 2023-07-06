
---
title: "QuickStart"
linkTitle: "QuickStart"
weight: 20
menu:
  main:
    weight: 20
---

{{% pageinfo %}}
This is a quick getting started guide
{{% /pageinfo %}}


When working with HPCs in general, or DAIC in particular, the workflow of _Fig 1_ needs to be followed, where code is developed locally (eg, in a laptop or PC), then ported to the cluster for further testing (eg, in an interactive node). If successful, jobs scripts are created and submitted to slurm, and progress is monitored. Finally, once all is done, intermediate files are ideally deleted, and final results downloaded for subsequent downstream analysis.

{{< figure src="clusterWorkflow.png" caption=">Fig 1: Cluster workflow, with key Unix* based commands for each step. Text within angle brackets `<`, `>` denote names that are chosen by the user" >}}




