---
title: "Job chains"
linkTitle: "Job chains"
weight: 30
description: >
  How to submit jobs to slurm?
---


### Deploying dependent jobs (job chains)

In certain scenarios, it might be desirable to condition the execution of a certain job on the status of another job. In such cases, the sbatch directive `--dependency=<condition>:<jobID>` can be used, where `<condition>` specifies the type of dependency (See table 2), and `<jobID>` is the slurm jobID upon which dependency is based. To specify more than one dependency, the `,` separator is used to indicate that all dependencies must be specified, and, `?` is used denotes that any dependency may be satisfied.

For example, assume the slurm job scripts, `job_1.sbatch`, ... `job_3.sbatch` need to run sequentially one after the other. To start this chain, submit the first job and obtain its jobID:

```bash
$ sbatch job_1.sbatch
Submitted batch job 8580135
```

Next, submit the second job to run only if the first job is successful:

```bash
$ sbatch --dependency=afterok:8580135 job_2.sbatch
Submitted batch job 8580136
```
{{% alert title="Note" color="warning"%}}
Note that if the first job (with jobID `8580135` in the example) fails, the second job (with jobID `8580136`) will not run, but it will remain in the queue. You have to use `scancel 8580136` to cancel this job
{{% /alert %}}


And, now, to run the third job only after the first two jobs have both run successfully:

```bash
$ sbatch --dependency=afterok:8580135,8580136 job_3.sbatch
Submitted batch job 8580140
```

Alternatively, if the third job is dependent on either job running successfully:
```bash
$ sbatch --dependency=afterok:8580135?8580136 job_3.sbatch
Submitted batch job 8580141
```



{{% alert title="Warning" color="warning"%}}
* If the jobs within a chain involve copying data files to a local disk (`/tmp`) on a node, you need to make sure all jobs use the same node (`--nodelist=<node>`, for example `--nodelist=insy15`)
{{% /alert %}}


<table>
<caption> Table 2: Possible sbatch dependency conditions
</caption>
<thead>
  <tr>
    <th>Argument</th>
    <th>Description</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>after</td>
    <td>This job can begin execution after the specified jobs have begun execution</td>
  </tr>
  <tr>
    <td>afterany</td>
    <td>This job can begin execution after the specified jobs have terminated.</td>
  </tr>
  <tr>
    <td>aftercorr</td>
    <td>A task of this job array can begin execution after the corresponding task ID in the specified job has completed successfully</td>
  </tr>
  <tr>
    <td>afternotok</td>
    <td>This job can begin execution after the specified jobs have terminated in some failed state</td>
  </tr>
  <tr>
    <td>afterok</td>
    <td>This job can begin execution after the specified jobs have successfully executed</td>
  </tr>
  <tr>
    <td>singleton</td>
    <td>This job can begin execution after any previously launched jobs sharing the same job name and user have terminated</td>
  </tr>
</tbody>
</table>
