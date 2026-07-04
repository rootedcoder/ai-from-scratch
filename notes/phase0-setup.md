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
