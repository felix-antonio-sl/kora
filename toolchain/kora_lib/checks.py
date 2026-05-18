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
import re


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
            path="docs/generated/catalog.yml",
            message="Catalog not found or invalid. Run 'kora index' first.",
            fix_hint="python3 toolchain/kora index",
        )]
    return []


def _check_urn_integrity(path_filter=None):
    """Verify all URN references resolve to existing catalog entries."""
    from .catalog import build_catalog_lookup, get_reference_entry, load_catalog, urn_is_known
    from .config import (
        AGENTS_ROOT,
        DEPRECATED_URN_ALIASES,
        KORA_ROOT,
        RETIRED_KB_URNS,
    )
    from .graph import build_reference_graph
    from .workspaces import fragment_exists

    doc = load_catalog()
    if not doc or "Catalog" not in doc:
        return []  # catalog-exists check will catch this

    known_urns, urn_to_entry = build_catalog_lookup(doc)
    _scanned, edges = build_reference_graph()
    aliases_to_retired = {
        alias for alias, canonical in DEPRECATED_URN_ALIASES.items()
        if canonical in RETIRED_KB_URNS
    }
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
            if edge.target in aliases_to_retired:
                canonical = DEPRECATED_URN_ALIASES[edge.target]
                diags.append(Diagnostic(
                    check_id="urn-integrity",
                    severity="high",
                    scope="artifact",
                    path=str(edge.source.relative_to(KORA_ROOT)),
                    message=(
                        f"Deprecated alias points to retired URN: "
                        f"{edge.target} -> {canonical} (RETIRED). "
                        "Migrate to current spec."
                    ),
                    fix_hint="Replace with the live URN that supersedes it",
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


def _check_bundle_coherence(path_filter=None):
    """Verify declarative AGENT.md deps resolve and point to productive artifacts."""
    from .artifacts import load_yaml_safe
    from .catalog import build_catalog_lookup, get_reference_entry, load_catalog, urn_is_known
    from .config import KORA_ROOT
    from .workspaces import iter_agent_workspaces

    doc = load_catalog()
    if not doc or "Catalog" not in doc:
        return []

    known_urns, urn_to_entry = build_catalog_lookup(doc)
    diags = []

    def _is_productive_entry(entry: dict | None) -> bool:
        if not entry:
            return False
        rel_path = str(entry["file"].relative_to(KORA_ROOT))
        return not any(marker in rel_path for marker in ("/_FRAGUA/", "/_TALLER/", "/_SCRIPTORIUM/"))

    for workspace_dir in iter_agent_workspaces():
        agent_md = workspace_dir / "AGENT.md"
        frontmatter, _ = load_yaml_safe(agent_md)
        if not isinstance(frontmatter, dict):
            continue
        kora_ext = (frontmatter.get("extensions") or {}).get("kora") or {}
        deps = []
        for field_name in ("conocimiento_permitido", "componible_con"):
            values = kora_ext.get(field_name) or []
            if isinstance(values, list):
                for urn in values:
                    if isinstance(urn, str) and urn:
                        deps.append((field_name, urn))
        if not deps:
            continue

        rel = str(agent_md.relative_to(KORA_ROOT))
        for field_name, urn in deps:
            if not urn_is_known(urn, known_urns):
                diags.append(Diagnostic(
                    check_id="bundle-coherence",
                    severity="high",
                    scope="workspace",
                    path=rel,
                    message=f"{field_name} declara URN inexistente: {urn}",
                    fix_hint="Corrige el URN o elimina la referencia",
                ))
                continue
            entry = get_reference_entry(urn, urn_to_entry)
            if not _is_productive_entry(entry):
                diags.append(Diagnostic(
                    check_id="bundle-coherence",
                    severity="high",
                    scope="workspace",
                    path=rel,
                    message=f"{field_name} apunta a artefacto no productivo: {urn}",
                    fix_hint="Promueve el artefacto objetivo o cambia la referencia a uno productivo",
                ))

    if path_filter:
        diags = [d for d in diags if d.path.startswith(path_filter)]
    return diags


def _check_lint_md(path_filter=None):
    """Lint published KORA/MD artifacts."""
    from .config import KORA_ROOT, KNOWLEDGE_ROOT, SPEC_ROOTS
    from .validation import lint_markdown_paths

    knowledge_paths = [child for child in KNOWLEDGE_ROOT.iterdir() if child.is_dir() and not child.name.startswith("_")]
    target_paths = [*(knowledge_paths or [KNOWLEDGE_ROOT]), *SPEC_ROOTS]
    if path_filter:
        candidate = KORA_ROOT / path_filter
        if candidate.exists():
            target_paths = [candidate]

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
                fix_hint="python3 toolchain/kora lint-md --fix",
            ))
        elif isinstance(issue, dict):
            diags.append(Diagnostic(
                check_id="lint-md",
                severity="low",
                scope="artifact",
                path=issue.get("path", ""),
                message=issue.get("message", str(issue)),
                fix_hint="python3 toolchain/kora lint-md --fix",
            ))
    return diags


def _fix_lint_md(diagnostics):
    """Auto-fix lint issues."""
    from .config import KNOWLEDGE_ROOT, SPEC_ROOTS
    from .validation import auto_fix_markdown_paths
    knowledge_paths = [child for child in KNOWLEDGE_ROOT.iterdir() if child.is_dir() and not child.name.startswith("_")]
    auto_fix_markdown_paths([*(knowledge_paths or [KNOWLEDGE_ROOT]), *SPEC_ROOTS], emit=False)


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
            path="artifacts/knowledge/",
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


def _collect_relation_edges(relation_type):
    """Recolecta los edges de un tipo de relacion desde frontmatter publicado.

    Retorna lista de tuplas (source_urn, target_urn, source_file_rel).
    """
    from .config import KORA_ROOT
    from .kb_graph import collect_knowledge_nodes

    edges = []
    for node in collect_knowledge_nodes():
        relations = node.get("relations") or {}
        if not isinstance(relations, dict):
            continue
        targets = relations.get(relation_type) or []
        if isinstance(targets, str):
            targets = [targets]
        if not isinstance(targets, list):
            continue
        source_urn = node.get("urn")
        source_file = node.get("file", "")
        for target in targets:
            if isinstance(target, str) and source_urn:
                edges.append((source_urn, target, source_file))
    return edges


def _find_cycles(edges):
    """Detecta nodos involucrados en ciclos. Algoritmo: DFS con tres-color.

    Retorna conjunto de URNs que pertenecen a algun ciclo.
    """
    from collections import defaultdict

    graph = defaultdict(list)
    nodes = set()
    for src, tgt, _ in edges:
        graph[src].append(tgt)
        nodes.add(src)
        nodes.add(tgt)

    WHITE, GRAY, BLACK = 0, 1, 2
    color = {n: WHITE for n in nodes}
    in_cycle = set()

    def dfs(start):
        stack = [(start, iter(graph[start]))]
        path = [start]
        color[start] = GRAY
        while stack:
            node, neighbors = stack[-1]
            try:
                nxt = next(neighbors)
            except StopIteration:
                color[node] = BLACK
                stack.pop()
                path.pop()
                continue
            if color.get(nxt, WHITE) == GRAY:
                # ciclo detectado: marcar todos en el camino desde nxt
                idx = path.index(nxt) if nxt in path else 0
                for n in path[idx:]:
                    in_cycle.add(n)
                in_cycle.add(nxt)
            elif color.get(nxt, WHITE) == WHITE:
                color[nxt] = GRAY
                path.append(nxt)
                stack.append((nxt, iter(graph[nxt])))
    for n in nodes:
        if color[n] == WHITE:
            dfs(n)
    return in_cycle


def _check_relations_laws(path_filter=None):
    """Verifica leyes algebraicas por tipo de relacion (knowledge-spec §6.3).

    Reglas verificadas:
      - aciclicidad de `supersedes`
      - aciclicidad de `refines`
      - antisimetria de `supersedes` (si A->B existe, B->A no debe existir)

    `cites` y `traces_requirements` no tienen estructura de orden y solo
    requieren resolubilidad (cubierto por `urn-integrity`).
    `depends` tiene su check dedicado `kb-graph-cycles`.
    """
    from .config import KORA_ROOT

    diags = []

    # Aciclicidad de supersedes
    supersedes_edges = _collect_relation_edges("supersedes")
    super_cycles = _find_cycles(supersedes_edges)
    for src, tgt, src_file in supersedes_edges:
        if src in super_cycles and tgt in super_cycles:
            try:
                rel = str(Path(src_file).relative_to(KORA_ROOT)) if src_file else ""
            except ValueError:
                rel = str(src_file)
            diags.append(Diagnostic(
                check_id="relations-laws",
                severity="high",
                scope="artifact",
                path=rel,
                message=(
                    f"`supersedes`: ciclo detectado que incluye {src} -> {tgt} "
                    "(knowledge-spec §6.3 r1: aciclicidad obligatoria)."
                ),
                fix_hint="Corta el ciclo: elimina supersedes que cierre la cadena o reemplaza por cites.",
            ))

    # Aciclicidad de refines
    refines_edges = _collect_relation_edges("refines")
    refines_cycles = _find_cycles(refines_edges)
    for src, tgt, src_file in refines_edges:
        if src in refines_cycles and tgt in refines_cycles:
            try:
                rel = str(Path(src_file).relative_to(KORA_ROOT)) if src_file else ""
            except ValueError:
                rel = str(src_file)
            diags.append(Diagnostic(
                check_id="relations-laws",
                severity="high",
                scope="artifact",
                path=rel,
                message=(
                    f"`refines`: ciclo detectado que incluye {src} -> {tgt} "
                    "(knowledge-spec §6.3 r3: aciclicidad obligatoria)."
                ),
                fix_hint="Corta el ciclo: elimina refines que cierre la cadena o reemplaza por cites.",
            ))

    # Antisimetria de supersedes
    super_pairs = {(src, tgt): src_file for src, tgt, src_file in supersedes_edges}
    seen_bidirectional = set()
    for (src, tgt), src_file in super_pairs.items():
        if (tgt, src) in super_pairs and (src, tgt) not in seen_bidirectional:
            seen_bidirectional.add((src, tgt))
            seen_bidirectional.add((tgt, src))
            try:
                rel = str(Path(src_file).relative_to(KORA_ROOT)) if src_file else ""
            except ValueError:
                rel = str(src_file)
            diags.append(Diagnostic(
                check_id="relations-laws",
                severity="high",
                scope="artifact",
                path=rel,
                message=(
                    f"`supersedes` no es antisimetrica: {src} <-> {tgt} "
                    "(knowledge-spec §6.3 r2: A supersedes B implica que B NO supersede A)."
                ),
                fix_hint="Decide direccion temporal: solo uno de los dos artefactos sucede al otro.",
            ))

    if path_filter:
        diags = [d for d in diags if d.path.startswith(path_filter)]
    return diags


