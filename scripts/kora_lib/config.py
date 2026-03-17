from pathlib import Path
import re


KORA_ROOT = Path(__file__).resolve().parents[2]
AGENTS_ROOT = KORA_ROOT / "AGENTS" if (KORA_ROOT / "AGENTS").exists() else KORA_ROOT / "agents"
KNOWLEDGE_ROOT = KORA_ROOT / "KNOWLEDGE" if (KORA_ROOT / "KNOWLEDGE").exists() else KORA_ROOT / "knowledge"
OPERATIONS_ROOT_NAME = "OPERATIONS"
OPERATIONS_ROOT = KORA_ROOT / OPERATIONS_ROOT_NAME
CATALOG_PATH = KORA_ROOT / "catalog" / "catalog_master_kora.yml"
GENERATED_DOCS_DIR = KORA_ROOT / "docs" / "generated"
BOOTSTRAP_SCHEMA_PATH = KORA_ROOT / "schemas" / "kora-agent-schema.json"
CONFIG_SCHEMA_PATH = KORA_ROOT / "schemas" / "kora-agent-config-schema.json"
AGENT_BOOTSTRAP_FILES = ("AGENTS.md", "SOUL.md", "USER.md", "TOOLS.md")
AGENT_REQUIRED_FILES = AGENT_BOOTSTRAP_FILES + ("config.json",)
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
    "scripts",
    "tests",
    "docs",
    "staging",
    "inbox",
    "source",
    "drafts",
    OPERATIONS_ROOT_NAME,
    ".claude",
    ".agent",
    ".venv",
    "__pycache__",
}
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
BROKEN_ROUTE_MAPPINGS = {
    "fxsl/coder": "dev/coder",
    "fxsl/dev": "dev/coder",
    "fxsl/pm": "dev/planner",
    "ops/tester": "ops/verificador",
}
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
    "kora/forgemaster",
    "kora/curator",
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
    "kora/forgemaster": {
        "status": "operating_core",
        "reason": "Nucleo operativo: disena, crea, valida y entrega handoff al custodio.",
    },
    "kora/curator": {
        "status": "operating_core",
        "reason": "Nucleo operativo: korafica, audita y entrega handoff al custodio.",
    },
    "kora/custodio": {
        "status": "operating_core",
        "reason": "Nucleo operativo: cierra salud, catalogo e ingesta del repo.",
    },
}
OPERATING_CORE_COHORTS = {
    "kora": (
        "kora/guardian",
        "kora/forgemaster",
        "kora/curator",
        "kora/custodio",
    ),
    "dev": (
        "dev/planner",
        "dev/coder",
        "dev/reviewer",
        "dev/sentinel",
    ),
    "ops": (
        "ops/orquestador-swarm",
        "ops/verificador",
        "ops/security",
    ),
    "domain_canary": (
        "gn/goreologo",
        "gn/digitrans",
    ),
}
SEMANTIC_TOOL_DOC_MARKERS = (
    "**Firma:**",
    "**Cuando usar:**",
    "**Cuando NO usar:**",
    "Firma:",
    "Cuando usar:",
    "Cuando NO usar:",
)
MISSING_SKILL_SPECS = {
    "AGENTS/kora/taskmaster": {
        "CM-CONTEXT-MANAGER": (
            "Mantiene coherencia de la conversacion y detecta cambios de hilo.",
            "estado_actual, mensaje_usuario",
            "context_shift, siguiente_estado",
        ),
        "CM-ISSUE-BUILDER": (
            "Construye un issue accionable con descripcion, alcance y criterios de aceptacion.",
            "solicitud_usuario",
            "issue_template",
        ),
        "CM-PRIORITY-MATRIX": (
            "Prioriza tareas segun impacto y urgencia.",
            "items",
            "items_priorizados",
        ),
        "CM-REQUEST-CLASSIFIER": (
            "Clasifica la intencion del usuario dentro del dominio de gestion de tareas.",
            "mensaje_usuario",
            "intent_classification",
        ),
        "CM-STATUS-REPORTER": (
            "Resume estado de backlog y ejecucion por columnas.",
            "scope",
            "status_report",
        ),
    },
    "AGENTS/salud/abogado-legislacion-medica": {
        "CM-CONSULTA-CLASSIFIER": (
            "Clasifica consultas legales en estatuto, derechos, procedimiento o materia especial.",
            "consulta_usuario",
            "clasificacion_consulta",
        ),
        "CM-MATERIA-ROUTER": (
            "Ruta materias especiales hacia la base normativa pertinente.",
            "consulta_clasificada",
            "ruta_normativa",
        ),
    },
    "AGENTS/fxsl/ingeniero-sistemas-composicional": {
        "CM-CONTEXT-ANALYZER": (
            "Analiza escala, perspectiva, rol y fase del sistema antes de modelar.",
            "solicitud_usuario",
            "contexto_sistemas",
        ),
    },
}


def operations_dir(name: str) -> Path:
    return OPERATIONS_ROOT / name


def resolve_operational_dir(name: str) -> Path:
    preferred = operations_dir(name)
    legacy = KORA_ROOT / name
    return preferred if preferred.exists() or not legacy.exists() else legacy


def resolve_logical_repo_path(path_str: str) -> Path:
    path = Path(path_str)
    if not path.parts:
        return KORA_ROOT
    root_name = path.parts[0]
    if root_name in {"inbox", "source", "drafts", "build"}:
        return resolve_operational_dir(root_name).joinpath(*path.parts[1:])
    return KORA_ROOT / path


def physical_to_logical_repo_path(path: Path) -> Path:
    resolved = path.resolve()
    for root_name in ("inbox", "source", "drafts", "build"):
        physical_root = operations_dir(root_name).resolve()
        legacy_root = (KORA_ROOT / root_name).resolve()
        for candidate in (physical_root, legacy_root):
            if resolved == candidate or candidate in resolved.parents:
                return Path(root_name) / resolved.relative_to(candidate)
    return resolved.relative_to(KORA_ROOT.resolve())
