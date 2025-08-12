---
title: "Cluster comparison"
weight: 6
description: >
  Overview of the clusters available to TU Delft (CS) researchers
---

## Cluster comparison

{{< alert title="TL;DR" color=secondary >}}
- Most AI training → DAIC.
- Many CPUs / high-memory or MPI jobs → DelftBlue.
- Distributed/experimental systems work → DAS-6.
- Bigger than local capacity or cross-institutional projects → Snellius (SURF).
- Euro-scale GPU runs → LUMI (EuroHPC via SURF).
{{< /alert >}}



### TU Delft clusters
DAIC is one of several clusters accessible to TU Delft CS researchers (and their collaborators). The table below gives a comparison between these in terms of use case, eligible users, and other characteristics.

{{% alert title="Tip" color="dark"%}}
- When in doubt, start on DAIC for prototyping. If you hit limits (time-to-solution, memory, scale), graduate to DelftBlue, then Snellius/LUMI.
- TU Delft has other clusters that are not listed here. These tend to be more specialized or have different access requirements.
{{% /alert %}}

<table id="clusters-table" class="display">
  <thead>
    <tr>
      <th>System</th>
      <th>Best for</th>
      <th>Strengths</th>
      <th>Use it when</th>
      <th>Access & Support</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td> 🎓 <a href="/docs/system/#daic">
      <img src="/docs/system/images/logo.svg" alt="DAIC Logo" style="height:50px; margin-right:5px; vertical-align:middle;">
      </a></td>
      <td>AI/ML training; data-centric workflows; GPU‑intensive workloads</td>
      <td>Large NVIDIA GPU pool (L40, A40, RTX 2080 Ti, V100 SXM2); local expert support (<a href="https://reit.tudelft.nl/">REIT</a> and ICT); direct <a href="/docs/system/storage/">TU Delft storage</a></td>
      <td>Quick iteration, hyper‑parameter sweeps, demos, and <i>almost any workload from  <a href="/docs/about/contributors-funders/#contributing-departments">participating groups</a></i>; queues are generally shorter than DelftBlue but limited by available GPUs</td>
      <td>
        <a href="https://tudelft.topdesk.net/tas/public/ssp/content/detail/service?unid=c6d0e44564b946eaa049898ffd4e6938&from=d75e860b-7825-4711-8225-8754895b3507"> Access </a> •
        <a href="/docs/system/">Specs</a> •
        <a href="https://mattermost.tudelft.nl/signup_user_complete/?id=cb1k3t6ytpfjbf7r397395axyc&md=link&sbr=su"> Community</a>
      </td>
    </tr>
    <tr>
      <td>🎓 <a href="https://doc.dhpc.tudelft.nl/"> <img src="/docs/system/images/logo_DelftBlue.png" alt="DelftBlue Logo" style="height:60px; margin-right:0px; vertical-align:middle;"> </a> </td>
      <td>CPU/MPI jobs; high‑memory runs; large per-GPU memory needed; <i>education</i></td>
      <td>Large CPU pool; larger Nvidia GPUs (A100); dedicated scratch storage; local expert support (<a href="https://www.tudelft.nl/dhpc">DHPC</a>, ICT)</td>
      <td>Many cores, tightly‑coupled MPI, long CPU jobs, or very high memory per node; <i>education</i></td>
      <td>
        <a href="https://doc.dhpc.tudelft.nl/delftblue/Accounting-and-shares/">Access</a> • <a href="https://doc.dhpc.tudelft.nl/delftblue/DHPC-hardware/">Specs</a> •
        <a href="https://doc.dhpc.tudelft.nl/delftblue/mattermost/">Community</a>
      </td>
    </tr>
    <tr>
      <td>🎓 <a href="https://www.cs.vu.nl/das/"> <img src="/docs/system/images/logo_das6.png" alt="DAS-6 Logo" style="height:50px; margin-right:0px; vertical-align:middle;"> </a> </td>
      <td>Distributed systems research; streaming; edge/fog computing; in-network processing</td>
      <td>Multi‑site testbed; mix of GPUs (16× A4000, 4× A5000) and CPUs</td>
      <td>Cross‑cluster experiments, network‑sensitive prototypes</td>
      <td>
        <a href="mailto:das-account@cs.vu.nl">Access</a>
        • <a href="https://www.cs.vu.nl/das/">Docs</a> 
        • <a href="https://asci.school/project-das/">Project</a>
      </td>
    </tr>
    <tr>
      <td>🇳🇱 <a href="https://www.surf.nl/en/services/compute/snellius-the-national-supercomputer">
      <img src="/docs/system/images/logo_snellius.svg" alt="Snellius Logo" style="height:50px;  margin-right:0px; vertical-align:middle;"> </a></td>
      <td>National‑scale runs; larger GPU pools; cross‑institutional projects</td>
      <td>Large CPU+GPU partitions (A100 and H100); mature SURF user support; common NL platform</td>
      <td>When local capacity/queue limits progress or when collaborating with other Dutch institutions</td>
      <td>
        <a href="https://www.surf.nl/en/access-to-compute-services" target="_blank" rel="noopener">Access</a> • 
        <a href="https://servicedesk.surf.nl/wiki/spaces/WIKI/pages/30660184/Snellius" target="_blank" rel="noopener">Docs</a> •
        <a href="https://servicedesk.surf.nl/wiki/spaces/WIKI/pages/30660208/Snellius+hardware" target="_blank" rel="noopener">Specs</a>
      </td>
    </tr>
    <tr>
      <td>🇪🇺 <a href="https://www.lumi-supercomputer.eu/">
      <img src="/docs/system/images/logo_lumi.png" alt="LUMI Logo" style="height:50px; width:500px; margin-right:0px; vertical-align:middle;"> </a></td>
      <td>Euro‑scale AI/data; very large GPU jobs; benchmarking at scale</td>
      <td>Tier‑0 system with AMD MI250 GPUs (LUMI‑G); high‑performance I/O; strong EuroHPC ecosystem</td>
      <td>Beyond Snellius capacity or part of a funded EU consortium / EuroHPC allocation</td>
      <td>
      <a href="https://servicedesk.surf.nl/wiki/spaces/WIKI/pages/102837156/Obtaining+compute+time" target="_blank" rel="noopener">Access</a> •
        <a href="https://docs.lumi-supercomputer.eu/" target="_blank" rel="noopener">Docs</a>
      </td>
    </tr>
  </tbody>
</table>







### TU Delft cloud resources
For both education and research activities, TU Delft has established the [Cloud4Research program](https://tu-delft-ict-innovation.github.io/Cloud4Research/). Cloud4Research aims to facilite the use of public cloud resources, primarily Amazon AWS. At the administrative level, Cloud4Research provides AWS accounts with an initial budget. Subsequent billing can be incurred via a project code, instead of a personal credit card. At the technical level, the ICT innovation teams provides intake meetings to facilitate getting started. Please refer to the [Policies](https://tu-delft-ict-innovation.github.io/Cloud4Research/policy/) and [FAQ](https://tu-delft-ict-innovation.github.io/Cloud4Research/faq/) pages for more details.

{{% alert title="!" color=success %}}
Are you planning infrastructure proposals or strategic partnerships? Contact us to discuss collaborative opportunities and view alignment materials
{{% /alert %}} 