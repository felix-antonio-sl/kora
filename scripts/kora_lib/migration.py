import json
import re

import yaml

from .artifacts import dump_yaml_frontmatter_and_body, load_markdown_parts
from .config import (
    BROKEN_ROUTE_MAPPINGS,
    KB_PIPELINE_NORMALIZATION,
    KORA_ROOT,
    LEGACY_SKILL_HEADING_ALIASES,
    LOW_LEVEL_RUNTIME_HINTS,
    MISSING_SKILL_SPECS,
    TOOL_IDENTIFIER_PATTERN,
)
from .workspaces import extract_declared_tool_headings, iter_agent_workspaces


def canonicalize_heading_line(line):
    stripped = line.strip()
    return LEGACY_SKILL_HEADING_ALIASES.get(stripped, stripped)


def ensure_skill_sections(frontmatter, body, skill_name):
    lines = body.splitlines()
    new_lines = []
    for line in lines:
        if line.strip().startswith("## "):
            prefix = line[: len(line) - len(line.lstrip())]
            canonical = canonicalize_heading_line(line)
            if canonical != line.strip():
                new_lines.append(prefix + canonical)
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)
    body = "\n".join(new_lines)

    for heading, stub in (
        ("## Proposito", f"Transformacion cognitiva de {skill_name}."),
        (
            "## Input/Output",
            "- **Input:** contexto actual\n- **Output:** resultado estructurado",
        ),
        (
            "## Procedimiento",
            "1. Analizar el input.\n2. Aplicar la transformacion cognitiva.\n3. Entregar resultado consistente.",
        ),
        ("## Signature Output", "Formato estructurado acorde al dominio del skill."),
    ):
        if heading not in body:
            if heading == "## Input/Output" and "## Procedimiento" in body:
                body = body.replace("## Procedimiento", f"{heading}\n{stub}\n\n## Procedimiento", 1)
            elif heading == "## Signature Output":
                body = body.rstrip() + f"\n\n{heading}\n{stub}\n"
            else:
                body = body.rstrip() + f"\n\n{heading}\n{stub}\n"

    urn = frontmatter.get("_manifest", {}).get("urn", "")
    if ":agent-bootstrap:" in urn:
        parts = urn.split(":")
        namespace = parts[1]
        version = parts[-1]
        frontmatter["_manifest"]["urn"] = f"urn:{namespace}:skill:{skill_name.lower()}:{version}"
    return frontmatter, body


def normalize_tools_markdown(content):
    changed = False
    result = []
    in_code_block = False
    for line in content.splitlines():
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code_block = not in_code_block
            result.append(line)
            continue
        if not in_code_block and stripped.startswith("## "):
            heading = stripped[3:].strip()
            base = heading.split(" (slash command:")[0].strip()
            base = base.split(" (comando:")[0].strip()
            base = base.split(" (command:")[0].strip()
            if TOOL_IDENTIFIER_PATTERN.fullmatch(base):
                if base != heading:
                    indent = line[: len(line) - len(line.lstrip())]
                    line = f"{indent}## {base}"
                    changed = True
            elif not TOOL_IDENTIFIER_PATTERN.fullmatch(heading):
                indent = line[: len(line) - len(line.lstrip())]
                line = f"{indent}### {heading}"
                changed = True
        result.append(line)
    return "\n".join(result) + "\n", changed


def merge_unique(existing, incoming):
    merged = list(existing or [])
    for item in incoming or []:
        if item not in merged:
            merged.append(item)
    return merged


def migrate_config_to_semantic_tools(config_data, semantic_tools):
    changed = False
    tools_cfg = config_data.setdefault("tools", {})
    old_allow = list(tools_cfg.get("allow", []))
    old_deny = list(tools_cfg.get("deny", []))
    semantic_set = sorted(set(semantic_tools))
    runtime_cfg = config_data.setdefault("runtime_capabilities", {})

    if config_data.get("sub_agents", {}).get("max_concurrent") == 0:
        config_data["sub_agents"]["max_concurrent"] = 1
        changed = True

    if old_allow != semantic_set:
        runtime_cfg["allow"] = merge_unique(runtime_cfg.get("allow", []), old_allow)
        semantic_denies = [item for item in old_deny if item in semantic_set]
        runtime_denies = [item for item in old_deny if item not in semantic_set]
        runtime_cfg["deny"] = merge_unique(runtime_cfg.get("deny", []), runtime_denies)
        tools_cfg["allow"] = semantic_set
        tools_cfg["deny"] = semantic_denies
        changed = True
    elif any(item in LOW_LEVEL_RUNTIME_HINTS for item in old_deny):
        runtime_cfg["deny"] = merge_unique(runtime_cfg.get("deny", []), old_deny)
        tools_cfg["deny"] = [item for item in old_deny if item in semantic_set]
        changed = True

    runtime_allow = [item for item in runtime_cfg.get("allow", []) if item not in semantic_set]
    runtime_deny = [item for item in runtime_cfg.get("deny", []) if item not in semantic_set]
    if runtime_allow != runtime_cfg.get("allow", []):
        runtime_cfg["allow"] = runtime_allow
        changed = True
    if runtime_deny != runtime_cfg.get("deny", []):
        runtime_cfg["deny"] = runtime_deny
        changed = True

    return config_data, changed


