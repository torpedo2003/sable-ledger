# Sable Ledger Refinement Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Refine the application chrome and typography so the theme feels quieter, more native, and more aligned with Claude's current public-site tone.

**Architecture:** Keep the work CSS-only and narrowly scoped. Add tests for the approved chrome and typography markers first, then adjust shared tokens and the native app sections of `theme.css`, and finally re-run the structural checks and package sanity checks.

**Tech Stack:** Obsidian theme CSS, Style Settings metadata comments, Python `unittest`, Markdown documentation.

---

### Task 1: Lock chrome refinement expectations with tests

**Files:**
- Modify: `tests/test_theme_structure.py`
- Test: `tests/test_theme_structure.py`

**Step 1: Write the failing test**

Add assertions that `theme.css` contains the new approved chrome markers:
- `--sl-panel-alpha`
- `--sl-tab-alpha`
- `--sl-header-height`
- `padding: 0.3rem 0.45rem 0;`
- `min-height: var(--sl-header-height);`

**Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests/test_theme_structure.py -v`
Expected: FAIL because the current chrome still uses the previous values and does not define these markers.

**Step 3: Write minimal implementation**

Add the chrome tokens and update the native app shell sections to use them.

**Step 4: Run test to verify it passes**

Run: `python3 -m unittest tests/test_theme_structure.py -v`
Expected: PASS.

**Step 5: Commit**

```bash
git add theme.css tests/test_theme_structure.py
git commit -m "feat: refine app chrome surfaces"
```

### Task 2: Lock typography refinement expectations with tests

**Files:**
- Modify: `tests/test_theme_structure.py`
- Test: `tests/test_theme_structure.py`

**Step 1: Write the failing test**

Add assertions that `theme.css` contains the new approved typography markers:
- `--sl-body-measure: 72ch;`
- `--h1-size: 2.45rem;`
- `--h2-size: 1.72rem;`
- `--h3-size: 1.28rem;`
- `text-underline-offset: 0.16em;`
- `padding: 0.8rem 0.95rem;`

**Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests/test_theme_structure.py -v`
Expected: FAIL because the current typography does not define these markers.

**Step 3: Write minimal implementation**

Update typography variables and the editor content rules to use the refined heading scale, paragraph rhythm, quote treatment, and flatter code spacing.

**Step 4: Run test to verify it passes**

Run: `python3 -m unittest tests/test_theme_structure.py -v`
Expected: PASS.

**Step 5: Commit**

```bash
git add theme.css tests/test_theme_structure.py
git commit -m "feat: refine typography rhythm"
```

### Task 3: Final verification

**Files:**
- Verify only: `theme.css`
- Verify only: `tests/test_theme_structure.py`

**Step 1: Run structural verification**

Run: `python3 -m unittest tests/test_theme_structure.py -v`
Expected: PASS.

**Step 2: Run package sanity checks**

Run: `python3 - <<'PY'
import json, pathlib
root = pathlib.Path('.')
manifest = json.loads((root/'manifest.json').read_text())
versions = json.loads((root/'versions.json').read_text())
assert manifest['version'] in versions
assert versions[manifest['version']] == manifest['minAppVersion']
assert (root/'theme.css').stat().st_size > 0
print('packaging ok')
PY`
Expected: `packaging ok`
