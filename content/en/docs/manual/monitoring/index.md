---
title: Monitoring
description: Tools to monitor your jobs.
weight: 60

---

<ul>
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
  <li>
      <summary>{{< external-link "https://login.daic.tudelft.nl/" "DAIC status check (Access from TUD network)" >}} </summary>
      A brief overview of:
      <ul>
        <li>Login nodes status</li>
        <li>Compute nodes status </li>
        <li>Summary graphs</li>
      </ul>
  </li>
  </li>
</ul>







