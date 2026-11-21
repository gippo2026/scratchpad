"""Headless matplotlib helper for this Codespace.

There is no GUI/Tk display here, so matplotlib's default `plt.show()` silently
does nothing. Monkeypatch it to save the figure as a PNG and open it in the
VS Code image viewer.

Usage (just add this line to the top of any script in this project):

    import show_plot  # noqa: F401  (patches plt.show)

Then `plt.show()` saves plot.png and opens it in the VS Code viewer.
No sys.path boilerplate is needed — a .pth in the venv handles it.
"""
from __future__ import annotations

import os

import matplotlib
import matplotlib.pyplot as plt

# Headless: force a non-interactive backend so nothing tries to open a window.
matplotlib.use("agg", force=True)

_DEFAULT_NAME = os.path.join(os.getcwd(), "plot.png")


def show(*args, **kwargs):  # noqa: ANN001, ANN401
    """Save the current figure to plot.png and open it in VS Code."""
    fname = kwargs.get("fname", _DEFAULT_NAME)
    plt.savefig(fname, dpi=100, bbox_inches="tight")
    try:
        import subprocess

        subprocess.run(["code", "--goto", f"{fname}:1"], check=False)
    except Exception as exc:  # noqa: BLE001
        print(f"Could not open VS Code viewer: {exc}")
    print(f"Saved figure to {fname}")


# Replace matplotlib's show with our headless version.
plt.show = show