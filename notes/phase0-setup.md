# Phase 0 — Setup & Environment Notes

---

## Lesson 0.1 — Python Environment Setup

**Date:** 2026-06-19
**Repo cross-reference:** `phases/00-setup-and-tooling/`

### Concept

A virtual environment is an isolated folder that holds Python + all libraries for one project only — same idea as `node_modules` in a JS project. Without it, libraries install globally and eventually conflict across projects.

### Key commands (Windows)

```bash
# Create the virtual environment
python -m venv venv
# venv (first) = the built-in Python module that creates environments
# venv (second) = name of the folder it creates

# Activate it — tells terminal to use THIS project's Python/pip
venv\Scripts\activate
# You'll see (venv) at the start of your prompt — that's the confirmation

# Install core libraries
pip install numpy matplotlib jupyter ipykernel

# To freeze the package version, so that when installing it in future will make the others to use the same version
pip freeze > requirements.txt
```

### What each library does

- `numpy` — fast array/matrix math. Our only "calculator" tool — used in every phase
- `matplotlib` — plotting and graphing. Lets us visualize training, loss curves, etc.
- `jupyter` — notebook environment. Industry standard for exploration and sharing ML work
- `ipykernel` — lets VS Code talk to Jupyter notebooks inside the editor

### Verified versions (Development machine)

- Python 3.14.3
- numpy 2.5.0
- matplotlib 3.11.0
- jupyter ✓

### The `# %%` cell marker

`#` = Python comment, ignored at runtime. But VS Code's Python extension treats `# %%` as a cell boundary — splits the file into runnable sections like Jupyter, while keeping it a clean `.py` file. Same interactivity, clean git diffs, runs as a normal script in production.

### Tool workflow (industry standard)

- **VS Code + `# %%`** — primary tool for writing and running lesson code
- **Jupyter** — exploration, research, sharing results (introduced Phase 2)
- **Google Colab** — cloud GPU access for heavy training (introduced Phase 3)

### Gotchas

- Python 3.14 is bleeding edge — may cause issues with some ML libraries in later phases (PyTorch etc.). Will switch to 3.11 if install errors appear, not before.
- Always activate venv before working (`venv\Scripts\activate`). If `(venv)` isn't showing, you're installing into global Python.
- `deactivate` command exits the environment. Closing the terminal also exits it.

### Git commit

`Phase 0.1: virtual environment setup, numpy 2.5.0, matplotlib 3.11.0, jupyter installed`

---

## Lesson 0.2 — VS Code Setup

**Date:** 2026-06-19
**Repo cross-reference:** `phases/00-setup-and-tooling/`

### Extensions installed

- **Python** (Microsoft) — core Python support, IntelliSense, debugging
- **Pylance** (Microsoft) — better autocomplete and type checking, installs alongside Python
- **Python Debugger** (Microsoft) — step-through debugging
- **Jupyter** (Microsoft) — runs `.ipynb` files and `# %%` cells inside VS Code
- **GitLens** (GitKraken) — inline git history, blame, authorship per line

### Pointing VS Code to venv

`Ctrl + Shift + P` → `Python: Select Interpreter` → pick the one with `venv` in the path:

```
Python 3.14.3 ('venv': venv) .\venv\Scripts\python.exe
```

Confirmed in top-right corner of VS Code — shows `venv (Python 3.14.3)`.

### How # %% cells work — key rule

Each cell only knows about what's inside it OR what was run before it in the same session.
Imports must be inside a cell, not floating above the first `# %%` marker.

Wrong:

```python
import numpy as np   # outside any cell — ignored when running cells below
# %%
print(np.__version__)  # NameError: np not defined
```

Correct:

```python
# %%
import numpy as np
print(np.__version__)  # works fine
```

### Gotcha

If VS Code opens a new PowerShell terminal, it auto-activates venv via:
`venv\Scripts\Activate.ps1` — you'll see `(venv)` in the terminal automatically.
If it doesn't, manually run `venv\Scripts\activate` before running any code.

