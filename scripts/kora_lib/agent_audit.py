from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

from .config import GENERATED_DOCS_DIR, KORA_ROOT
from .validation import validate_workspaces
from .workspaces import iter_agent_workspaces


DOMAIN_SUBGROUPS = ("gn", "pro", "fxsl", "korvo")
BASELINE_SPECS = [
    "specs/gobernanza.md",
    "specs/agent-spec-md.md",
    "specs/skill-spec-md.md",
    "specs/md-spec.md",
    "specs/spec-md.md",
    "specs/runtime-spec-md.md",
    "specs/swarm-spec-md.md",
]

SEMANTIC_RUNTIME_CAPABILITIES = {
    "analysis",
    "planning",
    "eval_execution",
    "eval_audit",
}

AGENT_RULES = {
    "agent.fsm_pseudostate_destination": {
        "label": "Destino de control no declarado",
        "severity": "P1",
        "spec_rule": "agent-spec-md §4.2-§4.3",
        "closure_type": "agent_fix",
        "enforcement_candidate": "lint",
        "why": "La FSM solo admite estados declarados `S-*` o `[terminal]`; pseudoestados rompen cierre y verificabilidad.",
    },
    "agent.missing_transition_precedence": {
        "label": "Precedencia de transiciones no declarada",
        "severity": "P2",
        "spec_rule": "agent-spec-md §4.2.6",
        "closure_type": "agent_fix",
        "enforcement_candidate": "manual",
        "why": "Ramas simultaneas sin precedencia dejan el determinismo del agente en estado implícito.",
    },
    "tools.policy_leakage": {
        "label": "Policy operativa filtrada en TOOLS.md",
        "severity": "P2",
        "spec_rule": "agent-spec-md §4.4.4",
        "closure_type": "agent_fix",
        "enforcement_candidate": "lint",
        "why": "TOOLS.md gobierna interfaz semántica; confirmaciones y restricciones operativas pertenecen a config o runtime.",
    },
    "config.semantic_runtime_capability": {
        "label": "Facultad semántica en runtime_capabilities",
        "severity": "P2",
        "spec_rule": "agent-spec-md §5",
        "closure_type": "agent_fix",
        "enforcement_candidate": "lint",
        "why": "runtime_capabilities debe contener permisos crudos del runtime, no facultades abstractas del agente.",
    },
}

SKILL_RULES = {
    "skill.state_variable_leak": {
        "label": "Skill degenerado recibe o emite estado FSM",
        "severity": "P1",
        "spec_rule": "skill-spec-md §3, tabla de patrones prohibidos",
        "closure_type": "agent_fix",
        "enforcement_candidate": "lint",
        "why": "Un skill degenerado no debe codificar variables de estado del agente ni decidir transiciones.",
    },
    "skill.transition_classifier_leak": {
        "label": "Skill degenerado clasifica transiciones o continuidad FSM",
        "severity": "P1",
        "spec_rule": "skill-spec-md §3-§6",
        "closure_type": "agent_fix",
        "enforcement_candidate": "lint",
        "why": "La transición del agente pertenece a AGENTS.md; el skill solo puede producir señal semántica, no control efectivo.",
    },
    "skill.agent_phase_orchestration": {
        "label": "Skill orquesta fases del agente",
        "severity": "P1",
        "spec_rule": "skill-spec-md §3, Orquestacion de fases del agente",
        "closure_type": "agent_fix",
        "enforcement_candidate": "lint",
        "why": "El control secuencial del ciclo del agente no debe vivir dentro del CM degenerado.",
    },
    "skill.relaxes_hard_rule": {
        "label": "Skill relaja o reinterpreta una regla dura del bootstrap",
        "severity": "P1",
        "spec_rule": "skill-spec-md §6.6",
        "closure_type": "agent_fix",
        "enforcement_candidate": "manual",
        "why": "Si una regla dura debe cambiar, se modifica en AGENTS.md o en la spec; no en el skill.",
    },
    "skill.ad_hoc_root_metadata": {
        "label": "Skill prescribe metadata raíz ad hoc",
        "severity": "P2",
        "spec_rule": "gobernanza.md §6 / md-spec §3.1",
        "closure_type": "agent_fix",
        "enforcement_candidate": "lint",
        "why": "La metadata adicional debe tener soporte normativo explícito; no puede aparecer por costumbre dentro de un CM.",
    },
}


