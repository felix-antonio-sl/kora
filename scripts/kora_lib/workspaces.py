import re

from .artifacts import load_yaml_safe
from .config import (
    AGENT_ROUTE_PATTERN,
    BOOTSTRAP_MANIFEST_TYPES,
    COHORT_NAMESPACE_GROUPS,
    COHORT_WORKSPACE_OVERRIDES,
    CM_REF_PATTERN,
    KORA_ROOT,
    SKILL_MANIFEST_TYPE,
    SKILL_REQUIRED_HEADINGS,
    TOOL_IDENTIFIER_PATTERN,
)

WORKSPACE_REF_PATTERN = re.compile(r"\b([a-z0-9-]+/[A-Za-z0-9_-]+)\b")
EXPLICIT_ID_PATTERN_TEMPLATE = r"\bID:\s*{fragment}\b"
TABLE_ANCHOR_PATTERN_TEMPLATE = r"^\|\s*{fragment}\s*\|"
HTML_ANCHOR_PATTERN_TEMPLATE = r"""<(?:a|span)\b[^>]*\b(?:id|name)=["']{fragment}["'][^>]*>"""
WORKSPACE_BOOTSTRAP_URN_PATTERN = re.compile(
    r"^urn:([a-z0-9-]+):agent-bootstrap:([a-z0-9._-]+)-agents:[0-9]+\.[0-9]+\.[0-9]+$"
)


def workspace_in_cohort(workspace_dir, cohort=None):
    if not cohort:
        return True
    namespace = workspace_dir.parent.name
    name = workspace_dir.name
    if cohort in COHORT_NAMESPACE_GROUPS:
        if namespace not in COHORT_NAMESPACE_GROUPS[cohort]:
            return False
        overrides = COHORT_WORKSPACE_OVERRIDES.get(cohort)
        if overrides is None:
            return True
        return name in overrides
    return False


def iter_agent_workspaces(cohort=None):
    agents_root = KORA_ROOT / "agents"
    if not agents_root.exists():
        return []

    workspaces = []
    for namespace_dir in sorted(agents_root.iterdir()):
        if not namespace_dir.is_dir() or namespace_dir.name.startswith("."):
            continue
        for workspace_dir in sorted(namespace_dir.iterdir()):
            if (
                workspace_dir.is_dir()
                and not workspace_dir.name.startswith(".")
                and workspace_in_cohort(workspace_dir, cohort=cohort)
            ):
                workspaces.append(workspace_dir)
    return workspaces


def get_workspace_missing_files(workspace_dir, required_files):
    return [name for name in required_files if not (workspace_dir / name).exists()]


def slugify_heading(text):
    slug = text.strip().lower()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"\s+", "-", slug)
    return slug


def iter_markdown_headings(content):
    in_code_block = False
    for line in content.splitlines():
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code_block = not in_code_block
            continue
        if in_code_block or not stripped.startswith("#"):
            continue
        level = len(stripped) - len(stripped.lstrip("#"))
        yield level, stripped[level:].strip()


def workspace_ref_exists(workspace_ref):
    try:
        namespace, name = workspace_ref.split("/", 1)
    except ValueError:
        return False
    return (KORA_ROOT / "agents" / namespace / name).is_dir()


def extract_workspace_tokens(text, self_workspace=None):
    refs = set()
    for ref in WORKSPACE_REF_PATTERN.findall(text):
        if ref == self_workspace:
            continue
        if workspace_ref_exists(ref):
            refs.add(ref)
    return refs


def fragment_exists(file_path, fragment):
    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception:
        return False

    if file_path.suffix != ".md":
        return False

    target = slugify_heading(fragment)
    for _level, heading in iter_markdown_headings(content):
        if slugify_heading(heading) == target:
            return True

    explicit_id_pattern = re.compile(EXPLICIT_ID_PATTERN_TEMPLATE.format(fragment=re.escape(fragment)))
    table_anchor_pattern = re.compile(
        TABLE_ANCHOR_PATTERN_TEMPLATE.format(fragment=re.escape(fragment)),
        re.MULTILINE,
    )
    html_anchor_pattern = re.compile(
        HTML_ANCHOR_PATTERN_TEMPLATE.format(fragment=re.escape(fragment)),
        re.IGNORECASE,
    )

    if explicit_id_pattern.search(content):
        return True
    if table_anchor_pattern.search(content):
        return True
    if html_anchor_pattern.search(content):
        return True
    return False


