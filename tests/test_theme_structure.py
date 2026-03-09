import json
import pathlib
import unittest


ROOT = pathlib.Path(__file__).resolve().parent.parent


class ThemeStructureTests(unittest.TestCase):
    def test_manifest_exists_and_contains_required_fields(self) -> None:
        manifest_path = ROOT / "manifest.json"
        self.assertTrue(manifest_path.exists(), "manifest.json must exist")

        manifest = json.loads(manifest_path.read_text())
        for field in ["name", "version", "minAppVersion", "author", "authorUrl", "modes"]:
            self.assertIn(field, manifest)

    def test_versions_exists_and_includes_manifest_version(self) -> None:
        manifest_path = ROOT / "manifest.json"
        versions_path = ROOT / "versions.json"

        self.assertTrue(manifest_path.exists(), "manifest.json must exist")
        self.assertTrue(versions_path.exists(), "versions.json must exist")

        manifest = json.loads(manifest_path.read_text())
        versions = json.loads(versions_path.read_text())

        self.assertIn(manifest["version"], versions)

    def test_theme_css_exists(self) -> None:
        self.assertTrue((ROOT / "theme.css").exists(), "theme.css must exist")

    def test_theme_css_defines_light_dark_and_shared_tokens(self) -> None:
        theme_css = (ROOT / "theme.css").read_text()

        for marker in [
            "body.theme-light",
            "body.theme-dark",
            "--sl-color-text-normal",
            "--sl-color-bg-primary",
            "--sl-color-border-muted",
            "--sl-color-accent",
            "--sl-radius-m",
            "--sl-shadow-surface",
        ]:
            self.assertIn(marker, theme_css)

    def test_theme_css_uses_wider_readable_width_defaults(self) -> None:
        theme_css = (ROOT / "theme.css").read_text()

        for marker in [
            "--sl-readable-line-width: 1080px;",
            "--file-line-width: var(--sl-readable-line-width);",
            "default: 1080",
            "max: 1240",
        ]:
            self.assertIn(marker, theme_css)

    def test_theme_css_uses_cleaner_neutral_palette_markers(self) -> None:
        theme_css = (ROOT / "theme.css").read_text()

        for marker in [
            "--sl-color-bg-primary: #f7f5f2;",
            "--sl-color-bg-secondary: #f1efeb;",
            "--sl-color-text-normal: #1f1d1a;",
            "--sl-color-bg-primary: #151515;",
            "--sl-color-bg-secondary: #1b1b1a;",
            "--sl-color-text-normal: #f3efe8;",
            "background: var(--background-primary);",
        ]:
            self.assertIn(marker, theme_css)

    def test_theme_css_refines_typography_and_chrome_toward_claude_docs(self) -> None:
        theme_css = (ROOT / "theme.css").read_text()

        for marker in [
            '--sl-font-interface: "Anthropic Sans", "Anthropic Sans Text",',
            '--sl-font-heading: "Anthropic Sans", "Anthropic Sans Text",',
            'padding: 0.35rem 0.45rem 0;',
            'backdrop-filter: blur(6px);',
            'font-size: 2.45rem;',
            'font-size: 1.86rem;',
            'font-size: 1.46rem;',
        ]:
            self.assertIn(marker, theme_css)

        self.assertNotIn('Iowan Old Style', theme_css)

    def test_theme_css_refines_codeblocks_and_top_corner_chrome(self) -> None:
        theme_css = (ROOT / "theme.css").read_text()

        for marker in [
            '--sl-code-shell-bg',
            '--sl-code-shell-header',
            '.markdown-rendered pre::before',
            '.code-block-flair',
            '.markdown-source-view.mod-cm6 .cm-line.HyperMD-codeblock',
            '.titlebar-button-container.mod-left',
            '.titlebar-button-container.mod-right',
        ]:
            self.assertIn(marker, theme_css)

    def test_theme_css_polishes_codeblock_button_table_rows_and_mermaid_pie(self) -> None:
        theme_css = (ROOT / "theme.css").read_text()

        for marker in [
            'top: 0.08rem;',
            'display: flex;',
            'align-items: flex-start;',
            'button.copy-code-button .code-block-flair',
            '.markdown-rendered tbody tr:nth-child(odd),',
            '.markdown-rendered tbody tr:nth-child(odd) > td',
            '.markdown-rendered tbody tr:nth-child(even),',
            '.markdown-rendered tbody tr:nth-child(even) > td',
            '.table-view-table tbody tr:nth-child(odd),',
            '.table-view-table tbody tr:nth-child(odd) > td',
            '.table-view-table tbody tr:nth-child(even),',
            '.table-view-table tbody tr:nth-child(even) > td',
            'background: inherit;',
            '.mermaid svg',
            '.mermaid .pieTitleText',
            'overflow: visible;',
            'translateX(14px)',
        ]:
            self.assertIn(marker, theme_css)

    def test_theme_css_improves_notice_contrast(self) -> None:
        theme_css = (ROOT / "theme.css").read_text()

        for marker in [
            '--cm-notice-bg-default',
            '--cm-notice-text-default',
            '.notice',
            '.notice-message',
        ]:
            self.assertIn(marker, theme_css)

    def test_theme_css_covers_native_surfaces(self) -> None:
        theme_css = (ROOT / "theme.css").read_text()

        for marker in [
            "/* Workspace chrome */",
            "/* Sidebars and tabs */",
            "/* Editor typography */",
            "/* Callouts, quotes, tables, and code */",
        ]:
            self.assertIn(marker, theme_css)

    def test_demo_vault_has_initial_native_showcases(self) -> None:
        for relative_path in [
            "demo-vault/00-Start Here.md",
            "demo-vault/01-Longform Reading.md",
        ]:
            self.assertTrue((ROOT / relative_path).exists(), f"{relative_path} must exist")

    def test_theme_css_covers_target_plugins(self) -> None:
        theme_css = (ROOT / "theme.css").read_text()

        for marker in [
            "/* @settings",
            "/* Dataview */",
            "/* Kanban */",
            "sable-ledger-strong-accents",
        ]:
            self.assertIn(marker, theme_css)

    def test_demo_vault_has_plugin_showcases_and_configs(self) -> None:
        for relative_path in [
            "demo-vault/02-Dataview Showcase.md",
            "demo-vault/03-Kanban Showcase.md",
            "demo-vault/04-Callouts and Tables.md",
            "demo-vault/.obsidian/app.json",
            "demo-vault/.obsidian/appearance.json",
        ]:
            self.assertTrue((ROOT / relative_path).exists(), f"{relative_path} must exist")

    def test_readme_covers_installation_modes_and_plugin_scope(self) -> None:
        readme_path = ROOT / "README.md"
        self.assertTrue(readme_path.exists(), "README.md must exist")

        readme = readme_path.read_text()
        for marker in [
            "Installation",
            "light mode",
            "dark mode",
            "demo vault",
            "Dataview",
            "Kanban",
            "Style Settings",
            "1080px",
            "cleaner neutral palette",
        ]:
            self.assertIn(marker, readme)

    def test_readme_mentions_round3_claude_docs_refinement(self) -> None:
        readme = (ROOT / "README.md").read_text()

        for marker in [
            "code.claude.com",
            "sans-forward typography",
            "lighter chrome",
            "docs-like feel",
        ]:
            self.assertIn(marker, readme)

    def test_manifest_and_versions_stay_in_sync(self) -> None:
        manifest = json.loads((ROOT / "manifest.json").read_text())
        versions = json.loads((ROOT / "versions.json").read_text())

        self.assertEqual(versions[manifest["version"]], manifest["minAppVersion"])


if __name__ == "__main__":
    unittest.main()
