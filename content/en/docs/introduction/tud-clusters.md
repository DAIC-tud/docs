---
title: "TU Delft clusters comparison"
weight: 2
description: >
  How does DAIC compare to other TU Delft cluster?
---

## Cluster comparison
### TU Delft clusters
DAIC is one of several clusters accessible to TU Delft CS researchers (and their collaborators). The table below gives a comparison between these in terms of use case, eligible users, and other characteristics.

<table>
<thead>
  <tr>
    <th></th>
    <th>DAIC</th>
    <th>DelftBlue</th>
    <th>DAS</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>Primary use cases</td>
    <td>Research, especially in AI</td>
    <td>Research &amp; Education</td>
    <td>Distributed systems research, streaming applications, edge and fog computing, in-network processing, and complex security and trust policies, Machine learning research, ...</td>
  </tr>
  <tr>
    <td>Contributors</td>
    <td>Certain groups within TU Delft (see <a href="#contributing-departments">Contributing departments</a>)</td>
    <td>All TU Delft faculties</td>
    <td>Multiple universities &amp; SURF</td>
  </tr>
  <tr>
    <td>Eligible users</td>
    <td>
    <ul>
      <li>Faculty, PhD students, and researchers from contributing departments </li>
      <li>MSc and BSc students (if recommended by a professor) are provided limited access  </li>
    </ul>
    </td>
    <td>All TU Delft affiliates</td>
    <td>  
    <ul>
      <li> Faculty and PhD students who are either members of the ASCI research school or the ASCI partner universities </li>
      <li> <a href="https://www.astron.nl/">ASTRON</a> employees </li>
      <li> <a href="https://www.esciencecenter.nl/">NLeSC</a> employees </li>
      <li> Master students (if recommended by a professor) are provided limited access </li>
    </ul>
    </td>
  </tr>
  <tr>
    <td>Website</td>
    <td><a href="https://doc.daic.tudelft.nl/">DAIC documentation</a></td>
    <td><a href="https://doc.dhpc.tudelft.nl/delftblue/">DelftBlue Documentation</a></td>
    <td><a href="https://asci.tudelft.nl/project-das/">DAS Documentation</a></td>
  </tr>
  <tr>
    <td>Contact info</td>
    <td><a href="https://mattermost.tudelft.nl/signup_user_complete/?id=cb1k3t6ytpfjbf7r397395axyc&md=link&sbr=su"> DAIC community</a></td>
    <td><a href="https://tudelft.topdesk.net/tas/public/ssp/content/detail/service?unid=b7e2b7b46ac94cf688c21761aa324fc1">DHPC team</a></td>
    <td><a href="mailto:das-account@cs.vu.nl">DAS admin</a></td>
  </tr>
  <tr>
    <td>Request account</td>
    <td><a href="/docs/policies#access-accounts/"> Access and accounts </a></td>
    <td><a href="https://doc.dhpc.tudelft.nl/delftblue/Accounting-and-shares/">Get an account</a></td>
    <td><a href="mailto:das-account@cs.vu.nl">Email DAS admin</a> with details like user's affiliation and the planned purpose of the account.</td>
  </tr>
  <tr>
    <td>Getting started</td>
    <td><a href="/tutorials/quickstart/">Quickstart</a></td>
    <td><a href="https://doc.dhpc.tudelft.nl/delftblue/crash-course/">Crash course</a></td>
    <td></td>
  </tr>
  <tr>
    <td>Hardware</td>
    <td><a href="/docs/system">System specifications</a></td>
    <td><a href="https://doc.dhpc.tudelft.nl/delftblue/DHPC-hardware/">DHPC hardware</a></td>
    <td> Head node +
    <ul>
      <li> 16 x FAT nodes (Lenovo SR665, dual socket, 2x16 core, 128 GB memory, 1xA4000) </li>
      <li> 4 x GPU nodes (Lenovo SR665, dual socket, 2x16 core, 128 GB memory, 1xA5000) </li>
    </ul>
    </td>
  </tr>
  <tr>
    <td>Software stack</td>
    <td><a href="/docs/manual/software/">Software</a></td>
    <td><a href="https://doc.dhpc.tudelft.nl/delftblue/DHPC-modules/">DHPC modules</a></td>
    <td>Base OS: Rocky Linux, OpenHPC, Slurm Workload Manager</td>
  </tr>
  <tr>
    <td>Data storage</td>
    <td><a href="/docs/system#storage">Storage</a></td>
    <td><a href="https://doc.dhpc.tudelft.nl/delftblue/DHPC-hardware/#storage">Storage</a></td>
    <td>Storage: 128 TB (RAID6) </td>
  </tr>
  <tr>
    <td>Access to TU Delft Network storage</td>
    <td>✓</td>
    <td>Only in login nodes</td>
    <td> Not supported </td>
  </tr>
  <tr>
    <td>Sharing data in collaboration</td>
    <td>✓</td>
    <td>✗</td>
    <td></td>
  </tr>
  <tr>
    <td>Has GPUs?</td>
    <td>✓</td>
    <td>✓</td>
    <td>✓</td>
  </tr>
  <tr>
    <td>Cost of use</td>
    <td>Contribution towards hardware purchase</td>
    <td></td>
    <td>-</td>
  </tr>
</tbody>
</table>

### SURF clusters
[SURF](https://www.surf.nl/en), the collaborative organization for IT in Dutch education and research, has installed and is currently operating the Dutch National supercomputer, [Snellius](https://www.surf.nl/en/dutch-national-supercomputer-snellius), which houses 144 40GB A100 GPUs as of Q3 2021 (36 gcn nodes x 4 A100 GPUs/node = 144 A100 GPUs total) with other specs detailed in the [Snellius hardware and file systems wiki](https://servicedesk.surf.nl/wiki/display/WIKI/Snellius+hardware+and+file+systems). 

SURF also operates other clusters like [Spider](https://servicedesk.surf.nl/wiki/display/WIKI/Spider+-+Description) for processing large structured data sets, and [ODISSEI Secure Supercomputer (OSSC)](https://servicedesk.surf.nl/wiki/display/WIKI/ODISSEI+Secure+Supercomputer) for large-scale analyses of highly-sensitive data. For an overview of SURF clusters, see the [SURF wiki](https://servicedesk.surf.nl/wiki/).

TU Delft researchers in TBM and CITG already have direct and easy access to the compute power and data services of SURF, while members of other faculties need to apply for access as detailed in [SURF's guide to Apply for access to compute services](https://www.surf.nl/en/research-it/apply-for-access-to-compute-services).

### TU Delft cloud resources
For both education and research activities, TU Delft has established the [Cloud4Research program](https://tu-delft-ict-innovation.github.io/Cloud4Research/). Cloud4Research aims to facilite the use of public cloud resources, primarily Amazon AWS. At the administrative level, Cloud4Research provides AWS accounts with an initial budget. Subsequent billing can be incurred via a project code, instead of a personal credit card. At the technical level, the ICT innovation teams provides intake meetings to facilitate getting started. Please refer to the [Policies](https://tu-delft-ict-innovation.github.io/Cloud4Research/policy/) and [FAQ](https://tu-delft-ict-innovation.github.io/Cloud4Research/faq/) pages for more details.
