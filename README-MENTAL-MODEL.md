# Mental Model — How This Environment Is Organized

> This document explains **why** everything is where it is, so an AI agent can
> reason about new tasks instead of replaying steps mechanically. For the exact
> chronological steps, see `README.md`; for upstream history, see
> `README-REPO-CONTEXT.md`.

---

## 1. The one-sentence model

**`main` is an immutable, generic codespace template; everything task-specific
lives in separate branches (coursework, docs) or outside git entirely (runtimes,
deployed web files).**

The repo `/workspaces/uni-practicals` (`https://github.com/fg65hg67/uni-practicals.git`)
is the *template*. The practicals and the setup log are *payloads* carried on
other branches of that same repo. The running machine is *state* that the
template plus payloads produce.

---

## 2. The three planes

Keep these separate in your head — confusing them is the main source of mistakes.

| Plane | What it is | Where it lives | Committed? |
| --- | --- | --- | --- |
| **Code / identity** | The repo and its branches | `git` objects, pushed to GitHub | Yes |
| **Toolchain / machine state** | Runtimes, LSPs, shell config, venv | `$HOME`, apt, mise, Mason | **No** — recreated by post-create / setup docs |
| **Workload / deployed files** | What Apache actually serves | `/var/www/html` | **No** — it's a deployment target |

Key consequence: the PHP files are **both** committed on `html-practicals`
(source of truth) **and** copied into `/var/www/html` (runtime location). Editing
one does not edit the other. The Python project is committed on `py-practical`
and checked out in `python-practicals/` at the workspace root — there it *is* the same files.

---

## 3. Branch topology and ownership

```
main                  (generic baseline — DO NOT COMMIT TO THIS)
│                       .devcontainer/devcontainer.json
│                       .devcontainer/post-create.sh
│
├── env-setup-log     (agent context — documentation only)
│                       README.md                 ← start here
│                       README-MENTAL-MODEL.md    ← this file
│                       README-REPO-CONTEXT.md
│                       README-PYTHON-PRACTICALS.md
│
├── py-practical      (Python coursework)
│                       assignment1/, assignment2/, pyproject.toml,
│                       uv.lock, uv.toml, show_plot.py, data, DEV_ENV.md
│
└── html-practicals   (PHP/HTML/CSS coursework)
                        assignment1/ … assignment4/, composer.json,
                        .phpactor.json, .php-cs-fixer.dist.php
```

These are **orphan branches**: they share no history with `main` and with each
other. That is deliberate — each branch is an independent payload that can be
checked out without dragging the others along.

### Routing rule for any new file

1. Is it generic devcontainer/tooling config for *every* codespace? → `main`.
2. Is it documentation/context for the agent? → `env-setup-log` (README files only).
3. Is it Python coursework? → `py-practical`.
4. Is it PHP/HTML/CSS coursework? → `html-practicals`.
5. Is it machine state (venv, caches, installed tools, `/var/www/html`)? → **not in git**.

---

## 4. The runtime stack (bottom-up)

```
┌─────────────────────────────────────────────────────────────┐
│ WORKLOADS                                                   │
│  Apache → /var/www/html  (PHP assignments, localhost)        │
│  Python project → python-practicals/ + .venv (uv)           │
├─────────────────────────────────────────────────────────────┤
│ LANGUAGE TOOLING                                            │
│  Neovim/LazyVim: jdtls, pyright+ruff, phpactor + DAP/test   │
│  Runtimes: Java 25, Python 3.13, PHP 8.4, Node, Composer    │
├─────────────────────────────────────────────────────────────┤
│ BASE (from .devcontainer/post-create.sh on main)            │
│  mise activation, zsh plugins, zoxide, LazyVim starter,     │
│  global toolchain, skip-worktree protection                 │
└─────────────────────────────────────────────────────────────┘
```

Layer 1 is automated by the repo. Layers 2–3 were set up manually in this
codespace and are recorded in `README.md`; they are *not* automated and *not*
committed to `main` (by design — `main` must stay generic).

---

## 5. Why things are where they are

- **Why is PHP served from `/var/www/html`, not the repo?** Apache's docroot is
  `/var/www/html`. The repo is a git workspace under `/workspaces`, not a web
  root. The upstream repo even has commits that first symlinked, then decided
  to serve files directly from the docroot — see `README-REPO-CONTEXT.md`.
- **Why is the Python project in its own `python-practicals/` folder?** It keeps
  the Python tooling (`pyproject.toml`, `uv.lock`, `.venv`, `pyright`/`ruff`
  config, `import show_plot`) self-contained and separate from the generic repo
  configs on `main`. Run `uv sync` / `uv run ...` from inside that folder.
- **Why isn't `.venv` committed?** It is machine-specific and large; `.gitignore`
  excludes it. `uv sync` regenerates it from `uv.lock`.
