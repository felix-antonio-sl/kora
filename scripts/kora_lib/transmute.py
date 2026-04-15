"""Transmutation orchestrator: validate IR, prepare BUILD/, emit manifest."""

import hashlib
from datetime import datetime, timezone
from pathlib import Path

import yaml

from .artifacts import load_markdown_parts
from .config import AGENTS_ROOT, KORA_ROOT


BUILD_ROOT = KORA_ROOT / "BUILD"
SKILLS_ROOT = KORA_ROOT / "SKILLS"

REQUIRED_DIMENSIONS = (
    "coalgebra",
    "plan",
    "interface",
    "fibers",
    "composition",
    "safety",
)

TARGET_ADAPTERS = {
    "claude-code": "transmute-claude-code",
    "openclaw": "transmute-openclaw",
}

# Default fidelity per target (placeholder until adapter fills real values)
DEFAULT_FIDELITY = {
    "claude-code": {
        "dim_1_coalgebra": "degraded",
        "dim_2_plan": "preserved",
        "dim_3_interface": "degraded",
        "dim_4_fibers": {
            "identity": "preserved",
            "operator": "preserved",
            "memory": "lost",
            "runtime": "degraded",
            "knowledge": "degraded",
        },
        "dim_5_composition": "degraded",
        "dim_6_safety": "degraded",
    },
    "openclaw": {
        "dim_1_coalgebra": "preserved",
        "dim_2_plan": "preserved",
        "dim_3_interface": "preserved",
        "dim_4_fibers": {
            "identity": "preserved",
            "operator": "preserved",
            "memory": "preserved",
            "runtime": "degraded",
            "knowledge": "preserved",
        },
        "dim_5_composition": "preserved",
        "dim_6_safety": "preserved",
    },
}

DEFAULT_LOSSES = {
    "claude-code": [
        "dim_1: FSM serializada como secciones markdown; sin engine de estados",
        "dim_3: tools como instrucciones informativas; sin enforcement nativo",
        "dim_4.memory: Claude Code gestiona memoria propia; no inyectable",
        "dim_4.runtime: model_routing no aplicable; runtime_capabilities implicitas",
        "dim_5: sub-agentes parciales; hooks cross-gateway no disponibles",
        "dim_6: sandbox, limits y policy_flags no configurables via .md",
    ],
    "openclaw": [
        "dim_4.runtime: lifecycle (heartbeat, cron) y dissipation requieren config manual en openclaw.json5",
    ],
}


def _sha256(path: Path) -> str:
    """Return sha256:<hex> of file contents."""
    content = path.read_bytes()
    return "sha256:" + hashlib.sha256(content).hexdigest()


def _parse_agent_md(agent_md_path: Path):
    """Parse AGENT.md, return (frontmatter, body) or raise."""
    frontmatter, body = load_markdown_parts(agent_md_path)
    if frontmatter is None:
        raise ValueError(f"No YAML frontmatter in {agent_md_path}")
    return frontmatter, body


def _validate_dimensions(frontmatter: dict, agent_md_path: Path):
    """Ensure all 6 dimensions are present under agent.*."""
    agent = frontmatter.get("agent")
    if not isinstance(agent, dict):
        raise ValueError(f"{agent_md_path}: missing 'agent' key in frontmatter")

    missing = [dim for dim in REQUIRED_DIMENSIONS if dim not in agent]
    if missing:
        raise ValueError(
            f"{agent_md_path}: missing dimensions: {', '.join(missing)}"
        )
    return agent


def _resolve_agent_path(agent_ref: str) -> Path:
    """Resolve 'ns/name' to AGENTS/{ns}/{name}/AGENT.md."""
    parts = agent_ref.strip().split("/")
    if len(parts) != 2:
        raise ValueError(
            f"Agent ref must be 'namespace/name', got: {agent_ref}"
        )
    ns, name = parts
    agent_dir = AGENTS_ROOT / ns / name
    if not agent_dir.is_dir():
        raise ValueError(f"Agent directory not found: {agent_dir}")
    agent_md = agent_dir / "AGENT.md"
    if not agent_md.is_file():
        raise ValueError(f"AGENT.md not found: {agent_md}")
    return agent_md


def _resolve_adapter_skill(target: str) -> Path:
    """Verify adapter skill exists, return its SKILL.md path."""
    adapter_name = TARGET_ADAPTERS.get(target)
    if not adapter_name:
        raise ValueError(f"Unknown target: {target}")

    skill_dir = SKILLS_ROOT / "kora" / adapter_name
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        raise ValueError(
            f"Adapter skill not found: {skill_md}\n"
            f"Create SKILLS/kora/{adapter_name}/SKILL.md first."
        )
    return skill_md


