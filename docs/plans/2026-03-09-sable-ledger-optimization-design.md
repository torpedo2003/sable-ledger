# Sable Ledger Optimization Design Brief

Date: 2026-03-09
Status: Approved
Scope: Width and palette refinement

## Problem statement

The first version landed with two user-visible issues:

1. The markdown content area feels too narrow on desktop.
2. The light and dark palettes feel too warm and too editorial, drifting away from the calmer, cleaner direction of Anthropic's current public surfaces.

## Root cause

### Width

The theme currently hard-limits the main reading and editing surface with a custom width token set to `860px`. That value is too narrow for the desired desktop-first experience. It also duplicates behavior that Obsidian already exposes through `--file-line-width`.

### Palette

The current palette leans on oat, terracotta, and brown-charcoal values. That creates a cozy editorial mood, but it is more nostalgic than the cleaner Claude-like aesthetic requested by the user.

## Design direction

Adopt a cleaner Anthropic-inspired direction while preserving Obsidian usability.

Core descriptors:

- Bone-white light surfaces rather than oat paper
- Ink and graphite text rather than brown-black text
- Minimal warm accent, not copper-forward accent
- Wider, calmer reading surface on desktop
- Lower texture, lower shadow, lower visual noise

## Width strategy

Follow Obsidian's own readable-width variable instead of only styling internal containers.

Implementation intent:

- Set `--file-line-width` to a wider default
- Keep a theme-level variable for Style Settings control
- Raise default width to `1080px`
- Keep maximum slider value at `1240px`
- Retain centered reading without forcing near-full-width behavior

This aligns with Obsidian's documented `--file-line-width` variable for readable line width behavior.

## Palette strategy

### Light mode

Shift from warm oat to restrained bone and chalk neutrals:

- Primary background near soft bone white
- Secondary surfaces near pale stone grey
- Text near graphite / ink
- Borders near cool warm-grey rather than brown
- Accent near muted taupe-sand instead of terracotta

### Dark mode

Shift from warm brown charcoal to graphite-black neutral dark mode:

- Primary background near deep graphite
- Secondary surfaces near charcoal slate
- Text near soft porcelain
- Borders near subtle smoke grey
- Accent near quiet warm stone

## Surface and interaction strategy

- Remove decorative radial background treatment from the main app canvas
- Reduce card and floating shadows
- Make tabs and sidebars flatter and more native
- Keep code blocks and callouts distinct but quieter
- Preserve plugin compatibility by reusing the same tokens

## Validation strategy

### Structural checks

- Confirm width defaults changed in both theme CSS and Style Settings metadata
- Confirm the theme defines Obsidian's `--file-line-width`

### Visual checks

Review in both modes:

- long-form reading note
- tab strip and sidebars
- Dataview table note
- Kanban board note

## References

- Obsidian documents `--file-line-width` as the variable controlling line width when readable line width is enabled
- Anthropic and Claude public product pages currently present a visually cleaner and less bronze-heavy aesthetic than the first draft of this theme
