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


def rel_path(path: Path, repo_root: Path) -> str:
    try:
        return str(path.relative_to(repo_root))
    except ValueError:
        return str(path)


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: validate_workspace.py /abs/path/to/AGENTS/<namespace>/<name>")
        return 2

    workspace = Path(sys.argv[1]).expanduser().resolve()
    if not workspace.is_dir():
        print(json.dumps({"result": "FAIL", "error": f"workspace '{workspace}' does not exist"}, ensure_ascii=False, indent=2))
        return 1

    repo_root = repo_root_from_script(Path(__file__))
    scripts_dir = repo_root / "scripts"
    if str(scripts_dir) not in sys.path:
        sys.path.insert(0, str(scripts_dir))

    import jsonschema

    from kora_lib.artifacts import load_yaml_safe
    from kora_lib.config import AGENT_BOOTSTRAP_FILES
    from kora_lib.validation import (
        validate_agents_canonical_structure,
        validate_coinduction_minimum,
        validate_multiturno_minimum,
        validate_skill_purity,
        validate_soul_canonical,
        validate_skill_tool_closure,
        validate_traces_semantics,
        validate_workspace_semantics,
    )
    from kora_lib.workspaces import (
        extract_cm_refs,
        extract_declared_tool_headings,
        extract_skill_symbols,
        extract_workspace_refs,
        find_skill_materialization_conflicts,
        expected_bootstrap_manifest_type,
        iter_skill_bundle_dirs,
        iter_skill_entrypoints,
        validate_skill_bundle_dir,
        validate_skill_file,
    )

    config_path = workspace / "config.json"
    tools_path = workspace / "TOOLS.md"
    agents_path = workspace / "AGENTS.md"
    soul_path = workspace / "SOUL.md"
    skill_dir = workspace / "skills"
    bootstrap_schema_path = repo_root / "schemas" / "kora-agent-schema.json"
    config_schema_path = repo_root / "schemas" / "kora-agent-config-schema.json"

    try:
        config_data = load_json(config_path)
    except Exception as exc:
        print(json.dumps({"result": "FAIL", "error": f"invalid config.json: {exc}"}, ensure_ascii=False, indent=2))
        return 1
    try:
        bootstrap_schema = load_json(bootstrap_schema_path)
        config_schema = load_json(config_schema_path)
    except Exception as exc:
        print(json.dumps({"result": "FAIL", "error": f"invalid validation schema: {exc}"}, ensure_ascii=False, indent=2))
        return 1

    _headings, valid_tool_names, _invalid = extract_declared_tool_headings(tools_path)
    issues = []

    try:
        jsonschema.validate(instance=config_data, schema=config_schema)
    except jsonschema.exceptions.ValidationError as exc:
        issues.append(
            {
                "kind": "config_schema",
                "path": str(config_path),
                "message": exc.message,
            }
        )

    declared_allow = config_data.get("tools", {}).get("allow", [])
    if set(valid_tool_names) != set(declared_allow):
        issues.append(
            {
                "kind": "tool_allow_mismatch",
                "path": str(workspace),
                "message": f"TOOLS.md headings {sorted(valid_tool_names)} != config.json.tools.allow {sorted(declared_allow)}",
            }
        )

    for bootstrap_name in AGENT_BOOTSTRAP_FILES:
        bootstrap_path = workspace / bootstrap_name
        if not bootstrap_path.exists():
            continue
        bootstrap_data, err = load_yaml_safe(bootstrap_path)
        if not bootstrap_data:
            issues.append(
                {
                    "kind": "bootstrap_parse",
                    "path": str(bootstrap_path),
                    "message": f"Could not parse YAML. Error: {err}",
                }
            )
            continue
        try:
            jsonschema.validate(instance=bootstrap_data, schema=bootstrap_schema)
        except jsonschema.exceptions.ValidationError as exc:
            issues.append(
                {
                    "kind": "bootstrap_schema",
                    "path": str(bootstrap_path),
                    "message": exc.message,
                }
            )
        expected_type = expected_bootstrap_manifest_type(bootstrap_path)
        actual_type = bootstrap_data.get("_manifest", {}).get("type") if isinstance(bootstrap_data, dict) else None
        if expected_type and actual_type != expected_type:
            issues.append(
                {
                    "kind": "bootstrap_manifest_type",
                    "path": str(bootstrap_path),
                    "message": f"_manifest.type '{actual_type}' != '{expected_type}'",
                }
            )
        if isinstance(bootstrap_data, dict):
            extra_keys = sorted(set(bootstrap_data.keys()) - {"_manifest", "_md_body"})
            if extra_keys:
                issues.append(
                    {
                        "kind": "bootstrap_frontmatter",
                        "path": str(bootstrap_path),
                        "message": f"bootstrap frontmatter contiene campos fuera de _manifest: {extra_keys}",
                    }
                )

    if agents_path.exists():
        agents_text = agents_path.read_text(encoding="utf-8")
        for failure in validate_agents_canonical_structure(agents_text):
            issues.append({"kind": "agents_grammar", "path": str(agents_path), "message": failure})
        for failure in validate_coinduction_minimum(agents_text):
            issues.append({"kind": "coinduction_minimum", "path": str(agents_path), "message": failure})
        for failure in validate_multiturno_minimum(agents_text):
            issues.append({"kind": "multiturno_minimum", "path": str(agents_path), "message": failure})
        for failure in validate_traces_semantics(agents_path, agents_text):
            issues.append({"kind": "trace_semantics", "path": str(agents_path), "message": failure})
        skill_names = extract_skill_symbols(skill_dir)
        for cm_ref in sorted(extract_cm_refs(agents_path)):
            if cm_ref not in skill_names:
                issues.append(
                    {
                        "kind": "missing_cm",
                        "path": str(agents_path),
                        "message": f"missing referenced skill '{cm_ref}'",
                    }
                )
        for namespace, name in sorted(extract_workspace_refs(agents_path)):
            route_path = repo_root / "AGENTS" / namespace / name
            if not route_path.is_dir():
                issues.append(
                    {
                        "kind": "broken_agent_route",
                        "path": str(agents_path),
                        "message": f"broken cross-agent route '{namespace}/{name}'",
                    }
                )

    if soul_path.exists():
        soul_text = soul_path.read_text(encoding="utf-8")
        for failure in validate_soul_canonical(soul_text):
            issues.append({"kind": "soul_canonical", "path": str(soul_path), "message": failure})

    for symbol in find_skill_materialization_conflicts(skill_dir):
        issues.append(
            {
                "kind": "skill_conflict",
                "path": str(skill_dir),
                "message": f"skill '{symbol}' materialized as both degenerate file and extended bundle",
                }
            )

    for symbol in sorted(extract_skill_symbols(skill_dir)):
        if symbol != symbol.upper():
            issues.append(
                {
                    "kind": "skill_naming",
                    "path": str(skill_dir),
                    "message": f"skill '{symbol}' no usa SCREAMING_CASE (esperado: '{symbol.upper()}')",
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
        skill_data, _ = load_yaml_safe(skill_path)
        if isinstance(skill_data, dict):
            extra_keys = sorted(set(skill_data.keys()) - {"_manifest", "_md_body", "extensions"})
            if extra_keys:
                issues.append(
                    {
                        "kind": "skill_frontmatter",
                        "path": str(skill_path),
                        "message": f"skill frontmatter contiene campos fuera de _manifest/extensions: {extra_keys}",
                    }
                )
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
        "workspace": rel_path(workspace, repo_root),
        "issues": issues,
    }
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0 if not issues else 1


if __name__ == "__main__":
    raise SystemExit(main())
