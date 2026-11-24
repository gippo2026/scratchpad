# Python Practicals — Headless Plots & Offline Introspection

> Part of the `env-setup-log` handoff docs. `SETUP.md` has the environment
> chronology; this file is the day-to-day Python workflow.

## Headless plotting: `show_plot.py` + `local.showplot-bg`

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
