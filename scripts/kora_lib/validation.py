import json
import re
import unicodedata
from collections import Counter
from functools import lru_cache
from pathlib import Path

from .artifacts import load_markdown_parts, load_yaml_safe
from .config import (
    AGENT_BOOTSTRAP_FILES,
    AGENT_REQUIRED_FILES,
    AGENTS_FORBIDDEN_PATTERNS,
    BOOTSTRAP_MANIFEST_TYPES,
    BOOTSTRAP_SCHEMA_PATH,
    CONFIG_SCHEMA_PATH,
    KB_PIPELINE_PATTERN,
    KORA_ROOT,
    LOW_LEVEL_RUNTIME_HINTS,
    SEMANTIC_TOOL_DOC_MARKERS,
    SKILL_RAW_COMMAND_PATTERNS,
    SEMANTIC_TURN_CONTROL_PATTERNS,
    SOUL_FORBIDDEN_PATTERNS,
    TOOL_IDENTIFIER_PATTERN,
    TRACES_TO_DOC_PATTERN,
    TRACES_TO_SECTION_PATTERN,
    USER_FORBIDDEN_PATTERNS,
)
from .workspaces import (
    extract_cm_refs,
    extract_declared_tool_headings,
    extract_workspace_refs,
    get_workspace_missing_files,
    iter_markdown_headings,
    iter_agent_workspaces,
    expected_bootstrap_manifest_type,
    validate_skill_file,
)


CANONICAL_AGENT_SECTION_PATTERNS = (
    ("## 1. FSM", re.compile(r"^1\.\s+fsm(?:\b|[\s(])")),
    ("## 2. Reglas Duras", re.compile(r"^2\.\s+reglas duras(?:\b|[\s(])")),
    ("## 3. Co-induccion", re.compile(r"^3\.\s+co-induccion(?:\b|[\s(])")),
    ("## 4. Contexto Multi-turno", re.compile(r"^4\.\s+contexto multi-turno(?:\b|[\s(])")),
    ("## 5. Wiring", re.compile(r"^5\.\s+wiring(?:\b|[\s(])")),
)
TRUNCATED_HEADING_PATTERN = re.compile(r"\.\.\.$|…$")
HTML_TAG_PATTERN = re.compile(r"<[A-Za-z][^>]*>")
OPAQUE_INTERNAL_REF_PATTERN = re.compile(r"\[->\s*([A-Z0-9-]{8,})\]\(#([^)]+)\)")
UNVERIFIABLE_REFERENCE_PATTERNS = (
    re.compile(r"\bkb_[a-z0-9_]+\.md\b"),
    re.compile(r"`[A-Z]{2,}(?:-[A-Z0-9]+){1,}`"),
    re.compile(r"\bGUIDE-STS-[A-Z0-9-]*\b"),
)
META_INTRO_HEADING_TITLES = {
    "introduccion",
    "introduccion general",
    "proposito",
    "proposito alcance y estructura del manual",
    "alcance",
    "estructura",
}
DEFAULT_MAX_LINES_PER_PRIMARY_CHUNK = 120
FAMILY_MAX_LINES_PER_PRIMARY_CHUNK = {
    "generic": 120,
    "normative": 80,
    "glossary": 60,
    "organigram": 90,
    "cq_catalog": 90,
    "inventory": 200,
    "omega": 120,
}


def validate_patterns(text, patterns, message_template):
    failures = []
    for pattern in patterns:
        for match in pattern.finditer(text):
            failures.append(message_template.format(match=match.group(0)))
    return failures


def validate_soul_semantics(text):
    return validate_patterns(
        text,
        SOUL_FORBIDDEN_PATTERNS,
        "SOUL contiene leakage de behavior/state-machine ('{match}')",
    )


def validate_user_semantics(text):
    return validate_patterns(
        text,
        USER_FORBIDDEN_PATTERNS,
        "USER contiene leakage de security o wiring ('{match}')",
    )


def validate_agents_semantics(text):
    return validate_patterns(
        text,
        AGENTS_FORBIDDEN_PATTERNS,
        "AGENTS contiene leakage de security/runtime ('{match}')",
    )


def validate_skill_purity(text):
    return validate_patterns(
        text,
        SEMANTIC_TURN_CONTROL_PATTERNS,
        "Skill contiene control conversacional no permitido ('{match}')",
    )


