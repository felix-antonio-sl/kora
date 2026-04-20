"""Transmutation orchestrator: proyecta KORA IR a un runtime target.

Implementa el functor T_R: KORA_IR → Runtime_R de transmutation-spec v1.0,
usando las matrices de preservacion declaradas en cada runtime-extension.

Funciones principales:
- cmd_transmute: ejecuta la transmutacion, emite _transmutation.yml y prepara
  el workspace de output en {workspace}/_BUILD/{target}/.
- cmd_ingest: ingesta inversa Lift_R — absorbe un artefacto runtime foraneo
  a KORA IR.
"""

import json
import hashlib
import subprocess
from datetime import datetime, timezone
from pathlib import Path

import yaml

from .artifacts import load_markdown_parts, dump_yaml_frontmatter_and_body
from .catalog import build_catalog_lookup, get_reference_entry, load_catalog
from .config import AGENTS_ROOT, KORA_ROOT, SKILLS_ROOT


# ---------------------------------------------------------------------------
# Matrices de preservacion por runtime (derivadas de runtime-extensions)
# ---------------------------------------------------------------------------

# Formato: cada entrada es { eje_valor: {projected, fidelity, loss?} }
# fidelity ∈ {full, partial, none}

PRESERVATION_MATRIX = {
    "agentskills": {
        # Solo habilidades (forma_material: habilidad) se proyectan aqui.
        # Dominio acotado al de habilidad en autoria-spec §5.1.
        "domain": {"pi": [0,1,2], "mu": [0,1], "xi": [0,1,2], "lambda": [0], "phi": [0,1], "sigma_max": [3,3,3,3,3]},
        "pi":      {0: (0, "full"), 1: (1, "full"), 2: (2, "full"), 3: (None, "none", "agentskills.io no soporta Π=3 en habilidad portable")},
        "mu":      {0: (0, "full"), 1: (1, "full"), 2: (None, "none", "habilidades no tienen memoria persistente en agentskills.io")},
        "xi":      {0: (0, "full"), 1: (1, "full"), 2: (2, "full"), 3: (None, "none"), 4: (None, "none")},
        "lambda":  {0: (0, "full"), 1: (None, "none"), 2: (None, "none"), 3: (None, "none")},
        "phi":     {0: (0, "full"), 1: (1, "full"), 2: (None, "none"), 3: (None, "none"), 4: (None, "none")},
    },
    "claude-code": {
        "domain": {"pi": [0,1,2,3], "mu": [0,1,2], "xi": [0,1,2,3,4], "lambda": [0,1,2], "phi": [0,1,2,3], "sigma_max": [3,2,3,2,1]},
        "pi":      {0: (0, "full"), 1: (1, "full"), 2: (2, "full"), 3: (2, "partial", "fixed-points se aplanan al FSM plano")},
        "mu":      {0: (0, "full"), 1: (1, "full"), 2: (2, "full"), 3: (None, "none", "Claude Code no soporta always-on")},
        "xi":      {0: (0, "full"), 1: (1, "full"), 2: (2, "full"), 3: (2, "partial", "multi-fase se aplana a lente simple"), 4: (2, "partial", "operad dinamica no soportada nativamente")},
        "lambda":  {0: (0, "full"), 1: (1, "full"), 2: (1, "partial", "ecosystem colapsa a organizacional"), 3: (None, "none", "society-in-the-loop no soportado")},
        "phi":     {0: (0, "full"), 1: (1, "full"), 2: (2, "full"), 3: (2, "partial", "hybrid cognition no modelado"), 4: (None, "none", "co-evolutivo no soportado")},
    },
    "codex": {
        "domain": {"pi": [0,1,2,3], "mu": [0,1,2], "xi": [0,1,2,3,4], "lambda": [0,1,2], "phi": [0,1,2,3], "sigma_max": [3,2,2,2,1]},
        "pi":      {0: (0, "full"), 1: (1, "full"), 2: (2, "full"), 3: (3, "partial", "recursion con budget acotado")},
        "mu":      {0: (0, "full"), 1: (1, "full"), 2: (1, "partial", "session-resumable pero no memory:user transparente"), 3: (None, "none", "Codex es CLI sincrono")},
        "xi":      {0: (0, "full"), 1: (1, "full"), 2: (2, "full"), 3: (2, "partial", "multi-fase se aplana"), 4: (2, "partial", "operad no soportada")},
        "lambda":  {0: (0, "full"), 1: (1, "full"), 2: (1, "partial", "ecosystem colapsa"), 3: (None, "none", "society no soportado")},
        "phi":     {0: (0, "full"), 1: (1, "full"), 2: (2, "partial", "sin identidad persistente"), 3: (2, "partial", "hybrid no nativo"), 4: (None, "none", "co-evolutivo no soportado")},
    },
    "gemini": {
        "domain": {"pi": [0,1,2,3], "mu": [0,1,2], "xi": [0,1,2,3,4], "lambda": [0,1,2], "phi": [0,1,2,3], "sigma_max": [3,2,2,1,1]},
        "pi":      {0: (0, "full"), 1: (1, "full"), 2: (2, "full"), 3: (2, "partial", "fixed-points no soportados")},
        "mu":      {0: (0, "full"), 1: (1, "full"), 2: (1, "partial", "memory cross-session limitado"), 3: (None, "none", "Gemini CLI no es daemon")},
        "xi":      {0: (0, "full"), 1: (1, "full"), 2: (2, "full"), 3: (2, "partial"), 4: (2, "partial", "operad no soportada")},
        "lambda":  {0: (0, "full"), 1: (1, "full"), 2: (1, "partial"), 3: (None, "none")},
        "phi":     {0: (0, "full"), 1: (1, "full"), 2: (2, "full"), 3: (2, "partial"), 4: (None, "none")},
    },
    "mastra": {
        "domain": {"pi": [0,1,2,3], "mu": [0,1,2,3], "xi": [0,1,2,3,4], "lambda": [0,1,2], "phi": [0,1,2,3], "sigma_max": [3,2,3,2,1]},
        "pi":      {0: (0, "full"), 1: (1, "full"), 2: (2, "full"), 3: (3, "partial", "workflows y loops existen, pero el fixed-point completo depende del wrapper aplicativo")},
        "mu":      {0: (0, "full"), 1: (1, "full"), 2: (2, "full"), 3: (3, "partial", "persistencia y resume existen; la daemonidad depende del host")},
        "xi":      {0: (0, "full"), 1: (1, "full"), 2: (2, "full"), 3: (3, "full"), 4: (4, "partial", "agent networks y workflows aproximan la operad, pero la topologia dinamica completa queda en la app")},
        "lambda":  {0: (0, "full"), 1: (1, "full"), 2: (2, "partial", "ecosystem via MCP y auth context; fronteras organizacionales dependen del deploy"), 3: (None, "none", "society-in-the-loop no soportado como primitive")},
        "phi":     {0: (0, "full"), 1: (1, "full"), 2: (2, "full"), 3: (3, "partial", "human-in-the-loop y runtime context existen, pero la cognicion hibrida completa es aplicativo"), 4: (None, "none", "co-evolutivo no soportado")},
    },
    "openclaw": {
        "domain": {"pi": [0,1,2,3], "mu": [0,1,2,3], "xi": [0,1,2,3,4], "lambda": [0,1,2,3], "phi": [0,1,2,3], "sigma_max": [3,3,3,3,2]},
        "pi":      {0: (0, "full"), 1: (1, "full"), 2: (2, "full"), 3: (3, "full")},
        "mu":      {0: (0, "full"), 1: (1, "full"), 2: (2, "full"), 3: (3, "full")},
        "xi":      {0: (0, "full"), 1: (1, "full"), 2: (2, "full"), 3: (3, "full"), 4: (4, "full")},
        "lambda":  {0: (0, "full"), 1: (1, "full"), 2: (2, "full"), 3: (3, "partial", "society-in-the-loop requiere gobernanza externa")},
        "phi":     {0: (0, "full"), 1: (1, "full"), 2: (2, "full"), 3: (3, "partial"), 4: (None, "none", "co-evolutivo no soportado")},
    },
}