def extract_declared_tool_headings(tools_path):
    try:
        content = tools_path.read_text(encoding="utf-8")
    except Exception:
        return [], [], []

    headings = []
    in_code_block = False
    for line in content.splitlines():
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue
        if stripped.startswith("## "):
            headings.append(stripped[3:].strip())

    valid = [heading for heading in headings if TOOL_IDENTIFIER_PATTERN.fullmatch(heading)]
    invalid = [heading for heading in headings if heading not in valid]
    return headings, valid, invalid


def extract_cm_refs(agents_path):
    try:
        content = agents_path.read_text(encoding="utf-8")
    except Exception:
        return set()
    return set(CM_REF_PATTERN.findall(content))


def extract_workspace_refs(agents_path):
    try:
        content = agents_path.read_text(encoding="utf-8")
    except Exception:
        return set()
    return set(AGENT_ROUTE_PATTERN.findall(content))


def iter_skill_entrypoints(skill_dir):
    if not skill_dir.exists():
        return []
    return sorted(skill_dir.glob("CM-*.md")) + sorted(skill_dir.glob("CM-*/SKILL.md"))


def extract_skill_symbols(skill_dir):
    if not skill_dir.exists():
        return set()
    return {path.stem for path in skill_dir.glob("CM-*.md")} | {
        path.parent.name for path in skill_dir.glob("CM-*/SKILL.md")
    }


def iter_skill_bundle_dirs(skill_dir):
    if not skill_dir.exists():
        return []
    return sorted(path for path in skill_dir.glob("CM-*") if path.is_dir())


def validate_skill_bundle_dir(bundle_dir):
    failures = []
    entrypoint = bundle_dir / "SKILL.md"
    if not entrypoint.exists():
        failures.append(f"extended skill bundle '{bundle_dir.name}' missing entrypoint 'SKILL.md'")
        return failures
    allowed_children = {"SKILL.md", "scripts", "references", "assets"}
    extra_children = sorted(path.name for path in bundle_dir.iterdir() if path.name not in allowed_children)
    if extra_children:
        failures.append(
            f"extended skill bundle '{bundle_dir.name}' contains unsupported children {extra_children}"
        )
    return failures


def find_skill_materialization_conflicts(skill_dir):
    if not skill_dir.exists():
        return []
    degenerate = {path.stem for path in skill_dir.glob("CM-*.md")}
    extended = {path.parent.name for path in skill_dir.glob("CM-*/SKILL.md")}
    return sorted(degenerate & extended)


def validate_skill_file(skill_path):
    failures = []
    content = ""
    try:
        content = skill_path.read_text(encoding="utf-8")
    except Exception as exc:
        return [f"unreadable skill file: {exc}"]

    doc, err = load_yaml_safe(skill_path)
    if not doc:
        failures.append(f"invalid frontmatter: {err}")
        return failures

    urn = doc.get("_manifest", {}).get("urn", "")
    manifest_type = doc.get("_manifest", {}).get("type", "")
    if urn and ":skill:" not in urn:
        failures.append(f"skill identity must use ':skill:' URN, found '{urn}'")
    if manifest_type and manifest_type != SKILL_MANIFEST_TYPE:
        failures.append(f"skill manifest type must be '{SKILL_MANIFEST_TYPE}', found '{manifest_type}'")

    headings = {f"## {heading}" for level, heading in iter_markdown_headings(content) if level == 2}
    for heading in SKILL_REQUIRED_HEADINGS:
        if heading not in headings:
            failures.append(f"missing required heading '{heading}'")
    return failures


def expected_bootstrap_manifest_type(path):
    return BOOTSTRAP_MANIFEST_TYPES.get(path.name)


def workspace_exists_from_urn(urn):
    base_urn = urn.partition("#")[0]
    match = WORKSPACE_BOOTSTRAP_URN_PATTERN.fullmatch(base_urn)
    if not match:
        return False
    namespace, workspace_name = match.groups()
    return (KORA_ROOT / "agents" / namespace / workspace_name).is_dir()
