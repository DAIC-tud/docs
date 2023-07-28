
---
title: "TU Delft clusters comparison"
weight: 10
menu:
  main:
    weight: 10
---

## TU Delft clusters

DAIC is one of several clusters accessible to TU Delft researchers (and their collaborators). The table below gives a comparison between these in terms of use case, eligible users, and other characteristics.


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
    <td>Certain groups within TU Delft (see <a href="http://localhost:1313/DAICdocumentation/docs/intro_daic/_index.md#brief-history-of-daic">Brief history of DAIC</a>)</td>
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
    <td><a href="https://aeaahmed.pages.ewi.tudelft.nl/DAICdocumentation/">DAIC documentation</a></td>
    <td><a href="https://doc.dhpc.tudelft.nl/delftblue/">DelftBlue Documentation</a></td>
    <td><a href="https://asci.tudelft.nl/project-das/">DAS Documentation</a></td>
  </tr>
  <tr>
    <td>Contact info</td>
    <td></td>
    <td><a href="https://tudelft.topdesk.net/tas/public/ssp/content/detail/service?unid=b7e2b7b46ac94cf688c21761aa324fc1">DHPC team</a></td>
    <td><a href="mailto:das-account@cs.vu.nl">DAS admin</a></td>
  </tr>
  <tr>
    <td>Request account</td>
    <td></td>
    <td><a href="https://doc.dhpc.tudelft.nl/delftblue/Accounting-and-shares/">Get an account</a></td>
    <td><a href="mailto:das-account@cs.vu.nl">Email DAS admin</a> with details like user's affiliation and the planned purpose of the account.</td>
  </tr>
  <tr>
    <td>Getting started</td>
    <td><a href="http://localhost:1313/DAICdocumentation/quickstart/_index.md#quick-start">Quick start</a></td>
    <td><a href="https://doc.dhpc.tudelft.nl/delftblue/crash-course/">Crash course</a></td>
    <td></td>
  </tr>
  <tr>
    <td>Hardware</td>
    <td><a href="http://localhost:1313/DAICdocumentation/docs/intro_daic/daic_architecture.md#hardware-infrastructure">Hardware infrastructure</a></td>
    <td><a href="https://doc.dhpc.tudelft.nl/delftblue/DHPC-hardware/">DHPC hardware</a></td>
    <td> Head node +
    <ul>
      <li> 6 FAT node Lenovo SR665, dual socket, 2x16core, 128 GB memory, + A4000 </li>
      <li> 4 GPU node Lenovo SR665, dual socket, 2x16core, 128 GB memory + A5000 </li>
    </ul>
    </td>
  </tr>
  <tr>
    <td>Software stack</td>
    <td><a href="http://localhost:1313/DAICdocumentation/docs/software_environment/_index.md#software-environment">Software environment</a></td>
    <td><a href="https://doc.dhpc.tudelft.nl/delftblue/DHPC-modules/">DHPC modules</a></td>
    <td>Base OS: Rocky Linux, OpenHPC, Slurm Workload Manager</td>
  </tr>
  <tr>
    <td>Data storage</td>
    <td><a href="http://localhost:1313/DAICdocumentation/docs/filesystem/_index.md#filesystem-and-storage">Filesystem &amp; storage</a></td>
    <td><a href="https://doc.dhpc.tudelft.nl/delftblue/DHPC-hardware/#storage">Storage</a></td>
    <td>Storage: 128 TB (RAID6) </td>
  </tr>
  <tr>
    <td>Access to TU Delft Network storage</td>
    <td>✓</td>
    <td>Only in login nodes</td>
    <td></td>
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


## Other clusters

In this website of [Snellius](https://www.surf.nl/en/dutch-national-supercomputer-snellius), there is a tab called "technical specifications", where you can find the number GPU they have is 144 A100 GPU.

More details information can be found [here](https://servicedesk.surf.nl/wiki/display/WIKI/Snellius+hardware+and+file+systems), where they state the A100 GPU exists from Q3 2021. The details is in section "Phase 1 (Q3 2021)", the "Accelerator" column, there are 36 nodes, and each node has 4 A100 GPU = 144 GPUs. Note the type of A100 they have is the 40 GB memory version, not the 80 GB memory version.

## SURF
https://servicedesk.surf.nl/wiki/

## TU Delft cloud resources

For both education and research activities, TU Delft has established the [Cloud4Research program](https://tu-delft-ict-innovation.github.io/Cloud4Research/). Cloud4Research aims to facilite the use of public cloud resources, primarily Amazon AWS. At the administrative level, Cloud4Research provides AWS accounts with an initial budget. Subsequent billing can be incurred via a project code, instead of a personal credit card. At the technical level, the ICT innovation teams provides intake meetings to facilitate getting started. Please refer to the [Policies](https://tu-delft-ict-innovation.github.io/Cloud4Research/policy/) and [FAQ](https://tu-delft-ict-innovation.github.io/Cloud4Research/faq/) pages for more details.