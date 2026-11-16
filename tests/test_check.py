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

    def skill(self, directory, *lines, text=None):
        if text is None:
            text = "---\n" + "".join(line + "\n" for line in lines) + "---\n\n# Skill: Example\n"
        path = self.put(f".agents/skills/{directory}/SKILL.md", text)
        try:
            return checker.static_findings(self.root)
        finally:
            path.unlink()

    def test_valid_skill_frontmatter(self):
        self.put(".agents/templates/SKILL.md", "---\nname: <skill-directory-name>\n"
                 "description: <when to use this skill>\n---\n")
        name = "name: example"
        for directory, lines in (
            ("example", (name, "description: Use when testing the checker.")),
            ("example", ('name: "example"', 'description: "Use for x: y, not #1."')),
            ("example", (name, r'description: "Use when printing \"x: y\"."')),
            ("example", (name, r'description: "Use when reading C:\\temp: examples."')),
            ("example", (name, r'description: "Use for caf\u00e9 menus."')),
            ("a" * 64, ("name: " + "a" * 64, "description: " + "x" * 200)),
        ):
            with self.subTest(lines=lines):
                self.assertEqual(self.skill(directory, *lines), [])

    def test_skill_frontmatter_failures(self):
        name, description = "name: example", "description: Use when testing."
        body = "name: example\ndescription: Use.\n---\n"
        for directory, lines, text, expected in (
            ("example", (), "# Skill: Example\n", "first line must be ---"),
            ("example", (), "\n---\n" + body, "first line must be ---"),
            ("example", (), "﻿---\n" + body, "first line must be ---"),
            ("example", (), "---\nname: example\ndescription: Use.\n", "no closing ---"),
            ("example", (description,), None, "has no name"),
            ("example", ("name: other", description), None, "does not match its directory"),
            ("-example", ("name: -example", description), None, "must be 1-64"),
            ("example-", ("name: example-", description), None, "must be 1-64"),
            ("ex--ample", ("name: ex--ample", description), None, "must be 1-64"),
            ("Upper", ("name: Upper", description), None, "must be 1-64"),
            ("a" * 65, ("name: " + "a" * 65, description), None, "must be 1-64"),
            ("example", (name,), None, "has no description"),
            ("example", (name, "description:"), None, "description is empty"),
            ("example", (name, 'description: ""'), None, "description is empty"),
            ("example", (name, "description: " + "x" * 201), None, "longer than 200"),
            ("example", (name, "description: Use <here>."), None, "< or >"),
            ("example", (name, "description: Use when a > b."), None, "< or >"),
            ("example", (name, "description: Use for x: y."), None, "double-quoted"),
            ("example", (name, "description: Use for #1."), None, "double-quoted"),
            ("example", (name, 'description: "Use.'), None, "double-quoted"),
            ("example", (name, r'description: "Use.\"'), None, "double-quoted"),
            ("example", (name, 'description: "Use "x" here."'), None, "double-quoted"),
            ("example", (name, r'description: "Use \x41 here."'), None, "double-quoted"),
            ("example", (name, r'description: "Use\nhere."'), None, "double-quoted"),
            ("example", (name, r'description: "Use <here>."'), None, "< or >"),
            ("example", (name, "description: |", "  Use."), None, "double-quoted"),
            ("example", (name, "description: Use", "  when testing."), None, "`key: value`"),
            ("example", (name, description, description), None, "duplicate frontmatter key"),
        ):
            with self.subTest(directory=directory, lines=lines, text=text):
                findings = self.skill(directory, *lines, text=text)
                self.assertTrue(any(expected in finding for finding in findings), findings)


if __name__ == "__main__":
    unittest.main()
