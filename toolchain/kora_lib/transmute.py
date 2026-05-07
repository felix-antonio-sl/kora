"""Transmutation orchestrator: proyecta KORA IR a un runtime target.

Implementa el functor T_R: KORA_IR → Runtime_R de transmutation-spec v1.2,
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

from .artifacts import load_markdown_parts, dump_yaml_frontmatter_and_body, load_yaml_safe
from .catalog import build_catalog_lookup, get_reference_entry, load_catalog
from .config import AGENTS_ROOT, KORA_ROOT, SKILLS_ROOT, TALLER_ROOT
from .lifecycle import is_deprecated_status, is_retired_status, read_declared_status


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
    "opencode": {
        "domain": {"pi": [0,1,2,3], "mu": [0,1,2], "xi": [0,1,2,3,4], "lambda": [0,1,2], "phi": [0,1,2,3], "sigma_max": [3,2,2,2,1]},
        "pi":      {0: (0, "full"), 1: (1, "full"), 2: (2, "full"), 3: (3, "partial", "fixed-points acotados por campo `steps` del agente")},
        "mu":      {0: (0, "full"), 1: (1, "full"), 2: (2, "partial", "sessions con jerarquia parent/child pero sin memory:user transparente"), 3: (None, "none", "OpenCode CLI/TUI sincrono, no daemon always-on")},
        "xi":      {0: (0, "full"), 1: (1, "full"), 2: (2, "full"), 3: (3, "partial", "subagent @mention + Task tool con permission gates"), 4: (3, "partial", "operad dinamica completa requiere wrapper aplicativo")},
        "lambda":  {0: (0, "full"), 1: (1, "full"), 2: (1, "partial", "ecosystem colapsa a organizacional"), 3: (None, "none", "society-in-the-loop no soportado")},
        "phi":     {0: (0, "full"), 1: (1, "full"), 2: (2, "full", "permission system con `ask` materializa HOTL granular"), 3: (2, "partial", "hybrid cognition completa requiere wrapper aplicativo"), 4: (None, "none", "co-evolutivo no soportado")},
    },
}

TARGET_ADAPTERS = {
    "claude-code": "transmute-claude-code",
    "openclaw": "transmute-openclaw",
    "codex": "transmute-codex",
    "gemini": "transmute-gemini",
    "mastra": "transmute-mastra",
    "opencode": "transmute-opencode",
    "agentskills": None,  # proyeccion directa sin LLM (byte-identical)
}

SUPPORTED_TARGETS = tuple(PRESERVATION_MATRIX.keys())

PRESENTACION_MAP = {
    "estado-primario": "estado-primario",
    "accion-primaria": "accion-primaria",
    "state-primary": "estado-primario",
    "action-primary": "accion-primaria",
}

TRACE_FIDELITY_BY_TARGET = {
    "claude-code": {
        "level": "media",
        "capture_mechanism": "hook SubagentStop + JSONL ~/.claude/projects/*/",
        "notes": "requiere captura operatoria estable para evidencia de tool calls",
    },
    "codex": {
        "level": "pendiente",
        "capture_mechanism": "por documentar en codex-runtime-extension",
        "notes": "no cerrar verificacion estricta de trazabilidad hasta completar runtime-extension",
    },
    "gemini": {
        "level": "pendiente",
        "capture_mechanism": "por documentar en gemini-runtime-extension",
        "notes": "no cerrar verificacion estricta de trazabilidad hasta completar runtime-extension",
    },
    "mastra": {
        "level": "pendiente",
        "capture_mechanism": "logs server-side por especificar",
        "notes": "no cerrar verificacion estricta de trazabilidad hasta completar runtime-extension",
    },
    "openclaw": {
        "level": "pendiente",
        "capture_mechanism": "journalctl --user + session jsonl por especificar",
        "notes": "no cerrar verificacion estricta de trazabilidad hasta completar runtime-extension",
    },
    "opencode": {
        "level": "pendiente",
        "capture_mechanism": "session id + child sessions navigation (parent/child)",
        "notes": "OpenCode mantiene jerarquia de sessions; mecanismo estable de exportacion para audit pendiente",
    },
    "agentskills": {
        "level": "heredada",
        "capture_mechanism": "meta-runtime; hereda del runtime que ejecuta el paquete",
        "notes": "agentskills no ejecuta por si mismo",
    },
}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _sha256(path: Path) -> str:
    """Return sha256:<hex> of file contents."""
    return "sha256:" + hashlib.sha256(path.read_bytes()).hexdigest()


def _resolve_agent_path(agent_ref: str) -> Path:
    from .workspaces import find_agent_workspace

    parts = agent_ref.strip().split("/")
    if len(parts) != 2:
        raise ValueError(f"Agent ref must be 'namespace/name', got: {agent_ref}")
    agent_dir = find_agent_workspace(agent_ref, include_staging=True)
    if agent_dir is None:
        ns, name = parts
        agent_dir = AGENTS_ROOT / ns / name
        raise ValueError(f"Agent directory not found: {agent_dir}")
    agent_md = agent_dir / "AGENT.md"
    if not agent_md.is_file():
        raise ValueError(f"AGENT.md not found: {agent_md}")
    return agent_md


def _build_target_path(agent_dir: Path, target: str) -> Path:
    """Output vive en {workspace}/_BUILD/{target}/ segun gobernanza §3.2 y runtime-spec-md."""
    return agent_dir / "_BUILD" / target


def _get_vector_ontologico(frontmatter: dict) -> dict:
    """Extrae el vector ontologico PMI × LFS del IR.

    Acepta ambos nombres por compatibilidad:
      - `vector_ontologico` (canonico en autoria-spec)
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


def _get_harness_vector(frontmatter: dict) -> dict:
    """Alias legacy para callers internos antiguos."""
    return _get_vector_ontologico(frontmatter)


def _get_presentacion(frontmatter: dict) -> str:
    """Extrae la presentacion canonica, aceptando el nombre legacy."""
    kora_ext = frontmatter.get("extensions", {}).get("kora", {})
    raw = kora_ext.get("presentacion") or kora_ext.get("presentation") or "estado-primario"
    return PRESENTACION_MAP.get(raw, raw)


def _trace_fidelity_for_target(target: str) -> dict:
    return dict(TRACE_FIDELITY_BY_TARGET.get(target, {
        "level": "pendiente",
        "capture_mechanism": "runtime no registrado",
        "notes": "declaracion faltante",
    }))


def _structural_preservation_record(target: str) -> dict:
    """Evidencia minima honesta: separar lo verificado de lo declarado."""
    return {
        "composition": {
            "status": "preserved",
            "evidence": "domain-check + preservation-matrix",
        },
        "identity": {
            "status": "preserved",
            "evidence": "source_urn/source_hash retained in manifest",
        },
        "xi_naturality": {
            "status": "declared",
            "evidence": f"requires runtime review for {target}",
        },
        "safety_closure": {
            "status": "declared",
            "evidence": "source IR must pass coalgebra/vector checks before strict runtime verification",
        },
        "kleisli_composition": {
            "status": "declared",
            "evidence": "risk/effect composition not fully mechanized in transmute",
        },
        "pi_monotonicity": {
            "status": "preserved",
            "evidence": "axis projection is <= source or equal",
        },
        "mu_monotonicity": {
            "status": "preserved",
            "evidence": "axis projection is <= source or equal",
        },
        "xi_monotonicity": {
            "status": "preserved",
            "evidence": "axis projection is <= source or equal",
        },
    }


def _validate_transmutation_manifest(manifest: dict) -> None:
    """Valida el manifiesto contra el schema publicado si jsonschema existe."""
    schema_path = KORA_ROOT / "serialization" / "schemas" / "kora-transmutation-schema.json"
    if not schema_path.is_file():
        raise ValueError(f"Missing transmutation schema: {schema_path.relative_to(KORA_ROOT)}")
    try:
        import jsonschema
    except ImportError as exc:
        raise ValueError("jsonschema is required to validate _transmutation.yml") from exc
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    jsonschema.Draft202012Validator(schema).validate(manifest)