TARGET_ADAPTERS = {
    "claude-code": "transmute-claude-code",
    "openclaw": "transmute-openclaw",
    "codex": "transmute-codex",
    "gemini": "transmute-gemini",
    "mastra": "transmute-mastra",
    "agentskills": None,  # proyeccion directa sin LLM (byte-identical)
}

SUPPORTED_TARGETS = tuple(PRESERVATION_MATRIX.keys())


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _sha256(path: Path) -> str:
    """Return sha256:<hex> of file contents."""
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def _resolve_agent_path(agent_ref: str) -> Path:
    parts = agent_ref.strip().split("/")
    if len(parts) != 2:
        raise ValueError(f"Agent ref must be 'namespace/name', got: {agent_ref}")
    ns, name = parts
    agent_dir = AGENTS_ROOT / ns / name
    if not agent_dir.is_dir():
        raise ValueError(f"Agent directory not found: {agent_dir}")
    agent_md = agent_dir / "AGENT.md"
    if not agent_md.is_file():
        raise ValueError(f"AGENT.md not found: {agent_md}")
    return agent_md


def _build_target_path(ns: str, name: str, target: str) -> Path:
    """Output vive en {workspace}/_BUILD/{target}/ segun gobernanza §3.2 y runtime-spec-md."""
    return AGENTS_ROOT / ns / name / "_BUILD" / target


def _get_harness_vector(frontmatter: dict) -> dict:
    """Extrae el vector ontologico PMI × LFS del IR.

    Acepta ambos nombres por compatibilidad:
      - `vector_ontologico` (canonico en autoria-spec v1.0+, glosario es)
      - `harness_vector` (legacy pre-unificacion)
    """
    kora_ext = frontmatter.get("extensions", {}).get("kora", {})
    vector = kora_ext.get("vector_ontologico") or kora_ext.get("harness_vector")
    if not isinstance(vector, dict):
        raise ValueError(
            "Missing extensions.kora.vector_ontologico. "
            "Run `kora migrate --perfil a-autoria` to normalize shape."
        )
    return vector


def _project_axis(axis_name: str, value, matrix: dict):
    """Aplica la proyeccion de un eje segun la matriz del runtime.

    Returns: (projected_value, fidelity, loss_reason | None)
    """
    if axis_name == "sigma":
        # sigma es vector: componente a componente con sigma_max
        sigma_max = matrix["domain"]["sigma_max"]
        if not isinstance(value, list) or len(value) != 5:
            raise ValueError(f"sigma must be list of 5 ints, got: {value}")
        projected = [min(v, maxv) for v, maxv in zip(value, sigma_max)]
        losses = []
        for i, (v, maxv) in enumerate(zip(value, sigma_max)):
            if v > maxv:
                comp = ["safety_norm", "fairness", "transparency", "accountability", "sustainability"][i]
                losses.append(f"{comp}: declared {v}, projected {maxv}")
        fidelity = "partial" if losses else "full"
        return projected, fidelity, "; ".join(losses) if losses else None

    rules = matrix.get(axis_name, {})
    if value not in rules:
        raise ValueError(f"Axis {axis_name} value {value} not in matrix domain")
    entry = rules[value]
    if len(entry) == 2:
        return entry[0], entry[1], None
    return entry[0], entry[1], entry[2]


def _project_vector(vector: dict, target: str):
    """Proyecta vector IR al dominio del runtime. Falla si fuera de dominio.

    Returns: (projected_vector, projections_detail_dict)
    """
    matrix = PRESERVATION_MATRIX.get(target)
    if not matrix:
        raise ValueError(f"Unknown target: {target}. Supported: {SUPPORTED_TARGETS}")

    projected = {}
    detail = {}
    out_of_domain = []

    for axis in ("pi", "mu", "xi", "lambda", "phi", "sigma"):
        v = vector.get(axis)
        try:
            proj, fid, loss = _project_axis(axis, v, matrix)
        except ValueError as e:
            out_of_domain.append(str(e))
            continue
        if proj is None and fid == "none":
            out_of_domain.append(f"{axis}={v}: {loss or 'not supported'}")
        else:
            projected[axis] = proj
            detail[axis] = {"projected_to": proj, "fidelity": fid}
            if loss:
                detail[axis]["loss"] = loss

    if out_of_domain:
        raise ValueError(
            f"Vector excedes dominio de {target}:\n  - " +
            "\n  - ".join(out_of_domain) +
            f"\n\nConsulta {target}-runtime-extension §3."
        )

    return projected, detail


def _resolve_adapter_skill(target: str) -> Path | None:
    """Adapter skill (opcional): si no existe, se usa matriz directa."""
    adapter_name = TARGET_ADAPTERS.get(target)
    if not adapter_name:
        return None
    skill_md = SKILLS_ROOT / "kora" / adapter_name / "SKILL.md"
    return skill_md if skill_md.is_file() else None


def append_retrieval_record(record: dict, path: Path | None = None) -> Path:
    """Append retrieval evidence to docs/generated/retrieval.jsonl."""
    target = path or (KORA_ROOT / "docs" / "generated" / "retrieval.jsonl")
    target.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "ts": datetime.now(timezone.utc).isoformat(),
        **record,
    }
    with target.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(payload, ensure_ascii=False) + "\n")
    return target


def append_lead_time_record(record: dict, path: Path | None = None) -> Path:
    """Append lead-time evidence to docs/generated/lead-time.jsonl."""
    target = path or (KORA_ROOT / "docs" / "generated" / "lead-time.jsonl")
    target.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "ts": datetime.now(timezone.utc).isoformat(),
        **record,
    }
    with target.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(payload, ensure_ascii=False) + "\n")
    return target


def _git_last_commit_ts(path: Path) -> datetime | None:
    try:
        result = subprocess.run(
            ["git", "log", "-1", "--format=%cI", "--", str(path)],
            cwd=str(KORA_ROOT),
            capture_output=True,
            text=True,
            check=False,
        )
    except Exception:
        return None
    value = (result.stdout or "").strip()
    if not value:
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def stamp_verified_at(path: Path, timestamp: datetime | None = None) -> Path:
    frontmatter, body = load_markdown_parts(path)
    if not isinstance(frontmatter, dict):
        raise ValueError(f"No YAML frontmatter in {path}")
    ts = (timestamp or datetime.now(timezone.utc)).isoformat()
    extensions = frontmatter.setdefault("extensions", {})
    kora_ext = extensions.setdefault("kora", {})
    kora_ext["verified_at"] = ts
    content = "---\n"
    content += yaml.safe_dump(frontmatter, sort_keys=False, allow_unicode=True).strip()
    content += "\n---\n\n"
    content += body.rstrip() + "\n"
    path.write_text(content, encoding="utf-8")
    return path


