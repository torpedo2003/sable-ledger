# Sable Ledger Optimization Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Widen the markdown experience and retune the theme palette toward a cleaner Claude-like visual direction without breaking plugin compatibility.

**Architecture:** Keep the change CSS-first and minimal. Update structural tests first, then revise theme tokens and layout variables in `theme.css`, and finally adjust README guidance so the new defaults are documented. Prefer Obsidian's documented `--file-line-width` variable over custom-only width control.

**Tech Stack:** Obsidian theme CSS, Style Settings metadata comments, Python `unittest`, Markdown documentation.

---

### Task 1: Lock width expectations with tests

**Files:**
- Modify: `tests/test_theme_structure.py`
- Test: `tests/test_theme_structure.py`

**Step 1: Write the failing test**

Add assertions that `theme.css` contains:
- `--sl-readable-line-width: 1080px;`
- `--file-line-width: var(--sl-readable-line-width);`
- Style Settings slider default `1080`
- Style Settings slider max `1240`

**Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests/test_theme_structure.py -v`
Expected: FAIL because the current theme still uses `860px` and the old slider bounds.

**Step 3: Write minimal implementation**

Update `theme.css` width variables and Style Settings metadata to the approved values.

**Step 4: Run test to verify it passes**

Run: `python3 -m unittest tests/test_theme_structure.py -v`
Expected: PASS.

**Step 5: Commit**

```bash
git add theme.css tests/test_theme_structure.py
git commit -m "feat: widen readable line width defaults"
```

### Task 2: Lock palette direction with tests

**Files:**
- Modify: `tests/test_theme_structure.py`
- Test: `tests/test_theme_structure.py`

**Step 1: Write the failing test**

Add assertions that `theme.css` includes the new target palette markers:
- `--sl-color-bg-primary: #f7f5f2;`
- `--sl-color-bg-secondary: #f1efeb;`
- `--sl-color-text-normal: #1f1d1a;`
- `--sl-color-bg-primary: #151515;`
- `--sl-color-bg-secondary: #1b1b1a;`
- `--sl-color-text-normal: #f3efe8;`

**Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests/test_theme_structure.py -v`
Expected: FAIL because the current palette still uses the warmer first draft values.

**Step 3: Write minimal implementation**

Update light and dark token blocks, reduce background ornamentation, flatten shadows, and keep plugin styles mapped to the new neutral palette.

**Step 4: Run test to verify it passes**

Run: `python3 -m unittest tests/test_theme_structure.py -v`
Expected: PASS.

**Step 5: Commit**

```bash
git add theme.css tests/test_theme_structure.py
git commit -m "feat: refine palette toward cleaner neutrals"
```

### Task 3: Update documentation and re-verify package health

**Files:**
- Modify: `README.md`
- Modify: `tests/test_theme_structure.py`
- Test: `tests/test_theme_structure.py`

**Step 1: Write the failing test**

Extend README assertions to require mention of:
- wider readable width defaults
- cleaner neutral palette direction

**Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests/test_theme_structure.py -v`
Expected: FAIL until README is updated.

**Step 3: Write minimal implementation**

Update README so installation users understand the default desktop width and palette direction of the optimized theme.

**Step 4: Run test to verify it passes**

Run: `python3 -m unittest tests/test_theme_structure.py -v`
Expected: PASS.

**Step 5: Commit**

```bash
git add README.md tests/test_theme_structure.py
git commit -m "docs: describe optimized width and palette"
```
