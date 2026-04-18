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
    _collect_atomic_bundle_paths,
    parse_atomic_propositions,
    resolve_atomic_role,
)


SUSPICIOUS_TEXT_PATTERNS = [
    re.compile(r"table of contents", re.IGNORECASE),
    re.compile(r"^fig(?:ure)?\.\s*\d", re.IGNORECASE),
    re.compile(r"^figure\s+\d", re.IGNORECASE),
    re.compile(r"©|copyright|isbn|doi", re.IGNORECASE),
]


def _iter_bundle_paths(path: Path) -> list[Path]:
    bundle = _collect_atomic_bundle_paths(path)
    return bundle or [path]


def _extract_source_path(frontmatter: dict, fallback: str | None) -> Path | None:
    if fallback:
        candidate = Path(fallback).expanduser().resolve()
        return candidate if candidate.exists() else None

    atomic = frontmatter.get("extensions", {}).get("kora", {}).get("atomic", {})
    if not isinstance(atomic, dict):
        return None
    raw = atomic.get("source_corpus")
    if not raw:
        return None
    candidate = Path(str(raw)).expanduser().resolve()
    return candidate if candidate.exists() else None


def _source_metrics(path: Path | None) -> tuple[int | None, int | None]:
    if path is None:
        return None, None
    if path.is_file():
        lines = sum(1 for _ in path.open("r", encoding="utf-8"))
        return path.stat().st_size, lines
    if path.is_dir():
        total_chars = 0
        total_lines = 0
        for candidate in sorted(path.rglob("*")):
            if not candidate.is_file() or candidate.suffix.lower() not in {".md", ".txt", ".rst"}:
                continue
            total_chars += candidate.stat().st_size
            total_lines += sum(1 for _ in candidate.open("r", encoding="utf-8"))
        return total_chars or None, total_lines or None
    return None, None


def _resolve_target_path(artifact_path: Path, target: str) -> Path | None:
    target_path = target.split("#", 1)[0]
    if not target_path:
        return None
    candidate = (artifact_path.parent / target_path).resolve()
    return candidate if candidate.exists() else None


def _scan_suspicious_propositions(bundle_paths: list[Path]) -> list[tuple[str, str, str]]:
    findings = []
    for artifact_path in bundle_paths:
        frontmatter, body = load_markdown_parts(artifact_path)
        if resolve_atomic_role(frontmatter) == "index":
            continue
        for proposition in parse_atomic_propositions(body):
            for pattern in SUSPICIOUS_TEXT_PATTERNS:
                if pattern.search(proposition["text"]):
                    findings.append((artifact_path.name, proposition["id"], proposition["text"]))
                    break
    return findings


def _scan_anchor_ranges(bundle_paths: list[Path]) -> list[tuple[str, str, str]]:
    findings = []
    line_cache: dict[Path, int] = {}
    for artifact_path in bundle_paths:
        frontmatter, body = load_markdown_parts(artifact_path)
        if resolve_atomic_role(frontmatter) == "index":
            continue
        for proposition in parse_atomic_propositions(body):
            for source in proposition["sources"]:
                match = re.search(r"#L(\d+)(?:-L(\d+))?$", source["target"])
                if not match:
                    continue
                target_path = _resolve_target_path(artifact_path, source["target"])
                if target_path is None or not target_path.is_file():
                    findings.append((artifact_path.name, proposition["id"], source["target"]))
                    continue
                start = int(match.group(1))
                end = int(match.group(2) or match.group(1))
                source_lines = line_cache.get(target_path)
                if source_lines is None:
                    source_lines = sum(1 for _ in target_path.open("r", encoding="utf-8"))
                    line_cache[target_path] = source_lines
                if start < 1 or end < start or end > source_lines:
                    findings.append((artifact_path.name, proposition["id"], source["target"]))
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run editorial quality checks on an atomic artifact or bundle."
    )
    parser.add_argument("path", help="Path to any atomic file in the bundle")
    parser.add_argument(
        "--source",
        help="Override source corpus path when frontmatter source_corpus is unavailable or wrong",
    )
    args = parser.parse_args()

    input_path = Path(args.path).expanduser().resolve()
    if not input_path.exists():
        print(f"ERROR: file not found: {input_path}")
        return 1

    bundle_paths = _iter_bundle_paths(input_path)
    index_frontmatter, _index_body = load_markdown_parts(bundle_paths[0])
    source_path = _extract_source_path(index_frontmatter, args.source)
    source_chars, source_lines = _source_metrics(source_path)
    proposition_total = 0
    microsegments = []

    for artifact_path in bundle_paths:
        frontmatter, body = load_markdown_parts(artifact_path)
        if resolve_atomic_role(frontmatter) == "index":
            continue
        propositions = parse_atomic_propositions(body)
        proposition_total += len(propositions)
        if len(propositions) < 5:
            microsegments.append((artifact_path.name, len(propositions)))

    suspicious_props = _scan_suspicious_propositions(bundle_paths)
    bad_anchors = _scan_anchor_ranges(bundle_paths)

    print(f"bundle_files: {len(bundle_paths)}")
    print(f"propositions: {proposition_total}")
    if source_path is not None:
        print(f"source: {source_path}")
        print(f"source_chars: {source_chars}")
        print(f"source_lines: {source_lines}")
        chars_per_proposition = source_chars / proposition_total if proposition_total else None
        if chars_per_proposition is not None:
            print(f"chars_per_proposition: {chars_per_proposition:.1f}")
    else:
        chars_per_proposition = None

    status = 0

    if microsegments:
        status = 1
        print("microsegments: WARN")
        for name, count in microsegments[:10]:
            print(f"  - {name}: {count} proposiciones")
    else:
        print("microsegments: OK")

    if chars_per_proposition is not None and (
        chars_per_proposition > 800 or (source_chars and source_chars > 100000 and proposition_total < 500)
    ):
        status = 1
        print("density: WARN")
        print(f"  - densidad semantica sospechosamente baja: {chars_per_proposition:.1f} chars/proposicion")
    else:
        print("density: OK")

    if suspicious_props:
        status = 1
        print("contamination: WARN")
        for artifact_name, proposition_id, text in suspicious_props[:12]:
            print(f"  - {artifact_name} {proposition_id}: {text[:160]}")
    else:
        print("contamination: OK")

    if bad_anchors:
        status = 1
        print("anchors: WARN")
        for artifact_name, proposition_id, target in bad_anchors[:12]:
            print(f"  - {artifact_name} {proposition_id}: {target}")
    else:
        print("anchors: OK")

    return status


if __name__ == "__main__":
    raise SystemExit(main())
