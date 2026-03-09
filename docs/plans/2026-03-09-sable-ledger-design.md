# Sable Ledger Design Brief

Date: 2026-03-09
Status: Approved
Theme name: Sable Ledger

## Goal

Build a complete Obsidian theme package plus a demo vault. The visual language should be inspired by Anthropic's website aesthetic without directly copying it. The outcome should feel editorial, warm, quiet, and credible, while remaining practical for daily knowledge work.

## Product scope

This first version includes:

- A standalone Obsidian theme package with `manifest.json` and `theme.css`
- Support for both light mode and dark mode
- A demo vault for visual review and regression checks
- Desktop-first layouts
- Compatibility work for common community plugins, especially `Style Settings`, `Dataview`, and `Kanban`

This first version does not include:

- A build pipeline unless needed later
- Remote assets such as web fonts or hosted images
- Mobile-first optimization
- Broad compatibility work for every plugin in the ecosystem

## Aesthetic direction

Recommended direction: original knowledge-work theme with Anthropic-inspired warmth.

Core descriptors:

- Warm minimal editorial
- Serious but soft
- Calm research-institute tone
- Paper-like surfaces, not glossy app chrome
- Conservative interaction feedback

The goal is not visual cloning. The goal is to produce a theme that plausibly feels like an original Obsidian theme designed with similar taste.

## Visual language

### Light mode

- Backgrounds use paper and oat tones rather than pure white
- Primary text uses deep graphite instead of true black
- Borders are low-contrast warm neutrals
- Elevated surfaces are subtle and rely more on spacing than shadow

### Dark mode

- Base background uses charcoal with a slight warm brown cast
- Text is warm ivory rather than cold blue-white
- Accent usage remains low-saturation and selective
- Contrast supports long reading sessions without harsh glow

### Accent philosophy

- Accent color is restrained and earthy
- The initial accent family will explore terracotta, copper, and sand
- Accent tokens should be sparse and purposeful: links, focus states, selections, and primary emphasis only

## Typography

- Prefer native system font stacks for performance and reliability
- Body text should optimize reading comfort over density
- Heading hierarchy should feel editorial and deliberate
- Code text should remain crisp, neutral, and easy to scan

## Component principles

### Core app chrome

- Sidebars visually recede so the note body becomes the center of attention
- Tabs feel like document tabs rather than browser tabs
- Inputs and buttons use quiet outlines and moderate corner radii
- Status and utility surfaces should look integrated, not detached

### Reading and editing

- Reading mode and Live Preview should align closely
- Spacing changes in Live Preview must prefer padding over margin to avoid editor glitches
- Lists, quotes, callouts, and tables should read like composed documents
- Code blocks should feel embedded in the page, not pasted from a different theme

### Plugin compatibility

- `Style Settings`: expose a limited set of practical controls, such as radius, accent intensity, and readable line width
- `Dataview`: style tables, lists, inline fields, and task results with the same structural language as native notes
- `Kanban`: style boards, columns, cards, and selection states so they look native to the theme

## Technical constraints

This project should follow Obsidian's official theme guidance.

### Official guidance to follow

- Prefer overriding built-in CSS variables over relying on brittle selectors
- Avoid `!important` unless absolutely necessary
- Avoid changing vertical margins on classes used in Live Preview; use padding instead
- Avoid `:has()` unless there is no reasonable alternative due to performance concerns
- Keep assets local; do not depend on remote fonts or remote images
- Keep release screenshots small; recommended thumbnail size is 512 x 288

### Repository and packaging

The repository should include:

- `manifest.json`
- `theme.css`
- `README.md`
- `versions.json`
- `docs/plans/`
- `demo-vault/`

## Information architecture

Recommended repository structure:

```text
sable-ledger/
├── manifest.json
├── theme.css
├── versions.json
├── README.md
├── docs/
│   └── plans/
│       └── 2026-03-09-sable-ledger-design.md
└── demo-vault/
    ├── 00-Start Here.md
    ├── 01-Longform Reading.md
    ├── 02-Dataview Showcase.md
    ├── 03-Kanban Showcase.md
    ├── 04-Callouts and Tables.md
    └── .obsidian/
```

## Validation strategy

### Visual validation

Use the demo vault as the acceptance environment for both light and dark themes. Review the following after each major styling milestone:

- Core layout and sidebars
- Reading view and Live Preview
- Headings, lists, tables, callouts, and code blocks
- Dataview result pages
- Kanban board pages

### Structural validation

- Confirm the repository matches the minimum Obsidian theme package structure
- Confirm the theme loads without relying on a build step
- Confirm naming and metadata fields are valid for release preparation

### Regression strategy

Each time a new styling layer is added, revisit all demo notes in both light and dark modes to catch regressions early.

## Git workflow

- Create a dedicated Git repository for the theme
- Commit the approved design brief before implementation
- Implement in small, reviewable commits
- Keep the main branch in a usable state

## Implementation plan handoff

After this document is committed, the next phase is to write a detailed implementation plan and then build the theme using the approved constraints above.
