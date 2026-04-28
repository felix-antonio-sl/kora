from pathlib import Path
import re


KORA_ROOT = Path(__file__).resolve().parents[2]

# Topologia v5 (reorg 2026-04-18): estructura explicita por capa de gobernanza.
# Artefactos agenticos y knowledge viven bajo artifacts/; specs se parten en
# 4 capas (governance/ontology/serialization/runtime); scripts se unifican
# bajo toolchain/.
ARTIFACTS_ROOT = KORA_ROOT / "artifacts"
AGENTS_ROOT = ARTIFACTS_ROOT / "agents"
SKILLS_ROOT = ARTIFACTS_ROOT / "skills"
KNOWLEDGE_ROOT = ARTIFACTS_ROOT / "knowledge"
# Capas de specs (separadas desde reorg v5; antes todas en specs/).
GOVERNANCE_ROOT = KORA_ROOT / "governance"
ONTOLOGY_ROOT = KORA_ROOT / "ontology"
SERIALIZATION_ROOT = KORA_ROOT / "serialization"
RUNTIME_ROOT = KORA_ROOT / "runtime"
SPEC_ROOTS = (GOVERNANCE_ROOT, ONTOLOGY_ROOT, SERIALIZATION_ROOT, RUNTIME_ROOT)
TOOLCHAIN_ROOT = KORA_ROOT / "toolchain"

