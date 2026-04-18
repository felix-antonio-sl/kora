"""Unified check algebra for KORA maintenance.

Categorical model:
- A Check is a morphism in CheckCat: RepoState → DiagSet
- Checks compose via dependency ordering (topological sort)
- A Fix is the left adjoint of a Check: DiagSet → RepoState
- The Kleisli category of the Diag monad is the check-then-fix pipeline

Every check has:
- id: unique identifier
- scope: what it inspects (artifact | workspace | repo)
- severity: impact if it fails (critical | high | medium | low)
- enforcement: how it's verified (schema | lint | runtime | eval | manual)
- depends: checks that must pass first (DAG of dependencies)
- check_fn: produces diagnostics
- fix_fn: optional — canonical fix (left adjoint)
"""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Optional
import json


# ---------------------------------------------------------------------------
# Core data types
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Check:
    """A maintenance check — morphism in CheckCat."""
    id: str
    description: str
    scope: str                # artifact | workspace | repo
    severity: str             # critical | high | medium | low
    enforcement: str          # schema | lint | runtime | eval | manual
    spec_ref: str             # which spec section defines this
    depends: tuple = ()       # check ids that must pass first
    phase: str = "verify"     # index | verify | lint | graph | report


@dataclass
class Diagnostic:
    """Output of a check — object in DiagSet."""
    check_id: str
    severity: str
    scope: str
    path: str                 # file or workspace path (relative to repo root)
    message: str
    fix_hint: str = ""        # what would fix it (empty if no known fix)

    def __str__(self):
        prefix = f"[{self.severity.upper()}]"
        return f"{prefix} {self.check_id}: {self.path} — {self.message}"


@dataclass
class CheckResult:
    """Result of running the full check pipeline."""
    diagnostics: list = field(default_factory=list)
    checks_run: int = 0
    checks_passed: int = 0
    checks_failed: int = 0
    by_severity: dict = field(default_factory=dict)
    by_scope: dict = field(default_factory=dict)
    by_phase: dict = field(default_factory=dict)

    @property
    def ok(self):
        return self.checks_failed == 0

    def add(self, diag: Diagnostic):
        self.diagnostics.append(diag)
        self.by_severity[diag.severity] = self.by_severity.get(diag.severity, 0) + 1
        self.by_scope[diag.scope] = self.by_scope.get(diag.scope, 0) + 1


# ---------------------------------------------------------------------------
# Check registry — the single source of truth for all maintenance checks
# ---------------------------------------------------------------------------

# All checks, keyed by id
_REGISTRY: dict[str, Check] = {}

# Check implementations: id → callable(config) → list[Diagnostic]
_IMPLEMENTATIONS: dict[str, Callable] = {}

# Fix implementations: id → callable(diagnostics) → None
_FIXES: dict[str, Callable] = {}


def register_check(check: Check, impl: Callable, fix: Optional[Callable] = None):
    """Register a check with its implementation and optional fix."""
    _REGISTRY[check.id] = check
    _IMPLEMENTATIONS[check.id] = impl
    if fix:
        _FIXES[check.id] = fix


def get_check(check_id: str) -> Optional[Check]:
    return _REGISTRY.get(check_id)


def all_checks() -> list[Check]:
    return list(_REGISTRY.values())


# ---------------------------------------------------------------------------
# Topological ordering — ensures checks run in dependency order
# ---------------------------------------------------------------------------

def _topo_sort(checks: list[Check]) -> list[Check]:
    """Topological sort of checks by their depends field."""
    check_map = {c.id: c for c in checks}
    visited = set()
    order = []

    def visit(cid):
        if cid in visited:
            return
        visited.add(cid)
        c = check_map.get(cid)
        if c:
            for dep in c.depends:
                visit(dep)
            order.append(c)

    for c in checks:
        visit(c.id)
    return order


# ---------------------------------------------------------------------------
# Pipeline runner — the compositional maintenance pipeline
# ---------------------------------------------------------------------------

