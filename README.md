# Environment Setup Log — Handoff Context for AI Agents

> **Purpose of this branch:** this is a documentation-only branch (`env-setup-log`).
> Its tree contains **only README files**. It records, step by step, everything
> that was done to set up this codespace so that a fresh codespace / AI agent
> can pick up the full context immediately without re-explaining the task.
>
> Read this file first. Then read `README-MENTAL-MODEL.md` (the design/why —
> **essential context**). Also see `README-REPO-CONTEXT.md` (git history of the
> upstream practicals repo) and `README-PYTHON-PRACTICALS.md` (the original
> Python project README, preserved verbatim).

> **Next codespace:** clone/create from
> `https://github.com/fg65hg67/uni-practicals.git` using the **`env-setup-log`**
> branch. `main` is deliberately kept clean/generic (only `.devcontainer/`
> config) — do not commit docs or practicals there. These README files are the
> handoff context the AI agent should read on first load.

---

## 1. Quick context

- **Container:** Debian 13 (trixie) devcontainer, user `vscode`, `sudo` available.
- **No systemd:** services must be managed with `sudo service <name> start|restart|status`.
  Nothing auto-starts on container recreation.
- **Workspace repo:** `/workspaces/uni-practicals`
  - `origin` = `https://github.com/fg65hg67/uni-practicals`
  - `main` tracks only `.devcontainer/devcontainer.json` and
    `.devcontainer/post-create.sh` (both marked `skip-worktree` by post-create).
- **Upstream practicals repo:** `https://github.com/gipoo2026/practical-exams.git`
  - Cloned, used, then **removed** at the user's request. Its history is
    summarized in `README-REPO-CONTEXT.md`.
- **Network note:** `pypi.org` is **unreachable** (timeouts). The Aliyun mirror
  `https://mirrors.aliyun.com/pypi/simple/` **works** and is configured in the
  Python project's `uv.toml`. Debian apt, GitHub and npm all work.

### Final layout

| Path | Contents |
| --- | --- |
| `/var/www/html/` | PHP/HTML/CSS practicals, **flattened**: `assignment1/` … `assignment4/`, plus `composer.json`, `.phpactor.json`, `.php-cs-fixer.dist.php`. Served by Apache at `http://localhost/...`. |
| `/workspaces/uni-practicals/python-practicals/` | **Python practicals** project: `assignment1/`, `assignment2/`, `pyproject.toml`, `uv.lock`, `uv.toml`, `show_plot.py`, `heightweight.csv`, `DEV_ENV.md`, `.venv/`. |
| `~/.config/nvim/` | LazyVim config: `lazyvim.json`, `lua/plugins/languages.lua`, `lua/config/options.lua`. |
| `~/.config/mise/config.toml` | Global mise toolchain (node, opencode, neovim, btop, zoxide, java, python, uv). |
| `~/.vscode-remote/extensions/local.showplot-bg-0.0.1/` | Manual VS Code extension for headless plots; source/VSIX in `/tmp/showplot-bg/` and `/tmp/showplot-bg.vsix`. See §5. |

The cloned `practical-exams/` directory no longer exists.

---

## 2. Full chronological setup log

### Phase 1 — Clone and baseline devcontainer setup
1. Verified the upstream repo was reachable (`git ls-remote` HEAD `1546f96`).
2. Fully cloned `https://github.com/gipoo2026/practical-exams.git` into
   `/workspaces/uni-practicals/practical-exams` with full history and submodules
   (there were none), and created local tracking branches for all three remote
   branches: `main`, `html-practicals`, `py-practical`.
3. Inspected the repo: `main` is only a generic devcontainer/mise baseline
   (`README.md` was just `# practical-exams-`); the real coursework lives on
   the two other branches.
4. Ran the repo's own `.devcontainer/post-create.sh`, which:
   - added `eval "$(mise activate bash|zsh)"` to shell rc files,
   - installed zsh-autosuggestions + zsh-syntax-highlighting,
   - copied `mise.toml` to `~/.config/mise/config.toml` (global toolchain),
   - `mise install` → `btop`, `neovim`, `node`, `opencode`, `zoxide`,
   - cloned the LazyVim starter into `~/.config/nvim`, set `vi → nvim` alias,
   - enabled zoxide shell integration,
   - marked all tracked files `skip-worktree`.
