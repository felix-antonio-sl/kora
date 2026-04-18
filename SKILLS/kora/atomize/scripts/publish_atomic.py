#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path

from _common import find_repo_root, run_kora

REVIEW_TYPE = "atomic_acceptance"


def _bundle_root_name(path: Path) -> str:
    stem = path.stem
    if stem.endswith("-review"):
        stem = stem[:-7]
    if stem.endswith("-index"):
        return stem[:-6]
    return re.sub(r"-\d+$", "", stem)


def _default_review_path(path: Path) -> Path:
    return path.with_name(f"{_bundle_root_name(path)}-review.md")


def _load_markdown_parts(path: Path) -> tuple[dict | None, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return None, text
    head, _sep, rest = text[4:].partition("\n---\n")
    if not _sep:
        return None, text
    import yaml

    return yaml.safe_load(head), rest


def _bundle_latest_mtime(path: Path) -> float:
    root = _bundle_root_name(path)
    latest = path.stat().st_mtime
    for candidate in path.parent.glob(f"{root}*.md"):
        if candidate.name.endswith("-review.md"):
            continue
        latest = max(latest, candidate.stat().st_mtime)
    return latest


def _validate_acceptance_review(target_path: Path, review_path: Path) -> tuple[bool, str]:
    if not review_path.exists():
        return False, f"missing acceptance review: {review_path}"

    frontmatter, _body = _load_markdown_parts(review_path)
    if not isinstance(frontmatter, dict):
        return False, f"cannot parse acceptance review frontmatter: {review_path}"
    if frontmatter.get("review_type") != REVIEW_TYPE:
        return False, f"invalid review_type in {review_path}"
    if frontmatter.get("bundle_root") != _bundle_root_name(target_path):
        return False, f"review bundle_root does not match target bundle: {review_path}"
    if frontmatter.get("decision") != "accept":
        return False, f"review decision is not accept: {review_path}"
    if not frontmatter.get("publish_ready"):
        return False, f"review is not publish_ready: {review_path}"
    if review_path.stat().st_mtime < _bundle_latest_mtime(target_path):
        return False, f"review is stale for current bundle state: {review_path}"
    return True, ""


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

    review_path = Path(args.review).expanduser().resolve() if args.review else _default_review_path(target_path)
    valid_review, message = _validate_acceptance_review(target_path, review_path)
    if not valid_review:
        print(f"ERROR: {message}")
        print(
            "Run review_atomic_acceptance.py with --decision accept after finishing bundle and semantic review."
        )
        return 1

    repo_root = find_repo_root(Path(__file__))
    print(f"ACCEPTANCE REVIEW: {review_path}")
    promote_code = run_kora(repo_root, ["promote", str(target_path)])
    if promote_code != 0:
        return promote_code
    return run_kora(repo_root, ["index"])


if __name__ == "__main__":
    raise SystemExit(main())
