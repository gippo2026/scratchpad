# Python Practicals

Python practical files. Dependencies are managed with [uv](https://docs.astral.sh/uv/).

## Setup

```bash
uv venv                 # create .venv (already present locally)
uv pip install <pkg>    # install into the isolated .venv
```

To use this environment in Neovim, open a file in this directory and select the
venv via `venv-selector` (`<leader>usv` / `:VenvSelect`).