def run_checks(
    scope_filter: str = None,        # artifact | workspace | repo | None (all)
    severity_min: str = None,        # minimum severity to include
    phase_filter: str = None,        # index | verify | lint | graph | None (all)
    path_filter: str = None,         # restrict to a subtree
    check_ids: list = None,          # specific checks to run (None = all)
    emit: bool = True,
) -> CheckResult:
    """Run checks in topological order, producing a CheckResult."""
    severity_order = {"critical": 0, "high": 1, "medium": 2, "low": 3}
    min_sev = severity_order.get(severity_min, 3) if severity_min else 3

    # Select checks
    checks = list(_REGISTRY.values())
    if check_ids:
        checks = [c for c in checks if c.id in check_ids]
    if scope_filter:
        checks = [c for c in checks if c.scope == scope_filter]
    if phase_filter:
        checks = [c for c in checks if c.phase == phase_filter]
    checks = [c for c in checks if severity_order.get(c.severity, 3) <= min_sev]

    # Add dependencies that were filtered out
    needed = {c.id for c in checks}
    for c in checks:
        for dep in c.depends:
            needed.add(dep)
    checks = [c for c in _REGISTRY.values() if c.id in needed]

    # Sort topologically
    ordered = _topo_sort(checks)

    result = CheckResult()
    failed_checks = set()

    for check in ordered:
        impl = _IMPLEMENTATIONS.get(check.id)
        if not impl:
            continue

        # Skip if a dependency failed
        if any(dep in failed_checks for dep in check.depends):
            if emit:
                print(f"  [SKIP] {check.id} (dependency failed)")
            continue

        try:
            diags = impl(path_filter=path_filter)
        except Exception as exc:
            diags = [Diagnostic(
                check_id=check.id,
                severity="high",
                scope=check.scope,
                path="(runtime)",
                message=f"Check raised exception: {exc}",
            )]

        result.checks_run += 1
        result.by_phase[check.phase] = result.by_phase.get(check.phase, 0) + 1

        if diags:
            result.checks_failed += 1
            failed_checks.add(check.id)
            for d in diags:
                result.add(d)
                if emit:
                    print(f"  {d}")
        else:
            result.checks_passed += 1

    return result


def run_fixes(diagnostics: list, emit: bool = True) -> int:
    """Apply canonical fixes for diagnostics that have fix implementations."""
    fixed = 0
    by_check = {}
    for d in diagnostics:
        by_check.setdefault(d.check_id, []).append(d)

    for check_id, diags in by_check.items():
        fix = _FIXES.get(check_id)
        if not fix:
            continue
        try:
            fix(diags)
            fixed += len(diags)
            if emit:
                print(f"  [FIX] {check_id}: {len(diags)} issue(s) fixed")
        except Exception as exc:
            if emit:
                print(f"  [FIX-FAIL] {check_id}: {exc}")
    return fixed


# ---------------------------------------------------------------------------
# Built-in checks — extracted from audit.py, validation.py, kb_graph.py
# ---------------------------------------------------------------------------

def _check_catalog_exists(path_filter=None):
    """Verify catalog exists and is loadable."""
    from .catalog import load_catalog
    doc = load_catalog()
    if not doc or "Catalog" not in doc:
        return [Diagnostic(
            check_id="catalog-exists",
            severity="critical",
            scope="repo",
            path="catalog/catalog_master_kora.yml",
            message="Catalog not found or invalid. Run 'kora index' first.",
            fix_hint="python3 scripts/kora index",
        )]
    return []


def _check_urn_integrity(path_filter=None):
    """Verify all URN references resolve to existing catalog entries."""
    from .catalog import build_catalog_lookup, get_reference_entry, load_catalog, urn_is_known
    from .config import AGENTS_ROOT, KORA_ROOT
    from .graph import build_reference_graph
    from .workspaces import fragment_exists

    doc = load_catalog()
    if not doc or "Catalog" not in doc:
        return []  # catalog-exists check will catch this

    known_urns, urn_to_entry = build_catalog_lookup(doc)
    _scanned, edges = build_reference_graph()
    diags = []

    for edge in edges:
        if edge.kind in ("XRef", "TracesTo", "AllowsKB"):
            if not edge.target.startswith("urn:"):
                if edge.kind == "AllowsKB":
                    diags.append(Diagnostic(
                        check_id="urn-integrity",
                        severity="medium",
                        scope="workspace",
                        path=str(edge.source.relative_to(KORA_ROOT)),
                        message=f"Non-URN entry in allowed_kb: '{edge.target}'",
                        fix_hint="Replace with valid URN or remove",
                    ))
                continue
            if not urn_is_known(edge.target, known_urns):
                diags.append(Diagnostic(
                    check_id="urn-integrity",
                    severity="high",
                    scope="artifact",
                    path=str(edge.source.relative_to(KORA_ROOT)),
                    message=f"Broken URN reference: {edge.target}",
                    fix_hint="Correct the URN or remove the reference",
                ))
                continue
            entry = get_reference_entry(edge.target, urn_to_entry)
            if edge.fragment and entry and not fragment_exists(entry["file"], edge.fragment):
                diags.append(Diagnostic(
                    check_id="urn-integrity",
                    severity="medium",
                    scope="artifact",
                    path=str(edge.source.relative_to(KORA_ROOT)),
                    message=f"Broken URN fragment: {edge.target}#{edge.fragment}",
                ))
        elif edge.kind == "RoutesToAgent":
            ns, name = edge.target.split("/", 1)
            if not (AGENTS_ROOT / ns / name).is_dir():
                diags.append(Diagnostic(
                    check_id="urn-integrity",
                    severity="high",
                    scope="workspace",
                    path=str(edge.source.relative_to(KORA_ROOT)),
                    message=f"Broken agent route: {edge.target}",
                ))

    if path_filter:
        diags = [d for d in diags if d.path.startswith(path_filter)]
    return diags


