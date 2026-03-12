#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path


def repo_root_from_script(script_path: Path) -> Path:
    return script_path.resolve().parents[6]


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: audit_artifact.py /abs/path/to/artifact.md")
        return 2

    artifact = Path(sys.argv[1]).expanduser().resolve()
    if not artifact.is_file():
        print(json.dumps({"result": "FAIL", "error": f"artifact '{artifact}' does not exist"}, ensure_ascii=False, indent=2))
        return 1

    repo_root = repo_root_from_script(Path(__file__))
    scripts_dir = repo_root / "scripts"
    if str(scripts_dir) not in sys.path:
        sys.path.insert(0, str(scripts_dir))

    from kora_lib.artifacts import load_markdown_parts
    from kora_lib.validation import lint_kora_markdown_parts, resolve_document_family, validate_traces_semantics

    frontmatter, body = load_markdown_parts(artifact)
    if not isinstance(frontmatter, dict):
        print(json.dumps({"result": "FAIL", "error": "frontmatter YAML ausente o invalido"}, ensure_ascii=False, indent=2))
        return 1

    lint_failures = lint_kora_markdown_parts(frontmatter, body or "")
    trace_failures = validate_traces_semantics(artifact, artifact.read_text(encoding="utf-8"))
    payload = {
        "result": "PASS" if not lint_failures and not trace_failures else "FAIL",
        "artifact": str(artifact),
        "family": resolve_document_family(frontmatter),
        "lint_failures": lint_failures,
        "trace_failures": trace_failures,
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0 if payload["result"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
