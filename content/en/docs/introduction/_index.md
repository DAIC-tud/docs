---
title: "The Delft AI cluster (DAIC)"
linkTitle: "The Delft AI Cluster (DAIC)"
weight: 1
description: >
  What is DAIC, what are its components, and what are the policies surrounding its use?
---

## Purpose and Benefits of HPC Systems

A High Performance Computing (HPC) cluster, is a collection of (large) computing resources, like Processors (CPUs), Graphics processors (GPUs), Memory and Storage, that are shared among a group of users.

Using multiple computers as such makes it possible to perform lengthy and resource-intense computations beyond the capabilities of a single computer, and is especially handy for modern scientific computing applications where datasets are typically large in size, models are big in parameters' size and complexity, and computations need specialized hardware (like GPUs and FPGAs). 

## Contributing departments

The Delft AI Cluster (DAIC - formerly known as INSY-HPC or just plainly HPC) is an HPC cluster that was initiated within the INSY department in 2015. Later, resources were joined with ST, collectively called _CS@Delft_, and with other departments across faculties in subsequent expansion cycles. Today, DAIC servers are organized as partitions (see [Batch Queuing System Overview ](../job_submissions/#batch-queuing-system-overview)) that corresponds to the groups contributing these resources, as can be seen in Table 1.

 DAIC has been designed based on the needs of CS@Delft from the beginning. It has grown in time to serve researchers in other TU Delft Departments but maintained the needs of CS and AI in each expansion phase (See [TU Delft clusters comparison](../../tud_clusters/)).

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
    <td><a href="https://3d.bk.tudelft.nl/"><img src="images/logo_3dgi.png" height=20 width=60/>3D Geoinformation</a></td>
    <td><a href="https://www.tudelft.nl/en/architecture-and-the-built-environment">  Faculty of Architecture and the Built Environment</a></td>
    <td>ABE/BK</td>
  </tr>
  <tr>
    <td>2</td>
    <td>asm</td>
    <td> <a href="https://www.tudelft.nl/en/ae/organisation/departments/aerospace-structures-and-materials"> <img src="images/logo_asm.png" height=20 width=70/> Aerospace Structures and Materials</a></td>
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
    <td><a href="https://www.tudelft.nl/me/over/afdelingen/cognitive-robotics-cor"><img src="images/logo_cor.png" height=20 width=70/>Cognitive Robotics</a></td>
    <td><a href="Mechanical Engineering">Faculty of Mechanical Engineering</a></td>
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

<!--------------

{{< blocks/section color="white" height="mid" >}}
{{% blocks/feature icon="fa fa-blank" title="" %}}

{{% /blocks/feature %}}
{{% blocks/feature icon="fa fa-blank" title="" %}}

{{% /blocks/feature %}}
{{% blocks/feature icon="fa fa-blank" title="" %}}

{{% /blocks/feature %}}
{{< /blocks/section >}}


---->

## Funding sources

In addition to funding received from departmental sources, DAIC has also been financially supported by the following projects and granting sources:

{{< cardpane >}}
  {{< card header="" title="" subtitle=""  >}}
  <a href="https://www.nwo.nl/en/researchprogrammes/nwo-talent-programme/projects-vidi">
	  <img src="https://bscs.umcg.nl/nl/wp-content/uploads/sites/2/2022/07/VIDI2.png" height=50 width=70/>
  </a>
  {{< /card >}}
  {{< card header="" title="" subtitle=""  >}}
  <a href="https://research-and-innovation.ec.europa.eu/funding/funding-opportunities/funding-programmes-and-open-calls/horizon-2020_en">
	  <img src="https://www.tbvi.eu/wp-content/uploads/2019/03/EU-H2020-logo.png" height=50 width=170>
  </a>
  {{< /card >}}
  {{< card header="" title="" subtitle=""  >}}
  <a href="https://www.epistemic-ai.eu/home">
	  <img src="https://lh5.googleusercontent.com/ZsNxsQsyARMx4hFHpd5aBuT_c8t1L1OXkCN3QI9x9bCjQI0alin9tLXz3jvsmautWKu5cvkDjsXDum2BPRZehOM=w16383" height=50 width=170 />
  </a>
  {{< /card >}}
{{< /cardpane >}}

## DAIC advisory board

{{< cardpane >}}
  {{< card header="Thomas Abeel" title="Department of Intelligent Systems" subtitle="Pattern Recognition and Bioinformatics group">}}
  <img src="images/thomas.abeel.png" alt="Thomas Abeel" width="500" height="600">
  {{< /card >}}
  {{< card header="Frans Oliehoek" title="Department of Intelligent Systems" subtitle="Interactive Intelligence group"  >}}
  <img src="images/frans.oliehoek.png" alt="Frans Oliehoek" width="500" height="600">
  {{< /card >}}
  {{< card header="Asterios Katsifodimos" title="Software Technology Department" subtitle="Web Informatics group"  >}}
  <img src="images/asterios.katsifodimos.png" alt="Asterios Katsifodimos" width="500" height="600">
  {{< /card >}}
{{< /cardpane >}}
