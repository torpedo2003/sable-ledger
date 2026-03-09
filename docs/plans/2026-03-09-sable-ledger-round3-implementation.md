# Sable Ledger Round 3 Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Refine the theme's typography and app chrome toward the Claude Code docs aesthetic while preserving the widened layout and dual-mode usability.

**Architecture:** Extend the existing CSS token system instead of rewriting the theme. Add tests that lock in the new font direction and chrome density, then update `theme.css` and finally document the refined direction in the README.

**Tech Stack:** Obsidian theme CSS, Python `unittest`, Markdown documentation.

---

### Task 1: Lock typography and chrome expectations with tests

**Files:**
- Modify: `tests/test_theme_structure.py`
- Test: `tests/test_theme_structure.py`

**Step 1: Write the failing test**

Require markers for:
- `Anthropic Sans`-first font stacks
- sans-serif heading stack replacing the earlier serif direction
- tighter tab container padding
- refined heading scale markers

**Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests/test_theme_structure.py -v`
Expected: FAIL because the current theme still uses the earlier heading stack and looser chrome values.

**Step 3: Write minimal implementation**

Update font stacks, heading rhythm, and tab/header spacing in `theme.css`.

**Step 4: Run test to verify it passes**

Run: `python3 -m unittest tests/test_theme_structure.py -v`
Expected: PASS.

**Step 5: Commit**

```bash
git add theme.css tests/test_theme_structure.py
git commit -m "feat: refine typography and chrome rhythm"
```

### Task 2: Update docs and re-verify

**Files:**
- Modify: `README.md`
- Modify: `tests/test_theme_structure.py`

**Step 1: Write the failing test**

Require README mention of:
- `code.claude.com` inspired refinement
- sans-forward typography
- lighter chrome / docs-like feel

**Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests/test_theme_structure.py -v`
Expected: FAIL until the README is updated.

**Step 3: Write minimal implementation**

Update README to describe the refined design direction.

**Step 4: Run test to verify it passes**

Run: `python3 -m unittest tests/test_theme_structure.py -v`
Expected: PASS.

**Step 5: Commit**

```bash
git add README.md tests/test_theme_structure.py
git commit -m "docs: describe round 3 refinement"
```
