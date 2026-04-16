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
    if isinstance(data, dict) and "runtime_patch" in data:
        return data["runtime_patch"]
    return data


def issue(kind: str, message: str) -> dict:
    return {"kind": kind, "message": message}


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: validate_runtime_patch.py /abs/path/to/runtime-patch.yml")
        return 2

    path = Path(sys.argv[1]).expanduser().resolve()
    if not path.is_file():
        print(json.dumps({"result": "FAIL", "issues": [issue("missing_file", f"patch '{path}' does not exist")]}, ensure_ascii=False, indent=2))
        return 1

    try:
        patch = load_payload(path)
    except Exception as exc:
        print(json.dumps({"result": "FAIL", "issues": [issue("parse_error", str(exc))]}, ensure_ascii=False, indent=2))
        return 1

    issues: list[dict] = []
    if not isinstance(patch, dict):
        issues.append(issue("patch_type", "runtime_patch must be a mapping"))
        print(json.dumps({"result": "FAIL", "issues": issues}, ensure_ascii=False, indent=2))
        return 1

    if patch.get("mode") != "patch":
        issues.append(issue("mode", "runtime_patch.mode must be 'patch'"))

    operations = patch.get("operations")
    if not isinstance(operations, list) or not operations:
        issues.append(issue("operations", "runtime_patch.operations must be a non-empty list"))
    else:
        seen: set[str] = set()
        for index, op in enumerate(operations):
            if not isinstance(op, dict):
                issues.append(issue("operation_type", f"operation {index} must be a mapping"))
                continue
            target_path = op.get("target_path")
            opcode = op.get("op")
            restart_required = op.get("restart_required")
            if not isinstance(target_path, str) or not target_path.strip():
                issues.append(issue("target_path", f"operation {index} missing non-empty target_path"))
            elif target_path in seen:
                issues.append(issue("duplicate_target_path", f"duplicate target_path '{target_path}'"))
            else:
                seen.add(target_path)
            if opcode not in {"merge", "replace", "remove"}:
                issues.append(issue("op", f"operation {index} has invalid op '{opcode}'"))
            if not isinstance(restart_required, bool):
                issues.append(issue("restart_required", f"operation {index} restart_required must be boolean"))
            if opcode == "merge" and not isinstance(op.get("value"), dict):
                issues.append(issue("merge_value", f"operation {index} with op=merge must provide an object value"))
            if opcode == "remove" and "value" in op and op.get("value") not in (None, {}):
                issues.append(issue("remove_value", f"operation {index} with op=remove must omit value or use null"))
            if opcode == "replace" and "value" not in op:
                issues.append(issue("replace_value", f"operation {index} with op=replace must provide value"))

    result = "PASS" if not issues else "FAIL"
    print(json.dumps({"result": result, "issues": issues}, ensure_ascii=False, indent=2))
    return 0 if result == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