def _build_target_path(target: str, ns: str, name: str) -> Path:
    """Compute the output directory under BUILD/."""
    return BUILD_ROOT / target / ns


def _emit_transmutation_yml(
    target_dir: Path,
    agent_md_path: Path,
    target: str,
    ns: str,
    name: str,
    version: str,
    source_hash: str,
):
    """Write _transmutation.yml manifest next to generated artifacts."""
    adapter_name = TARGET_ADAPTERS[target]
    # Compute target_path relative to repo
    if target == "claude-code":
        target_path = f"BUILD/claude-code/{ns}/{name}.md"
    elif target == "openclaw":
        target_path = f"BUILD/openclaw/{ns}/{name}/"
    else:
        target_path = f"BUILD/{target}/{ns}/{name}/"

    source_rel = str(agent_md_path.relative_to(KORA_ROOT))

    manifest = {
        "source": source_rel,
        "source_hash": source_hash,
        "target": target,
        "target_path": target_path,
        "adapter": f"CM-TRANSMUTE-{target.upper().replace('-', '-')}",
        "timestamp": datetime.now(timezone.utc).astimezone().isoformat(),
        "version": version,
        "fidelity": DEFAULT_FIDELITY.get(target, {}),
        "losses": DEFAULT_LOSSES.get(target, []),
    }

    yml_path = target_dir / f"{name}._transmutation.yml"
    yml_path.write_text(
        yaml.safe_dump(manifest, sort_keys=False, allow_unicode=True),
        encoding="utf-8",
    )
    return yml_path


def cmd_transmute(target: str, agent: str, dry_run: bool = False):
    """Orchestrate transmutation: validate IR, prepare BUILD/, emit manifest.

    This command does NOT perform the semantic compilation (that is done by
    an LLM executing the adapter skill). It prepares the workspace:
    1. Validates the AGENT.md has all 6 dimensions
    2. Verifies the adapter skill exists
    3. Creates BUILD/{target}/{ns}/
    4. Emits _transmutation.yml with source hash and fidelity placeholders
    5. Reports what the LLM should do next
    """
    # 1. Resolve agent
    agent_md_path = _resolve_agent_path(agent)
    ns, name = agent.strip().split("/")

    print(f"=== KORA Transmutation: {agent} -> {target} ===\n")

    # 2. Parse and validate IR
    print(f"  Source: {agent_md_path.relative_to(KORA_ROOT)}")
    frontmatter, body = _parse_agent_md(agent_md_path)
    agent_data = _validate_dimensions(frontmatter, agent_md_path)
    version = frontmatter.get("version", "0.0.0")
    print(f"  Version: {version}")
    print(f"  Dimensions: {', '.join(REQUIRED_DIMENSIONS)} -- all present")

    # 3. Verify adapter skill
    adapter_skill_path = _resolve_adapter_skill(target)
    print(f"  Adapter: {adapter_skill_path.relative_to(KORA_ROOT)}")

    # 4. Compute hash
    source_hash = _sha256(agent_md_path)
    print(f"  Hash: {source_hash[:20]}...")

    # 5. Target directory
    target_dir = _build_target_path(target, ns, name)
    print(f"  Output: BUILD/{target}/{ns}/")

    if dry_run:
        print(f"\n  [dry-run] Would create: {target_dir}/")
        print(f"  [dry-run] Would emit: {target_dir}/{name}._transmutation.yml")
        print(f"\n  Next step: invoke LLM with adapter skill to compile IR -> {target}")
        return

    # 6. Create output directory
    target_dir.mkdir(parents=True, exist_ok=True)

    # 7. Emit transmutation manifest
    yml_path = _emit_transmutation_yml(
        target_dir, agent_md_path, target, ns, name, version, source_hash
    )
    print(f"  Manifest: {yml_path.relative_to(KORA_ROOT)}")

    # 8. Report next steps
    print(f"\n  Transmutation workspace prepared.")
    print(f"  The adapter skill is at: {adapter_skill_path.relative_to(KORA_ROOT)}")
    print(f"  Source IR is at: {agent_md_path.relative_to(KORA_ROOT)}")
    print(f"\n  Next step: invoke an LLM with the adapter skill.")
    print(f"  The LLM will read the AGENT.md, execute the skill procedure,")
    print(f"  and write compiled artifacts to BUILD/{target}/{ns}/")
