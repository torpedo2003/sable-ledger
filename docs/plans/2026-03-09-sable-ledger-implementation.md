# Sable Ledger Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Build a complete desktop-first Obsidian theme package and demo vault with Anthropic-inspired warm editorial aesthetics, light/dark support, and compatibility styling for Style Settings, Dataview, and Kanban.

**Architecture:** Keep the package build-free and CSS-first. Define a stable token system in `theme.css`, layer native Obsidian component styles on top of official CSS variables, then add plugin compatibility sections backed by the same tokens. Use a lightweight validation script plus fixture-style checks to catch packaging mistakes before visual review.

**Tech Stack:** Obsidian theme package (`manifest.json`, `theme.css`, `versions.json`), Markdown demo vault, Git, Python `unittest` for structural checks.

---

### Task 1: Scaffold package metadata and validation harness

**Files:**
- Create: `manifest.json`
- Create: `versions.json`
- Create: `tests/test_theme_structure.py`

**Step 1: Write the failing test**

Create `tests/test_theme_structure.py` with checks for:
- `manifest.json` exists and has `name`, `version`, `minAppVersion`, `author`, `authorUrl`, and `modes`
- `versions.json` exists and includes the manifest version key
- `theme.css` exists

**Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests/test_theme_structure.py -v`
Expected: FAIL because the package files do not exist yet.

**Step 3: Write minimal implementation**

Create `manifest.json` and `versions.json` with valid placeholder release metadata compatible with Obsidian theme packaging.

**Step 4: Run test to verify it passes**

Run: `python3 -m unittest tests/test_theme_structure.py -v`
Expected: PASS.

**Step 5: Commit**

Run:
```bash
git add manifest.json versions.json tests/test_theme_structure.py
git commit -m "feat: add theme package metadata"
```

### Task 2: Define light and dark design tokens

**Files:**
- Modify: `theme.css`
- Modify: `tests/test_theme_structure.py`

**Step 1: Write the failing test**

Extend the test file to assert that `theme.css` contains:
- a `theme-light` token section
- a `theme-dark` token section
- shared semantic tokens for text, background, border, accent, radius, and shadow

**Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests/test_theme_structure.py -v`
Expected: FAIL because `theme.css` is not implemented yet.

**Step 3: Write minimal implementation**

Create `theme.css` with:
- theme header comment
- light token block
- dark token block
- shared typography, spacing, and surface tokens

**Step 4: Run test to verify it passes**

Run: `python3 -m unittest tests/test_theme_structure.py -v`
Expected: PASS.

**Step 5: Commit**

Run:
```bash
git add theme.css tests/test_theme_structure.py
git commit -m "feat: add core light and dark tokens"
```

### Task 3: Style native Obsidian chrome and editor surfaces

**Files:**
- Modify: `theme.css`
- Create: `demo-vault/00-Start Here.md`
- Create: `demo-vault/01-Longform Reading.md`
- Modify: `tests/test_theme_structure.py`

**Step 1: Write the failing test**

Extend structural checks so `theme.css` must contain styling sections for:
- workspace chrome
- sidebars and tabs
- editor typography
- callouts, blockquotes, tables, and code blocks

Also assert the two demo notes exist.

**Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests/test_theme_structure.py -v`
Expected: FAIL because the new sections and notes do not exist yet.

**Step 3: Write minimal implementation**

Add CSS rules for the native app shell and note surfaces. Create two demo notes that exercise long-form reading, headings, lists, callouts, tables, and code.

**Step 4: Run test to verify it passes**

Run: `python3 -m unittest tests/test_theme_structure.py -v`
Expected: PASS.

**Step 5: Commit**

Run:
```bash
git add theme.css demo-vault/00-Start\ Here.md demo-vault/01-Longform\ Reading.md tests/test_theme_structure.py
git commit -m "feat: style native app surfaces"
```

### Task 4: Add plugin compatibility layers and demo fixtures

**Files:**
- Modify: `theme.css`
- Create: `demo-vault/02-Dataview Showcase.md`
- Create: `demo-vault/03-Kanban Showcase.md`
- Create: `demo-vault/04-Callouts and Tables.md`
- Create: `demo-vault/.obsidian/app.json`
- Create: `demo-vault/.obsidian/appearance.json`
- Modify: `tests/test_theme_structure.py`

**Step 1: Write the failing test**

Extend the tests to require:
- plugin styling markers for `Style Settings`, `Dataview`, and `Kanban`
- all demo notes and `.obsidian` config files exist

**Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests/test_theme_structure.py -v`
Expected: FAIL because plugin sections and demo fixtures are missing.

**Step 3: Write minimal implementation**

Add compatibility styling for the targeted plugins and create demo vault fixtures plus minimal Obsidian settings files that make the vault easy to preview.

**Step 4: Run test to verify it passes**

Run: `python3 -m unittest tests/test_theme_structure.py -v`
Expected: PASS.

**Step 5: Commit**

Run:
```bash
git add theme.css demo-vault tests/test_theme_structure.py
git commit -m "feat: add plugin compatibility fixtures"
```

### Task 5: Document installation and release readiness

**Files:**
- Modify: `README.md`
- Modify: `manifest.json`
- Modify: `versions.json`
- Modify: `theme.css`
- Modify: `tests/test_theme_structure.py`

**Step 1: Write the failing test**

Extend the tests to require:
- README installation instructions
- README mentions light mode, dark mode, demo vault, Dataview, Kanban, and Style Settings
- manifest and versions metadata stay in sync with the current version

**Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests/test_theme_structure.py -v`
Expected: FAIL until the documentation and metadata are complete.

**Step 3: Write minimal implementation**

Finish the README, verify release metadata, and tighten final CSS organization without changing the approved aesthetic direction.

**Step 4: Run test to verify it passes**

Run: `python3 -m unittest tests/test_theme_structure.py -v`
Expected: PASS.

**Step 5: Commit**

Run:
```bash
git add README.md manifest.json versions.json theme.css tests/test_theme_structure.py
git commit -m "docs: finalize theme packaging and usage"
```

### Task 6: Final verification pass

**Files:**
- Verify only: `manifest.json`
- Verify only: `versions.json`
- Verify only: `theme.css`
- Verify only: `demo-vault/`

**Step 1: Run structural verification**

Run: `python3 -m unittest tests/test_theme_structure.py -v`
Expected: PASS.

**Step 2: Run packaging sanity checks**

Run: `python3 - <<'PY'
import json, pathlib
root = pathlib.Path('.')
manifest = json.loads((root/'manifest.json').read_text())
versions = json.loads((root/'versions.json').read_text())
assert manifest['version'] in versions
assert (root/'theme.css').stat().st_size > 0
print('packaging ok')
PY`
Expected: `packaging ok`

**Step 3: Manual visual checklist**

Review in Obsidian:
- light mode in the demo vault
- dark mode in the demo vault
- Dataview note
- Kanban note
- typography and code blocks in Live Preview

**Step 4: Commit only if changes were needed**

Run:
```bash
git status --short
```
If any fixes were required after verification, commit them with a focused message.