def validate_skill_tool_closure(text, valid_tool_names):
    failures = []
    for pattern, semantic_tool in SKILL_RAW_COMMAND_PATTERNS:
        if not pattern.search(text):
            continue
        if semantic_tool in valid_tool_names:
            failures.append(
                f"Skill describe plumbing crudo en vez de la tool semantica '{semantic_tool}'"
            )
        else:
            failures.append(
                f"Skill requiere la tool semantica '{semantic_tool}' pero no esta declarada en TOOLS.md"
            )
    return failures


def normalize_heading_token(text):
    normalized = unicodedata.normalize("NFKD", text)
    normalized = normalized.encode("ascii", "ignore").decode("ascii")
    return re.sub(r"\s+", " ", normalized.strip().lower())


def collect_markdown_headings(text, min_level=1, max_level=6):
    return [
        (level, heading)
        for level, heading in iter_markdown_headings(text)
        if min_level <= level <= max_level
    ]


def find_truncated_markdown_headings(text):
    return [
        heading
        for _level, heading in collect_markdown_headings(text)
        if TRUNCATED_HEADING_PATTERN.search(heading.strip())
    ]


def find_field_like_markdown_headings(text, banned_titles):
    banned = {normalize_heading_token(title) for title in banned_titles}
    return [
        heading
        for _level, heading in collect_markdown_headings(text)
        if normalize_heading_token(heading) in banned
    ]


def find_html_fragments(text):
    return [match.group(0) for match in HTML_TAG_PATTERN.finditer(text)]


def find_opaque_internal_refs(text):
    return [match.group(1) for match in OPAQUE_INTERNAL_REF_PATTERN.finditer(text)]


def find_unverifiable_external_references(text):
    findings = []
    for pattern in UNVERIFIABLE_REFERENCE_PATTERNS:
        findings.extend(match.group(0) for match in pattern.finditer(text))
    return findings


def find_meta_intro_headings(text):
    headings = collect_markdown_headings(text, min_level=2, max_level=4)
    early_headings = headings[:6]
    return [
        heading
        for _level, heading in early_headings
        if normalize_heading_token(heading) in META_INTRO_HEADING_TITLES
    ]


def find_empty_primary_wrapper_headings(text):
    lines = text.splitlines()
    findings = []
    for index, line in enumerate(lines):
        if not line.startswith("## "):
            continue
        heading = line[3:].strip()
        cursor = index + 1
        while cursor < len(lines) and not lines[cursor].strip():
            cursor += 1
        if cursor < len(lines) and lines[cursor].startswith("## "):
            findings.append(heading)
    return findings


def find_oversized_primary_chunks(text, max_lines=DEFAULT_MAX_LINES_PER_PRIMARY_CHUNK):
    lines = text.splitlines()
    starts = [index for index, line in enumerate(lines) if line.startswith("## ")]
    findings = []
    for pos, start in enumerate(starts):
        end = starts[pos + 1] if pos + 1 < len(starts) else len(lines)
        size = end - start
        if size > max_lines:
            findings.append((lines[start][3:].strip(), size))
    return findings


def suggest_primary_chunk_splits(text, max_lines=DEFAULT_MAX_LINES_PER_PRIMARY_CHUNK):
    lines = text.splitlines()
    starts = [index for index, line in enumerate(lines) if line.startswith("## ")]
    suggestions = []
    for pos, start in enumerate(starts):
        end = starts[pos + 1] if pos + 1 < len(starts) else len(lines)
        size = end - start
        if size <= max_lines:
            continue
        child_h3 = [line[3:].strip() for line in lines[start + 1 : end] if line.startswith("### ")]
        if child_h3:
            suggestions.append((lines[start][3:].strip(), child_h3))
    return suggestions


def resolve_document_family(frontmatter):
    if not isinstance(frontmatter, dict):
        return "generic"
    extensions = frontmatter.get("extensions", {})
    if isinstance(extensions, dict):
        kora_ext = extensions.get("kora")
        if isinstance(kora_ext, dict) and kora_ext.get("family"):
            return str(kora_ext["family"])
        gn_ext = extensions.get("gn")
        if isinstance(gn_ext, dict) and gn_ext.get("document_family"):
            return str(gn_ext["document_family"])
    return "generic"


def resolve_max_lines_per_h2(frontmatter, explicit=None):
    if explicit is not None:
        return explicit
    family = resolve_document_family(frontmatter)
    return FAMILY_MAX_LINES_PER_PRIMARY_CHUNK.get(family, DEFAULT_MAX_LINES_PER_PRIMARY_CHUNK)


def should_enforce_published_kora_markdown(frontmatter, path):
    if not isinstance(frontmatter, dict):
        return False
    if path.suffix != ".md":
        return False
    if frontmatter.get("status") != "published":
        return False
    urn = frontmatter.get("_manifest", {}).get("urn", "")
    return isinstance(urn, str) and ":kb:" in urn


