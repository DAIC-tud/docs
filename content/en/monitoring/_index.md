---
title: Monitoring
menu:
  main:
    weight: 60
---




<ul>
  <li>
    <details>
      <summary>{{< external-link "https://login.hpc.tudelft.nl/protected/slurmtop.txt" "slurmtop (login required)" >}}</summary>
      <code>slurmtop</code> is available as both a cluster command, and as a webpage. Both the command and webpage  display the following tables:
      <ul>
        <li>Summary on resources allocations in the <code>general</code> partition in: <code>Allocated/</li>Idle/Other/Total</code> (in the command line version) or <code>Total/allocation</code> (in the webpage version) format
        <li>Per-node details on status and resources allocations in the <code>general</code> partition </li>
        <li>Normalized and Effective per-account resource usage information </li>
        <li>Resource usage and fairshare information for the top 10 cluster users (in terms of </li>Normalized usage)
        <li>Details of jobs in the cluster, sorted by priority and jobID </li>
      </ul>
    </details>
  </li>
  <li>{{< external-link "https://login.hpc.tudelft.nl/protected/job_efficiency.cgi" "SlurmEff (login required)" >}}
  </li>
  <li>
    {{< external-link "https://login.hpc.tudelft.nl/cacti/graph_view.php" "Cluster Monitoring Graphs" >}}
  </li>
  <li>
    <details>
      <summary>Login nodes status </summary>
      {{< tableiframe "https://login.hpc.tudelft.nl/" "top: -10px; left: -10px; width: 500px; height: 200px;" "width: 562px; height: 161px;" >}}
    </details>
  </li>
  <li>
    <details>
      <summary>Compute nodes status</summary>
      {{< tableiframe "https://login.hpc.tudelft.nl/" "top: -10px; left: -10px; width: 500px; height: 200px;" "width: 576px; height: 1785px;" >}}
  </details>
  </li>
  <li>
    <details>
      <summary>Summary graphs</summary>
      {{< tableiframe "https://login.hpc.tudelft.nl/" "top: -10px; left: -10px; width: 500px; height: 200px;" "width: 1240px; height: 1816px;" >}}
  </details>
  </li>
</ul>







