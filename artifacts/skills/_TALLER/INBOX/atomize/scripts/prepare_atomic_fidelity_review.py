#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

from _common import ensure_repo_pythonpath, find_repo_root

REPO_ROOT = find_repo_root(Path(__file__))
ensure_repo_pythonpath(REPO_ROOT)

from kora_lib.artifacts import load_markdown_parts
from kora_lib.validation import _collect_atomic_bundle_paths, parse_atomic_propositions, resolve_atomic_role


NEGATION_PATTERN = re.compile(r"\b(?:no|not|never|without|sin|except|excepto|salvo|unless|only|solo|unicamente)\b", re.IGNORECASE)
NUMERIC_PATTERN = re.compile(r"\b\d+(?:[.,]\d+)?\b")
DATEISH_PATTERN = re.compile(r"\b(?:\d{4}|\d{1,2}\s+(?:days?|dias|días|weeks?|semanas|months?|meses|years?|anos|años))\b", re.IGNORECASE)


@dataclass
class PropositionRecord:
    artifact_name: str
    proposition_id: str
    prop_type: str
    text: str
    sources: list[dict]
    risk_flags: list[str]
    score: int
    selection_reason: str = ""


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


def _resolve_target_path(bundle_dir: Path, target: str, fallback_source: Path | None) -> Path | None:
    target_path = target.split("#", 1)[0]
    if target_path:
        candidate = (bundle_dir / target_path).resolve()
        if candidate.exists():
            return candidate
        if fallback_source is not None and fallback_source.is_dir():
            fallback_candidate = (fallback_source / target_path).resolve()
            if fallback_candidate.exists():
                return fallback_candidate
    if fallback_source is not None and fallback_source.is_file():
        return fallback_source
    return None


def _risk_flags(prop_type: str, text: str, source_count: int) -> tuple[list[str], int]:
    flags: list[str] = []
    score = 0

    if prop_type in {"constraint", "obligation", "exclusion", "permission", "deadline", "tension", "definition"}:
        flags.append(prop_type)
        score += 3
    if NEGATION_PATTERN.search(text):
        flags.append("negation_or_exception")
        score += 2
    if NUMERIC_PATTERN.search(text):
        flags.append("numeric")
        score += 2
    if DATEISH_PATTERN.search(text):
        flags.append("date_or_duration")
        score += 2
    if source_count > 1:
        flags.append("multi_source")
        score += 1
    if len(text) > 220:
        flags.append("long_statement")
        score += 1
    return flags, score


def _collect_records(bundle_paths: list[Path]) -> list[PropositionRecord]:
    records: list[PropositionRecord] = []
    for artifact_path in bundle_paths:
        frontmatter, body = load_markdown_parts(artifact_path)
        if resolve_atomic_role(frontmatter) == "index":
            continue
        for proposition in parse_atomic_propositions(body):
            flags, score = _risk_flags(proposition["type"], proposition["text"], len(proposition["sources"]))
            records.append(
                PropositionRecord(
                    artifact_name=artifact_path.name,
                    proposition_id=proposition["id"],
                    prop_type=proposition["type"],
                    text=proposition["text"],
                    sources=proposition["sources"],
                    risk_flags=flags,
                    score=score,
                    selection_reason="",
                )
            )
    return records


def _bundle_stats(records: list[PropositionRecord]) -> dict:
    type_counts = Counter(record.prop_type for record in records)
    return {
        "record_count": len(records),
        "tension_count": type_counts.get("tension", 0),
        "multi_source_count": sum(1 for record in records if len(record.sources) > 1),
        "negation_or_exception_count": sum(1 for record in records if "negation_or_exception" in record.risk_flags),
        "high_risk_count": sum(1 for record in records if record.score >= 4),
        "type_counts": dict(sorted(type_counts.items())),
    }


def _excerpt_for_target(
    line_cache: dict[Path, list[str]],
    bundle_dir: Path,
    target: str,
    fallback_source: Path | None,
) -> str:
    match = re.search(r"#L(\d+)(?:-L(\d+))?$", target)
    if not match:
        return ""
    source_path = _resolve_target_path(bundle_dir, target, fallback_source)
    if source_path is None or not source_path.is_file():
        return ""
    lines = line_cache.get(source_path)
    if lines is None:
        lines = source_path.read_text(encoding="utf-8").splitlines()
        line_cache[source_path] = lines
    start = int(match.group(1))
    end = int(match.group(2) or match.group(1))
    start_index = max(1, start) - 1
    end_index = min(len(lines), end)
    if start_index >= len(lines) or start_index >= end_index:
        return ""
    return "\n".join(lines[start_index:end_index]).strip()