def iter_cohort_workspaces():
    yield "meta-kora", list(iter_agent_workspaces(cohort="meta-kora"))
    yield "dev", list(iter_agent_workspaces(cohort="dev"))
    yield "ops", list(iter_agent_workspaces(cohort="ops"))
    domains = list(iter_agent_workspaces(cohort="domains"))
    yield "domains", domains


def rel_path(path: Path) -> str:
    return str(path.relative_to(KORA_ROOT))


def line_numbers_matching(text: str, pattern: re.Pattern[str]):
    lines = []
    for index, line in enumerate(text.splitlines(), start=1):
        if pattern.search(line):
            lines.append((index, line.strip()))
    return lines


def make_finding(workspace, rule_id, path, line, snippet, fix, closure_type=None):
    rule = AGENT_RULES.get(rule_id) or SKILL_RULES.get(rule_id)
    return {
        "workspace": workspace,
        "rule_id": rule_id,
        "rule": rule["label"],
        "severity": rule["severity"],
        "spec_rule": rule["spec_rule"],
        "evidence": {
            "path": str(path),
            "line": line,
            "snippet": snippet,
        },
        "why_real": rule["why"],
        "minimal_fix": fix,
        "closure_type": closure_type or rule["closure_type"],
        "enforcement_candidate": rule["enforcement_candidate"],
    }


def audit_agents_file(workspace: str, path: Path):
    findings = []
    text = path.read_text(encoding="utf-8")

    pseudo_pattern = re.compile(r"->\s*([A-Z][A-Z0-9_-]+)\b")
    for line_no, line in enumerate(text.splitlines(), start=1):
        stripped = line.strip()
        transition_text = None
        if "Trans:" in stripped:
            transition_text = stripped.split("Trans:", 1)[1]
        elif stripped.startswith("- IF"):
            transition_text = stripped
        else:
            continue
        for token in pseudo_pattern.findall(transition_text):
            if token.startswith("S-") or token in {"PASS", "FAIL", "WARN", "WARNING", "ERROR", "OK"}:
                continue
            findings.append(
                make_finding(
                    workspace,
                    "agent.fsm_pseudostate_destination",
                    path,
                    line_no,
                    stripped,
                    "Reemplazar el pseudoestado por un `S-*` declarado o por `[terminal]`, y mover la semántica auxiliar al texto explicativo.",
                )
            )

    return findings


def audit_tools_file(workspace: str, path: Path):
    findings = []
    text = path.read_text(encoding="utf-8")
    policy_pattern = re.compile(
        r"\b(?:siempre requiere confirmacion|requiere confirmacion|requiere aprobacion|solo con aprobacion)\b",
        re.IGNORECASE,
    )
    for line_no, snippet in line_numbers_matching(text, policy_pattern):
        findings.append(
            make_finding(
                workspace,
                "tools.policy_leakage",
                path,
                line_no,
                snippet,
                "Mover la política operativa a `config.json` o al runtime y dejar en TOOLS.md solo semántica de interfaz.",
            )
        )
    return findings


def audit_config_file(workspace: str, path: Path):
    findings = []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return findings

    for capability in data.get("runtime_capabilities", {}).get("allow", []):
        if capability not in SEMANTIC_RUNTIME_CAPABILITIES:
            continue
        findings.append(
            make_finding(
                workspace,
                "config.semantic_runtime_capability",
                path,
                1,
                f'"{capability}" en runtime_capabilities.allow',
                "Mover la facultad semántica a tools/interfaz o eliminarla; mantener en runtime_capabilities solo permisos crudos.",
            )
        )
    return findings


