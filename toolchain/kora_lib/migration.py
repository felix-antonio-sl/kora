import json
import re

import yaml

from .artifacts import dump_yaml_frontmatter_and_body, load_markdown_parts
from .config import (
    AGENTS_ROOT,
    BROKEN_ROUTE_MAPPINGS,
    KB_PIPELINE_NORMALIZATION,
    KORA_ROOT,
    LEGACY_SKILL_HEADING_ALIASES,
    LOW_LEVEL_RUNTIME_HINTS,
    MISSING_SKILL_SPECS,
    SKILLS_ROOT,
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
        "status": "publicado",
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


def ensure_missing_skills(workspace_dir, newly_scaffolded):
    """Create stub skills only for workspaces scaffolded in this migration run.

    This prevents resurrecting skills that were intentionally deleted from
    pre-existing workspaces.
    """
    changed_files = []
    if workspace_dir not in newly_scaffolded:
        return changed_files
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
    """Scaffold minimal guardian workspace (v7 legacy).

    En v8 (pipeline descentralizado), si guardian vive en staging
    `artifacts/agents/_FRAGUA/INBOX/guardian/`, NO se re-scaffoldea productivo;
    queda como deuda de promocion. Esta funcion se conserva solo por
    compatibilidad con `kora migrate --profile transitional` antiguo.
    """
    from .config import META_KORA_STATUS
    from .workspaces import find_agent_workspace

    if META_KORA_STATUS.get("kora/guardian", {}).get("status") == "rebuild_required":
        # Guardian debe reconstruirse desde cero; no reactivar scaffold legacy.
        return []

    if find_agent_workspace("kora/guardian", include_staging=True) is not None:
        # Guardian esta en staging — no re-scaffoldear productivo.
        return []

    workspace_dir = AGENTS_ROOT / "kora" / "guardian"
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
                    "urn:kora:kb:md-spec",
                    "urn:kora:kb:agentfile-spec",
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


def derive_harness_vector_from_legacy(frontmatter, agent_path):
    """Deriva heuristicamente harness_vector PMI x LFS desde campos v1 legacy.

    Se usa durante migracion v1 → v2 del agentfile-spec.
    Ver harness-spec §3 y agentfile-spec v2 §14.
    """
    agent = frontmatter.get("agent", {})

    # Pi (plan) — derivado del FSM declarado en agent.plan
    plan = agent.get("plan", {})
    states = plan.get("states", []) or []
    if not states:
        pi = 0
    elif len(states) <= 1:
        pi = 1
    elif any(isinstance(s.get("transitions"), list) and len(s.get("transitions", [])) > 1 for s in states):
        pi = 2  # FSM ramificado
    else:
        pi = 1  # FSM lineal

    # Mu (materia) — derivado de fibers.memory.mode o inferido
    fibers = agent.get("fibers", {})
    memory_mode = fibers.get("memory", {}).get("mode", "stateless")
    mu_map = {"stateless": 0, "session": 1, "persistent": 2}
    mu = mu_map.get(memory_mode, 0)

    # Xi (interaccion) — derivado de interface + composition
    interface = agent.get("interface", {})
    composition = agent.get("composition", {})
    has_sub_agents = bool(composition.get("sub_agents"))
    has_tools = bool(interface.get("tools"))
    if has_sub_agents and composition.get("golden_paths"):
        xi = 4  # operad dinamica
    elif has_sub_agents:
        xi = 3  # protocolo multi-fase
    elif has_tools:
        xi = 2  # lente polinomial con tools
    elif has_tools is False and plan:
        xi = 1  # atomica
    else:
        xi = 1

    # Lambda (nivel sociotecnico) — inferido por scope y sub_agents
    if has_sub_agents:
        lambda_lvl = 1  # organizacional
    else:
        lambda_lvl = 0  # individual

    # Phi (acoplamiento humano) — derivado de fibers.operator
    operator = fibers.get("operator", {})
    safety_align = agent.get("safety", {}).get("alignment", {})
    if safety_align.get("principal") and operator.get("role"):
        phi = 2  # colaborativo
    elif operator.get("role"):
        phi = 1  # instrumental
    else:
        phi = 0

    # Sigma (vector etico) — defaults conservadores, autor ajusta
    # [safety, fairness, transparency, accountability, sustainability]
    safety_obj = agent.get("safety", {})
    hard_rules = safety_obj.get("hard_rules", {})
    co_induction = safety_obj.get("co_induction", {})
    sigma = [
        2 if hard_rules else 1,              # safety_norm
        1,                                    # fairness (default)
        2 if co_induction else 1,             # transparency
        2 if hard_rules.get("scope") else 1,  # accountability
        1,                                    # sustainability (default)
    ]

    return {
        "pi": pi,
        "mu": mu,
        "xi": xi,
        "lambda": lambda_lvl,
        "phi": phi,
        "sigma": sigma,
    }


def migrate_to_v2_agentfile(workspace_dir, dry_run=False):
    """Agrega extensions.kora.vector_ontologico derivado al AGENT.md si falta.

    Compatibilidad historica: si encuentra harness_vector/presentation, los
    normaliza al glosario vigente en vez de reintroducir overlays legacy.
    """
    agent_path = workspace_dir / "AGENT.md"
    if not agent_path.exists():
        return []

    frontmatter, body = load_markdown_parts(agent_path)
    if not isinstance(frontmatter, dict):
        return []

    extensions = frontmatter.setdefault("extensions", {})
    kora_ext = extensions.setdefault("kora", {})

    changed = False

    if "vector_ontologico" not in kora_ext:
        if isinstance(kora_ext.get("harness_vector"), dict):
            kora_ext["vector_ontologico"] = kora_ext.pop("harness_vector")
        else:
            kora_ext["vector_ontologico"] = derive_harness_vector_from_legacy(frontmatter, agent_path)
        changed = True
    elif "harness_vector" in kora_ext:
        del kora_ext["harness_vector"]
        changed = True

    if "presentation" in kora_ext:
        raw_presentation = kora_ext.pop("presentation")
        kora_ext.setdefault(
            "presentacion",
            AUTORIA_PRESENTACION_MAP.get(raw_presentation, raw_presentation),
        )
        changed = True
    elif "presentacion" not in kora_ext:
        kora_ext["presentacion"] = "estado-primario"
        changed = True

    if not changed:
        return []

    if not dry_run:
        dump_yaml_frontmatter_and_body(agent_path, frontmatter, body)

    return [agent_path]


# ---------------------------------------------------------------------------
# Perfil a-autoria: migracion forzada a autoria-spec v1.2 (una pasada,
# idempotente). Ver serialization/autoria-spec.md §13.
# ---------------------------------------------------------------------------

AUTORIA_STATUS_MAP = {
    "active": "activo",
    "draft": "borrador",
    "deprecated": "deprecado",
    "retired": "retirado",
    "published": "publicado",
}

AUTORIA_PRESENTACION_MAP = {
    "state-primary": "estado-primario",
    "action-primary": "accion-primaria",
}

AUTORIA_PRESCRIPCION_MAP = {
    "high": "alto",
    "medium": "medio",
    "low": "bajo",
}

AUTORIA_FORMA_MATERIAL_MAP = {
    "skill-standard": "habilidad",
    "agent-workspace": "agente-propiamente-tal",
    "agent-platform": "agente-plataforma",
    "subagent": "subagente",
}

AUTORIA_ATLAS_A_MAP = {
    "utility": "utilidad",
    "discipline": "disciplina",
    "delegate": "delegado",
    "person": "persona",
    "orchestrator": "orquestador",
    "service": "servicio",
    "archetype": "arquetipo",
}

AUTORIA_METAFORA_MAP = {
    "super-tool": "supertool",
    "tele-bot": "telebot",
    "active-appliance": "electrodomestico-activo",
    "control-panel": "centro-de-control",
    "centro-control": "centro-de-control",
}

AUTORIA_KORA_KEY_RENAMES = {
    "harness_vector": "vector_ontologico",
    "presentation": "presentacion",
    "skill_freedom": "nivel_prescripcion",
    "allowed_knowledge": "conocimiento_permitido",
    "composable_with": "componible_con",
    "target_environments": "entornos_objetivo",
    "targets": "entornos_objetivo",
}

AUTORIA_ATLAS_KEY_RENAMES = {
    "harness_name": "arnes_categorico",
    "harness": "arnes_categorico",
    "form": "forma_material",
    "relational_metaphor": "metafora_relacional",
    "metaphor": "metafora_relacional",
}

AUTORIA_ENVELOPE_RENAMES = {
    "name": "nombre",
    "description": "descripcion",
}

# Renames profundos del shape agent.* -> artefacto.*
AUTORIA_AGENT_SECTION_RENAMES = {
    "interface": "interfaz",
    "context": "contexto",
    "composition": "composicion",
    "invariants": "invariantes",
    "safety": "invariantes",  # fusion: safety entra como invariantes.*
}

# Dentro de agent.coalgebra.* (promocion a artefacto.perfil.*)
AUTORIA_COALGEBRA_RENAMES = {
    "description": "descripcion",
    "domain": "dominio",
    "triggers": "disparadores",
    "outputs": "salidas",
    "narrative": "narrativa",
    "invariants": "_invariantes_agent_profile",  # se mueve a artefacto.invariantes
}

# Dentro de agent.plan.*
AUTORIA_PLAN_RENAMES = {
    "initial_state": "estado_inicial",
    "terminal_state": "estado_terminal",
    "states": "estados",
}

AUTORIA_PLAN_STATE_RENAMES = {
    "transitions": "transiciones",
    "act": "accion",
}

AUTORIA_PLAN_TRANSITION_RENAMES = {
    "condition": "condicion",
    "target": "destino",
    "priority": "prioridad",
}

# Scaffolds legacy que se eliminan del workspace.
AUTORIA_LEGACY_SCAFFOLDS = (
    "SOUL.md",
    "IDENTITY.md",
    "USER.md",
    "TOOLS.md",
    "AGENTS.md",
    "config.json",
    "README.md",
)

# Subdirs que se renombran a glosario espanol (§15.3).
AUTORIA_SUBDIR_RENAMES = {
    "references": "referencias",
    "assets": "recursos",
    "memory": "memoria",
}

# Artefactos que NO se migran (dependencias en flight, gestionados a mano).
# Se listan como rutas relativas a KORA_ROOT.
AUTORIA_MIGRATION_SKIPLIST = (
    "artifacts/skills/kora/atomize",  # Felix trabaja la linea atomize por separado.
    "artifacts/skills/_TALLER/INBOX/atomize",  # Ubicacion vigente tras re-stage v8.
)


URN_LEGACY_PATTERN = re.compile(
    r"urn:(?P<ns>[a-z0-9\-]+):(?P<kind>agent|skill):(?P<id>[a-z0-9\-]+)(?::(?P<ver>\d+\.\d+\.\d+(?:[a-z0-9\-\.]*)?))?"
)

URN_SPEC_MD_PATTERN = re.compile(r"urn:kora:kb:spec-md\b")


def _autoria_rename_urn(urn_str):
    """urn:{ns}:agent:{id}[:{ver}] | urn:{ns}:skill:{id}[:{ver}] -> canonico.

    Returns tuple (new_urn, extracted_version_or_None).
    """
    if not isinstance(urn_str, str):
        return urn_str, None
    m = URN_LEGACY_PATTERN.match(urn_str.strip())
    if not m:
        return urn_str, None
    ns = m.group("ns")
    artifact_id = m.group("id")
    ver = m.group("ver")
    new_urn = f"urn:{ns}:artefacto:{artifact_id}"
    return new_urn, ver


def _autoria_rewrite_urn_refs(value):
    """Rewrite urn:{ns}:agent:{id} / urn:{ns}:skill:{id}[:{ver}] in any string.

    Also barres urn:kora:kb:spec-md -> urn:kora:kb:md-spec.
    """
    if not isinstance(value, str):
        return value, False
    original = value
    value = URN_SPEC_MD_PATTERN.sub("urn:kora:kb:md-spec", value)

    def _sub(match):
        ns = match.group("ns")
        artifact_id = match.group("id")
        return f"urn:{ns}:artefacto:{artifact_id}"

    value = URN_LEGACY_PATTERN.sub(_sub, value)
    return value, value != original


def _autoria_rewrite_urn_list(items):
    if not isinstance(items, list):
        return items, False
    changed = False
    out = []
    for item in items:
        new_item, did = _autoria_rewrite_urn_refs(item) if isinstance(item, str) else (item, False)
        out.append(new_item)
        changed = changed or did
    return out, changed


def _rename_keys(mapping, rename_map):
    """Rename top-level keys of a dict in place. Returns True if anything changed."""
    if not isinstance(mapping, dict):
        return False
    changed = False
    for old_key, new_key in list(rename_map.items()):
        if old_key == new_key:
            continue
        if old_key in mapping and new_key not in mapping:
            mapping[new_key] = mapping.pop(old_key)
            changed = True
        elif old_key in mapping and new_key in mapping:
            # Target already exists (ya migrado); descartar el legacy.
            mapping.pop(old_key)
            changed = True
    return changed


def _remap_value(mapping, key, value_map):
    if not isinstance(mapping, dict) or key not in mapping:
        return False
    current = mapping[key]
    if not isinstance(current, str):
        return False
    new = value_map.get(current)
    if new is None or new == current:
        return False
    mapping[key] = new
    return True


def _autoria_migrate_envelope(frontmatter):
    """Rename top-level envelope fields: name->nombre, description->descripcion.

    Normalize status to Spanish lifecycle. Ensure lang=es default.
    """
    changed = False
    if _rename_keys(frontmatter, AUTORIA_ENVELOPE_RENAMES):
        changed = True
    if _remap_value(frontmatter, "status", AUTORIA_STATUS_MAP):
        changed = True
    if "lang" not in frontmatter:
        frontmatter["lang"] = "es"
        changed = True
    return changed


def _autoria_migrate_manifest(frontmatter):
    """Rewrite _manifest.urn to artefacto regime, set type=artefacto.

    Tambien mueve `status` y `version` desde `_manifest` al root del
    frontmatter (autoria-spec §3.1). Cierra los codes
    `envelope-status-fuera-de-lugar` y `envelope-version-fuera-de-lugar`
    del validador (adjuncion Check ⊣ Fix sobre envelope).

    Politica de conflicto: si la clave esta en ambos lugares (`_manifest.k`
    y root.k), prevalece root y se elimina la copia en `_manifest`.
    """
    manifest = frontmatter.get("_manifest")
    if not isinstance(manifest, dict):
        return False
    changed = False
    urn = manifest.get("urn")
    if isinstance(urn, str):
        new_urn, extracted_ver = _autoria_rename_urn(urn)
        if new_urn != urn:
            manifest["urn"] = new_urn
            changed = True
        if extracted_ver and not frontmatter.get("version"):
            frontmatter["version"] = extracted_ver
            changed = True
    if manifest.get("type") != "artefacto":
        manifest["type"] = "artefacto"
        changed = True

    # Envelope hoist: status y version siempre en root (autoria-spec §3.1).
    # Politica de conflicto: root prevalece; _manifest.k se elimina sin reescribir root.
    hoisted = {}
    for key in ("version", "status"):
        if key in manifest:
            value = manifest.pop(key)
            if frontmatter.get(key) is None:
                hoisted[key] = value
            changed = True

    if hoisted:
        # Reorganiza el dict para preservar orden idiomatico:
        # _manifest, version, status, resto.
        existing = {k: frontmatter[k] for k in list(frontmatter.keys()) if k != "_manifest"}
        frontmatter.clear()
        frontmatter["_manifest"] = manifest
        for key in ("version", "status"):
            if key in hoisted:
                frontmatter[key] = hoisted[key]
            elif key in existing:
                frontmatter[key] = existing.pop(key)
        frontmatter.update(existing)

    return changed


def _autoria_migrate_kora_overlay(frontmatter):
    """Rename extensions.kora.* legacy keys and atlas slugs to Spanish."""
    extensions = frontmatter.get("extensions")
    if not isinstance(extensions, dict):
        return False
    kora = extensions.get("kora")
    if not isinstance(kora, dict):
        return False

    changed = False
    if _rename_keys(kora, AUTORIA_KORA_KEY_RENAMES):
        changed = True
    if _remap_value(kora, "presentacion", AUTORIA_PRESENTACION_MAP):
        changed = True
    if _remap_value(kora, "nivel_prescripcion", AUTORIA_PRESCRIPCION_MAP):
        changed = True

    atlas = kora.get("atlas")
    if isinstance(atlas, dict):
        if _rename_keys(atlas, AUTORIA_ATLAS_KEY_RENAMES):
            changed = True
        if _remap_value(atlas, "arnes_categorico", AUTORIA_ATLAS_A_MAP):
            changed = True
        if _remap_value(atlas, "forma_material", AUTORIA_FORMA_MATERIAL_MAP):
            changed = True
        if _remap_value(atlas, "metafora_relacional", AUTORIA_METAFORA_MAP):
            changed = True

    for key in ("conocimiento_permitido", "componible_con"):
        if key in kora:
            new_list, did = _autoria_rewrite_urn_list(kora.get(key))
            if did:
                kora[key] = new_list
                changed = True

    return changed


def _autoria_migrate_plan(plan):
    if not isinstance(plan, dict):
        return False
    changed = _rename_keys(plan, AUTORIA_PLAN_RENAMES)
    estados = plan.get("estados")
    if isinstance(estados, list):
        for estado in estados:
            if not isinstance(estado, dict):
                continue
            if _rename_keys(estado, AUTORIA_PLAN_STATE_RENAMES):
                changed = True
            transiciones = estado.get("transiciones")
            if isinstance(transiciones, list):
                for trans in transiciones:
                    if isinstance(trans, dict):
                        if _rename_keys(trans, AUTORIA_PLAN_TRANSITION_RENAMES):
                            changed = True
    return changed


def _autoria_migrate_shape(frontmatter):
    """Rewrite agent.* -> artefacto.*; coalgebra -> perfil; Spanish sub-field renames.

    Idempotente: si `artefacto.*` ya esta en forma canonica, retorna False.
    """
    changed = False

    if "agent" in frontmatter:
        legacy = frontmatter.pop("agent")
        if "artefacto" in frontmatter and isinstance(frontmatter["artefacto"], dict) and isinstance(legacy, dict):
            # Fusion defensiva: ya hay artefacto parcial y sobrevive agent legacy.
            for key, val in legacy.items():
                frontmatter["artefacto"].setdefault(key, val)
        else:
            frontmatter["artefacto"] = legacy
        changed = True

    artefacto = frontmatter.get("artefacto")
    if not isinstance(artefacto, dict):
        return changed

    # coalgebra -> perfil (fusion).
    if "coalgebra" in artefacto:
        coalgebra = artefacto.pop("coalgebra")
        perfil = artefacto.setdefault("perfil", {})
        if isinstance(coalgebra, dict):
            for src, dst in AUTORIA_COALGEBRA_RENAMES.items():
                if src in coalgebra:
                    perfil[dst] = coalgebra.pop(src)
            for leftover_key, leftover_val in coalgebra.items():
                perfil.setdefault(leftover_key, leftover_val)
            # Mueve invariants de coalgebra a artefacto.invariantes.reglas_duras
            legacy_invariants = perfil.pop("_invariantes_agent_profile", None)
            if legacy_invariants:
                invariantes = artefacto.setdefault("invariantes", {})
                existing = invariantes.get("reglas_duras") or []
                if isinstance(existing, list) and isinstance(legacy_invariants, list):
                    invariantes["reglas_duras"] = existing + [
                        rule for rule in legacy_invariants if rule not in existing
                    ]
                elif not existing:
                    invariantes["reglas_duras"] = legacy_invariants
        changed = True

    if _rename_keys(artefacto, AUTORIA_AGENT_SECTION_RENAMES):
        changed = True

    if "fibers" in artefacto:
        fibers = artefacto.pop("fibers")
        if isinstance(fibers, dict):
            contexto = artefacto.setdefault("contexto", {})
            for fk, fv in fibers.items():
                contexto.setdefault(fk, fv)
        changed = True

    if _autoria_migrate_plan(artefacto.get("plan")):
        changed = True

    return changed


def _autoria_sweep_urn_refs(value):
    """Recursively rewrite urn:{ns}:agent:*/skill:* and urn:kora:kb:spec-md in any string inside dict/list."""
    if isinstance(value, str):
        return _autoria_rewrite_urn_refs(value)
    if isinstance(value, list):
        changed_any = False
        for i, item in enumerate(value):
            new_item, did = _autoria_sweep_urn_refs(item)
            if did:
                value[i] = new_item
                changed_any = True
        return value, changed_any
    if isinstance(value, dict):
        changed_any = False
        for k, v in list(value.items()):
            new_v, did = _autoria_sweep_urn_refs(v)
            if did:
                value[k] = new_v
                changed_any = True
        return value, changed_any
    return value, False


def migrate_artifact_to_autoria(path, dry_run=False):
    """Migra un AGENT.md o SKILL.md en sitio a autoria-spec v1.2.

    Idempotente: si ya esta migrado, no hace cambios.
    Retorna lista con el path si cambio.
    """
    if not path.exists():
        return []

    frontmatter, body = load_markdown_parts(path)
    if not isinstance(frontmatter, dict):
        return []

    changed = False
    if _autoria_migrate_manifest(frontmatter):
        changed = True
    if _autoria_migrate_envelope(frontmatter):
        changed = True
    if _autoria_migrate_kora_overlay(frontmatter):
        changed = True
    if _autoria_migrate_shape(frontmatter):
        changed = True

    _, swept = _autoria_sweep_urn_refs(frontmatter)
    if swept:
        changed = True

    # Body: barrer urn:kora:kb:spec-md y urn:{ns}:agent/skill:*.
    new_body, body_changed = _autoria_rewrite_urn_refs(body)
    if body_changed:
        body = new_body
        changed = True

    if changed and not dry_run:
        dump_yaml_frontmatter_and_body(path, frontmatter, body)
    return [path] if changed else []


def _autoria_rename_subdirs(workspace_dir, dry_run=False):
    changed = []
    for old, new in AUTORIA_SUBDIR_RENAMES.items():
        old_path = workspace_dir / old
        new_path = workspace_dir / new
        if old_path.exists() and old_path.is_dir() and not new_path.exists():
            if not dry_run:
                old_path.rename(new_path)
            changed.append(new_path)
    return changed


def _autoria_purge_legacy_scaffolds(workspace_dir, dry_run=False):
    removed = []
    for scaffold in AUTORIA_LEGACY_SCAFFOLDS:
        scaffold_path = workspace_dir / scaffold
        if scaffold_path.exists() and scaffold_path.is_file():
            if not dry_run:
                scaffold_path.unlink()
            removed.append(scaffold_path)
    # skills/ legacy subdir (material embebido v1) — si existe, NO lo borramos
    # aqui; es un path productivo de v1 que el autor revisa manualmente para
    # promover a artifacts/skills/{ns}/{name}/.
    return removed


def _iter_productive_skill_files():
    """Yield SKILL.md paths bajo artifacts/skills/{ns}/{name}/ y artifacts/skills/{name}/ productivos."""
    if not SKILLS_ROOT.exists():
        return
    for entry in sorted(SKILLS_ROOT.iterdir()):
        if not entry.is_dir() or entry.name.startswith(("_", ".")):
            continue
        # Caso A: artifacts/skills/{name}/SKILL.md (top-level productivo)
        direct = entry / "SKILL.md"
        if direct.exists():
            yield direct
            continue
        # Caso B: artifacts/skills/{ns}/{name}/SKILL.md
        for sub in sorted(entry.iterdir()):
            if not sub.is_dir() or sub.name.startswith(("_", ".")):
                continue
            candidate = sub / "SKILL.md"
            if candidate.exists():
                yield candidate


def _is_skipped_for_autoria(path):
    try:
        rel = path.relative_to(KORA_ROOT).as_posix()
    except ValueError:
        return False
    return any(rel == skip or rel.startswith(skip + "/") for skip in AUTORIA_MIGRATION_SKIPLIST)


def migrate_to_autoria(dry_run=False, cohort=None):
    """Perfil a-autoria: migracion forzada de todo el corpus productivo.

    Idempotente: segunda corrida = sin cambios.
    Alcance: artifacts/agents/{ns}/{name}/AGENT.md, artifacts/skills/{ns}/{name}/SKILL.md.
    NO toca staging (_FRAGUA/, _TALLER/, _SCRIPTORIUM/) ni artefactos en
    AUTORIA_MIGRATION_SKIPLIST.
    """
    changed_paths = []

    for workspace_dir in iter_agent_workspaces(cohort=cohort):
        if _is_skipped_for_autoria(workspace_dir):
            continue
        agent_path = workspace_dir / "AGENT.md"
        changed_paths.extend(migrate_artifact_to_autoria(agent_path, dry_run=dry_run))
        changed_paths.extend(_autoria_rename_subdirs(workspace_dir, dry_run=dry_run))
        changed_paths.extend(_autoria_purge_legacy_scaffolds(workspace_dir, dry_run=dry_run))

    # Cohort no aplica a artifacts/skills/ — son portables.
    for skill_path in _iter_productive_skill_files():
        if _is_skipped_for_autoria(skill_path.parent):
            continue
        changed_paths.extend(migrate_artifact_to_autoria(skill_path, dry_run=dry_run))

    return changed_paths


def migrate_agents(profile="transitional", dry_run=False, cohort=None):
    # Perfil a-autoria: ruptura forzada a autoria-spec v1.2. No scaffoldea
    # legacy (SOUL/USER/AGENTS.md). Idempotente. Ver spec §13.
    if profile == "a-autoria":
        return migrate_to_autoria(dry_run=dry_run, cohort=cohort)

    changed_paths = []
    newly_scaffolded = set()
    if profile != "legacy":
        scaffolded = ensure_guardian_workspace() if not dry_run else []
        changed_paths.extend(scaffolded)
        newly_scaffolded.update(scaffolded)

    # Perfil v2-agentfile: auto-derivar vector_ontologico en cada workspace
    if profile == "v2-agentfile":
        for workspace_dir in iter_agent_workspaces(cohort=cohort):
            changed_paths.extend(migrate_to_v2_agentfile(workspace_dir, dry_run=dry_run))
        return changed_paths

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
            changed_paths.extend(ensure_missing_skills(workspace_dir, newly_scaffolded))

    return changed_paths