def append_invocation_record(record: dict, path: Path | None = None, retrieval_path: Path | None = None) -> Path:
    """Append a canary/runtime invocation record to docs/generated/invocations.jsonl."""
    target = path or (KORA_ROOT / "docs" / "generated" / "invocations.jsonl")
    target.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "ts": datetime.now(timezone.utc).isoformat(),
        **record,
    }
    with target.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(payload, ensure_ascii=False) + "\n")
    retrieval_urns = record.get("retrieval_urns")
    if isinstance(retrieval_urns, list) and retrieval_urns:
        append_retrieval_record(
            {
                "agent_urn": record.get("agent_urn", ""),
                "retrieval_urns": retrieval_urns,
                "input_hash": record.get("input_hash", ""),
            },
            path=retrieval_path,
        )
    return target


def _collect_knowledge_contract(frontmatter: dict) -> dict:
    kora_ext = (frontmatter.get("extensions") or {}).get("kora") or {}
    artefacto = frontmatter.get("artefacto") or {}
    contexto = artefacto.get("contexto") or {}
    knowledge = contexto.get("knowledge") or {}
    agent = frontmatter.get("agent") or {}
    legacy_knowledge = agent.get("knowledge") or {}

    allowed_urns = []
    for bucket in (
        kora_ext.get("conocimiento_permitido") or [],
        knowledge.get("allowed_kb") or [],
        legacy_knowledge.get("allowed_kb") or [],
        agent.get("context", {}).get("kb_refs") or [],
    ):
        if not isinstance(bucket, list):
            continue
        for urn in bucket:
            if isinstance(urn, str) and urn and urn not in allowed_urns:
                allowed_urns.append(urn)

    routes = {}
    for route_map in (
        knowledge.get("kb_routes") or {},
        legacy_knowledge.get("kb_routes") or {},
    ):
        if not isinstance(route_map, dict):
            continue
        for route_name, urn in route_map.items():
            if isinstance(route_name, str) and isinstance(urn, str) and urn:
                routes[route_name] = urn
                if urn not in allowed_urns:
                    allowed_urns.append(urn)

    catalog = load_catalog()
    resolved_paths = {}
    unresolved_urns = []
    route_entries = {}
    if catalog and "Catalog" in catalog:
        known_urns, urn_to_entry = build_catalog_lookup(catalog)
        for urn in allowed_urns:
            entry = get_reference_entry(urn, urn_to_entry) if urn in known_urns or get_reference_entry(urn, urn_to_entry) else None
            if entry:
                resolved_paths[urn] = str(entry["file"].relative_to(KORA_ROOT))
            else:
                resolved_paths[urn] = None
                unresolved_urns.append(urn)
        for route_name, urn in routes.items():
            route_entries[route_name] = {
                "urn": urn,
                "path": resolved_paths.get(urn),
            }
    else:
        for urn in allowed_urns:
            resolved_paths[urn] = None
        unresolved_urns = list(allowed_urns)
        for route_name, urn in routes.items():
            route_entries[route_name] = {"urn": urn, "path": None}

    return {
        "allowed_urns": allowed_urns,
        "routes": route_entries,
        "resolved_paths": resolved_paths,
        "unresolved_urns": unresolved_urns,
    }


def record_invocation(
    *,
    agent_urn: str,
    input_text: str,
    output_text: str,
    eval_result: str,
    retrieval_urns: list[str] | None = None,
    verified_paths: list[Path] | None = None,
    source_paths: list[Path] | None = None,
    invocations_path: Path | None = None,
    retrieval_path: Path | None = None,
    lead_time_path: Path | None = None,
) -> Path:
    retrieval_urns = retrieval_urns or []
    verified_paths = verified_paths or []
    source_paths = source_paths or []
    input_hash = "sha256:" + hashlib.sha256(input_text.encode()).hexdigest()
    output_hash = "sha256:" + hashlib.sha256(output_text.encode()).hexdigest()
    invocation_path = append_invocation_record(
        {
            "agent_urn": agent_urn,
            "input_hash": input_hash,
            "output_hash": output_hash,
            "eval_result": eval_result,
            "retrieval_urns": retrieval_urns,
        },
        path=invocations_path,
        retrieval_path=retrieval_path,
    )
    event_ts = datetime.now(timezone.utc)
    for path in verified_paths:
        stamp_verified_at(Path(path), timestamp=event_ts)
    for path in source_paths:
        commit_ts = _git_last_commit_ts(Path(path))
        if commit_ts is None:
            continue
        append_lead_time_record(
            {
                "agent_urn": agent_urn,
                "source_path": str(path),
                "source_commit_ts": commit_ts.isoformat(),
                "observed_ts": event_ts.isoformat(),
                "lead_time_seconds": max(0.0, (event_ts - commit_ts).total_seconds()),
                "eval_result": eval_result,
            },
            path=lead_time_path,
        )
    return invocation_path


def _extract_provenance_value(text: str, label: str) -> str:
    prefix = f"- {label}: `"
    for line in text.splitlines():
        if line.startswith(prefix) and line.endswith("`"):
            return line[len(prefix):-1]
    return ""


def build_deploy_status_report(
    claude_agents_dir: Path | None = None,
    openclaw_workspaces_dir: Path | None = None,
) -> dict:
    from .workspaces import iter_agent_workspaces

    claude_dir = Path(claude_agents_dir or Path.home() / ".claude" / "agents").expanduser()
    openclaw_dir = Path(openclaw_workspaces_dir or Path.home() / "openclaw-fleet" / "workspaces").expanduser()

    agents = []
    summary = {"ok": 0, "stale": 0, "missing": 0, "unsupported": 0}

    for workspace_dir in iter_agent_workspaces():
        agent_md = workspace_dir / "AGENT.md"
        frontmatter, _ = load_markdown_parts(agent_md)
        if not isinstance(frontmatter, dict):
            continue
        current_hash = _sha256(agent_md)
        targets = ((frontmatter.get("extensions") or {}).get("kora") or {}).get("entornos_objetivo") or []
        item = {"agent": f"{workspace_dir.parent.name}/{workspace_dir.name}"}

        for target in targets:
            if target == "claude-code":
                deployed_path = claude_dir / f"{workspace_dir.name}.md"
                if not deployed_path.exists():
                    status = {"status": "missing", "path": str(deployed_path)}
                else:
                    text = deployed_path.read_text(encoding="utf-8")
                    deployed_hash = _extract_provenance_value(text, "Source Hash")
                    status = {
                        "status": "ok" if deployed_hash == current_hash else "stale",
                        "path": str(deployed_path),
                        "source_hash": deployed_hash,
                        "current_hash": current_hash,
                    }
                item[target] = status
                summary[status["status"]] += 1
            elif target == "openclaw":
                deployed_path = openclaw_dir / workspace_dir.name
                status = {"status": "missing" if not deployed_path.exists() else "unsupported", "path": str(deployed_path)}
                item[target] = status
                summary[status["status"]] += 1
        agents.append(item)

    return {"summary": summary, "agents": agents}


