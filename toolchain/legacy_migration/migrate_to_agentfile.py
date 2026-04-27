#!/usr/bin/env python3
"""
Migrate legacy 5-file agent workspaces to AGENT.md (agentfile-spec v1.0.0).
Reads AGENTS.md, SOUL.md, USER.md, TOOLS.md, config.json -> produces AGENT.md.
"""

import json
import re
import os
import sys
import textwrap
from pathlib import Path
from datetime import date

AGENTS_ROOT = Path("/home/felix/kora/AGENTS")
TODAY = date.today().isoformat()

WORKSPACES = [
    "dev/steipete",
    "fxsl/arquitecto-automatizacion-organizacional",
    "fxsl/arquitecto-sistemas-informacion",
    "fxsl/ingeniero-sistemas-composicional",
    "fxsl/neriomath",
    "fxsl/ontologista-gist",
    "fxsl/pensador-generador",
    "gn/ar-virtual",
    "gn/asesor-juridico",
    "gn/dgi-virtual",
    "gn/digitrans",
    "gn/erp-gore",
    "gn/gestor-ipr-360",
    "gn/gobernador-virtual",
    "gn/goreologo",
    "kora/clawforge",
    "kora/custodio",
    "kora/forgemaster",
    "kora/guardian",
    "korvo/korax",
    "ops/clawstack",
    "salud/medico-urgencias",
    "salud/salubrista",
    "salud/salubrista-hah",
]


def read_file(path):
    """Read file, return content or empty string if missing."""
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return ""


def parse_config(ws_path):
    """Parse config.json."""
    content = read_file(ws_path / "config.json")
    if not content:
        return {}
    try:
        return json.loads(content)
    except json.JSONDecodeError:
        print(f"  WARN: config.json parse error in {ws_path}")
        return {}


def extract_version(config):
    """Extract version from config URN or default."""
    urn = config.get("_manifest", {}).get("urn", "")
    # URN format: urn:ns:agent-bootstrap:name:VERSION
    parts = urn.split(":")
    if len(parts) >= 5:
        v = parts[-1]
        if re.match(r"^\d+\.\d+\.\d+$", v):
            return v
    return "1.0.0"


def extract_section(text, section_num, title_pattern=None):
    """Extract section content from AGENTS.md by section number or pattern."""
    if not text:
        return ""
    # Try numbered section first
    pattern = rf"^#+\s*{section_num}[\.\s]"
    lines = text.split("\n")
    start = None
    for i, line in enumerate(lines):
        if re.match(pattern, line):
            start = i + 1
            break
    if start is None and title_pattern:
        for i, line in enumerate(lines):
            if re.search(title_pattern, line, re.IGNORECASE):
                start = i + 1
                break
    if start is None:
        return ""
    # Find next section of same or higher level
    result = []
    for i in range(start, len(lines)):
        if re.match(r"^#+\s*\d+[\.\s]", lines[i]):
            break
        result.append(lines[i])
    return "\n".join(result).strip()


def extract_fsm_states(agents_text):
    """Extract FSM states from AGENTS.md section 1."""
    section = extract_section(agents_text, 1, r"FSM|Maquina|Estado")
    if not section:
        return None

    states = []
    # Look for state definitions: **S-NAME** or S-NAME:
    state_pattern = re.compile(r'\*?\*?(S-[A-Z_-]+)\*?\*?')
    lines = section.split("\n")

    current_state = None
    current_act = ""
    transitions = []

    for line in lines:
        state_match = re.match(r'^\s*[-*]\s*\*?\*?(S-[A-Z_-]+)\*?\*?\s*[:\-]?\s*(.*)', line)
        if state_match:
            if current_state:
                states.append({
                    "id": current_state,
                    "act": current_act.strip() or f"Procesar estado {current_state}",
                    "transitions": transitions if transitions else [{"condition": "completado", "target": "S-END", "priority": 1}]
                })
            current_state = state_match.group(1)
            current_act = state_match.group(2).strip()
            transitions = []
        elif current_state and ("→" in line or "->" in line or "target" in line.lower()):
            # Try to parse transitions
            trans_match = re.search(r'(\w[\w\s]*?)\s*(?:→|->)\s*(S-[A-Z_-]+)', line)
            if trans_match:
                transitions.append({
                    "condition": trans_match.group(1).strip(),
                    "target": trans_match.group(2).strip(),
                    "priority": len(transitions) + 1
                })

    if current_state:
        states.append({
            "id": current_state,
            "act": current_act.strip() or f"Procesar estado {current_state}",
            "transitions": transitions if transitions else [{"condition": "[terminal]", "target": current_state, "priority": 1}]
        })

    return states if states else None


