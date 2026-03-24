#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path


def load_payload(path: Path):
    text = path.read_text(encoding="utf-8")
    try:
        import yaml  # type: ignore

        data = yaml.safe_load(text)
    except Exception:
        data = json.loads(text)
    if isinstance(data, dict) and "_transmutation" in data:
        return data["_transmutation"]
    return data


def issue(kind: str, message: str) -> dict:
    return {"kind": kind, "message": message}


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: verify_handoff_manifest.py /abs/path/to/_transmutation.yml")
        return 2

    path = Path(sys.argv[1]).expanduser().resolve()
    if not path.is_file():
        print(json.dumps({"result": "FAIL", "issues": [issue("missing_file", f"manifest '{path}' does not exist")]}, ensure_ascii=False, indent=2))
        return 1

    try:
        manifest = load_payload(path)
    except Exception as exc:
        print(json.dumps({"result": "FAIL", "issues": [issue("parse_error", str(exc))]}, ensure_ascii=False, indent=2))
        return 1

    issues: list[dict] = []
    if not isinstance(manifest, dict):
        issues.append(issue("manifest_type", "manifest must be a mapping"))
        print(json.dumps({"result": "FAIL", "issues": issues}, ensure_ascii=False, indent=2))
        return 1

    source = manifest.get("source", {})
    target = manifest.get("target", {})
    metadata = manifest.get("metadata", {})

    if not isinstance(source, dict):
        issues.append(issue("source", "source must be a mapping"))
    else:
        if not source.get("agent") and not source.get("workspace"):
            issues.append(issue("source_agent", "source.agent or source.workspace is required"))
        if not source.get("path") and not source.get("workspace"):
            issues.append(issue("source_path", "source.path or source.workspace is required"))
        hashes = source.get("hashes") or source.get("components")
        if not isinstance(hashes, dict) or not hashes:
            issues.append(issue("source_hashes", "source hashes/components must be a non-empty mapping"))

    if not isinstance(target, dict):
        issues.append(issue("target", "target must be a mapping"))
    else:
        if target.get("platform") != "openclaw":
            issues.append(issue("target_platform", "target.platform must be 'openclaw'"))
        artifacts = target.get("artifacts")
        if not isinstance(artifacts, list) or not artifacts:
            issues.append(issue("target_artifacts", "target.artifacts must be a non-empty list"))

    if not isinstance(metadata, dict):
        issues.append(issue("metadata", "metadata must be a mapping"))
    else:
        for key in ("transmitted_at", "agent_spec_version", "runtime_spec_version"):
            if not metadata.get(key):
                issues.append(issue("metadata_field", f"metadata.{key} is required"))

    if "platform_contract" not in manifest:
        issues.append(issue("platform_contract", "platform_contract is required for openclaw handoff"))

    result = "PASS" if not issues else "FAIL"
    print(json.dumps({"result": result, "issues": issues}, ensure_ascii=False, indent=2))
    return 0 if result == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