def _check_workspace_validity(path_filter=None):
    """Validate workspaces against schema + semantic invariants (strict)."""
    from .validation import validate_workspaces
    result = validate_workspaces(profile="strict", emit=False)
    diags = []
    for issue in result.get("issues", []):
        severity = issue.get("severity")
        if severity is None:
            category = issue.get("category", "")
            severity = (
                "high"
                if category.endswith("_parse")
                or category.endswith("_schema")
                or category in {"missing_files", "invalid_json", "config_schema"}
                else "medium"
            )
        diags.append(Diagnostic(
            check_id="workspace-validity",
            severity=severity,
            scope="workspace",
            path=issue.get("path", ""),
            message=issue.get("message", str(issue)),
        ))
    if path_filter:
        diags = [d for d in diags if d.path.startswith(path_filter)]
    return diags


def _check_lint_md(path_filter=None):
    """Lint published KORA/MD artifacts."""
    from .config import KNOWLEDGE_ROOT
    from .validation import lint_markdown_paths

    target_paths = [child for child in KNOWLEDGE_ROOT.iterdir() if child.is_dir() and not child.name.startswith("_")]
    if not target_paths:
        target_paths = [KNOWLEDGE_ROOT]
    if path_filter:
        target_paths = [KNOWLEDGE_ROOT / path_filter] if (KNOWLEDGE_ROOT / path_filter).exists() else target_paths

    result = lint_markdown_paths(target_paths, emit=False)
    diags = []
    for issue in result.get("issues", []):
        # lint issues are tuples (rel_path, failure_string)
        if isinstance(issue, tuple) and len(issue) == 2:
            rel_path, failure = issue
            diags.append(Diagnostic(
                check_id="lint-md",
                severity="low",
                scope="artifact",
                path=str(rel_path),
                message=failure,
                fix_hint="python3 scripts/kora lint-md --fix",
            ))
        elif isinstance(issue, dict):
            diags.append(Diagnostic(
                check_id="lint-md",
                severity="low",
                scope="artifact",
                path=issue.get("path", ""),
                message=issue.get("message", str(issue)),
                fix_hint="python3 scripts/kora lint-md --fix",
            ))
    return diags


def _fix_lint_md(diagnostics):
    """Auto-fix lint issues."""
    from .config import KNOWLEDGE_ROOT
    from .validation import auto_fix_markdown_paths
    target_paths = [child for child in KNOWLEDGE_ROOT.iterdir() if child.is_dir() and not child.name.startswith("_")]
    auto_fix_markdown_paths(target_paths or [KNOWLEDGE_ROOT], emit=False)


def _check_kb_graph_cycles(path_filter=None):
    """Check for cycles in knowledge graph depends edges."""
    from .kb_graph import collect_knowledge_nodes, build_graph
    nodes = collect_knowledge_nodes()
    graph = build_graph(nodes)
    diags = []
    if graph["stats"]["cycles_in_depends"] > 0:
        diags.append(Diagnostic(
            check_id="kb-graph-cycles",
            severity="high",
            scope="repo",
            path="KNOWLEDGE/",
            message=f"{graph['stats']['cycles_in_depends']} cycle(s) in depends graph",
        ))
    for edge in graph.get("broken_edges", []):
        diags.append(Diagnostic(
            check_id="kb-graph-cycles",
            severity="medium",
            scope="artifact",
            path=edge["from"],
            message=f"Broken relation: --{edge['type']}--> {edge['to']}",
            fix_hint="Correct the URN in the relations field",
        ))
    return diags