def strip_html_anchor_lines(text):
    return "\n".join(
        line for line in text.splitlines() if not re.fullmatch(r'\s*<a id="[^"]+"></a>\s*', line)
    )


def replace_html_breaks(text):
    return text.replace("<br>", "; ")


def build_heading_slug_map(text):
    mapping = {}
    for _level, heading in collect_markdown_headings(text):
        mapping[slugify_heading(heading)] = heading
    return mapping


def slugify_heading(text):
    slug = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    slug = slug.lower()
    slug = re.sub(r"[^a-z0-9\s-]", "", slug)
    slug = re.sub(r"\s+", "-", slug.strip())
    slug = re.sub(r"-+", "-", slug)
    return slug.strip("-")


def semanticize_opaque_internal_refs(text):
    slug_map = build_heading_slug_map(text)

    def replace(match):
        label, target = match.group(1), match.group(2)
        if not re.fullmatch(r"[A-Z0-9-]{8,}", label):
            return match.group(0)
        semantic = slug_map.get(target)
        if not semantic:
            return match.group(0)
        return f"[-> {semantic}](#{target})"

    return OPAQUE_INTERNAL_REF_PATTERN.sub(replace, text)


def remove_leading_meta_intro_sections(text):
    lines = text.splitlines()
    headings = [(index, line[3:].strip()) for index, line in enumerate(lines) if line.startswith("## ")]
    to_remove = set()
    cursor = 0
    while cursor < len(headings):
        start, title = headings[cursor]
        normalized = normalize_heading_token(title).replace("-", " ")
        if normalized not in META_INTRO_HEADING_TITLES:
            break
        end = headings[cursor + 1][0] if cursor + 1 < len(headings) else len(lines)
        to_remove.update(range(start, end))
        cursor += 1
    if not to_remove:
        return text
    kept = [line for index, line in enumerate(lines) if index not in to_remove]
    return "\n".join(kept)


def remove_empty_primary_wrappers_body(text):
    lines = text.splitlines()
    out = []
    index = 0
    while index < len(lines):
        line = lines[index]
        if line.startswith("## "):
            cursor = index + 1
            while cursor < len(lines) and not lines[cursor].strip():
                cursor += 1
            if cursor < len(lines) and lines[cursor].startswith("## "):
                index += 1
                continue
        out.append(line)
        index += 1
    return "\n".join(out)


def promote_nested_headings_in_oversized_chunks(text, max_lines):
    lines = text.splitlines()
    starts = [index for index, line in enumerate(lines) if line.startswith("## ")]
    oversized_ranges = []
    for pos, start in enumerate(starts):
        end = starts[pos + 1] if pos + 1 < len(starts) else len(lines)
        if end - start > max_lines:
            oversized_ranges.append((start, end))
    if not oversized_ranges:
        return text

    def in_oversized(index):
        return any(start < index < end for start, end in oversized_ranges)

    out = []
    for index, line in enumerate(lines):
        if in_oversized(index) and line.startswith("### "):
            out.append("## " + line[4:])
        elif in_oversized(index) and line.startswith("#### "):
            out.append("### " + line[5:])
        else:
            out.append(line)
    return "\n".join(out)


def normalize_blank_lines(text):
    out = []
    previous_blank = False
    for line in text.splitlines():
        blank = not line.strip()
        if blank and previous_blank:
            continue
        out.append(line)
        previous_blank = blank
    return "\n".join(out).strip() + "\n"


def auto_fix_published_kora_markdown_parts(frontmatter, body, max_lines_per_h2=None):
    max_lines = resolve_max_lines_per_h2(frontmatter, explicit=max_lines_per_h2)
    current = body
    for _ in range(4):
        updated = current
        updated = strip_html_anchor_lines(updated)
        updated = replace_html_breaks(updated)
        updated = semanticize_opaque_internal_refs(updated)
        updated = remove_leading_meta_intro_sections(updated)
        updated = remove_empty_primary_wrappers_body(updated)
        updated = promote_nested_headings_in_oversized_chunks(updated, max_lines)
        updated = remove_empty_primary_wrappers_body(updated)
        updated = normalize_blank_lines(updated)
        if updated == current:
            break
        current = updated
    return current


