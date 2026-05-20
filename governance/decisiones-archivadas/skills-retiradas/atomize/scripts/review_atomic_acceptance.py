#!/usr/bin/env python3
from __future__ import annotations

import argparse
import subprocess
import sys
import textwrap
from datetime import datetime, timezone
from pathlib import Path
import re

from _common import ensure_repo_pythonpath, find_repo_root
from prepare_atomic_fidelity_review import _bundle_stats, _collect_records, _iter_bundle_paths

REPO_ROOT = find_repo_root(Path(__file__))
ensure_repo_pythonpath(REPO_ROOT)

from kora_lib.artifacts import dump_yaml_frontmatter_and_body, load_markdown_parts


def _bundle_root_name(path: Path) -> str:
    stem = path.stem
    if stem.endswith("-review"):
        stem = stem[:-7]
    if stem.endswith("-index"):
        return stem[:-6]
    # Atomic bundle segments are emitted as short numeric suffixes
    # (`-01`, `-100`). Long numeric slug tails must remain part of identity.
    return re.sub(r"-\d{2,3}$", "", stem)


def _default_review_path(path: Path) -> Path:
    return path.with_name(f"{_bundle_root_name(path)}-review.md")


def _extract_source_path(path: Path) -> str | None:
    frontmatter, _body = load_markdown_parts(path)
    if not isinstance(frontmatter, dict):
        return None
    atomic = frontmatter.get("extensions", {}).get("kora", {}).get("atomic", {})
    if not isinstance(atomic, dict):
        return None
    raw = atomic.get("source_corpus")
    return str(raw) if raw else None


def _run_script(script_name: str, args: list[str]) -> subprocess.CompletedProcess[str]:
    script_path = Path(__file__).with_name(script_name)
    return subprocess.run(
        [sys.executable, str(script_path), *args],
        cwd=str(REPO_ROOT),
        capture_output=True,
        text=True,
    )