def _check_knowledge_zone(path_filter=None):
    """Verify all files in KNOWLEDGE/{ns}/ (productivo) have valid _manifest.

    Excluye KNOWLEDGE/_SCRIPTORIUM/ (staging pre-categorial) del check: el
    SCRIPTORIUM acepta material crudo sin frontmatter.
    """
    import os
    from .config import KNOWLEDGE_ROOT, KORA_ROOT, SCRIPTORIUM_ROOT

    diags = []
    if not KNOWLEDGE_ROOT.exists():
        return diags

    scriptorium = SCRIPTORIUM_ROOT.resolve() if SCRIPTORIUM_ROOT.exists() else None

    def is_in_scriptorium(path: Path) -> bool:
        if scriptorium is None:
            return False
        try:
            resolved = path.resolve()
        except OSError:
            return False
        return resolved == scriptorium or scriptorium in resolved.parents

    for root, dirs, files in os.walk(KNOWLEDGE_ROOT):
        # Poda: no descender en _SCRIPTORIUM/
        dirs[:] = [d for d in dirs if d != "_SCRIPTORIUM"]
        for fname in sorted(files):
            fpath = Path(root) / fname
            if is_in_scriptorium(fpath):
                continue
            if fname == "README.md":
                continue
            if fname.endswith(".md"):
                try:
                    with open(fpath) as f:
                        head = f.read(2000)
                except Exception:
                    continue
                if "_manifest:" not in head:
                    rel = str(fpath.relative_to(KORA_ROOT))
                    diags.append(Diagnostic(
                        check_id="knowledge-zone",
                        severity="high",
                        scope="artifact",
                        path=rel,
                        message="File in KNOWLEDGE/{ns}/ lacks _manifest frontmatter",
                        fix_hint="Add KORA/MD frontmatter or move to KNOWLEDGE/_SCRIPTORIUM/INBOX/",
                    ))
            elif not fname.startswith("."):
                rel = str(fpath.relative_to(KORA_ROOT))
                diags.append(Diagnostic(
                    check_id="knowledge-zone",
                    severity="medium",
                    scope="artifact",
                    path=rel,
                    message=f"Non-markdown file in KNOWLEDGE/{{ns}}/: {fname}",
                    fix_hint="Move to KNOWLEDGE/_SCRIPTORIUM/INBOX/",
                ))

    if path_filter:
        diags = [d for d in diags if d.path.startswith(path_filter)]
    return diags


def _check_spec_traces(path_filter=None):
    """Verify Traces to: lines point to existing formal layer docs."""
    import re
    from .config import KORA_ROOT, KNOWLEDGE_ROOT
    from .graph import build_formal_trace_lookup

    specs_dir = KORA_ROOT / "specs"
    if not specs_dir.exists():
        return []

    formal_lookup = build_formal_trace_lookup()
    trace_pattern = re.compile(r"Traces to:\s*(.+)")
    section_pattern = re.compile(r"formal/(\d{2})\s+§([\d.]+)")
    diags = []

    for spec_file in sorted(specs_dir.glob("*.md")):
        content = spec_file.read_text(encoding="utf-8")
        for match in trace_pattern.finditer(content):
            trace_line = match.group(1)
            for doc_id, section in section_pattern.findall(trace_line):
                if doc_id not in formal_lookup:
                    diags.append(Diagnostic(
                        check_id="spec-traces",
                        severity="medium",
                        scope="artifact",
                        path=str(spec_file.relative_to(KORA_ROOT)),
                        message=f"Traces to formal/{doc_id} but no formal layer doc with prefix {doc_id} exists",
                    ))

    if path_filter:
        diags = [d for d in diags if d.path.startswith(path_filter)]
    return diags


