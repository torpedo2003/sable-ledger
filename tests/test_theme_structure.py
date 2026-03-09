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


if __name__ == "__main__":
    unittest.main()