### Git commit

`Phase 0.2: VS Code setup complete, extensions installed, venv interpreter selected`

---

## Lesson 0.3 — Git Basics for This Curriculum

**Date:** 2026-06-19
**Repo cross-reference:** `phases/00-setup-and-tooling/`

### Why git matters in ML specifically

In ML, git tracks three things simultaneously:

- **Code** — model, training loop, experiments
- **Notes** — your understanding of each concept
- **Progress** — which topics are done, what numbers looked like

Clean commit history = a readable diary of your entire learning journey.

### Commands used every session

```bash
git status                    # see what's changed — run before every commit
git log --oneline             # one line per commit — your progress diary
git add filename.py           # stage specific files, never blind `git add .`
git restore --staged file.py  # unstage something added by mistake
git diff filename.py          # see exactly what changed before committing
```

### Commit format (used throughout this curriculum)

```
Phase X.Y: <what was built>
```

Examples:

- `Phase 0.1: virtual environment setup, numpy 2.5.0, matplotlib 3.11.0, jupyter installed`
- `Phase 2.2: linear regression from scratch, no libraries`
- `Phase 3.5: autograd engine (micrograd-style)`

### .gitignore rules for ML projects

```
venv/                  # never commit the virtual environment
__pycache__/           # Python bytecode cache
.DS_Store              # Mac metadata (good habit even on Windows)
*.pyc                  # compiled Python files
*.pth                  # PyTorch model weights — too large for git
*.pkl                  # pickle files
data/                  # raw datasets — too large
.ipynb_checkpoints/    # Jupyter auto-save files
```

### Gotcha

Files showing `U` in VS Code sidebar = unstaged changes. Always check `git status` before assuming your repo is clean. Commit these before ending any session.

### Git commit

`Phase 0.3: gitignore updated with ML-specific exclusions`

---

## Lesson 0.4 — Jupyter Notebooks

**Date:** 2026-06-19
**Repo cross-reference:** `phases/00-setup-and-tooling/`

### How Jupyter works

Runs a local server on your machine, opens a browser at `http://localhost:8888`. Code runs on the local server — no internet needed.

- `.ipynb` file — stores code cells, markdown cells, and outputs in one JSON file
- Kernel — the Python process running behind the scenes executing your code

### Start Jupyter

```bash
jupyter notebook   # starts server, opens browser automatically
```

### Key shortcuts

| Shortcut        | Action                   |
| --------------- | ------------------------ |
| `Shift + Enter` | Run cell, move to next   |
| `A`             | Insert cell above        |
| `B`             | Insert cell below        |
| `DD`            | Delete cell (D twice)    |
| `M`             | Switch cell to Markdown  |
| `Y`             | Switch cell back to Code |

### Cell types

- **Code cell** — runs Python, shows output below
- **Markdown cell** — renders formatted text, used for documenting experiments alongside code
- `[1]:` next to a cell = execution counter, shows the order cells were run

### When to use what

- **Jupyter** — exploring data, visualizing results, sharing work with others
- **VS Code `# %%`** — writing lesson code, anything going into git (clean diffs)

### Gotcha

Jupyter notebooks store outputs inside the `.ipynb` JSON file — this makes git diffs messy. That's why `.ipynb_checkpoints/` is in `.gitignore`, and why we use VS Code `# %%` for code that gets committed.

### Git commit

`Phase 0.4: Jupyter setup verified, notebook basics covered`

---

## Lesson 0.5 — GPU Setup & Google Colab

**Date:** 2026-07-04
**Repo cross-reference:** `phases/00-setup-and-tooling/`

### Why GPUs matter

CPUs execute tasks sequentially — fast per task but one at a time.
GPUs have thousands of smaller cores running simple calculations in parallel simultaneously.
Training = millions of matrix multiplications — GPUs are built exactly for this.

