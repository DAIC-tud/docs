---
title: "Introduction"
weight: 1
description: >
  What are the foundational components of DAIC?
---

DAIC (formerly known as INSY-HPC or just plainly HPC) is a TU Delft High Performance Computing (HPC) cluster consisting of Linux compute servers with a lot of processing power and memory for running large, long or GPU-enabled jobs. DAIC was initiated within the INSY department in 2015, and later, resources were joined with ST (both from EWI), and with other departments across TU Delft faculties (TNW, TPM, 3mE and CiTG). The cluster is available (only) to users from the participating departments, and access can be arranged through the department's contact persons (see [Access and accounts](/docs/policies#access-and-accounts)).

### What is an HPC cluster?
{{< figure src="/img/DAIC_partitions.png" caption="DAIC partitions and access/usage best practices" ref="fig:daic_partitions" width="750px">}}

A High Performance Computing (HPC) cluster, is a collection of (large) computing resources, like Processors (CPUs), Graphics processors (GPUs), Memory and Storage, that are shared among a group of users. Using multiple computers as such makes it possible to perform lengthy and resource-intense computations beyond the capabilities of a single computer, and is especially handy for modern scientific computing applications where datasets are typically large in size, models are big in parameters' size and complexity, and computations need specialized hardware (like GPUs and FPGAs). 