def cmd_deploy_status():
    report = build_deploy_status_report()
    print("=== KORA Deploy Status ===\n")
    for item in report["agents"]:
        print(f"[{item['agent']}]")
        for target, status in item.items():
            if target == "agent":
                continue
            print(f"  - {target}: {status['status']} ({status['path']})")
    print("\nSummary:")
    for key, value in report["summary"].items():
        print(f"  {key}: {value}")
    if report["summary"]["stale"] > 0:
        raise SystemExit(1)


def cmd_record_invocation(
    *,
    agent_urn: str,
    input_text: str,
    output_text: str,
    eval_result: str,
    retrieval_urns: list[str] | None = None,
    verified_paths: list[str] | None = None,
    source_paths: list[str] | None = None,
):
    record_invocation(
        agent_urn=agent_urn,
        input_text=input_text,
        output_text=output_text,
        eval_result=eval_result,
        retrieval_urns=retrieval_urns or [],
        verified_paths=[KORA_ROOT / path for path in (verified_paths or [])],
        source_paths=[KORA_ROOT / path for path in (source_paths or [])],
    )
    print("Invocation recorded.")


def _emit_transmutation_yml(target_dir: Path, agent_md_path: Path, target: str,
                             ns: str, name: str, version: str,
                             source_hash: str, frontmatter: dict,
                             vector: dict, projected: dict,
                             projections_detail: dict):
    """Emite _transmutation.yml conforme transmutation-spec §6."""
    adapter = _resolve_adapter_skill(target)
    presentation = frontmatter.get("extensions", {}).get("kora", {}).get("presentation", "state-primary")
    knowledge_contract = _collect_knowledge_contract(frontmatter)

    manifest = {
        "transmutation": {
            # Identificacion
            "source_urn": frontmatter.get("_manifest", {}).get("urn", ""),
            "source_version": version,
            "source_path": str(agent_md_path.relative_to(KORA_ROOT)),
            "source_hash": source_hash,
            "target": target,
            "functor": f"T_{target}_v1.0",
            "adapter_skill": str(adapter.relative_to(KORA_ROOT)) if adapter else None,
            "timestamp": datetime.now(timezone.utc).isoformat(),

            # Vector IR fuente
            "source_vector": {
                "pi": vector.get("pi"),
                "mu": vector.get("mu"),
                "xi": vector.get("xi"),
                "lambda": vector.get("lambda"),
                "phi": vector.get("phi"),
                "sigma": vector.get("sigma"),
                "presentation": presentation,
            },

            # Preservacion estructural (obligatoria - transmutation-spec §3.2)
            "structural_preservation": {
                "composition": "preserved",
                "identity": "preserved",
                "xi_naturality": "preserved",
                "safety_closure": "preserved",
                "kleisli_composition": "preserved",
                "pi_monotonicity": "preserved",
                "mu_monotonicity": "preserved",
                "xi_monotonicity": "preserved",
            },

            # Proyeccion por eje
            "projections": projections_detail,

            # Claim de bisimulacion
            "bisimulation_claim": "equivalent-modulo-projections",
            "bisimulation_scope": f"observaciones soportadas por {target}",

            # Referencias
            "references": {
                "harness_spec": "urn:kora:kb:harness-spec",
                "transmutation_spec": "urn:kora:kb:transmutation-spec",
                "runtime_extension": f"urn:kora:kb:{target}-runtime-extension"
                    if target != "openclaw"
                    else "urn:agengai:kb:openclaw-runtime-extension",
            },
            "knowledge_contract": knowledge_contract,
        }
    }

    yml_path = target_dir / "_transmutation.yml"
    yml_path.write_text(
        yaml.safe_dump(manifest, sort_keys=False, allow_unicode=True),
        encoding="utf-8",
    )
    return yml_path


def _collect_interface_tool_names(frontmatter: dict) -> list[str]:
    interface = frontmatter.get("artefacto", {}).get("interfaz", {})
    tools = interface.get("tools") or []
    names = []
    for item in tools:
        if isinstance(item, dict):
            name = item.get("name")
        elif isinstance(item, str):
            name = item
        else:
            name = None
        if isinstance(name, str) and name and name not in names:
            names.append(name)
    return names or ["Read"]


def _project_claude_code_tools(frontmatter: dict) -> list[str]:
    semantic_tools = _collect_interface_tool_names(frontmatter)
    projected = []
    mapping = {
        "catalog_resolve": "Read",
        "kb_route": "Grep",
    }
    for semantic in semantic_tools:
        runtime_tool = mapping.get(semantic)
        if runtime_tool and runtime_tool not in projected:
            projected.append(runtime_tool)
    for default_tool in ("Read", "Grep", "Glob"):
        if default_tool not in projected:
            projected.append(default_tool)
    return projected


def _emit_claude_code_bundle(
    target_dir: Path,
    name: str,
    frontmatter: dict,
    body: str,
    transmutation_path: Path,
) -> Path:
    transmutation_payload = yaml.safe_load(transmutation_path.read_text(encoding="utf-8")) or {}
    transmutation = transmutation_payload.get("transmutation", {})
    runtime_ext = (
        frontmatter.get("artefacto", {})
        .get("contexto", {})
        .get("runtime_extensions", {})
        .get("claude_code", {})
    )
    bundle_frontmatter = {
        "name": name,
        "description": frontmatter.get("descripcion", name),
        "tools": _project_claude_code_tools(frontmatter),
        "model": runtime_ext.get("model", "opus"),
        "color": runtime_ext.get("color", "gray"),
        "max_turns": runtime_ext.get("max_turns", 12),
    }
    knowledge_contract = transmutation.get("knowledge_contract", {})
    knowledge_lines = [
        "## Knowledge Contract",
        "",
    ]
    for urn in knowledge_contract.get("allowed_urns", []):
        path = (knowledge_contract.get("resolved_paths") or {}).get(urn)
        if path:
            knowledge_lines.append(f"- `{urn}` -> `{path}`")
        else:
            knowledge_lines.append(f"- `{urn}` -> `(unresolved)`")
    if knowledge_contract.get("routes"):
        knowledge_lines.extend(["", "### KB Routes", ""])
        for route_name, item in sorted((knowledge_contract.get("routes") or {}).items()):
            route_path = item.get("path")
            if route_path:
                knowledge_lines.append(f"- `{route_name}` -> `{item['urn']}` -> `{route_path}`")
            else:
                knowledge_lines.append(f"- `{route_name}` -> `{item['urn']}` -> `(unresolved)`")
    metadata_lines = [
        "## Provenance",
        "",
        f"- Source URN: `{transmutation.get('source_urn', '')}`",
        f"- Source Hash: `{transmutation.get('source_hash', '')}`",
        f"- Transmuted At: `{transmutation.get('timestamp', '')}`",
        "",
        *knowledge_lines,
        "",
        "## Instructions",
        "",
        body.strip(),
        "",
    ]
    bundle_path = target_dir / f"{name}.md"
    bundle_path.write_text(
        "---\n"
        + yaml.safe_dump(bundle_frontmatter, sort_keys=False, allow_unicode=True).strip()
        + "\n---\n\n"
        + "\n".join(metadata_lines),
        encoding="utf-8",
    )
    return bundle_path


# ---------------------------------------------------------------------------
# Proyeccion directa a agentskills.io (byte-identical, sin LLM)
# ---------------------------------------------------------------------------