def _check_supersedes_consistency(path_filter=None):
    """If A supersedes B, B must have status: deprecated."""
    from .kb_graph import collect_knowledge_nodes
    nodes = collect_knowledge_nodes()
    urn_to_status = {n["urn"]: n.get("status", "") for n in nodes if "urn" in n}
    diags = []
    for node in nodes:
        relations = node.get("relations", {})
        if not isinstance(relations, dict):
            continue
        targets = relations.get("supersedes", [])
        if isinstance(targets, str):
            targets = [targets]
        for target_urn in (targets or []):
            target_status = urn_to_status.get(target_urn, "")
            if target_status and target_status != "deprecated":
                diags.append(Diagnostic(
                    check_id="supersedes-consistency",
                    severity="medium",
                    scope="artifact",
                    path=node.get("file", node["urn"]),
                    message=f"Supersedes {target_urn} but target has status '{target_status}', expected 'deprecated'",
                    fix_hint=f"Set status: deprecated in {target_urn}",
                ))
    if path_filter:
        diags = [d for d in diags if d.path.startswith(path_filter)]
    return diags


def _check_agentfile_dimensions(path_filter=None):
    """Every AGENT.md must declare the real autoria dimensions in artefacto.*."""
    import os
    from .config import AGENTS_ROOT, KORA_ROOT, AGENTFILE_NAME
    from .artifacts import load_yaml_safe

    required_dims = {"perfil", "plan", "interfaz", "contexto", "invariantes"}
    diags = []

    if not AGENTS_ROOT.exists():
        return diags

    for ns_dir in sorted(AGENTS_ROOT.iterdir()):
        if not ns_dir.is_dir() or ns_dir.name.startswith((".", "_")):
            continue
        for ws_dir in sorted(ns_dir.iterdir()):
            if not ws_dir.is_dir():
                continue
            agentfile = ws_dir / AGENTFILE_NAME
            if not agentfile.exists():
                continue
            fm, err = load_yaml_safe(agentfile)
            if err or not isinstance(fm, dict):
                continue
            artefacto = fm.get("artefacto")
            if isinstance(artefacto, dict):
                required_for_file = set(required_dims)
                xi = (
                    ((fm.get("extensions") or {}).get("kora") or {})
                    .get("vector_ontologico", {})
                    .get("xi")
                )
                if isinstance(xi, int) and xi >= 4:
                    required_for_file.add("composicion")
                present = {
                    dim
                    for dim in required_for_file | {"composicion"}
                    if isinstance(artefacto.get(dim), dict)
                }
                missing = required_for_file - present
                message = f"AGENT.md missing artefacto dimensions: {', '.join(sorted(missing))}"
                fix_hint = "Add the missing artefacto.* dimensions to AGENT.md frontmatter"
            else:
                agent = fm.get("agent", {})
                if not isinstance(agent, dict):
                    continue
                legacy_dims = {"coalgebra", "plan", "interface", "fibers", "composition", "safety"}
                present = set(agent.keys()) & legacy_dims
                missing = legacy_dims - present
                message = f"AGENT.md missing legacy dimensions: {', '.join(sorted(missing))}"
                fix_hint = "Add the missing legacy agent.* dimensions to AGENT.md frontmatter"
            if missing:
                rel = str(agentfile.relative_to(KORA_ROOT))
                diags.append(Diagnostic(
                    check_id="agentfile-dimensions",
                    severity="medium",
                    scope="workspace",
                    path=rel,
                    message=message,
                    fix_hint=fix_hint,
                ))

    if path_filter:
        diags = [d for d in diags if d.path.startswith(path_filter)]
    return diags


def _check_tools_config_coherence(path_filter=None):
    """TOOLS.md and config.json tools.allow must match."""
    from .config import AGENTS_ROOT, KORA_ROOT
    from .workspaces import extract_declared_tool_headings, iter_agent_workspaces

    diags = []
    for ws_dir in iter_agent_workspaces():
        tools_md = ws_dir / "TOOLS.md"
        config_json = ws_dir / "config.json"
        if not tools_md.exists() or not config_json.exists():
            continue
        # Skip if AGENT.md exists (agentfile supersedes legacy)
        if (ws_dir / "AGENT.md").exists():
            continue

        _, valid_tools, _ = extract_declared_tool_headings(tools_md)
        try:
            config = json.loads(config_json.read_text(encoding="utf-8"))
        except Exception:
            continue
        config_tools = set(config.get("tools", {}).get("allow", []))
        tools_set = set(valid_tools)

        in_tools_not_config = tools_set - config_tools
        in_config_not_tools = config_tools - tools_set

        rel = str(ws_dir.relative_to(KORA_ROOT))
        if in_tools_not_config:
            diags.append(Diagnostic(
                check_id="tools-config-coherence",
                severity="medium",
                scope="workspace",
                path=rel,
                message=f"Tools in TOOLS.md but not in config.json: {', '.join(sorted(in_tools_not_config))}",
                fix_hint="Add to config.json tools.allow or remove from TOOLS.md",
            ))
        if in_config_not_tools:
            diags.append(Diagnostic(
                check_id="tools-config-coherence",
                severity="medium",
                scope="workspace",
                path=rel,
                message=f"Tools in config.json but not in TOOLS.md: {', '.join(sorted(in_config_not_tools))}",
                fix_hint="Add to TOOLS.md or remove from config.json",
            ))

    if path_filter:
        diags = [d for d in diags if d.path.startswith(path_filter)]
    return diags