## Contributing departments
The Delft AI Cluster (DAIC - formerly known as INSY-HPC or just plainly HPC) is an HPC cluster that was initiated within the INSY department in 2015. Later, resources were joined with ST, collectively called _CS@Delft_, and with other departments across faculties in subsequent expansion cycles. Today, DAIC servers are organized as [partitions](/docs/manual/job-submission/partitions/) which correspond to the groups contributing these resources, as can be seen in Table 1.

 DAIC has been designed based on the needs of CS@Delft from the beginning. It has grown in time to serve researchers in other TU Delft Departments but maintained the needs of CS and AI in each expansion phase (See [TU Delft clusters comparison](/docs/introduction#tud-clusters)).

<table>
<caption> Table 1: Current partitions within DAIC and contributing TU Delft departments/faculties.
</caption>
<thead>
  <tr>
    <th>I</th>
    <th>DAIC partition</th>
    <th>Contributor</th>
    <th>Faculty</th>
    <th>Faculty abbreviation (English/Dutch)</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>1</td>
    <td>3dgi</td>
    <td><a href="https://3d.bk.tudelft.nl/"><img src="/img/logo_3dgi.png" height=20 width=60/>3D Geoinformation</a></td>
    <td><a href="https://www.tudelft.nl/en/architecture-and-the-built-environment">  Faculty of Architecture and the Built Environment</a></td>
    <td>ABE/BK</td>
  </tr>
  <tr>
    <td>2</td>
    <td>asm</td>
    <td> <a href="https://www.tudelft.nl/en/ae/organisation/departments/aerospace-structures-and-materials"> <img src="/img/logo_asm.png" height=20 width=70/> Aerospace Structures and Materials</a></td>
    <td><a href="https://www.tudelft.nl/en/ae">Faculty of Aerospace Engineering</a></td>
    <td>AE/LR</td>
  </tr>
  <tr>
    <td>3</td>
    <td>imphys</td>
    <td><a href="https://www.tudelft.nl/en/faculty-of-applied-sciences/about-faculty/departments/imphys">Imaging Physics</a></td>
    <td><a href="https://www.tudelft.nl/en/faculty-of-applied-sciences">Faculty of Applied Sciences</a></td>
    <td>AS/TNW</td>
  </tr>
  <tr>
    <td>4</td>
    <td>cor</td>
    <td><a href="https://www.tudelft.nl/me/over/afdelingen/cognitive-robotics-cor"><img src="/img/logo_cor.png" height=20 width=70/>Cognitive Robotics</a></td>
    <td><a href="https://www.tudelft.nl/en/me">Faculty of Mechanical Engineering</a></td>
    <td>ME</td>
  </tr>
  <tr>
    <td>5</td>
    <td>grs</td>
    <td><a href="https://www.tudelft.nl/citg/over-faculteit/afdelingen/geoscience-remote-sensing">Geoscience &amp; Remote Sensing</a></td>
    <td><a href="https://www.tudelft.nl/en/ceg">Faculty Of Civil Engineering and Geosciences</a></td>
    <td>CEG/CiTG</td>
  </tr>
  <tr>
    <td>6</td>
    <td>influence</td>
    <td rowspan="3"><a href="https://www.tudelft.nl/en/eemcs/the-faculty/departments/intelligent-systems">Intelligent Systems</a></td>
    <td rowspan="5"><a href="https://www.tudelft.nl/en/eemcs">Faculty of Electrical Engineering, Mathematics &amp; Computer Science</a></td>
    <td rowspan="5">EEMCS/EWI</td>
  </tr>
  <tr>
    
  </tr>
  <tr>
    <td>7</td>
    <td>insy</td>
  </tr>
  <tr>
    <td>8</td>
    <td>st</td>
    <td rowspan="2"><a href="https://www.tudelft.nl/ewi/over-de-faculteit/afdelingen/software-technology">Software Technology</a></td>
  </tr>

</tbody>
</table>

## Funding sources
In addition to funding received from departmental sources, DAIC has also been financially supported by the following projects and granting sources:

{{< cardpane >}}
  {{< card header="NWO" title="" subtitle=""  >}}
  <a href="https://www.nwo.nl/en/researchprogrammes/nwo-talent-programme/projects-vidi">
	  <img src="https://bscs.umcg.nl/nl/wp-content/uploads/sites/2/2022/07/VIDI2.png" height=80 width=100/>
  </a>
  {{< /card >}}
  {{< card header="Horizon 2020" title="" subtitle=""  >}}
  <a href="https://research-and-innovation.ec.europa.eu/funding/funding-opportunities/funding-programmes-and-open-calls/horizon-2020_en">
	  <img src="https://www.tbvi.eu/wp-content/uploads/2019/03/EU-H2020-logo.png"  >
  </a>
  {{< /card >}}
  
{{< /cardpane >}}

{{< cardpane >}}
{{< card header="Epistemic AI" title="" subtitle=""  >}}
  <a href="https://www.epistemic-ai.eu/home">
	  <img src="/img/logo-epistemic-ai.png"  />
  </a>
  {{< /card >}}

   {{< card header="MMLL" title="" subtitle=""  >}}
    <a href="">
	    <img src="images/funders_MMLLlogo.png" height=50 width=170/>
    </a>
  {{< /card >}}
{{< /cardpane>}}


{{< cardpane >}}
  {{< card header="Booking.com" title="" subtitle=""  >}}
  <a href="https://www.booking.com/">
	  <img src="https://eur03.safelinks.protection.outlook.com/?url=https%3A%2F%2Fassets-global.website-files.com%2F658f265af26f3187eb6b03b0%2F65fa9bd046a7b0dba64008fe_1280px-Booking.com_logo.svg-p-500.png&data=05%7C02%7CA.E.Ahmed%40tudelft.nl%7C5897e06bc0cf49e02a5b08dc7a51e22b%7C096e524d692940308cd38ab42de0887b%7C0%7C0%7C638519739312808690%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C0%7C%7C%7C&sdata=KacApWStt6AIp2SeMlR2MqzHxoVuou7aJZuS7%2BwjXpY%3D&reserved=0" height=50 width=170/>
  </a>
  {{< /card >}}

 {{< card header="Others" title="" subtitle=""  >}}
    <a href="https://daic.tudelft.nl/docs/introduction/#contributing-departments">
	    Contributing departments' funding
    </a>
  {{< /card >}}
 
{{< /cardpane >}}




## Advisory board
{{< cardpane >}}
  {{< card header="Thomas Abeel" title="Department of Intelligent Systems" subtitle="Pattern Recognition and Bioinformatics group">}}
  <img src="/img/thomas.abeel.png" alt="Thomas Abeel" width="500" height="600">
  {{< /card >}}
  {{< card header="Frans Oliehoek" title="Department of Intelligent Systems" subtitle="Interactive Intelligence group">}}

  <img src="/img/frans.oliehoek.png" alt="Frans Oliehoek" width="500" height="600">
  {{< /card >}}
  {{< card header="Asterios Katsifodimos" title="Software Technology Department" subtitle="Web Informatics group">}}
  <img src="/img/asterios.katsifodimos.png" alt="Asterios Katsifodimos" width="500" height="600">
  {{< /card >}}
{{< /cardpane >}}


## Scientific impact
Since 2015, DAIC has facilitated more than 2000 scientific outputs from the various DAIC-participating departments:

{{% alert title="Note" color="info" %}}
The compilation of the following list is done retrospectively by the Data Insights team and/or is based on self-reporting by individual researchers. As a result, it may not be exhaustive nor complete. 
  * If your paper is not in this list, then please post its details to the [ScientificOutput MatterMost channel](https://mattermost.tudelft.nl/daic/channels/scientificoutput); and make sure to acknowledge and cite us as shown in the Acknowledgement section.
{{% /alert %}}

|                 | Article | Conference/Meeting contribution | Book/Book chapter/Book editing | Dissertation (TU Delft) | Abstract | Other | Editorial | Patent | **Grand Total** |
| --------------- | --------------------- | -------------------- | ------------------------ | ---------------- | --------- | -------------- | ----------------------------- | ------------------------- | --------------- |
| **Grand Total** | 1067               | 854              | 123                    | 99           | 69     | 32         | 29                         | 8                    | **2281**        |

These outputs span a wide range of application areas, with titles reflecting an emphasis on data analysis and machine learning:

{{< figure src="/img/common_words_outputs.png" caption="Wordcloud of the most common words in titles of Scientific outputs produced via DAIC" ref="fig:daic_wordcloud">}}

{{% alert title="Reference" color="info" %}}

The table and wordcloud provided here are based on retrospective retrieval of all DAIC users' scientific outputs between 2015-2023 from TU Delft's Pure database.
The data has been generated by the [Strategic Development – Data Insights team](https://www.youtube.com/watch?v=RIq_-TEIkQI).

{{% /alert %}}

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
