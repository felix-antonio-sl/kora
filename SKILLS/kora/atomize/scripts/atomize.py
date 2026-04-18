#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

from _common import find_repo_root, run_kora


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Canonical wrapper for the `atomize` producer via `kora atomize`."
    )
    parser.add_argument("input_path", help="Source file or directory to atomize")
    parser.add_argument("--slug", default=None, help="Override artifact slug")
    parser.add_argument("--output", default=None, help="Override output directory")
    args = parser.parse_args()

    repo_root = find_repo_root(Path(__file__))
    cli_args = ["atomize", args.input_path]
    if args.slug:
        cli_args.extend(["--slug", args.slug])
    if args.output:
        cli_args.extend(["--output", args.output])
    return run_kora(repo_root, cli_args)


if __name__ == "__main__":
    raise SystemExit(main())
