---
title: "Cancelling jobs"
linkTitle: "Cancelling jobs"
weight: 28
description: >
  How to cancel/stop scheduled or running jobs?
---


* And finally, to cancel a given job:

```bash
$ scancel <jobID>
```

{{% alert title="Note" color="warning"%}}
It is possible to specify the `sbatch` directives, like `--mem`, `--ntasks`, ... etc in the command line as in:
```bash
$ sbatch --time=00:02:00 jobscript.sbatch
```
This specification is generally not recommended for production, as it is less reproducible than specifying within the job script itself.
{{% /alert %}}