5. Synced LazyVim plugins with `nvim --headless "+Lazy! sync" +qa`.

### Phase 2 — PHP / Java / Python language support in Neovim
Docs consulted (per the user's "refer docs extensively"):
`https://www.lazyvim.org/extras/lang/{python,java,php}`,
`/extras/dap/core`, `/extras/test/core`, `/plugins/lsp`, `/extras`, plus the
installed LazyVim 16.0.2 source to confirm exact module names, `opts_extend`
behaviour and Java requirements.

6. Installed runtimes:
   - `java` via mise — first `21` (LTS), later **upgraded to 25** (see fixes),
   - `python 3.13` + `uv` via mise,
   - `php 8.4` + common extensions + `composer` via apt (mise's PHP source
     build failed — see fixes).
   - `fd-find` via apt + `/usr/local/bin/fd → /usr/bin/fdfind` symlink.
7. Enabled LazyVim extras in `~/.config/nvim/lazyvim.json`:
   `dap.core`, `test.core`, `lang.java`, `lang.php`, `lang.python`.
8. Created `~/.config/nvim/lua/plugins/languages.lua` with Mason
   `ensure_installed` for: `jdtls`, `phpactor`, `pyright`, `ruff`, `phpcs`,
   `php-cs-fixer`, `stylua`, `shfmt`, `java-debug-adapter`, `java-test`,
   `php-debug-adapter` (and later disabled Mason-DAP auto-install).
9. Set explicit LSP choices in `~/.config/nvim/lua/config/options.lua`:
   `vim.g.lazyvim_php_lsp = "phpactor"`,
   `vim.g.lazyvim_python_lsp = "pyright"`,
   `vim.g.lazyvim_python_ruff = "ruff"`.
10. `Lazy! sync` installed nvim-jdtls, neotest (+ python/phpunit/pest adapters),
    nvim-dap, dap-ui, dap-virtual-text, dap-python, venv-selector.nvim,
    mason-nvim-dap.
11. Installed all Mason packages via a headless Lua script
    (`/tmp/mason_install.lua`) that loads Mason and polls `registry` until every
    package reports installed. Mason binaries live in
    `~/.local/share/nvim/mason/bin/`.
12. Verified with headless Neovim opening real sample files:
    Java → `jdtls`, Python → `pyright,ruff`, PHP → `phpactor`; Treesitter
    parsers java/python/php OK; DAP adapters `python,debugpy,php` and
    configurations `python,java,php`.

### Phase 3 — Apache/PHP web root
13. Installed `apache2` + `libapache2-mod-php8.4` via apt (PHP 8.4 module),
    added `/etc/apache2/conf-available/servername.conf` with
    `ServerName localhost`, enabled it, and started Apache with
    `sudo service apache2 start`.
14. Exported the `html-practicals` branch with
    `git archive html-practicals | sudo tar -x -C /var/www/html`, removed the
    stock `index.html`, set ownership `vscode:vscode` and permissions
    (dirs 755, files 644).
15. Verified: `http://localhost/` → HTTP 200; `.html` files serve; PHP executes
    (`curl 'http://localhost/assignment2/setAq1.php?num1=7&num2=3&op=1'` →
    `Mod = 1`).

### Phase 4 — Python project
16. Exported the `py-practical` branch and later moved the whole Python project
    into `python-practicals/` at the workspace root (the only top-level dir in
    that branch).
17. Ran `uv sync` in `/workspaces/uni-practicals/python-practicals/` → created `.venv` and
    installed 14 packages from `uv.lock` via the Aliyun mirror:
    matplotlib 3.11.2, numpy 2.5.5, pandas 3.1.1, ruff 0.17.6, editable
    `show_plot`, plus dependencies.
18. Verified: `uv run python -c "import matplotlib, numpy, pandas, show_plot"`
    OK; `uv run ruff check .` → "All checks passed!"; sample script
    `assignment1/setA/q1.py` runs and prints its DataFrame; `.venv/bin/python`
    is 3.13.18.

### Phase 5 — Cleanup and this branch
19. Deleted `/workspaces/uni-practicals/practical-exams` (cloned repo root) at
    the user's request.
20. Re-verified Neovim LSPs at the **new** locations:
    `/var/www/html/...php` → `phpactor`;
    `/workspaces/uni-practicals/...py` → `pyright,ruff`.
21. Created this orphan branch `env-setup-log` containing only README files.

---

## 3. Problems hit and how they were fixed

| Problem | Fix |
| --- | --- |
| `mise use -g php@8.4` failed: vfox PHP build needs `autoconf` and a long source build | Installed PHP 8.4 + extensions + Composer from Debian apt instead; removed `php` from the global mise config. |
| `pypi.org` times out (pip/uv cannot reach it) | Python deps use the repo's `uv.toml` Aliyun mirror; apt `python3-debugpy` + a `debugpy-adapter` wrapper at `~/.local/bin/debugpy-adapter` (symlinked into Mason's bin) provide Python debugging; `mason-nvim-dap` `automatic_installation = false` stops futile retries. |
| Mason's `debugpy` package was an empty venv | Removed it from `ensure_installed`; apt-managed debugpy used instead. |
| `jdtls` exited with code 13 | Its OSGi bundles require `JavaSE 25`; Java 21 was too old. Installed Temurin 25 LTS via mise (`mise use -g java@25`). |
| `fd` missing (Snacks/venv-selector error on Python buffers) | apt `fd-find` + `sudo ln -s /usr/bin/fdfind /usr/local/bin/fd`. |
| Apache warning "Could not reliably determine the server's FQDN" | `echo 'ServerName localhost' > /etc/apache2/conf-available/servername.conf` + `a2enconf servername`. |
| Ruff "Error while resolving settings from workspace" during a test | Caused by a malformed temporary test `pyproject.toml` (NUL bytes); the real project file is fine — `uv run ruff check .` passes. |
| Only the last PNG of a multi-plot script appeared in VS Code | The `local.showplot-bg` extension used `preview: true`; preview tabs are **replaced and reused** by the next preview. Set `preview: false` (pinned tabs), keep `preserveFocus: true`, then **Developer: Reload Window**. |
| Rapid `plt.show()` calls lost plots / opened duplicate tabs | `show_plot.py` now writes `/tmp/show_plot_request.txt` atomically (temp file + `os.replace`) instead of truncate-then-write, so the extension's `fs.watch` reads exactly one complete request per plot. |

