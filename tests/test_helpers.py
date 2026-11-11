"""Bounded channel-helper regressions; no third-party test dependencies.

Run via python3 -B -I tools/check_kit.py. KIT_HELPERS_DIR selects pre-fix copies
for regression demonstrations only; it does not change the helpers' interface.
"""
import concurrent.futures
import os
from pathlib import Path
import re
import subprocess
import tempfile
import threading
import time
import unittest

ROOT = Path(__file__).resolve().parents[1]
HELPERS = Path(os.environ.get(
    "KIT_HELPERS_DIR", ROOT / ".agents/skills/multi-agent-workflow/scripts"
)).resolve()


class Helpers(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix=".kit-tests-", dir=ROOT)
        self.addCleanup(self.temp.cleanup)
        self.dir = Path(self.temp.name)
        self.channel = self.dir / "channel with spaces.md"
        self.channel.write_text("initial\n", encoding="utf-8")
        self.message = self.dir / "message with spaces.md"
        self.message.write_text("message\n", encoding="utf-8")

    def run_helper(self, name, *args, env=None):
        return subprocess.run(
            ["sh", str(HELPERS / (name + ".sh")), *map(str, args)],
            text=True, capture_output=True, timeout=5, env=env,
        )

    def read(self, seen=0, channel=None):
        result = self.run_helper("read", channel or self.channel, seen)
        self.assertEqual(result.returncode, 0, result.stderr)
        match = re.search(r"^seen=(\d+) sum=(\d+-\d+)\n\Z", result.stdout, re.M)
        self.assertIsNotNone(match, result.stdout)
        return result.stdout[:match.start()], int(match[1]), match[2]

    def shim(self, name, body):
        bindir = self.dir / "bin"
        bindir.mkdir(exist_ok=True)
        script = bindir / name
        script.write_text("#!/bin/sh\n" + body + "\n", encoding="utf-8")
        script.chmod(0o700)
        return dict(os.environ, PATH=str(bindir) + os.pathsep + os.environ["PATH"])

    def test_documented_loop(self):
        body, seen, checksum = self.read(-60)
        self.assertEqual(body, "initial\n")
        result = self.run_helper("append", self.channel, self.message)
        self.assertEqual(result.returncode, 0, result.stderr)
        # Carry the old sum across the append: the change must not be missed.
        self.assertEqual(self.run_helper("wait", self.channel, checksum, 0).returncode, 0)
        body, seen, checksum = self.read(seen)
        self.assertEqual(body, "message\n\n")
        timeout = self.run_helper("wait", self.channel, checksum, 0)
        self.assertEqual(timeout.returncode, 1, timeout.stderr)
        self.assertEqual(self.read(seen)[0], "")
        # The ordinary cksum form is supported too.
        self.assertEqual(self.run_helper(
            "wait", self.channel, checksum.replace("-", " "), 0
        ).returncode, 1)

    def test_newline_repair_and_new_channel(self):
        self.channel.write_text("initial", encoding="utf-8")
        self.message.write_text("message", encoding="utf-8")
        result = self.run_helper("append", self.channel, self.message)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.channel.read_text(), "initial\nmessage\n\n")
        self.channel.unlink()  # Only this test's disposable file.
        result = self.run_helper("append", self.channel, self.message)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.channel.read_text(), "message\n\n")

    def test_invalid_cursors(self):
        for cursor in ("", "08", "-08", "--1", "1-2", "x", "2147483648", "9" * 60):
            with self.subTest(cursor=cursor):
                result = self.run_helper("read", self.channel, cursor)
                self.assertEqual(result.returncode, 64, result.stderr)
                self.assertNotIn("seen=", result.stdout)

    def test_valid_cursor_bounds(self):
        for cursor, expected in ((0, "initial\n"), (2147483647, "initial\n"),
                                 (-2147483647, "initial\n"), ("-0", "")):
            with self.subTest(cursor=cursor):
                self.assertEqual(self.read(cursor)[0], expected)

    def test_read_failures_never_advance_cursor(self):
        for command in ("sed", "wc", "cksum"):
            with self.subTest(command=command):
                env = self.shim(command, "echo 'injected read failure' >&2; exit 23")
                result = self.run_helper("read", self.channel, 0, env=env)
                self.assertEqual(result.returncode, 2, result.stderr)
                self.assertNotIn("seen=", result.stdout)
                (self.dir / "bin" / command).unlink()

    def test_read_complete_lines_and_rotation(self):
        self.channel.write_text("one\ntwo\npartial", encoding="utf-8")
        body, seen, _ = self.read(-1)
        self.assertEqual(body, "two\n")
        self.assertEqual(seen, 2)
        with self.channel.open("a", encoding="utf-8") as stream:
            stream.write(" completed\n")
        self.assertEqual(self.read(seen)[0], "partial completed\n")
        self.channel.write_text("replacement\n", encoding="utf-8")
        self.assertEqual(self.read(20)[0], "replacement\n")
        # On an announced rotation, reset even if the new file is longer.
        rotated = self.dir / "next channel.md"
        rotated.write_text("a\nb\nc\nd\n", encoding="utf-8")
        self.assertEqual(self.read(0, rotated)[0], rotated.read_text())

    def test_missing_files_and_wait_usage(self):
        missing = self.dir / "absent"
        self.assertEqual(self.run_helper("read", missing).returncode, 2)
        self.assertEqual(self.run_helper("wait", missing, "1-1", 0).returncode, 2)
        for checksum in ("", "1", "a-b", "-1", "1-", "1-2-3"):
            with self.subTest(checksum=checksum):
                self.assertEqual(self.run_helper(
                    "wait", self.channel, checksum, 0
                ).returncode, 64)
        for seconds in ("-1", "01", "10000", "x"):
            with self.subTest(seconds=seconds):
                self.assertEqual(self.run_helper(
                    "wait", self.channel, "1-1", seconds
                ).returncode, 64)

    def test_append_rejects_self_aliases(self):
        symlink = self.dir / "message symlink"
        symlink.symlink_to(self.channel)
        for message in (self.channel, str(self.dir) + "/./" + self.channel.name, symlink):
            with self.subTest(message=message):
                before = self.channel.read_bytes()
                result = self.run_helper("append", self.channel, message)
                self.assertEqual(result.returncode, 64, result.stderr)
                self.assertEqual(self.channel.read_bytes(), before)
        directory_alias = self.dir / "directory alias"
        directory_alias.symlink_to(self.dir, target_is_directory=True)
        result = self.run_helper("append", self.channel, directory_alias / self.channel.name)
        self.assertEqual(result.returncode, 64, result.stderr)
        result = self.run_helper("append", directory_alias / self.channel.name, self.message)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.channel.read_text(), "initial\nmessage\n\n")
        hardlink = self.dir / "message hardlink"
        os.link(self.channel, hardlink)
        before = self.channel.read_bytes()
        result = self.run_helper("append", self.channel, hardlink)
        self.assertEqual(result.returncode, 64, result.stderr)
        self.assertEqual(self.channel.read_bytes(), before)

    def test_append_rejects_channel_aliases(self):
        for kind in ("symlink", "hardlink"):
            with self.subTest(kind=kind):
                alias = self.dir / kind
                if kind == "symlink":
                    alias.symlink_to(self.channel)
                else:
                    os.link(self.channel, alias)
                before = self.channel.read_bytes()
                result = self.run_helper("append", alias, self.message)
                self.assertEqual(result.returncode, 64, result.stderr)
                self.assertEqual(self.channel.read_bytes(), before)
                alias.unlink()

    def test_bad_message_and_stale_lock(self):
        self.assertEqual(self.run_helper("append", self.channel, self.dir).returncode, 64)
        lock = Path(str(self.channel) + ".lock")
        env = self.shim("sleep", "exit 0")  # Exercise retries without a 29-second delay.
        for kind in ("directory", "file"):
            with self.subTest(kind=kind):
                if kind == "directory":
                    lock.mkdir()
                else:
                    lock.write_text("stale fixture\n", encoding="utf-8")
                result = self.run_helper("append", self.channel, self.message, env=env)
                self.assertEqual(result.returncode, 1, result.stderr)
                self.assertTrue(lock.exists())  # Never remove another writer's lock.
                self.assertEqual(self.channel.read_text(), "initial\n")
                if kind == "directory":
                    lock.rmdir()
                else:
                    lock.unlink()

    def test_concurrent_appenders_and_readers(self):
        self.channel.write_text("", encoding="utf-8")
        done = threading.Event()
        expected = {
            f"writer-{writer}-{number}:" + "x" * 8192 + "\n\n"
            for writer in range(4) for number in range(8)
        }

        def writer(index):
            message = self.dir / f"writer-{index}.md"
            for number in range(8):
                message.write_text(f"writer-{index}-{number}:" + "x" * 8192,
                                   encoding="utf-8")
                result = self.run_helper("append", self.channel, message)
                self.assertEqual(result.returncode, 0, result.stderr)

        def reader():
            chunks, seen = [], 0
            deadline = time.monotonic() + 25
            while time.monotonic() < deadline:
                body, seen, _ = self.read(seen)
                chunks.append(body)
                if done.is_set():
                    body, _, _ = self.read(seen)
                    chunks.append(body)
                    return "".join(chunks)
            self.fail("reader deadline exceeded")

        with concurrent.futures.ThreadPoolExecutor(max_workers=6) as pool:
            readers = [pool.submit(reader) for _ in range(2)]
            writers = [pool.submit(writer, index) for index in range(4)]
            try:
                for future in writers:
                    future.result(timeout=25)
            finally:
                done.set()
            observed = [future.result(timeout=10) for future in readers]
        content = self.channel.read_text()
        self.assertEqual(set(part + "\n\n" for part in content.split("\n\n")[:-1]), expected)
        self.assertEqual(content.count("writer-"), len(expected))
        self.assertTrue(content.endswith("\n\n"))
        for readback in observed:
            self.assertEqual(readback, content)
        self.assertFalse(Path(str(self.channel) + ".lock").exists())


if __name__ == "__main__":
    unittest.main()
