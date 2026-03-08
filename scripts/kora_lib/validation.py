import json
import re
from collections import Counter
from functools import lru_cache

from .artifacts import load_yaml_safe
from .config import (
    AGENT_BOOTSTRAP_FILES,
    AGENT_REQUIRED_FILES,
    AGENTS_FORBIDDEN_PATTERNS,
    BOOTSTRAP_SCHEMA_PATH,
    CONFIG_SCHEMA_PATH,
    KB_PIPELINE_PATTERN,
    KORA_ROOT,
    LOW_LEVEL_RUNTIME_HINTS,
    SEMANTIC_TOOL_DOC_MARKERS,
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
    iter_agent_workspaces,
    validate_skill_file,
)


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


def split_tool_sections(content):
    sections = {}
    current_heading = None
    current_lines = []
    in_code_block = False

    for line in content.splitlines():
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code_block = not in_code_block
        if not in_code_block and stripped.startswith("## "):
            if current_heading is not None:
                sections[current_heading] = "\n".join(current_lines).strip()
            current_heading = stripped[3:].strip()
            current_lines = []
            continue
        if current_heading is not None:
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
        if section_body and not any(marker in section_body for marker in SEMANTIC_TOOL_DOC_MARKERS):
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
    if config_data:
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


def cmd_validate(profile="transitional", cohort=None):
    print(f"Validating KORA agent workspaces against schema + semantic invariants ({profile})...")
    try:
        import jsonschema
    except ImportError:
        print("Error: 'jsonschema' module is required for validation. Run 'pip install jsonschema'.")
        raise SystemExit(1)

    schema, _ = load_yaml_safe(BOOTSTRAP_SCHEMA_PATH)
    if not schema:
        print(f"Error: Could not load schema from {BOOTSTRAP_SCHEMA_PATH}")
        raise SystemExit(1)

    config_schema, _ = load_yaml_safe(CONFIG_SCHEMA_PATH)
    if not config_schema:
        print(f"Error: Could not load schema from {CONFIG_SCHEMA_PATH}")
        raise SystemExit(1)

    workspace_valid = 0
    workspace_invalid = 0
    bootstrap_validated = 0
    global_failures = 0
    issue_counts = Counter()

    for workspace_dir in iter_agent_workspaces(cohort=cohort):
        rel_workspace = workspace_dir.relative_to(KORA_ROOT)
        workspace_ok = True
        missing_files = get_workspace_missing_files(workspace_dir, AGENT_REQUIRED_FILES)
        if missing_files:
            print(f"[FAIL] {rel_workspace} - missing required files: {', '.join(missing_files)}")
            issue_counts["missing_files"] += 1
            workspace_ok = False

        config_path = workspace_dir / "config.json"
        config_data = None
        try:
            with open(config_path, "r", encoding="utf-8") as handle:
                config_data = json.load(handle)
        except Exception as exc:
            print(f"[FAIL] {config_path.relative_to(KORA_ROOT)} - invalid JSON: {exc}")
            issue_counts["invalid_json"] += 1
            workspace_ok = False

        if config_data and profile != "legacy":
            try:
                jsonschema.validate(instance=config_data, schema=config_schema)
            except jsonschema.exceptions.ValidationError as exc:
                print(f"[FAIL] {config_path.relative_to(KORA_ROOT)} - {exc.message}")
                issue_counts["config_schema"] += 1
                workspace_ok = False

        for bootstrap_file in AGENT_BOOTSTRAP_FILES:
            agent_path = workspace_dir / bootstrap_file
            if not agent_path.exists():
                continue
            agent_data, err = load_yaml_safe(agent_path)
            if not agent_data:
                print(f"[FAIL] Could not parse YAML: {agent_path.relative_to(KORA_ROOT)}. Error: {err}")
                issue_counts["bootstrap_parse"] += 1
                workspace_ok = False
                continue

            try:
                jsonschema.validate(instance=agent_data, schema=schema)
                bootstrap_validated += 1
            except jsonschema.exceptions.ValidationError as exc:
                print(f"[FAIL] {agent_path.relative_to(KORA_ROOT)} - {exc.message}")
                issue_counts["bootstrap_schema"] += 1
                workspace_ok = False

        tools_path = workspace_dir / "TOOLS.md"
        valid_tool_names = []
        if tools_path.exists():
            tools_text = tools_path.read_text(encoding="utf-8")
            _, valid_tool_names, invalid_tool_names = extract_declared_tool_headings(tools_path)
            if profile != "legacy":
                for invalid_name in invalid_tool_names:
                    print(f"[FAIL] {tools_path.relative_to(KORA_ROOT)} - invalid tool identifier '{invalid_name}'")
                    issue_counts["tool_identifier"] += 1
                    workspace_ok = False
                for failure in validate_traces_semantics(tools_path, tools_text):
                    print(f"[FAIL] {tools_path.relative_to(KORA_ROOT)} - {failure}")
                    issue_counts["trace_semantics"] += 1
                    workspace_ok = False

        declared_allow = []
        if config_data:
            declared_allow = config_data.get("tools", {}).get("allow", [])
        if profile != "legacy" and (valid_tool_names or declared_allow):
            if set(valid_tool_names) != set(declared_allow):
                print(
                    f"[FAIL] {rel_workspace} - TOOLS.md headings {sorted(valid_tool_names)} != config.json.tools.allow {sorted(declared_allow)}"
                )
                issue_counts["tool_allow_mismatch"] += 1
                workspace_ok = False

        agents_path = workspace_dir / "AGENTS.md"
        skill_dir = workspace_dir / "skills"
        skill_names = {path.stem for path in skill_dir.glob("*.md")} if skill_dir.exists() else set()
        if profile != "legacy":
            if agents_path.exists():
                agents_text = agents_path.read_text(encoding="utf-8")
                for failure in validate_traces_semantics(agents_path, agents_text):
                    print(f"[FAIL] {agents_path.relative_to(KORA_ROOT)} - {failure}")
                    issue_counts["trace_semantics"] += 1
                    workspace_ok = False
            for cm_ref in sorted(extract_cm_refs(agents_path)):
                if cm_ref not in skill_names:
                    print(f"[FAIL] {agents_path.relative_to(KORA_ROOT)} - missing referenced skill '{cm_ref}'")
                    issue_counts["missing_cm"] += 1
                    workspace_ok = False

            for namespace, name in sorted(extract_workspace_refs(agents_path)):
                if not (KORA_ROOT / "agents" / namespace / name).is_dir():
                    print(
                        f"[FAIL] {agents_path.relative_to(KORA_ROOT)} - broken cross-agent route '{namespace}/{name}'"
                    )
                    issue_counts["broken_agent_route"] += 1
                    workspace_ok = False

        if profile != "legacy" and skill_dir.exists():
            for skill_path in sorted(skill_dir.glob("*.md")):
                skill_text = skill_path.read_text(encoding="utf-8")
                for failure in validate_skill_file(skill_path):
                    print(f"[FAIL] {skill_path.relative_to(KORA_ROOT)} - {failure}")
                    issue_counts["skill_semantics"] += 1
                    workspace_ok = False
                for failure in validate_skill_purity(skill_text):
                    print(f"[FAIL] {skill_path.relative_to(KORA_ROOT)} - {failure}")
                    issue_counts["skill_purity"] += 1
                    workspace_ok = False
                for failure in validate_traces_semantics(skill_path, skill_text):
                    print(f"[FAIL] {skill_path.relative_to(KORA_ROOT)} - {failure}")
                    issue_counts["trace_semantics"] += 1
                    workspace_ok = False

        if profile != "legacy":
            for failure in validate_workspace_semantics(workspace_dir, config_data, valid_tool_names):
                print(f"[FAIL] {rel_workspace} - {failure}")
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
                print(f"[FAIL] {spec_path.relative_to(KORA_ROOT)} - {failure}")
                issue_counts["spec_trace_semantics"] += 1
                global_failures += 1

    print(
        "Validation complete! "
        f"Workspaces valid: {workspace_valid}, Invalid: {workspace_invalid}, "
        f"Bootstrap files validated: {bootstrap_validated}"
    )
    if issue_counts:
        print("Issue breakdown:")
        for issue, count in sorted(issue_counts.items()):
            print(f"  {issue}: {count}")
    if workspace_invalid or global_failures:
        raise SystemExit(1)
