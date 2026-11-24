# Environment Setup Log — Handoff Context for AI Agents

This is a **documentation-only orphan branch** (`env-setup-log`). Its only job is
to let a fresh codespace or AI agent pick up the full context immediately. The
repo is `/workspaces/uni-practicals` (`origin` = `https://github.com/fg65hg67/uni-practicals`).

Create new codespaces from **this branch**, not `main` — `main` is deliberately
kept generic (only `.devcontainer/`). These docs are split by purpose; start
with the mental model, then go to the topic you need.

## Read in this order

| File | What it answers |
| --- | --- |
| `MENTAL-MODEL.md` | **Why** things are where they are: the three planes, branch ownership, routing rules, invariants, failure modes. Read this first. |
| `SETUP.md` | **What happened and how to reproduce it**: chronological log, container facts, network notes, problems/fixes, everyday commands, recreate-from-scratch checklist, references. |
| `PYTHON.md` | Python practicals: `show_plot.py`, the `local.showplot-bg` VS Code extension, and offline exam introspection (`inspect.signature`, `__doc__`, `dir`). |
| `JAVA.md` | Java practicals: `java-practical` branch, jdtls `.project`/`.classpath`, and the generated/dynamic classpath. |
| `REPO-CONTEXT.md` | History of the upstream `practical-exams` repo that explains why manual setup was needed. |
| `PYTHON-PROJECT-README.md` | The original Python project README, preserved verbatim. |

## Branch map

| Branch | Content |
| --- | --- |
| `main` | Generic template only: `.devcontainer/devcontainer.json`, `post-create.sh`. **Never commit project work here.** |
| `env-setup-log` | These docs only — no practicals. |
| `py-practical` | Python coursework in `python-practicals/`. |
| `html-practicals` | PHP/HTML/CSS coursework (deployed to `/var/www/html`). |
| `java-practical` | Java coursework in `java-practical/`. |

All five are orphan branches: no shared history, each independently check-outable.
A directory like `python-practicals/` or `java-practical/` exists only when its
branch is checked out; switching branches hides it (the `.venv` stays on disk).

## Three planes in one paragraph

1. **Identity** — git branches: code and docs. Committed and pushed.
2. **Machine state** — runtimes, `.venv`, Neovim/Mason config, VS Code extensions,
   generated `.classpath`. Lives in `~`, apt, mise, Mason — **not in git**.
3. **Workload** — deployed artifacts: `/var/www/html` and compiled Java output.
   Produced from branches, never edited in place.

Confusing these planes is the main source of mistakes. The full routing rule and
invariants are in `MENTAL-MODEL.md` §§3, 6.

## Environment in a nutshell

- Debian 13 devcontainer, **no systemd** → `sudo service apache2 start` after recreation.
- Runtimes: Java 25 (jdtls needs ≥21), Python 3.13.18, PHP 8.4, Node, Composer.
- `pypi.org` unreachable → Aliyun mirror in `python-practicals/uv.toml`; Debian
  apt, GitHub, npm and UCI work.
- Python plots: `show_plot.py` + `local.showplot-bg` → `PYTHON.md`.
- Java LSP: jdtls with a **generated** `.classpath` → `JAVA.md`.

## Verification before you finish a task

Run a real command, not just a visual check: `curl http://localhost/`,
`uv run ruff check .`, `uv run python assignment1/setA/q.py`, `javac -Xlint:all *.java`,
headless nvim LSP checks. Then push the branch — leave `main` untouched.

## Next codespace

Clone/create from `https://github.com/fg65hg67/uni-practicals` using the
**`env-setup-log`** branch. If a codespace was created from `main`, the agent
will not have this context — fetch/check out this branch first.