def audit_skill_file(workspace: str, path: Path, agents_text: str):
    findings = []
    text = path.read_text(encoding="utf-8")

    state_var_pattern = re.compile(r"\b(?:current_state|estado_actual\s*:|estado_fsm|fase_actual)\b")
    transition_pattern = re.compile(
        r"\b(?:CONTEXT_SHIFT|NEXT_STATE|estado_destino|la FSM debe volver a despachar|volver a despachar)\b",
        re.IGNORECASE,
    )
    phase_pattern = re.compile(r"^###\s+Fase\s+[0-9]+", re.IGNORECASE)
    deprecated_pattern = re.compile(r"\bdeprecated_by\b")

    for line_no, snippet in line_numbers_matching(text, state_var_pattern):
        findings.append(
            make_finding(
                workspace,
                "skill.state_variable_leak",
                path,
                line_no,
                snippet,
                "Sustituir el estado FSM por una señal semántica del dominio del skill o mover la lógica de control a AGENTS.md.",
            )
        )

    for line_no, snippet in line_numbers_matching(text, transition_pattern):
        findings.append(
            make_finding(
                workspace,
                "skill.transition_classifier_leak",
                path,
                line_no,
                snippet,
                "Eliminar control de transición o continuidad del CM y devolver solo clasificación semántica neutral.",
            )
        )

    if "LIFECYCLE-ORCHESTRATOR" in path.name:
        for line_no, snippet in line_numbers_matching(text, phase_pattern):
            findings.append(
                make_finding(
                    workspace,
                    "skill.agent_phase_orchestration",
                    path,
                    line_no,
                    snippet,
                    "Mover la orquestación secuencial del agente a la FSM y dejar en el skill solo consolidación o transformación local.",
                )
            )

    strict_cr_rule = "CR>1.5" in agents_text and "objetivo" not in agents_text.lower() and "justificacion explicita" not in agents_text.lower()
    if strict_cr_rule and re.search(r"CR\s*<\s*1\.5", text):
        line_no = next((i for i, line in enumerate(text.splitlines(), start=1) if "CR < 1.5" in line or "CR<1.5" in line), 1)
        snippet = text.splitlines()[line_no - 1].strip()
        findings.append(
            make_finding(
                workspace,
                "skill.relaxes_hard_rule",
                path,
                line_no,
                snippet,
                "Alinear el skill con la regla dura vigente o modificar primero el bootstrap/spec que define el umbral.",
            )
        )

    for line_no, snippet in line_numbers_matching(text, deprecated_pattern):
        findings.append(
            make_finding(
                workspace,
                "skill.ad_hoc_root_metadata",
                path,
                line_no,
                snippet,
                "Reemplazar metadata raíz ad hoc por un campo normado o mover la extensión a `extensions.{namespace}` con soporte de spec.",
            )
        )

    return findings


def audit_workspace(workspace_dir: Path):
    workspace = f"{workspace_dir.parent.name}/{workspace_dir.name}"
    findings = []
    agents_path = workspace_dir / "AGENTS.md"
    tools_path = workspace_dir / "TOOLS.md"
    config_path = workspace_dir / "config.json"
    skill_dir = workspace_dir / "skills"

    agents_text = agents_path.read_text(encoding="utf-8") if agents_path.exists() else ""
    if agents_path.exists():
        findings.extend(audit_agents_file(workspace, agents_path))
    if tools_path.exists():
        findings.extend(audit_tools_file(workspace, tools_path))
    if config_path.exists():
        findings.extend(audit_config_file(workspace, config_path))
    if skill_dir.exists():
        for skill_path in sorted(skill_dir.glob("*.md")):
            findings.extend(audit_skill_file(workspace, skill_path, agents_text))
    return findings


def summarize_repeated_findings(findings):
    buckets = defaultdict(list)
    for finding in findings:
        buckets[finding["rule_id"]].append(finding)

    summary = []
    for rule_id, items in sorted(buckets.items(), key=lambda item: (-len(item[1]), item[0])):
        first = items[0]
        summary.append(
            {
                "rule_id": rule_id,
                "rule": first["rule"],
                "severity": first["severity"],
                "count": len(items),
                "workspaces": sorted({item["workspace"] for item in items}),
                "closure_type": first["closure_type"],
                "enforcement_candidate": first["enforcement_candidate"],
            }
        )
    return summary


