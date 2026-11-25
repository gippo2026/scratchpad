# Java Practicals — `java-practical` Branch & jdtls Classpath

> Part of the `env-setup-log` handoff docs. See `README.md` (index),
> `MENTAL-MODEL.md` (design), `SETUP.md` (environment chronology).

## Branch and layout

`java-practical` is an orphan branch created from a clean tree. Its tree:

```
java-practical/
├── .gitignore                     # *.class, build/, out/, target/, .idea/
├── generate_classpath.py          # generates the repo-root .classpath
├── practice-set/
│   ├── 10-marks/                  # standalone .java files, no packages
│   └── 20-marks/                  # ALL 20-mark solutions live here
│       ├── *.java                 # standalone (abstract/inheritance/interface)
│       ├── MyMath/ArithOp.java         # package MyMath; folder matches package
│       ├── TestArithOp.java            # default package, imports MyMath.ArithOp
│       ├── AdvMath/NumericOp.java      # package AdvMath; folder matches package
│       └── TestNumericOp.java
```

At the repo root, **only on this branch**: `.project` (Eclipse/JDT project
marker), `.classpath` (generated), and a root `.gitignore` that ignores
`python-practicals/` (the 388 MB Python `.venv` stays on disk but is hidden
while on this branch) and `.bin/` (hidden jdtls build output).

Compile/run is plain JDK — no Maven/Gradle:

```bash
cd java-practical/practice-set/20-marks
javac -Xlint:all *.java
java -cp . OperationCylinder
```

## jdtls needs a matching source root

jdtls does **not** accept a `.java` file unless its folder is a source root and
its folder path matches its `package` declaration. Symptoms:

- yellow warning: *"X is not on the classpath of the project java-practicals"*
  → file's folder was not a source root;
- *"The declared package 'MyMath' does not match the expected package …"*
  → folder path did not match `package MyMath;`.

`.classpath` declares just **two source roots**: `10-marks` and `20-marks`.
Every 20-mark file is directly under `20-marks`, and package files sit in
`MyMath/` and `AdvMath/` folders whose names **exactly match** their `package`
declarations — so a single source root is enough. The earlier red *"declared
package \"\" does not match expected package AdvMathPackage"* came from extra
`MyMathPackage`/`AdvMathPackage` wrapper folders plus overlapping source roots;
those wrappers are gone. The generated build output folder is hidden `.bin/`.
`org.eclipse.jdt.launching.JRE_CONTAINER` supplies the JDK and `bin/` is output.

## Dynamic generation (do not hand-edit `.classpath`)

`java-practical/generate_classpath.py` scans every `.java` file:

- `package a.b;` → source root is the ancestor folder whose path ends in `a/b`;
- no package → the file's own folder;
- nested roots are automatically `excluding`-ed from parents;
- writes root `.classpath` **only when content changes**, printing `changed` or
  `unchanged` (avoids pointless jdtls restarts).

Run manually with `python3 java-practical/generate_classpath.py`.

### Neovim integration (machine state — not in git)

`~/.config/nvim/lua/config/autocmds.lua` (LazyVim auto-loads this file) contains:

- `BufWritePost` on `java-practical/**/*.java` → runs the generator via
  `vim.system()`;
- if output says `changed` → `vim.cmd("lsp restart jdtls")` (Nvim 0.12's
  documented `:lsp restart [client]`) and a notification;
- user command `:JavaClasspath` for manual regeneration;
- one generation at load time.

So: add a new package folder + `.java` file, save it, and jdtls updates itself.
If errors linger, run `:JavaClasspath` or `:lsp restart jdtls`.

Docs consulted for this (per the user's "rely heavily on docs"):
- LazyVim config/file structure: https://www.lazyvim.org/configuration
- Neovim `nvim_create_autocmd()`: https://neovim.io/doc/user/api.html
- Neovim `vim.system()` / `lua.txt`: https://neovim.io/doc/user/lua.html
- Neovim `:lsp restart`: https://neovim.io/doc/user/lsp.html
- jdtls `ProjectOptions.sourcePaths` / init options:
  https://github.com/eclipse/eclipse.jdt.ls/wiki/Running-the-JAVA-LS-server-from-the-command-line

## Lab pitfalls (10-mark set)

- `nextInt()` leaves a newline — call `nextLine()` before reading a string.
- Armstrong: raise each digit to the **number of digits**, not always 3; use
  `Math.abs` for negatives; cast `Math.pow` to int.
- Factorial: `long` overflows after 20!, negative `n` silently gives 1.
- Command-line args are Strings — `Integer.parseInt` before `Arrays.sort`
  (string sort puts `"10"` before `"2"`).
- `double / 0.0` gives `Infinity`, it does **not** throw `ArithmeticException`
  (only integer division does).
- `new File("numbers.txt")` resolves from the terminal cwd, not the `.java` file.
- Print doubles with `printf("%.2f%n", x)` to avoid `62.839999999999996`.
- `i`/`j` loops: decide 0-based vs 1-based once; diagonals are `i == j` and
  `i + j == n - 1` with 0-based loops; transpose uses `j` outer, `i` inner.
