# Sable Ledger

中文 | [English](#english)

Sable Ledger 是一个受 Anthropic / Claude 视觉语言启发的 Obsidian 主题，面向长文阅读、研究笔记、知识整理与写作场景。它强调 cleaner neutral palette、克制的排版、精致的浅色与深色模式、稳定的 Markdown 渲染，以及接近 Claude 文档与对话界面的阅读气质。

## 特色

- 支持浅色 / 深色双模式，并分别做了细致调校
- 视觉方向受 Anthropic、Claude 与 `code.claude.com` 启发
- 保留 `code.claude.com` 风格中的 sans-forward typography、lighter chrome 与 docs-like feel
- 默认阅读宽度为 `1080px`，适合桌面端长文阅读与写作
- 优化标题、正文、代码块、表格、Mermaid 图表、侧边栏与顶部 chrome
- 支持 `Anthropic Sans` / `Anthropic Sans Text` 本地字体优先回退
- 对 `Dataview`、`Kanban`、`Style Settings` 做了兼容性打磨
- 附带一个 `demo-vault/` 用于视觉验收与回归检查

## 安装

1. 打开你的 Obsidian vault。
2. 进入 `设置` → `外观` → `主题`。
3. 打开主题文件夹。
4. 在主题目录里创建一个名为 `Sable Ledger` 的文件夹。
5. 将以下三个文件复制进去：
   - `manifest.json`
   - `theme.css`
   - `versions.json`
6. 回到 Obsidian，在主题列表中启用 `Sable Ledger`。

如果你想直接查看演示内容，可以把 `demo-vault/` 作为单独 vault 打开；也就是仓库内置的 demo vault。

## 模式说明

### 浅色模式

浅色模式采用接近骨白、纸灰与石墨黑的中性体系，减少噪声感，让内容比界面更先进入视线。它更接近 Claude 公共页面和文档站那种克制、清晰、安静的阅读气质。

### 深色模式

深色模式采用更中性的石墨黑与柔和浅字，而不是偏棕的暗色界面。目标是在夜间也保持清晰和舒适，同时避免界面显得发灰或发脏。

## 插件兼容

### Style Settings

Sable Ledger 暴露了一些实用但克制的可调参数：

- 阅读宽度
- 圆角大小
- 浅色 / 深色强调色
- 更强强调模式

### Dataview

Dataview 的表格、任务、内联字段与错误框会继承统一的主题语言，而不是看起来像外挂控件。

### Kanban

Kanban 的列、卡片、计数和操作按钮都做了统一化处理，让它们尽量融入主题，而不是成为另一套视觉系统。

## Demo Vault

`demo-vault/` 包含以下演示页面：

- `00-Start Here.md`
- `01-Longform Reading.md`
- `02-Dataview Showcase.md`
- `03-Kanban Showcase.md`
- `04-Callouts and Tables.md`

建议在每次大改后，用这些页面检查：

- 浅色模式
- 深色模式
- Live Preview
- 代码块与复制按钮
- 表格与 Mermaid 图表
- Dataview / Kanban 效果

## 开发说明

- 主题采用纯 CSS 方案，不依赖构建步骤
- 样式主文件为 `theme.css`
- 结构化检查位于 `tests/test_theme_structure.py`
- 仓库中保留了多轮设计与实现计划，便于后续继续迭代

## 仓库结构

- `manifest.json`
- `theme.css`
- `versions.json`
- `README.md`
- `demo-vault/`
- `docs/plans/`
- `tests/test_theme_structure.py`

## 许可与使用

当前仓库未单独声明许可证文件；如需公开分发与社区发布，建议后续补充许可证与发布说明。

---

## English

Sable Ledger is an Obsidian theme inspired by Anthropic and Claude’s visual language. It is designed for long-form reading, research notes, knowledge management, and writing workflows, with a focus on restrained typography, polished light/dark modes, and refined markdown rendering.

## Highlights

- Carefully tuned light mode and dark mode
- Visual direction inspired by Anthropic, Claude, and `code.claude.com`
- Desktop-first reading layout with a default readable width of `1080px`
- Refined typography, code blocks, tables, Mermaid charts, sidebars, and top chrome
- Local-first font stack with `Anthropic Sans` / `Anthropic Sans Text` fallbacks
- Compatibility polish for `Dataview`, `Kanban`, and `Style Settings`
- Bundled `demo-vault/` for visual review and regression checks, i.e. the included demo vault

## Installation

1. Open your Obsidian vault.
2. Go to `Settings` → `Appearance` → `Themes`.
3. Open the themes folder.
4. Create a folder named `Sable Ledger`.
5. Copy these files into it:
   - `manifest.json`
   - `theme.css`
   - `versions.json`
6. Return to Obsidian and enable `Sable Ledger`.

If you want to preview the bundled examples, open `demo-vault/` as a separate vault.

## Modes

### light mode

Light mode uses bone-white, soft stone, and graphite tones to keep the interface quiet and content-first. The goal is to feel closer to Claude’s calm documentation and product pages than a decorative blog theme.

### dark mode

Dark mode uses more neutral graphite surfaces and soft high-contrast text rather than brown-heavy dark styling. It is tuned for clarity, comfort, and a cleaner late-night reading experience.

## Plugin Compatibility

### Style Settings

Sable Ledger exposes a small set of practical controls:

- readable line width
- surface radius
- light and dark accent colors
- stronger accent mode

### Dataview

Dataview tables, tasks, inline fields, and error boxes inherit the theme’s core visual language instead of feeling like external widgets.

### Kanban

Kanban lanes, cards, counts, and actions are styled to feel native to the same system.

## Demo Vault

The `demo-vault/` includes:

- `00-Start Here.md`
- `01-Longform Reading.md`
- `02-Dataview Showcase.md`
- `03-Kanban Showcase.md`
- `04-Callouts and Tables.md`

Use it to review:

- light mode
- dark mode
- Live Preview
- code blocks and copy controls
- tables and Mermaid charts
- Dataview / Kanban rendering

## Development Notes

- The theme is CSS-first and build-free
- The main stylesheet lives in `theme.css`
- Structural checks live in `tests/test_theme_structure.py`
- The repository keeps multiple design and implementation plans for future iterations

## Repository Layout

- `manifest.json`
- `theme.css`
- `versions.json`
- `README.md`
- `demo-vault/`
- `docs/plans/`
- `tests/test_theme_structure.py`

## License

No standalone license file is included yet. If you plan to distribute the project publicly or publish it to a theme gallery, adding a license and release notes is recommended.