def _write_transmutation_manifest(path: Path, manifest: dict) -> Path:
    _validate_transmutation_manifest(manifest)
    path.write_text(
        yaml.safe_dump(manifest, sort_keys=False, allow_unicode=True),
        encoding="utf-8",
    )
    return path


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


def _collect_openclaw_kora_repo_access(frontmatter: dict) -> dict:
    """Return the live KORA clone access contract for OpenClaw builds."""
    openclaw_ext = (frontmatter.get("extensions") or {}).get("openclaw") or {}
    return {
        "required": bool(openclaw_ext.get("kora_repo_required", True)),
        "host_env": openclaw_ext.get("kora_repo_env", "KORA_REPO"),
        "default_host_path": openclaw_ext.get("kora_repo_default", str(KORA_ROOT)),
        "container_mount": openclaw_ext.get("kora_repo_mount", "/" + "home/node/repos/kora"),
        "mode": openclaw_ext.get("knowledge_mount_mode", "ro"),
        "sync_strategy": openclaw_ext.get(
            "knowledge_mount_strategy", "bind_mount_live_kora_clone"
        ),
        "knowledge_root": "artifacts/knowledge",
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
    codex_skills_dir: Path | None = None,
    opencode_agents_dir: Path | None = None,
) -> dict:
    from .workspaces import iter_agent_workspaces

    claude_dir = Path(claude_agents_dir or Path.home() / ".claude" / "agents").expanduser()
    openclaw_dir = Path(openclaw_workspaces_dir or Path.home() / "openclaw-fleet" / "workspaces").expanduser()
    codex_dir = Path(codex_skills_dir or Path.home() / ".codex" / "skills").expanduser()
    opencode_dir = Path(opencode_agents_dir or Path.home() / ".config" / "opencode" / "agents").expanduser()

    agents = []
    summary = {"ok": 0, "stale": 0, "missing": 0, "unsupported": 0}

    def _hash_status(deployed_path: Path) -> dict:
        if not deployed_path.exists():
            return {"status": "missing", "path": str(deployed_path)}
        text = deployed_path.read_text(encoding="utf-8")
        deployed_hash = _extract_provenance_value(text, "Source Hash")
        return {
            "status": "ok" if deployed_hash == current_hash else "stale",
            "path": str(deployed_path),
            "source_hash": deployed_hash,
            "current_hash": current_hash,
        }

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
                status = _hash_status(claude_dir / f"{workspace_dir.name}.md")
            elif target == "codex":
                status = _hash_status(codex_dir / workspace_dir.name / "SKILL.md")
            elif target == "opencode":
                status = _hash_status(opencode_dir / f"{workspace_dir.name}.md")
            elif target == "openclaw":
                deployed_path = openclaw_dir / workspace_dir.name
                status = {"status": "missing" if not deployed_path.exists() else "unsupported", "path": str(deployed_path)}
            else:
                continue
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
    presentacion = _get_presentacion(frontmatter)
    knowledge_contract = _collect_knowledge_contract(frontmatter)

    manifest = {
        "transmutation": {
            "metadata": {
                "trace_fidelity": _trace_fidelity_for_target(target),
                "evidence_level": "mechanical-projection-plus-declared-laws",
                "schema": "serialization/schemas/kora-transmutation-schema.json",
            },
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
                "presentacion": presentacion,
            },

            # Preservacion estructural (obligatoria - transmutation-spec §3.2)
            "structural_preservation": _structural_preservation_record(target),

            # Proyeccion por eje
            "projections": projections_detail,

            # Claim de bisimulacion
            "bisimulation_claim": "equivalent-modulo-projections",
            "bisimulation_scope": f"observaciones soportadas por {target}",
            "bisimulation_evidence": "bounded-by-preservation-matrix",

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
    if target == "openclaw":
        manifest["transmutation"]["kora_repo_access"] = _collect_openclaw_kora_repo_access(
            frontmatter
        )

    yml_path = target_dir / "_transmutation.yml"
    return _write_transmutation_manifest(yml_path, manifest)


def _collect_interface_tool_names(frontmatter: dict) -> list[str]:
    interface = frontmatter.get("artefacto", {}).get("interfaz", {})
    tools = interface.get("herramientas") or interface.get("tools") or []
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


CLAUDE_CODE_NATIVE_TOOLS = {
    "Read", "Write", "Edit", "MultiEdit", "Bash", "Glob", "Grep",
    "WebFetch", "WebSearch", "Task", "TodoWrite", "NotebookEdit",
}


def _project_claude_code_tools(frontmatter: dict) -> list[str]:
    semantic_tools = _collect_interface_tool_names(frontmatter)
    projected = []
    semantic_to_native = {
        "catalog_resolve": "Read",
        "kb_route": "Grep",
    }
    for semantic in semantic_tools:
        if semantic in CLAUDE_CODE_NATIVE_TOOLS:
            if semantic not in projected:
                projected.append(semantic)
            continue
        runtime_tool = semantic_to_native.get(semantic)
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
    runtime_ext = (frontmatter.get("extensions") or {}).get("claude_code") or (
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
    for optional_key in ("memory", "effort", "permissionMode", "background", "isolation"):
        if optional_key in runtime_ext:
            bundle_frontmatter[optional_key] = runtime_ext[optional_key]
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


def _agent_knowledge_lines(transmutation: dict) -> list[str]:
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
    return knowledge_lines


def _agent_projection_lines(transmutation: dict) -> list[str]:
    source_vector = transmutation.get("source_vector") or {}
    projections = transmutation.get("projections") or {}
    lines = [
        "## Runtime Projection",
        "",
        f"- Target: `{transmutation.get('target', '')}`",
        f"- Functor: `{transmutation.get('functor', '')}`",
        f"- Source vector: `{source_vector}`",
    ]
    losses = []
    for axis, detail in projections.items():
        if isinstance(detail, dict) and detail.get("loss"):
            losses.append(f"{axis}: {detail['loss']}")
    if losses:
        lines.append(f"- Declared losses: `{'; '.join(losses)}`")
    else:
        lines.append("- Declared losses: `none`")
    return lines


def _agent_provenance_lines(transmutation: dict) -> list[str]:
    return [
        "## Provenance",
        "",
        f"- Source URN: `{transmutation.get('source_urn', '')}`",
        f"- Source Hash: `{transmutation.get('source_hash', '')}`",
        f"- Transmuted At: `{transmutation.get('timestamp', '')}`",
    ]


def _emit_codex_agent_bundle(
    target_dir: Path,
    name: str,
    frontmatter: dict,
    body: str,
    transmutation_path: Path,
) -> Path:
    """Emit a Codex skill bundle from an agent IR.

    Codex CLI does not load `~/.codex/agents/`; only skills under
    `~/.codex/skills/{name}/SKILL.md`. Personas projected to Codex are
    materialised as skills (skill-shape directory with SKILL.md +
    agents/openai.yaml). See codex-runtime-extension §2 — Codex does not
    support cross-session transparent personas; the projection flattens
    to session-resumable.
    """
    transmutation_payload = yaml.safe_load(transmutation_path.read_text(encoding="utf-8")) or {}
    transmutation = transmutation_payload.get("transmutation", {})
    description = frontmatter.get("descripcion", name)
    short_description = frontmatter.get("nombre") or name

    bundle_frontmatter = {
        "name": name,
        "description": description,
        "metadata": {"short-description": short_description},
        "runtime": "codex",
        "source_urn": transmutation.get("source_urn", ""),
    }

    bundle_dir = target_dir / name
    bundle_dir.mkdir(parents=True, exist_ok=True)

    content_lines = [
        *_agent_provenance_lines(transmutation),
        "",
        *_agent_projection_lines(transmutation),
        "",
        *_agent_knowledge_lines(transmutation),
        "",
        "## Instructions",
        "",
        body.strip(),
        "",
    ]
    bundle_path = bundle_dir / "SKILL.md"
    bundle_path.write_text(
        "---\n"
        + yaml.safe_dump(bundle_frontmatter, sort_keys=False, allow_unicode=True).strip()
        + "\n---\n\n"
        + "\n".join(content_lines),
        encoding="utf-8",
    )

    agents_dir = bundle_dir / "agents"
    agents_dir.mkdir(parents=True, exist_ok=True)
    openai_yaml = {
        "interface": {
            "display_name": short_description,
            "short_description": description.split(".")[0][:120] if description else short_description,
        }
    }
    (agents_dir / "openai.yaml").write_text(
        yaml.safe_dump(openai_yaml, sort_keys=False, allow_unicode=True),
        encoding="utf-8",
    )

    return bundle_path


def _opencode_agent_mode(frontmatter: dict) -> str:
    forma = (
        (frontmatter.get("extensions") or {})
        .get("kora", {})
        .get("atlas", {})
        .get("forma_material")
    )
    if forma == "subagente":
        return "subagent"
    return "primary"


def _emit_opencode_agent_bundle(
    target_dir: Path,
    name: str,
    frontmatter: dict,
    body: str,
    transmutation_path: Path,
) -> Path:
    transmutation_payload = yaml.safe_load(transmutation_path.read_text(encoding="utf-8")) or {}
    transmutation = transmutation_payload.get("transmutation", {})
    opencode_ext = (frontmatter.get("extensions") or {}).get("opencode") or {}
    bundle_frontmatter = {
        "name": name,
        "description": frontmatter.get("descripcion", name),
        "mode": opencode_ext.get("mode", _opencode_agent_mode(frontmatter)),
        "source_urn": transmutation.get("source_urn", ""),
        "permission": opencode_ext.get(
            "permission",
            {"bash": "ask", "edit": "ask", "webfetch": "deny", "external_directory": "deny"},
        ),
    }
    if opencode_ext.get("model"):
        bundle_frontmatter["model"] = opencode_ext["model"]

    content_lines = [
        *_agent_provenance_lines(transmutation),
        "",
        *_agent_projection_lines(transmutation),
        "",
        *_agent_knowledge_lines(transmutation),
        "",
        "## Instructions",
        "",
        body.strip(),
        "",
    ]
    bundle_dir = target_dir / "agents"
    bundle_dir.mkdir(parents=True, exist_ok=True)
    bundle_path = bundle_dir / f"{name}.md"
    bundle_path.write_text(
        "---\n"
        + yaml.safe_dump(bundle_frontmatter, sort_keys=False, allow_unicode=True).strip()
        + "\n---\n\n"
        + "\n".join(content_lines),
        encoding="utf-8",
    )
    return bundle_path


def _list_to_markdown(items) -> str:
    if not isinstance(items, list) or not items:
        return "- none"
    return "\n".join(f"- {item}" for item in items)


def _tool_names_from_items(items) -> list[str]:
    if not isinstance(items, list):
        return []
    names = []
    for item in items:
        if isinstance(item, str):
            name = item
        elif isinstance(item, dict):
            name = item.get("name") or item.get("nombre") or item.get("tool")
        else:
            name = None
        if isinstance(name, str) and name and name not in names:
            names.append(name)
    return names


def _stringify_markdown_value(value) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value
    if isinstance(value, (dict, list)):
        return yaml.safe_dump(value, sort_keys=False, allow_unicode=True).strip()
    return str(value)


def _emit_openclaw_agent_workspace(
    target_dir: Path,
    name: str,
    frontmatter: dict,
    body: str,
    transmutation_path: Path,
) -> list[Path]:
    transmutation_payload = yaml.safe_load(transmutation_path.read_text(encoding="utf-8")) or {}
    transmutation = transmutation_payload.get("transmutation", {})
    artefacto = frontmatter.get("artefacto") or {}
    perfil = artefacto.get("perfil") or {}
    plan = artefacto.get("plan") or {}
    interfaz = artefacto.get("interfaz") or {}
    contexto = artefacto.get("contexto") or {}
    composicion = artefacto.get("composicion") or {}
    invariantes = artefacto.get("invariantes") or {}
    openclaw_ext = (frontmatter.get("extensions") or {}).get("openclaw") or {}
    tool_names = _tool_names_from_items(interfaz.get("herramientas"))

    workspace_dir = target_dir / "workspace"
    config_dir = target_dir / "config"
    workspace_dir.mkdir(parents=True, exist_ok=True)
    config_dir.mkdir(parents=True, exist_ok=True)

    emitted: list[Path] = []

    agents_md = workspace_dir / "AGENTS.md"
    agents_md.write_text(
        "\n".join(
            [
                f"# {name}",
                "",
                *_agent_provenance_lines(transmutation),
                "",
                *_agent_projection_lines(transmutation),
                "",
                *_agent_knowledge_lines(transmutation),
                "",
                "## Plan",
                "",
                f"- Initial state: `{plan.get('estado_inicial', '')}`",
                f"- Terminal state: `{plan.get('estado_terminal', '')}`",
                "",
                "### States",
                "",
                _list_to_markdown(plan.get("estados")),
                "",
                "## Interface",
                "",
                f"- Tools: `{', '.join(tool_names)}`",
                f"- Permissions: {_stringify_markdown_value(interfaz.get('permisos'))}",
                "",
                "## Instructions",
                "",
                body.strip(),
                "",
            ]
        ),
        encoding="utf-8",
    )
    emitted.append(agents_md)

    soul_md = workspace_dir / "SOUL.md"
    identity = contexto.get("identity") or {}
    soul_md.write_text(
        "\n".join(
            [
                f"# {name} Soul",
                "",
                _stringify_markdown_value(perfil.get("descripcion") or frontmatter.get("descripcion", "")),
                "",
                "## Identity",
                "",
                f"- Paradigm: {_stringify_markdown_value(identity.get('paradigm'))}",
                f"- Tone: {_stringify_markdown_value(identity.get('tone'))}",
                "",
                "## Domain",
                "",
                _list_to_markdown(perfil.get("dominio")),
                "",
                "## Hard Rules",
                "",
                _list_to_markdown(invariantes.get("reglas_duras")),
                "",
            ]
        ),
        encoding="utf-8",
    )
    emitted.append(soul_md)

    identity_md = workspace_dir / "IDENTITY.md"
    atlas = ((frontmatter.get("extensions") or {}).get("kora") or {}).get("atlas") or {}
    identity_md.write_text(
        "\n".join(
            [
                f"# {name} Identity",
                "",
                f"- URN: `{transmutation.get('source_urn', '')}`",
                f"- Version: `{frontmatter.get('version', '')}`",
                f"- Status: `{frontmatter.get('status', '')}`",
                f"- Categorical harness: `{atlas.get('arnes_categorico', '')}`",
                f"- Material form: `{atlas.get('forma_material', '')}`",
                f"- Relational metaphor: `{atlas.get('metafora_relacional', '')}`",
                "",
            ]
        ),
        encoding="utf-8",
    )
    emitted.append(identity_md)

    user_md = workspace_dir / "USER.md"
    operator = contexto.get("operator") or {}
    user_md.write_text(
        "\n".join(
            [
                f"# {name} User Context",
                "",
                f"- Role: {_stringify_markdown_value(operator.get('role'))}",
                f"- Context: {_stringify_markdown_value(operator.get('context'))}",
                "",
            ]
        ),
        encoding="utf-8",
    )
    emitted.append(user_md)

    tools_md = workspace_dir / "TOOLS.md"
    protocols = interfaz.get("protocolos") or {}
    tools_md.write_text(
        "\n".join(
            [
                f"# {name} Tools",
                "",
                "## Allowed Tools",
                "",
                _list_to_markdown(tool_names),
                "",
                "## Permissions",
                "",
                _stringify_markdown_value(interfaz.get("permisos")),
                "",
                "## IO Protocol",
                "",
                f"- Input: {_stringify_markdown_value(protocols.get('entrada'))}",
                f"- Output: {_stringify_markdown_value(protocols.get('salida'))}",
                "",
            ]
        ),
        encoding="utf-8",
    )
    emitted.append(tools_md)

    boot_md = workspace_dir / "BOOT.md"
    boot_md.write_text(
        "\n".join(
            [
                f"# {name} Boot",
                "",
                f"Start in `{plan.get('estado_inicial', '')}`.",
                "",
                "## Triggers",
                "",
                _list_to_markdown(perfil.get("disparadores")),
                "",
                "## Expected Outputs",
                "",
                _list_to_markdown(perfil.get("salidas")),
                "",
            ]
        ),
        encoding="utf-8",
    )
    emitted.append(boot_md)

    memory_md = workspace_dir / "MEMORY.md"
    memory_md.write_text(
        "\n".join(
            [
                f"# {name} Memory",
                "",
                "This file is a declarative memory contract emitted from KORA IR.",
                "",
                "## Memory Config",
                "",
                yaml.safe_dump(contexto.get("memoria_config") or {}, sort_keys=False, allow_unicode=True).strip() or "{}",
                "",
                "## Risk Register",
                "",
                yaml.safe_dump(contexto.get("risk_register") or [], sort_keys=False, allow_unicode=True).strip() or "[]",
                "",
                "## Composition",
                "",
                yaml.safe_dump(composicion, sort_keys=False, allow_unicode=True).strip() or "{}",
                "",
            ]
        ),
        encoding="utf-8",
    )
    emitted.append(memory_md)

    config_path = config_dir / "openclaw.json5"
    config = {
        "agent": {
            "id": openclaw_ext.get("agent_id", name),
            "urn": transmutation.get("source_urn", ""),
            "workspace_path": f"workspaces/{name}/",
        },
        "runtime": {
            "bot_handler": openclaw_ext.get("bot_handler"),
            "acp_compliant": bool(openclaw_ext.get("acp_compliant", True)),
            "kora_repo_access": transmutation.get("kora_repo_access", {}),
        },
    }
    config_path.write_text(json.dumps(config, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    emitted.append(config_path)

    deploy_md = target_dir / "DEPLOY.md"
    deploy_md.write_text(
        "\n".join(
            [
                f"# Deploy {name} to OpenClaw",
                "",
                "Generated KORA build artifact. Runtime state, credentials, sessions, pairing stores and caches are not included.",
                "",
                "## Source",
                "",
                f"- Manifest: `{transmutation_path.relative_to(KORA_ROOT)}`",
                f"- Workspace: `{workspace_dir.relative_to(KORA_ROOT)}`",
                f"- Config: `{config_path.relative_to(KORA_ROOT)}`",
                "",
                "## Manual Sync",
                "",
                f"Copy `workspace/` contents into the target OpenClaw workspace for `{name}` and apply `config/openclaw.json5` through the gateway policy you use in production.",
                "",
            ]
        ),
        encoding="utf-8",
    )
    emitted.append(deploy_md)

    return emitted


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


def _skill_rebuild_requires_fresh_source(doc: dict) -> bool:
    rebuild = (
        doc.get("extensions", {})
        .get("kora", {})
        .get("rebuild", {})
        if isinstance(doc, dict)
        else {}
    )
    return (
        isinstance(rebuild, dict)
        and rebuild.get("required") is True
        and rebuild.get("current_is_source") is False
    )


def _assert_active_skill_source(skill_md: Path) -> None:
    doc, err = load_yaml_safe(skill_md)
    if err or not isinstance(doc, dict):
        raise ValueError(f"Invalid SKILL.md frontmatter: {skill_md}")
    status = read_declared_status(doc)
    if is_deprecated_status(status) or is_retired_status(status):
        raise ValueError(f"SKILL.md is not an active source ({status}): {skill_md}")
    if _skill_rebuild_requires_fresh_source(doc):
        raise ValueError(
            "SKILL.md requires fresh rebuild and cannot be used as transmutation source: "
            f"{skill_md}"
        )


def _resolve_skill_path_candidate(skill_ref: str) -> Path | None:
    candidate = Path(skill_ref).expanduser()
    if not candidate.exists():
        return None
    skill_md = candidate / "SKILL.md" if candidate.is_dir() else candidate
    if skill_md.name != "SKILL.md" or not skill_md.is_file():
        raise ValueError(f"Skill path must point to SKILL.md or its directory: {skill_ref}")
    _assert_active_skill_source(skill_md)
    return skill_md


def _find_staged_skill_path(ns: str | None, name: str) -> Path | None:
    if not TALLER_ROOT.exists():
        return None
    target_urn = f"urn:{ns}:artefacto:{name}" if ns else None
    candidates = []
    for skill_md in sorted(TALLER_ROOT.glob("**/SKILL.md")):
        if "_BUILD" in skill_md.parts:
            continue
        doc, err = load_yaml_safe(skill_md)
        if err or not isinstance(doc, dict):
            continue
        urn = doc.get("_manifest", {}).get("urn")
        if target_urn:
            if urn != target_urn:
                continue
        elif not isinstance(urn, str) or not urn.endswith(f":artefacto:{name}"):
            continue
        status = read_declared_status(doc)
        if (
            is_deprecated_status(status)
            or is_retired_status(status)
            or _skill_rebuild_requires_fresh_source(doc)
        ):
            continue
        rel = skill_md.parent.relative_to(SKILLS_ROOT).as_posix()
        direct_namespaced = bool(ns) and rel.endswith(f"/{ns}/{name}")
        direct_named = rel.endswith(f"/{name}")
        candidates.append((0 if direct_namespaced else 1 if direct_named else 2, len(rel), skill_md))
    if not candidates:
        return None
    return sorted(candidates, key=lambda item: (item[0], item[1], item[2].as_posix()))[0][2]


def _resolve_skill_path(skill_ref: str) -> Path:
    """Resuelve path, ref 'ns/nombre' o 'nombre' a SKILL.md activo."""
    path_candidate = _resolve_skill_path_candidate(skill_ref)
    if path_candidate is not None:
        return path_candidate

    parts = skill_ref.strip().split("/")
    if len(parts) == 2:
        ns, name = parts
        skill_md = SKILLS_ROOT / ns / name / "SKILL.md"
    elif len(parts) == 1:
        ns = None
        name = parts[0]
        skill_md = SKILLS_ROOT / name / "SKILL.md"
    else:
        raise ValueError(f"Skill ref must be 'ns/nombre' or 'nombre', got: {skill_ref}")
    if skill_md.is_file():
        _assert_active_skill_source(skill_md)
        return skill_md
    staged = _find_staged_skill_path(ns, name)
    if staged is not None:
        return staged
    raise ValueError(f"SKILL.md not found: {skill_md}")
    return skill_md


def _build_agentskills_target_path(skill_md_path: Path) -> Path:
    """Output vive en {skill_dir}/_BUILD/agentskills/."""
    return skill_md_path.parent / "_BUILD" / "agentskills"


def _build_claude_code_skill_target_path(skill_md_path: Path) -> Path:
    """Output vive en {skill_dir}/_BUILD/claude-code/."""
    return skill_md_path.parent / "_BUILD" / "claude-code"


def _build_codex_skill_target_path(skill_md_path: Path) -> Path:
    """Output vive en {skill_dir}/_BUILD/codex/."""
    return skill_md_path.parent / "_BUILD" / "codex"


def _build_opencode_skill_target_path(skill_md_path: Path) -> Path:
    """Output vive en {skill_dir}/_BUILD/opencode/."""
    return skill_md_path.parent / "_BUILD" / "opencode"


def _build_openclaw_skill_target_path(skill_md_path: Path) -> Path:
    """Output vive en {skill_dir}/_BUILD/openclaw/."""
    return skill_md_path.parent / "_BUILD" / "openclaw"


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


def _project_skill_frontmatter_to_claude_code(frontmatter: dict, skill_name: str) -> dict:
    """Project a KORA skill to Claude Code skill frontmatter.

    Official Claude Code skills use a SKILL.md file with lightweight frontmatter.
    The only fields we emit by default are the ones that map cleanly and are
    documented as stable: `name` and `description`.
    """
    description = frontmatter.get("descripcion") or frontmatter.get("description") or skill_name
    return {
        "name": skill_name,
        "description": description,
    }


def _project_skill_frontmatter_to_codex(frontmatter: dict, skill_name: str) -> dict:
    """Project a KORA skill to Codex skill frontmatter."""
    description = frontmatter.get("descripcion") or frontmatter.get("description") or skill_name
    return {
        "name": skill_name,
        "description": description,
    }


def _emit_claude_code_skill_bundle(
    target_dir: Path,
    skill_name: str,
    frontmatter: dict,
    body: str,
    transmutation_path: Path,
) -> Path:
    transmutation_payload = yaml.safe_load(transmutation_path.read_text(encoding="utf-8")) or {}
    transmutation = transmutation_payload.get("transmutation", {})
    bundle_dir = target_dir / skill_name
    bundle_dir.mkdir(parents=True, exist_ok=True)
    bundle_frontmatter = _project_skill_frontmatter_to_claude_code(frontmatter, skill_name)

    knowledge_contract = transmutation.get("knowledge_contract", {})
    knowledge_lines = []
    allowed_urns = knowledge_contract.get("allowed_urns") or []
    if allowed_urns:
        knowledge_lines.extend(["", "## Knowledge Contract", ""])
        for urn in allowed_urns:
            path = (knowledge_contract.get("resolved_paths") or {}).get(urn)
            if path:
                knowledge_lines.append(f"- `{urn}` -> `{path}`")
            else:
                knowledge_lines.append(f"- `{urn}` -> `(unresolved)`")
        routes = knowledge_contract.get("routes") or {}
        if routes:
            knowledge_lines.extend(["", "### KB Routes", ""])
            for route_name, item in sorted(routes.items()):
                route_path = item.get("path")
                if route_path:
                    knowledge_lines.append(f"- `{route_name}` -> `{item['urn']}` -> `{route_path}`")
                else:
                    knowledge_lines.append(f"- `{route_name}` -> `{item['urn']}` -> `(unresolved)`")

    content = "---\n"
    content += yaml.safe_dump(bundle_frontmatter, sort_keys=False, allow_unicode=True).strip()
    content += "\n---\n\n"
    content += body.rstrip()
    if knowledge_lines:
        content += "\n" + "\n".join(knowledge_lines)
    content += "\n"

    out_skill_md = bundle_dir / "SKILL.md"
    out_skill_md.write_text(content, encoding="utf-8")
    return out_skill_md


def _emit_codex_skill_bundle(
    target_dir: Path,
    skill_name: str,
    frontmatter: dict,
    body: str,
) -> Path:
    bundle_dir = target_dir / skill_name
    bundle_dir.mkdir(parents=True, exist_ok=True)
    bundle_frontmatter = _project_skill_frontmatter_to_codex(frontmatter, skill_name)

    content = "---\n"
    content += yaml.safe_dump(bundle_frontmatter, sort_keys=False, allow_unicode=True).strip()
    content += "\n---\n\n"
    content += body.rstrip()
    content += "\n"

    out_skill_md = bundle_dir / "SKILL.md"
    out_skill_md.write_text(content, encoding="utf-8")
    return out_skill_md


def _emit_opencode_skill_bundle(
    target_dir: Path,
    skill_name: str,
    frontmatter: dict,
    body: str,
) -> Path:
    bundle_dir = target_dir / skill_name
    bundle_dir.mkdir(parents=True, exist_ok=True)
    bundle_frontmatter = _project_skill_frontmatter(frontmatter)
    bundle_frontmatter["name"] = skill_name
    projected_body = _project_skill_body(body)

    content = "---\n"
    content += yaml.safe_dump(bundle_frontmatter, sort_keys=False, allow_unicode=True).strip()
    content += "\n---\n\n"
    content += projected_body.rstrip()
    content += "\n"

    out_skill_md = bundle_dir / "SKILL.md"
    out_skill_md.write_text(content, encoding="utf-8")
    return out_skill_md


def _emit_openclaw_skill_bundle(
    target_dir: Path,
    skill_name: str,
    frontmatter: dict,
    body: str,
) -> Path:
    bundle_dir = target_dir / "skills" / skill_name
    bundle_dir.mkdir(parents=True, exist_ok=True)
    bundle_frontmatter = _project_skill_frontmatter(frontmatter)
    bundle_frontmatter["name"] = skill_name
    projected_body = _project_skill_body(body)

    content = "---\n"
    content += yaml.safe_dump(bundle_frontmatter, sort_keys=False, allow_unicode=True).strip()
    content += "\n---\n\n"
    content += projected_body.rstrip()
    content += "\n"

    out_skill_md = bundle_dir / "SKILL.md"
    out_skill_md.write_text(content, encoding="utf-8")
    return out_skill_md


def _transmute_skill_to_claude_code(skill_md_path: Path, dry_run: bool = False) -> tuple[Path, dict]:
    """Project a KORA skill to Claude Code skill layout.

    Target layout follows Claude Code official skill docs:
    ~/.claude/skills/<skill-name>/SKILL.md
    represented here as:
    {skill_dir}/_BUILD/claude-code/<skill-name>/SKILL.md
    """
    frontmatter, body = load_markdown_parts(skill_md_path)
    if not isinstance(frontmatter, dict):
        raise ValueError(f"No YAML frontmatter in {skill_md_path}")

    forma = (
        (frontmatter.get("extensions") or {}).get("kora", {}).get("atlas", {}).get("forma_material")
    )
    if forma != "habilidad":
        raise ValueError(
            f"claude-code skill target solo aplica a forma_material=habilidad, "
            f"pero {skill_md_path.relative_to(KORA_ROOT)} es '{forma}'"
        )

    vector = _get_vector_ontologico(frontmatter)
    projected, detail = _project_vector(vector, "claude-code")
    target_dir = _build_claude_code_skill_target_path(skill_md_path)
    skill_name = skill_md_path.parent.name

    summary = {
        "source": str(skill_md_path.relative_to(KORA_ROOT)),
        "target_dir": str(target_dir.relative_to(KORA_ROOT)),
        "bundle_path": str((target_dir / skill_name / "SKILL.md").relative_to(KORA_ROOT)),
        "projected_vector": projected,
        "loss_by_axis": {ax: d.get("loss") for ax, d in detail.items() if d.get("loss")},
    }
    if dry_run:
        return target_dir, summary

    target_dir.mkdir(parents=True, exist_ok=True)
    source_hash = _sha256(skill_md_path)
    yml_path = _emit_transmutation_yml(
        target_dir,
        skill_md_path,
        "claude-code",
        skill_md_path.parent.parent.name,
        skill_name,
        frontmatter.get("version", "0.0.0"),
        source_hash,
        frontmatter,
        vector,
        projected,
        detail,
    )
    bundle_path = _emit_claude_code_skill_bundle(target_dir, skill_name, frontmatter, body, yml_path)

    # Copy supporting files following Claude skill layout.
    for entry in skill_md_path.parent.iterdir():
        if entry.name in {"SKILL.md", "_BUILD"} or entry.name.startswith("."):
            continue
        if entry.is_dir():
            dst_dir = bundle_path.parent / entry.name
            dst_dir.mkdir(parents=True, exist_ok=True)
            for item in entry.rglob("*"):
                if item.is_file():
                    rel = item.relative_to(entry)
                    dst_file = dst_dir / rel
                    dst_file.parent.mkdir(parents=True, exist_ok=True)
                    dst_file.write_bytes(item.read_bytes())
        elif entry.is_file():
            (bundle_path.parent / entry.name).write_bytes(entry.read_bytes())

    return target_dir, summary


def _transmute_skill_to_codex(skill_md_path: Path, dry_run: bool = False) -> tuple[Path, dict]:
    """Project a KORA skill to Codex skill layout.

    Target layout follows Codex skill conventions:
    ~/.codex/skills/<skill-name>/SKILL.md
    represented here as:
    {skill_dir}/_BUILD/codex/<skill-name>/SKILL.md
    """
    frontmatter, body = load_markdown_parts(skill_md_path)
    if not isinstance(frontmatter, dict):
        raise ValueError(f"No YAML frontmatter in {skill_md_path}")

    forma = (
        (frontmatter.get("extensions") or {}).get("kora", {}).get("atlas", {}).get("forma_material")
    )
    if forma != "habilidad":
        raise ValueError(
            f"codex skill target solo aplica a forma_material=habilidad, "
            f"pero {skill_md_path.relative_to(KORA_ROOT)} es '{forma}'"
        )

    vector = _get_vector_ontologico(frontmatter)
    projected, detail = _project_vector(vector, "codex")
    target_dir = _build_codex_skill_target_path(skill_md_path)
    skill_name = skill_md_path.parent.name

    summary = {
        "source": str(skill_md_path.relative_to(KORA_ROOT)),
        "target_dir": str(target_dir.relative_to(KORA_ROOT)),
        "bundle_path": str((target_dir / skill_name / "SKILL.md").relative_to(KORA_ROOT)),
        "projected_vector": projected,
        "loss_by_axis": {ax: d.get("loss") for ax, d in detail.items() if d.get("loss")},
        "subdirs_renamed": {},
    }
    if dry_run:
        return target_dir, summary

    target_dir.mkdir(parents=True, exist_ok=True)
    source_hash = _sha256(skill_md_path)
    yml_path = _emit_transmutation_yml(
        target_dir,
        skill_md_path,
        "codex",
        skill_md_path.parent.parent.name,
        skill_name,
        frontmatter.get("version", "0.0.0"),
        source_hash,
        frontmatter,
        vector,
        projected,
        detail,
    )
    bundle_path = _emit_codex_skill_bundle(target_dir, skill_name, frontmatter, body)

    for entry in skill_md_path.parent.iterdir():
        if entry.name in {"SKILL.md", "_BUILD"} or entry.name.startswith("."):
            continue
        if entry.is_dir():
            dst_name = AGENTSKILLS_SUBDIR_RENAMES.get(entry.name, entry.name)
            if dst_name != entry.name:
                summary["subdirs_renamed"][entry.name] = dst_name
            dst_dir = bundle_path.parent / dst_name
            dst_dir.mkdir(parents=True, exist_ok=True)
            for item in entry.rglob("*"):
                if item.is_file():
                    rel = item.relative_to(entry)
                    dst_file = dst_dir / rel
                    dst_file.parent.mkdir(parents=True, exist_ok=True)
                    dst_file.write_bytes(item.read_bytes())
        elif entry.is_file():
            (bundle_path.parent / entry.name).write_bytes(entry.read_bytes())

    return target_dir, summary


def _transmute_skill_to_opencode(skill_md_path: Path, dry_run: bool = False) -> tuple[Path, dict]:
    """Project a KORA skill to OpenCode skill layout.

    OpenCode discovers project skills at `.opencode/skills/<skill-name>/SKILL.md`.
    KORA materializes the equivalent bundle under:
      {skill_dir}/_BUILD/opencode/<skill-name>/SKILL.md

    The bundle is agentskills.io-compatible: KORA `referencias/` becomes
    `references/`, `recursos/` becomes `assets/`, and `scripts/` is preserved.
    """
    frontmatter, body = load_markdown_parts(skill_md_path)
    if not isinstance(frontmatter, dict):
        raise ValueError(f"No YAML frontmatter in {skill_md_path}")

    forma = (
        (frontmatter.get("extensions") or {}).get("kora", {}).get("atlas", {}).get("forma_material")
    )
    if forma != "habilidad":
        raise ValueError(
            f"opencode skill target solo aplica a forma_material=habilidad, "
            f"pero {skill_md_path.relative_to(KORA_ROOT)} es '{forma}'"
        )

    vector = _get_vector_ontologico(frontmatter)
    projected, detail = _project_vector(vector, "opencode")
    target_dir = _build_opencode_skill_target_path(skill_md_path)
    skill_name = skill_md_path.parent.name

    summary = {
        "source": str(skill_md_path.relative_to(KORA_ROOT)),
        "target_dir": str(target_dir.relative_to(KORA_ROOT)),
        "bundle_path": str((target_dir / skill_name / "SKILL.md").relative_to(KORA_ROOT)),
        "projected_vector": projected,
        "loss_by_axis": {ax: d.get("loss") for ax, d in detail.items() if d.get("loss")},
        "subdirs_renamed": {},
    }
    if dry_run:
        return target_dir, summary

    target_dir.mkdir(parents=True, exist_ok=True)
    source_hash = _sha256(skill_md_path)
    yml_path = _emit_transmutation_yml(
        target_dir,
        skill_md_path,
        "opencode",
        skill_md_path.parent.parent.name,
        skill_name,
        frontmatter.get("version", "0.0.0"),
        source_hash,
        frontmatter,
        vector,
        projected,
        detail,
    )
    bundle_path = _emit_opencode_skill_bundle(target_dir, skill_name, frontmatter, body)

    for entry in skill_md_path.parent.iterdir():
        if entry.name in {"SKILL.md", "_BUILD"} or entry.name.startswith("."):
            continue
        if entry.is_dir():
            dst_name = AGENTSKILLS_SUBDIR_RENAMES.get(entry.name, entry.name)
            if dst_name != entry.name:
                summary["subdirs_renamed"][entry.name] = dst_name
            dst_dir = bundle_path.parent / dst_name
            dst_dir.mkdir(parents=True, exist_ok=True)
            for item in entry.rglob("*"):
                if item.is_file():
                    rel = item.relative_to(entry)
                    dst_file = dst_dir / rel
                    dst_file.parent.mkdir(parents=True, exist_ok=True)
                    dst_file.write_bytes(item.read_bytes())
        elif entry.is_file():
            (bundle_path.parent / entry.name).write_bytes(entry.read_bytes())

    # Keep yml_path referenced for parity with other skill transmuters.
    _ = yml_path
    return target_dir, summary


def _transmute_skill_to_openclaw(skill_md_path: Path, dry_run: bool = False) -> tuple[Path, dict]:
    """Project a KORA skill to OpenClaw skill layout.

    OpenClaw workspaces discover skills under `skills/<skill-name>/SKILL.md`.
    KORA materializes the standalone bundle under:
      {skill_dir}/_BUILD/openclaw/skills/<skill-name>/SKILL.md

    The bundle is agentskills.io-compatible: KORA `referencias/` becomes
    `references/`, `recursos/` becomes `assets/`, and `scripts/` is preserved.
    """
    frontmatter, body = load_markdown_parts(skill_md_path)
    if not isinstance(frontmatter, dict):
        raise ValueError(f"No YAML frontmatter in {skill_md_path}")

    forma = (
        (frontmatter.get("extensions") or {}).get("kora", {}).get("atlas", {}).get("forma_material")
    )
    if forma != "habilidad":
        raise ValueError(
            f"openclaw skill target solo aplica a forma_material=habilidad, "
            f"pero {skill_md_path.relative_to(KORA_ROOT)} es '{forma}'"
        )

    vector = _get_vector_ontologico(frontmatter)
    projected, detail = _project_vector(vector, "openclaw")
    target_dir = _build_openclaw_skill_target_path(skill_md_path)
    skill_name = skill_md_path.parent.name

    summary = {
        "source": str(skill_md_path.relative_to(KORA_ROOT)),
        "target_dir": str(target_dir.relative_to(KORA_ROOT)),
        "bundle_path": str((target_dir / "skills" / skill_name / "SKILL.md").relative_to(KORA_ROOT)),
        "projected_vector": projected,
        "loss_by_axis": {ax: d.get("loss") for ax, d in detail.items() if d.get("loss")},
        "subdirs_renamed": {},
    }
    if dry_run:
        return target_dir, summary

    target_dir.mkdir(parents=True, exist_ok=True)
    source_hash = _sha256(skill_md_path)
    yml_path = _emit_transmutation_yml(
        target_dir,
        skill_md_path,
        "openclaw",
        skill_md_path.parent.parent.name,
        skill_name,
        frontmatter.get("version", "0.0.0"),
        source_hash,
        frontmatter,
        vector,
        projected,
        detail,
    )
    bundle_path = _emit_openclaw_skill_bundle(target_dir, skill_name, frontmatter, body)

    for entry in skill_md_path.parent.iterdir():
        if entry.name in {"SKILL.md", "_BUILD"} or entry.name.startswith("."):
            continue
        if entry.is_dir():
            dst_name = AGENTSKILLS_SUBDIR_RENAMES.get(entry.name, entry.name)
            if dst_name != entry.name:
                summary["subdirs_renamed"][entry.name] = dst_name
            dst_dir = bundle_path.parent / dst_name
            dst_dir.mkdir(parents=True, exist_ok=True)
            for item in entry.rglob("*"):
                if item.is_file():
                    rel = item.relative_to(entry)
                    dst_file = dst_dir / rel
                    dst_file.parent.mkdir(parents=True, exist_ok=True)
                    dst_file.write_bytes(item.read_bytes())
        elif entry.is_file():
            (bundle_path.parent / entry.name).write_bytes(entry.read_bytes())

    # Keep yml_path referenced for parity with other skill transmuters.
    _ = yml_path
    return target_dir, summary


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
    vector = _get_vector_ontologico(frontmatter)
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
            "metadata": {
                "trace_fidelity": _trace_fidelity_for_target("agentskills"),
                "evidence_level": "byte-identical-projection-plus-declared-laws",
                "schema": "serialization/schemas/kora-transmutation-schema.json",
            },
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
                "presentacion": _get_presentacion(frontmatter),
            },
            "structural_preservation": _structural_preservation_record("agentskills"),
            "projection_preservation": {
                "semantic_body": {
                    "status": "preserved",
                    "evidence": "body projected with heading/subdir renames only",
                },
            },
            "projections": detail,
            "field_renames": AGENTSKILLS_FIELD_RENAMES,
            "subdir_renames": summary["subdirs_renamed"],
            "section_renames": AGENTSKILLS_SECTION_RENAMES,
            "bisimulation_claim": "byte-identical-modulo-renames",
            "bisimulation_evidence": "filesystem diff modulo declared renames",
            "references": {
                "autoria_spec": "urn:kora:kb:autoria-spec",
                "transmutation_spec": "urn:kora:kb:transmutation-spec",
            },
        }
    }
    yml_path = target_dir / "_transmutation.yml"
    _write_transmutation_manifest(yml_path, manifest)

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

    Para target=claude-code, target=codex, target=opencode u target=openclaw,
    si `agent` resuelve a una skill productiva se usa el fast-path skill->runtime. Para otros targets, o si no
    hay skill resoluble, el artefacto es un AGENT.md y la compilacion final
    requiere un adapter skill o LLM.

    Para otros targets (gemini, mastra), el artefacto
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

    if target == "claude-code":
        try:
            skill_md_path = _resolve_skill_path(agent)
        except ValueError:
            skill_md_path = None
        if skill_md_path is not None:
            print(f"=== KORA Transmutation: {agent} -> claude-code skill ===\n")
            print(f"  Source: {skill_md_path.relative_to(KORA_ROOT)}")
            if dry_run:
                target_dir, summary = _transmute_skill_to_claude_code(skill_md_path, dry_run=True)
                print(f"  [dry-run] Would emit: {target_dir.relative_to(KORA_ROOT)}/")
                print(f"  [dry-run] Would emit bundle: {summary['bundle_path']}")
                return
            target_dir, summary = _transmute_skill_to_claude_code(skill_md_path, dry_run=False)
            print(f"  Output: {target_dir.relative_to(KORA_ROOT)}/")
            print(f"  Manifest: {target_dir.relative_to(KORA_ROOT) / '_transmutation.yml'}")
            print(f"  Bundle: {summary['bundle_path']}")
            print(f"\n  Proyeccion skill -> Claude Code completada.")
            return

    if target == "codex":
        try:
            skill_md_path = _resolve_skill_path(agent)
        except ValueError:
            skill_md_path = None
        if skill_md_path is not None:
            print(f"=== KORA Transmutation: {agent} -> codex skill ===\n")
            print(f"  Source: {skill_md_path.relative_to(KORA_ROOT)}")
            if dry_run:
                target_dir, summary = _transmute_skill_to_codex(skill_md_path, dry_run=True)
                print(f"  [dry-run] Would emit: {target_dir.relative_to(KORA_ROOT)}/")
                print(f"  [dry-run] Would emit bundle: {summary['bundle_path']}")
                return
            target_dir, summary = _transmute_skill_to_codex(skill_md_path, dry_run=False)
            print(f"  Output: {target_dir.relative_to(KORA_ROOT)}/")
            print(f"  Manifest: {target_dir.relative_to(KORA_ROOT) / '_transmutation.yml'}")
            print(f"  Bundle: {summary['bundle_path']}")
            if summary["subdirs_renamed"]:
                print(f"  Subdirs renombrados:")
                for src, dst in summary["subdirs_renamed"].items():
                    print(f"    {src}/ -> {dst}/")
            print(f"\n  Proyeccion skill -> Codex completada.")
            return

    if target == "opencode":
        try:
            skill_md_path = _resolve_skill_path(agent)
        except ValueError:
            skill_md_path = None
        if skill_md_path is not None:
            print(f"=== KORA Transmutation: {agent} -> opencode skill ===\n")
            print(f"  Source: {skill_md_path.relative_to(KORA_ROOT)}")
            if dry_run:
                target_dir, summary = _transmute_skill_to_opencode(skill_md_path, dry_run=True)
                print(f"  [dry-run] Would emit: {target_dir.relative_to(KORA_ROOT)}/")
                print(f"  [dry-run] Would emit bundle: {summary['bundle_path']}")
                return
            target_dir, summary = _transmute_skill_to_opencode(skill_md_path, dry_run=False)
            print(f"  Output: {target_dir.relative_to(KORA_ROOT)}/")
            print(f"  Manifest: {target_dir.relative_to(KORA_ROOT) / '_transmutation.yml'}")
            print(f"  Bundle: {summary['bundle_path']}")
            if summary["subdirs_renamed"]:
                print(f"  Subdirs renombrados:")
                for src, dst in summary["subdirs_renamed"].items():
                    print(f"    {src}/ -> {dst}/")
            print(f"\n  Proyeccion skill -> OpenCode completada.")
            return

    if target == "openclaw":
        try:
            skill_md_path = _resolve_skill_path(agent)
        except ValueError:
            skill_md_path = None
        if skill_md_path is not None:
            print(f"=== KORA Transmutation: {agent} -> openclaw skill ===\n")
            print(f"  Source: {skill_md_path.relative_to(KORA_ROOT)}")
            if dry_run:
                target_dir, summary = _transmute_skill_to_openclaw(skill_md_path, dry_run=True)
                print(f"  [dry-run] Would emit: {target_dir.relative_to(KORA_ROOT)}/")
                print(f"  [dry-run] Would emit bundle: {summary['bundle_path']}")
                return
            target_dir, summary = _transmute_skill_to_openclaw(skill_md_path, dry_run=False)
            print(f"  Output: {target_dir.relative_to(KORA_ROOT)}/")
            print(f"  Manifest: {target_dir.relative_to(KORA_ROOT) / '_transmutation.yml'}")
            print(f"  Bundle: {summary['bundle_path']}")
            if summary["subdirs_renamed"]:
                print(f"  Subdirs renombrados:")
                for src, dst in summary["subdirs_renamed"].items():
                    print(f"    {src}/ -> {dst}/")
            print(f"\n  Proyeccion skill -> OpenClaw completada.")
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
    vector = _get_vector_ontologico(frontmatter)
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
    target_dir = _build_target_path(agent_md_path.parent, target)
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
        elif target == "codex":
            print(f"  [dry-run] Would emit skill: {target_dir}/{name}/SKILL.md")
        elif target == "opencode":
            print(f"  [dry-run] Would emit agent: {target_dir}/agents/{name}.md")
        elif target == "openclaw":
            print(f"  [dry-run] Would emit workspace: {target_dir}/workspace/")
            print(f"  [dry-run] Would emit config: {target_dir}/config/openclaw.json5")
            print(f"  [dry-run] Would emit deploy guide: {target_dir}/DEPLOY.md")
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
    elif target == "codex":
        bundle_path = _emit_codex_agent_bundle(target_dir, name, frontmatter, body, yml_path)
        print(f"  Bundle: {bundle_path.relative_to(KORA_ROOT)}")
    elif target == "opencode":
        bundle_path = _emit_opencode_agent_bundle(target_dir, name, frontmatter, body, yml_path)
        print(f"  Agent: {bundle_path.relative_to(KORA_ROOT)}")
    elif target == "openclaw":
        emitted = _emit_openclaw_agent_workspace(target_dir, name, frontmatter, body, yml_path)
        print(f"  Workspace: {(target_dir / 'workspace').relative_to(KORA_ROOT)}/")
        print(f"  Config: {(target_dir / 'config' / 'openclaw.json5').relative_to(KORA_ROOT)}")
        print(f"  Deploy: {(target_dir / 'DEPLOY.md').relative_to(KORA_ROOT)}")
        print(f"  Files: {len(emitted)}")

    print(f"\n  Transmutacion preparada.")
    if target in {"claude-code", "codex", "opencode", "openclaw"}:
        print(f"  Artefactos {target} emitidos desde AGENT.md + _transmutation.yml.")
    else:
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

    # Construir AGENT.md canonico en _FRAGUA/INBOX/
    fragua_path = AGENTS_ROOT / "_FRAGUA" / "INBOX" / name / "AGENT.md"
    fragua_path.parent.mkdir(parents=True, exist_ok=True)

    new_frontmatter = {
        "_manifest": {
            "urn": f"urn:{namespace}:artefacto:{name}",
            "type": "artefacto",
            "provenance": {
                "created_by": "kora-ingest",
                "created_at": datetime.now().strftime("%Y-%m-%d"),
                "source": str(file_path),
            },
        },
        "version": "1.0.0",
        "status": "borrador",
        "nombre": name,
        "descripcion": description[:200] if len(description) > 200 else description,
        "tags": ["ingested", "claude-code", namespace],
        "lang": "es",
        "extensions": {
            "kora": {
                "vector_ontologico": vector,
                "presentacion": "estado-primario",
                "atlas": {
                    "arnes_categorico": "persona" if vector["mu"] >= 2 else "delegado",
                    "forma_material": "agente-propiamente-tal" if vector["mu"] >= 2 else "subagente",
                    "metafora_relacional": "centro-de-control" if vector["phi"] >= 2 else "superherramienta",
                },
                "entornos_objetivo": ["claude-code"],
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
        "artefacto": {
            "perfil": {
                "descripcion": description[:200] if len(description) > 200 else description,
                "dominio": [namespace],
                "narrativa": description,
            },
            "plan": {
                "estado_inicial": "S-START",
                "estado_terminal": "S-END",
                "estados": [
                    {"id": "S-START", "accion": "Estado de entrada derivado de ingestion. Revisar body para FSM."},
                    {"id": "S-END", "accion": "Terminal.", "transiciones": "terminal"},
                ],
            },
            "interfaz": {"tools": [], "permissions": {"allow": []}},
            "contexto": {
                "memoria_config": {"mode": "persistent" if memory == "user" else "session"},
            },
            "invariantes": {
                "compromisos_eticos": {
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


def _lift_codex_skill(file_path: Path, from_runtime: str = "codex", namespace: str = "kora"):
    """Eleva un skill runtime a artifacts/skills/_TALLER/INBOX/."""
    frontmatter, body = load_markdown_parts(file_path)
    if not isinstance(frontmatter, dict):
        raise ValueError(f"No YAML frontmatter in {file_path}")

    name = frontmatter.get("name", file_path.stem)
    description = frontmatter.get("description", "")

    vector = dict(DEFAULT_VECTORS_BY_FROM[from_runtime])

    taller_path = SKILLS_ROOT / "_TALLER" / "INBOX" / name / "SKILL.md"
    taller_path.parent.mkdir(parents=True, exist_ok=True)

    new_frontmatter = {
        "_manifest": {
            "urn": f"urn:{namespace}:artefacto:{name}",
            "type": "artefacto",
            "provenance": {
                "created_by": "kora-ingest",
                "created_at": datetime.now().strftime("%Y-%m-%d"),
                "source": str(file_path),
            },
        },
        "version": "1.0.0",
        "status": "borrador",
        "nombre": name,
        "descripcion": description,
        "tags": ["ingested", from_runtime, namespace],
        "lang": "es",
        "extensions": {
            "kora": {
                "vector_ontologico": vector,
                "presentacion": "estado-primario",
                "atlas": {
                    "arnes_categorico": "disciplina" if vector["pi"] >= 2 else "utilidad",
                    "forma_material": "habilidad",
                    "metafora_relacional": "superherramienta",
                },
                "entornos_objetivo": [from_runtime],
                "nivel_prescripcion": "medio",
                "ingested_from": from_runtime,
            },
            from_runtime.replace("-", "_"): {
                "allowed_tools": frontmatter.get("allowed-tools", "Read"),
            },
        },
        "artefacto": {
            "perfil": {
                "descripcion": description,
                "dominio": [namespace],
                "disparadores": [],
                "salidas": [],
            },
            "plan": {
                "estado_inicial": "S-START",
                "estado_terminal": "S-END",
                "estados": [
                    {"id": "S-START", "accion": "Ejecutar habilidad."},
                    {"id": "S-END", "accion": "Terminal.", "transiciones": "terminal"},
                ],
            },
            "interfaz": {"tools": [], "permissions": {"allow": []}},
            "contexto": {},
            "invariantes": {"reglas_duras": []},
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
            "urn": f"urn:kora:artefacto:{agent_id}",
            "type": "artefacto",
            "provenance": {
                "created_by": "kora-ingest",
                "created_at": datetime.now().strftime("%Y-%m-%d"),
                "source": str(workspace_dir),
            },
        },
        "version": "1.0.0",
        "status": "borrador",
        "nombre": agent_id,
        "descripcion": description or f"OpenClaw agent {agent_id}",
        "tags": ["ingested", "openclaw"],
        "lang": "es",
        "extensions": {
            "kora": {
                "vector_ontologico": vector,
                "presentacion": "estado-primario",
                "atlas": {
                    "arnes_categorico": "servicio",
                    "forma_material": "agente-plataforma",
                    "metafora_relacional": "centro-de-control",
                },
                "entornos_objetivo": ["openclaw"],
                "ingested_from": "openclaw",
            },
            "openclaw": {
                "agent_id": agent_id,
                "workspace_path": f"workspaces/{agent_id}/",
            },
        },
        "artefacto": {
            "perfil": {
                "descripcion": description or f"OpenClaw agent {agent_id}",
                "dominio": ["openclaw-fleet"],
            },
            "plan": {
                "estado_inicial": "S-START",
                "estado_terminal": "S-END",
                "estados": [
                    {"id": "S-START", "accion": "Entry."},
                    {"id": "S-END", "accion": "Terminal.", "transiciones": "terminal"},
                ],
            },
            "interfaz": {"tools": [], "permissions": {"allow": []}},
            "contexto": {
                "memoria_config": {"mode": "ambient", "storage": f"{workspace_dir}/memory/"},
            },
            "invariantes": {
                "compromisos_eticos": {
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

    elif from_runtime in ("codex", "gemini", "opencode"):
        if not file:
            raise ValueError(f"--file required for {from_runtime} ingest")
        file_path = Path(file).expanduser().resolve()
        if not file_path.is_file():
            raise ValueError(f"File not found: {file_path}")
        print(f"  Source: {file_path}")
        if dry_run:
            print(f"  [dry-run] Would lift skill to artifacts/skills/_TALLER/INBOX/")
            return
        # opencode skills son agentskills.io-compatible (frontmatter name + description),
        # mismo lift que codex/gemini. Para opencode agents (.md con mode), pendiente
        # un lifter dedicado en v1.1 — usar `_lift_claude_code_subagent` como fallback
        # si el frontmatter declara `mode`.
        result = _lift_codex_skill(file_path, from_runtime=from_runtime, namespace=namespace)
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
                         f"Supported: claude-code, codex, gemini, opencode, openclaw")

    print(f"\n  Ingest preparado. El artefacto en staging requiere:")
    print(f"    1. Completar campos TODO en artefacto.invariantes.compromisos_eticos.")
    print(f"    2. Ajustar vector_ontologico si la heuristica fue imprecisa.")
    print(f"    3. Revisar plan FSM (auto-generado como stub).")
    print(f"    4. Pasar por REVIEW y publicar segun el pipeline _FRAGUA/_TALLER vigente.")
