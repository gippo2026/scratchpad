# Python Practicals

Python practical files. Dependencies are managed with [uv](https://docs.astral.sh/uv/).

## Setup

```bash
uv venv                 # create .venv (already present locally)
uv pip install <pkg>    # install into the isolated .venv
```

To use this environment in Neovim, open a file in this directory and select the
venv via `venv-selector` (`<leader>usv` / `:VenvSelect`).

---

> Note (added by the environment-setup documentation branch): this file is a
> verbatim copy of the Python project README from the `py-practical` branch,
> whose project now lives in `python-practicals/` at the workspace root. The
> setup handoff documents are `README.md` (index), `SETUP.md` and `PYTHON.md`
> on this `env-setup-log` branch.
