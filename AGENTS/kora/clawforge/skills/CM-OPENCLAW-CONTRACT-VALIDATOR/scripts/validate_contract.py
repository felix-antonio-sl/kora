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
    if isinstance(data, dict) and "platform_contract" in data:
        return data["platform_contract"]
    return data


def issue(kind: str, message: str, severity: str = "ERROR") -> dict:
    return {"severity": severity, "kind": kind, "message": message}


def install_key(item: object) -> str | None:
    if isinstance(item, dict):
        for field in ("locator", "slug", "name", "id"):
            value = item.get(field)
            if isinstance(value, str) and value.strip():
                return f"{field}:{value.strip()}"
    return None


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: validate_contract.py /abs/path/to/platform-contract.yml")
        return 2

    path = Path(sys.argv[1]).expanduser().resolve()
    if not path.is_file():
        print(json.dumps({"result": "FAIL", "issues": [issue("missing_file", f"contract '{path}' does not exist")]}, ensure_ascii=False, indent=2))
        return 1

    try:
        contract = load_payload(path)
    except Exception as exc:
        print(json.dumps({"result": "FAIL", "issues": [issue("parse_error", str(exc))]}, ensure_ascii=False, indent=2))
        return 1

    issues: list[dict] = []
    if not isinstance(contract, dict):
        issues.append(issue("contract_type", "platform_contract must be a mapping"))
        print(json.dumps({"result": "FAIL", "issues": issues}, ensure_ascii=False, indent=2))
        return 1

    required_top = ["config_projection", "managed_installs", "deployment_hints", "provenance", "runtime_exclusions"]
    for key in required_top:
        if key not in contract:
            issues.append(issue("missing_top_key", f"missing required key '{key}'"))

    config_projection = contract.get("config_projection", {})
    if isinstance(config_projection, dict):
        for key in ("gateway", "sandbox", "tools", "agents"):
            if key not in config_projection:
                issues.append(issue("config_projection", f"config_projection missing '{key}'"))
        agents = config_projection.get("agents", {})
        if isinstance(agents, dict):
            for key in ("defaults", "list"):
                if key not in agents:
                    issues.append(issue("agents_projection", f"config_projection.agents missing '{key}'"))
        else:
            issues.append(issue("agents_projection", "config_projection.agents must be a mapping"))
    else:
        issues.append(issue("config_projection", "config_projection must be a mapping"))

    deployment_hints = contract.get("deployment_hints", {})
    if isinstance(deployment_hints, dict):
        checks = deployment_hints.get("validation_checks", [])
        if checks is not None:
            if not isinstance(checks, list):
                issues.append(issue("validation_checks", "deployment_hints.validation_checks must be a list"))
            else:
                normalized = [c for c in checks if isinstance(c, str) and c.strip()]
                if len(normalized) != len(checks):
                    issues.append(issue("validation_checks", "deployment_hints.validation_checks contains empty or non-string entries"))
                if len(set(normalized)) != len(normalized):
                    issues.append(issue("validation_checks", "deployment_hints.validation_checks contains duplicates"))
        manual_inputs = deployment_hints.get("manual_inputs_required", [])
        if manual_inputs is not None and not isinstance(manual_inputs, list):
            issues.append(issue("manual_inputs_required", "deployment_hints.manual_inputs_required must be a list"))
    else:
        issues.append(issue("deployment_hints", "deployment_hints must be a mapping"))

    provenance = contract.get("provenance", {})
    if not isinstance(provenance, dict) or not provenance:
        issues.append(issue("provenance", "provenance must be a non-empty mapping"))

    runtime_exclusions = contract.get("runtime_exclusions", [])
    if not isinstance(runtime_exclusions, list):
        issues.append(issue("runtime_exclusions", "runtime_exclusions must be a list"))

    managed_installs = contract.get("managed_installs", {})
    seen: set[str] = set()
    if isinstance(managed_installs, dict):
        for bucket in ("workspace_skills", "skills", "plugins", "bundles"):
            value = managed_installs.get(bucket, [])
            if not isinstance(value, list):
                issues.append(issue("managed_installs", f"managed_installs.{bucket} must be a list"))
                continue
            for item in value:
                key = install_key(item)
                if key and key in seen:
                    issues.append(issue("managed_installs_duplicate", f"duplicate managed install '{key}'"))
                elif key:
                    seen.add(key)
    else:
        issues.append(issue("managed_installs", "managed_installs must be a mapping"))

    result = "PASS" if not issues else "FAIL"
    print(json.dumps({"result": result, "issues": issues}, ensure_ascii=False, indent=2))
    return 0 if result == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
