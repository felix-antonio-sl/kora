import json
import re
from dataclasses import asdict, dataclass
from functools import lru_cache

from .config import KORA_ROOT, OPERATING_CORE_COHORTS
from .workspaces import extract_cm_refs


STATE_LINE_PATTERN = re.compile(r"^\d+\.\s+STATE:\s+(S-[A-Z0-9-]+)\s*(?:->|→)\s*ACT:\s*(.+)$")
RULE_LINE_PATTERN = re.compile(r"^\s*-\s*(Allowed|Forbidden|Rejection)\s*:\s*(.+)$", re.MULTILINE)
AGENT_TOKEN_PATTERN = re.compile(r"\b([a-z0-9-]+/[A-Za-z0-9_-]+)\b")
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


def workspace_dir_from_ref(workspace_ref):
    namespace, name = workspace_ref.split("/", 1)
    return KORA_ROOT / "agents" / namespace / name


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
    targets = set()
    for route in AGENT_TOKEN_PATTERN.findall(text):
        if route != self_workspace:
            targets.add(route)
    return sorted(targets)


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


@lru_cache(maxsize=None)
def load_workspace_contract(workspace_ref):
    workspace_dir = workspace_dir_from_ref(workspace_ref)
    namespace, name = workspace_ref.split("/", 1)
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

    route_targets = set(extract_targets_from_text("\n".join([allowed_line, forbidden_line, rejection_line]), workspace_ref))
    sub_agents = sorted(set(SUB_AGENT_PATTERN.findall(agents_text)))
    handoff_targets = sorted(
        set(sub_agents)
        | set(route_targets)
        | set(extract_targets_from_text(agents_text, workspace_ref))
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
    payload = {"cohorts": {}, "totals": {"workspaces": 0, "states": 0, "tools": 0, "handoffs": 0}}
    for cohort_name, workspaces in OPERATING_CORE_COHORTS.items():
        items = []
        for workspace_ref in workspaces:
            contract = load_workspace_contract(workspace_ref)
            item = {
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
            items.append(item)
            payload["totals"]["workspaces"] += 1
            payload["totals"]["states"] += len(item["state_names"])
            payload["totals"]["tools"] += len(item["tool_names"])
            payload["totals"]["handoffs"] += len(item["handoff_targets"])
        payload["cohorts"][cohort_name] = items
    return payload


def render_operating_core_markdown(payload):
    lines = [
        "# KORA Operating Core Contracts",
        "",
        "Este documento es generado por `scripts/kora sync-docs`. No editar a mano.",
        "",
        "## Resumen",
        "",
        f"- Workspaces cubiertos: {payload['totals']['workspaces']}",
        f"- Estados declarados: {payload['totals']['states']}",
        f"- Tools semanticas declaradas: {payload['totals']['tools']}",
        f"- Handoffs declarados: {payload['totals']['handoffs']}",
    ]

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
