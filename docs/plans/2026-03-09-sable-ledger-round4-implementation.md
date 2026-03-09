# Sable Ledger Round 4 Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Preserve the current theme as a checkpoint, then fix image centering in the active vault, redesign code blocks closer to Claude chat markdown output, and remove mismatched shaded corner chrome in the Obsidian window.

**Architecture:** Keep the theme changes narrow and CSS-first. Treat image centering as a vault-level snippet issue with a DOM-selector mismatch, and treat the code block plus corner-shadow issues as theme regressions solved in `theme.css`. Add structural tests for the theme-side changes, then sync the final CSS into the active vault theme install.

**Tech Stack:** Obsidian theme CSS, Obsidian vault CSS snippet, Python `unittest`, Git.

---

### Task 1: Lock code block and corner fixes with tests

**Files:**
- Modify: `tests/test_theme_structure.py`
- Test: `tests/test_theme_structure.py`

**Step 1: Write the failing test**

Require markers for:
- Claude-like code block shell tokens
- code block header row treatment
- flatter container border style
- titlebar and ribbon corner normalization selectors

**Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests/test_theme_structure.py -v`
Expected: FAIL because the current theme does not yet include the new markers.

**Step 3: Write minimal implementation**

Update `theme.css` with the new code block shell and top-corner normalization rules.

**Step 4: Run test to verify it passes**

Run: `python3 -m unittest tests/test_theme_structure.py -v`
Expected: PASS.

**Step 5: Commit**

```bash
git add theme.css tests/test_theme_structure.py
git commit -m "feat: refine code blocks and top chrome"
```

### Task 2: Fix active vault image centering snippet

**Files:**
- Modify: `/Users/leiyu/Library/Mobile Documents/iCloud~md~obsidian/Documents/Papers-Vault/.obsidian/snippets/center-images.css`
- Modify: `/Users/leiyu/Library/Mobile Documents/iCloud~md~obsidian/Documents/Papers-Vault/.obsidian/appearance.json`

**Step 1: Create the failing reproduction hypothesis**

Record that the current snippet only targets `.image-embed` and misses raw markdown images plus some embed wrappers in reading and live preview.

**Step 2: Verify current configuration**

Run commands that print the current snippet and enabled snippet list.
Expected: snippet exists and is enabled, but selector coverage is too narrow.

**Step 3: Write minimal implementation**

Replace the snippet with centered rules that cover raw markdown images, internal image embeds, and live preview wrappers while staying scoped only to images.

**Step 4: Verify the new snippet file**

Run commands that print the final snippet and enabled list.
Expected: the new selectors are present and `center-images` remains enabled.

### Task 3: Sync theme into the active vault and run final verification

**Files:**
- Modify: `/Users/leiyu/Library/Mobile Documents/iCloud~md~obsidian/Documents/Papers-Vault/.obsidian/themes/Sable Ledger/theme.css`
- Verify only: `tests/test_theme_structure.py`

**Step 1: Sync latest theme CSS into the installed vault theme**

Copy the repository `theme.css` into the active vault theme directory.

**Step 2: Run final verification**

Run:
- `python3 -m unittest tests/test_theme_structure.py -v`
- a packaging sanity check
- grep checks for the synced vault theme and snippet

Expected: all tests pass and synced files contain the new markers.
