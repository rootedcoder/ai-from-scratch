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

### Verified versions (Ajay's machine)

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
