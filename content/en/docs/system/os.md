---
title: "Operating system"
weight: 1
description: >
  Overview of the DAIC operating system and its implications for available software.
---


{{% pageinfo %}}
At present, DAIC and [DelftBlue](https://doc.dhpc.tudelft.nl/delftblue) use different software stacks. This includes differences in the operating system (CentOS 7 for DAIC _vs._ Red Hat Enterprise Linux 8 for DelftBlue) and, consequently, the available modules. 

Be mindful that code or environments developed on one system may not run identically on the other. Check the [DelftBlue modules](https://doc.dhpc.tudelft.nl/delftblue/DHPC-modules/) and [DAIC software](/docs/manual/software) pages to avoid portability issues.

{{% /pageinfo %}}

## Operating system

DAIC runs the {{< external-link "https://en.wikipedia.org/wiki/Red_Hat_Enterprise_Linux" "Red Hat Enterprise Linux 7" >}} distribution. Most common software—such as programming languages, libraries, and development tools—is installed on the nodes (see [Available software](/docs/manual/software/available-software)).

However, niche or recently released packages may be missing. If your work depends on a state-of-the-art program not yet available for Red Hat 7, you’ll need to install it manually. See [Installing software](/docs/manual/software/installing-software/) for instructions.

