#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

from _common import find_repo_root, run_kora


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run KORA markdown lint over atomic drafts or published artifacts."
    )
    parser.add_argument(
        "paths",
        nargs="*",
        help="Atomic file or directory to validate. Defaults to KNOWLEDGE/_SCRIPTORIUM/REVIEW/kora/atomic/",
    )
    args = parser.parse_args()

    repo_root = find_repo_root(Path(__file__))
    target_paths = args.paths or ["KNOWLEDGE/_SCRIPTORIUM/REVIEW/kora/atomic"]
    return run_kora(repo_root, ["lint-md", *target_paths])


if __name__ == "__main__":
    raise SystemExit(main())