def _fix_catalog_rebuild(diagnostics):
    """Rebuild the catalog — fix for catalog-exists."""
    from .catalog import cmd_index
    cmd_index()


def _check_skill_structure(path_filter=None):
    """Habilidades productivas cumplen la estructura portable (autoria-spec §5.1).

    Valida:
    - Subdirs productivos solo pueden ser {scripts, referencias, recursos}
      (glosario canonico espanol de autoria-spec §15.3).
    - Si existe alguno de esos subdirs, el SKILL.md menciona `## Recursos`.
    - No hay anidamiento `skills/CM-*` en habilidades productivas `activo`.

    Excluye skills en staging (_TALLER/) y bundles legacy CM-* (exentos).

    Los nombres en ingles (`references/`, `assets/`, `## Resources`) son
    proyecciones del transmutor a agentskills.io (autoria-spec §5.5) y no
    constituyen shape de autoria valido.
    """
    import re
    from .config import SKILLS_ROOT, KORA_ROOT

    CANONICAL_SUBDIRS = {"scripts", "referencias", "recursos"}
    # Mapa subdir -> heading esperado en ## Recursos
    SUBDIR_HEADINGS = {
        "scripts": "Scripts",
        "referencias": "Referencias",
        "recursos": "Recursos",
    }
    diags = []

    if not SKILLS_ROOT.exists():
        return diags

    def iter_productive_skills():
        for entry in sorted(SKILLS_ROOT.iterdir()):
            if not entry.is_dir() or entry.name.startswith((".", "_")):
                continue
            # Directo: SKILLS/{name}/SKILL.md
            if (entry / "SKILL.md").exists():
                yield entry
                continue
            # Con namespace: SKILLS/{ns}/{name}/SKILL.md
            for sub in sorted(entry.iterdir()):
                if not sub.is_dir() or sub.name.startswith((".", "_")):
                    continue
                if sub.name.startswith("CM-"):
                    continue  # perfil legacy, exento
                if (sub / "SKILL.md").exists():
                    yield sub

    for skill_dir in iter_productive_skills():
        rel = str(skill_dir.relative_to(KORA_ROOT))
        skill_md = skill_dir / "SKILL.md"

        # Check subdirs no canonicos
        present_canonical = set()
        for child in skill_dir.iterdir():
            if not child.is_dir() or child.name.startswith("."):
                continue
            if child.name in CANONICAL_SUBDIRS:
                present_canonical.add(child.name)
            elif child.name == "skills":
                # Anidamiento de sub-skills solo permitido en CM-* legacy
                diags.append(Diagnostic(
                    check_id="skill-structure",
                    severity="medium",
                    scope="artifact",
                    path=rel,
                    message="Habilidad productiva anida 'skills/' — composicionalidad debe declararse en extensions.kora.componible_con (autoria-spec §9)",
                    fix_hint="Extrae sub-habilidades a SKILLS/{name}/ top-level y referencialas via componible_con",
                ))
            else:
                diags.append(Diagnostic(
                    check_id="skill-structure",
                    severity="medium",
                    scope="artifact",
                    path=rel,
                    message=f"Subdir no canonico en habilidad productiva: '{child.name}' (canonicos: scripts, referencias, recursos)",
                    fix_hint=f"Renombra '{child.name}/' a referencias/ o recursos/ segun semantica (autoria-spec §5.1, §15.3)",
                ))

        # Check seccion ## Recursos cuando hay subdirs canonicos
        if present_canonical:
            try:
                body = skill_md.read_text(encoding="utf-8")
            except Exception:
                continue
            has_resources_section = bool(re.search(r"^##\s+Recursos\s*$", body, re.MULTILINE))
            if not has_resources_section:
                diags.append(Diagnostic(
                    check_id="skill-structure",
                    severity="medium",
                    scope="artifact",
                    path=rel,
                    message=f"Habilidad usa subdirs ({', '.join(sorted(present_canonical))}) pero body carece de seccion '## Recursos' (autoria-spec §5.1, §7.1)",
                    fix_hint="Agrega '## Recursos' al body del SKILL.md con subsecciones ### Scripts, ### Referencias, ### Recursos segun corresponda",
                ))
            else:
                # Validar que cada subdir presente tiene subseccion
                for subdir in sorted(present_canonical):
                    heading = SUBDIR_HEADINGS[subdir]
                    if not re.search(rf"^###\s+{heading}\s*$", body, re.MULTILINE):
                        diags.append(Diagnostic(
                            check_id="skill-structure",
                            severity="low",
                            scope="artifact",
                            path=rel,
                            message=f"Subdir '{subdir}/' presente pero sin subseccion '### {heading}' en ## Recursos",
                            fix_hint=f"Agrega subseccion '### {heading}' describiendo el uso de {subdir}/",
                        ))

    if path_filter:
        diags = [d for d in diags if d.path.startswith(path_filter)]
    return diags


