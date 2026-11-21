# Local Python dev environment

All setup here is **project-local**. The git-tracked baseline files
(`.devcontainer/*`, `mise.toml`, `show_plot.py`, `assignment1/**`) are unchanged.

## What is installed where

| Piece | Where | Notes |
| --- | --- | --- |
| Python 3.13 | mise, via `.mise.toml` | Gitignored/local-excluded; nothing global changed |
| Dependencies | `.venv/` + `uv.lock` | Declared in `pyproject.toml`, reproducible with `uv sync` |
| Ruff | venv dev group | `uv run ruff ...` |
| Pyright | Neovim/Mason LSP | Reads the same `pyproject.toml` settings |
| Lint/type config | `pyproject.toml` | Glob patterns, no per-file lists |

In an interactive shell opened inside this directory, `python` resolves to
`.venv/bin/python` (mise applies the local env config). For scripts/CI, use
`uv run python ...`, which always picks the project venv.

## Everyday commands

```bash
uv sync                      # install/repair the venv from pyproject.toml + uv.lock
python path/to/script.py     # interactive shell, any subdirectory
uv run python path/to/script.py   # works from any shell, including scripts
uv run ruff check .          # lint
uv run ruff format .         # format
pyright                      # type check (same LSP as Neovim)
```

## Writing a new plotting script

`show_plot` is installed editable, so `import show_plot` works from any
subdirectory — no `sys.path` boilerplate. It only patches `plt.show()`, so:

```python
import show_plot  # side effect: patches plt.show
import matplotlib.pyplot as plt

plt.plot([1, 2], [3, 4])
plt.show()
```

`np.histogram()` only computes counts; use `plt.hist()` to draw a histogram.

## How the "false error" suppression stays generic

- `pyright.include = ["**/*.py"]` — every new file is checked automatically.
- Ruff's `per-file-ignores` uses the `assignment1/**/*.py` **directory pattern**
  for the untouched baseline scripts, not individual filenames.
- `src = ["."]` lets Ruff detect local modules (like `show_plot`) as first-party,
  so import ordering adapts to any new local module.
- `ignore = ["F401", "RUF100"]`: F401 is off because `import show_plot` is
  always an intentional side-effect import, so **no per-line noqa is ever
  needed**. RUF100 avoids flagging legacy noqa comments from other linters.
  Everything else is linted normally. Trade-off: genuinely unused imports are
  not reported — the linter no longer distinguishes them from side-effect
  imports.
