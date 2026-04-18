#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path

from _common import ensure_repo_pythonpath, find_repo_root

REPO_ROOT = find_repo_root(Path(__file__))
ensure_repo_pythonpath(REPO_ROOT)

from kora_lib.artifacts import load_markdown_parts
from kora_lib.validation import (
    lint_kora_markdown_parts,
    parse_atomic_propositions,
    parse_atomic_source_index,
    resolve_atomic_role,
    resolve_document_family,
)


def collect_bundle_paths(path: Path) -> list[Path]:
    stem = path.stem
    if stem.endswith("-index"):
        root = stem[:-6]
    else:
        root = re.sub(r"-\d+$", "", stem)

    candidates = []
    index_path = path.parent / f"{root}-index{path.suffix}"
    if index_path.exists():
        candidates.append(index_path)
    segment_pattern = re.compile(rf"^{re.escape(root)}-(\d+){re.escape(path.suffix)}$")
    segment_matches = []
    for candidate in path.parent.glob(f"{root}-*{path.suffix}"):
        match = segment_pattern.match(candidate.name)
        if match:
            segment_matches.append((int(match.group(1)), candidate))
    candidates.extend(
        candidate for _, candidate in sorted(segment_matches, key=lambda item: item[0])
    )
    if not candidates and path.exists():
        candidates.append(path)
    return candidates


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Inspect an atomic artifact or segmented bundle and report integrity."
    )
    parser.add_argument("path", help="Path to any atomic artifact in the bundle")
    args = parser.parse_args()

    input_path = Path(args.path).expanduser().resolve()
    if not input_path.exists():
        print(f"ERROR: file not found: {input_path}")
        return 1

    bundle_paths = collect_bundle_paths(input_path)
    if not bundle_paths:
        print(f"ERROR: no bundle files found near: {input_path}")
        return 1

    all_ids = []
    failed = False
    for artifact_path in bundle_paths:
        frontmatter, body = load_markdown_parts(artifact_path)
        family = resolve_document_family(frontmatter)
        role = resolve_atomic_role(frontmatter)
        propositions = parse_atomic_propositions(body)
        source_index = parse_atomic_source_index(body)
        lint_failures = lint_kora_markdown_parts(frontmatter, body, path=artifact_path)

        print(f"{artifact_path.name}")
        print(f"  family: {family}")
        print(f"  role: {role}")
        print(f"  propositions: {len(propositions)}")
        print(f"  indexed_sources: {len(source_index)}")

        all_ids.extend(item["id"] for item in propositions)
        if lint_failures:
            failed = True
            print("  lint: FAIL")
            for failure in lint_failures[:8]:
                print(f"    - {failure}")
        else:
            print("  lint: OK")

    duplicate_ids = len(all_ids) != len(set(all_ids))
    if duplicate_ids:
        failed = True
        print("bundle_ids: FAIL")
        print("  - duplicated Pxxx IDs across bundle")
    else:
        print("bundle_ids: OK")

    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