def _fix_autoria_conformance(diagnostics):
    """Adjoint izquierdo PARCIAL de `autoria-conformance`.

    Factoriza el check en dos sub-functores:
      Check = CheckRenames  (+)  CheckFibra
      Fix   = FixRenames        (FixFibra no existe)

    `FixRenames = migrate_to_autoria` cubre diagnostics mecanicamente
    reparables (codes envelope-urn-formato, envelope-type-artefacto,
    envelope-nombre/descripcion-requerida, envelope-status-enum,
    atlas-*-enum). Los diagnostics de fibra (forma-* bounds, compromisos
    eticos, nivel_prescripcion faltante) requieren autor humano — son
    residual tras aplicar el fix.

    Propiedades esperadas (tests las verifican):
      - Idempotencia:   fix . fix = fix
      - Reduccion:      diagnose . fix  no contiene codes rename-like
    """
    from .migration import migrate_to_autoria
    migrate_to_autoria(dry_run=False)


def _check_autoria_conformance(path_filter=None):
    """Artefactos productivos (AGENT.md + SKILL.md) conforman a autoria-spec v1.0.

    Morfismo: cada artefacto se proyecta sobre atlas.forma_material y se
    compone con el functor R de reglas (pullback). Implementacion vive en
    `kora_lib.autoria_validate` como composicion funcional pura.

    Este check es la superficie de reporting del validador; las reglas
    individuales y su estructura monoidal estan en autoria_validate.
    """
    from .artifacts import load_yaml_safe
    from .autoria_validate import validate
    from .config import AGENTS_ROOT, KORA_ROOT, SKILLS_ROOT

    diags = []

    def iter_productive_artifacts():
        if AGENTS_ROOT.exists():
            for ns_dir in sorted(AGENTS_ROOT.iterdir()):
                if not ns_dir.is_dir() or ns_dir.name.startswith((".", "_")):
                    continue
                for ws_dir in sorted(ns_dir.iterdir()):
                    if not ws_dir.is_dir() or ws_dir.name.startswith((".", "_")):
                        continue
                    agent_md = ws_dir / "AGENT.md"
                    if agent_md.exists():
                        yield agent_md
        if SKILLS_ROOT.exists():
            for entry in sorted(SKILLS_ROOT.iterdir()):
                if not entry.is_dir() or entry.name.startswith((".", "_")):
                    continue
                direct = entry / "SKILL.md"
                if direct.exists():
                    yield direct
                    continue
                for sub in sorted(entry.iterdir()):
                    if not sub.is_dir() or sub.name.startswith((".", "_")):
                        continue
                    candidate = sub / "SKILL.md"
                    if candidate.exists():
                        yield candidate

    for artifact_path in iter_productive_artifacts():
        frontmatter, err = load_yaml_safe(artifact_path)
        if err or not isinstance(frontmatter, dict):
            continue
        rel = str(artifact_path.relative_to(KORA_ROOT))
        scope_kind = "workspace" if artifact_path.name == "AGENT.md" else "artifact"
        for d in validate(frontmatter):
            diags.append(Diagnostic(
                check_id="autoria-conformance",
                severity=d.severity,
                scope=scope_kind,
                path=rel,
                message=f"{d.code} @ {d.path}: {d.message}",
                fix_hint="Run `kora migrate --perfil a-autoria` para renames estructurales; campos de shape/invariantes son manuales.",
            ))

    if path_filter:
        diags = [d for d in diags if d.path.startswith(path_filter)]
    return diags


