#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path


def repo_root_from_script(script_path: Path) -> Path:
    return script_path.resolve().parents[6]


def load_json(path: Path):
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: validate_workspace.py /abs/path/to/agents/<namespace>/<name>")
        return 2

    workspace = Path(sys.argv[1]).expanduser().resolve()
    if not workspace.is_dir():
        print(json.dumps({"result": "FAIL", "error": f"workspace '{workspace}' does not exist"}, ensure_ascii=False, indent=2))
        return 1

    repo_root = repo_root_from_script(Path(__file__))
    scripts_dir = repo_root / "scripts"
    if str(scripts_dir) not in sys.path:
        sys.path.insert(0, str(scripts_dir))

    from kora_lib.validation import (
        validate_skill_purity,
        validate_skill_tool_closure,
        validate_traces_semantics,
        validate_workspace_semantics,
    )
    from kora_lib.workspaces import (
        extract_declared_tool_headings,
        find_skill_materialization_conflicts,
        iter_skill_bundle_dirs,
        iter_skill_entrypoints,
        validate_skill_bundle_dir,
        validate_skill_file,
    )

    config_path = workspace / "config.json"
    tools_path = workspace / "TOOLS.md"
    skill_dir = workspace / "skills"

    try:
        config_data = load_json(config_path)
    except Exception as exc:
        print(json.dumps({"result": "FAIL", "error": f"invalid config.json: {exc}"}, ensure_ascii=False, indent=2))
        return 1

    _headings, valid_tool_names, _invalid = extract_declared_tool_headings(tools_path)
    issues = []

    for symbol in find_skill_materialization_conflicts(skill_dir):
        issues.append(
            {
                "kind": "skill_conflict",
                "path": str(skill_dir),
                "message": f"skill '{symbol}' materialized as both degenerate file and extended bundle",
            }
        )

    for bundle_dir in iter_skill_bundle_dirs(skill_dir):
        for failure in validate_skill_bundle_dir(bundle_dir):
            issues.append(
                {
                    "kind": "skill_bundle",
                    "path": str(bundle_dir),
                    "message": failure,
                }
            )

    for skill_path in iter_skill_entrypoints(skill_dir):
        skill_text = skill_path.read_text(encoding="utf-8")
        for failure in validate_skill_file(skill_path):
            issues.append({"kind": "skill_semantics", "path": str(skill_path), "message": failure})
        for failure in validate_skill_purity(skill_text):
            issues.append({"kind": "skill_purity", "path": str(skill_path), "message": failure})
        for failure in validate_skill_tool_closure(skill_text, valid_tool_names):
            issues.append({"kind": "skill_tool_closure", "path": str(skill_path), "message": failure})
        for failure in validate_traces_semantics(skill_path, skill_text):
            issues.append({"kind": "trace_semantics", "path": str(skill_path), "message": failure})

    for failure in validate_workspace_semantics(workspace, config_data, valid_tool_names):
        issues.append({"kind": "workspace_semantics", "path": str(workspace), "message": failure})

    payload = {
        "result": "PASS" if not issues else "FAIL",
        "workspace": str(workspace),
        "issues": issues,
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0 if not issues else 1


if __name__ == "__main__":
    raise SystemExit(main())