- **Why is the handoff context on a branch instead of `main`?** Because the user
  explicitly wants the generic baseline clean — no project-specific commits in
  the template. A new codespace must therefore be created from the
  `env-setup-log` branch, or the agent must be told to read that branch.
- **Why are there no systemd services?** This is a devcontainer; `service ...`
  is the only way to start Apache, and nothing auto-starts after recreation.
- **Why an Aliyun PyPI mirror?** `pypi.org` is unreachable from this environment;
  `uv.toml` in the Python project pins the working mirror.
- **Why is the plot viewer an extension instead of just `code --goto`?** The CLI
  opens a foreground tab and steals focus from the maximized terminal. The
  manual `local.showplot-bg` extension opens PNGs with `preserveFocus: true`
  (background) and `preview: false` (pinned, so every plot of a multi-plot
  script stays in a tab). It is machine state like `.venv` — never in git; see
  `README.md` §5.

---

## 6. Invariants — do not break these

1. **Never commit to `main`** unless it is a genuinely generic template change
   the user asked for. Keep its two-file tree intact.
2. **Keep `env-setup-log` README-only.** Don't mix practical files into it.
3. **Don't confuse source with deployment.** Changing `html-practicals` requires
   re-deploying to `/var/www/html`; changing `py-practical` requires `uv sync`
   only if dependencies changed.
4. **Java must stay ≥ 21 for jdtls** (we use 25). Downgrading breaks Java LSP
   with exit code 13.
5. **Python debugging comes from apt** (`python3-debugpy` + `debugpy-adapter`
   wrapper), not Mason, because PyPI is unreachable.
6. **Apache must be started manually after container recreation.**
7. **Prefer `uv run ...`** for Python commands — it always picks the project venv.
8. **Clipboard:** `~/.config/nvim/lua/config/options.lua` sets
   `vim.opt.clipboard = "unnamedplus"` and forces `vim.g.clipboard = "osc52"`
   when there is no X/Wayland display (this container has none, so OSC 52 is
   the only working "system clipboard"). LazyVim temporarily clears the option
   at startup and restores it on `VeryLazy` — a headless check before that
   event will misleadingly show an empty `clipboard`.
9. **Motions:** `vim.opt.startofline = true` in `options.lua`, so `gg`, `G`,
   `H/M/L`, `CTRL-D/U/F/B` land on the first non-blank of the destination line
   instead of keeping the previous column (Neovim default is off; `:h 'sol'`).
10. **Wrapping:** `vim.opt.wrap = true` globally in `options.lua`; LazyVim only
    turned it on for text/markdown filetypes. `linebreak` is already on, so
    wraps happen at word boundaries (`:h 'wrap'`, `:h 'linebreak'`).
11. **Headless plots:** `show_plot.py` patches `plt.show` and hands PNG paths to
    `local.showplot-bg` via `/tmp/show_plot_request.txt` (atomic write). The
    extension must use `preview: false` — preview tabs are replaced, so
    `preview: true` shows only the **last** plot. Keep `preserveFocus: true` so
    the terminal keeps focus. After editing extension JS, reload the VS Code
    window; the extension/source/VSIX are machine state in `~` and `/tmp`,
    never committed.

---

## 7. How to approach a new task

1. Read `README.md` (steps/state) and this file (design).
2. Identify which **plane** the task touches: git branch, machine state, or
   deployment.
3. Pick the **branch** using the routing rule in §3; never default to `main`.
4. If the task changes a deployed artifact, re-deploy it (copy to
   `/var/www/html` / re-run `uv sync`) and **verify with a real command**
   (`curl`, `uv run ruff check .`, headless nvim LSP check).
5. Push the branch; leave `main` untouched.

---

## 8. Failure modes and their meaning

| Symptom | Likely cause |
| --- | --- |
| `jdtls` exits 13 | Java older than 21 — reinstall Java 25 via mise |
| Mason `debugpy` empty venv / pip timeouts | PyPI blocked — use apt debugpy + wrapper |
| `Cannot find any fd binary` | `fd-find` missing → symlink `/usr/local/bin/fd` |
| Apache FQDN warning | `ServerName localhost` conf missing/disabled |
| Blank PHP page | Check GET params / Apache error log; PHP itself works |
| `python` resolves to 3.13 but not venv packages | Use `uv run python ...` (or select `.venv` via venv-selector in nvim) |
| New codespace lacks the setup log | It was created from `main`; use `env-setup-log` instead |
| Only the last plot appears for a multi-plot script | Extension uses `preview: true`; set `preview: false` + reload window (§5 of `README.md`) |
| Plots save but no tab opens | `local.showplot-bg` missing/not loaded — reinstall from `/tmp/showplot-bg.vsix` and reload window |
| Some plots missing on rapid `plt.show()` calls | Request file written non-atomically; use temp file + `os.replace` in `show_plot.py` |
