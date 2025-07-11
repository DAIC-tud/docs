---
title: "Running LLMs on DAIC"
weight: 4
description: "Guide to serving and running Ollama models on DAIC."
---

This guide shows you how to serve and use Large Language Models (LLMs) on DAIC using [Ollama](https://ollama.com/), a tool that lets you run models like [Meta's Llama models](https://ai.meta.com/llama/), [Mistral models](https://mistral.ai/models), or [HuggingFace's models](https://huggingface.co/models) for inference.

## 1. Clone the Template Repository

First, navigate to your project storage space. Then, clone the public [REIT Ollama Serving repository](https://gitlab.ewi.tudelft.nl/reit/reit-ollama-serving-template). This ensures that all generated files, models, and containers are stored in the correct location, not in your home directory.


```bash
cd /tudelft.net/staff-umbrella/<your_project_name> # Replace with your actual project path
git clone https://gitlab.ewi.tudelft.nl/reit/reit-ollama-serving-template.git
tree  reit-ollama-serving-template
```

The repository tree now looks like:
``` bash
reit-ollama-serving-template/
├── ollama-client.sbatch       # Slurm script to run a client job
├── ollama-server.sbatch       # Slurm script to run a server job
├── start-serve-client.sh      # Convenience script to start both server and client
└── template-ollama.sh         # Defines the `ollama` function
```

Finally:

```bash
# Set the PROJECT_DIR environment variable for this session.
# The helper scripts will use this path to store models and other data.
export PROJECT_DIR=$PWD
```

## 2. (Optional) Pull the Ollama Container


For simplicity, we will use the Ollama container image available on Docker Hub. You can pull it using Apptainer. This step is optional, as the `template-ollama.sh` script will build the image automatically if it's not found.


```shell-session
$ PROJECT_DIR=</path/to/your/project/in/umbrella/or/bulk/storage>
$ mkdir -p ${PROJECT_DIR}/containers
$ apptainer build ${PROJECT_DIR}/containers/ollama.sif docker://ollama/ollama
WARNING: 'nodev' mount option set on /tmp, it could be a source of failure during build process
INFO:    Starting build...
Copying blob 6574d8471920 done   | 
Copying blob 13b7e930469f done   | 
Copying blob 97ca0261c313 done   | 
Copying blob e0fa0ad9f5bd done   | 
Copying config b9d03126ef done   | 
Writing manifest to image destination
2025/06/24 12:57:55  info unpack layer: sha256:13b7e930469f6d3575a320709035c6acf6f5485a76abcf03d1b92a64c09c2476
2025/06/24 12:57:56  info unpack layer: sha256:97ca0261c3138237b4262306382193974505ab6967eec51bbfeb7908fb12b034
2025/06/24 12:57:57  info unpack layer: sha256:e0fa0ad9f5bdc7d30b05be00c3663e4076d288995657ebe622a4c721031715b6
2025/06/24 12:57:57  info unpack layer: sha256:6574d84719207f59862dad06a34eec2b332afeccf4d51f5aae16de99fd72b8a7
INFO:    Creating SIF file...
INFO:    Build complete: /tudelft.net/staff-bulk/ewi/insy/PRLab/Staff/aeahmed/ollama_tutorial/containers/ollama.sif
```

{{% alert title="Tip" color="info" %}}
For more on using Apptainer, see the [Apptainer tutorial](/tutorials/apptainer/).
{{% /alert %}}

{{% alert title="Tip" color="info" %}}
The wrapper script in the template will build the image automatically if you skip this step, but running it yourself lets you watch progress and reuse a shared cache.
{{% /alert %}}


## 3. Quick Interactive Test

1. Start an interactive GPU session:

```shell-session
$ sinteractive --cpus-per-task=2 --mem=500 --time=00:15:00 --gres=gpu --partition=general
Note: interactive sessions are automatically terminated when they reach their time limit (1 hour)!
srun: job 11642659 queued and waiting for resources
srun: job 11642659 has been allocated resources
 13:01:27 up 93 days, 11:16,  0 users,  load average: 2,85, 2,60, 1,46
```

2. Once you are allocated resources on a compute node, set your project directory, source the `template-ollama.sh` script, and run the Ollama server (from the container):

```bash
export PROJECT_DIR=</path/to/your/project/in/umbrella/or/bulk/storage>          # replace with your actual project path
source template-ollama.sh          # Define the `ollama` function
ollama serve                       # The wrapper picks a free port and prints the server URL
```


3. Keep this terminal open to monitor logs and keep the Ollama server running.

4. Open a second terminal, login to DAIC, and interact with the server (e.g., from the login node). In the example below, we run the `codellama` model

```bash
export PROJECT_DIR=</path/to/your/project/in/umbrella/or/bulk/storage> # Ensure this matches the server's PROJECT_DIR
source template-ollama.sh

ollama run codellama               # Forwards the command to the running server
```

You can check the health of the server by running:

```shell-session
$ curl http://$(cat ${PROJECT_DIR}/ollama/host.txt):$(cat ${PROJECT_DIR}/ollama/port.txt)
Ollama is running
Ollama is running
```

5. Interact with the model by typing your queries. For example, you can ask it to generate code or answer questions.

```shell-session
>>> who are you?
I am LLaMA, an AI assistant developed by Meta AI that can understand and respond to 
human input in a conversational manner. I am trained on a massive dataset of text from 
the internet and can answer questions or provide information on a wide range of topics.

>>>
```

6. Stop the server with `Ctrl‑C`in the server terminal. The `host.txt` and `port.txt` files will be cleaned up automatically.



## 4.  Production batch jobs


The template already contains working Slurm scripts.  They inherit
`PROJECT_DIR` from the environment exported by `start-serve-client.sh`.

### 4.1. Submit Server and Client Jobs

```bash
bash start-serve-client.sh  -p  </path/to/your/project/in/umbrella/or/bulk/storage> # Specify your project path. Defaults to `$PWD` if omitted.
```

This script:

1. sets `PROJECT_DIR` to the path you pass (or `$PWD` if omitted),
2. submits **`ollama-server.sbatch`**,
3. submits **`ollama-client.sbatch`** with `--dependency=after:<server‑id>`.

Watch progress:

```bash
squeue -j <server‑id>,<client‑id>
```

### 4.2. Understanding the Scripts

`ollama-server.sbatch` requests one GPU, 8 GB RAM, four CPUs, two‑hour limit,
then runs:

```bash
source template-ollama.sh
ollama serve        # Starts the server and writes host.txt / port.txt
```

`ollama-client.sbatch` waits for the server, pulls a model, and runs `test.py`:

```bash
source template-ollama.sh
ollama pull deepseek-r1:7b  # Pull the model if not already cached

```

Both scripts fall back to `$PWD` as `PROJECT_DIR` when you run them manually.

## 5. (Optional) Python Client Environment

The repository includes `test.py` for quick health checks. To set up a Python environment for client scripts, create a lightweight Conda environment once:

```bash
$ module use /opt/insy/modulefiles
module load miniconda/3.11
conda create -n ollama-client python=3.11 -y
conda activate ollama-client
pip install -r requirements.txt     
```

Now, you can run Python scripts that interact with the Ollama server. For example, you can run `test.py` to check if the server is running and responding correctly:

```bash
# Read the host and port from the files created by the server
HOST=$(cat "${PROJECT_DIR}/ollama/host.txt")
PORT=$(cat "${PROJECT_DIR}/ollama/port.txt")

python3 test.py --host "$HOST" --port "$PORT" # Run a Python client script
```

{{% alert title="Tip" color="info" %}}
Include `conda activate ollama-client` near the top of `ollama-client.sbatch` if you plan to run Python code there.
{{% /alert %}}


Alternatively, you can use [`uv`](https://docs.astral.sh/uv/) or [`pixi`](https://pixi.sh/latest/) if you prefer.



## 6. Best Practices

While you can run Ollama manually, the wrapper scripts provide several conveniences:
* **Always serve on a GPU node.** The wrapper prints an error if you try to
  serve from a login node.
* **Client jobs don’t need `--nv`.** The wrapper omits it automatically when
  no GPU is detected, eliminating noisy warnings.
* **Model cache is project‑scoped.**  All blobs land in
  `$PROJECT_DIR/ollama/models`, so they don’t consume `$HOME` quota.
* **Image builds use `/tmp`.**  The wrapper builds via a local cache to avoid
  NFS root‑squash errors.
* **Automatic cleanup.** The wrapper cleans up `host.txt` and `port.txt` files after the server stops, so you can tell if you have a server up and running.



## 7. Troubleshooting

| Symptom                                     | Fix                                                                                    |
| ------------------------------------------- | -------------------------------------------------------------------------------------- |
| `host.txt / port.txt not found`             | Start the server first: `ollama serve` (interactive) or submit `ollama-server.sbatch`. |
| `Could not find any nv files on this host!` | Safe to ignore; client ran on CPU.                                                     |
| Build fails with `operation not permitted`  | Ensure the wrapper’s `/tmp` build cache patch is in place, or add `--disable-cache`.   |