def lint_published_kora_markdown_parts(frontmatter, body, max_lines_per_h2=None):
    max_lines = resolve_max_lines_per_h2(frontmatter, explicit=max_lines_per_h2)
    failures = []

    for heading in find_meta_intro_headings(body):
        failures.append(f"meta_intro_heading: heading introductorio no permitido '{heading}'")

    for fragment in find_html_fragments(body):
        failures.append(f"html_raw: HTML crudo no permitido '{fragment}'")

    for ref in find_opaque_internal_refs(body):
        failures.append(f"opaque_internal_ref: referencia interna usa id opaco '{ref}'")

    for ref in find_unverifiable_external_references(body):
        failures.append(f"unverifiable_ref: referencia no comprobable '{ref}'")

    for heading in find_empty_primary_wrapper_headings(body):
        failures.append(f"empty_primary_wrapper: '## {heading}' solo envuelve otros headings")

    split_suggestions = dict(suggest_primary_chunk_splits(body, max_lines=max_lines))
    for heading, size in find_oversized_primary_chunks(body, max_lines=max_lines):
        suggestion = ""
        if heading in split_suggestions:
            promoted = ", ".join(split_suggestions[heading][:4])
            suffix = "..." if len(split_suggestions[heading]) > 4 else ""
            suggestion = f"; split sugerido via promotion de ###: {promoted}{suffix}"
        failures.append(
            f"oversized_primary_chunk: '## {heading}' ocupa {size} lineas (max {max_lines}){suggestion}"
        )

    banned_field_headings = {"titulo", "path", "artefactos", "contenido", "asunto", "tipo", "status", "source_id"}
    for heading in find_field_like_markdown_headings(body, banned_field_headings):
        failures.append(f"field_like_heading: heading serializado no permitido '{heading}'")

    for heading in find_truncated_markdown_headings(body):
        failures.append(f"truncated_heading: heading truncado '{heading}'")

    return failures


def lint_kora_markdown_parts(frontmatter, body, max_lines_per_h2=None):
    urn = frontmatter.get("_manifest", {}).get("urn", "") if isinstance(frontmatter, dict) else ""
    if not (isinstance(urn, str) and ":kb:" in urn):
        return []
    return lint_published_kora_markdown_parts(frontmatter, body, max_lines_per_h2=max_lines_per_h2)


def lint_published_kora_markdown(path, max_lines_per_h2=None):
    frontmatter, body = load_markdown_parts(path)
    if not should_enforce_published_kora_markdown(frontmatter, path):
        return []
    return lint_published_kora_markdown_parts(frontmatter, body, max_lines_per_h2=max_lines_per_h2)


def iter_markdown_lint_targets(paths):
    for raw_path in paths:
        path = Path(raw_path).expanduser().resolve()
        if path.is_file() and path.suffix == ".md":
            yield path
            continue
        if path.is_dir():
            for child in sorted(path.rglob("*.md")):
                yield child


def lint_markdown_paths(paths, max_lines_per_h2=None, emit=True):
    issue_counts = Counter()
    issues = []

    for path in iter_markdown_lint_targets(paths):
        rel_path = path.relative_to(KORA_ROOT) if KORA_ROOT in path.parents or path == KORA_ROOT else path
        for failure in lint_published_kora_markdown(path, max_lines_per_h2=max_lines_per_h2):
            category = failure.split(":", 1)[0]
            issue_counts[category] += 1
            issues.append((rel_path, failure))
            if emit:
                print(f"[FAIL] {rel_path} - {failure}")

    if emit:
        total = sum(issue_counts.values())
        print(f"Markdown lint complete. Issues: {total}")
        if issue_counts:
            print("Issue breakdown:")
            for name, count in sorted(issue_counts.items()):
                print(f"  {name}: {count}")

    return {
        "issues": issues,
        "issue_counts": dict(sorted(issue_counts.items())),
        "ok": not issues,
    }


def validate_agents_canonical_structure(text):
    headings = [normalize_heading_token(heading) for level, heading in iter_markdown_headings(text) if level == 2]
    failures = []
    positions = {}

    for required_label, pattern in CANONICAL_AGENT_SECTION_PATTERNS:
        matching_positions = [index for index, heading in enumerate(headings) if pattern.match(heading)]
        if not matching_positions:
            failures.append(f"AGENTS.md carece de seccion canonica '{required_label}'")
            continue
        if len(matching_positions) > 1:
            failures.append(f"AGENTS.md duplica seccion canonica '{required_label}'")
            continue
        positions[required_label] = matching_positions[0]

    ordered_positions = [positions[label] for label, _pattern in CANONICAL_AGENT_SECTION_PATTERNS if label in positions]
    if len(ordered_positions) == len(CANONICAL_AGENT_SECTION_PATTERNS) and ordered_positions != sorted(ordered_positions):
        failures.append("AGENTS.md viola el orden canonico FSM -> Reglas Duras -> Co-induccion -> Contexto Multi-turno -> Wiring")

    return failures