# autoria-spec §5.5 — mapeo canonico de renames es → en
AGENTSKILLS_FIELD_RENAMES = {
    "nombre": "name",
    "descripcion": "description",
}
AGENTSKILLS_SUBDIR_RENAMES = {
    "referencias": "references",
    "recursos": "assets",
    # scripts se preserva (mismo nombre en ambos regimenes)
}
AGENTSKILLS_SECTION_RENAMES = {
    "Recursos": "Resources",
    "Referencias": "References",
    # Scripts se preserva
}


def _resolve_skill_path(skill_ref: str) -> Path:
    """Resuelve ref 'ns/nombre' o 'nombre' a SKILL.md productivo."""
    parts = skill_ref.strip().split("/")
    if len(parts) == 2:
        ns, name = parts
        skill_md = SKILLS_ROOT / ns / name / "SKILL.md"
    elif len(parts) == 1:
        name = parts[0]
        skill_md = SKILLS_ROOT / name / "SKILL.md"
    else:
        raise ValueError(f"Skill ref must be 'ns/nombre' or 'nombre', got: {skill_ref}")
    if not skill_md.is_file():
        raise ValueError(f"SKILL.md not found: {skill_md}")
    return skill_md


def _build_agentskills_target_path(skill_md_path: Path) -> Path:
    """Output vive en {skill_dir}/_BUILD/agentskills/."""
    return skill_md_path.parent / "_BUILD" / "agentskills"


def _project_skill_frontmatter(frontmatter: dict) -> dict:
    """Proyecta frontmatter KORA (es) a agentskills.io (en). autoria-spec §5.5.

    - Remueve extensions.kora (overlay KORA no se exporta).
    - Remueve _manifest (no es parte del estandar externo).
    - Renombra nombre->name, descripcion->description.
    - Preserva allowed-tools si existe.
    """
    out = {}
    name = frontmatter.get("nombre") or frontmatter.get("name")
    description = frontmatter.get("descripcion") or frontmatter.get("description")
    if name:
        out["name"] = name
    if description:
        out["description"] = description
    allowed_tools = frontmatter.get("allowed-tools")
    if allowed_tools is not None:
        out["allowed-tools"] = allowed_tools
    return out


def _project_skill_body(body: str) -> str:
    """Proyecta body markdown: renombra secciones KORA a estandar externo."""
    import re
    for es_section, en_section in AGENTSKILLS_SECTION_RENAMES.items():
        # Solo renombra headings exactos ## o ### para evitar reemplazos en prosa
        body = re.sub(
            rf"^(#{{2,3}}\s+){re.escape(es_section)}(\s*)$",
            rf"\1{en_section}\2",
            body,
            flags=re.MULTILINE,
        )
    return body


def _transmute_skill_to_agentskills(skill_md_path: Path, dry_run: bool = False) -> tuple[Path, dict]:
    """Proyecta un SKILL.md + subdirs a agentskills.io byte-identical.

    Retorna (target_dir, summary_dict).
    """
    import yaml

    frontmatter, body = load_markdown_parts(skill_md_path)
    if not isinstance(frontmatter, dict):
        raise ValueError(f"No YAML frontmatter in {skill_md_path}")

    # Validar que es habilidad
    forma = (
        (frontmatter.get("extensions") or {}).get("kora", {}).get("atlas", {}).get("forma_material")
    )
    if forma != "habilidad":
        raise ValueError(
            f"agentskills target solo aplica a forma_material=habilidad, "
            f"pero {skill_md_path.relative_to(KORA_ROOT)} es '{forma}'"
        )

    # Proyectar vector (verifica dominio)
    vector = _get_harness_vector(frontmatter)
    projected, detail = _project_vector(vector, "agentskills")

    target_dir = _build_agentskills_target_path(skill_md_path)
    source_skill_dir = skill_md_path.parent

    projected_fm = _project_skill_frontmatter(frontmatter)
    projected_body = _project_skill_body(body)

    summary = {
        "source": str(skill_md_path.relative_to(KORA_ROOT)),
        "target_dir": str(target_dir.relative_to(KORA_ROOT)),
        "projected_vector": projected,
        "loss_by_axis": {ax: d.get("loss") for ax, d in detail.items() if d.get("loss")},
        "subdirs_renamed": {},
        "body_sections_renamed": list(AGENTSKILLS_SECTION_RENAMES.keys()),
    }

    if dry_run:
        return target_dir, summary

    # Materializar output
    target_dir.mkdir(parents=True, exist_ok=True)
    out_skill_md = target_dir / "SKILL.md"
    content = "---\n" + yaml.safe_dump(projected_fm, sort_keys=False, allow_unicode=True) + "---\n" + projected_body
    out_skill_md.write_text(content, encoding="utf-8")

    # Copiar subdirs con renames
    for entry in source_skill_dir.iterdir():
        if not entry.is_dir() or entry.name.startswith((".", "_")):
            continue
        src_name = entry.name
        dst_name = AGENTSKILLS_SUBDIR_RENAMES.get(src_name, src_name)
        if dst_name != src_name:
            summary["subdirs_renamed"][src_name] = dst_name
        dst_dir = target_dir / dst_name
        dst_dir.mkdir(parents=True, exist_ok=True)
        for item in entry.rglob("*"):
            if item.is_file():
                rel = item.relative_to(entry)
                dst_file = dst_dir / rel
                dst_file.parent.mkdir(parents=True, exist_ok=True)
                dst_file.write_bytes(item.read_bytes())

    # Emit _transmutation.yml para skills
    source_hash = _sha256(skill_md_path)
    manifest = {
        "transmutation": {
            "source_urn": frontmatter.get("_manifest", {}).get("urn", ""),
            "source_version": frontmatter.get("version", "0.0.0"),
            "source_path": str(skill_md_path.relative_to(KORA_ROOT)),
            "source_hash": source_hash,
            "target": "agentskills",
            "functor": "T_agentskills_v1.0",
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "source_vector": {
                "pi": vector.get("pi"), "mu": vector.get("mu"), "xi": vector.get("xi"),
                "lambda": vector.get("lambda"), "phi": vector.get("phi"), "sigma": vector.get("sigma"),
            },
            "structural_preservation": {
                "composition": "preserved",
                "identity": "preserved",
                "semantic_body": "preserved",
            },
            "projections": detail,
            "field_renames": AGENTSKILLS_FIELD_RENAMES,
            "subdir_renames": summary["subdirs_renamed"],
            "section_renames": AGENTSKILLS_SECTION_RENAMES,
            "bisimulation_claim": "byte-identical-modulo-renames",
            "references": {
                "autoria_spec": "urn:kora:kb:autoria-spec",
                "transmutation_spec": "urn:kora:kb:transmutation-spec",
            },
        }
    }
    yml_path = target_dir / "_transmutation.yml"
    yml_path.write_text(yaml.safe_dump(manifest, sort_keys=False, allow_unicode=True), encoding="utf-8")

    return target_dir, summary


# ---------------------------------------------------------------------------
# Round-trip verification: T_target ∘ Lift_target ≈ id
# ---------------------------------------------------------------------------