def _sample_records(records: list[PropositionRecord], sample_size: int) -> list[PropositionRecord]:
    if len(records) <= sample_size:
        for record in records:
            record.selection_reason = "full_bundle"
        return records

    chosen: list[PropositionRecord] = []
    seen = set()

    def add_records(candidates: list[PropositionRecord], reason: str) -> None:
        for record in candidates:
            if len(chosen) >= sample_size:
                return
            if record.proposition_id in seen:
                continue
            record.selection_reason = reason
            chosen.append(record)
            seen.add(record.proposition_id)

    tensions = sorted(
        [record for record in records if record.prop_type == "tension"],
        key=lambda item: item.proposition_id,
    )
    add_records(tensions, "tension")

    negation_or_exception = sorted(
        [record for record in records if "negation_or_exception" in record.risk_flags and record.prop_type != "tension"],
        key=lambda item: (-item.score, item.proposition_id),
    )
    add_records(negation_or_exception, "negation_or_exception")

    multi_source = sorted(
        [record for record in records if len(record.sources) > 1 and record.prop_type != "tension"],
        key=lambda item: (-item.score, item.proposition_id),
    )
    add_records(multi_source, "multi_source")

    positions = [0, len(records) // 4, len(records) // 2, (3 * len(records)) // 4, len(records) - 1]
    positional_records = [records[index] for index in positions]
    add_records(positional_records, "positional")

    by_risk = sorted(records, key=lambda item: (-item.score, item.proposition_id))
    add_records(by_risk, "risk_score")

    return chosen[:sample_size]


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Prepare a semantic fidelity review packet for an atomic bundle."
    )
    parser.add_argument("path", help="Path to any atomic file in the bundle")
    parser.add_argument(
        "--source",
        help="Override source corpus path when frontmatter source_corpus is unavailable or wrong",
    )
    parser.add_argument(
        "--sample-size",
        type=int,
        default=10,
        help="Number of propositions to sample for fidelity review",
    )
    args = parser.parse_args()

    input_path = Path(args.path).expanduser().resolve()
    if not input_path.exists():
        print(f"ERROR: file not found: {input_path}")
        return 1

    bundle_paths = _iter_bundle_paths(input_path)
    first_frontmatter, _body = load_markdown_parts(bundle_paths[0])
    source_path = _extract_source_path(first_frontmatter, args.source)
    records = _collect_records(bundle_paths)
    stats = _bundle_stats(records)
    sample = _sample_records(records, max(1, args.sample_size))
    line_cache: dict[Path, list[str]] = {}
    bundle_dir = bundle_paths[0].parent

    print("packet_type: semantic_fidelity_review")
    print(f"bundle_files: {len(bundle_paths)}")
    print(f"record_count: {stats['record_count']}")
    print(f"tension_count: {stats['tension_count']}")
    print(f"multi_source_count: {stats['multi_source_count']}")
    print(f"negation_or_exception_count: {stats['negation_or_exception_count']}")
    print(f"high_risk_count: {stats['high_risk_count']}")
    print(f"sample_size: {len(sample)}")
    print(f"sample_contains_tension: {'yes' if any(record.prop_type == 'tension' for record in sample) else 'no'}")
    type_counts_str = ", ".join(f"{key}={value}" for key, value in stats["type_counts"].items()) or "none"
    print(f"type_counts: {type_counts_str}")
    if source_path is not None:
        print(f"source: {source_path}")

    print("note: este script no juzga la fidelidad semantica por si solo; prepara evidencia para revision del agente o humana.")

    for index, record in enumerate(sample, start=1):
        print("")
        print(f"[{index:02d}] {record.artifact_name} {record.proposition_id} `{record.prop_type}`")
        if record.risk_flags:
            print(f"risk_flags: {', '.join(record.risk_flags)}")
        else:
            print("risk_flags: none")
        print(f"selection_reason: {record.selection_reason or 'unspecified'}")
        print(f"proposition: {record.text}")
        for source_index, source in enumerate(record.sources[:2], start=1):
            print(f"source_{source_index}: {source['target']}")
            excerpt = _excerpt_for_target(line_cache, bundle_dir, source["target"], source_path)
            if excerpt:
                print("excerpt:")
                print(excerpt)
            else:
                print("excerpt: <unavailable>")
        print("review:")
        print("- ¿La proposicion esta totalmente soportada por el excerpt?")
        print("- ¿Perdio negaciones, cuantificadores, excepciones o condiciones?")
        print("- ¿Fusiona mas de un hecho distinguible?")
        print("- ¿Introduce interpretacion no sustentada por la fuente?")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
