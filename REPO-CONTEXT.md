# Upstream Practicals Repo — Git History Context

Source: `https://github.com/gipoo2026/practical-exams.git`

This repo was cloned and fully inspected during the setup, then removed from the
workspace at the user's request. History below was read from a temporary bare
clone at the time. It explains *why* the environment ended up needing manual
PHP/Neovim/Python setup: the elaborate setup was once built here, then
deliberately reverted to a generic baseline.

---

## 1. Branch graph (all branches)

```
* 05e6913 2026-11-21  (py-practical) Add reproducible local Python dev environment
* 1cd6ee6 2026-11-21  Add assignment2 Set A solutions
* b361d84 2026-11-20  Add assignment1 practice
* fb41ac3 2026-11-20  Reorganize Set A practicals: assignment1/setA/q1..q8.py
* deb9ccd 2026-11-20  Ignore generated plot PNGs
* 5d5733a 2026-11-20  Add Heights and Weights dataset (Kaggle)
* 5eb02a4 2026-11-20  Simplify show_plot usage: just 'import show_plot'
* d75d928 2026-11-20  Add headless matplotlib show helper
* 5de94d7 2026-11-20  Add uv mirror config (PyPI unreachable) and Python practical file
 \ 
  * a7a2fe0 2026-11-20  Init Python practicals (uv venv setup)
* d046f6f 2026-11-19  (html-practicals) Add php assignment 4
 \ 
  * ec84093 2026-11-19  Add PHP/HTML/CSS practicals (assignments 1-3)
* 1546f96 2026-11-17  (main, HEAD) Lock tracked config files with skip-worktree in post-create
* be0f00a 2026-11-17  Make the tracked mise.toml the global codespace toolchain
* 8d9b508 2026-11-17  Track a generic mise.toml and tidy post-create setup
* 660d6db 2026-11-17  Ignore machine-local mise.toml
* 6d8c68c 2026-11-17  Restore generic devcontainer setup
* e004c26 2026-11-17  Remove the php web-root symlink and php-practicals directory
* e5286ed 2026-11-17  Configure LazyVim for PHP, HTML/CSS, Java and Python
* 20bf156 2026-11-17  Serve /var/www/html as a browsable directory index
* 46d6f80 2026-11-17  Set up PHP/PostgreSQL practicals environment in devcontainer
* 326cd82 2026-11-16  Use latest tags for mise feature and zsh plugins
* bdb1971 2026-11-16  Install zoxide via mise and initialize it for zsh
* 799f313 2026-11-16  Set up devcontainer with mise activation, zsh plugins, Node and LazyVim
* 01e6554 2026-11-16  Use Debian 13 (trixie) base image
* d26ff7f 2026-11-16  Add minimal devcontainer config with mise only
* 1a15bef 2026-11-16  Initial commit
```

## 2. What each branch holds

- **`main`** (HEAD `1546f96`) — generic codespace baseline only:
  `.devcontainer/devcontainer.json`, `.devcontainer/post-create.sh`, `mise.toml`,
  `.gitignore`, and a one-line `README.md` (`# practical-exams-`).
  `mise.toml` declares `btop`, `neovim`, `node`, `opencode`, `zoxide` as
  "latest"; post-create copies it to `~/.config/mise/config.toml`, wires shell
  activation, zsh plugins, zoxide, LazyVim, and marks tracked files
  `skip-worktree` so codespace-local edits can't be committed back.
- **`html-practicals`** (`d046f6f`, "Add php assignment 4") — PHP/HTML/CSS
  assignments `assignment1/` … `assignment4/` (sets A and B), plus
  `composer.json` (`{}`), `.phpactor.json` (`{}`), `.php-cs-fixer.dist.php` and
  a small `.gitignore`. **This is the content deployed to `/var/www/html/`.**
- **`py-practical`** (`05e6913`, "Add reproducible local Python dev
  environment") — Python assignments (`assignment1/setA/q1..q8.py`,
  `setB/q1..q7.py`, `assignment2/setA/q1..q5.py`), `heightweight.csv`,
  `show_plot.py`, `pyproject.toml`, `uv.lock`, `uv.toml` and `DEV_ENV.md`.
  **This is the content deployed to `python-practicals/` at the workspace root.**

## 3. Key historical setup commits (and why they matter)

- **`46d6f80` — "Set up PHP/PostgreSQL practicals environment in devcontainer"**
  Installed PHP 8.4 via mise (source build with many dev libs), Apache +
  `libapache2-mod-php`, PHP MySQL/pgsql/mcrypt extensions and PostgreSQL 17;
  exposed `php-practicals/` as `/var/www/html/php` via symlink; configured a
  `postgres` DB role/password; started services with `sudo service ...` because
  systemd is absent. This confirms the user's expectation that Apache serves
  the PHP practicals on localhost.
- **`20bf156` — "Serve /var/www/html as a browsable directory index"**
  Removed the stock Apache landing page and made the web root writable by the
  devcontainer user — matching the current `/var/www/html` deployment.
- **`e5286ed` — "Configure LazyVim for PHP, HTML/CSS, Java and Python"**
  Enabled LazyVim language extras and added `html-lsp`/`css-lsp`/`prettier`
  via `nvim-lspconfig` opts (HTML/CSS have no LazyVim extra), installed Mason
  tools (phpactor, phpcs, php-cs-fixer, jdtls, java-debug-adapter, java-test,
  pyright, ruff), enabled treesitter parsers, installed `fd-find` for
  venv-selector/pickers, and noted "Java needs a JRE (Java 27 is installed in
  this container)" — evidence that jdtls needs a newer Java than 21 (we used 25).
- **`e004c26` — "Remove the php web-root symlink and php-practicals directory"**
  Decided to serve files directly from `/var/www/html` instead of symlinking —
  exactly the flattened deployment done in this session.
- **`6d8c68c` — "Restore generic devcontainer setup"**
  Reverted all project-specific post-create/README changes so the image config
  stays generic. This is why a fresh codespace from the current `main` has only
  the base toolchain and requires the manual language/web setup recorded in
  `README.md`.
- **`be0f00a` / `1546f96`** — made the tracked `mise.toml` the global toolchain
  and locked tracked files with `skip-worktree` (current `main` state).

## 4. Timeline summary

| Date | Milestone |
| --- | --- |
| 2026-11-16 | Debian 13 base, mise, zsh plugins, zoxide, Node, LazyVim |
| 2026-11-17 | LAMP + PostgreSQL, directory-index web root, LazyVim languages — then reverted to a generic baseline |
| 2026-11-19 | PHP/HTML/CSS assignments 1–4 committed on `html-practicals` |
| 2026-11-20 | Python practicals, uv mirror (`uv.toml` — PyPI unreachable), dataset, plotting helper |
| 2026-11-21 | Reproducible Python environment (pyproject + uv.lock + DEV_ENV.md) |

The `uv.toml` mirror note from commit `5de94d7`
("PyPI unreachable — use the Aliyun mirror") is the reason this session's
Python deps were installed via `https://mirrors.aliyun.com/pypi/simple/`.