| Hardware | Training time    |
| -------- | ---------------- |
| CPU      | Hours to days    |
| GPU      | Minutes to hours |

CPU is fine for Phases 0-2. GPU needed from Phase 3 onwards.

### Used GPU

- **GPU**: NVIDIA GeForce RTX 2060
- **VRAM**: 6GB
- **CUDA Version**: 13.2
- **Driver**: 596.21

**6GB VRAM is sufficient for:**

- All neural net from-scratch work (Phase 3-4)
- Small GPT training (Phase 4)
- LoRA/QLoRA fine-tuning (Phase 5+)
- Vision, audio, diffusion experiments on small datasets

**Not sufficient for:** training large LLMs (70B+ params) — use Colab or cloud for those.

### PyTorch GPU setup (deferred to Phase 3)

When installing PyTorch, install the CUDA-enabled version:

```bash
pip install torch --index-url https://download.pytorch.org/whl/cu121
```

This tells PyTorch to use the RTX 2060 automatically.

### Google Colab (backup for >6GB jobs)

- Go to colab.research.google.com
- Runtime → Change Runtime Type → T4 GPU → Save
- Free, browser-based, no install needed
- Limitation: sessions timeout after ~12 hours, no persistent storage

### Git commit

`Phase 0.5: GPU setup verified (RTX 2060, 6GB VRAM, CUDA 13.2), Colab configured`

### Key concepts clarified during 0.5

**What is CUDA?**
CUDA (Compute Unified Device Architecture) = NVIDIA's bridge between Python code and GPU cores.
Without CUDA: PyTorch uses CPU only.
With CUDA: PyTorch offloads matrix math to GPU automatically.

```
Your Python code → PyTorch → CUDA → RTX 2060
```

**What is PyTorch? (preview — covered properly in Phase 3.14)**
Two things:

1. Fast tensor math on GPU via CUDA
2. Automatic differentiation (autograd) — calculates gradients automatically via `.backward()`

We build both of these ourselves first in Phase 3, THEN use PyTorch so it's never a black box.

**Different GPUs need different bridges:**
| GPU Brand | Bridge | PyTorch support |
|---|---|---|
| NVIDIA | CUDA | Best — 15+ years, industry standard |
| AMD | ROCm | Good but patchier |
| Apple M1/M2 | MPS (Metal) | Added 2022, works well |
| Intel | oneAPI | Newest, least mature |

NVIDIA dominates ML not just for raw performance but because CUDA has a massive ecosystem head start — every ML library was built CUDA-first.

**Why hand-built autograd still runs on CPU (Phase 3):**
Pure Python/NumPy doesn't speak CUDA. But that's fine — hand-built nets are tiny (2 layers, ~50 neurons), CPU runs them in milliseconds. GPU only becomes essential in Phase 4 when training real models on real data.

"From scratch" means building the math and logic yourself — not rewriting CUDA drivers. Nobody does that, not even Google or Meta.

---

## Lesson 0.6 — Docker for AI (Intro Only)

**Date:** 2026-07-04
**Repo cross-reference:** `phases/00-setup-and-tooling/`

### The problem Docker solves

venv solves Python library isolation but doesn't cover:

- The OS itself
- System-level dependencies
- CUDA driver versions
- Other software the project needs

Result without Docker: works on your machine, breaks on every other machine.

### What Docker does

Packages the entire environment into a container:

```
Docker Container
├── OS layer (e.g. Ubuntu 22.04)
├── CUDA drivers (specific version)
├── Python 3.11
├── numpy 2.5.0
├── your code
└── everything else needed
```

Runs identically on any machine with Docker installed.

### venv vs Docker (Ajay's own words — correct)

"venv is a Python virtual environment tool used to create one locally and packages are installed within that environment, but it doesn't control the OS version and CUDA drivers. To overcome this, Docker is used, where it creates an optimal environment for the model to run — starting from package version match to OS version including CUDA drivers version optimal for PyTorch. This Docker container can be shipped anywhere and run without any extra configuration."