def _collect_comparable_projection(skill_md_path: Path):
    """Extrae el conjunto minimo comparable de un SKILL.md KORA.

    Retorna dict con claves que SOBREVIVEN al round-trip a agentskills:
    {name, description, body_semantic, subdirs_files_hash}.
    """
    import hashlib
    fm, body = load_markdown_parts(skill_md_path)
    name = (fm or {}).get("nombre") or (fm or {}).get("name") or ""
    desc = (fm or {}).get("descripcion") or (fm or {}).get("description") or ""

    # Body semantico: texto sin headings (que se renombran)
    import re
    body_no_headings = re.sub(r"^#{1,6}\s.*$", "", body, flags=re.MULTILINE).strip()
    body_hash = hashlib.sha256(body_no_headings.encode("utf-8")).hexdigest()

    # Hash de contenido de subdirs (scripts/referencias/recursos en KORA;
    # scripts/references/assets en agentskills — los archivos son los mismos).
    skill_dir = skill_md_path.parent
    file_hashes = {}
    KORA_TO_AGENTSKILLS = {"referencias": "references", "recursos": "assets"}
    AGENTSKILLS_TO_KORA = {v: k for k, v in KORA_TO_AGENTSKILLS.items()}
    for sub in ("scripts", "referencias", "recursos", "references", "assets"):
        sub_dir = skill_dir / sub
        if not sub_dir.is_dir():
            continue
        # Clave canonica en espanol para comparacion cross-regimen
        canonical = AGENTSKILLS_TO_KORA.get(sub, sub)
        for f in sorted(sub_dir.rglob("*")):
            if f.is_file():
                rel = f.relative_to(sub_dir)
                key = f"{canonical}/{rel}"
                file_hashes[key] = hashlib.sha256(f.read_bytes()).hexdigest()

    return {
        "name": name,
        "description": desc,
        "body_semantic_hash": body_hash,
        "file_hashes": file_hashes,
    }


def cmd_roundtrip_check(agent_ref: str, target: str = "agentskills"):
    """Verifica la dualidad T_target ∘ Lift_target ≈ id para una habilidad.

    Para target=agentskills, la proyeccion es byte-identical modulo renames;
    el round-trip se valida comparando (name, description, body_semantic, files)
    entre la fuente KORA y el output proyectado (que es lo que un runtime
    foraneo veria).

    Para otros targets, el round-trip requiere Lift_R dedicado; v1.0 solo
    cubre agentskills.
    """
    if target != "agentskills":
        print(f"round-trip-check v1.0 solo cubre target=agentskills; {target} aun no tiene Lift dedicado")
        raise SystemExit(2)

    skill_md = _resolve_skill_path(agent_ref)
    print(f"=== Round-trip check: {agent_ref} ↔ {target} ===\n")

    # Proyecta
    target_dir, _summary = _transmute_skill_to_agentskills(skill_md, dry_run=False)
    projected_skill_md = target_dir / "SKILL.md"
    if not projected_skill_md.exists():
        print(f"ERROR: proyeccion no produjo {projected_skill_md}")
        raise SystemExit(1)

    # Recolecta fingerprints comparables
    source = _collect_comparable_projection(skill_md)
    proj = _collect_comparable_projection(projected_skill_md)

    diffs = []
    if source["name"] != proj["name"]:
        diffs.append(f"name: KORA='{source['name']}' vs agentskills='{proj['name']}'")
    if source["description"] != proj["description"]:
        diffs.append(f"description: KORA='{source['description'][:60]}...' vs agentskills='{proj['description'][:60]}...'")
    if source["body_semantic_hash"] != proj["body_semantic_hash"]:
        diffs.append("body semantico (sin headings) difiere — proyeccion no preserva contenido")
    # File hashes: deben coincidir cuando se normaliza a clave canonica es
    source_files = source["file_hashes"]
    proj_files = proj["file_hashes"]
    only_source = set(source_files) - set(proj_files)
    only_proj = set(proj_files) - set(source_files)
    mismatched = {k for k in set(source_files) & set(proj_files) if source_files[k] != proj_files[k]}
    if only_source:
        diffs.append(f"archivos solo en KORA: {sorted(only_source)[:5]}")
    if only_proj:
        diffs.append(f"archivos solo en agentskills: {sorted(only_proj)[:5]}")
    if mismatched:
        diffs.append(f"archivos con contenido distinto: {sorted(mismatched)[:5]}")

    if diffs:
        print("ROUND-TRIP FALLA — la proyeccion no es byte-identical:")
        for d in diffs:
            print(f"  - {d}")
        raise SystemExit(1)
    else:
        print("ROUND-TRIP OK — T_agentskills preserva name, description, body semantico y contenidos.")
        print(f"  Source:    {skill_md.relative_to(KORA_ROOT)}")
        print(f"  Projected: {projected_skill_md.relative_to(KORA_ROOT)}")


# ---------------------------------------------------------------------------
# CLI commands
# ---------------------------------------------------------------------------

def cmd_transmute(target: str, agent: str, dry_run: bool = False):
    """Transmuta un artefacto IR al runtime target.

    Para target=agentskills, el artefacto DEBE ser una habilidad productiva
    (SKILL.md en artifacts/skills/{ns}/{name}/ con forma_material: habilidad). La
    proyeccion es byte-identical (sin LLM) segun autoria-spec §5.5.

    Para otros targets (claude-code, codex, gemini, mastra, openclaw), el artefacto
    es un AGENT.md y la compilacion final requiere un adapter skill o LLM.
    """
    if target not in SUPPORTED_TARGETS:
        raise ValueError(f"Unknown target: {target}. Supported: {SUPPORTED_TARGETS}")

    # Target agentskills: proyeccion de habilidad
    if target == "agentskills":
        skill_md_path = _resolve_skill_path(agent)
        print(f"=== KORA Transmutation: {agent} -> agentskills.io ===\n")
        print(f"  Source: {skill_md_path.relative_to(KORA_ROOT)}")
        if dry_run:
            target_dir, summary = _transmute_skill_to_agentskills(skill_md_path, dry_run=True)
            print(f"  [dry-run] Would emit: {target_dir.relative_to(KORA_ROOT)}/")
            print(f"  [dry-run] Projected vector: {summary['projected_vector']}")
            return
        target_dir, summary = _transmute_skill_to_agentskills(skill_md_path, dry_run=False)
        print(f"  Output: {target_dir.relative_to(KORA_ROOT)}/")
        if summary["loss_by_axis"]:
            print(f"  Perdidas declaradas:")
            for ax, loss in summary["loss_by_axis"].items():
                if loss:
                    print(f"    - {ax}: {loss}")
        else:
            print(f"  Perdidas declaradas: ninguna")
        if summary["subdirs_renamed"]:
            print(f"  Subdirs renombrados:")
            for src, dst in summary["subdirs_renamed"].items():
                print(f"    {src}/ -> {dst}/")
        print(f"\n  Proyeccion byte-identical completada.")
        return

    agent_md_path = _resolve_agent_path(agent)
    ns, name = agent.strip().split("/")

    print(f"=== KORA Transmutation: {agent} → {target} ===\n")
    print(f"  Source: {agent_md_path.relative_to(KORA_ROOT)}")

    # Parse
    frontmatter, body = load_markdown_parts(agent_md_path)
    if not isinstance(frontmatter, dict):
        raise ValueError(f"No YAML frontmatter in {agent_md_path}")
    version = frontmatter.get("version", "0.0.0")
    print(f"  Version: {version}")

    # Vector IR
    vector = _get_harness_vector(frontmatter)
    print(f"  Vector IR: Π={vector['pi']} Μ={vector['mu']} Ξ={vector['xi']} "
          f"Λ={vector['lambda']} Φ={vector['phi']} Σ={vector['sigma']}")

    # Proyeccion
    projected, detail = _project_vector(vector, target)
    print(f"  Proyectado: Π={projected.get('pi')} Μ={projected.get('mu')} "
          f"Ξ={projected.get('xi')} Λ={projected.get('lambda')} "
          f"Φ={projected.get('phi')} Σ={projected.get('sigma')}")

    # Pérdidas
    losses = [(ax, d.get("loss")) for ax, d in detail.items() if d.get("loss")]
    if losses:
        print("  Perdidas declaradas:")
        for ax, loss in losses:
            print(f"    - {ax}: {loss}")
    else:
        print("  Perdidas declaradas: ninguna (fidelity full en todos los ejes)")

    # Hash
    source_hash = _sha256(agent_md_path)
    print(f"  Hash: {source_hash[:20]}...")

    # Target dir
    target_dir = _build_target_path(ns, name, target)
    print(f"  Output: {target_dir.relative_to(KORA_ROOT)}/")

    # Adapter
    adapter = _resolve_adapter_skill(target)
    if adapter:
        print(f"  Adapter: {adapter.relative_to(KORA_ROOT)}")
    else:
        print(f"  Adapter: ninguno — usar LLM generico con {target}-runtime-extension")

    if dry_run:
        print(f"\n  [dry-run] Would create: {target_dir}/")
        print(f"  [dry-run] Would emit: {target_dir}/_transmutation.yml")
        if target == "claude-code":
            print(f"  [dry-run] Would emit bundle: {target_dir}/{name}.md")
        return

    # Crear y emitir
    target_dir.mkdir(parents=True, exist_ok=True)
    yml_path = _emit_transmutation_yml(
        target_dir, agent_md_path, target, ns, name, version,
        source_hash, frontmatter, vector, projected, detail
    )
    print(f"  Manifest: {yml_path.relative_to(KORA_ROOT)}")

    bundle_path = None
    if target == "claude-code":
        bundle_path = _emit_claude_code_bundle(target_dir, name, frontmatter, body, yml_path)
        print(f"  Bundle: {bundle_path.relative_to(KORA_ROOT)}")

    print(f"\n  Transmutacion preparada.")
    print(f"  Proximo paso: compilar AGENT.md → artefactos {target}")
    print(f"  (el adapter skill o un LLM lee AGENT.md + _transmutation.yml y produce el output)")