# Staging areas descentralizados (v8): el procesamiento vive dentro de cada
# directorio principal, no en un OPERATIONS/ centralizado.
# - artifacts/agents/_FRAGUA/{INBOX,REVIEW} para agentes en staging.
# - artifacts/skills/_TALLER/{INBOX,REVIEW} para skills en staging.
# - artifacts/knowledge/_SCRIPTORIUM/{INBOX,REVIEW} para knowledge en staging.
# Los subdirectorios de INBOX/ son pre-categoriales (sin namespace KORA); el
# URN se asigna al promover a REVIEW y luego a productivo.
FRAGUA_ROOT = AGENTS_ROOT / "_FRAGUA"
TALLER_ROOT = SKILLS_ROOT / "_TALLER"
SCRIPTORIUM_ROOT = KNOWLEDGE_ROOT / "_SCRIPTORIUM"
STAGING_ROOTS = (FRAGUA_ROOT, TALLER_ROOT, SCRIPTORIUM_ROOT)
STAGING_DIR_NAMES = {"_FRAGUA", "_TALLER", "_SCRIPTORIUM"}
STAGING_STAGES = ("INBOX", "REVIEW")
CATALOG_PATH = KORA_ROOT / "docs" / "generated" / "catalog.yml"
GENERATED_DOCS_DIR = KORA_ROOT / "docs" / "generated"
BOOTSTRAP_SCHEMA_PATH = SERIALIZATION_ROOT / "schemas" / "kora-agent-schema.json"
CONFIG_SCHEMA_PATH = SERIALIZATION_ROOT / "schemas" / "kora-agent-config-schema.json"
AGENTFILE_SCHEMA_PATH = SERIALIZATION_ROOT / "schemas" / "kora-agentfile-schema.json"
AGENT_BOOTSTRAP_FILES = ("AGENTS.md", "SOUL.md", "USER.md", "TOOLS.md")
# autoria-spec v1.2 §13.2: el workspace productivo solo requiere AGENT.md.
# AGENT_BOOTSTRAP_FILES se conserva para lookup historico de manifest types.
AGENT_REQUIRED_FILES = ("AGENT.md",)
AGENTFILE_NAME = "AGENT.md"
BOOTSTRAP_MANIFEST_TYPES = {
    "AGENTS.md": "bootstrap_agents",
    "SOUL.md": "bootstrap_soul",
    "USER.md": "bootstrap_user",
    "TOOLS.md": "bootstrap_tools",
    "config.json": "bootstrap_config",
}
SKILL_MANIFEST_TYPE = "lazy_load_endofunctor"
IGNORED_DIRS = {
    ".git",
    "build",
    "toolchain",
    "scripts",  # retrocompat: si un fork historico todavia tiene scripts/
    "tests",
    "docs",
    "_FRAGUA",
    "_TALLER",
    "_SCRIPTORIUM",
    "_BUILD",
    ".claude",
    ".agent",
    ".gemini",
    ".venv",
    "__pycache__",
    "_backups",
}
# Directorios al raíz del repo que se ignoran explícitamente (distintos de
# los ignored-by-name porque aquí el match es por path absoluto al raíz).
ROOT_IGNORED_DIRS = {"atomize", "_backups"}
IGNORED_FILES = {
    "README.md",
    "CLAUDE.md",
}
SKILL_REQUIRED_HEADINGS = (
    "## Proposito",
    "## Input/Output",
    "## Procedimiento",
    "## Signature Output",
)
TOOL_IDENTIFIER_PATTERN = re.compile(r"^/?[A-Za-z0-9._-]+$")
URN_REF_PATTERN = re.compile(
    r"(urn:[a-z0-9-]+:[a-z0-9-]+:(?:[A-Za-z0-9._/-]+:)*[A-Za-z0-9._/-]+(?:#[A-Za-z0-9._-]+)?)"
)
AGENT_ROUTE_PATTERN = re.compile(r"(?:->|→)([a-z0-9-]+)/([A-Za-z0-9_-]+)")
CM_REF_PATTERN = re.compile(r"CM-[A-Za-z0-9_-]+")
LEGACY_SKILL_HEADING_ALIASES = {
    "## I/O": "## Input/Output",
    "## Input / Output": "## Input/Output",
    "## Input-Output": "## Input/Output",
    "## Purpose": "## Proposito",
    "## Propósito": "## Proposito",
    "## Procedure": "## Procedimiento",
    "## Signature output": "## Signature Output",
}
LOW_LEVEL_RUNTIME_HINTS = {
    "filesystem_read",
    "filesystem_write",
    "code_execution",
    "git",
    "git_write",
    "lint",
    "test_runner",
    "test_execution",
    "test_read",
    "metrics_read",
    "kb_read",
    "analysis",
    "planning",
    "eval_execution",
    "eval_audit",
    "dependency_check",
    "deploy",
    "production_access",
    "secret_management",
    "config_write",
    "read_file",
    "write_file",
    "read_calendar",
    "send_message_telegram",
}
BROKEN_ROUTE_MAPPINGS = {}
KB_PIPELINE_NORMALIZATION = {
    "catalog→kb_route": "kb_route→catalog_resolve",
    "catalog -> kb_route": "kb_route -> catalog_resolve",
    "catalog→ kb_route": "kb_route→catalog_resolve",
    "catalog → kb_route": "kb_route → catalog_resolve",
}
SEMANTIC_TURN_CONTROL_PATTERNS = (
    re.compile(r"\bpreguntar al usuario\b", re.IGNORECASE),
    re.compile(r"\besperar respuesta\b", re.IGNORECASE),
    re.compile(r"\besperar al usuario\b", re.IGNORECASE),
    re.compile(r"\bofrecer continuar\b", re.IGNORECASE),
    re.compile(r"\bsolicitar clarificaci[oó]n\b", re.IGNORECASE),
    re.compile(r"\bsolicitar aclaraci[oó]n\b", re.IGNORECASE),
    re.compile(r"\bsi el usuario desea continuar\b", re.IGNORECASE),
)
SKILL_RAW_COMMAND_PATTERNS = (
    (re.compile(r"`(?:scripts/)?kora health`", re.IGNORECASE), "repo_health"),
    (re.compile(r"`(?:scripts/)?kora validate`", re.IGNORECASE), "repo_health"),
    (re.compile(r"`(?:scripts/)?kora stats`", re.IGNORECASE), "repo_health"),
    (re.compile(r"`git status`", re.IGNORECASE), "git_status"),
    (re.compile(r"`git log --oneline -5`", re.IGNORECASE), "git_status"),
    (re.compile(r"`(?:scripts/)?kora index`", re.IGNORECASE), "catalog_sync"),
    (re.compile(r"`(?:scripts/)?kora resolve", re.IGNORECASE), "urn_resolve"),
    (re.compile(r"`(?:scripts/)?kora intake`", re.IGNORECASE), "intake_pipeline"),
)
SOUL_FORBIDDEN_PATTERNS = (
    re.compile(r"\bSTATE:"),
    re.compile(r"\bTrans:"),
    re.compile(r"\bIF\s+.+(?:->|→)\s+S-[A-Z][A-Z0-9_-]+\b"),
)
SOUL_CANONICAL_HEADINGS = {"identidad dialectica", "paradigma cognitivo", "tono", "voz"}
SOUL_BEHAVIOR_HEADINGS = {"saludo", "estilo", "estilo respuesta", "ejemplos",
                          "ejemplos comportamiento", "ejemplos de comportamiento",
                          "comportamiento", "comportamiento operativo",
                          "contrato conductual", "estilo comunicativo"}
