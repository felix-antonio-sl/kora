import json
import re
from dataclasses import asdict, dataclass
from functools import lru_cache

from .artifacts import load_yaml_safe
from .config import AGENTS_ROOT, KORA_ROOT, META_KORA_AUDIT_WORKSPACES, META_KORA_STATUS, OPERATING_CORE_COHORTS
from .workspaces import extract_cm_refs, extract_workspace_tokens, find_agent_workspace, iter_skill_entrypoints


STATE_LINE_PATTERN = re.compile(r"^\d+\.\s+STATE:\s+(S-[A-Z0-9-]+)\s*(?:->|→)\s*ACT:\s*(.+)$")
RULE_LINE_PATTERN = re.compile(r"^\s*-\s*(Allowed|Forbidden|Rejection)\s*:\s*(.+)$", re.MULTILINE)
SUB_AGENT_PATTERN = re.compile(r"^\s*-\s*Sub-agente:\s*([a-z0-9-]+/[A-Za-z0-9_-]+)", re.MULTILINE)
TOOL_SIGNATURE_PATTERN = re.compile(r"\*\*Firma:\*\*\s*(.+)")
EVIDENCE_PATTERNS = (
    re.compile(r"\bevidencia\b", re.IGNORECASE),
    re.compile(r"\breporte\b", re.IGNORECASE),
    re.compile(r"\bveredicto\b", re.IGNORECASE),
    re.compile(r"PASS\|FAIL"),
    re.compile(r"APROBADO\|RECHAZADO"),
    re.compile(r"\bhallazg", re.IGNORECASE),
    re.compile(r"\bgate\b", re.IGNORECASE),
)
_PLACEHOLDER_TOOL_NAMES = {"firma", "parametros", "parameters", "signature"}


@dataclass(frozen=True)
class ToolContract:
    name: str
    signature: str
    output_signature: str
    body: str


@dataclass(frozen=True)
class CapabilityContract:
    workspace: str
    namespace: str
    name: str
    states: dict
    skill_refs: list
    tools: dict
    tools_allow: list
    allowed_kb: list
    allowed_line: str
    forbidden_line: str
    rejection_line: str
    route_targets: list
    sub_agents: list
    handoff_targets: list
    evidence_lines: list
    report_lines: list
    sources: dict

    def to_dict(self):
        payload = asdict(self)
        payload["tool_names"] = sorted(self.tools.keys())
        payload["state_names"] = sorted(self.states.keys())
        return payload


def build_contract_summary(contract):
    return {
        "workspace": contract.workspace,
        "state_names": sorted(contract.states.keys()),
        "tool_names": sorted(contract.tools.keys()),
        "tools_allow": contract.tools_allow,
        "skill_refs": contract.skill_refs,
        "handoff_targets": contract.handoff_targets,
        "route_targets": contract.route_targets,
        "sub_agents": contract.sub_agents,
        "evidence_lines": contract.evidence_lines,
        "allowed_kb_count": len(contract.allowed_kb),
        "sources": contract.sources,
    }


def workspace_dir_from_ref(workspace_ref):
    resolved = find_agent_workspace(workspace_ref, include_staging=True)
    if resolved is not None:
        return resolved
    namespace, name = workspace_ref.split("/", 1)
    return AGENTS_ROOT / namespace / name


def split_markdown_sections(content):
    sections = {}
    current_heading = None
    current_lines = []
    in_code_block = False

    for line in content.splitlines():
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code_block = not in_code_block
        if not in_code_block and stripped.startswith("## "):
            if current_heading is not None:
                sections[current_heading] = "\n".join(current_lines).strip()
            current_heading = stripped[3:].strip()
            current_lines = []
            continue
        if current_heading is not None:
            current_lines.append(line)

    if current_heading is not None:
        sections[current_heading] = "\n".join(current_lines).strip()
    return sections


def parse_states(agents_text):
    states = {}
    for line in agents_text.splitlines():
        match = STATE_LINE_PATTERN.match(line.strip())
        if not match:
            continue
        state_name, action = match.groups()
        states[state_name] = action.strip()
    return states


def parse_rule_field(agents_text, label):
    for match in RULE_LINE_PATTERN.finditer(agents_text):
        current_label, body = match.groups()
        if current_label == label:
            return body.strip()
    return ""


def extract_targets_from_text(text, self_workspace):
    return sorted(extract_workspace_tokens(text, self_workspace=self_workspace))


def get_section_by_keyword(content, keyword):
    for heading, body in split_markdown_sections(content).items():
        if keyword.lower() in heading.lower():
            return body
    return ""


