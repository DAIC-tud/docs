---
title: "Help resources"
linkTitle: "Help resources"
weight: 1
description: >
    Help yourself resources.
---

## Cluster monitoring
My jobs are not starting, is the cluster busy? The following links are resources that monitor the current state of DAIC.

<ul>
  <li>
      <summary>{{< external-link "https://login.daic.tudelft.nl/" "DAIC status check (Access from TUD network)" >}} </summary>
      A brief overview of:
      <ul>
        <li>Login nodes status</li>
        <li>Compute nodes status </li>
        <li>Summary graphs</li>
      </ul>
  </li>
  <li> 
    <summary>{{< external-link "https://login.daic.tudelft.nl/protected/slurmtop.txt" "slurmtop (login required)" >}}</summary> 
    <code>slurmtop</code> is available as both a cluster command, and as a webpage. Both the command and webpage  display the following tables:
      <ul>
        <li>Summary on resources allocations in the <code>general</code> partition in: <code>Allocated/</li>Idle/Other/Total</code> (in the command line version) or <code>Total/allocation</code> (in the webpage version) format
        <li>Per-node details on status and resources allocations in the <code>general</code> partition </li>
        <li>Normalized and Effective per-account resource usage information </li>
        <li>Resource usage and fairshare information for the top 10 cluster users (in terms of </li>Normalized usage)
        <li>Details of jobs in the cluster, sorted by priority and jobID </li>
      </ul>
    
  </li>
  <li>
      <summary>{{< external-link "https://login.daic.tudelft.nl/protected/job_efficiency.cgi" "SlurmEff (login required)" >}}</summary>
      A summary of efficiency statistics of your own jobs. Statistics are calculated on the basis of requested vs consumed resources. 
  </li>
  <li>{{< external-link "https://login.daic.tudelft.nl/cacti/graph_view.php" "Cluster Monitoring Graphs" >}}
  </li>

  </li>
</ul>


<!--add blocks of content here to add more sections to the community page -->
## Group-specific resources 
In line with the steps in [What to do in case of problems](../docs/intro_daic/user_agreement#what-to-do-in-case-of-problems), the following links are group-specific resources that you may find relevant:

- [x] {{< external-link "https://login.daic.tudelft.nl/" "Main DAIC landing page" >}}  
- [x] {{< external-link "https://wiki.tudelft.nl/bin/view/Research/InsyCluster/WebHome" "Central wiki" >}}
- [ ] {{< external-link "https://gitlab.tudelft.nl/pattern-recognition-and-bioinformatics/wiki/-/wikis/HPC-quickstart-guide" "PRB wiki">}} <!--from Ruud & Tom V) -->
- [ ] {{< external-link "https://gitlab.tudelft.nl/delft-bioinformatics-lab/wiki/-/wikis/Cluster" "DBL wiki" >}} <!--from Yasin -->
- [ ] {{< external-link "https://qiweb.tudelft.nl/sysman/awi2insy.html" "Imphys docs" >}} <!--(https://qiweb.tudelft.nl/sysman/hpc_servers.html; https://qiweb.tudelft.nl/sysman/hpc/hpc.html from Ronald) -->
- [ ] {{< external-link "https://github.com/oliehoek-research/organization/tree/master/howto" "Influence github resources" >}} <!--(from Frans O) -->
- [ ] {{< external-link "https://docs.google.com/document/d/1FnUzmHchHdZi4Iw3UDE-2sPrG_RF-qqIilKLDRXMHyo/edit#heading=h.jjiiwty148c2" "WIS Google doc" >}} <!-- from Ziyu, WIS -->


## Linux support
* Linux [Q&A Portal](https://linux.ewi.tudelft.nl/): This page aims to be a hub for sharing knowledge, seeking support and prioritizing community issues through upvoting.
* Linux [Mattermost channel](https://mattermost.tudelft.nl/linux-user-group/): for daily news, light-hearted conversations, urgent requests, and connecting        with peers.
        

<!-- 
Additional resources:
* Walk-in sessions
* Training materials
* Tutorials and or external resources

Style guide:
https://www.kubeflow.org/docs/about/style-guide/

Interesting documentations:
https://support.ceci-hpc.be/doc/index.html
-->

## External resources:
- {{< external-link "https://carpentries-incubator.github.io/hpc-intro/" "Introduction to High-Performance Computing" >}}
- {{< external-link "https://hpc-carpentry.github.io/hpc-shell/" "Introduction to Using the Shell in a High-Performance Computing Context" >}}
- {{< external-link "https://swcarpentry.github.io/shell-novice/" "The Unix Shell" >}}
- {{< external-link "https://www.hpc-carpentry.org/community-lessons/#hpc-carpentry" "HPC carpentry lessons" >}}
- {{< external-link "https://software-carpentry.org/lessons/" "Other software carpentry lessons" >}}
- {{< external-link "https://datacarpentry.org/lessons/" "Data carpentry lessons" >}}