---
area: Plugin Compatibility
status: Ready
theme_section: Dataview
---

# Dataview Showcase

This note exists to inspect how `Dataview` tables, task lists, inline fields, and error surfaces inherit the same editorial system as native notes.

## Inline field preview

Project:: Sable Ledger
Mode:: Light + Dark
Priority:: High

## Table query

```dataview
TABLE area, status, theme_section
FROM ""
WHERE contains(theme_section, "")
SORT file.name ASC
```

## Task query

```dataview
TASK
FROM ""
WHERE !completed
```

## Notes

- The table should feel like a native Obsidian table.
- Inline fields should look intentionally tagged, not default blue pills.
- Error boxes should remain readable and restrained.