def extract_evidence_lines(*texts):
    lines = []
    seen = set()
    for text in texts:
        for line in text.splitlines():
            stripped = line.strip()
            if not stripped:
                continue
            if any(pattern.search(stripped) for pattern in EVIDENCE_PATTERNS):
                if stripped not in seen:
                    lines.append(stripped)
                    seen.add(stripped)
    return lines


def build_tool_contracts(tools_text):
    contracts = {}
    for tool_name, body in split_markdown_sections(tools_text).items():
        if tool_name.startswith("1.") or tool_name.startswith("2."):
            continue
        signature_match = TOOL_SIGNATURE_PATTERN.search(body)
        signature = signature_match.group(1).strip() if signature_match else ""
        if "→" in signature:
            output_signature = signature.split("→", 1)[1].strip()
        elif "->" in signature:
            output_signature = signature.split("->", 1)[1].strip()
        else:
            output_signature = ""
        contracts[tool_name] = ToolContract(
            name=tool_name,
            signature=signature,
            output_signature=output_signature,
            body=body,
        )
    return contracts


def _nested_get(mapping, *keys):
    current = mapping
    for key in keys:
        if not isinstance(current, dict):
            return None
        current = current.get(key)
    return current


def _dedupe(items):
    seen = set()
    ordered = []
    for item in items:
        if item in seen:
            continue
        seen.add(item)
        ordered.append(item)
    return ordered


def _is_semantic_tool_name(name):
    if not isinstance(name, str):
        return False
    stripped = name.strip()
    if not stripped or stripped.lower() in _PLACEHOLDER_TOOL_NAMES:
        return False
    return bool(re.fullmatch(r"[A-Za-z0-9._/-]+", stripped))


def _extract_output_signature(signature):
    if "→" in signature:
        return signature.split("→", 1)[1].strip()
    if "->" in signature:
        return signature.split("->", 1)[1].strip()
    return ""


def _build_tool_contracts_from_entries(entries):
    contracts = {}
    for entry in entries or []:
        if not isinstance(entry, dict):
            continue
        name = str(entry.get("name", "")).strip()
        if not _is_semantic_tool_name(name):
            continue
        signature = str(entry.get("parameters") or "").strip()
        description = str(entry.get("description") or "").strip()
        when_to_use = str(entry.get("when_to_use") or "").strip()
        when_not_to_use = str(entry.get("when_not_to_use") or "").strip()
        body = "\n".join(
            part for part in (description, signature, when_to_use, when_not_to_use) if part
        )
        contracts[name] = ToolContract(
            name=name,
            signature=signature,
            output_signature=_extract_output_signature(signature or description),
            body=body,
        )
    return contracts


def _extract_autoria_states(doc):
    states = {}
    state_entries = (
        _nested_get(doc, "artefacto", "plan", "estados")
        or _nested_get(doc, "agent", "plan", "states")
        or []
    )
    for item in state_entries:
        if not isinstance(item, dict):
            continue
        state_id = item.get("id") or item.get("name")
        if not isinstance(state_id, str) or not state_id:
            continue
        action = item.get("accion") or item.get("action") or ""
        states[state_id] = str(action).strip()
    return states


def _extract_autoria_skill_refs(agent_path, doc):
    refs = set(extract_cm_refs(agent_path))
    skill_entries = (
        _nested_get(doc, "artefacto", "skills")
        or _nested_get(doc, "agent", "skills")
        or doc.get("skills")
        or []
    )
    for item in skill_entries:
        if not isinstance(item, dict):
            continue
        skill_id = item.get("id")
        if isinstance(skill_id, str) and skill_id:
            refs.add(skill_id)
    return sorted(refs)


def _extract_autoria_allowed_tools(doc):
    values = (
        _nested_get(doc, "artefacto", "interfaz", "permissions", "allow")
        or _nested_get(doc, "agent", "interface", "permissions", "allow")
        or []
    )
    return sorted(
        _dedupe(
            item.strip()
            for item in values
            if isinstance(item, str) and _is_semantic_tool_name(item)
        )
    )


def _extract_autoria_allowed_kb(doc):
    values = (
        _nested_get(doc, "artefacto", "contexto", "knowledge", "allowed_kb")
        or _nested_get(doc, "agent", "context", "kb_refs")
        or []
    )
    return _dedupe(item for item in values if isinstance(item, str) and item)


def _extract_autoria_sub_agents(doc):
    values = (
        _nested_get(doc, "artefacto", "composicion", "sub_agents")
        or _nested_get(doc, "agent", "composition", "sub_agents")
        or []
    )
    refs = []
    for item in values:
        if isinstance(item, str):
            refs.append(item)
        elif isinstance(item, dict):
            ref = item.get("ref") or item.get("workspace") or item.get("id")
            if isinstance(ref, str):
                refs.append(ref)
    return sorted(
        ref for ref in _dedupe(refs) if re.fullmatch(r"[a-z0-9-]+/[A-Za-z0-9_-]+", ref)
    )


