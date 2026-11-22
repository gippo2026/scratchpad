"""Headless matplotlib helper for this Codespace.

There is no GUI/Tk display here, so matplotlib's default `plt.show()` silently
does nothing. Monkeypatch it to save the figure as a PNG file.

Usage (just add this line to the top of any script in this project):

    import show_plot  # noqa: F401  (patches plt.show)

Each `plt.show()` saves a PNG (plot.png, plot_2.png, plot_3.png, ...), prints
its path, and asks the small local VS Code extension `local.showplot-bg` to
open each one in its own **background (pinned) editor tab** — so your maximized
terminal keeps focus and every plot stays open instead of a single preview tab
being reused. Multiple show() calls no longer overwrite each other, and the
figure is closed so the next plot starts fresh. The extension is optional:
without it the PNGs are still saved, they just aren't opened automatically.

No sys.path boilerplate is needed — a .pth in the venv handles it.

Options:
    SHOW_PLOT_OPEN=cli uv run python script.py   # use `code --goto` instead
                                                   (steals terminal focus)
    SHOW_PLOT_DISABLE=1 uv run python script.py  # only save, never open
"""
from __future__ import annotations

import os
from itertools import count

import matplotlib
import matplotlib.pyplot as plt

# Headless: force a non-interactive backend so nothing tries to open a window.
matplotlib.use("agg", force=True)

_show_count = count(1)
_REQUEST_FILE = "/tmp/show_plot_request.txt"


def _default_name() -> str:
    """Unique filename per show() call within a script run."""
    index = next(_show_count)
    base = "plot.png" if index == 1 else f"plot_{index}.png"
    return os.path.join(os.getcwd(), base)


def _request_background_open(fname: str) -> None:
    """Ask the local VS Code extension to open the PNG without stealing focus."""
    tmp = f"{_REQUEST_FILE}.{os.getpid()}.tmp"
    try:
        with open(tmp, "w") as req:
            req.write(os.path.abspath(fname) + "\n")
        # Atomic rename: the extension's fs.watch only ever sees a complete
        # request, so it can't read an empty/partial file, and each show()
        # produces exactly one open instead of several.
        os.replace(tmp, _REQUEST_FILE)
    except OSError:
        pass


def show(*args, **kwargs):  # noqa: ANN001, ANN401
    """Save the current figure to a PNG, then close it."""
    fname = kwargs.get("fname") or _default_name()
    plt.savefig(fname, dpi=100, bbox_inches="tight")
    print(f"Saved figure to {fname}")

    if os.environ.get("SHOW_PLOT_DISABLE") != "1":
        if os.environ.get("SHOW_PLOT_OPEN") == "cli":
            try:
                import subprocess

                subprocess.run(["code", "--goto", f"{fname}:1"], check=False)
            except Exception as exc:  # noqa: BLE001
                print(f"Could not open VS Code viewer: {exc}")
        else:
            _request_background_open(fname)

    # A real plt.show() clears the figure; do the same so subsequent plots in
    # the same script don't accumulate on top of the one just saved.
    plt.close("all")


# Replace matplotlib's show with our headless version.
plt.show = show