def build_cohort_payload(name, workspaces):
    validation = validate_workspaces(profile="strict", cohort=name, emit=False)

    workspace_findings = []
    subgroup_payloads = {}

    if name == "domains":
        for subgroup in DOMAIN_SUBGROUPS:
            subgroup_workspaces = [workspace for workspace in workspaces if workspace.parent.name == subgroup]
            subgroup_findings = []
            for workspace_dir in subgroup_workspaces:
                subgroup_findings.extend(audit_workspace(workspace_dir))
            subgroup_payloads[subgroup] = {
                "workspace_count": len(subgroup_workspaces),
                "findings": subgroup_findings,
                "repeated_findings": summarize_repeated_findings(subgroup_findings),
            }
            workspace_findings.extend(subgroup_findings)
    else:
        for workspace_dir in workspaces:
            workspace_findings.extend(audit_workspace(workspace_dir))

    repeated = summarize_repeated_findings(workspace_findings)
    finding_counter = Counter(finding["severity"] for finding in workspace_findings)

    return {
        "name": name,
        "workspace_count": len(workspaces),
        "validate_strict": validation,
        "summary": {
            "findings_total": len(workspace_findings),
            "p1": finding_counter.get("P1", 0),
            "p2": finding_counter.get("P2", 0),
            "p3": finding_counter.get("P3", 0),
            "strict_validate_green": validation["ok"],
        },
        "findings": workspace_findings,
        "repeated_findings": repeated,
        "subgroups": subgroup_payloads or None,
    }


def build_global_summary(cohort_payloads):
    all_findings = []
    for payload in cohort_payloads.values():
        all_findings.extend(payload["findings"])

    repeated = summarize_repeated_findings(all_findings)
    top_systemic = repeated[:5]
    false_greens = [
        item
        for item in repeated
        if item["enforcement_candidate"] == "lint"
    ][:5]

    audited_rules = {}
    for item in repeated:
        audited_rules[item["rule_id"]] = item["count"]

    tracked_rules = list(AGENT_RULES) + list(SKILL_RULES)
    absorbed = [rule_id for rule_id in tracked_rules if rule_id not in audited_rules]
    not_institutionalized = [rule_id for rule_id in tracked_rules if rule_id in audited_rules]

    rollout = {
        "lint": sorted({item["rule"] for item in repeated if item["enforcement_candidate"] == "lint"})[:10],
        "manual": sorted({item["rule"] for item in repeated if item["enforcement_candidate"] == "manual"})[:10],
        "do_not_automate": [
            "Juicios de densidad o calidad semántica sin ancla estructural fuerte",
            "Determinismo cuando depende de semántica de dominio no reducible a patrón estático simple",
        ],
    }

    return {
        "top_systemic_debts": top_systemic,
        "top_false_greens": false_greens,
        "rules_absorbed": absorbed,
        "rules_not_institutionalized": not_institutionalized,
        "enforcement_rollout": rollout,
    }


def build_agent_audit_payload():
    cohorts = {}
    for cohort_name, workspaces in iter_cohort_workspaces():
        cohorts[cohort_name] = build_cohort_payload(cohort_name, workspaces)

    return {
        "generated_at": date.today().isoformat(),
        "baseline_specs": [str(KORA_ROOT / rel) for rel in BASELINE_SPECS],
        "methodology": {
            "cohort_order": ["meta-kora", "dev", "ops", "domains"],
            "rules": [
                "No marcar como hallazgo algo ya aceptado explícitamente por la spec vigente o detectado por validate.",
                "No tratar template drift como prioridad salvo que produzca ambigüedad operacional real.",
            ],
        },
        "cohorts": cohorts,
        "global_summary": build_global_summary(cohorts),
    }