def split_tool_sections(content):
    sections = {}
    current_heading = None
    current_lines = []
    in_code_block = False

    for line in content.splitlines():
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code_block = not in_code_block
            continue
        if not in_code_block and stripped.startswith("## "):
            if current_heading is not None:
                sections[current_heading] = "\n".join(current_lines).strip()
            current_heading = stripped[3:].strip()
            current_lines = []
            continue
        if current_heading is not None and not in_code_block:
            current_lines.append(line)

    if current_heading is not None:
        sections[current_heading] = "\n".join(current_lines).strip()
    return sections


def validate_tools_semantics(content, valid_tool_names):
    failures = []
    sections = split_tool_sections(content)
    for tool_name in valid_tool_names:
        if tool_name in LOW_LEVEL_RUNTIME_HINTS:
            failures.append(f"tool '{tool_name}' usa un permiso runtime crudo como interfaz semantica")
        section_body = sections.get(tool_name, "")
        if not any(marker in section_body for marker in SEMANTIC_TOOL_DOC_MARKERS):
            failures.append(f"tool '{tool_name}' carece de documentacion semantica canonica")
    return failures


def normalize_pipeline_edge(source, target):
    return (source.lower().strip(), target.lower().strip())


def extract_kb_pipeline_edges(text):
    return {normalize_pipeline_edge(source, target) for source, target in KB_PIPELINE_PATTERN.findall(text)}


def validate_kb_pipeline_consistency(texts):
    combined = "\n".join(texts)
    edges = extract_kb_pipeline_edges(combined)
    failures = []
    forbidden = {
        ("catalog", "kb_route"),
        ("catalog_resolve", "kb_route"),
        ("catalog", "catalog_resolve"),
    }
    for edge in sorted(edges):
        if edge in forbidden:
            failures.append(f"pipeline KB incompatible detectado: {edge[0]} -> {edge[1]}")
    return failures


@lru_cache(maxsize=1)
def build_formal_trace_targets():
    targets = {}
    formal_root = KORA_ROOT / "knowledge" / "kora" / "categorical-foundations"
    for path in sorted(formal_root.glob("*.md")):
        doc, _ = load_yaml_safe(path)
        urn = doc.get("_manifest", {}).get("urn") if isinstance(doc, dict) else None
        prefix = path.name.split("-", 1)[0]
        if urn and re.fullmatch(r"[0-9]{2}", prefix):
            targets[prefix] = {
                "urn": urn,
                "path": path,
            }
    return targets


def formal_section_exists(path, section):
    heading_pattern = re.compile(rf"^#+\s+{re.escape(section)}(?:\b|[ .:-])")
    for line in path.read_text(encoding="utf-8").splitlines():
        if heading_pattern.match(line.strip()):
            return True
    return False


def validate_traces_semantics(path, text):
    failures = []
    if "Traces to:" not in text:
        return failures

    for line in text.splitlines():
        if not line.strip().startswith("Traces to:"):
            continue
        if "knowledge/fxsl/cat" in line or "urn:fxsl:" in line:
            failures.append("Traces to referencia corpus FXSL auxiliar en vez de la formal layer oficial")
        doc_refs = TRACES_TO_DOC_PATTERN.findall(line)
        section_refs = TRACES_TO_SECTION_PATTERN.findall(line)
        if doc_refs and not section_refs:
            failures.append("Traces to carece de ancla de seccion formal")
            continue
        if len(doc_refs) != len(section_refs):
            failures.append("Traces to mezcla documentos formales con referencias sin ancla")
        for doc_id, section in section_refs:
            target = build_formal_trace_targets().get(doc_id)
            if not target:
                failures.append(f"Traces to apunta a formal/{doc_id} inexistente")
                continue
            if not formal_section_exists(target["path"], section):
                failures.append(f"Traces to apunta a formal/{doc_id} §{section} inexistente")
    return failures