def _format_output_block(title: str, completed: subprocess.CompletedProcess[str]) -> str:
    command = " ".join(completed.args)
    output = completed.stdout.rstrip()
    if completed.stderr.strip():
        output = f"{output}\n\n[stderr]\n{completed.stderr.rstrip()}".strip()
    if not output:
        output = "<no output>"
    return textwrap.dedent(
        f"""\
        ## {title}

        - Exit code: `{completed.returncode}`
        - Command: `{command}`

        ```text
        {output}
        ```
        """
    ).strip()


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Write a persistent acceptance review for an atomic bundle."
    )
    parser.add_argument("path", help="Path to any atomic draft or bundle file")
    parser.add_argument(
        "--decision",
        choices=("accept", "reject"),
        required=True,
        help="Semantic/editorial decision for the current bundle state",
    )
    parser.add_argument(
        "--summary",
        required=True,
        help="Short justification for the review decision",
    )
    parser.add_argument(
        "--reviewer",
        default="agent",
        help="Reviewer name recorded in the acceptance review",
    )
    parser.add_argument(
        "--source",
        help="Override source corpus path when frontmatter source_corpus is unavailable or wrong",
    )
    parser.add_argument(
        "--sample-size",
        type=int,
        default=8,
        help="Number of propositions to sample in the fidelity packet",
    )
    parser.add_argument(
        "--notes-file",
        help="Optional markdown file with additional review notes",
    )
    parser.add_argument(
        "--output",
        help="Optional output path for the acceptance review artifact",
    )
    args = parser.parse_args()

    input_path = Path(args.path).expanduser().resolve()
    if not input_path.exists():
        print(f"ERROR: file not found: {input_path}")
        return 1

    review_path = Path(args.output).expanduser().resolve() if args.output else _default_review_path(input_path)
    bundle_root = _bundle_root_name(input_path)
    source_override = args.source or _extract_source_path(input_path)
    bundle_paths = _iter_bundle_paths(input_path)
    records = _collect_records(bundle_paths)
    stats = _bundle_stats(records)
    effective_sample_size = max(1, args.sample_size)
    if stats["tension_count"] > 0:
        effective_sample_size = max(effective_sample_size, min(12, stats["tension_count"] + 2))
    notes = ""
    if args.notes_file:
        notes = Path(args.notes_file).expanduser().read_text(encoding="utf-8").strip()

    bundle_args = [str(input_path)]
    quality_args = [str(input_path)]
    fidelity_args = [str(input_path), "--sample-size", str(effective_sample_size)]
    if source_override:
        quality_args.extend(["--source", source_override])
        fidelity_args.extend(["--source", source_override])

    bundle_result = _run_script("check_atomic_bundle.py", bundle_args)
    quality_result = _run_script("review_atomic_quality.py", quality_args)
    fidelity_result = _run_script("prepare_atomic_fidelity_review.py", fidelity_args)

    checks = {
        "bundle_integrity": "pass" if bundle_result.returncode == 0 else "fail",
        "editorial_quality": "pass" if quality_result.returncode == 0 else "fail",
        "fidelity_packet": "pass" if fidelity_result.returncode == 0 else "fail",
    }

    blockers: list[str] = []
    if checks["bundle_integrity"] != "pass":
        blockers.append("bundle_integrity")
    if checks["editorial_quality"] != "pass":
        blockers.append("editorial_quality")
    if checks["fidelity_packet"] != "pass":
        blockers.append("fidelity_packet")
    if args.decision != "accept":
        blockers.append("decision_reject")

    publish_ready = not blockers
    generated_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()

    frontmatter = {
        "review_type": "atomic_acceptance",
        "decision": args.decision,
        "publish_ready": publish_ready,
        "reviewer": args.reviewer,
        "generated_at": generated_at,
        "review_target": str(input_path),
        "bundle_root": bundle_root,
        "review_artifact": str(review_path),
        "requested_sample_size": max(1, args.sample_size),
        "sample_size": effective_sample_size,
        "source_corpus": source_override,
        "bundle_stats": stats,
        "checks": checks,
        "blockers": blockers,
    }

    body_parts = [
        "# Atomic Acceptance Review",
        "",
        "## Target",
        "",
        f"- Bundle root: `{bundle_root}`",
        f"- Target path: `{input_path}`",
        f"- Review artifact: `{review_path}`",
        f"- Reviewer: `{args.reviewer}`",
        f"- Decision: `{args.decision}`",
        f"- Publish ready: `{'yes' if publish_ready else 'no'}`",
        f"- Requested sample size: `{max(1, args.sample_size)}`",
        f"- Effective sample size: `{effective_sample_size}`",
        "",
        "## Summary",
        "",
        args.summary.strip(),
        "",
        "## Bundle Risk Summary",
        "",
        f"- `record_count`: `{stats['record_count']}`",
        f"- `tension_count`: `{stats['tension_count']}`",
        f"- `multi_source_count`: `{stats['multi_source_count']}`",
        f"- `negation_or_exception_count`: `{stats['negation_or_exception_count']}`",
        f"- `high_risk_count`: `{stats['high_risk_count']}`",
        f"- `type_counts`: `{', '.join(f'{key}={value}' for key, value in stats['type_counts'].items()) or 'none'}`",
        "",
        "## Gate Results",
        "",
        f"- `bundle_integrity`: `{checks['bundle_integrity']}`",
        f"- `editorial_quality`: `{checks['editorial_quality']}`",
        f"- `fidelity_packet`: `{checks['fidelity_packet']}`",
    ]

    if blockers:
        body_parts.extend(
            [
                "",
                "## Blockers",
                "",
                *[f"- `{item}`" for item in blockers],
            ]
        )

    if notes:
        body_parts.extend(["", "## Notes", "", notes])

    body_parts.extend(
        [
            "",
            _format_output_block("Bundle Integrity", bundle_result),
            "",
            _format_output_block("Editorial Quality", quality_result),
            "",
            _format_output_block("Semantic Fidelity Packet", fidelity_result),
            "",
        ]
    )

    review_path.parent.mkdir(parents=True, exist_ok=True)
    dump_yaml_frontmatter_and_body(review_path, frontmatter, "\n".join(body_parts), lint_guard=False)

    print(f"REVIEW WRITTEN: {review_path}")
    print(f"decision: {args.decision}")
    print(f"publish_ready: {'yes' if publish_ready else 'no'}")
    if blockers:
        print("blockers:")
        for item in blockers:
            print(f"  - {item}")

    if args.decision == "accept" and not publish_ready:
        print("ERROR: acceptance review cannot mark this bundle publish-ready.")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