def render_findings_table(findings):
    lines = [
        "| Workspace | Regla | Sev | Evidencia | Fix minimo | Cierre |",
        "|-----------|-------|-----|-----------|------------|--------|",
    ]
    for finding in findings:
        evidence = f"{finding['evidence']['path']}:{finding['evidence']['line']}"
        lines.append(
            f"| {finding['workspace']} | {finding['rule']} | {finding['severity']} | {evidence} | {finding['minimal_fix']} | {finding['closure_type']} |"
        )
    if len(lines) == 2:
        lines.append("| - | Sin hallazgos manuales nuevos | - | - | - | - |")
    return "\n".join(lines)


def render_repeated_findings(repeated_findings):
    lines = [
        "| Regla | Sev | Casos | Workspaces | Cierre |",
        "|-------|-----|-------|------------|--------|",
    ]
    for item in repeated_findings:
        lines.append(
            f"| {item['rule']} | {item['severity']} | {item['count']} | {', '.join(item['workspaces'][:6])} | {item['closure_type']} |"
        )
    if len(lines) == 2:
        lines.append("| - | - | 0 | - | - |")
    return "\n".join(lines)


def render_agent_audit_markdown(payload):
    lines = [
        "# Agent Audit",
        "",
        "Este documento es generado por `scripts/kora sync-docs`. No editar a mano.",
        "",
        "## Resumen global",
        "",
        f"- Fecha: {payload['generated_at']}",
        f"- Cohortes auditadas: {', '.join(payload['methodology']['cohort_order'])}",
        f"- Reglas absorbidas sin hallazgos manuales: {len(payload['global_summary']['rules_absorbed'])}",
        f"- Reglas aun no institucionalizadas: {len(payload['global_summary']['rules_not_institutionalized'])}",
        "",
        "## Top 5 deudas sistemicas",
        "",
        render_repeated_findings(payload["global_summary"]["top_systemic_debts"]),
        "",
        "## Top 5 falsos verdes del validator actual",
        "",
        render_repeated_findings(payload["global_summary"]["top_false_greens"]),
        "",
    ]

    for cohort_name in payload["methodology"]["cohort_order"]:
        cohort = payload["cohorts"][cohort_name]
        lines.extend(
            [
                f"## Cohorte {cohort_name}",
                "",
                f"- Workspaces auditados: {cohort['workspace_count']}",
                f"- `validate --profile strict` verde: {'si' if cohort['summary']['strict_validate_green'] else 'no'}",
                f"- Hallazgos manuales: {cohort['summary']['findings_total']}",
                f"- P1: {cohort['summary']['p1']} | P2: {cohort['summary']['p2']} | P3: {cohort['summary']['p3']}",
                "",
            ]
        )
        if cohort["subgroups"]:
            for subgroup, subgroup_payload in cohort["subgroups"].items():
                lines.extend(
                    [
                        f"### Subgrupo {subgroup}",
                        "",
                        f"- Workspaces: {subgroup_payload['workspace_count']}",
                        f"- Hallazgos: {len(subgroup_payload['findings'])}",
                        "",
                        render_findings_table(subgroup_payload["findings"]),
                        "",
                        "Hallazgos repetidos:",
                        "",
                        render_repeated_findings(subgroup_payload["repeated_findings"]),
                        "",
                    ]
                )
        else:
            lines.extend(
                [
                    render_findings_table(cohort["findings"]),
                    "",
                    "Hallazgos repetidos:",
                    "",
                    render_repeated_findings(cohort["repeated_findings"]),
                    "",
                ]
            )

    lines.extend(
        [
            "## Rollout de enforcement",
            "",
            f"- Pasar a lint: {', '.join(payload['global_summary']['enforcement_rollout']['lint']) or 'ninguno'}",
            f"- Mantener manual: {', '.join(payload['global_summary']['enforcement_rollout']['manual']) or 'ninguno'}",
            "",
        ]
    )
    return "\n".join(lines)


def write_agent_audit_docs(output_dir=GENERATED_DOCS_DIR):
    output_dir.mkdir(parents=True, exist_ok=True)
    payload = build_agent_audit_payload()
    json_path = output_dir / "agent-audit.json"
    md_path = output_dir / "agent-audit.md"
    json_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    md_path.write_text(render_agent_audit_markdown(payload), encoding="utf-8")
    return payload, json_path, md_path
