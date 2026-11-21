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
> verbatim copy of the Python project README that was at the workspace root
> when the `env-setup-log` branch was created. The setup handoff document is
> `README.md` in this branch; `README.md` at the workspace root now contains
> that handoff log, so this copy preserves the original project README.
