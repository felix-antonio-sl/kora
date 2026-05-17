#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

from _common import ensure_repo_pythonpath, find_repo_root, run_kora


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Promote an atomic draft only after a fresh accepted review exists, then rebuild the catalog."
    )
    parser.add_argument("path", help="Path to atomic draft or `-index.md` file")
    parser.add_argument(
        "--review",
        help="Optional path to an acceptance review artifact; defaults to atomic-<slug>-review.md next to the bundle",
    )
    args = parser.parse_args()

    target_path = Path(args.path).expanduser().resolve()
    if not target_path.exists():
        print(f"ERROR: file not found: {target_path}")
        return 1

    repo_root = find_repo_root(Path(__file__))
    ensure_repo_pythonpath(repo_root)

    from kora_lib.promote import default_atomic_review_path, validate_atomic_acceptance_review

    review_path = Path(args.review).expanduser().resolve() if args.review else default_atomic_review_path(target_path)
    valid_review, message, _resolved_review_path = validate_atomic_acceptance_review(
        target_path,
        review_path=review_path,
    )
    if not valid_review:
        print(f"ERROR: {message}")
        print(
            "Run review_atomic_acceptance.py with --decision accept after finishing bundle and semantic review."
        )
        return 1

    promote_args = ["promote", str(target_path), "--review", str(review_path)]
    promote_code = run_kora(repo_root, promote_args)
    if promote_code != 0:
        return promote_code
    return run_kora(repo_root, ["index"])


if __name__ == "__main__":
    raise SystemExit(main())