---

## 4. Everyday commands

```bash
# Web / PHP
sudo service apache2 status                # running
curl http://localhost/                     # HTTP 200
curl 'http://localhost/assignment2/setAq1.php?num1=7&num2=3&op=1'

# Python (project lives in python-practicals/)
cd /workspaces/uni-practicals/python-practicals
uv sync                                    # repair venv from uv.lock + mirror
uv run python path/to/script.py
uv run ruff check .
.venv/bin/python --version

# Headless plots (PNG + background VS Code tabs) — see §5
# import show_plot at the top of the script, then call plt.show() as usual
SHOW_PLOT_OPEN=cli uv run python path/to/script.py   # use code --goto instead
SHOW_PLOT_DISABLE=1 uv run python path/to/script.py  # save only, don't open
# After changing extension JS: Ctrl+Shift+P → Developer: Reload Window

# Neovim
nvim                                       # vi alias → nvim
:Mason                                     # LSP/tool manager
:LspInfo                                   # attached servers
<leader>cf                                 # format
:LazyExtras                                # toggle extras

# Runtimes
java -version          # 25 LTS
python3 --version      # 3.13.18
php -v                 # 8.4.28
composer --version
uv --version
```

---

## 5. Headless plotting: `show_plot.py` + `local.showplot-bg`

There is no GUI/Tk display in this codespace, so plain `plt.show()` does
nothing. `python-practicals/show_plot.py` (on branch `py-practical`) patches
`plt.show` so scripts work unchanged:

```python
import show_plot  # noqa: F401 — patches plt.show
# ... build plots with matplotlib.pyplot as plt ...
plt.show()        # saves a PNG and opens it in a background VS Code tab
```

What it does, per call:

- forces the `agg` backend (switching after importing `pyplot` is supported —
  matplotlib's `use()` delegates to `switch_backend`, and non-interactive
  switches are always possible);
- saves to the **current working directory** as `plot.png`, `plot_2.png`,
  `plot_3.png`, … so multiple `show()` calls don't overwrite each other, prints
  the path, and calls `plt.close("all")` so each plot starts fresh;
