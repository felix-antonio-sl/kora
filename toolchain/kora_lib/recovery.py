"""Recovery inventory for KORA canonical artifacts and local runtime exports."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any

from .artifacts import load_yaml_safe
from .config import AGENTS_ROOT, KNOWLEDGE_ROOT, KORA_ROOT, SKILLS_ROOT


RUNTIME_FILE_NAMES = ("AGENT.md", "SKILL.md", "SOUL.md", "TOOLS.md", "USER.md", "MEMORY.md", "config.json")


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _manifest(path: Path) -> dict[str, Any]:
    doc, _err = load_yaml_safe(path)
    return doc if isinstance(doc, dict) else {}


def _urn_slug(urn: Any) -> str | None:
    if not isinstance(urn, str) or ":" not in urn:
        return None
    return urn.rsplit(":", 1)[-1]


def _rel(path: Path) -> str:
    try:
        return path.resolve().relative_to(KORA_ROOT.resolve()).as_posix()
    except ValueError:
        return str(path.resolve())


def _scan_canonical_agents(agents_root: Path) -> dict[str, dict[str, Any]]:
    items: dict[str, dict[str, Any]] = {}
    if not agents_root.exists():
        return items
    for path in sorted(agents_root.glob("*/*/AGENT.md")):
        if any(part.startswith("_") for part in path.relative_to(agents_root).parts):
            continue
        doc = _manifest(path)
        urn = doc.get("_manifest", {}).get("urn") if isinstance(doc.get("_manifest"), dict) else None
        name = _urn_slug(urn) or path.parent.name
        items[name] = {
            "name": name,
            "urn": urn,
            "status": doc.get("status"),
            "version": doc.get("version"),
            "path": _rel(path),
            "sha256": _sha256(path),
        }
    return items


def _scan_canonical_skills(skills_root: Path) -> dict[str, dict[str, Any]]:
    items: dict[str, dict[str, Any]] = {}
    if not skills_root.exists():
        return items
    for path in sorted(skills_root.glob("*/*/SKILL.md")):
        if any(part.startswith("_") for part in path.relative_to(skills_root).parts):
            continue
        doc = _manifest(path)
        urn = doc.get("_manifest", {}).get("urn") if isinstance(doc.get("_manifest"), dict) else None
        name = _urn_slug(urn) or path.parent.name
        items[name] = {
            "name": name,
            "urn": urn,
            "status": doc.get("status"),
            "version": doc.get("version"),
            "path": _rel(path),
            "sha256": _sha256(path),
        }
    return items


def _scan_staged_agents(agents_root: Path) -> dict[str, dict[str, Any]]:
    items: dict[str, dict[str, Any]] = {}
    for stage in ("INBOX", "REVIEW"):
        root = agents_root / "_FRAGUA" / stage
        if not root.exists():
            continue
        for path in sorted(root.glob("**/AGENT.md")):
            if any(part in path.parts for part in ("_BUILD", "_archivo", "_rebuild_required")):
                continue
            doc = _manifest(path)
            urn = doc.get("_manifest", {}).get("urn") if isinstance(doc.get("_manifest"), dict) else None
            name = _urn_slug(urn) or path.parent.name
            items[name] = {
                "name": name,
                "urn": urn,
                "status": doc.get("status"),
                "version": doc.get("version"),
                "path": _rel(path),
                "stage": stage,
                "sha256": _sha256(path),
            }
    return items


def _scan_staged_skills(skills_root: Path) -> dict[str, dict[str, Any]]:
    items: dict[str, dict[str, Any]] = {}
    for stage in ("INBOX", "REVIEW"):
        root = skills_root / "_TALLER" / stage
        if not root.exists():
            continue
        for path in sorted(root.glob("**/SKILL.md")):
            if any(part in path.parts for part in ("_BUILD", "_archivo", "_rebuild_required")):
                continue
            doc = _manifest(path)
            urn = doc.get("_manifest", {}).get("urn") if isinstance(doc.get("_manifest"), dict) else None
            name = _urn_slug(urn) or path.parent.name
            items[name] = {
                "name": name,
                "urn": urn,
                "status": doc.get("status"),
                "version": doc.get("version"),
                "path": _rel(path),
                "stage": stage,
                "sha256": _sha256(path),
            }
    return items


def _scan_knowledge(knowledge_root: Path) -> dict[str, Any]:
    items: list[dict[str, Any]] = []
    source_gaps = 0
    by_namespace: dict[str, int] = {}
    if not knowledge_root.exists():
        return {"count": 0, "source_gaps": 0, "by_namespace": {}, "items": []}

    for path in sorted(knowledge_root.glob("**/*.md")):
        rel_parts = path.relative_to(knowledge_root).parts
        if "_SCRIPTORIUM" in rel_parts or any(part.startswith(".") for part in rel_parts):
            continue
        doc = _manifest(path)
        manifest = doc.get("_manifest", {}) if isinstance(doc.get("_manifest"), dict) else {}
        urn = manifest.get("urn")
        if not urn:
            continue
        namespace = rel_parts[0] if rel_parts else "_root"
        by_namespace[namespace] = by_namespace.get(namespace, 0) + 1
        provenance = manifest.get("provenance", {}) if isinstance(manifest.get("provenance"), dict) else {}
        has_source = bool(provenance.get("source"))
        if not has_source:
            source_gaps += 1
        items.append(
            {
                "urn": urn,
                "path": _rel(path),
                "namespace": namespace,
                "status": doc.get("status"),
                "family": (doc.get("extensions", {}).get("kora", {}) if isinstance(doc.get("extensions"), dict) else {}).get("family"),
                "has_source": has_source,
            }
        )
    return {
        "count": len(items),
        "source_gaps": source_gaps,
        "by_namespace": dict(sorted(by_namespace.items())),
        "items": items,
    }


def _staging_counts(knowledge_root: Path) -> dict[str, int]:
    scriptorium = knowledge_root / "_SCRIPTORIUM"
    return {
        "knowledge_inbox": len(list((scriptorium / "INBOX").glob("**/*.md"))) if (scriptorium / "INBOX").exists() else 0,
        "knowledge_review": len(list((scriptorium / "REVIEW").glob("**/*.md"))) if (scriptorium / "REVIEW").exists() else 0,
    }


def _mapping_for(
    name: str,
    agents: dict[str, dict[str, Any]],
    skills: dict[str, dict[str, Any]],
    staged_agents: dict[str, dict[str, Any]],
    staged_skills: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    if name in skills:
        return {"status": "mapped_skill", "urn": skills[name]["urn"], "path": skills[name]["path"]}
    if name in agents:
        return {"status": "mapped_agent", "urn": agents[name]["urn"], "path": agents[name]["path"]}
    if name in staged_skills:
        return {
            "status": "staged_skill",
            "urn": staged_skills[name]["urn"],
            "path": staged_skills[name]["path"],
            "stage": staged_skills[name]["stage"],
        }
    if name in staged_agents:
        return {
            "status": "staged_agent",
            "urn": staged_agents[name]["urn"],
            "path": staged_agents[name]["path"],
            "stage": staged_agents[name]["stage"],
        }
    return {"status": "orphan", "urn": None, "path": None}


def _runtime_item(
    path: Path,
    name: str,
    agents: dict[str, dict[str, Any]],
    skills: dict[str, dict[str, Any]],
    staged_agents: dict[str, dict[str, Any]],
    staged_skills: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    mapping = _mapping_for(name, agents, skills, staged_agents, staged_skills)
    file_hash = _sha256(path)
    canonical_hash = None
    if mapping["status"] == "mapped_skill" and name in skills:
        canonical_hash = skills[name]["sha256"]
    elif mapping["status"] == "mapped_agent" and name in agents:
        canonical_hash = agents[name]["sha256"]
    return {
        "name": name,
        "path": str(path.resolve()),
        "sha256": file_hash,
        "mapping": mapping,
        "same_hash_as_canonical": canonical_hash == file_hash if canonical_hash else False,
    }


def _scan_skill_root(
    root: Path,
    agents: dict[str, dict[str, Any]],
    skills: dict[str, dict[str, Any]],
    staged_agents: dict[str, dict[str, Any]],
    staged_skills: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    items = []
    if root.exists():
        for path in sorted(root.glob("**/SKILL.md")):
            if "_BUILD" in path.parts:
                continue
            name = path.parent.name
            items.append(_runtime_item(path, name, agents, skills, staged_agents, staged_skills))
    return {
        "root": str(root),
        "count": len(items),
        "mapped": sum(1 for item in items if item["mapping"]["status"] != "orphan"),
        "orphans": sum(1 for item in items if item["mapping"]["status"] == "orphan"),
        "items": items,
    }


def _scan_claude_agents(
    root: Path,
    agents: dict[str, dict[str, Any]],
    skills: dict[str, dict[str, Any]],
    staged_agents: dict[str, dict[str, Any]],
    staged_skills: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    items = []
    if root.exists():
        for path in sorted(root.glob("*.md")):
            items.append(_runtime_item(path, path.stem, agents, skills, staged_agents, staged_skills))
    return {
        "root": str(root),
        "count": len(items),
        "mapped": sum(1 for item in items if item["mapping"]["status"] != "orphan"),
        "orphans": sum(1 for item in items if item["mapping"]["status"] == "orphan"),
        "items": items,
    }


def _scan_openclaw(
    root: Path,
    agents: dict[str, dict[str, Any]],
    skills: dict[str, dict[str, Any]],
    staged_agents: dict[str, dict[str, Any]],
    staged_skills: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    items = []
    if root.exists():
        for workspace in sorted(path for path in root.iterdir() if path.is_dir()):
            runtime_files = sorted(name for name in RUNTIME_FILE_NAMES if (workspace / name).is_file())
            if not runtime_files:
                continue
            primary = workspace / ("AGENT.md" if "AGENT.md" in runtime_files else runtime_files[0])
            item = _runtime_item(primary, workspace.name, agents, skills, staged_agents, staged_skills)
            item["runtime_files"] = runtime_files
            items.append(item)
    return {
        "root": str(root),
        "count": len(items),
        "mapped": sum(1 for item in items if item["mapping"]["status"] != "orphan"),
        "orphans": sum(1 for item in items if item["mapping"]["status"] == "orphan"),
        "items": items,
    }


def collect_recovery_inventory(
    *,
    agents_root: Path = AGENTS_ROOT,
    skills_root: Path = SKILLS_ROOT,
    knowledge_root: Path = KNOWLEDGE_ROOT,
    home: Path | None = None,
    openclaw_workspaces: Path | None = None,
) -> dict[str, Any]:
    home = home or Path.home()
    openclaw_workspaces = openclaw_workspaces or (home / "openclaw-fleet" / "workspaces")
    agents = _scan_canonical_agents(agents_root)
    skills = _scan_canonical_skills(skills_root)
    staged_agents = _scan_staged_agents(agents_root)
    staged_skills = _scan_staged_skills(skills_root)
    knowledge = _scan_knowledge(knowledge_root)

    return {
        "canonical": {
            "counts": {
                "agents": len(agents),
                "skills": len(skills),
                "knowledge": knowledge["count"],
            },
            "agents": {"items": list(agents.values())},
            "skills": {"items": list(skills.values())},
            "staged_agents": {"count": len(staged_agents), "items": list(staged_agents.values())},
            "staged_skills": {"count": len(staged_skills), "items": list(staged_skills.values())},
            "knowledge": knowledge,
            "staging": _staging_counts(knowledge_root),
        },
        "external": {
            "codex_skills": _scan_skill_root(home / ".codex" / "skills", agents, skills, staged_agents, staged_skills),
            "claude_skills": _scan_skill_root(home / ".claude" / "skills", agents, skills, staged_agents, staged_skills),
            "claude_agents": _scan_claude_agents(home / ".claude" / "agents", agents, skills, staged_agents, staged_skills),
            "openclaw_workspaces": _scan_openclaw(openclaw_workspaces, agents, skills, staged_agents, staged_skills),
        },
    }


def render_recovery_inventory_markdown(payload: dict[str, Any]) -> str:
    canonical = payload["canonical"]
    lines = [
        "# KORA Recovery Inventory",
        "",
        "## Canonical",
        "",
        f"- Agents: {canonical['counts']['agents']}",
        f"- Skills: {canonical['counts']['skills']}",
        f"- Staged agents: {canonical['staged_agents']['count']}",
        f"- Staged skills: {canonical['staged_skills']['count']}",
        f"- Knowledge: {canonical['counts']['knowledge']}",
        f"- Knowledge source gaps: {canonical['knowledge']['source_gaps']}",
        f"- Knowledge INBOX: {canonical['staging']['knowledge_inbox']}",
        f"- Knowledge REVIEW: {canonical['staging']['knowledge_review']}",
        "",
        "## External Runtime Roots",
        "",
        "| Root | Count | Mapped | Orphans |",
        "|------|-------|--------|---------|",
    ]
    for key in ("codex_skills", "claude_skills", "claude_agents", "openclaw_workspaces"):
        section = payload["external"][key]
        lines.append(f"| `{key}` | {section['count']} | {section['mapped']} | {section['orphans']} |")
    lines.extend(["", "## Staged External Matches", ""])
    for key in ("codex_skills", "claude_skills", "claude_agents", "openclaw_workspaces"):
        staged = [item for item in payload["external"][key]["items"] if item["mapping"]["status"].startswith("staged_")]
        if not staged:
            continue
        lines.append(f"### {key}")
        for item in staged:
            lines.append(f"- `{item['name']}` — `{item['mapping']['status']}` at `{item['mapping']['path']}`")
        lines.append("")

    lines.extend(["## Orphans", ""])
    for key in ("codex_skills", "claude_skills", "claude_agents", "openclaw_workspaces"):
        orphans = [item for item in payload["external"][key]["items"] if item["mapping"]["status"] == "orphan"]
        if not orphans:
            continue
        lines.append(f"### {key}")
        for item in orphans:
            lines.append(f"- `{item['name']}` — `{item['path']}`")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def cmd_recovery_inventory(*, json_output: bool = False, output: str | None = None) -> None:
    payload = collect_recovery_inventory()
    content = json.dumps(payload, ensure_ascii=False, indent=2) + "\n" if json_output else render_recovery_inventory_markdown(payload)
    if output:
        out_path = Path(output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(content, encoding="utf-8")
        print(f"Wrote recovery inventory: {out_path}")
    else:
        print(content, end="")