COINDUCTION_REQUIRED_CHECKS = ("SCOPE_COMPLIANCE", "STATE_AWARENESS", "INTERFACE_DISCIPLINE")
MULTITURNO_DETECTION_KEYWORDS = (
    re.compile(r"\bdesv[ií][ao]\b", re.IGNORECASE),
    re.compile(r"\bdetec(?:tar|cion|ci[oó]n)\b", re.IGNORECASE),
    re.compile(r"\bshift\b", re.IGNORECASE),
    re.compile(r"\bcomparar\s+solicitud\b", re.IGNORECASE),
)
MULTITURNO_ACTION_KEYWORDS = (
    re.compile(r"\bS-DISPATCHER\b"),
    re.compile(r"\breclasificar\b", re.IGNORECASE),
    re.compile(r"\brechaz(?:ar|o)\b", re.IGNORECASE),
    re.compile(r"\breenrut(?:ar|e)\b", re.IGNORECASE),
)
MULTITURNO_RETENTION_KEYWORDS = (
    re.compile(r"\bretenci[oó]n\b", re.IGNORECASE),
    re.compile(r"\bpreservar?\b", re.IGNORECASE),
    re.compile(r"\bmantener\b", re.IGNORECASE),
    re.compile(r"\binvariant", re.IGNORECASE),
    re.compile(r"\bturno\s+(?:previo|anterior|siguiente)\b", re.IGNORECASE),
)
USER_FORBIDDEN_PATTERNS = (
    re.compile(r"\ballowed_kb\b"),
    re.compile(r"\bsandbox\b"),
    re.compile(r"\bruntime_capabilities\b"),
    re.compile(r"\bsub_agents\b"),
    re.compile(r"\bmodel_routing\b"),
    re.compile(r"\bwiring\b", re.IGNORECASE),
)
AGENTS_FORBIDDEN_PATTERNS = (
    re.compile(r"\bblock_instructions\b"),
    re.compile(r"\bforbid_internal_jargon\b"),
    re.compile(r"^\s*-\s*Confidentiality\s*:", re.IGNORECASE | re.MULTILINE),
    re.compile(r"^\s*-\s*Response on query\s*:", re.IGNORECASE | re.MULTILINE),
)
TRACES_TO_SECTION_PATTERN = re.compile(r"formal/([0-9]{2})\s+§([0-9]+(?:\.[0-9]+)*)")
TRACES_TO_DOC_PATTERN = re.compile(r"formal/([0-9]{2})")
KB_PIPELINE_PATTERN = re.compile(
    r"(catalog|kb_route|catalog_resolve|urn|path|file|markdown)\s*(?:->|→)\s*"
    r"(catalog|kb_route|catalog_resolve|urn|path|file|markdown)",
    re.IGNORECASE,
)
LEGACY_FXSL_SIGNALS = (
    "/KNOWLEDGE/cat/",
    ".koda.yml",
    "catalog_master_fxsl.yml",
    "work in progress",
)
COHORT_NAMESPACE_GROUPS = {
    "meta-kora": {"kora"},
    "dev": {"dev"},
    "ops": {"ops"},
    "domains": {"fxsl", "pro", "salud", "gn", "korvo"},
}
META_KORA_AUDIT_WORKSPACES = (
    "kora/guardian",
    "kora/custodio",
)
COHORT_WORKSPACE_OVERRIDES = {
    "meta-kora": {workspace.split("/", 1)[1] for workspace in META_KORA_AUDIT_WORKSPACES},
}
META_KORA_STATUS = {
    "kora/guardian": {
        "status": "operating_core",
        "reason": "Nucleo operativo constitucional: gobierna coherencia de specs, precedencia y validacion fundacional.",
    },
    "kora/custodio": {
        "status": "operating_core",
        "reason": "Nucleo operativo: cierra salud, catalogo e ingesta del repo.",
    },
}
def _discover_productive_workspaces():
    """Deriva los workspaces productivos desde el filesystem.

    Un workspace es productivo si:
      - vive en artifacts/agents/{ns}/{name}/ (ns no empieza con "_"),
      - contiene AGENT.md,
      - AGENT.md declara status: activo.

    Retorna dict {ns: tuple(ns/name, ...)} agrupado por namespace.
    """
    from .artifacts import load_yaml_safe
    from .lifecycle import canonicalize_status

    agents_root = AGENTS_ROOT
    if not agents_root.exists():
        return {}
    out = {}
    for ns_dir in sorted(agents_root.iterdir()):
        if not ns_dir.is_dir() or ns_dir.name.startswith((".", "_")):
            continue
        ns = ns_dir.name
        workspaces = []
        for ws_dir in sorted(ns_dir.iterdir()):
            if not ws_dir.is_dir() or ws_dir.name.startswith((".", "_")):
                continue
            agent_md = ws_dir / "AGENT.md"
            if not agent_md.exists():
                continue
            fm, err = load_yaml_safe(agent_md)
            if err or not isinstance(fm, dict):
                continue
            status = canonicalize_status(fm.get("status"))
            if status not in ("activo", "publicado"):
                continue
            workspaces.append(f"{ns}/{ws_dir.name}")
        if workspaces:
            out[ns] = tuple(workspaces)
    return out