- writes the absolute path to `/tmp/show_plot_request.txt` **atomically**
  (PID-unique temp file + `os.replace`) — a plain truncate-then-write let the
  extension's `fs.watch` read an empty/partial file (lost plots) and fired
  several duplicate opens per plot;
- honours `SHOW_PLOT_OPEN=cli` (fall back to `code --goto`, which steals terminal
  focus) and `SHOW_PLOT_DISABLE=1` (save only, never open).

Import order does not matter: Python modules are singletons, so patching
`plt.show` works even if a script imports `matplotlib.pyplot` before
`show_plot`.

### The extension is machine state, not git

`local.showplot-bg` v0.0.1 is **manually installed** — it is not part of the
repo, `post-create.sh`, or this docs branch. It lives at
`~/.vscode-remote/extensions/local.showplot-bg-0.0.1/`; the source is
`/tmp/showplot-bg/extension.js` and the installable package is
`/tmp/showplot-bg.vsix` (both patched — reinstall from there, not from an old
copy). It watches `/tmp/show_plot_request.txt` and calls:

```js
vscode.commands.executeCommand("vscode.open", vscode.Uri.file(line), {
  preserveFocus: true,  // maximized terminal keeps focus
  preview: false,       // pinned tabs: keep EVERY plot, not just the last
});
```

`preview: false` is essential. The VS Code API states that "preview tabs will
be replaced and reused until set to stay" — with `preview: true` a multi-plot
script shows only its **last** PNG. With `preserveFocus: true` the tabs open in
the background, so focus stays in the terminal.

If the extension JS is edited, the running extension host must be reloaded:
`Ctrl+Shift+P` → **Developer: Reload Window** (there is no CLI flag for this).
If the extension is missing entirely, PNGs still save — they just don't open.

---

## 6. Recreating this environment from scratch (checklist)

1. Base repo: `https://github.com/fg65hg67/uni-practicals` (the codespace
   template). Its `post-create.sh` handles mise activation, zsh plugins, base
   tools (btop/node/opencode/neovim/zoxide), LazyVim starter and skip-worktree.
2. Install extra runtimes:
   ```bash
   mise use -g java@25 python@3.13 uv
   mise reshim
   sudo apt-get install -y php8.4-cli php8.4-xml php8.4-mbstring php8.4-curl \
     php8.4-zip php8.4-intl php8.4-sqlite3 composer fd-find python3-debugpy \
     apache2 libapache2-mod-php8.4
   sudo ln -sf /usr/bin/fdfind /usr/local/bin/fd
   ```
3. Configure Neovim as in **Phase 2** (extras JSON + `languages.lua` +
   options), `Lazy! sync`, then install Mason packages and the apt debugpy
   wrapper.
4. Deploy PHP: `git archive html-practicals | sudo tar -x -C /var/www/html`
   after cloning the upstream repo; start Apache.
5. Deploy Python: `git archive py-practical | tar -x -C <workspace-root>`,
   then `uv sync`.
6. Install the headless-plot viewer:
   `code --install-extension /tmp/showplot-bg.vsix` (or keep the patched
   `~/.vscode-remote/extensions/local.showplot-bg-0.0.1/` in place), then
   **Developer: Reload Window**. Without it, plots save but never open.
   See §5.
7. Remember to re-run `sudo service apache2 start` after any container
   recreation (no systemd).

---

## 7. References

- LazyVim: https://www.lazyvim.org/extras/lang/python ·
  https://www.lazyvim.org/extras/lang/java ·
  https://www.lazyvim.org/extras/lang/php ·
  https://www.lazyvim.org/extras/dap/core ·
  https://www.lazyvim.org/extras/test/core ·
  https://www.lazyvim.org/plugins/lsp
- mise: https://mise.jdx.dev
- uv: https://docs.astral.sh/uv/ (mirror config: `uv.toml`)
- matplotlib `use()` / backend switching:
  https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.use
- VS Code built-in commands (`vscode.open`):
  https://code.visualstudio.com/api/references/commands ·
  `TextDocumentShowOptions` (`preview` / `preserveFocus`):
  https://code.visualstudio.com/api/references/vscode-api#TextDocumentShowOptions
- Upstream practicals repo context: `README-REPO-CONTEXT.md`
