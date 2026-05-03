"""Tests for KORA host-role identity and local git hook enforcement."""

import io
import os
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from common import ROOT
from kora_lib.host import (
    can_push_master,
    install_git_hooks,
    pre_push_master_guard,
    read_host_role,
)


class HostRoleIdentityTests(unittest.TestCase):
    def test_absent_marker_defaults_to_secondary(self):
        with tempfile.TemporaryDirectory() as tmp:
            marker = Path(tmp) / "host.yml"

            role = read_host_role(marker_path=marker)

        self.assertEqual(role.role, "secondary")
        self.assertEqual(role.source, "default")
        self.assertTrue(role.consistent)
        self.assertFalse(can_push_master(role))

    def test_primary_marker_with_matching_identity_can_push_master(self):
        with tempfile.TemporaryDirectory() as tmp, patch(
            "kora_lib.host._read_hostname", return_value="primary-box"
        ), patch("kora_lib.host._read_machine_id", return_value="machine-1"):
            marker = Path(tmp) / "host.yml"
            marker.write_text(
                "role: primary\nhostname: primary-box\nmachine_id: machine-1\n",
                encoding="utf-8",
            )

            role = read_host_role(marker_path=marker)

        self.assertEqual(role.role, "primary")
        self.assertTrue(role.consistent)
        self.assertTrue(can_push_master(role))

    def test_primary_marker_with_copied_identity_cannot_push_master(self):
        with tempfile.TemporaryDirectory() as tmp, patch(
            "kora_lib.host._read_hostname", return_value="secondary-box"
        ), patch("kora_lib.host._read_machine_id", return_value="machine-2"):
            marker = Path(tmp) / "host.yml"
            marker.write_text(
                "role: primary\nhostname: primary-box\nmachine_id: machine-1\n",
                encoding="utf-8",
            )

            role = read_host_role(marker_path=marker)

        self.assertEqual(role.role, "primary")
        self.assertFalse(role.consistent)
        self.assertFalse(can_push_master(role))

    def test_pre_push_guard_blocks_secondary(self):
        with tempfile.TemporaryDirectory() as tmp:
            stream = io.StringIO()
            code = pre_push_master_guard(stream=stream, marker_path=Path(tmp) / "missing.yml")

        self.assertEqual(code, 1)
        self.assertIn("bloqueado", stream.getvalue())
        self.assertIn("role=secondary", stream.getvalue())

    def test_install_git_hooks_sets_relative_hooks_path(self):
        with tempfile.TemporaryDirectory() as tmp:
            repo_root = Path(tmp)
            hooks_dir = repo_root / "toolchain" / "git-hooks"
            hooks_dir.mkdir(parents=True)
            (hooks_dir / "pre-push").write_text("#!/usr/bin/env sh\n", encoding="utf-8")
            calls = []

            def runner(args, cwd, check):
                calls.append((args, cwd, check))
                return subprocess.CompletedProcess(args, 0)

            installed = install_git_hooks(repo_root=repo_root, hooks_dir=hooks_dir, runner=runner)

        self.assertEqual(installed, hooks_dir)
        self.assertEqual(calls, [(["git", "config", "core.hooksPath", "toolchain/git-hooks"], str(repo_root), True)])


class PrePushHookTests(unittest.TestCase):
    def _run_hook(self, stdin: str):
        with tempfile.TemporaryDirectory() as home:
            env = {**os.environ, "HOME": home}
            return subprocess.run(
                [str(ROOT / "toolchain" / "git-hooks" / "pre-push")],
                cwd=str(ROOT),
                input=stdin,
                text=True,
                capture_output=True,
                env=env,
                check=False,
            )

    def test_hook_allows_feature_branch_from_secondary(self):
        result = self._run_hook(
            "refs/heads/feature/x 111111 refs/heads/feature/x 000000\n"
        )

        self.assertEqual(result.returncode, 0, result.stderr)

    def test_hook_blocks_master_from_secondary(self):
        result = self._run_hook("refs/heads/master 111111 refs/heads/master 000000\n")

        self.assertEqual(result.returncode, 1)
        self.assertIn("push directo a origin/master", result.stderr)


if __name__ == "__main__":
    unittest.main()
