#!/usr/bin/env python3
"""Validate the kit, not the adopting project's product code.

From the repository root: python3 -B -I tools/check_kit.py
Requires Python's standard library, sh and standard POSIX utilities. Excludes
.agents/workspace/. Runs static checks first, then bounded local unittest tests.
It neither stages files nor changes hooks, versions, services or project data.
"""
import json
import os
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit

LINK = re.compile(r"\[[^\]]*\]\(([^\s)]+)\)")
KIT_PATH = re.compile(r"`(\.agents/[^`\s]+)`")
SKILL_NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")
FIELD = re.compile(r"([A-Za-z0-9_-]+):(?:[ \t]+(.*))?")
YAML_INDICATOR = re.compile(r"""[,\[\]{}#&*!|>'"%@`]|[-?:](?:[ \t]|$)""")


def frontmatter_value(value):
    """Return a plain or double-quoted one-line value, or None outside that subset."""
    if value.startswith('"'):
        try:  # A JSON string is a YAML double-quoted scalar with the same escapes.
            text = json.loads(value, strict=False)
        except ValueError:
            return None
        return None if "\n" in text or "\r" in text else text
    if YAML_INDICATOR.match(value) or ":" in value or "#" in value:
        return None
    return value


def skill_findings(path, text):
    """Check Agent Skills frontmatter as `key: value` lines, without a YAML parser."""
    lines = text.split("\n")
    if lines[0] != "---":
        return ["first line must be ---"]
    if "---" not in lines[1:]:
        return ["frontmatter has no closing ---"]
    findings, fields = [], {}
    for number, line in enumerate(lines[1:lines.index("---", 1)], 2):
        match = FIELD.fullmatch(line)
        if not match:
            findings.append(f"frontmatter line {number} is not `key: value`")
        elif match[1] in fields:
            findings.append(f"duplicate frontmatter key: {match[1]}")
        else:
            fields[match[1]] = (match[2] or "").strip()
    values = {}
    for key in ("name", "description"):
        if key not in fields:
            findings.append(f"frontmatter has no {key}")
            continue
        values[key] = frontmatter_value(fields[key])
        if values[key] is None:
            findings.append(f"{key} must be one line of plain text, "
                            "double-quoted if it contains : or #")
    name, description = values.get("name"), values.get("description")
    if name is not None:
        if name != path.parent.name:
            findings.append(f"name {name!r} does not match its directory")
        if not SKILL_NAME.fullmatch(name) or len(name) > 64:
            findings.append(f"name {name!r} must be 1-64 lowercase letters or digits "
                            "in hyphen-separated words")
    if description is not None:
        if not description:
            findings.append("description is empty")
        elif len(description) > 200:
            findings.append("description is longer than 200 characters")
        if "<" in description or ">" in description:
            findings.append("description contains < or >")
    return findings


def source_files(root):
    files = [root / "AGENTS.md"]
    for directory, dirs, names in os.walk(root / ".agents"):
        dirs[:] = sorted(d for d in dirs if d != "__pycache__"
                         and not (Path(directory) == root / ".agents" and d == "workspace"))
        files.extend(Path(directory) / name for name in sorted(names))
    return files


def static_findings(root):
    root = root.resolve()
    findings = []
    markdown = {}
    for path in source_files(root):
        if not path.is_file():
            findings.append(f"missing file: {path.relative_to(root)}")
            continue
        label = str(path.relative_to(root))
        if path.suffix == ".md":
            try:
                raw = path.read_bytes()
                text = raw.decode("utf-8")
            except (OSError, UnicodeError) as error:
                findings.append(f"{label}: cannot read Markdown: {error}")
                continue
            markdown[path] = text
            if b"\r\n" in raw:
                findings.append(f"{label}: CRLF line endings")
            targets = []
            for match in LINK.finditer(text):
                target = match[1]
                parsed = urlsplit(target)
                if parsed.scheme or parsed.netloc or not parsed.path:
                    continue
                targets.append((path.parent / unquote(parsed.path), target))
            for match in KIT_PATH.finditer(text):
                target = match[1]
                if any(mark in target for mark in "<>*|") or target.startswith(".agents/workspace/"):
                    continue  # Template or local-only task path, not a shipped file.
                targets.append((root / target, target))
            for target, display in targets:
                if not target.resolve().is_relative_to(root):
                    findings.append(f"{label}: local reference escapes repository: {display}")
                elif not target.exists():
                    findings.append(f"{label}: missing local reference: {display}")
        elif path.suffix == ".sh":
            result = subprocess.run(
                ["sh", "-n", str(path)], capture_output=True, text=True, timeout=10
            )
            if result.returncode:
                findings.append(f"{label}: sh -n failed: {result.stderr.strip()}")
    # Every shipped domain policy needs a concrete loading/reference path.
    for path in sorted(markdown):
        if path.parent == root / ".agents/policies":
            reference = "policies/" + path.name
            if not any(reference in text for other, text in markdown.items() if other != path):
                findings.append(f"{path.relative_to(root)}: no explicit incoming policy reference")
    # Kit skills carry frontmatter; the template keeps its placeholders.
    for path in sorted(markdown):
        if path.name == "SKILL.md" and path.parent.parent == root / ".agents/skills":
            findings.extend(f"{path.relative_to(root)}: {finding}"
                            for finding in skill_findings(path, markdown[path]))
    return findings


def main():
    root = Path(__file__).resolve().parent.parent
    try:
        findings = static_findings(root)
        if findings:
            for finding in findings:
                print(f"FAIL: {finding}", flush=True)
            return 1
        print("PASS: local Markdown references, policy routing, skill frontmatter, "
              "line endings and shell syntax", flush=True)
        runner = (
            "import sys, unittest\n"
            "suite = unittest.defaultTestLoader.discover(sys.argv[1])\n"
            "if suite.countTestCases() == 0: sys.exit('FAIL: no tests discovered')\n"
            "sys.exit(not unittest.TextTestRunner(verbosity=2).run(suite).wasSuccessful())\n"
        )
        result = subprocess.run(
            [sys.executable, "-B", "-I", "-c", runner, str(root / "tests")],
            cwd=root, timeout=90,
        )
        return result.returncode
    except (OSError, subprocess.TimeoutExpired) as error:
        print(f"FAIL: validation environment: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