def _build_autoria_sources(workspace_dir):
    sources = {"agent": str((workspace_dir / "AGENT.md").relative_to(KORA_ROOT))}
    memory_path = workspace_dir / "MEMORY.md"
    if memory_path.exists():
        sources["memory"] = str(memory_path.relative_to(KORA_ROOT))
    for index, skill_path in enumerate(iter_skill_entrypoints(workspace_dir / "skills"), start=1):
        sources[f"skill_{index:02d}"] = str(skill_path.relative_to(KORA_ROOT))
    return sources


@lru_cache(maxsize=None)
def load_workspace_contract(workspace_ref):
    workspace_dir = workspace_dir_from_ref(workspace_ref)
    namespace, name = workspace_ref.split("/", 1)
    agent_path = workspace_dir / "AGENT.md"
    if agent_path.exists():
        agent_text = agent_path.read_text(encoding="utf-8")
        agent_doc, _ = load_yaml_safe(agent_path)
        if not isinstance(agent_doc, dict):
            agent_doc = {}
        sources = _build_autoria_sources(workspace_dir)
        source_texts = []
        for rel_path in sources.values():
            abs_path = KORA_ROOT / rel_path
            if abs_path.exists():
                source_texts.append(abs_path.read_text(encoding="utf-8"))
        combined_text = "\n".join(source_texts) if source_texts else agent_text

        states = _extract_autoria_states(agent_doc)
        states.update(parse_states(agent_text))
        states.update(parse_states(combined_text))

        tools = _build_tool_contracts_from_entries(
            _nested_get(agent_doc, "artefacto", "interfaz", "tools")
            or _nested_get(agent_doc, "agent", "interface", "tools")
            or []
        )
        tools_allow = _extract_autoria_allowed_tools(agent_doc)
        if not tools_allow and tools:
            tools_allow = sorted(tools.keys())
        allowed_kb = _extract_autoria_allowed_kb(agent_doc)
        allowed_line = combined_text
        forbidden_line = ""
        rejection_line = ""
        route_targets = extract_targets_from_text(combined_text, workspace_ref)
        sub_agents = sorted(set(_extract_autoria_sub_agents(agent_doc)) | set(SUB_AGENT_PATTERN.findall(combined_text)))
        handoff_targets = sorted(set(route_targets) | set(sub_agents))
        evidence_lines = extract_evidence_lines(*source_texts)
        report_lines = [
            line
            for line in evidence_lines
            if re.search(r"reporte|veredicto|PASS\|FAIL|APROBADO\|RECHAZADO", line, re.IGNORECASE)
        ]

        return CapabilityContract(
            workspace=workspace_ref,
            namespace=namespace,
            name=name,
            states=states,
            skill_refs=_extract_autoria_skill_refs(agent_path, agent_doc),
            tools=tools,
            tools_allow=tools_allow,
            allowed_kb=allowed_kb,
            allowed_line=allowed_line,
            forbidden_line=forbidden_line,
            rejection_line=rejection_line,
            route_targets=sorted(route_targets),
            sub_agents=sub_agents,
            handoff_targets=handoff_targets,
            evidence_lines=evidence_lines,
            report_lines=report_lines,
            sources=sources,
        )

    agents_path = workspace_dir / "AGENTS.md"
    tools_path = workspace_dir / "TOOLS.md"
    config_path = workspace_dir / "config.json"

    agents_text = agents_path.read_text(encoding="utf-8") if agents_path.exists() else ""
    tools_text = tools_path.read_text(encoding="utf-8") if tools_path.exists() else ""
    config_data = json.loads(config_path.read_text(encoding="utf-8")) if config_path.exists() else {}

    states = parse_states(agents_text)
    tools = build_tool_contracts(tools_text)
    allowed_line = parse_rule_field(agents_text, "Allowed")
    forbidden_line = parse_rule_field(agents_text, "Forbidden")
    rejection_line = parse_rule_field(agents_text, "Rejection")
    wiring_text = get_section_by_keyword(agents_text, "Wiring")

    route_targets = set(extract_targets_from_text("\n".join([allowed_line, forbidden_line, rejection_line]), workspace_ref))
    sub_agents = sorted(set(SUB_AGENT_PATTERN.findall(agents_text)))
    handoff_targets = sorted(
        set(sub_agents)
        | set(route_targets)
        | set(extract_targets_from_text(wiring_text, workspace_ref))
    )
    evidence_lines = extract_evidence_lines(agents_text, tools_text)
    report_lines = [
        line for line in evidence_lines if re.search(r"reporte|veredicto|PASS\|FAIL|APROBADO\|RECHAZADO", line, re.IGNORECASE)
    ]

    return CapabilityContract(
        workspace=workspace_ref,
        namespace=namespace,
        name=name,
        states=states,
        skill_refs=sorted(extract_cm_refs(agents_path)) if agents_path.exists() else [],
        tools=tools,
        tools_allow=sorted(config_data.get("tools", {}).get("allow", [])),
        allowed_kb=list(config_data.get("allowed_kb", [])),
        allowed_line=allowed_line,
        forbidden_line=forbidden_line,
        rejection_line=rejection_line,
        route_targets=sorted(route_targets),
        sub_agents=sub_agents,
        handoff_targets=handoff_targets,
        evidence_lines=evidence_lines,
        report_lines=report_lines,
        sources={
            "agents": str(agents_path.relative_to(KORA_ROOT)),
            "tools": str(tools_path.relative_to(KORA_ROOT)),
            "config": str(config_path.relative_to(KORA_ROOT)),
        },
    )


