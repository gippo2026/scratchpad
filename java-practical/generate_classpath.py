"""Generate the repo-root .classpath from the Java folder structure.

Source roots are discovered automatically:
  * a file with `package a.b;` belongs to the ancestor folder whose path ends
    in `a/b`;
  * a package-less file belongs to its own folder.

Nested roots are excluded from their parent so jdtls never sees the same
.java file twice. Run directly, or let the nvim autocmd call it on save.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
JAVA = ROOT / "java-practical"
OUTPUT = ROOT / ".classpath"
PACKAGE = re.compile(r"^\s*package\s+([\w.]+)\s*;", re.MULTILINE)


def source_root(java_file: Path) -> Path:
    match = PACKAGE.search(java_file.read_text(encoding="utf-8", errors="replace"))
    if not match:
        return java_file.parent

    parts = match.group(1).split(".")
    path_parts = java_file.relative_to(ROOT).parts
    for i in range(len(path_parts)):
        if tuple(path_parts[i : i + len(parts)]) == tuple(parts):
            return ROOT.joinpath(*path_parts[:i])
    # No folder matches the package: fall back to the file's folder and let
    # jdtls report the mismatch rather than guessing.
    return java_file.parent


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def main() -> None:
    roots = sorted({relative(source_root(f)) for f in JAVA.rglob("*.java")})

    entries = []
    for root in roots:
        # Exclude any deeper source roots from this one, if nested.
        children = [r[len(root) + 1 :] for r in roots if r.startswith(root + "/")]
        attr = f' excluding="{",".join(c + "/**" for c in children)}"' if children else ""
        entries.append(f'\t<classpathentry kind="src" path="{root}"{attr}/>')

    body = "\n".join(
        [
            '<?xml version="1.0" encoding="UTF-8"?>',
            "<classpath>",
            *entries,
            '\t<classpathentry kind="con" path="org.eclipse.jdt.launching.JRE_CONTAINER"/>',
            '\t<classpathentry kind="output" path=".bin"/>',
            "</classpath>",
            "",
        ]
    )

    if OUTPUT.exists() and OUTPUT.read_text(encoding="utf-8") == body:
        print("unchanged")
        return

    OUTPUT.write_text(body, encoding="utf-8")
    print("changed")


if __name__ == "__main__":
    main()