def apply_route_mappings(content):
    changed = False
    for source, target in BROKEN_ROUTE_MAPPINGS.items():
        if source in content:
            content = content.replace(source, target)
            changed = True
    for source, target in KB_PIPELINE_NORMALIZATION.items():
        if source in content:
            content = content.replace(source, target)
            changed = True
    return content, changed


def scrub_legacy_agent_flags(content):
    changed = False
    patterns = (
        re.compile(r"^\s*-\s*Confidentiality\s*:.*\n?", re.IGNORECASE | re.MULTILINE),
        re.compile(r"^\s*-\s*Response on query\s*:.*\n?", re.IGNORECASE | re.MULTILINE),
    )
    for pattern in patterns:
        new_content, count = pattern.subn("", content)
        if count:
            content = new_content
            changed = True
    return content, changed


def build_minimal_skill_content(
    namespace,
    workspace_name,
    skill_name,
    version,
    purpose,
    input_desc,
    output_desc,
):
    frontmatter = {
        "_manifest": {
            "urn": f"urn:{namespace}:skill:{workspace_name}-{skill_name.lower().replace('cm-', '')}:{version}",
            "type": "lazy_load_endofunctor",
        },
        "version": version,
        "status": "published",
        "lang": "es",
    }
    body = f"""# {skill_name}

## Proposito
{purpose}

## Input/Output
- **Input:** {input_desc}
- **Output:** {output_desc}

## Procedimiento
1. Recibir y estructurar el input relevante.
2. Aplicar la transformacion cognitiva segun el dominio.
3. Entregar un output claro y reutilizable por la FSM.

## Signature Output
Resultado estructurado consistente con el dominio del skill.
"""
    return frontmatter, body


def ensure_missing_skills(workspace_dir):
    changed_files = []
    rel = str(workspace_dir.relative_to(KORA_ROOT))
    skill_specs = MISSING_SKILL_SPECS.get(rel, {})
    if not skill_specs:
        return changed_files

    skill_dir = workspace_dir / "skills"
    skill_dir.mkdir(exist_ok=True)
    namespace = workspace_dir.parent.name
    workspace_name = workspace_dir.name
    version = "1.0.0"
    for skill_name, (purpose, input_desc, output_desc) in skill_specs.items():
        skill_path = skill_dir / f"{skill_name}.md"
        if skill_path.exists():
            continue
        frontmatter, body = build_minimal_skill_content(
            namespace,
            workspace_name,
            skill_name,
            version,
            purpose,
            input_desc,
            output_desc,
        )
        dump_yaml_frontmatter_and_body(skill_path, frontmatter, body)
        changed_files.append(skill_path)
    return changed_files


