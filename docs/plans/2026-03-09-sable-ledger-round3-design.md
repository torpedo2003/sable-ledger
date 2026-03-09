# Sable Ledger Round 3 Refinement Brief

Date: 2026-03-09
Status: Approved
Reference: https://code.claude.com/docs/zh-CN/overview

## Goal

Refine the theme toward the calmer, cleaner, more product-doc-like feel of the Claude Code docs site while preserving Obsidian usability in both light and dark modes.

## Reference cues

From inspection of the current Claude Code docs site and related Anthropic public pages:

- The docs use an Anthropic Sans-driven visual system
- Light mode is very bright and neutral, close to bone white
- Dark mode is deep graphite, not sepia
- Typography relies on sans-serif hierarchy rather than serif editorial contrast
- Chrome is quiet: tabs, nav, controls, and borders recede behind content
- Hover and active treatments are soft rounded surfaces, not strong cards

## Design direction

### Typography

- Promote a docs-like sans hierarchy by using `Anthropic Sans` as an optional first font with local system fallbacks
- Remove the remaining serif heading direction
- Tighten heading rhythm and improve large-title scaling
- Keep body text relaxed and readable in both light and dark modes

### Chrome

- Make sidebars and tab strips flatter and more native
- Reduce padding, border weight, and shadow on chrome surfaces
- Improve buttons and form controls so they feel closer to a product docs UI than a themed notebook skin

### Dual-mode quality bar

- Light mode should stay crisp and nearly white without turning sterile
- Dark mode should stay neutral and luminous without becoming too black or too brown
- Plugin surfaces must continue to inherit the same base system

## Validation

- Add CSS tests for typography and chrome markers
- Re-run the structural suite and packaging checks
- Keep the theme free of remote assets, `!important`, and `:has()`
