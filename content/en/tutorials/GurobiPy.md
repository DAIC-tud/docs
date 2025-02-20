---
title: "Installing and Using GurobiPy on DAIC"
linkTitle: "GurobiPy"
weight: 3
description: "Guide to installing and configuring GurobiPy on DAIC."
---


## Installation

You can install GurobiPy using `pip` or `conda` in a virtual environment. Please refer to the [Managing Environment](docs/manual/software/installing-software/#managing-environments) manual for more information on using `pip` and `conda`.

```bash
# Using pip (in a virtual environment or with --user)
pip install gurobipy

# Or using Conda (in a virtual environment)
conda install gurobi::gurobi 
```

## Using GurobiPy

To use GurobiPy, you need to import the `gurobipy` module in your Python script. Here is an example script that creates a Gurobi model and solves it:

{{< cardpane >}}
{{< card header="tst_gurobi.py" code=true lang=python >}}
import gurobipy as gp
m = gp.Model()
m.optimize()
{{< /card >}}
{{< /cardpane >}}

You can run the script using the following command:


```shell-session
$ sinteractive --ntasks=2 --mem=2G --time=00:05:00
$ python tst_gurobi.py 
Restricted license - for non-production use only - expires 2026-11-23
Gurobi Optimizer version 12.0.1 build v12.0.1rc0 (linux64 - "Red Hat Enterprise Linux")

CPU model: AMD EPYC 7543 32-Core Processor, instruction set [SSE2|AVX|AVX2]
Thread count: 64 physical cores, 64 logical processors, using up to 32 threads

Optimize a model with 0 rows, 0 columns and 0 nonzeros
Model fingerprint: 0xf9715da1
Coefficient statistics:
  Matrix range     [0e+00, 0e+00]
  Objective range  [0e+00, 0e+00]
  Bounds range     [0e+00, 0e+00]
  RHS range        [0e+00, 0e+00]
Presolve time: 0.01s
Presolve: All rows and columns removed
Iteration    Objective       Primal Inf.    Dual Inf.      Time
       0    0.0000000e+00   0.000000e+00   0.000000e+00      0s

Solved in 0 iterations and 0.01 seconds (0.00 work units)
Optimal objective  0.000000000e+00
```

## Configuring the License

If needed, and since DAIC uses a remote license server, you can specify the license settings in your script:

```python
import gurobipy as gp

connection_params = {
    "TokenServer": "flexserv-x1.tudelft.nl",
    "TSPort": "27099"
}

with gp.Env(params=connection_params) as env:
    with gp.Model(env=env) as model:
        try:
            populate_and_solve(model)
        except:
            # Add appropriate error handling here.
            raise
```

