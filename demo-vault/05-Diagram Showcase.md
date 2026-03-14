---
area: Plugin Compatibility
status: Ready
theme_section: Diagrams
---

# Diagram Showcase

This page checks Mermaid readability in both light mode and dark mode. The diagrams should stay aligned with the warm editorial feel of Sable Ledger while remaining obviously legible.

## Flowchart

```mermaid
graph TD
    A[Open note] --> B{Dark mode?}
    B -->|Yes| C[Use high-contrast diagram tokens]
    B -->|No| D[Use softer light-mode surfaces]
    C --> E[Readable labels]
    D --> E
```

## Sequence

```mermaid
sequenceDiagram
    participant User
    participant Theme
    participant Diagram
    User->>Theme: Toggle appearance
    Theme->>Diagram: Apply chart tokens
    Diagram-->>User: Preserve legibility
```

## Class

```mermaid
classDiagram
    class Theme {
        +accent
        +surface
        +text
        applyDiagramTokens()
    }
    class Mermaid {
        +render()
    }
    Theme --> Mermaid : styles
```

## State

```mermaid
stateDiagram-v2
    [*] --> Draft
    Draft --> Review
    Review --> Approved
    Review --> Draft
    Approved --> [*]
```

## ER

```mermaid
erDiagram
    NOTE ||--o{ DIAGRAM : contains
    DIAGRAM {
        string type
        string title
        string status
    }
    THEME ||--o{ DIAGRAM : styles
    THEME {
        string accent
        string surface
        string text
    }
```

## Journey

```mermaid
journey
    title Diagram review
    section Reading
      Open showcase note: 4: User
      Scan labels in dark mode: 5: User
    section Theme
      Check node contrast: 5: Theme
      Check connector contrast: 4: Theme
```

## Gantt

```mermaid
gantt
    title Theme refinement
    dateFormat  YYYY-MM-DD
    section Audit
    Inspect diagrams        :done, a1, 2026-03-13, 1d
    section Styling
    Add diagram tokens      :active, a2, 2026-03-14, 1d
    Add type-specific rules :a3, after a2, 1d
```

## Pie

```mermaid
pie title Diagram coverage
    "Flowchart" : 20
    "Sequence" : 15
    "Class" : 10
    "State" : 10
    "ER" : 10
    "Journey" : 10
    "Gantt" : 15
    "Other" : 10
```

## Git Graph

```mermaid
gitGraph
    commit id: "base"
    branch refine-diagrams
    checkout refine-diagrams
    commit id: "tokens"
    commit id: "contrast"
    checkout main
    merge refine-diagrams
```