# ---------------------------------------------------------------------------
# Ingesta inversa (Lift_R)
# ---------------------------------------------------------------------------

DEFAULT_VECTORS_BY_FROM = {
    "claude-code": {  # subagent single-file
        "pi": 2, "mu": 1, "xi": 2, "lambda": 0, "phi": 1,
        "sigma": [1, 1, 2, 1, 0],
    },
    "codex": {  # skill estandar
        "pi": 2, "mu": 0, "xi": 1, "lambda": 0, "phi": 1,
        "sigma": [1, 1, 2, 1, 0],
    },
    "gemini": {  # skill
        "pi": 2, "mu": 0, "xi": 1, "lambda": 0, "phi": 1,
        "sigma": [1, 1, 2, 1, 0],
    },
    "openclaw": {  # workspace agente
        "pi": 2, "mu": 3, "xi": 3, "lambda": 1, "phi": 2,
        "sigma": [2, 2, 2, 2, 1],
    },
}


def _lift_claude_code_subagent(file_path: Path, namespace: str = "kora"):
    """Eleva un subagente Claude Code single-file a workspace KORA IR."""
    frontmatter, body = load_markdown_parts(file_path)
    if not isinstance(frontmatter, dict):
        raise ValueError(f"No YAML frontmatter in {file_path}")

    name = frontmatter.get("name", file_path.stem)
    description = frontmatter.get("description", "")
    tools = frontmatter.get("tools", "")
    model = frontmatter.get("model", "sonnet")
    memory = frontmatter.get("memory", None)
    max_turns = frontmatter.get("maxTurns", frontmatter.get("max_turns", None))
    color = frontmatter.get("color", None)
    effort = frontmatter.get("effort", None)

    # Derivar vector heuristicamente
    vector = dict(DEFAULT_VECTORS_BY_FROM["claude-code"])
    if memory == "user":
        vector["mu"] = 2  # persistente cross-session
        vector["phi"] = 2  # collaborative aligned con user
    elif memory is None:
        vector["mu"] = 1  # scratchpad Task-scope
    if max_turns and isinstance(max_turns, int) and max_turns >= 10:
        vector["pi"] = 2  # plan ramificado para multi-turn largo

    # Construir AGENT.md v2 en _FRAGUA/INBOX/
    fragua_path = AGENTS_ROOT / "_FRAGUA" / "INBOX" / name / "AGENT.md"
    fragua_path.parent.mkdir(parents=True, exist_ok=True)

    new_frontmatter = {
        "_manifest": {
            "urn": f"urn:{namespace}:agent:{name}",
            "provenance": {
                "created_by": "kora-ingest",
                "created_at": datetime.now().strftime("%Y-%m-%d"),
                "source": str(file_path),
            },
        },
        "version": "1.0.0",
        "name": name,
        "status": "draft",
        "tags": ["ingested", "claude-code", namespace],
        "lang": "es",
        "extensions": {
            "kora": {
                "harness_vector": vector,
                "presentation": "state-primary",
                "atlas": {
                    "harness_name": "persona" if vector["mu"] >= 2 else "delegado",
                    "form": "agent-proper" if vector["mu"] >= 2 else "subagent",
                    "hcai_metaphor": "control-center" if vector["phi"] >= 2 else "supertool",
                },
                "ingested_from": "claude-code",
            },
            "claude_code": {
                "model": model,
                "tools": tools if isinstance(tools, list) else (tools.split(",") if tools else []),
                "memory": memory,
                "max_turns": max_turns,
                "color": color,
                "effort": effort,
            },
        },
        "agent": {
            "profile": {
                "description": description[:200] if len(description) > 200 else description,
                "domain": [namespace],
                "narrative": description,
            },
            "plan": {
                "initial_state": "S-START",
                "terminal_state": "S-END",
                "states": [
                    {"id": "S-START", "act": "Entry state derived from ingestion. Review body for FSM."},
                    {"id": "S-END", "act": "Terminal.", "transitions": "terminal"},
                ],
            },
            "interface": {"tools": [], "permissions": {"allow": []}},
            "context": {
                "memory_config": {"mode": "persistent" if memory == "user" else "session"},
            },
            "invariants": {
                "ethical_commitments": {
                    "safety_norm": "TODO — revisar tras ingestion",
                    "fairness": "TODO",
                    "transparency": "TODO",
                    "accountability": "TODO",
                    "sustainability": "TODO",
                },
            },
        },
    }

    new_body = f"# {name}\n\n(Ingested from Claude Code subagent — body original preservado abajo)\n\n---\n\n{body}"

    dump_yaml_frontmatter_and_body(fragua_path, new_frontmatter, new_body)
    return fragua_path