def validate_config_semantics(config_data, valid_tool_names):
    failures = []
    tools_allow = set(config_data.get("tools", {}).get("allow", []))
    tools_deny = set(config_data.get("tools", {}).get("deny", []))
    runtime_allow = set(config_data.get("runtime_capabilities", {}).get("allow", []))
    runtime_deny = set(config_data.get("runtime_capabilities", {}).get("deny", []))
    semantic_set = set(valid_tool_names) | tools_allow

    overlap = sorted((runtime_allow | runtime_deny) & semantic_set)
    if overlap:
        failures.append(f"runtime_capabilities reintroduce interfaz semantica {overlap}")

    invalid_deny = sorted(item for item in tools_deny if item not in semantic_set)
    if invalid_deny:
        failures.append(f"tools.deny contiene permisos crudos o tools no semanticas {invalid_deny}")

    raw_tools = sorted(item for item in tools_allow if item in LOW_LEVEL_RUNTIME_HINTS or not TOOL_IDENTIFIER_PATTERN.fullmatch(item))
    if raw_tools:
        failures.append(f"tools.allow contiene permisos runtime crudos {raw_tools}")

    return failures


def validate_workspace_semantics(workspace_dir, config_data, valid_tool_names):
    failures = []

    soul_path = workspace_dir / "SOUL.md"
    user_path = workspace_dir / "USER.md"
    agents_path = workspace_dir / "AGENTS.md"
    tools_path = workspace_dir / "TOOLS.md"

    if soul_path.exists():
        failures.extend((f"SOUL: {item}" for item in validate_soul_semantics(soul_path.read_text(encoding="utf-8"))))
    if user_path.exists():
        failures.extend((f"USER: {item}" for item in validate_user_semantics(user_path.read_text(encoding="utf-8"))))
    if agents_path.exists():
        failures.extend((f"AGENTS: {item}" for item in validate_agents_semantics(agents_path.read_text(encoding="utf-8"))))
    if tools_path.exists():
        tools_text = tools_path.read_text(encoding="utf-8")
        failures.extend((f"TOOLS: {item}" for item in validate_tools_semantics(tools_text, valid_tool_names)))
    if config_data is not None:
        failures.extend((f"CONFIG: {item}" for item in validate_config_semantics(config_data, valid_tool_names)))

    kb_texts = []
    for path in (agents_path, tools_path):
        if path.exists():
            kb_texts.append(path.read_text(encoding="utf-8"))
    concept_explainer = workspace_dir / "skills" / "CM-CONCEPT-EXPLAINER.md"
    if concept_explainer.exists():
        kb_texts.append(concept_explainer.read_text(encoding="utf-8"))
    failures.extend((f"KB: {item}" for item in validate_kb_pipeline_consistency(kb_texts)))

    return failures


