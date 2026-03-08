import re

from .artifacts import load_yaml_safe
from .config import (
    AGENT_ROUTE_PATTERN,
    COHORT_NAMESPACE_GROUPS,
    COHORT_WORKSPACE_OVERRIDES,
    CM_REF_PATTERN,
    KORA_ROOT,
    SKILL_REQUIRED_HEADINGS,
    TOOL_IDENTIFIER_PATTERN,
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


def fragment_exists(file_path, fragment):
    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception:
        return False

    if fragment in content:
        return True

    if file_path.suffix != ".md":
        return False

    target = slugify_heading(fragment)
    for line in content.splitlines():
        stripped = line.strip()
        if stripped.startswith("#"):
            heading = stripped.lstrip("#").strip()
            if slugify_heading(heading) == target:
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
    if urn and ":skill:" not in urn:
        failures.append(f"skill identity must use ':skill:' URN, found '{urn}'")

    for heading in SKILL_REQUIRED_HEADINGS:
        if heading not in content:
            failures.append(f"missing required heading '{heading}'")
    return failures


def workspace_exists_from_urn(urn):
    parts = urn.split(":")
    return len(parts) == 4 and parts[2] == "agent" and (KORA_ROOT / "agents" / parts[1] / parts[3]).is_dir()
