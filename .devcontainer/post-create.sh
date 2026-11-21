#!/usr/bin/env bash
set -euo pipefail

# The mise devcontainer feature installs the `mise` binary (to /usr/local/bin)
# but does NOT set up shell activation or install the project's tools.
# As a result `mise` itself is available in a fresh Codespace, but the tools
# declared in mise.toml (node, opencode) never make it onto PATH.
# This script wires both pieces up once, when the container is created.

MISE_BIN="$(command -v mise || true)"
if [[ -z "$MISE_BIN" ]]; then
  echo "post-create: mise not found on PATH; check the mise devcontainer feature." >&2
  exit 1
fi

# Resolve the workspace folder relative to this script (.devcontainer/ -> repo root).
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE_DIR="$(dirname "$SCRIPT_DIR")"

# --- 1. Shell activation (idempotent) ---------------------------------------
# Future interactive terminals source this and get mise's tool dirs + shims
# onto PATH whenever the working directory changes.
activate_bash='eval "$(mise activate bash)"'
if ! grep -qF "$activate_bash" "$HOME/.bashrc" 2>/dev/null; then
  printf '\n# mise activation (added by devcontainer postCreateCommand)\n%s\n' \
    "$activate_bash" >> "$HOME/.bashrc"
fi

if [[ -f "$HOME/.zshrc" ]]; then
  activate_zsh='eval "$(mise activate zsh)"'
  if ! grep -qF "$activate_zsh" "$HOME/.zshrc"; then
    printf '\n# mise activation (added by devcontainer postCreateCommand)\n%s\n' \
      "$activate_zsh" >> "$HOME/.zshrc"
  fi
fi

# --- 2. zsh plugins (oh-my-zsh) ----------------------------------------------
# The base image ships oh-my-zsh with only the `git` plugin enabled. Install
# zsh-autosuggestions and zsh-syntax-highlighting from their latest branches
# and enable them in ~/.zshrc so they are ready in the first zsh terminal.
if [[ -f "$HOME/.zshrc" ]] && command -v git >/dev/null 2>&1; then
  ZSH_CUSTOM_DIR="${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}"
  AUTOSUGGESTIONS_DIR="$ZSH_CUSTOM_DIR/plugins/zsh-autosuggestions"
  SYNTAX_HIGHLIGHTING_DIR="$ZSH_CUSTOM_DIR/plugins/zsh-syntax-highlighting"

  clone_plugin() {
    local url="$1" dir="$2" plugin_file="$3"
    if [[ -e "$dir" && ! -f "$dir/$plugin_file" ]]; then
      rm -rf "$dir"   # replace an incomplete/foreign checkout
    fi
    if [[ ! -f "$dir/$plugin_file" ]]; then
      mkdir -p "$(dirname "$dir")"
      git clone --depth 1 "$url" "$dir"
    fi
  }

  clone_plugin https://github.com/zsh-users/zsh-autosuggestions.git \
    "$AUTOSUGGESTIONS_DIR" zsh-autosuggestions.plugin.zsh
  clone_plugin https://github.com/zsh-users/zsh-syntax-highlighting.git \
    "$SYNTAX_HIGHLIGHTING_DIR" zsh-syntax-highlighting.zsh

  # Add plugins idempotently. Syntax highlighting must be loaded LAST.
  if grep -q '^plugins=' "$HOME/.zshrc"; then
    if ! grep -qE '^plugins=\([^)]*zsh-autosuggestions' "$HOME/.zshrc"; then
      sed -i -E 's/^plugins=\(([^)]*)\)/plugins=(zsh-autosuggestions \1)/' "$HOME/.zshrc"
    fi
    if ! grep -qE '^plugins=\([^)]*zsh-syntax-highlighting' "$HOME/.zshrc"; then
      sed -i -E 's/^plugins=\(([^)]*)\)/plugins=(\1 zsh-syntax-highlighting)/' "$HOME/.zshrc"
    fi
  fi
fi

# --- 3. Install the shared toolchain with mise (GLOBAL) ----------------------
# The tracked mise.toml is the single source of truth for every new Codespace.
# Copying it to mise's global config makes its tools available everywhere
# (not only inside the workspace folder), then install them. Personal overrides
# can still live in .mise.toml (gitignored).
cd "$WORKSPACE_DIR"
mkdir -p "$HOME/.config/mise"
if [[ -f "mise.toml" ]]; then
  cp "mise.toml" "$HOME/.config/mise/config.toml"