def extract_hard_rules(agents_text):
    """Extract hard rules from AGENTS.md section 2."""
    section = extract_section(agents_text, 2, r"Reglas?\s*Duras?|Hard\s*Rules?")
    if not section:
        return []
    rules = []
    for line in section.split("\n"):
        line = line.strip()
        if line.startswith(("-", "*", "1", "2", "3", "4", "5", "6", "7", "8", "9")):
            rule = re.sub(r'^[-*\d.)\s]+', '', line).strip()
            if rule:
                rules.append(rule)
    return rules


def extract_co_induction(agents_text):
    """Extract co-induction from AGENTS.md section 3."""
    section = extract_section(agents_text, 3, r"[Cc]o[-\s]?[Ii]nducc?i[oó]n")
    checks = []
    if not section:
        return checks
    for line in section.split("\n"):
        line = line.strip()
        if line.startswith(("-", "*")):
            check = re.sub(r'^[-*\s]+', '', line).strip()
            if check:
                checks.append(check)
    return checks


def extract_wiring(agents_text):
    """Extract wiring/composition from AGENTS.md section 5."""
    section = extract_section(agents_text, 5, r"[Ww]iring|[Cc]omposic")
    sub_agents = []
    if not section:
        return sub_agents
    # Look for URN references to other agents
    for match in re.finditer(r'urn:(\w+):(?:agent-bootstrap|agent):([^:\s]+)', section):
        ns, name = match.group(1), match.group(2)
        sub_agents.append({"urn": f"urn:{ns}:agent:{name}", "role": name})
    return sub_agents


def parse_soul(soul_text):
    """Extract identity info from SOUL.md."""
    result = {"paradigm": "", "tone": "", "description": "", "domain": []}
    if not soul_text:
        return result

    lines = soul_text.split("\n")
    current_section = ""
    buffer = []

    for line in lines:
        lower = line.lower().strip()
        if "paradigm" in lower or "identidad" in lower or "quien" in lower or "qué es" in lower:
            if buffer and current_section:
                result[current_section] = " ".join(buffer).strip()
            current_section = "paradigm"
            buffer = []
            content = re.sub(r'^[#*\s]*(?:paradigma?|identidad|quien\s+(?:soy|eres)|qué\s+es)[:\s]*', '', line, flags=re.IGNORECASE).strip()
            if content:
                buffer.append(content)
        elif "tono" in lower or "tone" in lower or "estilo" in lower:
            if buffer and current_section:
                result[current_section] = " ".join(buffer).strip()
            current_section = "tone"
            buffer = []
            content = re.sub(r'^[#*\s]*(?:tono|tone|estilo)[:\s]*', '', line, flags=re.IGNORECASE).strip()
            if content:
                buffer.append(content)
        elif "dominio" in lower or "domain" in lower or "competencia" in lower:
            if buffer and current_section:
                result[current_section] = " ".join(buffer).strip()
            current_section = "domain"
            buffer = []
        elif line.strip().startswith(("-", "*")) and current_section == "domain":
            item = re.sub(r'^[-*\s]+', '', line).strip()
            if item:
                result["domain"].append(item)
        elif current_section and line.strip():
            if current_section == "domain" and line.strip().startswith(("-", "*")):
                item = re.sub(r'^[-*\s]+', '', line).strip()
                if item:
                    result["domain"].append(item)
            else:
                buffer.append(line.strip())

    if buffer and current_section:
        result[current_section] = " ".join(buffer).strip()

    # If no structured extraction, use full text
    if not result["paradigm"]:
        # Take first substantial paragraph
        for line in lines:
            line = line.strip()
            if line and not line.startswith("#") and not line.startswith("---") and len(line) > 20:
                result["paradigm"] = line
                break

    return result