### When Docker appears in this curriculum

- Phase 0-4: not needed — local dev, venv is enough
- Phase 11: deploy trained model — Docker packages it for any server
- Phase 12: capstone projects — production-ready containers

### Git commit

`Phase 0.6: Docker intro — concept understood, hands-on deferred to Phase 11`

---

## Lesson 0.7 — Data Management Basics

**Date:** 2026-07-04
**Repo cross-reference:** `phases/00-setup-and-tooling/`

### Three file formats in ML

**CSV** — small tabular data, human readable, slow at scale

```
age,salary,hired
25,50000,1
30,75000,1
```

Used for: classic ML datasets (Phase 2), features and labels

**JSON** — configs and structured metadata

```json
{ "layers": 6, "learning_rate": 0.001 }
```

Used for: model configs, hyperparameters, tokenizer vocab, API responses

**Parquet** — large datasets, binary, compressed, 10-100x faster than CSV
Used for: large training datasets, production pipelines (Phase 6+)

### Standard ML folder structure

```
project/
├── data/
│   ├── raw/          # original data — never touch
│   ├── processed/    # cleaned/transformed copy
│   └── splits/       # train, val, test splits
├── models/           # saved weights
├── notebooks/        # exploration
├── src/              # source code
└── configs/          # hyperparameter configs
```

### Why never modify raw data

Raw data = source of truth. If processing script corrupts it and original is gone:

- Can't debug whether problem was in data or code
- Can't rerun processing from clean starting point
- Can't compare processed vs raw to verify cleaning worked
- Have to re-download the entire dataset

Same principle as React — never mutate state directly, work on a copy.
Raw data is immutable. Processing scripts are rerunnable. That's the invariant.

### Two rules

1. Never modify raw data — always work on a processed copy
2. Never commit data to git — too large, already in `.gitignore`

### Git commit

Combined with 0.8 at end of Phase 0

---

## Lesson 0.8 — Debugging & Profiling Python

**Date:** 2026-07-04
**Repo cross-reference:** `phases/00-setup-and-tooling/`

### Debugging — pdb (Python Debugger)

Python's built-in debugger. Pauses execution at a line and gives an interactive prompt to inspect state at runtime.

```python
import pdb; pdb.set_trace()  # drop anywhere, pauses here
```

**Key commands:**
| Command | Action |
|---|---|
| `n` | Next line |
| `s` | Step into function |
| `c` | Continue to next breakpoint |
| `p variable` | Print variable value |
| `q` | Quit debugger |

**In VS Code:** click red dot left of line number → set breakpoint → F5 to run in debug mode. Same concept, visual interface.

**Bonus capability:** can change variable values mid-execution to test a fix without restarting. Critical in ML — if loss explodes at step 500, pause there, inspect tensors, tweak, continue without rerunning 500 steps.

### print() vs pdb

`print()` = add statements, run, read output, change code, run again. Slow feedback loop, requires code changes.
`pdb` = pause at runtime, inspect any variable interactively, step line by line, no code changes needed. Same reason browser DevTools is better than `console.log` everywhere.

### Profiling — finding what's slow

**`cProfile`** — built-in, time per function:

```bash
python -m cProfile -s cumtime your_script.py
```

**`line_profiler`** — time per line inside a specific function:

```bash
pip install line_profiler
kernprof -l -v your_script.py
```

Add `@profile` decorator to the function you want to measure.

### When to use what

| Tool                | When                                                |
| ------------------- | --------------------------------------------------- |
| VS Code breakpoints | Daily — any bug while writing code                  |
| `pdb`               | Running scripts outside VS Code                     |
| `cProfile`          | Training loop slower than expected                  |
| `line_profiler`     | Know which function is slow, want line-level detail |

### Git commit

`Phase 0.8: debugging and profiling concepts covered — Phase 0 complete`