elif [[ -f ".mise.toml" ]]; then
  cp ".mise.toml" "$HOME/.config/mise/config.toml"
else
  # Fallback for repositories without a tracked toolchain: a usable baseline.
  printf '[tools]\nnode = "latest"\n' > "$HOME/.config/mise/config.toml"
fi
mise trust   # avoid an interactive trust prompt in a fresh Codespace
mise install # installs every tool declared in the global config

# --- 4. Neovim via mise + LazyVim starter ------------------------------------
# Neovim is installed/managed by mise (not apt/vim), configured with the
# official LazyVim starter, and exposed as `vi` via a normal shell alias.
if command -v git >/dev/null 2>&1; then
  # Neovim is installed globally from the tracked mise.toml in section 3.

  # LazyVim starter per https://lazyvim.github.io/installation
  if [[ ! -f "$HOME/.config/nvim/lua/config/lazy.lua" ]]; then
    if [[ -e "$HOME/.config/nvim" ]]; then
      mv "$HOME/.config/nvim" "$HOME/.config/nvim.bak.$(date +%s)"
    fi
    git clone https://github.com/LazyVim/starter.git "$HOME/.config/nvim"
    rm -rf "$HOME/.config/nvim/.git"
  fi

  # Best effort: pre-fetch LazyVim plugins so the first launch is ready.
  # Use `mise exec` because the shims are not on PATH in this non-interactive
  # shell yet (the activation line only takes effect in new terminals).
  if [[ -x "$HOME/.local/share/mise/shims/nvim" ]]; then
    mise exec -- nvim --headless "+Lazy! sync" +qa >/dev/null 2>&1 || \
      echo "post-create: LazyVim plugin sync deferred to first nvim launch." >&2
  fi
fi

# Normal shell alias (not a mise shell_alias): vi -> the mise-installed nvim.
alias_line='alias vi="nvim"'
for rc in "$HOME/.zshrc" "$HOME/.bashrc"; do
  if [[ -f "$rc" ]] && ! grep -qF "$alias_line" "$rc"; then
    printf '\n# Neovim (installed via mise) as the default vi\nalias vi="nvim"\n' >> "$rc"
  fi
done

# --- 5. zoxide shell integration ---------------------------------------------
# zoxide itself is installed globally from the tracked mise.toml in section 3.
# Smarter cd, managed by mise. zoxide docs: add `eval "$(zoxide init zsh)"`
# to the zsh startup file. Appended after the mise activation line above so
# `zoxide` is on PATH when this runs.
zoxide_line='eval "$(zoxide init zsh)"'
if [[ -f "$HOME/.zshrc" ]] && ! grep -qF "$zoxide_line" "$HOME/.zshrc"; then
  printf '\n# zoxide (installed via mise)\n%s\n' "$zoxide_line" >> "$HOME/.zshrc"
fi

zoxide_bash_line='eval "$(zoxide init bash)"'
if [[ -f "$HOME/.bashrc" ]] && ! grep -qF "$zoxide_bash_line" "$HOME/.bashrc"; then
  printf '\n# zoxide (installed via mise)\n%s\n' "$zoxide_bash_line" >> "$HOME/.bashrc"
fi

# --- 6. Protect the shared baseline from codespace-local edits --------------
# Mark every tracked file skip-worktree so anything changed inside a codespace
# (tool configs, experiments, local paths) is silently ignored by git and can
# never be committed back to the generic baseline. New/untracked files are
# unaffected. This keeps each codespace from polluting the next one.
if command -v git >/dev/null 2>&1 && git -C "$WORKSPACE_DIR" rev-parse --git-dir >/dev/null 2>&1; then
  git -C "$WORKSPACE_DIR" ls-files -z | \
    xargs -0 -r git -C "$WORKSPACE_DIR" update-index --skip-worktree --
fi

echo "post-create: mise activated with the shared global toolchain (btop, node, opencode, neovim, zoxide); LazyVim + vi alias, zsh plugins and zoxide shell integration enabled; tracked files locked with skip-worktree."