def _check_knowledge_zone(path_filter=None):
    """Verify artefactos en artifacts/knowledge/{ns}/ cumplen las invariantes del pipeline.

    Reglas que aplica (knowledge-spec §3.2, §4.2):
      1. Todo .md productivo tiene `_manifest` valido (URN + status).
      2. status pertenece a {publicado, deprecado} (no borrador).
      3. namespace del URN coincide con el primer subdirectorio bajo
         artifacts/knowledge/.

    Excluye artifacts/knowledge/_SCRIPTORIUM/ del check: el SCRIPTORIUM acepta
    material crudo sin frontmatter (knowledge-spec §8.1 r3).
    """
    import os
    from .artifacts import load_markdown_parts
    from .config import KNOWLEDGE_ROOT, KORA_ROOT, SCRIPTORIUM_ROOT
    from .lifecycle import canonicalize_status

    diags = []
    if not KNOWLEDGE_ROOT.exists():
        return diags

    scriptorium = SCRIPTORIUM_ROOT.resolve() if SCRIPTORIUM_ROOT.exists() else None
    productive_statuses = {"publicado", "deprecado"}

    def is_in_scriptorium(path: Path) -> bool:
        if scriptorium is None:
            return False
        try:
            resolved = path.resolve()
        except OSError:
            return False
        return resolved == scriptorium or scriptorium in resolved.parents

    def first_subdir(rel_path: Path) -> str:
        parts = rel_path.parts
        # rel_path es relativa a KNOWLEDGE_ROOT; el primer componente es el ns.
        return parts[0] if parts else ""

    def urn_namespace(urn: str) -> str:
        # urn:{ns}:{type}:{id} → {ns}
        if not isinstance(urn, str) or not urn.startswith("urn:"):
            return ""
        parts = urn.split(":")
        return parts[1] if len(parts) >= 3 else ""

    for root, dirs, files in os.walk(KNOWLEDGE_ROOT):
        # Poda: no descender en _SCRIPTORIUM/
        dirs[:] = [d for d in dirs if d != "_SCRIPTORIUM"]
        for fname in sorted(files):
            fpath = Path(root) / fname
            if is_in_scriptorium(fpath):
                continue
            if fname == "README.md":
                continue
            rel = str(fpath.relative_to(KORA_ROOT))
            rel_to_knowledge = fpath.relative_to(KNOWLEDGE_ROOT)
            ns_subdir = first_subdir(rel_to_knowledge)

            if fname.endswith(".md"):
                try:
                    with open(fpath) as f:
                        head = f.read(2000)
                except Exception:
                    continue
                if "_manifest:" not in head:
                    diags.append(Diagnostic(
                        check_id="knowledge-zone",
                        severity="high",
                        scope="artifact",
                        path=rel,
                        message="File in artifacts/knowledge/{ns}/ lacks _manifest frontmatter",
                        fix_hint="Add KORA/MD frontmatter or move to artifacts/knowledge/_SCRIPTORIUM/INBOX/",
                    ))
                    continue
                # Regla 2 + 3: status-por-directorio y namespace-directorio
                try:
                    frontmatter, _body = load_markdown_parts(fpath)
                except Exception:
                    continue
                if not isinstance(frontmatter, dict):
                    continue
                manifest = frontmatter.get("_manifest") or {}
                status = canonicalize_status(
                    frontmatter.get("status") or manifest.get("status") or ""
                )
                if status and status not in productive_statuses:
                    diags.append(Diagnostic(
                        check_id="knowledge-zone",
                        severity="high",
                        scope="artifact",
                        path=rel,
                        message=(
                            f"status: {status} no es valido en artifacts/knowledge/{ns_subdir}/ "
                            f"(knowledge-spec §4.2: solo publicado o deprecado)"
                        ),
                        fix_hint=(
                            "Mover a artifacts/knowledge/_SCRIPTORIUM/REVIEW/ o promover con "
                            "`python3 toolchain/kora promote`."
                        ),
                    ))
                urn = manifest.get("urn", "")
                urn_ns = urn_namespace(urn)
                if urn_ns and ns_subdir and urn_ns != ns_subdir:
                    diags.append(Diagnostic(
                        check_id="knowledge-zone",
                        severity="high",
                        scope="artifact",
                        path=rel,
                        message=(
                            f"namespace del URN ('{urn_ns}') no coincide con subdirectorio "
                            f"('{ns_subdir}') (knowledge-spec §3.2)"
                        ),
                        fix_hint=(
                            f"Reubicar a artifacts/knowledge/{urn_ns}/ o corregir el URN."
                        ),
                    ))
            elif not fname.startswith("."):
                diags.append(Diagnostic(
                    check_id="knowledge-zone",
                    severity="medium",
                    scope="artifact",
                    path=rel,
                    message=f"Non-markdown file in artifacts/knowledge/{{ns}}/: {fname}",
                    fix_hint="Move to artifacts/knowledge/_SCRIPTORIUM/INBOX/",
                ))

    if path_filter:
        diags = [d for d in diags if d.path.startswith(path_filter)]
    return diags


def _check_spec_traces(path_filter=None):
    """Verify Traces to: lines point to existing formal layer docs."""
    import re
    from .config import KORA_ROOT, KNOWLEDGE_ROOT, SPEC_ROOTS
    from .graph import build_formal_trace_lookup

    spec_files = []
    for spec_root in SPEC_ROOTS:
        if spec_root.exists():
            spec_files.extend(sorted(spec_root.glob("*.md")))
    if not spec_files:
        return []

    formal_lookup = build_formal_trace_lookup()
    trace_pattern = re.compile(r"Traces to:\s*(.+)")
    section_pattern = re.compile(r"formal/(\d{2})\s+§([\d.]+)")
    diags = []

    for spec_file in spec_files:
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


def _check_formal_trace_discipline(path_filter=None):
    """Verify `Traces to:` URNs stay inside the official KORA Formal Layer.

    `Rationale:` may cite auxiliary corpora such as FXSL/ICAS. `Traces to:` is
    reserved for formal traceability to `artifacts/knowledge/kora/categorical-foundations/`.
    """
    import re
    from .catalog import build_catalog_lookup, load_catalog, urn_is_known
    from .config import KORA_ROOT

    doc = load_catalog()
    known_urns, urn_to_entry = build_catalog_lookup(doc) if doc else (set(), {})
    scan_roots = (
        "governance",
        "ontology",
        "serialization",
        "runtime",
        "artifacts/skills",
        "artifacts/agents",
        "artifacts/knowledge/kora",
    )
    excluded_markers = ("/_SCRIPTORIUM/", "/_TALLER/INBOX/", "/_FRAGUA/INBOX/")
    trace_pattern = re.compile(r"Traces to:\s*(.+)")
    urn_pattern = re.compile(r"urn:[a-z0-9\-]+:[a-z0-9\-]+:[A-Za-z0-9_.\-{}]+")
    formal_prefix = "artifacts/knowledge/kora/categorical-foundations/"
    diags = []

    for rel_root in scan_roots:
        root = KORA_ROOT / rel_root
        if not root.exists():
            continue
        for md_path in sorted(root.rglob("*.md")):
            rel = str(md_path.relative_to(KORA_ROOT))
            if any(marker in f"/{rel}" for marker in excluded_markers):
                continue
            if path_filter and not rel.startswith(path_filter):
                continue
            try:
                text = md_path.read_text(encoding="utf-8")
            except (OSError, UnicodeDecodeError):
                continue
            for line_no, line in enumerate(text.splitlines(), start=1):
                match = trace_pattern.search(line)
                if not match:
                    continue
                for urn in urn_pattern.findall(match.group(1)):
                    if "{" in urn or "}" in urn or urn.endswith("-"):
                        continue
                    if not urn_is_known(urn, known_urns):
                        diags.append(Diagnostic(
                            check_id="formal-trace-discipline",
                            severity="medium",
                            scope="artifact",
                            path=rel,
                            message=f"line {line_no}: Traces to unresolved URN {urn}",
                            fix_hint="Use a resolvable Formal Layer URN or move this citation to Rationale.",
                        ))
                        continue
                    entry = urn_to_entry.get(urn)
                    target_rel = str(entry["file"].relative_to(KORA_ROOT)) if entry else ""
                    if not target_rel.startswith(formal_prefix):
                        diags.append(Diagnostic(
                            check_id="formal-trace-discipline",
                            severity="medium",
                            scope="artifact",
                            path=rel,
                            message=f"line {line_no}: Traces to {urn}, outside official Formal Layer",
                            fix_hint="Trace to urn:kora:kb:cat-* (or another URN under categorical-foundations) and cite auxiliary material as Rationale.",
                        ))

    return diags


def _check_supersedes_consistency(path_filter=None):
    """If A supersedes B, B must have status: deprecated."""
    from .kb_graph import collect_knowledge_nodes
    from .lifecycle import is_deprecated_status
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
            if target_status and not is_deprecated_status(target_status):
                diags.append(Diagnostic(
                    check_id="supersedes-consistency",
                    severity="medium",
                    scope="artifact",
                    path=node.get("file", node["urn"]),
                    message=f"Supersedes {target_urn} but target has status '{target_status}', expected 'deprecado'",
                    fix_hint=f"Set status: deprecado in {target_urn}",
                ))
    if path_filter:
        diags = [d for d in diags if d.path.startswith(path_filter)]
    return diags