def validate_workspaces(profile="transitional", cohort=None, emit=True):
    if emit:
        print(f"Validating KORA agent workspaces against schema + semantic invariants ({profile})...")
    try:
        import jsonschema
    except ImportError:
        if emit:
            print("Error: 'jsonschema' module is required for validation. Run 'pip install jsonschema'.")
        raise SystemExit(1)

    schema, _ = load_yaml_safe(BOOTSTRAP_SCHEMA_PATH)
    if not schema:
        if emit:
            print(f"Error: Could not load schema from {BOOTSTRAP_SCHEMA_PATH}")
        raise SystemExit(1)

    config_schema, _ = load_yaml_safe(CONFIG_SCHEMA_PATH)
    if not config_schema:
        if emit:
            print(f"Error: Could not load schema from {CONFIG_SCHEMA_PATH}")
        raise SystemExit(1)

    workspace_valid = 0
    workspace_invalid = 0
    bootstrap_validated = 0
    global_failures = 0
    issue_counts = Counter()
    issues = []

    def report_issue(path, category, message, workspace=None):
        entry = {
            "path": str(path),
            "workspace": str(workspace) if workspace else None,
            "category": category,
            "message": message,
        }
        issues.append(entry)
        if emit:
            print(f"[FAIL] {path} - {message}")

    for workspace_dir in iter_agent_workspaces(cohort=cohort):
        rel_workspace = workspace_dir.relative_to(KORA_ROOT)
        workspace_ok = True
        missing_files = get_workspace_missing_files(workspace_dir, AGENT_REQUIRED_FILES)
        if missing_files:
            report_issue(rel_workspace, "missing_files", f"missing required files: {', '.join(missing_files)}", workspace=rel_workspace)
            issue_counts["missing_files"] += 1
            workspace_ok = False

        config_path = workspace_dir / "config.json"
        config_data = None
        try:
            with open(config_path, "r", encoding="utf-8") as handle:
                config_data = json.load(handle)
        except Exception as exc:
            report_issue(config_path.relative_to(KORA_ROOT), "invalid_json", f"invalid JSON: {exc}", workspace=rel_workspace)
            issue_counts["invalid_json"] += 1
            workspace_ok = False

        if config_data is not None and profile != "legacy":
            try:
                jsonschema.validate(instance=config_data, schema=config_schema)
            except jsonschema.exceptions.ValidationError as exc:
                report_issue(config_path.relative_to(KORA_ROOT), "config_schema", exc.message, workspace=rel_workspace)
                issue_counts["config_schema"] += 1
                workspace_ok = False

        for bootstrap_file in AGENT_BOOTSTRAP_FILES:
            agent_path = workspace_dir / bootstrap_file
            if not agent_path.exists():
                continue
            agent_data, err = load_yaml_safe(agent_path)
            if not agent_data:
                report_issue(agent_path.relative_to(KORA_ROOT), "bootstrap_parse", f"Could not parse YAML. Error: {err}", workspace=rel_workspace)
                issue_counts["bootstrap_parse"] += 1
                workspace_ok = False
                continue

            try:
                jsonschema.validate(instance=agent_data, schema=schema)
                bootstrap_validated += 1
            except jsonschema.exceptions.ValidationError as exc:
                report_issue(agent_path.relative_to(KORA_ROOT), "bootstrap_schema", exc.message, workspace=rel_workspace)
                issue_counts["bootstrap_schema"] += 1
                workspace_ok = False

            expected_type = expected_bootstrap_manifest_type(agent_path)
            actual_type = agent_data.get("_manifest", {}).get("type") if isinstance(agent_data, dict) else None
            if expected_type and actual_type != expected_type:
                report_issue(
                    agent_path.relative_to(KORA_ROOT),
                    "bootstrap_manifest_type",
                    f"_manifest.type '{actual_type}' != '{expected_type}'",
                    workspace=rel_workspace,
                )
                issue_counts["bootstrap_manifest_type"] += 1
                workspace_ok = False

        tools_path = workspace_dir / "TOOLS.md"
        valid_tool_names = []
        if tools_path.exists():
            tools_text = tools_path.read_text(encoding="utf-8")
            _, valid_tool_names, invalid_tool_names = extract_declared_tool_headings(tools_path)
            if profile != "legacy":
                for invalid_name in invalid_tool_names:
                    report_issue(
                        tools_path.relative_to(KORA_ROOT),
                        "tool_identifier",
                        f"invalid tool identifier '{invalid_name}'",
                        workspace=rel_workspace,
                    )
                    issue_counts["tool_identifier"] += 1
                    workspace_ok = False
                for failure in validate_traces_semantics(tools_path, tools_text):
                    report_issue(tools_path.relative_to(KORA_ROOT), "trace_semantics", failure, workspace=rel_workspace)
                    issue_counts["trace_semantics"] += 1
                    workspace_ok = False

        declared_allow = []
        if config_data is not None:
            declared_allow = config_data.get("tools", {}).get("allow", [])
        if profile != "legacy" and (valid_tool_names or declared_allow):
            if set(valid_tool_names) != set(declared_allow):
                report_issue(
                    rel_workspace,
                    "tool_allow_mismatch",
                    f"TOOLS.md headings {sorted(valid_tool_names)} != config.json.tools.allow {sorted(declared_allow)}",
                    workspace=rel_workspace,
                )
                issue_counts["tool_allow_mismatch"] += 1
                workspace_ok = False

        agents_path = workspace_dir / "AGENTS.md"
        skill_dir = workspace_dir / "skills"
        skill_names = {path.stem for path in skill_dir.glob("*.md")} if skill_dir.exists() else set()
        if profile != "legacy":
            if agents_path.exists():
                agents_text = agents_path.read_text(encoding="utf-8")
                for failure in validate_agents_canonical_structure(agents_text):
                    report_issue(agents_path.relative_to(KORA_ROOT), "agents_grammar", failure, workspace=rel_workspace)
                    issue_counts["agents_grammar"] += 1
                    workspace_ok = False
                for failure in validate_traces_semantics(agents_path, agents_text):
                    report_issue(agents_path.relative_to(KORA_ROOT), "trace_semantics", failure, workspace=rel_workspace)
                    issue_counts["trace_semantics"] += 1
                    workspace_ok = False
            for cm_ref in sorted(extract_cm_refs(agents_path)):
                if cm_ref not in skill_names:
                    report_issue(
                        agents_path.relative_to(KORA_ROOT),
                        "missing_cm",
                        f"missing referenced skill '{cm_ref}'",
                        workspace=rel_workspace,
                    )
                    issue_counts["missing_cm"] += 1
                    workspace_ok = False

            for namespace, name in sorted(extract_workspace_refs(agents_path)):
                if not (KORA_ROOT / "agents" / namespace / name).is_dir():
                    report_issue(
                        agents_path.relative_to(KORA_ROOT),
                        "broken_agent_route",
                        f"broken cross-agent route '{namespace}/{name}'",
                        workspace=rel_workspace,
                    )
                    issue_counts["broken_agent_route"] += 1
                    workspace_ok = False

        if profile != "legacy" and skill_dir.exists():
            for skill_path in sorted(skill_dir.glob("*.md")):
                skill_text = skill_path.read_text(encoding="utf-8")
                for failure in validate_skill_file(skill_path):
                    report_issue(skill_path.relative_to(KORA_ROOT), "skill_semantics", failure, workspace=rel_workspace)
                    issue_counts["skill_semantics"] += 1
                    workspace_ok = False
                for failure in validate_skill_purity(skill_text):
                    report_issue(skill_path.relative_to(KORA_ROOT), "skill_purity", failure, workspace=rel_workspace)
                    issue_counts["skill_purity"] += 1
                    workspace_ok = False
                for failure in validate_skill_tool_closure(skill_text, valid_tool_names):
                    report_issue(skill_path.relative_to(KORA_ROOT), "skill_tool_closure", failure, workspace=rel_workspace)
                    issue_counts["skill_tool_closure"] += 1
                    workspace_ok = False
                for failure in validate_traces_semantics(skill_path, skill_text):
                    report_issue(skill_path.relative_to(KORA_ROOT), "trace_semantics", failure, workspace=rel_workspace)
                    issue_counts["trace_semantics"] += 1
                    workspace_ok = False

        if profile != "legacy":
            for failure in validate_workspace_semantics(workspace_dir, config_data, valid_tool_names):
                report_issue(rel_workspace, "workspace_semantics", failure, workspace=rel_workspace)
                issue_counts["workspace_semantics"] += 1
                workspace_ok = False

        if workspace_ok:
            workspace_valid += 1
        else:
            workspace_invalid += 1

    if profile != "legacy" and cohort is None:
        for spec_path in sorted((KORA_ROOT / "specs").glob("*.md")):
            spec_text = spec_path.read_text(encoding="utf-8")
            for failure in validate_traces_semantics(spec_path, spec_text):
                report_issue(spec_path.relative_to(KORA_ROOT), "spec_trace_semantics", failure, workspace=None)
                issue_counts["spec_trace_semantics"] += 1
                global_failures += 1

    if emit:
        print(
            "Validation complete! "
            f"Workspaces valid: {workspace_valid}, Invalid: {workspace_invalid}, "
            f"Bootstrap files validated: {bootstrap_validated}"
        )
        if issue_counts:
            print("Issue breakdown:")
            for issue, count in sorted(issue_counts.items()):
                print(f"  {issue}: {count}")

    return {
        "profile": profile,
        "cohort": cohort,
        "workspace_valid": workspace_valid,
        "workspace_invalid": workspace_invalid,
        "bootstrap_validated": bootstrap_validated,
        "global_failures": global_failures,
        "issue_counts": dict(sorted(issue_counts.items())),
        "issues": issues,
        "ok": workspace_invalid == 0 and global_failures == 0,
    }