def _build_operating_core_cohorts():
    """Agrupa workspaces productivos en cohortes canonicas.

    Regla: namespace `kora` es cohort core; todo otro namespace es
    domain cohort. Resultado es dict {cohort_name: tuple(workspaces)}.
    """
    productive = _discover_productive_workspaces()
    cohorts = {}
    if "kora" in productive:
        cohorts["kora"] = productive["kora"]
    domain_workspaces = []
    for ns, workspaces in productive.items():
        if ns == "kora":
            continue
        domain_workspaces.extend(workspaces)
    if domain_workspaces:
        cohorts["domain_canary"] = tuple(domain_workspaces)
    return cohorts


# Vista materializada de los cohorts productivos. Derivado del filesystem:
# pasa a ser fuente de verdad cualquier AGENT.md con status activo.
OPERATING_CORE_COHORTS = _build_operating_core_cohorts()

DEPRECATED_URN_ALIASES = {
    "urn:kora:kb:spec-md": "urn:kora:kb:md-spec",
    "urn:kora:kb:agent-spec-md": "urn:kora:kb:agentfile-spec",
    "urn:kora:kb:skill-spec-md": "urn:kora:kb:skill-overlay-spec",
    "urn:kora:kb:swarm-spec-md": "urn:kora:kb:agentfile-spec",
    "urn:kora:kb:05-governance-lattice": "urn:kora:kb:cat-governance-lattice",
    "urn:kora:kb:transmutation-spec": "urn:kora:kb:runtime-spec-md",
    "urn:salud:artefacto:salubrista-hah": "urn:salud:artefacto:salubrista",
    "urn:salud:kb:firs-framework-integrado-razonamiento-salud": "urn:salud:artefacto:firs-razonamiento-sanitario",
    "urn:salud:kb:perfil-salubrista-copiloto-estrategico": "urn:salud:artefacto:salubrista",
    "urn:salud:kb:perfil-salubrista-hospitalizacion-integrada": "urn:salud:artefacto:hospitalizacion-domiciliaria",
    "urn:salud:kb:salubrista-fuente-publihealth-oxford-alias": "urn:salud:kb:salubrista-fuente-salud-publica-global",
    "urn:salud:kb:salubrista-fuente-publihealth-oxford-alias-p02": "urn:salud:kb:salubrista-fuente-salud-publica-global",
    "urn:salud:kb:salubrista-fuente-publihealth-oxford-alias-p03": "urn:salud:kb:salubrista-fuente-salud-publica-global",
    "urn:salud:kb:salubrista-fuente-publihealth-oxford-alias-p04": "urn:salud:kb:salubrista-fuente-salud-publica-global",
    "urn:salud:kb:salubrista-fuente-publihealth-oxford-alias-p05": "urn:salud:kb:salubrista-fuente-salud-publica-global",
    "urn:salud:kb:salubrista-fuente-publihealth-oxford-alias-p06": "urn:salud:kb:salubrista-fuente-salud-publica-global",
}
RETIRED_KB_URNS = frozenset({
    "urn:kora:kb:agentfile-spec",
    "urn:kora:kb:skill-overlay-spec",
})
LEGACY_BOOTSTRAP_URN_PATTERN = re.compile(
    r"^urn:[a-z0-9-]+:agent-bootstrap:[A-Za-z0-9._-]+:[0-9]+\.[0-9]+\.[0-9]+$"
)
SEMANTIC_TOOL_DOC_MARKERS = (
    "**Firma:**",
    "**Cuando usar:**",
    "**Cuando NO usar:**",
    "Firma:",
    "Cuando usar:",
    "Cuando NO usar:",
)
MISSING_SKILL_SPECS = {}  # Only for newly-scaffolded workspaces; never for pre-existing ones


def staging_dir(kind: str, stage: str) -> Path:
    """Resuelve el directorio de staging por tipo y etapa.

    kind: 'agents' | 'skills' | 'knowledge'
    stage: 'INBOX' | 'REVIEW'
    """
    roots = {
        "agents": FRAGUA_ROOT,
        "skills": TALLER_ROOT,
        "knowledge": SCRIPTORIUM_ROOT,
    }
    if kind not in roots:
        raise ValueError(f"Unknown staging kind: {kind}")
    if stage not in STAGING_STAGES:
        raise ValueError(f"Unknown staging stage: {stage}")
    return roots[kind] / stage


def is_in_staging(path: Path) -> bool:
    """True si el path vive dentro de algun staging area (_FRAGUA/_TALLER/_SCRIPTORIUM)."""
    try:
        resolved = path.resolve()
    except OSError:
        return False
    for staging_root in STAGING_ROOTS:
        if staging_root.exists() and (resolved == staging_root.resolve() or staging_root.resolve() in resolved.parents):
            return True
    return False


def resolve_logical_repo_path(path_str: str) -> Path:
    return KORA_ROOT / Path(path_str)


def physical_to_logical_repo_path(path: Path) -> Path:
    resolved = path.resolve()
    return resolved.relative_to(KORA_ROOT.resolve())
