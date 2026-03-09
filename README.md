# Sable Ledger

Sable Ledger is an Obsidian theme inspired by Anthropic's warm editorial aesthetic. It is designed for quiet reading, serious note-taking, and a cleaner neutral palette across the native app UI.

This round also refines the theme against the visual direction of `code.claude.com`, especially the calmer product-doc treatment of typography, colors, and chrome.

## Highlights

- cleaner neutral palette instead of the warmer first draft
- Support for both light mode and dark mode
- Desktop-first layout tuned for reading and writing, with a default readable width of `1080px`
- sans-forward typography with `Anthropic Sans`-first local fallbacks
- lighter chrome and a more docs-like feel for tabs, headers, and controls
- Compatibility styling for Dataview and Kanban
- Style Settings support for line width, surface radius, and accent tuning
- Included demo vault for visual review and regression checking

## Installation

1. Open your Obsidian vault.
2. Go to `Settings` → `Appearance` → `Themes`.
3. Open your themes folder.
4. Copy `manifest.json`, `theme.css`, and `versions.json` into a folder named `Sable Ledger`.
5. Return to Obsidian and select `Sable Ledger` as the active CSS theme.

If you want to inspect the bundled demo vault, open `demo-vault/` as a separate vault from Obsidian's vault switcher.

## Modes

### light mode

Light mode now uses bone-white and pale stone neutrals, low-noise borders, and ink-like text. The goal is to feel closer to Claude's calmer public product surfaces instead of a bronze editorial layout, with lighter chrome around the content pane.

### dark mode

Dark mode now uses graphite-black neutrals and soft porcelain text instead of brown-heavy charcoal. It stays calm at night without looking sepia, and keeps the same docs-like feel in sidebars, headers, and controls.

## Plugin compatibility

### Style Settings

Sable Ledger exposes a small set of theme controls through Style Settings:

- readable line width
- surface radius
- light and dark accent colors
- stronger accent mode

The default readable line width is `1080px`, and the slider can extend the layout to `1240px` for wider desktop note panes.

### Dataview

Dataview tables, inline fields, task results, and error boxes inherit the same card, border, and typography language as native Obsidian surfaces.

### Kanban

Kanban lanes, cards, counts, and action buttons are styled to feel like part of the same editorial system rather than a separate UI layer.

## Demo vault

The demo vault is located in `demo-vault/` and includes:

- `00-Start Here.md`
- `01-Longform Reading.md`
- `02-Dataview Showcase.md`
- `03-Kanban Showcase.md`
- `04-Callouts and Tables.md`

Use the demo vault to review light mode, dark mode, Live Preview, tables, code blocks, Dataview output, and Kanban boards after each change.

## Development notes

- This theme follows Obsidian's official CSS variable guidance and sample theme packaging structure.
- The package is intentionally build-free: the source of truth is `theme.css`.
- Structural checks live in `tests/test_theme_structure.py`.

## Repository layout

- `manifest.json`
- `theme.css`
- `versions.json`
- `demo-vault/`
- `docs/plans/`
- `tests/test_theme_structure.py`