def parse_user(user_text):
    """Extract operator info from USER.md."""
    result = {"role": "", "context": ""}
    if not user_text:
        return result

    lines = user_text.split("\n")
    content_lines = [l.strip() for l in lines if l.strip() and not l.strip().startswith("#") and not l.strip().startswith("---")]

    if content_lines:
        result["role"] = content_lines[0]
        if len(content_lines) > 1:
            result["context"] = " ".join(content_lines[1:3])

    return result


def parse_tools(tools_text):
    """Extract tools from TOOLS.md."""
    tools = []
    if not tools_text:
        return tools

    lines = tools_text.split("\n")
    current_tool = None

    for line in lines:
        # Tool name patterns: ### tool_name, **tool_name**, - tool_name:
        tool_match = re.match(r'^#{2,4}\s+(\w[\w_-]*)', line)
        if not tool_match:
            tool_match = re.match(r'^\s*[-*]\s*\*?\*?(\w[\w_-]*)\*?\*?\s*[:\-]', line)

        if tool_match:
            name = tool_match.group(1).strip()
            if name.lower() not in ("tools", "herramientas", "interface", "interfaz", "permissions", "permisos",
                                     "allow", "deny", "kb", "knowledge", "routing", "routes", "notas", "notes"):
                if current_tool:
                    tools.append(current_tool)
                current_tool = {
                    "name": name,
                    "description": "",
                    "parameters": "input -> output",
                    "when_to_use": "Cuando se necesite " + name,
                    "when_not_to_use": "Datos ya disponibles en contexto"
                }
                # Get inline description
                desc = re.sub(r'^#{2,4}\s+\w[\w_-]*\s*[:\-]?\s*', '', line).strip()
                if not desc:
                    desc = re.sub(r'^\s*[-*]\s*\*?\*?\w[\w_-]*\*?\*?\s*[:\-]\s*', '', line).strip()
                if desc:
                    current_tool["description"] = desc
        elif current_tool:
            line_s = line.strip().lower()
            if "descripci" in line_s or "description" in line_s:
                val = re.sub(r'^.*?[:\-]\s*', '', line.strip())
                if val:
                    current_tool["description"] = val
            elif "param" in line_s or "firma" in line_s or "signature" in line_s:
                val = re.sub(r'^.*?[:\-]\s*', '', line.strip())
                if val:
                    current_tool["parameters"] = val
            elif "cuando usar" in line_s or "when_to_use" in line_s or "cuándo usar" in line_s:
                val = re.sub(r'^.*?[:\-]\s*', '', line.strip())
                if val:
                    current_tool["when_to_use"] = val
            elif "cuando no" in line_s or "when_not" in line_s or "cuándo no" in line_s:
                val = re.sub(r'^.*?[:\-]\s*', '', line.strip())
                if val:
                    current_tool["when_not_to_use"] = val

    if current_tool:
        tools.append(current_tool)

    return tools


def get_skills(ws_path):
    """List CM-* skills from skills/ directory."""
    skills_dir = ws_path / "skills"
    if not skills_dir.exists():
        return []
    skills = []
    for item in sorted(skills_dir.iterdir()):
        name = item.stem if item.is_file() else item.name
        if name.startswith("CM-"):
            skills.append({"id": name, "required": True})
    return skills


def extract_behavior_body(agents_text):
    """Extract behavior content from AGENTS.md, excluding pure FSM section."""
    if not agents_text:
        return ""

    lines = agents_text.split("\n")
    # Skip frontmatter
    in_frontmatter = False
    start = 0
    for i, line in enumerate(lines):
        if line.strip() == "---":
            if not in_frontmatter:
                in_frontmatter = True
            else:
                start = i + 1
                break

    # Get everything after frontmatter and first heading
    content = "\n".join(lines[start:]).strip()

    # Remove the pure FSM state list (section 1) but keep behavior prose
    # Remove section headers with numbers
    sections = re.split(r'\n(?=#{1,3}\s+\d+[\.\s])', content)

    behavior_parts = []
    context_parts = []

    for section in sections:
        header_match = re.match(r'^(#{1,3})\s+(\d+)[\.\s]*(.*)', section)
        if header_match:
            sec_num = int(header_match.group(2))
            sec_title = header_match.group(3).strip()
            sec_body = section[len(header_match.group(0)):].strip()

            if sec_num == 1:
                # FSM section - skip pure state lists, keep prose
                prose_lines = []
                for line in sec_body.split("\n"):
                    # Skip lines that are just state definitions
                    if re.match(r'^\s*[-*]\s*\*?\*?S-[A-Z]', line):
                        continue
                    if re.match(r'^\s*[-*]\s*(?:→|->)', line):
                        continue
                    prose_lines.append(line)
                prose = "\n".join(prose_lines).strip()
                if prose:
                    behavior_parts.append(prose)
            elif sec_num == 2:
                # Hard rules - captured in frontmatter, skip
                pass
            elif sec_num == 3:
                # Co-induction - captured in frontmatter, skip
                pass
            elif sec_num == 4:
                # Context
                context_parts.append(sec_body)
            elif sec_num == 5:
                # Wiring - captured in frontmatter, skip
                pass
            else:
                behavior_parts.append(sec_body)
        else:
            # Non-numbered section
            if section.strip():
                behavior_parts.append(section.strip())

    return "\n\n".join(behavior_parts), "\n\n".join(context_parts)


