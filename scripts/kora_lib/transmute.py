"""Transmutation orchestrator: proyecta KORA IR a un runtime target.

Implementa el functor T_R: KORA_IR → Runtime_R de transmutation-spec v1.0,
usando las matrices de preservacion declaradas en cada runtime-extension.

Funciones principales:
- cmd_transmute: ejecuta la transmutacion, emite _transmutation.yml y prepara
  el workspace de output en {workspace}/_BUILD/{target}/.
- cmd_ingest: ingesta inversa Lift_R — absorbe un artefacto runtime foraneo
  a KORA IR.
"""

import hashlib
from datetime import datetime, timezone
from pathlib import Path

import yaml

from .artifacts import load_markdown_parts, dump_yaml_frontmatter_and_body
from .config import AGENTS_ROOT, KORA_ROOT, SKILLS_ROOT


# ---------------------------------------------------------------------------
# Matrices de preservacion por runtime (derivadas de runtime-extensions)
# ---------------------------------------------------------------------------

# Formato: cada entrada es { eje_valor: {projected, fidelity, loss?} }
# fidelity ∈ {full, partial, none}

PRESERVATION_MATRIX = {
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
    """Extrae harness_vector del IR. Falla si no esta declarado (requerido por v2)."""
    vector = frontmatter.get("extensions", {}).get("kora", {}).get("harness_vector")
    if not isinstance(vector, dict):
        raise ValueError(
            "Missing extensions.kora.harness_vector. "
            "Run `kora migrate --profile v2-agentfile` to auto-derive."
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


def _emit_transmutation_yml(target_dir: Path, agent_md_path: Path, target: str,
                             ns: str, name: str, version: str,
                             source_hash: str, frontmatter: dict,
                             vector: dict, projected: dict,
                             projections_detail: dict):
    """Emite _transmutation.yml conforme transmutation-spec §6."""
    adapter = _resolve_adapter_skill(target)
    presentation = frontmatter.get("extensions", {}).get("kora", {}).get("presentation", "state-primary")

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
        }
    }

    yml_path = target_dir / "_transmutation.yml"
    yml_path.write_text(
        yaml.safe_dump(manifest, sort_keys=False, allow_unicode=True),
        encoding="utf-8",
    )
    return yml_path


# ---------------------------------------------------------------------------
# CLI commands
# ---------------------------------------------------------------------------

def cmd_transmute(target: str, agent: str, dry_run: bool = False):
    """Transmuta un agente IR al runtime target.

    Pasos:
    1. Resuelve AGENT.md del agente.
    2. Valida que existe harness_vector (v2 del agentfile-spec).
    3. Proyecta el vector al dominio del runtime (puede fallar si fuera de dominio).
    4. Prepara {workspace}/_BUILD/{target}/.
    5. Emite _transmutation.yml con estructura completa.
    6. Reporta pasos siguientes (invocar adapter skill o LLM manual).
    """
    if target not in SUPPORTED_TARGETS:
        raise ValueError(f"Unknown target: {target}. Supported: {SUPPORTED_TARGETS}")

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
        return

    # Crear y emitir
    target_dir.mkdir(parents=True, exist_ok=True)
    yml_path = _emit_transmutation_yml(
        target_dir, agent_md_path, target, ns, name, version,
        source_hash, frontmatter, vector, projected, detail
    )
    print(f"  Manifest: {yml_path.relative_to(KORA_ROOT)}")

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
    """Eleva un skill Codex a SKILLS/_TALLER/INBOX/."""
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
    """Eleva un workspace OpenClaw completo a AGENTS/_FRAGUA/INBOX/."""
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
            print(f"  [dry-run] Would lift to AGENTS/_FRAGUA/INBOX/{file_path.stem}/AGENT.md")
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
            print(f"  [dry-run] Would lift skill to SKILLS/_TALLER/INBOX/")
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
            print(f"  [dry-run] Would lift workspace to AGENTS/_FRAGUA/INBOX/{ws_path.name}/")
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