def _lift_codex_skill(file_path: Path):
    """Eleva un skill Codex a artifacts/skills/_TALLER/INBOX/."""
    frontmatter, body = load_markdown_parts(file_path)
    if not isinstance(frontmatter, dict):
        raise ValueError(f"No YAML frontmatter in {file_path}")

    name = frontmatter.get("name", file_path.stem)
    description = frontmatter.get("description", "")

    vector = dict(DEFAULT_VECTORS_BY_FROM["codex"])

    taller_path = SKILLS_ROOT / "_TALLER" / "INBOX" / name / "SKILL.md"
    taller_path.parent.mkdir(parents=True, exist_ok=True)

    new_frontmatter = {
        "_manifest": {
            "urn": f"urn:kora:skill:{name}:1.0.0",
            "type": "lazy_load_endofunctor",
        },
        "name": name,
        "description": description,
        "allowed-tools": frontmatter.get("allowed-tools", "Read"),
        "extensions": {
            "kora": {
                "harness_vector": vector,
                "presentation": "state-primary",
                "skill_freedom": "medium",
                "atlas": {
                    "harness_name": "disciplina" if vector["pi"] >= 2 else "utilidad",
                    "form": "skill-standard",
                    "hcai_metaphor": "supertool",
                },
                "ingested_from": "codex",
                "lifecycle": {
                    "status": "draft",
                    "created": datetime.now().strftime("%Y-%m-%d"),
                },
            },
        },
    }

    dump_yaml_frontmatter_and_body(taller_path, new_frontmatter, body)

    # Copiar scripts/references/assets si existen (cross-runtime portable)
    src_dir = file_path.parent
    for subdir in ("scripts", "references", "assets"):
        src_sub = src_dir / subdir
        if src_sub.is_dir():
            dst_sub = taller_path.parent / subdir
            dst_sub.mkdir(parents=True, exist_ok=True)
            for item in src_sub.iterdir():
                if item.is_file():
                    (dst_sub / item.name).write_bytes(item.read_bytes())

    return taller_path


def _lift_openclaw_workspace(workspace_dir: Path):
    """Eleva un workspace OpenClaw completo a artifacts/agents/_FRAGUA/INBOX/."""
    agent_id = workspace_dir.name
    vector = dict(DEFAULT_VECTORS_BY_FROM["openclaw"])

    # Leer archivos canonicos si existen
    agents_md = workspace_dir / "AGENTS.md"
    soul_md = workspace_dir / "SOUL.md"
    tools_md = workspace_dir / "TOOLS.md"

    description = ""
    if soul_md.exists():
        description = soul_md.read_text(encoding="utf-8")[:200]

    fragua_path = AGENTS_ROOT / "_FRAGUA" / "INBOX" / agent_id / "AGENT.md"
    fragua_path.parent.mkdir(parents=True, exist_ok=True)

    new_frontmatter = {
        "_manifest": {
            "urn": f"urn:kora:agent:{agent_id}",
            "provenance": {
                "created_by": "kora-ingest",
                "created_at": datetime.now().strftime("%Y-%m-%d"),
                "source": str(workspace_dir),
            },
        },
        "version": "1.0.0",
        "name": agent_id,
        "status": "draft",
        "tags": ["ingested", "openclaw"],
        "lang": "es",
        "extensions": {
            "kora": {
                "harness_vector": vector,
                "presentation": "state-primary",
                "atlas": {
                    "harness_name": "servicio",
                    "form": "platform-agent",
                    "hcai_metaphor": "control-center",
                },
                "ingested_from": "openclaw",
            },
            "openclaw": {
                "agent_id": agent_id,
                "workspace_path": f"workspaces/{agent_id}/",
            },
        },
        "agent": {
            "profile": {
                "description": description or f"OpenClaw agent {agent_id}",
                "domain": ["openclaw-fleet"],
            },
            "plan": {
                "initial_state": "S-START",
                "terminal_state": "S-END",
                "states": [
                    {"id": "S-START", "act": "Entry."},
                    {"id": "S-END", "act": "Terminal.", "transitions": "terminal"},
                ],
            },
            "interface": {"tools": [], "permissions": {"allow": []}},
            "context": {
                "memory_config": {"mode": "ambient", "storage": f"{workspace_dir}/memory/"},
            },
            "invariants": {
                "ethical_commitments": {
                    "safety_norm": "TODO — revisar tras ingestion",
                    "fairness": "TODO",
                    "transparency": "TODO",
                    "accountability": "TODO",
                    "sustainability": "TODO",
                },
            },
        },
    }

    new_body = f"# {agent_id}\n\n(Ingested from OpenClaw workspace — archivos originales referenciados en workspace_path)\n"
    dump_yaml_frontmatter_and_body(fragua_path, new_frontmatter, new_body)
    return fragua_path


def cmd_ingest(from_runtime: str, file: str = None, workspace: str = None,
               namespace: str = "kora", dry_run: bool = False):
    """Ingesta inversa Lift_R — eleva artefacto foraneo a KORA IR.

    Uso:
      kora ingest --from claude-code --file ~/.claude/agents/polymath.md
      kora ingest --from codex --file ~/.codex/skills/X/SKILL.md
      kora ingest --from gemini --file path/SKILL.md
      kora ingest --from openclaw --workspace ~/openclaw-fleet/workspaces/X
    """
    print(f"=== KORA Ingest: {from_runtime} → IR ===\n")

    if from_runtime == "claude-code":
        if not file:
            raise ValueError("--file required for claude-code ingest")
        file_path = Path(file).expanduser().resolve()
        if not file_path.is_file():
            raise ValueError(f"File not found: {file_path}")
        print(f"  Source: {file_path}")
        if dry_run:
            print(f"  [dry-run] Would lift to artifacts/agents/_FRAGUA/INBOX/{file_path.stem}/AGENT.md")
            return
        result = _lift_claude_code_subagent(file_path, namespace=namespace)
        print(f"  Lifted to: {result.relative_to(KORA_ROOT)}")

    elif from_runtime in ("codex", "gemini"):
        if not file:
            raise ValueError(f"--file required for {from_runtime} ingest")
        file_path = Path(file).expanduser().resolve()
        if not file_path.is_file():
            raise ValueError(f"File not found: {file_path}")
        print(f"  Source: {file_path}")
        if dry_run:
            print(f"  [dry-run] Would lift skill to artifacts/skills/_TALLER/INBOX/")
            return
        result = _lift_codex_skill(file_path)
        print(f"  Lifted to: {result.relative_to(KORA_ROOT)}")

    elif from_runtime == "openclaw":
        if not workspace:
            raise ValueError("--workspace required for openclaw ingest")
        ws_path = Path(workspace).expanduser().resolve()
        if not ws_path.is_dir():
            raise ValueError(f"Workspace not found: {ws_path}")
        print(f"  Source: {ws_path}")
        if dry_run:
            print(f"  [dry-run] Would lift workspace to artifacts/agents/_FRAGUA/INBOX/{ws_path.name}/")
            return
        result = _lift_openclaw_workspace(ws_path)
        print(f"  Lifted to: {result.relative_to(KORA_ROOT)}")

    else:
        raise ValueError(f"Unknown source runtime: {from_runtime}. "
                         f"Supported: claude-code, codex, gemini, openclaw")

    print(f"\n  Ingest preparado. El artefacto en staging requiere:")
    print(f"    1. Completar campos TODO en invariants/ethical_commitments.")
    print(f"    2. Ajustar harness_vector si heuristica fue imprecisa.")
    print(f"    3. Revisar plan FSM (auto-generado como stub).")
    print(f"    4. Promover con `kora promote` cuando este listo.")