def _check_traces_requirements_semantics(path_filter=None):
    """Verify traces_requirements targets point to requirement-like nodes."""
    from .kb_graph import collect_knowledge_nodes

    nodes = collect_knowledge_nodes()
    node_by_urn = {n["urn"]: n for n in nodes if "urn" in n}
    diags = []

    for node in nodes:
        relations = node.get("relations", {})
        if not isinstance(relations, dict):
            continue
        targets = relations.get("traces_requirements", [])
        if isinstance(targets, str):
            targets = [targets]
        if not isinstance(targets, list):
            continue
        for target_urn in targets:
            target = node_by_urn.get(target_urn)
            if not target:
                continue
            if target.get("is_requirement") is True:
                continue
            diags.append(Diagnostic(
                check_id="traces-requirements-semantics",
                severity="high",
                scope="artifact",
                path=node.get("file", node["urn"]),
                message=f"traces_requirements points to non-requirement node: {target_urn}",
                fix_hint="Mark the target as a requirement or replace traces_requirements with cites/depends",
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
                previous_dims = {"coalgebra", "plan", "interface", "fibers", "composition", "safety"}
                present = set(agent.keys()) & previous_dims
                missing = previous_dims - present
                message = f"AGENT.md missing prior-shape dimensions: {', '.join(sorted(missing))}"
                fix_hint = "Add the missing prior-shape agent.* dimensions to AGENT.md frontmatter"
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
        # Skip if AGENT.md exists (agentfile supersedes prior scaffold)
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

    Excluye skills en staging (_TALLER/) y bundles historicos CM-* (exentos).

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
            # Directo: artifacts/skills/{name}/SKILL.md
            if (entry / "SKILL.md").exists():
                yield entry
                continue
            # Con namespace: artifacts/skills/{ns}/{name}/SKILL.md
            for sub in sorted(entry.iterdir()):
                if not sub.is_dir() or sub.name.startswith((".", "_")):
                    continue
                if sub.name.startswith("CM-"):
                    continue  # perfil historico, exento
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
            # _BUILD/ es output de transmutacion (gitignored), exento
            if child.name == "_BUILD":
                continue
            if child.name in CANONICAL_SUBDIRS:
                present_canonical.add(child.name)
            elif child.name == "skills":
                # Anidamiento de sub-skills solo permitido en CM-* historicos
                diags.append(Diagnostic(
                    check_id="skill-structure",
                    severity="medium",
                    scope="artifact",
                    path=rel,
                    message="Habilidad productiva anida 'skills/' — composicionalidad debe declararse en extensions.kora.componible_con (autoria-spec §9)",
                    fix_hint="Extrae sub-habilidades a artifacts/skills/{ns}/{name}/ y referencialas via componible_con",
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
    """Artefactos productivos (AGENT.md + SKILL.md) conforman a autoria-spec v1.2.

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

    from .lifecycle import canonicalize_status
    productive_statuses = {"activo", "deprecado", "retirado"}

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

        # Status-por-directorio: artefactos agenticos productivos solo en {activo, deprecado, retirado}
        # (autoria-spec §11 lifecycle). `borrador` queda restringido a _FRAGUA/REVIEW o _TALLER/REVIEW.
        status = canonicalize_status(frontmatter.get("status") or "")
        if status and status not in productive_statuses:
            diags.append(Diagnostic(
                check_id="autoria-conformance",
                severity="high",
                scope=scope_kind,
                path=rel,
                message=(
                    f"status: {status} no es valido en zona productiva "
                    f"(autoria-spec §11: solo activo/deprecado/retirado; borrador queda en staging)."
                ),
                fix_hint=(
                    "Mover a _FRAGUA/REVIEW o _TALLER/REVIEW, o promover con `kora promote`."
                ),
            ))

        # Namespace-directorio: el ns del URN coincide con el primer subdir bajo agents/ o skills/.
        # (autoria-spec §10.1 + paralelo a knowledge-spec §3.2).
        urn = (frontmatter.get("_manifest") or {}).get("urn", "")
        if isinstance(urn, str) and urn.startswith("urn:"):
            urn_parts = urn.split(":")
            urn_ns = urn_parts[1] if len(urn_parts) >= 3 else ""
            # Path: artifacts/agents/{ns}/{name}/AGENT.md o artifacts/skills/{ns}/{name}/SKILL.md
            try:
                rel_parts = artifact_path.relative_to(KORA_ROOT).parts
            except ValueError:
                rel_parts = ()
            # artifacts/{type}/{ns}/{name}/{FILE}
            if len(rel_parts) >= 5 and rel_parts[0] == "artifacts" and rel_parts[1] in ("agents", "skills"):
                subdir_ns = rel_parts[2]
                if urn_ns and urn_ns != subdir_ns:
                    diags.append(Diagnostic(
                        check_id="autoria-conformance",
                        severity="high",
                        scope=scope_kind,
                        path=rel,
                        message=(
                            f"namespace del URN ('{urn_ns}') no coincide con subdirectorio "
                            f"('{subdir_ns}') (autoria-spec §10.1)"
                        ),
                        fix_hint=(
                            f"Reubicar a artifacts/{rel_parts[1]}/{urn_ns}/ o corregir el URN."
                        ),
                    ))

    if path_filter:
        diags = [d for d in diags if d.path.startswith(path_filter)]
    return diags


def _check_vector_laws(path_filter=None):
    """Verifica las 5 leyes inter-eje declaradas en harness-spec §4.1.

    Leyes obligatorias (vector mal-formado si se violan):
      L1. Π>=3 ⟹ Μ>=1   (fixed-points requieren estado)
      L2. Ξ=4  ⟹ Λ>=1   (operad dinamica requiere composicion organizacional)
      L3. Φ>=2 ⟹ Μ>=1   (colaborativo requiere memoria observable)
      L4. Σ.accountability>=2 ⟹ Σ.transparency>=2   (responsabilidad requiere explicabilidad)
      L5. Λ=3  ⟹ Σᵢ>=2 para todo i   (sociedad requiere compromisos eticos completos)

    Se aplica a todo artefacto productivo con vector_ontologico declarado.
    """
    from .artifacts import load_yaml_safe
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
                    am = ws_dir / "AGENT.md"
                    if am.exists():
                        yield am
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
        fm, err = load_yaml_safe(artifact_path)
        if err or not isinstance(fm, dict):
            continue
        kora_ext = (fm.get("extensions") or {}).get("kora") or {}
        v = kora_ext.get("vector_ontologico") or kora_ext.get("harness_vector")
        if not isinstance(v, dict):
            continue

        pi = v.get("pi")
        mu = v.get("mu")
        xi = v.get("xi")
        lam = v.get("lambda")
        phi = v.get("phi")
        sigma = v.get("sigma") or []

        rel = str(artifact_path.relative_to(KORA_ROOT))
        scope_kind = "workspace" if artifact_path.name == "AGENT.md" else "artifact"

        def emit(code, msg, fix):
            diags.append(Diagnostic(
                check_id="vector-laws",
                severity="high",
                scope=scope_kind,
                path=rel,
                message=f"{code}: {msg}",
                fix_hint=fix,
            ))

        if isinstance(pi, int) and isinstance(mu, int):
            if pi >= 3 and mu < 1:
                emit("L1-pi-requiere-mu", f"Π={pi} requiere Μ>=1 (fixed-points necesitan estado); encontrado Μ={mu}",
                     "Sube mu a >=1 o baja pi a <=2")
        if isinstance(xi, int) and isinstance(lam, int):
            if xi == 4 and lam < 1:
                emit("L2-xi-requiere-lambda", f"Ξ=4 (operad dinamica) requiere Λ>=1; encontrado Λ={lam}",
                     "Declara composicion organizacional (Λ>=1) o baja xi a <=3")
        if isinstance(phi, int) and isinstance(mu, int):
            if phi >= 2 and mu < 1:
                emit("L3-phi-requiere-mu", f"Φ={phi} (colaborativo) requiere Μ>=1; encontrado Μ={mu}",
                     "Sube mu a >=1 o baja phi a <=1")
        if isinstance(sigma, list) and len(sigma) == 5:
            acc = sigma[3]
            trans = sigma[2]
            if isinstance(acc, int) and isinstance(trans, int):
                if acc >= 2 and trans < 2:
                    emit("L4-accountability-requiere-transparency",
                         f"Σ.accountability={acc} requiere Σ.transparency>=2; encontrado transparency={trans}",
                         "Sube transparency a >=2 o baja accountability a <=1")
        if isinstance(lam, int) and lam == 3 and isinstance(sigma, list) and len(sigma) == 5:
            low = [i for i, v in enumerate(sigma) if not isinstance(v, int) or v < 2]
            if low:
                emit("L5-sociedad-requiere-sigma-completo",
                     f"Λ=3 requiere todos los componentes de Σ>=2; insuficientes: indices {low} (valores {[sigma[i] for i in low]})",
                     "Sube los componentes de sigma a >=2 o baja lambda a <=2")

    if path_filter:
        diags = [d for d in diags if d.path.startswith(path_filter)]
    return diags


def _check_spec_procedure_coherence(path_filter=None):
    """Repo-level guard for spec titles, section numbering and live CLI examples."""
    from .config import KORA_ROOT

    diags = []
    spec_roots = [
        KORA_ROOT / "governance",
        KORA_ROOT / "ontology",
        KORA_ROOT / "serialization",
        KORA_ROOT / "runtime",
    ]

    forbidden = {
        "python3 toolchain/kora promover": "No existe CLI productiva `promover`; documenta procedimiento manual o implementa comando.",
        "--artefacto": "El CLI vivo de transmute usa `--agent`.",
        "Contrato vigente v4.4": "Contrato stale en gobernanza; debe coincidir con version vigente.",
        "Contrato vigente v3.7.0": "Contrato stale en runtime-spec-md; debe coincidir con version vigente.",
    }

    for root in spec_roots:
        if not root.exists():
            continue
        for path in sorted(root.rglob("*.md")):
            if path_filter and not str(path.relative_to(KORA_ROOT)).startswith(path_filter):
                continue
            text = path.read_text(encoding="utf-8")
            rel = str(path.relative_to(KORA_ROOT))

            if text.startswith("---"):
                parts = text.split("---", 2)
                if len(parts) == 3:
                    try:
                        import yaml
                        frontmatter = yaml.safe_load(parts[1]) or {}
                    except Exception:
                        frontmatter = {}
                    version = str(frontmatter.get("version", "")).strip()
                    h1 = next((line for line in parts[2].splitlines() if line.startswith("# ")), "")
                    match = re.search(r"\bv(\d+\.\d+(?:\.\d+)?)\b", h1)
                    if version and match and version != match.group(1):
                        diags.append(Diagnostic(
                            check_id="spec-procedure-coherence",
                            severity="medium",
                            scope="repo",
                            path=rel,
                            message=f"Version frontmatter ({version}) no coincide con H1 ({match.group(1)})",
                            fix_hint="Alinea el H1 con frontmatter.version o bumpea ambos explicitamente.",
                        ))

            seen_sections = {}
            for section in re.findall(r"(?m)^##\s+(\d+)\.\s+", text):
                if section in seen_sections:
                    diags.append(Diagnostic(
                        check_id="spec-procedure-coherence",
                        severity="medium",
                        scope="repo",
                        path=rel,
                        message=f"Seccion numerada duplicada: ## {section}.",
                        fix_hint="Renumerar secciones para restaurar orden editorial.",
                    ))
                else:
                    seen_sections[section] = True

            for needle, hint in forbidden.items():
                if needle in text:
                    diags.append(Diagnostic(
                        check_id="spec-procedure-coherence",
                        severity="medium",
                        scope="repo",
                        path=rel,
                        message=f"Procedimiento o contrato obsoleto: {needle}",
                        fix_hint=hint,
                    ))

    schema = KORA_ROOT / "serialization" / "schemas" / "kora-transmutation-schema.json"
    if not schema.is_file():
        diags.append(Diagnostic(
            check_id="spec-procedure-coherence",
            severity="medium",
            scope="repo",
            path=str(schema.relative_to(KORA_ROOT)),
            message="transmutation-spec declara schema de _transmutation.yml pero el archivo no existe",
            fix_hint="Agregar serialization/schemas/kora-transmutation-schema.json",
        ))

    return diags


def _iter_construction_artifacts(path_filter=None):
    """Yield current AGENT.md/SKILL.md artifacts in the construction gate scope."""
    from .artifacts import load_yaml_safe
    from .config import AGENTS_ROOT, KORA_ROOT, SKILLS_ROOT

    candidates = []

    def add_productive_agents():
        if not AGENTS_ROOT.exists():
            return
        for ns_dir in sorted(AGENTS_ROOT.iterdir()):
            if not ns_dir.is_dir() or ns_dir.name.startswith((".", "_")):
                continue
            for ws_dir in sorted(ns_dir.iterdir()):
                if not ws_dir.is_dir() or ws_dir.name.startswith((".", "_")):
                    continue
                agent_md = ws_dir / "AGENT.md"
                if agent_md.exists():
                    candidates.append(agent_md)

    def add_productive_skills():
        if not SKILLS_ROOT.exists():
            return
        for entry in sorted(SKILLS_ROOT.iterdir()):
            if not entry.is_dir() or entry.name.startswith((".", "_")):
                continue
            direct = entry / "SKILL.md"
            if direct.exists():
                candidates.append(direct)
                continue
            for sub in sorted(entry.iterdir()):
                if not sub.is_dir() or sub.name.startswith((".", "_")):
                    continue
                skill_md = sub / "SKILL.md"
                if skill_md.exists():
                    candidates.append(skill_md)

    add_productive_agents()
    add_productive_skills()

    # When a path filter targets staging or a concrete subtree, include it so
    # the next draft agent/skill can be checked before promotion.
    if path_filter:
        root = (KORA_ROOT / path_filter).resolve()
        if root.exists():
            if root.is_file() and root.name in {"AGENT.md", "SKILL.md"}:
                candidates.append(root)
            elif root.is_dir():
                candidates.extend(root.rglob("AGENT.md"))
                candidates.extend(root.rglob("SKILL.md"))

    seen = set()
    for path in candidates:
        try:
            rel = str(path.relative_to(KORA_ROOT))
        except ValueError:
            continue
        if path in seen:
            continue
        seen.add(path)
        if path_filter and not rel.startswith(path_filter):
            continue
        # _BUILD/ contiene derivados regenerables por target (gitignored, transmutation-spec).
        # No es fuente primaria — auditarlo como tal genera falsos positivos masivos.
        if "_BUILD" in path.parts:
            continue
        frontmatter, err = load_yaml_safe(path)
        if err or not isinstance(frontmatter, dict):
            continue
        if frontmatter.get("status") in {"deprecado", "retirado"}:
            continue
        yield path, rel, frontmatter


def _construction_scope(path: str) -> str:
    return "workspace" if path.endswith("/AGENT.md") else "artifact"


def _kora_ext(frontmatter: dict) -> dict:
    return (frontmatter.get("extensions") or {}).get("kora") or {}


def _forma_material(frontmatter: dict) -> str | None:
    return ((_kora_ext(frontmatter).get("atlas") or {}).get("forma_material"))


def _vector(frontmatter: dict) -> dict:
    return _kora_ext(frontmatter).get("vector_ontologico") or {}


def _emit_construction(diags, check_id, rel, message, fix_hint="", severity="medium"):
    diags.append(Diagnostic(
        check_id=check_id,
        severity=severity,
        scope=_construction_scope(rel),
        path=rel,
        message=message,
        fix_hint=fix_hint,
    ))


def _check_construction_source_primary(path_filter=None):
    """construction-source-primary: primary source file matches material form."""
    diags = []
    for path, rel, fm in _iter_construction_artifacts(path_filter):
        forma = _forma_material(fm)
        if "_BUILD" in path.parts:
            _emit_construction(
                diags,
                "construction-source-primary",
                rel,
                "Fuente primaria no puede vivir bajo _BUILD/; _BUILD es derivado.",
                "Mueve la fuente a artifacts/agents/{ns}/{id}/AGENT.md o artifacts/skills/{ns}/{id}/SKILL.md.",
                severity="high",
            )
        if path.name == "SKILL.md" and forma != "habilidad":
            _emit_construction(
                diags,
                "construction-source-primary",
                rel,
                f"SKILL.md debe declarar forma_material=habilidad; encontrado {forma!r}.",
                "Ajusta atlas.forma_material o materializa como AGENT.md.",
                severity="high",
            )
        if path.name == "AGENT.md" and forma == "habilidad":
            _emit_construction(
                diags,
                "construction-source-primary",
                rel,
                "AGENT.md no debe declarar forma_material=habilidad.",
                "Materializa habilidades como artifacts/skills/{ns}/{id}/SKILL.md.",
                severity="high",
            )
        urn = ((fm.get("_manifest") or {}).get("urn"))
        if not isinstance(urn, str) or ":artefacto:" not in urn:
            _emit_construction(
                diags,
                "construction-source-primary",
                rel,
                f"_manifest.urn debe usar regimen artefacto; encontrado {urn!r}.",
                "Usa urn:{ns}:artefacto:{id}.",
                severity="high",
            )
    return diags


def _check_construction_vector_fit(path_filter=None):
    """construction-vector-fit: canonical vector exists and fits material-form domain."""
    diags = []
    for _path, rel, fm in _iter_construction_artifacts(path_filter):
        kora = _kora_ext(fm)
        forma = _forma_material(fm)
        vec = _vector(fm)
        for retired_key in ("harness_vector", "presentation"):
            if retired_key in kora:
                _emit_construction(
                    diags,
                    "construction-vector-fit",
                    rel,
                    f"Overlay KORA contiene clave retirada {retired_key!r}.",
                    "Corre `python3 toolchain/kora migrate --profile a-autoria` y conserva solo vector_ontologico/presentacion.",
                    severity="high",
                )
        if not isinstance(vec, dict):
            _emit_construction(
                diags,
                "construction-vector-fit",
                rel,
                "Falta extensions.kora.vector_ontologico.",
                "Declara los 6 ejes PMI x LFS antes de construir o transmutar.",
                severity="high",
            )
            continue
        pi, mu, xi, lam = vec.get("pi"), vec.get("mu"), vec.get("xi"), vec.get("lambda")
        if forma == "habilidad" and not (
            isinstance(mu, int) and mu <= 1 and isinstance(lam, int) and lam == 0
        ):
            _emit_construction(
                diags,
                "construction-vector-fit",
                rel,
                f"habilidad requiere mu<=1 y lambda=0; encontrado mu={mu!r}, lambda={lam!r}.",
                "Baja la forma a habilidad solo si no necesita memoria/escala, o materializa como agente.",
                severity="high",
            )
        if forma == "subagente" and isinstance(lam, int) and lam > 0:
            _emit_construction(
                diags,
                "construction-vector-fit",
                rel,
                f"subagente no debe operar a escala sociotecnica lambda={lam}.",
                "Sube a agente-propiamente-tal si requiere escala organizacional.",
                severity="high",
            )
        if forma == "agente-plataforma" and not (isinstance(mu, int) and mu == 3):
            _emit_construction(
                diags,
                "construction-vector-fit",
                rel,
                f"agente-plataforma requiere materia ambiental mu=3; encontrado {mu!r}.",
                "Usa agente-propiamente-tal si no hay servicio/fleet always-on.",
                severity="high",
            )
        if forma == "habilidad" and any(isinstance(v, int) and v > bound for v, bound in ((pi, 2), (xi, 2))):
            _emit_construction(
                diags,
                "construction-vector-fit",
                rel,
                f"habilidad excede dominio portable pi<=2, xi<=2; encontrado pi={pi!r}, xi={xi!r}.",
                "Reduce el vector o promueve forma material.",
                severity="high",
            )
    return diags


def _check_construction_knowledge_explicit(path_filter=None):
    """construction-knowledge-explicit: knowledge contract uses resolvable URNs."""
    from .catalog import build_catalog_lookup, load_catalog, urn_is_known

    doc = load_catalog()
    known_urns, _urn_to_entry = build_catalog_lookup(doc) if doc else (set(), {})
    diags = []
    for _path, rel, fm in _iter_construction_artifacts(path_filter):
        allowed = _kora_ext(fm).get("conocimiento_permitido")
        if allowed is None:
            continue
        if not isinstance(allowed, list):
            _emit_construction(
                diags,
                "construction-knowledge-explicit",
                rel,
                "conocimiento_permitido debe ser lista de URNs.",
                "Usa una lista YAML de URNs resolubles o [] si no usa KB.",
                severity="high",
            )
            continue
        for item in allowed:
            if not isinstance(item, str) or not item.startswith("urn:"):
                _emit_construction(
                    diags,
                    "construction-knowledge-explicit",
                    rel,
                    f"conocimiento_permitido contiene entrada no-URN: {item!r}.",
                    "Reemplaza paths por URNs resolubles del catalogo.",
                    severity="high",
                )
                continue
            if known_urns and not urn_is_known(item, known_urns):
                _emit_construction(
                    diags,
                    "construction-knowledge-explicit",
                    rel,
                    f"URN de conocimiento no resuelve en catalogo: {item}",
                    "Corre `python3 toolchain/kora index` o corrige el URN.",
                    severity="high",
                )
    return diags


def _transition_targets(transitions):
    if not isinstance(transitions, list):
        return []
    targets = []
    for transition in transitions:
        if isinstance(transition, dict):
            target = transition.get("destino") or transition.get("target")
            if isinstance(target, str):
                targets.append(target)
    return targets


def _check_construction_fsm_valid(path_filter=None):
    """construction-fsm-valid: finite-state plans have coherent references."""
    diags = []
    for _path, rel, fm in _iter_construction_artifacts(path_filter):
        kora = _kora_ext(fm)
        plan = ((fm.get("artefacto") or {}).get("plan") or {})
        fsm = plan.get("fsm") if isinstance(plan, dict) else None
        if kora.get("verificacion_coalgebraica") is True and not isinstance(fsm, dict):
            _emit_construction(
                diags,
                "construction-fsm-valid",
                rel,
                "verificacion_coalgebraica=true requiere artefacto.plan.fsm.",
                "Declara plan.fsm o desactiva la verificacion coalgebraica.",
                severity="high",
            )
        machine = fsm if isinstance(fsm, dict) else plan
        if not isinstance(machine, dict):
            continue
        states = machine.get("estados") or machine.get("states")
        if not isinstance(states, list) or not states:
            continue
        state_ids = set()
        transitions_by_state = {}
        for state in states:
            if isinstance(state, str):
                state_ids.add(state)
            elif isinstance(state, dict):
                sid = state.get("id")
                if isinstance(sid, str):
                    state_ids.add(sid)
                    raw_transitions = state.get("transiciones") or state.get("transitions")
                    if isinstance(raw_transitions, list):
                        transitions_by_state[sid] = _transition_targets(raw_transitions)
        if not transitions_by_state:
            continue
        initial = machine.get("estado_inicial") or machine.get("initial_state")
        terminal = machine.get("estado_terminal") or machine.get("terminal_state")
        terminals = set(machine.get("terminales") or machine.get("terminals") or [])
        if isinstance(terminal, str):
            terminals.add(terminal)
        if isinstance(initial, str) and initial not in state_ids:
            _emit_construction(
                diags,
                "construction-fsm-valid",
                rel,
                f"estado_inicial {initial!r} no existe en estados.",
                "Agrega el estado inicial o corrige la referencia.",
                severity="high",
            )
        missing_terminals = sorted(t for t in terminals if t not in state_ids)
        if missing_terminals:
            _emit_construction(
                diags,
                "construction-fsm-valid",
                rel,
                f"terminales inexistentes: {missing_terminals}.",
                "Agrega estados terminales o corrige estado_terminal/terminales.",
                severity="high",
            )
        for sid, targets in transitions_by_state.items():
            missing = sorted(t for t in targets if t not in state_ids)
            if missing:
                _emit_construction(
                    diags,
                    "construction-fsm-valid",
                    rel,
                    f"estado {sid!r} transiciona a estados inexistentes: {missing}.",
                    "Corrige destino/target de transiciones.",
                    severity="high",
                )
        reverse = {sid: set() for sid in state_ids}
        for sid, targets in transitions_by_state.items():
            for target in targets:
                if target in reverse:
                    reverse[target].add(sid)
        reachable_to_terminal = set(terminals & state_ids)
        stack = list(reachable_to_terminal)
        while stack:
            current = stack.pop()
            for previous in reverse.get(current, set()):
                if previous not in reachable_to_terminal:
                    reachable_to_terminal.add(previous)
                    stack.append(previous)
        stuck = sorted(sid for sid in transitions_by_state if sid not in reachable_to_terminal)
        if terminals and stuck:
            _emit_construction(
                diags,
                "construction-fsm-valid",
                rel,
                f"estados sin camino a terminal: {stuck}.",
                "Agrega salida finita hacia estado_terminal o declara deuda antes de transmutar.",
                severity="high",
            )
    return diags


def _check_construction_interface_typed(path_filter=None):
    """construction-interface-typed: interface has observable tools/permissions/protocols."""
    diags = []
    observable_keys = {"tools", "herramientas", "permissions", "permisos", "protocolos", "entradas", "salidas"}
    for _path, rel, fm in _iter_construction_artifacts(path_filter):
        interfaz = ((fm.get("artefacto") or {}).get("interfaz") or {})
        if not isinstance(interfaz, dict):
            _emit_construction(
                diags,
                "construction-interface-typed",
                rel,
                "artefacto.interfaz debe ser objeto con capacidades observables.",
                "Declara herramientas/permisos/protocolos de interfaz.",
                severity="high",
            )
            continue
        if not any(key in interfaz for key in observable_keys):
            _emit_construction(
                diags,
                "construction-interface-typed",
                rel,
                "interfaz no declara tools/herramientas, permissions/permisos ni protocolos.",
                "Explicita capacidades observables antes de construir/transmutar.",
                severity="medium",
            )
    return diags


def _check_construction_risk_declared(path_filter=None):
    """construction-risk-declared: non-trivial risk has invariants, QA or risk register."""
    diags = []
    for _path, rel, fm in _iter_construction_artifacts(path_filter):
        forma = _forma_material(fm)
        vec = _vector(fm)
        sigma = vec.get("sigma") if isinstance(vec, dict) else None
        high_sigma = isinstance(sigma, list) and any(isinstance(v, int) and v >= 3 for v in sigma)
        needs_risk_surface = forma in {"agente-propiamente-tal", "agente-plataforma"} or high_sigma
        if not needs_risk_surface:
            continue
        artefacto = fm.get("artefacto") or {}
        contexto = artefacto.get("contexto") or {}
        has_surface = any(
            bool(value)
            for value in (
                artefacto.get("invariantes"),
                contexto.get("qa_budget"),
                contexto.get("risk_register"),
            )
        )
        if not has_surface:
            _emit_construction(
                diags,
                "construction-risk-declared",
                rel,
                "riesgo no trivial sin invariantes, qa_budget ni risk_register.",
                "Declara reglas duras y, si aplica, qa_budget/risk_register.",
                severity="medium",
            )
    return diags


def _check_construction_runtime_separation(path_filter=None):
    """construction-runtime-separation: runtime outputs never become source."""
    diags = []
    for path, rel, fm in _iter_construction_artifacts(path_filter):
        if "_BUILD" in path.parts:
            _emit_construction(
                diags,
                "construction-runtime-separation",
                rel,
                "Artefacto fuente ubicado bajo _BUILD/.",
                "_BUILD/ solo contiene derivados regenerables; mueve la fuente al workspace productivo o staging.",
                severity="high",
            )
        source = (((fm.get("_manifest") or {}).get("provenance") or {}).get("source") or "")
        if isinstance(source, str) and "_BUILD/" in source:
            _emit_construction(
                diags,
                "construction-runtime-separation",
                rel,
                "_manifest.provenance.source apunta a _BUILD/ derivado.",
                "Apunta a requerimiento, draft, knowledge o fuente primaria, no a output runtime.",
                severity="medium",
            )
    return diags


def _check_construction_categorical_minimality(path_filter=None):
    """construction-categorical-minimality: light guard against obvious over-formalization."""
    diags = []
    for _path, rel, fm in _iter_construction_artifacts(path_filter):
        forma = _forma_material(fm)
        vec = _vector(fm)
        mu, xi, lam = vec.get("mu"), vec.get("xi"), vec.get("lambda")
        if forma == "habilidad" and any(isinstance(v, int) and v > limit for v, limit in ((mu, 1), (xi, 2), (lam, 0))):
            _emit_construction(
                diags,
                "construction-categorical-minimality",
                rel,
                f"habilidad parece sobre-formalizada para su forma: mu={mu!r}, xi={xi!r}, lambda={lam!r}.",
                "Usa la forma mas baja suficiente o promueve materialmente con justificacion.",
                severity="medium",
            )
    return diags


def _check_construction_authoring_shape(path_filter=None):
    """construction-authoring-shape: artifacts use the current autoria envelope."""
    diags = []
    for _path, rel, fm in _iter_construction_artifacts(path_filter):
        artefacto = fm.get("artefacto")
        if not isinstance(artefacto, dict):
            _emit_construction(
                diags,
                "construction-authoring-shape",
                rel,
                "Falta top-level `artefacto` conforme a autoria-spec.",
                "Materializa el insumo en el envelope unificado de autoria-spec.",
                severity="high",
            )
        if "agent" in fm:
            _emit_construction(
                diags,
                "construction-authoring-shape",
                rel,
                "Top-level `agent` no es fuente de autoria vigente.",
                "Traduce la fuente a `artefacto` antes de promocionar o transmutar.",
                severity="high",
            )
    return diags


def _check_fidelidad_agentskills(path_filter=None):
    """Verifica que cada habilidad productiva se proyecta a agentskills.io sin perdida.

    Autoria-spec §5.5: las habilidades DEBEN ser transmutables byte-identical
    a paquetes agentskills.io-compatibles. Este check ejecuta la proyeccion
    en dry-run y verifica que no hay diagnostico de dominio ni perdida en
    ejes no-sigma (sigma acepta perdida cuando excede sigma_max).
    """
    from .artifacts import load_yaml_safe
    from .config import KORA_ROOT, SKILLS_ROOT
    from .transmute import _transmute_skill_to_agentskills

    diags = []
    if not SKILLS_ROOT.exists():
        return diags

    def iter_productive_skills():
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

    for skill_md in iter_productive_skills():
        fm, err = load_yaml_safe(skill_md)
        if err or not isinstance(fm, dict):
            continue
        forma = (fm.get("extensions") or {}).get("kora", {}).get("atlas", {}).get("forma_material")
        if forma != "habilidad":
            continue

        rel = str(skill_md.relative_to(KORA_ROOT))
        try:
            _target_dir, summary = _transmute_skill_to_agentskills(skill_md, dry_run=True)
        except ValueError as exc:
            diags.append(Diagnostic(
                check_id="fidelidad-agentskills",
                severity="high",
                scope="artifact",
                path=rel,
                message=f"Proyeccion a agentskills.io falla: {exc}",
                fix_hint="Ajusta vector_ontologico al dominio de habilidad (autoria-spec §5.1)",
            ))
            continue

        # Perdida solo aceptable en sigma; en ejes estructurales es bug
        losses = summary.get("loss_by_axis", {})
        structural_losses = {ax: loss for ax, loss in losses.items() if loss and ax != "sigma"}
        if structural_losses:
            diags.append(Diagnostic(
                check_id="fidelidad-agentskills",
                severity="high",
                scope="artifact",
                path=rel,
                message=f"Proyeccion con perdida estructural: {structural_losses}",
                fix_hint="Vector fuera de dominio de habilidad; ajustar o marcar como no-habilidad",
            ))

        # Frontmatter debe tener nombre o name
        has_name = bool(fm.get("nombre") or fm.get("name"))
        has_desc = bool(fm.get("descripcion") or fm.get("description"))
        if not has_name:
            diags.append(Diagnostic(
                check_id="fidelidad-agentskills",
                severity="medium",
                scope="artifact",
                path=rel,
                message="Habilidad sin campo 'nombre' (es) ni 'name' (en) — proyeccion emitira SKILL.md sin name",
                fix_hint="Agrega 'nombre: <slug>' al frontmatter",
            ))
        if not has_desc:
            diags.append(Diagnostic(
                check_id="fidelidad-agentskills",
                severity="medium",
                scope="artifact",
                path=rel,
                message="Habilidad sin campo 'descripcion' (es) ni 'description' (en) — proyeccion emitira SKILL.md sin description",
                fix_hint="Agrega 'descripcion: <linea>' al frontmatter",
            ))

    if path_filter:
        diags = [d for d in diags if d.path.startswith(path_filter)]
    return diags


def _check_fidelidad_mastra(path_filter=None):
    """Verifica que agentes productivos caen dentro del dominio Mastra.

    H23 cierra un target adicional de runtime. A diferencia de agentskills, la
    proyeccion actual es blueprint-first y no byte-identical, por lo que este
    check valida dominio + perdida declarada sin exigir round-trip.
    """
    from .artifacts import load_yaml_safe
    from .config import AGENTS_ROOT, KORA_ROOT
    from .transmute import _get_vector_ontologico, _project_vector

    diags = []
    if not AGENTS_ROOT.exists():
        return diags

    for ns_dir in sorted(AGENTS_ROOT.iterdir()):
        if not ns_dir.is_dir() or ns_dir.name.startswith((".", "_")):
            continue
        for agent_dir in sorted(ns_dir.iterdir()):
            if not agent_dir.is_dir() or agent_dir.name.startswith((".", "_")):
                continue
            agent_md = agent_dir / "AGENT.md"
            if not agent_md.is_file():
                continue

            fm, err = load_yaml_safe(agent_md)
            if err or not isinstance(fm, dict):
                continue
            rel = str(agent_md.relative_to(KORA_ROOT))

            try:
                vector = _get_vector_ontologico(fm)
                _project_vector(vector, "mastra")
            except ValueError as exc:
                diags.append(Diagnostic(
                    check_id="fidelidad-mastra",
                    severity="high",
                    scope="workspace",
                    path=rel,
                    message=f"Proyeccion a Mastra falla: {exc}",
                    fix_hint="Ajusta vector_ontologico o quita mastra del dominio esperado",
                ))

    if path_filter:
        diags = [d for d in diags if d.path.startswith(path_filter)]
    return diags


def _check_coalgebra_conformance(path_filter=None):
    """Verifica termination del FSM declarado en artefacto.plan.fsm (autoria-spec v1.1 §3.5).

    Solo aplica cuando el artefacto declara plan.fsm. Opcional por defecto;
    obligatorio cuando extensions.kora.verificacion_coalgebraica es true.

    Invariantes verificadas:
      - FSM bien formado: estados, inicial, terminales, transiciones presentes.
      - inicial existe en estados declarados.
      - todos los terminales existen en estados.
      - todos los targets de transiciones estan en estados.
      - termination: desde inicial todo camino alcanza un terminal (no hay
        ciclos sin salida a terminal).
      - sub_coalgebra_segura (si presente): cerrada bajo transiciones.
    """
    import os
    from .artifacts import load_yaml_safe
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
                    am = ws_dir / "AGENT.md"
                    if am.exists():
                        yield am
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
        artefacto = frontmatter.get("artefacto")
        if not isinstance(artefacto, dict):
            continue
        plan = artefacto.get("plan") or {}
        fsm = plan.get("fsm") if isinstance(plan, dict) else None
        strict_required = (
            (frontmatter.get("extensions") or {}).get("kora", {}).get("verificacion_coalgebraica") is True
        )

        rel = str(artifact_path.relative_to(KORA_ROOT))
        scope_kind = "workspace" if artifact_path.name == "AGENT.md" else "artifact"

        if not isinstance(fsm, dict):
            if strict_required:
                diags.append(Diagnostic(
                    check_id="coalgebra-conformance",
                    severity="high",
                    scope=scope_kind,
                    path=rel,
                    message="verificacion_coalgebraica=true pero artefacto.plan.fsm ausente",
                    fix_hint="Declara plan.fsm con {inicial, terminales, transiciones} segun autoria-spec §3.5",
                ))
            continue

        inicial = fsm.get("inicial")
        terminales = fsm.get("terminales") or []
        transiciones = fsm.get("transiciones") or {}
        estados_list = plan.get("estados") or []
        estados_ids = set()
        for s in estados_list:
            if isinstance(s, dict) and "id" in s:
                estados_ids.add(s["id"])

        if not isinstance(inicial, str) or inicial not in estados_ids:
            diags.append(Diagnostic(
                check_id="coalgebra-conformance", severity="high", scope=scope_kind, path=rel,
                message=f"plan.fsm.inicial '{inicial}' no esta en plan.estados",
                fix_hint="Agrega el estado inicial a plan.estados con su id correspondiente",
            ))
            continue
        if not isinstance(terminales, list) or not terminales:
            diags.append(Diagnostic(
                check_id="coalgebra-conformance", severity="high", scope=scope_kind, path=rel,
                message="plan.fsm.terminales esta vacio — todo FSM debe tener al menos un terminal",
                fix_hint="Declara al menos un estado terminal en plan.fsm.terminales",
            ))
            continue
        missing_terminals = [t for t in terminales if t not in estados_ids]
        if missing_terminals:
            diags.append(Diagnostic(
                check_id="coalgebra-conformance", severity="high", scope=scope_kind, path=rel,
                message=f"plan.fsm.terminales contiene ids no declarados en plan.estados: {missing_terminals}",
                fix_hint="Registra los ids como entradas en plan.estados",
            ))
            continue
        # Verifica targets en estados
        bad_targets = []
        for src, targets in transiciones.items():
            if src not in estados_ids:
                bad_targets.append(f"source '{src}' no en plan.estados")
                continue
            if not isinstance(targets, list):
                continue
            for t in targets:
                if t not in estados_ids:
                    bad_targets.append(f"transicion '{src} -> {t}' apunta a estado no declarado")
        if bad_targets:
            diags.append(Diagnostic(
                check_id="coalgebra-conformance", severity="high", scope=scope_kind, path=rel,
                message=f"plan.fsm.transiciones invalidas: {'; '.join(bad_targets[:5])}",
                fix_hint="Corrige ids en transiciones o agrega estados faltantes",
            ))
            continue

        # Termination: BFS desde inicial, cada estado visitado debe poder
        # alcanzar un terminal. Detectamos estados "atrapados" en ciclos sin
        # salida.
        terminal_set = set(terminales)
        reachable = {inicial}
        frontier = [inicial]
        while frontier:
            s = frontier.pop()
            for t in transiciones.get(s, []) or []:
                if t not in reachable:
                    reachable.add(t)
                    frontier.append(t)
        # Para cada estado alcanzable, verificar que puede alcanzar un terminal
        def can_reach_terminal(start):
            seen = {start}
            stack = [start]
            while stack:
                s = stack.pop()
                if s in terminal_set:
                    return True
                for t in transiciones.get(s, []) or []:
                    if t not in seen:
                        seen.add(t)
                        stack.append(t)
            return False
        trapped = [s for s in reachable if not can_reach_terminal(s)]
        if trapped:
            diags.append(Diagnostic(
                check_id="coalgebra-conformance", severity="high", scope=scope_kind, path=rel,
                message=f"FSM no termina: estados sin camino a terminal: {trapped[:5]}",
                fix_hint="Agrega transicion hacia un estado terminal o declara el estado como terminal",
            ))
            continue

        # Sub-coalgebra safety: closed under transitions
        sub_safe = artefacto.get("invariantes", {}).get("sub_coalgebra_segura")
        if isinstance(sub_safe, list) and sub_safe:
            sub_set = set(sub_safe)
            missing = [s for s in sub_safe if s not in estados_ids]
            if missing:
                diags.append(Diagnostic(
                    check_id="coalgebra-conformance", severity="medium", scope=scope_kind, path=rel,
                    message=f"sub_coalgebra_segura lista estados no declarados: {missing}",
                ))
                continue
            escapes = []
            for s in sub_safe:
                for t in transiciones.get(s, []) or []:
                    if t not in sub_set:
                        escapes.append(f"{s} -> {t}")
            if escapes:
                diags.append(Diagnostic(
                    check_id="coalgebra-conformance", severity="high", scope=scope_kind, path=rel,
                    message=f"sub_coalgebra_segura no cerrada bajo transiciones: {escapes[:3]}",
                    fix_hint="Agrega estados destino a la sub-coalgebra o remueve la transicion",
                ))

    if path_filter:
        diags = [d for d in diags if d.path.startswith(path_filter)]
    return diags


# ---------------------------------------------------------------------------
# claude-code-budget-piso: enforce piso funtorial sobre extensions.claude_code
# ---------------------------------------------------------------------------

def _derive_claude_code_floor(vector: dict) -> tuple[str, int | None]:
    """Replica reducida de transmute._derive_claude_code_budget para checks.

    Devuelve (modo, piso). Piso None si no aplica (skill o vector invalido).
    Mantiene logica espejo de claude-code-runtime-extension §4.1.
    """
    mu = vector.get("mu") if isinstance(vector, dict) else None
    pi = vector.get("pi") if isinstance(vector, dict) else None
    xi = vector.get("xi") if isinstance(vector, dict) else None

    if mu == 0:
        return "skill", None
    if mu == 1:
        modo, floor = "subagent", 10
    elif mu == 2:
        modo, floor = "persona", 12
    elif isinstance(mu, int) and mu >= 3:
        return "out-of-domain", None
    else:
        modo, floor = "persona", 12

    bonus = 0
    if pi == 3:
        bonus += 3
    if isinstance(xi, int) and xi >= 3:
        bonus += 3
    return modo, floor + bonus


def _check_claude_code_budget_piso(path_filter=None):
    """Verifica que extensions.claude_code.max_turns declarado >= piso derivado.

    Politica fuente: claude-code-runtime-extension §4.1 (politica funtorial
    de budget runtime). Aplica solo a artefactos productivos AGENT.md cuyo
    vector_ontologico cae en el dominio claude-code (mu in {1, 2}).
    """
    from .artifacts import load_yaml_safe
    from .config import AGENTS_ROOT, KORA_ROOT

    diags = []
    if not AGENTS_ROOT.exists():
        return diags

    for ns_dir in sorted(AGENTS_ROOT.iterdir()):
        if not ns_dir.is_dir() or ns_dir.name.startswith((".", "_")):
            continue
        for ws_dir in sorted(ns_dir.iterdir()):
            if not ws_dir.is_dir() or ws_dir.name.startswith((".", "_")):
                continue
            am = ws_dir / "AGENT.md"
            if not am.exists():
                continue
            fm, err = load_yaml_safe(am)
            if err or not isinstance(fm, dict):
                continue

            kora_ext = (fm.get("extensions") or {}).get("kora") or {}
            vector = kora_ext.get("vector_ontologico") or kora_ext.get("harness_vector")
            if not isinstance(vector, dict):
                continue

            cc_top = (fm.get("extensions") or {}).get("claude_code")
            cc_ctx = (
                (fm.get("artefacto") or {}).get("contexto") or {}
            ).get("runtime_extensions") or {}
            cc_ctx = cc_ctx.get("claude_code") if isinstance(cc_ctx, dict) else None
            cc_top = cc_top if isinstance(cc_top, dict) else {}
            cc_ctx = cc_ctx if isinstance(cc_ctx, dict) else {}
            if not cc_top and not cc_ctx:
                continue

            declared = cc_top.get("max_turns") if "max_turns" in cc_top else cc_ctx.get("max_turns")
            if not isinstance(declared, int):
                continue

            modo, floor = _derive_claude_code_floor(vector)
            if floor is None:
                continue

            if declared < floor:
                rel = str(am.relative_to(KORA_ROOT))
                diags.append(Diagnostic(
                    check_id="claude-code-budget-piso",
                    severity="medium",
                    scope="workspace",
                    path=rel,
                    message=(
                        f"extensions.claude_code.max_turns={declared} < piso derivado "
                        f"{floor} para modo '{modo}' (vector pi={vector.get('pi')}, "
                        f"mu={vector.get('mu')}, xi={vector.get('xi')}, phi={vector.get('phi')})"
                    ),
                    fix_hint=(
                        f"Sube max_turns a >= {floor} o ajusta el vector ontologico si "
                        f"el modo derivado no corresponde"
                    ),
                ))

    if path_filter:
        diags = [d for d in diags if d.path.startswith(path_filter)]
    return diags


# ---------------------------------------------------------------------------
# Portabilidad: detecta paths literales no portables en tests y toolchain
# ---------------------------------------------------------------------------

_NONPORTABLE_PATH_PATTERNS = (
    # literales tipicos que rompen en otra plataforma o usuario
    "/tmp/", "/var/folders/", "/Users/", "/home/", "/private/var/",  # portable-exempt
)
_PORTABILITY_SCAN_DIRS = ("tests", "toolchain")
_PORTABILITY_EXEMPT_TAG = "portable-exempt"
# subarboles explicitamente excluidos del scan (scripts one-shot historicos
# cuya funcion ya se ejecuto y que viven en el repo como archivo arqueologico)
_PORTABILITY_EXCLUDED_SUBTREES = (
    "toolchain/legacy_migration",
)


def _check_portabilidad_tests(path_filter=None):
    """Scan tests/ y toolchain/ en busca de paths literales no portables.

    Motivacion categorica: una asercion o valor literal que encodea un path
    especifico de plataforma rompe el funtor `Run : Environment -> Result`
    (viola naturalidad respecto a isomorfismos de entorno). Todo path
    observable debe pasar por un normalizador canonico o vivir en un
    tempfile.

    Excepcion: lineas con comentario `# portable-exempt` al final son
    ignoradas (escape hatch para cadenas descriptivas o URLs que contienen
    substrings similares por coincidencia).
    """
    from .config import KORA_ROOT
    diags = []
    excluded_paths = tuple(KORA_ROOT / s for s in _PORTABILITY_EXCLUDED_SUBTREES)
    for rel_dir in _PORTABILITY_SCAN_DIRS:
        base = KORA_ROOT / rel_dir
        if not base.exists():
            continue
        for py_file in base.rglob("*.py"):
            if any(ex in py_file.parents or py_file == ex for ex in excluded_paths):
                continue
            try:
                text = py_file.read_text(encoding="utf-8")
            except (OSError, UnicodeDecodeError):
                continue
            in_docstring = False  # heuristica: contar """ y ''' como toggles
            for lineno, line in enumerate(text.splitlines(), start=1):
                # detectar aperturas/cierres de triple-quote en esta linea
                triple_dq = line.count('"""')
                triple_sq = line.count("'''")
                was_in_docstring = in_docstring
                # toggle por cada triple detectado (aproximacion suficiente
                # para codigo estandar; no maneja raw strings mixtos)
                if (triple_dq + triple_sq) % 2 == 1:
                    in_docstring = not in_docstring
                # si la linea entra, pasa por o sale de un docstring, saltarla
                if was_in_docstring or in_docstring:
                    continue
                if _PORTABILITY_EXEMPT_TAG in line:
                    continue
                stripped = line.lstrip()
                if stripped.startswith("#"):
                    continue
                for pat in _NONPORTABLE_PATH_PATTERNS:
                    if pat in line:
                        rel = str(py_file.relative_to(KORA_ROOT))
                        diags.append(Diagnostic(
                            check_id="portabilidad-tests",
                            severity="medium",
                            scope="repo",
                            path=f"{rel}:{lineno}",
                            message=f"Path literal no portable: '{pat}' en codigo fuente",
                            fix_hint="Usar tempfile.TemporaryDirectory() / pathlib o marcar con '# portable-exempt' si es string descriptivo",
                        ))
                        break
    if path_filter:
        diags = [d for d in diags if d.path.startswith(path_filter)]
    return diags


def _check_staging_vs_productive_divergence(path_filter=None):
    """Detectar items en staging cuyo nombre coincida con un productivo.

    Cobertura:
    - artifacts/agents/_FRAGUA/{INBOX,REVIEW}/X vs artifacts/agents/{ns}/X/AGENT.md
    - artifacts/skills/_TALLER/{INBOX,REVIEW}/X  vs artifacts/skills/{ns}/X/SKILL.md
    - INBOX y REVIEW del mismo nombre simultaneamente (duplicado interno).

    Saltamos directorios de control (`_archivo`, `_BUILD`, `_rebuild_required`,
    nombres con prefijo `_`) — son metadirectorios reconocidos por la
    pipeline `INBOX -> REVIEW -> productivo`.
    """
    from .config import AGENTS_ROOT, SKILLS_ROOT, KORA_ROOT
    diags = []

    def _productive_names(root: Path, manifest_name: str) -> set[str]:
        """Nombres de workspaces productivos (con manifest declarado)."""
        names = set()
        if not root.exists():
            return names
        for ns_dir in root.iterdir():
            if not ns_dir.is_dir() or ns_dir.name.startswith("_"):
                continue
            for ws_dir in ns_dir.iterdir():
                if not ws_dir.is_dir():
                    continue
                if (ws_dir / manifest_name).exists():
                    names.add(ws_dir.name)
        return names

    def _scan(layer_root: Path, staging_root: Path, manifest_name: str, layer_label: str):
        if not staging_root.exists():
            return
        productive = _productive_names(layer_root, manifest_name)
        per_stage_items: dict[str, set[str]] = {}
        for stage in ("INBOX", "REVIEW"):
            stage_dir = staging_root / stage
            if not stage_dir.exists():
                per_stage_items[stage] = set()
                continue
            items = {
                p.name for p in stage_dir.iterdir()
                if p.is_dir() and not p.name.startswith("_")
            }
            per_stage_items[stage] = items
            for item in sorted(items):
                if item in productive:
                    diags.append(Diagnostic(
                        check_id="staging-vs-productive-divergence",
                        severity="medium",
                        scope="workspace",
                        path=str((stage_dir / item).relative_to(KORA_ROOT)),
                        message=(
                            f"{layer_label} '{item}' en staging coincide con "
                            f"productivo en {layer_root.relative_to(KORA_ROOT)}/. "
                            "Resolver: integrar al productivo o eliminar staging."
                        ),
                        fix_hint=(
                            f"Diff manual + decision: "
                            f"git rm -r {(stage_dir / item).relative_to(KORA_ROOT)} "
                            "o promover via kora promote."
                        ),
                    ))
        intersection = per_stage_items.get("INBOX", set()) & per_stage_items.get("REVIEW", set())
        for item in sorted(intersection):
            diags.append(Diagnostic(
                check_id="staging-vs-productive-divergence",
                severity="medium",
                scope="workspace",
                path=str((staging_root / "REVIEW" / item).relative_to(KORA_ROOT)),
                message=(
                    f"{layer_label} '{item}' duplicado en INBOX y REVIEW. "
                    "Pipeline pre-categorial roto."
                ),
                fix_hint="Consolidar — uno solo entre INBOX y REVIEW.",
            ))

    _scan(AGENTS_ROOT, AGENTS_ROOT / "_FRAGUA", "AGENT.md", "Agente")
    _scan(SKILLS_ROOT, SKILLS_ROOT / "_TALLER", "SKILL.md", "Skill")

    if path_filter:
        diags = [d for d in diags if d.path.startswith(path_filter)]
    return diags


def _check_compromisos_eticos_no_todo(path_filter=None):
    """Bloquear publicacion con literales TODO en compromisos_eticos.

    Motivacion: `kora ingest` y `kora transmute` emiten artefactos en staging
    con campos `compromisos_eticos.{safety_norm,fairness,transparency,
    accountability,sustainability}` rellenados como literal "TODO" hasta que
    el operador los completa. Si esos literales sobreviven hasta productivo
    son drift normativo: el artefacto declara invariantes vacios y igual pasa
    los checks estructurales.
    """
    from .artifacts import load_yaml_safe
    from .config import AGENTS_ROOT, SKILLS_ROOT, KORA_ROOT

    diags = []
    productive_paths = []
    for root, manifest in ((AGENTS_ROOT, "AGENT.md"), (SKILLS_ROOT, "SKILL.md")):
        if not root.exists():
            continue
        for ns_dir in root.iterdir():
            if not ns_dir.is_dir() or ns_dir.name.startswith("_"):
                continue
            for ws_dir in ns_dir.iterdir():
                if not ws_dir.is_dir():
                    continue
                manifest_path = ws_dir / manifest
                if manifest_path.exists():
                    productive_paths.append(manifest_path)

    for manifest_path in productive_paths:
        frontmatter, _err = load_yaml_safe(manifest_path)
        if not isinstance(frontmatter, dict):
            continue
        artefacto = (frontmatter.get("artefacto") or {})
        invariantes = (artefacto.get("invariantes") or {})
        compromisos = invariantes.get("compromisos_eticos") or {}
        if not isinstance(compromisos, dict):
            continue
        for campo, valor in compromisos.items():
            if isinstance(valor, str) and valor.strip().upper().startswith("TODO"):
                diags.append(Diagnostic(
                    check_id="compromisos-eticos-no-todo",
                    severity="high",
                    scope="artifact",
                    path=str(manifest_path.relative_to(KORA_ROOT)),
                    message=(
                        f"compromisos_eticos.{campo} = 'TODO' literal en "
                        f"productivo. Stub de ingest/transmute sin completar."
                    ),
                    fix_hint=(
                        f"Editar {manifest_path.relative_to(KORA_ROOT)} y "
                        f"reemplazar 'TODO' por compromiso real, o degradar a staging."
                    ),
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
              spec_ref="autoria-spec §3, §6; compat profile", depends=("catalog-exists",), phase="verify"),
        _check_workspace_validity,
    )
    register_check(
        Check("bundle-coherence", "AGENT.md declarative deps resolve to productive artifacts",
              scope="workspace", severity="high", enforcement="lint",
              spec_ref="autoria-spec §9, §16", depends=("catalog-exists",), phase="verify"),
        _check_bundle_coherence,
    )
    register_check(
        Check("knowledge-zone", "artifacts/knowledge/ contains only valid KORA/MD artifacts",
              scope="artifact", severity="high", enforcement="lint",
              spec_ref="knowledge-spec §3.2, §4.2, §8.1", phase="verify"),
        _check_knowledge_zone,
    )
    register_check(
        Check("lint-md", "KORA/MD artifacts pass structural lint",
              scope="artifact", severity="low", enforcement="lint",
              spec_ref="md-spec §5, §9", depends=("knowledge-zone",), phase="lint"),
        _check_lint_md,
        _fix_lint_md,
    )
    register_check(
        Check("kb-graph-cycles", "Knowledge graph has no cycles in depends",
              scope="repo", severity="high", enforcement="lint",
              spec_ref="knowledge-spec §6.2, §10", depends=("knowledge-zone",), phase="graph"),
        _check_kb_graph_cycles,
    )
    register_check(
        Check("relations-laws", "supersedes/refines acyclic; supersedes antisymmetric",
              scope="artifact", severity="high", enforcement="lint",
              spec_ref="knowledge-spec §6.3", depends=("knowledge-zone",), phase="graph"),
        _check_relations_laws,
    )
    register_check(
        Check("traces-requirements-semantics", "traces_requirements targets are requirement-like nodes",
              scope="artifact", severity="high", enforcement="lint",
              spec_ref="knowledge-spec §6.2 r4, §11 inv7", depends=("knowledge-zone",), phase="graph"),
        _check_traces_requirements_semantics,
    )
    register_check(
        Check("spec-traces", "Traces to: lines point to existing formal layer docs",
              scope="artifact", severity="medium", enforcement="lint",
              spec_ref="gobernanza §5.1", phase="verify"),
        _check_spec_traces,
    )
    register_check(
        Check("formal-trace-discipline", "Traces to: URNs stay inside the official KORA Formal Layer",
              scope="artifact", severity="medium", enforcement="lint",
              spec_ref="md-spec §5.6.2.3; cat-fxsl-bridge §3", depends=("catalog-exists",), phase="verify"),
        _check_formal_trace_discipline,
    )
    register_check(
        Check("supersedes-consistency", "Supersedes targets must be deprecated",
              scope="artifact", severity="medium", enforcement="lint",
              spec_ref="knowledge-spec §6.2 r2, §11 inv4", depends=("knowledge-zone",), phase="graph"),
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
              spec_ref="agentfile-spec compat profile", depends=("catalog-exists",), phase="verify"),
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
              "Artefactos productivos (AGENT.md + SKILL.md) conforman a autoria-spec v1.2 (universal + fibra por forma material)",
              scope="artifact", severity="high", enforcement="schema",
              spec_ref="autoria-spec §3, §6", depends=("catalog-exists",), phase="verify"),
        _check_autoria_conformance,
        _fix_autoria_conformance,
    )
    register_check(
        Check("coalgebra-conformance",
              "Artefactos con plan.fsm declarado verifican termination y sub-coalgebra de safety cerrada",
              scope="artifact", severity="high", enforcement="eval",
              spec_ref="autoria-spec §3.5; harness-spec §4; ICAS Part IV", depends=("catalog-exists",), phase="verify"),
        _check_coalgebra_conformance,
    )
    register_check(
        Check("vector-laws",
              "Vector PMI × LFS cumple las 5 leyes inter-eje de harness-spec §4.1",
              scope="artifact", severity="high", enforcement="schema",
              spec_ref="harness-spec §4.1", depends=("catalog-exists",), phase="verify"),
        _check_vector_laws,
    )
    register_check(
        Check("construction-source-primary",
              "Construccion agentica materializa AGENT.md/SKILL.md como fuente primaria segun forma material",
              scope="artifact", severity="high", enforcement="lint",
              spec_ref="agent-skill-construction-spec §1, §3.8, §5.2", phase="verify"),
        _check_construction_source_primary,
    )
    register_check(
        Check("construction-vector-fit",
              "Vector ontologico canonico encaja con el dominio de realizabilidad de la forma material",
              scope="artifact", severity="high", enforcement="lint",
              spec_ref="agent-skill-construction-spec §3.2-§3.3; harness-spec §4.1", phase="verify"),
        _check_construction_vector_fit,
    )
    register_check(
        Check("construction-knowledge-explicit",
              "Contrato de conocimiento usa URNs resolubles y no paths duros",
              scope="artifact", severity="high", enforcement="lint",
              spec_ref="agent-skill-construction-spec §3.4", depends=("catalog-exists",), phase="verify"),
        _check_construction_knowledge_explicit,
    )
    register_check(
        Check("construction-fsm-valid",
              "FSM de construccion declara estados, terminales y transiciones coherentes",
              scope="artifact", severity="high", enforcement="lint",
              spec_ref="agent-skill-construction-spec §3.5", phase="verify"),
        _check_construction_fsm_valid,
    )
    register_check(
        Check("construction-interface-typed",
              "Interfaz declara capacidades observables, herramientas, permisos o protocolos",
              scope="artifact", severity="medium", enforcement="manual",
              spec_ref="agent-skill-construction-spec §3.6", phase="verify"),
        _check_construction_interface_typed,
    )
    register_check(
        Check("construction-risk-declared",
              "Riesgo no trivial queda cubierto por invariantes, qa_budget o risk_register",
              scope="artifact", severity="medium", enforcement="manual",
              spec_ref="agent-skill-construction-spec §3.7", phase="verify"),
        _check_construction_risk_declared,
    )
    register_check(
        Check("construction-runtime-separation",
              "Construccion mantiene IR fuente separado de outputs runtime derivados",
              scope="artifact", severity="high", enforcement="manual",
              spec_ref="agent-skill-construction-spec §1.1, §2.2, §3.8", phase="verify"),
        _check_construction_runtime_separation,
    )
    register_check(
        Check("construction-categorical-minimality",
              "Forma material usa la lectura categorial mas debil suficiente",
              scope="artifact", severity="medium", enforcement="manual",
              spec_ref="agent-skill-construction-spec §2.3, §3.3", phase="verify"),
        _check_construction_categorical_minimality,
    )
    register_check(
        Check("construction-authoring-shape",
              "Construccion usa el envelope vigente de autoria-spec",
              scope="artifact", severity="high", enforcement="manual",
              spec_ref="agent-skill-construction-spec §4, §6", phase="verify"),
        _check_construction_authoring_shape,
    )
    register_check(
        Check("spec-procedure-coherence",
              "Specs vigentes alinean version/H1, numeracion y comandos CLI vivos",
              scope="repo", severity="medium", enforcement="lint",
              spec_ref="gobernanza §10; transmutation-spec §6.3; autoria-spec §8.3", phase="verify"),
        _check_spec_procedure_coherence,
    )
    register_check(
        Check("fidelidad-agentskills",
              "Habilidades productivas se transmutan byte-identical a agentskills.io sin perdida estructural",
              scope="artifact", severity="high", enforcement="eval",
              spec_ref="autoria-spec §5.5", depends=("catalog-exists",), phase="verify"),
        _check_fidelidad_agentskills,
    )
    register_check(
        Check("fidelidad-mastra",
              "Agentes productivos proyectan a Mastra dentro del dominio y con perdida declarada",
              scope="workspace", severity="high", enforcement="eval",
              spec_ref="mastra-runtime-extension §3, §8", depends=("catalog-exists",), phase="verify"),
        _check_fidelidad_mastra,
    )
    register_check(
        Check("portabilidad-tests",
              "Codigo de tests/ y toolchain/ no contiene paths literales no portables",
              scope="repo", severity="medium", enforcement="lint",
              spec_ref="CLAUDE.md §Portabilidad", phase="lint"),
        _check_portabilidad_tests,
    )
    register_check(
        Check("claude-code-budget-piso",
              "extensions.claude_code.max_turns (si declarado) >= piso derivado por politica funtorial",
              scope="workspace", severity="medium", enforcement="lint",
              spec_ref="claude-code-runtime-extension §4.1", depends=("vector-laws",), phase="verify"),
        _check_claude_code_budget_piso,
    )
    register_check(
        Check("staging-vs-productive-divergence",
              "Items en _FRAGUA/_TALLER staging no comparten nombre con productivos",
              scope="workspace", severity="medium", enforcement="lint",
              spec_ref="autoria-spec §13; gobernanza §11", phase="verify"),
        _check_staging_vs_productive_divergence,
    )
    register_check(
        Check("compromisos-eticos-no-todo",
              "Productivos no contienen literal 'TODO' en compromisos_eticos",
              scope="artifact", severity="high", enforcement="lint",
              spec_ref="autoria-spec §3.7; transmutation-spec §6", phase="verify"),
        _check_compromisos_eticos_no_todo,
    )


# Auto-register on module import
_register_builtins()