def yaml_str(s, indent=0):
    """Format string for YAML, using > for long strings."""
    if not s:
        return '""'
    s = s.replace('"', '\\"')
    if "\n" in s or len(s) > 100:
        prefix = " " * indent
        lines = s.split("\n")
        return ">\n" + "\n".join(prefix + "  " + l for l in lines)
    return f'"{s}"'


def yaml_list_str(items, indent=6):
    """Format a list of strings as YAML."""
    if not items:
        return "[]"
    prefix = " " * indent
    return "\n" + "\n".join(f"{prefix}- \"{item}\"" for item in items)


def build_tool_yaml(tool, indent=8):
    """Build YAML for a single tool entry."""
    prefix = " " * indent
    lines = [
        f'{prefix}- name: {tool["name"]}',
        f'{prefix}  description: "{tool.get("description", tool["name"])}"',
        f'{prefix}  parameters: "{tool.get("parameters", "input -> output")}"',
        f'{prefix}  when_to_use: "{tool.get("when_to_use", "Cuando se necesite")}"',
        f'{prefix}  when_not_to_use: "{tool.get("when_not_to_use", "Datos ya disponibles")}"',
    ]
    return "\n".join(lines)


def escape_yaml(s):
    """Escape a string for use in YAML double-quoted context."""
    if not s:
        return ""
    return s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", " ").strip()