def build_operating_core_payload():
    payload = {
        "cohorts": {},
        "totals": {"workspaces": 0, "states": 0, "tools": 0, "handoffs": 0},
        "meta_kora": {
            "summary": {"total_workspaces": 0, "operating_core": 0, "auxiliary": 0, "staged": 0},
            "workspaces": [],
        },
    }
    for cohort_name, workspaces in OPERATING_CORE_COHORTS.items():
        items = []
        for workspace_ref in workspaces:
            contract = load_workspace_contract(workspace_ref)
            item = build_contract_summary(contract)
            items.append(item)
            payload["totals"]["workspaces"] += 1
            payload["totals"]["states"] += len(item["state_names"])
            payload["totals"]["tools"] += len(item["tool_names"])
            payload["totals"]["handoffs"] += len(item["handoff_targets"])
        payload["cohorts"][cohort_name] = items

    core_workspaces = set()
    for workspaces in OPERATING_CORE_COHORTS.values():
        core_workspaces.update(workspaces)

    for workspace_ref in META_KORA_AUDIT_WORKSPACES:
        contract = load_workspace_contract(workspace_ref)
        item = build_contract_summary(contract)
        status_payload = META_KORA_STATUS[workspace_ref]
        item["status"] = status_payload["status"]
        item["status_reason"] = status_payload["reason"]
        item["in_operating_core"] = workspace_ref in core_workspaces
        payload["meta_kora"]["workspaces"].append(item)
        payload["meta_kora"]["summary"]["total_workspaces"] += 1
        payload["meta_kora"]["summary"].setdefault(item["status"], 0)
        payload["meta_kora"]["summary"][item["status"]] += 1
    return payload


def render_operating_core_markdown(payload):
    lines = [
        "# KORA Operating Core Contracts",
        "",
        "Este documento es generado por `python3 toolchain/kora sync-docs`. No editar a mano.",
        "",
        "## Resumen",
        "",
        f"- Workspaces cubiertos: {payload['totals']['workspaces']}",
        f"- Estados declarados: {payload['totals']['states']}",
        f"- Tools semanticas declaradas: {payload['totals']['tools']}",
        f"- Handoffs declarados: {payload['totals']['handoffs']}",
    ]

    meta_summary = payload["meta_kora"]["summary"]
    lines.extend(
        [
            "",
            "## Auditoria meta-kora",
            "",
            f"- Meta agentes auditados: {meta_summary['total_workspaces']}",
            f"- Meta agentes en nucleo operativo endurecido: {meta_summary['operating_core']}",
            f"- Meta agentes auxiliares explicitamente descopados: {meta_summary['auxiliary']}",
            f"- Meta agentes en staging/revalidacion: {meta_summary.get('staged', 0)}",
            "",
            "| Workspace | Estatus | Estados | Skills | Tools | Handoffs | Motivo |",
            "|-----------|---------|---------|--------|-------|----------|--------|",
        ]
    )
    for item in payload["meta_kora"]["workspaces"]:
        lines.append(
            f"| {item['workspace']} | {item['status']} | {len(item['state_names'])} | {len(item['skill_refs'])} | {len(item['tool_names'])} | {len(item['handoff_targets'])} | {item['status_reason']} |"
        )

    for cohort_name, items in payload["cohorts"].items():
        lines.extend(
            [
                "",
                f"## Cohorte {cohort_name}",
                "",
                "| Workspace | Estados | Tools | Handoffs |",
                "|-----------|---------|-------|----------|",
            ]
        )
        for item in items:
            lines.append(
                f"| {item['workspace']} | {len(item['state_names'])} | {len(item['tool_names'])} | {len(item['handoff_targets'])} |"
            )

    lines.append("")
    return "\n".join(lines)
