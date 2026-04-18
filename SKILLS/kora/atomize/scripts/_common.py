from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def find_repo_root(start: Path) -> Path:
    current = start.resolve()
    for candidate in [current, *current.parents]:
        if (candidate / "scripts" / "kora").exists() and (candidate / "KNOWLEDGE").exists():
            return candidate
    raise RuntimeError("Could not locate KORA repo root from skill script")


def ensure_repo_pythonpath(repo_root: Path) -> None:
    scripts_dir = repo_root / "scripts"
    if str(scripts_dir) not in sys.path:
        sys.path.insert(0, str(scripts_dir))


def run_kora(repo_root: Path, args: list[str]) -> int:
    command = [sys.executable, str(repo_root / "scripts" / "kora"), *args]
    completed = subprocess.run(command, cwd=str(repo_root))
    return completed.returncode