# ---------------------------------------------------------------------------
# Registration — wire up all built-in checks
# ---------------------------------------------------------------------------

def _register_builtins():
    register_check(
        Check("catalog-exists", "Catalog exists and is loadable",
              scope="repo", severity="critical", enforcement="schema",
              spec_ref="gobernanza §7.1", phase="index"),
        _check_catalog_exists,
        _fix_catalog_rebuild,
    )
    register_check(
        Check("urn-integrity", "All URN references resolve to existing entries",
              scope="repo", severity="high", enforcement="lint",
              spec_ref="gobernanza §8.2", depends=("catalog-exists",), phase="verify"),
        _check_urn_integrity,
    )
    register_check(
        Check("workspace-validity", "Workspaces validate against schema + semantics",
              scope="workspace", severity="high", enforcement="schema",
              spec_ref="autoria-spec §3, §6; legacy-compat profile", depends=("catalog-exists",), phase="verify"),
        _check_workspace_validity,
    )
    register_check(
        Check("knowledge-zone", "KNOWLEDGE/ contains only valid KORA/MD artifacts",
              scope="artifact", severity="high", enforcement="lint",
              spec_ref="knowledge-spec §3.1, §8.1", phase="verify"),
        _check_knowledge_zone,
    )
    register_check(
        Check("lint-md", "KORA/MD artifacts pass structural lint",
              scope="artifact", severity="low", enforcement="lint",
              spec_ref="md-spec §5", depends=("knowledge-zone",), phase="lint"),
        _check_lint_md,
        _fix_lint_md,
    )
    register_check(
        Check("kb-graph-cycles", "Knowledge graph has no cycles in depends",
              scope="repo", severity="high", enforcement="lint",
              spec_ref="knowledge-spec §4.3, §7.3", depends=("knowledge-zone",), phase="graph"),
        _check_kb_graph_cycles,
    )
    register_check(
        Check("spec-traces", "Traces to: lines point to existing formal layer docs",
              scope="artifact", severity="medium", enforcement="lint",
              spec_ref="gobernanza §5.1", phase="verify"),
        _check_spec_traces,
    )
    register_check(
        Check("supersedes-consistency", "Supersedes targets must be deprecated",
              scope="artifact", severity="medium", enforcement="lint",
              spec_ref="knowledge-spec §4.3", depends=("knowledge-zone",), phase="graph"),
        _check_supersedes_consistency,
    )
    register_check(
        Check("agentfile-dimensions", "AGENT.md declares required artefacto dimensions",
              scope="workspace", severity="medium", enforcement="schema",
              spec_ref="autoria-spec §3.4, §5.2-§5.4", depends=("catalog-exists",), phase="verify"),
        _check_agentfile_dimensions,
    )
    register_check(
        Check("tools-config-coherence", "TOOLS.md and config.json tools.allow match",
              scope="workspace", severity="medium", enforcement="lint",
              spec_ref="agentfile-spec legacy-compat profile", depends=("catalog-exists",), phase="verify"),
        _check_tools_config_coherence,
    )
    register_check(
        Check("skill-structure", "Habilidades productivas siguen estructura portable (scripts/referencias/recursos + ## Recursos)",
              scope="artifact", severity="medium", enforcement="lint",
              spec_ref="autoria-spec §5.1, §5.5, §15.3", phase="verify"),
        _check_skill_structure,
    )
    register_check(
        Check("autoria-conformance",
              "Artefactos productivos (AGENT.md + SKILL.md) conforman a autoria-spec v1.0 (universal + fibra por forma material)",
              scope="artifact", severity="high", enforcement="schema",
              spec_ref="autoria-spec §3, §6", depends=("catalog-exists",), phase="verify"),
        _check_autoria_conformance,
        _fix_autoria_conformance,
    )


# Auto-register on module import
_register_builtins()
