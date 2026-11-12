"""Exercise the kit checker on tiny disposable repositories, never product copies."""
import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("kit_check", ROOT / "tools/check_kit.py")
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class KitCheck(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix=".kit-check-tests-", dir=ROOT)
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / ".agents").mkdir()
        (self.root / "AGENTS.md").write_text("# Fixture\n", encoding="utf-8")

    def put(self, name, text):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
        return path

    def test_valid_links_and_placeholders(self):
        self.put(".agents/guide.md", "# Guide\n")
        self.put("AGENTS.md", "[Guide](.agents/guide.md#section)\n"
                 "[Web](https://example.invalid/never-fetched)\n"
                 "[Mail](mailto:example@example.invalid)\n[Here](#section)\n"
                 "`.agents/roles/<role>.md` `.agents/skills/*/SKILL.md`\n"
                 "`.agents/workspace/<task>/TASK.md`\n")
        self.assertEqual(checker.static_findings(self.root), [])

    def test_missing_markdown_and_inline_paths(self):
        self.put("AGENTS.md", "[Missing](missing.md)\n`.agents/missing.md`\n")
        findings = checker.static_findings(self.root)
        self.assertTrue(any("missing.md" in finding for finding in findings), findings)
        self.assertTrue(any(".agents/missing.md" in finding for finding in findings), findings)

    def test_policy_requires_incoming_reference(self):
        self.put(".agents/policies/example.md", "# Example\n")
        findings = checker.static_findings(self.root)
        self.assertTrue(any("no explicit incoming" in finding for finding in findings), findings)
        self.put("AGENTS.md", "Load [example](.agents/policies/example.md).\n")
        self.assertEqual(checker.static_findings(self.root), [])

    def test_workspace_is_not_inspected(self):
        self.put(".agents/workspace/private.md", "[Deliberately invalid](missing.md)\n")
        self.assertEqual(checker.static_findings(self.root), [])

    def test_shell_syntax_failure(self):
        self.put(".agents/bad.sh", "#!/bin/sh\nif then\n")
        findings = checker.static_findings(self.root)
        self.assertTrue(any("sh -n failed" in finding for finding in findings), findings)

    def test_crlf_and_invalid_utf8(self):
        (self.root / "AGENTS.md").write_bytes(b"# Fixture\r\n")
        findings = checker.static_findings(self.root)
        self.assertTrue(any("CRLF" in finding for finding in findings), findings)
        (self.root / "AGENTS.md").write_bytes(b"\xff")
        findings = checker.static_findings(self.root)
        self.assertTrue(any("cannot read Markdown" in finding for finding in findings), findings)

    def test_reference_cannot_escape_repository(self):
        self.put("AGENTS.md", "[Outside](../never-read.md)\n")
        findings = checker.static_findings(self.root)
        self.assertTrue(any("escapes repository" in finding for finding in findings), findings)


if __name__ == "__main__":
    unittest.main()