def build_agent_md(ws_name, ws_path):
    """Build AGENT.md content for a workspace."""
    namespace, agent_id = ws_name.split("/", 1)

    # Read all files
    agents_text = read_file(ws_path / "AGENTS.md")
    soul_text = read_file(ws_path / "SOUL.md")
    user_text = read_file(ws_path / "USER.md")
    tools_text = read_file(ws_path / "TOOLS.md")
    config = parse_config(ws_path)

    # Extract version
    version = extract_version(config)

    # Parse components
    soul = parse_soul(soul_text)
    user = parse_user(user_text)
    tools = parse_tools(tools_text)
    skills = get_skills(ws_path)
    hard_rules = extract_hard_rules(agents_text)
    co_induction_raw = extract_co_induction(agents_text)
    wiring = extract_wiring(agents_text)
    fsm_states = extract_fsm_states(agents_text)
    behavior_body, context_body = extract_behavior_body(agents_text)

    # Build name from agent_id
    name = agent_id.replace("-", " ").title()

    # Description from soul or agents
    description = soul.get("description", "")
    if not description and soul.get("paradigm"):
        description = soul["paradigm"][:200]
    if not description:
        # Try first line of AGENTS.md after frontmatter
        for line in agents_text.split("\n"):
            line = line.strip()
            if line and not line.startswith("#") and not line.startswith("---") and len(line) > 10:
                description = line[:200]
                break
    if not description:
        description = f"Agente {name}"

    # Domain
    domain = soul.get("domain", [])
    if not domain:
        # Extract from tags or config
        domain = [agent_id.replace("-", " ")]

    # Tags
    tags = [agent_id, namespace]

    # Paradigm and tone
    paradigm = soul.get("paradigm", f"Agente especializado en {agent_id.replace('-', ' ')}")
    tone = soul.get("tone", "Profesional, directo y preciso")

    # Operator
    op_role = user.get("role", "Operador KORA")
    op_context = user.get("context", f"Sesion de trabajo con {name}")

    # Tools permissions
    tool_names = [t["name"] for t in tools]
    if not tool_names and config.get("tools", {}).get("allow"):
        tool_names = config["tools"]["allow"]
        tools = [{"name": n, "description": n, "parameters": "input -> output",
                  "when_to_use": f"Cuando se necesite {n}", "when_not_to_use": "Datos ya disponibles"}
                 for n in tool_names]

    # Runtime
    sandbox = config.get("sandbox", {}).get("mode", "strict")
    model_routing = config.get("model_routing", {})
    limits = config.get("limits", {})

    # Knowledge
    allowed_kb = config.get("allowed_kb", [])
    kb_routes = {}

    # Try to extract kb_routes from TOOLS.md
    if tools_text:
        for match in re.finditer(r'([\w_]+)\s*(?:→|->|:)\s*(urn:\w+:kb:[\w-]+)', tools_text):
            kb_routes[match.group(1)] = match.group(2)

    # Build scope from hard rules
    allowed_scope = []
    forbidden_scope = []
    rejection = f"Fuera de scope. {name} solo opera en su dominio declarado."

    for rule in hard_rules:
        lower = rule.lower()
        if any(w in lower for w in ("no ", "nunca", "prohib", "forbidden", "jamás", "jamas")):
            forbidden_scope.append(rule)
        elif any(w in lower for w in ("solo", "sólo", "permitid", "allowed", "exclusiv")):
            allowed_scope.append(rule)
        else:
            allowed_scope.append(rule)

    if not allowed_scope:
        allowed_scope = [f"Operar en dominio: {', '.join(domain)}"]
    if not forbidden_scope:
        forbidden_scope = ["Operar fuera del dominio declarado"]

    # Constraints from remaining hard rules
    constraints = [r for r in hard_rules if r not in allowed_scope and r not in forbidden_scope]

    # --- Build YAML frontmatter ---

    # Tools YAML
    tools_yaml = ""
    if tools:
        tool_entries = []
        for t in tools:
            tool_entries.append(
                f'        - name: {t["name"]}\n'
                f'          description: "{escape_yaml(t.get("description", t["name"]))[:120]}"\n'
                f'          parameters: "{escape_yaml(t.get("parameters", "input -> output"))[:120]}"\n'
                f'          when_to_use: "{escape_yaml(t.get("when_to_use", "Cuando se necesite"))[:120]}"\n'
                f'          when_not_to_use: "{escape_yaml(t.get("when_not_to_use", "Datos ya disponibles"))[:120]}"'
            )
        tools_yaml = "\n".join(tool_entries)

    # Permissions YAML
    allow_yaml = "\n".join(f"          - {n}" for n in tool_names) if tool_names else "          []"

    # FSM states YAML
    plan_yaml = ""
    if fsm_states:
        state_entries = []
        for s in fsm_states:
            trans_entries = []
            for t in s.get("transitions", []):
                trans_entries.append(
                    f'            - {{condition: "{escape_yaml(t["condition"])}", '
                    f'target: {t["target"]}, priority: {t["priority"]}}}'
                )
            trans_yaml = "\n".join(trans_entries) if trans_entries else f'            - {{condition: "[terminal]", target: {s["id"]}, priority: 1}}'
            state_entries.append(
                f'        - id: {s["id"]}\n'
                f'          act: "{escape_yaml(s.get("act", "Procesar"))[:120]}"\n'
                f'          transitions:\n{trans_yaml}'
            )
        plan_yaml = "\n".join(state_entries)
        initial = fsm_states[0]["id"] if fsm_states else "S-DISPATCHER"
        terminal = fsm_states[-1]["id"] if fsm_states else "S-END"
    else:
        initial = "S-DISPATCHER"
        terminal = "S-END"
        plan_yaml = (
            f'        - id: S-DISPATCHER\n'
            f'          act: "Clasificar solicitud y determinar accion"\n'
            f'          transitions:\n'
            f'            - {{condition: "tarea_clara", target: S-EXECUTE, priority: 1}}\n'
            f'            - {{condition: "ambiguo", target: S-DISPATCHER, priority: 2}}\n'
            f'            - {{condition: "terminar", target: S-END, priority: 3}}\n'
            f'        - id: S-EXECUTE\n'
            f'          act: "Ejecutar tarea principal del dominio"\n'
            f'          transitions:\n'
            f'            - {{condition: "completado", target: S-VALIDATE, priority: 1}}\n'
            f'            - {{condition: "error", target: S-DISPATCHER, priority: 2}}\n'
            f'        - id: S-VALIDATE\n'
            f'          act: "Validar resultado contra invariantes"\n'
            f'          transitions:\n'
            f'            - {{condition: "valido", target: S-END, priority: 1}}\n'
            f'            - {{condition: "correccion_necesaria", target: S-EXECUTE, priority: 2}}\n'
            f'        - id: S-END\n'
            f'          act: "Emitir resultado final"\n'
            f'          transitions:\n'
            f'            - {{condition: "[terminal]", target: S-END, priority: 1}}'
        )

    # Domain YAML
    domain_yaml = "\n".join(f"        - {d}" for d in domain)

    # Tags YAML
    tags_yaml = ", ".join(tags)

    # Allowed KB YAML
    kb_yaml = "\n".join(f'          - "{kb}"' for kb in allowed_kb) if allowed_kb else "          []"

    # KB routes YAML
    kb_routes_yaml = ""
    if kb_routes:
        kb_routes_yaml = "\n      kb_routes:\n" + "\n".join(f'        {k}: "{v}"' for k, v in kb_routes.items())

    # Allowed scope YAML
    allowed_yaml = "\n".join(f'          - "{escape_yaml(s)}"' for s in allowed_scope)
    forbidden_yaml = "\n".join(f'          - "{escape_yaml(s)}"' for s in forbidden_scope)

    # Constraints YAML
    constraints_yaml = ""
    if constraints:
        constraints_yaml = "\n      constraints:\n" + "\n".join(f'        - "{escape_yaml(c)}"' for c in constraints)

    # Co-induction YAML
    co_checks = [
        '        - {id: SCOPE_COMPLIANCE, description: "Dentro del dominio declarado", on_fail: "reject"}',
        '        - {id: STATE_AWARENESS, description: "Coherente con estado FSM actual", on_fail: "redirect:S-DISPATCHER"}',
        '        - {id: INTERFACE_DISCIPLINE, description: "Solo usa tools y KBs declaradas", on_fail: "restrict"}',
    ]
    custom_checks = []
    for raw in co_induction_raw:
        # Try to extract check name
        match = re.match(r'\*?\*?([A-Z_]+)\*?\*?\s*[:\-]?\s*(.*)', raw)
        if match:
            cid = match.group(1)
            desc = match.group(2).strip() or raw
            if cid not in ("SCOPE_COMPLIANCE", "STATE_AWARENESS", "INTERFACE_DISCIPLINE"):
                custom_checks.append(
                    f'        - {{id: {cid}, description: "{escape_yaml(desc)[:100]}", on_fail: "retry"}}'
                )
        else:
            cid = "CHECK_" + str(len(custom_checks) + 1)
            custom_checks.append(
                f'        - {{id: {cid}, description: "{escape_yaml(raw)[:100]}", on_fail: "retry"}}'
            )

    co_induction_yaml = "\n".join(co_checks)
    custom_yaml = "\n".join(custom_checks) if custom_checks else ""

    # Skills YAML
    skills_yaml = ""
    if skills:
        skills_yaml = "\n".join(f'    - {{id: {s["id"]}, required: true}}' for s in skills)
    else:
        # Extract CM- references from AGENTS.md
        cm_refs = set(re.findall(r'(CM-[A-Z_-]+)', agents_text))
        if cm_refs:
            skills_yaml = "\n".join(f'    - {{id: {cm}, required: true}}' for cm in sorted(cm_refs))

    # Sub-agents YAML
    sub_agents_yaml = ""
    if wiring:
        entries = []
        for sa in wiring:
            entries.append(f'      - urn: "{sa["urn"]}"\n        role: "{sa["role"]}"')
        sub_agents_yaml = "\n" + "\n".join(entries)

    # Model routing YAML
    model_yaml = ""
    if model_routing:
        if isinstance(model_routing, dict) and "defaults" in model_routing:
            model_yaml = f'\n      model_routing:'
            for task, info in model_routing["defaults"].items():
                if isinstance(info, dict):
                    m = info.get("model", "")
                    model_yaml += f'\n        {task}: "{m}"'

    # Limits YAML
    limits_yaml = ""
    if limits:
        limits_yaml = "\n      limits:"
        for k, v in limits.items():
            if isinstance(v, dict):
                limits_yaml += f"\n        {k}:"
                for sk, sv in v.items():
                    limits_yaml += f"\n          {sk}: {json.dumps(sv)}"
            else:
                limits_yaml += f"\n        {k}: {v}"

    # --- Compose full AGENT.md ---

    frontmatter = f"""---
_manifest:
  urn: "urn:{namespace}:agent:{agent_id}"
  provenance:
    created_by: "FS"
    created_at: "{TODAY}"
    source: "{namespace}/{agent_id} workspace legacy v{version}, agentfile-spec v1.0.0"
version: "{version}"
name: "{name}"
status: active
tags: [{tags_yaml}]
lang: es
extensions: {{}}
agent:
  coalgebra:
    description: "{escape_yaml(description)[:200]}"
    domain:
{domain_yaml}
    triggers:
      - solicitud del operador
    outputs:
      - respuesta especializada en dominio
    invariants:
      - consistencia con dominio declarado

  plan:
    initial_state: {initial}
    terminal_state: {terminal}
    states:
{plan_yaml}

  interface:
    tools:
{tools_yaml if tools_yaml else '      []'}
    permissions:
      allow:
{allow_yaml}
      deny: []

  fibers:
    identity:
      paradigm: "{escape_yaml(paradigm)[:300]}"
      tone: "{escape_yaml(tone)[:200]}"
    operator:
      role: "{escape_yaml(op_role)[:200]}"
      context: "{escape_yaml(op_context)[:200]}"
    memory:
      mode: session
    runtime:
      sandbox: {sandbox}{model_yaml}{limits_yaml}
    knowledge:
      allowed_kb:
{kb_yaml}{kb_routes_yaml}

  composition:
    type: root
    sub_agents: {sub_agents_yaml if sub_agents_yaml else '[]'}
    delegation:
      max_depth: 1
      dissipation:
        propagate: []
        dissipate: [identity, operator]

  safety:
    hard_rules:
      scope:
        allowed:
{allowed_yaml}
        forbidden:
{forbidden_yaml}
        rejection: "{escape_yaml(rejection)[:200]}"{constraints_yaml}
    co_induction:
      pre_output_checks:
{co_induction_yaml}"""

    if custom_yaml:
        frontmatter += f"\n      custom_checks:\n{custom_yaml}"

    frontmatter += f"""
    guardrails: []
    alignment:
      principal: "KORA Governance (specs/gobernanza.md)"
      contract: "Operar dentro del dominio declarado con fidelidad y trazabilidad"

  skills:
{skills_yaml if skills_yaml else '    []'}
---"""

    # Body
    body = ""
    if behavior_body:
        body += f"\n\n## Behavior\n\n{behavior_body}"
    else:
        body += f"\n\n## Behavior\n\n{name} opera clasificando solicitudes y ejecutando acciones dentro de su dominio declarado."

    if context_body:
        body += f"\n\n## Context\n\n{context_body}"
    else:
        body += f"\n\n## Context\n\nDeteccion de desvio: si la solicitud sale del dominio declarado, redirigir a S-DISPATCHER.\nRetencion inter-turno: tarea activa, estado FSM, hallazgos pendientes."

    # Add style from SOUL.md tone
    if tone:
        body += f"\n\n## Style\n\n{tone}"

    return frontmatter + body + "\n"


def main():
    """Process all workspaces."""
    success = 0
    errors = []

    for ws_name in WORKSPACES:
        ws_path = AGENTS_ROOT / ws_name
        if not ws_path.exists():
            print(f"SKIP: {ws_name} (not found)")
            errors.append(ws_name)
            continue

        print(f"Processing: {ws_name}...")
        try:
            content = build_agent_md(ws_name, ws_path)
            output_path = ws_path / "AGENT.md"
            output_path.write_text(content, encoding="utf-8")
            print(f"  OK: {output_path}")
            success += 1
        except Exception as e:
            print(f"  ERROR: {e}")
            errors.append(ws_name)

    print(f"\nDone: {success}/{len(WORKSPACES)} migrated, {len(errors)} errors")
    if errors:
        print(f"Errors: {errors}")
    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