def cmd_validate(profile="transitional", cohort=None):
    result = validate_workspaces(profile=profile, cohort=cohort, emit=True)
    if not result["ok"]:
        raise SystemExit(1)


def auto_fix_markdown_paths(paths, max_lines_per_h2=None, emit=True):
    changed = []
    for path in iter_markdown_lint_targets(paths):
        frontmatter, body = load_markdown_parts(path)
        if not should_enforce_published_kora_markdown(frontmatter, path):
            continue
        fixed_body = auto_fix_published_kora_markdown_parts(frontmatter, body, max_lines_per_h2=max_lines_per_h2)
        if fixed_body != body:
            from .artifacts import dump_yaml_frontmatter_and_body

            dump_yaml_frontmatter_and_body(path, frontmatter, fixed_body)
            changed.append(path)
            if emit:
                rel_path = path.relative_to(KORA_ROOT) if KORA_ROOT in path.parents or path == KORA_ROOT else path
                print(f"[FIX] {rel_path}")
    return changed


def cmd_lint_md(paths=None, max_lines_per_h2=None, fix=False):
    target_paths = paths or [KORA_ROOT / "knowledge", KORA_ROOT / "drafts"]
    if fix:
        auto_fix_markdown_paths(target_paths, max_lines_per_h2=max_lines_per_h2, emit=True)
    result = lint_markdown_paths(target_paths, max_lines_per_h2=max_lines_per_h2, emit=True)
    if not result["ok"]:
        raise SystemExit(1)
