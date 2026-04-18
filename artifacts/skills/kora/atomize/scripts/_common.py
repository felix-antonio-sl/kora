from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def find_repo_root(start: Path) -> Path:
    current = start.resolve()
    for candidate in [current, *current.parents]:
        # Topologia v5 (reorg 2026-04-18): toolchain/kora + artifacts/knowledge/
        if (candidate / "toolchain" / "kora").exists() and (candidate / "artifacts" / "knowledge").exists():
            return candidate
        # Fallback legacy (pre-reorg v5)
        if (candidate / "scripts" / "kora").exists() and (candidate / "KNOWLEDGE").exists():
            return candidate
    raise RuntimeError("Could not locate KORA repo root from skill script")


def ensure_repo_pythonpath(repo_root: Path) -> None:
    toolchain_dir = repo_root / "toolchain"
    if not toolchain_dir.exists():
        toolchain_dir = repo_root / "scripts"  # fallback legacy
    if str(toolchain_dir) not in sys.path:
        sys.path.insert(0, str(toolchain_dir))


def run_kora(repo_root: Path, args: list[str]) -> int:
    kora_cli = repo_root / "toolchain" / "kora"
    if not kora_cli.exists():
        kora_cli = repo_root / "scripts" / "kora"  # fallback legacy
    command = [sys.executable, str(kora_cli), *args]
    completed = subprocess.run(command, cwd=str(repo_root))
    return completed.returncode