def ensure_guardian_workspace():
    workspace_dir = KORA_ROOT / "agents" / "kora" / "guardian"
    changed = []
    if workspace_dir.exists():
        return changed

    (workspace_dir / "skills").mkdir(parents=True, exist_ok=True)
    dump_yaml_frontmatter_and_body(
        workspace_dir / "AGENTS.md",
        {"_manifest": {"urn": "urn:kora:agent-bootstrap:guardian-agents:1.0.0", "type": "bootstrap_agents"}},
        """## 1. FSM
1. STATE: S-DISPATCHER -> ACT: Recibir solicitud sobre specs fundacionales. Clasificar: GOVERNANCE|SPEC_REWRITE|VALIDATION|END. -> Trans: IF governance/spec -> S-GOVERNANCE. IF validation -> S-VALIDATION. IF terminar -> S-END.
2. STATE: S-GOVERNANCE -> ACT: Analizar impacto normativo en specs fundacionales y proponer cambios consistentes. -> Trans: IF resuelto -> S-DISPATCHER. IF terminar -> S-END.
3. STATE: S-VALIDATION -> ACT: Verificar consistencia entre specs fundacionales, formal layer y toolchain. -> Trans: IF resuelto -> S-DISPATCHER. IF terminar -> S-END.
4. STATE: S-END -> ACT: Resumen y siguientes pasos. -> Trans: [terminal].

## 2. Reglas Duras
- Scope: specs fundacionales, gobernanza y coherencia normativa del ecosistema KORA
- Forbidden: cambios fuera del dominio de specs fundacionales

## 3. Wiring
- Agente raiz en namespace kora

## 4. Contexto
- Mantener estado de reformas normativas en curso
""",
    )
    dump_yaml_frontmatter_and_body(
        workspace_dir / "SOUL.md",
        {"_manifest": {"urn": "urn:kora:agent-bootstrap:guardian-soul:1.0.0", "type": "bootstrap_soul"}},
        """## Identidad
Custodio de consistencia normativa y formal del ecosistema KORA.

## Tono
Sobrio, preciso, no ornamental.
""",
    )
    dump_yaml_frontmatter_and_body(
        workspace_dir / "USER.md",
        {"_manifest": {"urn": "urn:kora:agent-bootstrap:guardian-user:1.0.0", "type": "bootstrap_user"}},
        """## Perfil
Operador que modifica o audita specs fundacionales de KORA.

## Rutinas
Revisiones de coherencia normativa y migraciones de specs.

## Preferencias de Output
Markdown breve, con reglas, riesgos y decisiones explicitas.
""",
    )
    dump_yaml_frontmatter_and_body(
        workspace_dir / "TOOLS.md",
        {"_manifest": {"urn": "urn:kora:agent-bootstrap:guardian-tools:1.0.0", "type": "bootstrap_tools"}},
        """## kb_route
- **Firma:** query_topic: string -> urn: string
- **Cuando usar:** Cuando se requiere resolver conocimiento formal de KORA.
- **Cuando NO usar:** Cuando la respuesta no depende de la KB.

## repo_health
- **Firma:** {} -> {issues: object[]}
- **Cuando usar:** Cuando se requiere auditar integridad del repo o de las specs.
- **Cuando NO usar:** Cuando basta con una respuesta conceptual sin auditoria.
""",
    )
    (workspace_dir / "config.json").write_text(
        json.dumps(
            {
                "_manifest": {
                    "urn": "urn:kora:agent-bootstrap:guardian-config:1.0.0",
                    "type": "bootstrap_config",
                },
                "allowed_kb": [
                    "urn:kora:kb:gobernanza",
                    "urn:kora:kb:spec-md",
                    "urn:kora:kb:md-spec",
                    "urn:kora:kb:agent-spec-md",
                ],
                "sandbox": {"mode": "strict"},
                "tools": {"allow": ["kb_route", "repo_health"], "deny": []},
                "runtime_capabilities": {
                    "allow": ["analysis"],
                    "deny": ["filesystem_write", "deploy"],
                },
                "sub_agents": {"max_depth": 0},
            },
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )
    changed.append(workspace_dir)
    return changed


def migrate_agents(profile="transitional", dry_run=False, cohort=None):
    changed_paths = []
    if profile != "legacy":
        changed_paths.extend(ensure_guardian_workspace() if not dry_run else [])

    for workspace_dir in iter_agent_workspaces(cohort=cohort):
        agents_path = workspace_dir / "AGENTS.md"
        if agents_path.exists():
            content = agents_path.read_text(encoding="utf-8")
            content, route_changed = apply_route_mappings(content)
            content, scrub_changed = scrub_legacy_agent_flags(content)
            if (route_changed or scrub_changed) and not dry_run:
                agents_path.write_text(content, encoding="utf-8")
                changed_paths.append(agents_path)

        tools_path = workspace_dir / "TOOLS.md"
        semantic_tools = []
        if tools_path.exists():
            tools_content = tools_path.read_text(encoding="utf-8")
            tools_content, tools_changed = normalize_tools_markdown(tools_content)
            if tools_changed and not dry_run:
                tools_path.write_text(tools_content, encoding="utf-8")
                changed_paths.append(tools_path)
            _, semantic_tools, _ = extract_declared_tool_headings(tools_path)

        config_path = workspace_dir / "config.json"
        if config_path.exists():
            config_data = json.loads(config_path.read_text(encoding="utf-8"))
            config_data, cfg_changed = migrate_config_to_semantic_tools(config_data, semantic_tools)
            if cfg_changed and not dry_run:
                config_path.write_text(
                    json.dumps(config_data, indent=2, ensure_ascii=False) + "\n",
                    encoding="utf-8",
                )
                changed_paths.append(config_path)

        skill_dir = workspace_dir / "skills"
        if skill_dir.exists():
            for skill_path in sorted(skill_dir.glob("*.md")):
                original_text = skill_path.read_text(encoding="utf-8")
                frontmatter, body = load_markdown_parts(skill_path)
                if not isinstance(frontmatter, dict):
                    continue
                skill_name = skill_path.stem
                frontmatter, body = ensure_skill_sections(frontmatter, body, skill_name)
                new_text = (
                    "---\n"
                    + yaml.safe_dump(frontmatter, sort_keys=False, allow_unicode=True).strip()
                    + "\n---\n\n"
                    + body.rstrip()
                    + "\n"
                )
                if not dry_run and new_text != original_text:
                    dump_yaml_frontmatter_and_body(skill_path, frontmatter, body)
                    changed_paths.append(skill_path)

        if profile != "legacy" and not dry_run:
            changed_paths.extend(ensure_missing_skills(workspace_dir))

    return changed_paths
