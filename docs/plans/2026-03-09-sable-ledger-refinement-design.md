# Sable Ledger Refinement Design Brief

Date: 2026-03-09
Status: Approved
Scope: Chrome and typography refinement

## Goal

Bring the theme closer to the current Claude public-site feel by making the application chrome more invisible and the content typography more product-editorial.

## Observed gap

After the width and palette optimization, the remaining gap is mostly in two areas:

1. The application chrome still feels a little too themed, especially tabs, panels, and utility surfaces.
2. The note typography is readable but does not yet have the same calm, highly controlled product-copy rhythm seen on Claude and Anthropic public pages.

## Direction

Use the approved mixed approach:

- Flatten the chrome further
- Reduce border and shadow presence
- Make tabs slimmer and quieter
- Tighten titlebar and header weight
- Increase heading restraint and hierarchy clarity
- Slightly improve paragraph rhythm and list cadence
- Keep plugin styling stable instead of redesigning it again

## Chrome changes

### Sidebars and panels

- Reduce panel tinting so sidebars feel closer to the app background
- Keep separation through very soft borders and subtle active states
- Preserve usability for file trees and search results

### Tabs and header

- Reduce tab mass and padding
- Make active tabs feel selected through tone and type weight rather than surface heaviness
- Keep the view header thinner and less glossy

### Controls

- Ensure buttons and form fields feel native and quiet
- Keep focus states visible but understated

## Typography changes

### Headings

- Keep the serif heading family but reduce display drama
- Improve H1/H2/H3 size and spacing rhythm
- Use cleaner weight transitions between levels

### Body copy

- Slightly tighten overall measure now that width increased
- Improve paragraph spacing and list indentation rhythm
- Keep links elegant and low-noise

### Quotes and code

- Make quotes more document-like and less card-like
- Make code blocks cleaner and flatter while preserving scanability

## Validation

- Structural tests should assert new chrome and typography markers exist
- Manual review should focus on `00-Start Here` and `01-Longform Reading`
- Plugin demo notes should remain visually coherent after the refinement
