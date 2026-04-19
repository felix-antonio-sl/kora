"""Promote a draft artifact from staging to productivo.

Pipeline descentralizado (v8):
- Knowledge: artifacts/knowledge/_SCRIPTORIUM/REVIEW/{ns}/... -> artifacts/knowledge/{ns}/...
- Agent: artifacts/agents/_FRAGUA/REVIEW/{name}/ -> artifacts/agents/{ns}/{name}/
- Skill: artifacts/skills/_TALLER/REVIEW/{name}/ -> artifacts/skills/{ns}/{name}/

El promote functor:
1. Verifies the artifact has valid _manifest with status: draft
2. Runs lint checks on the artifact
3. Changes status: draft -> published
4. Moves the file to productivo (mirroring REVIEW/ subpath when aplica)
5. Triggers kora index to update the catalog

Nota v8: el staging previo de drafts/ en OPERATIONS/ fue eliminado.
SCRIPTORIUM/REVIEW reemplaza OPERATIONS/drafts/ para knowledge.
"""

import re
from pathlib import Path

from .artifacts import dump_yaml_frontmatter_and_body
from .config import KORA_ROOT, KNOWLEDGE_ROOT, SCRIPTORIUM_ROOT
from .validation import lint_kora_markdown_parts, load_markdown_parts, resolve_document_family

ATOMIC_ACCEPTANCE_REVIEW_TYPE = "atomic_acceptance"


def _atomic_bundle_root(stem):
    if stem.endswith("-index"):
        return stem[:-6]
    return re.sub(r"-\d+$", "", stem)


def default_atomic_review_path(draft_path):
    return draft_path.with_name(f"{_atomic_bundle_root(draft_path.stem)}-review{draft_path.suffix}")


def _atomic_bundle_paths(draft_path, frontmatter):
    if resolve_document_family(frontmatter) != "atomic":
        return [draft_path]

    atomic_ext = frontmatter.get("extensions", {}).get("kora", {}).get("atomic", {})
    if not isinstance(atomic_ext, dict) or not atomic_ext.get("segmented"):
        return [draft_path]

    root = _atomic_bundle_root(draft_path.stem)

    candidates = []
    index_path = draft_path.parent / f"{root}-index{draft_path.suffix}"
    if index_path.exists():
        candidates.append(index_path)
    segment_pattern = re.compile(rf"^{re.escape(root)}-(\d+){re.escape(draft_path.suffix)}$")
    segment_matches = []
    for candidate in draft_path.parent.glob(f"{root}-*{draft_path.suffix}"):
        match = segment_pattern.match(candidate.name)
        if match:
            segment_matches.append((int(match.group(1)), candidate))
    candidates.extend(
        candidate for _, candidate in sorted(segment_matches, key=lambda item: item[0])
    )
    if draft_path not in candidates:
        candidates.append(draft_path)

    unique = []
    for item in candidates:
        if item not in unique:
            unique.append(item)
    return unique


def _atomic_bundle_latest_mtime(bundle_paths):
    return max(path.stat().st_mtime for path in bundle_paths)


def _display_review_path(review_path):
    try:
        return review_path.relative_to(KORA_ROOT)
    except ValueError:
        return review_path


def validate_atomic_acceptance_review(draft_path, *, review_path=None, bundle_paths=None):
    review_path = review_path or default_atomic_review_path(draft_path)
    if not review_path.exists():
        return False, f"missing acceptance review: {review_path}", review_path

    review_frontmatter, _review_body = load_markdown_parts(review_path)
    if not isinstance(review_frontmatter, dict):
        return False, f"cannot parse acceptance review frontmatter: {review_path}", review_path
    if review_frontmatter.get("review_type") != ATOMIC_ACCEPTANCE_REVIEW_TYPE:
        return False, f"invalid review_type in {review_path}", review_path
    if review_frontmatter.get("bundle_root") != _atomic_bundle_root(draft_path.stem):
        return False, f"review bundle_root does not match target bundle: {review_path}", review_path
    if review_frontmatter.get("decision") != "accept":
        return False, f"review decision is not accept: {review_path}", review_path
    if not review_frontmatter.get("publish_ready"):
        return False, f"review is not publish_ready: {review_path}", review_path

    if bundle_paths is None:
        frontmatter, _body = load_markdown_parts(draft_path)
        if not isinstance(frontmatter, dict):
            return False, f"cannot parse frontmatter in {draft_path}", review_path
        bundle_paths = _atomic_bundle_paths(draft_path, frontmatter)
    if review_path.stat().st_mtime < _atomic_bundle_latest_mtime(bundle_paths):
        return False, f"review is stale for current bundle state: {review_path}", review_path

    return True, "", review_path


def cmd_promote_cohort(namespace: str):
    """Batch promote: todos los drafts en artifacts/knowledge/_SCRIPTORIUM/REVIEW/{ns}/.

    Itera archivos .md en review/{ns}/ y sus subdirectorios; para cada draft
    con status: draft, ejecuta cmd_promote. Acumula resultados; aborta al
    primer fallo para preservar composicion (no promueve parcialmente).
    """
    review_root = (SCRIPTORIUM_ROOT / "REVIEW").resolve()
    ns_dir = review_root / namespace

    if not review_root.exists():
        print(f"ERROR: {review_root} does not exist")
        raise SystemExit(1)

    # Perimetro del cohort: {ns}/ subtree + archivos top-level que tengan urn:{ns}:
    candidates = []
    if ns_dir.exists() and ns_dir.is_dir():
        for p in sorted(ns_dir.rglob("*.md")):
            candidates.append(p)
    # Archivos sueltos en REVIEW/ (no en subdir) cuyo URN declara el ns
    for p in sorted(review_root.iterdir()):
        if not p.is_file() or not p.suffix == ".md":
            continue
        try:
            fm, _body = load_markdown_parts(p)
        except Exception:
            continue
        if not isinstance(fm, dict):
            continue
        urn = (fm.get("_manifest") or {}).get("urn", "")
        if urn.startswith(f"urn:{namespace}:"):
            candidates.append(p)

    if not candidates:
        print(f"No draft candidates found for cohort '{namespace}' in {review_root}")
        return

    # Filtra por status: draft (skip bundle variants que ya fueron promovidas
    # por su index/primer archivo — cmd_promote maneja bundle de atomic)
    draft_files = []
    seen_bundle_roots = set()
    for p in candidates:
        try:
            fm, _body = load_markdown_parts(p)
        except Exception:
            continue
        if not isinstance(fm, dict):
            continue
        if fm.get("status") != "draft":
            continue
        # Dedup bundle de atomic: solo procesa el archivo index (o el primer
        # archivo del bundle); cmd_promote procesa todos los segmentos a la vez.
        if resolve_document_family(fm) == "atomic":
            atomic_ext = (fm.get("extensions") or {}).get("kora", {}).get("atomic") or {}
            if atomic_ext.get("segmented"):
                root = _atomic_bundle_root(p.stem)
                if root in seen_bundle_roots:
                    continue
                # Preferir el -index.md si existe
                index_candidate = p.parent / f"{root}-index.md"
                if index_candidate.exists() and index_candidate != p:
                    continue  # sera procesado cuando iteremos al index
                seen_bundle_roots.add(root)
        draft_files.append(p)

    print(f"=== Cohort promote: {namespace} ===")
    print(f"  Candidates: {len(draft_files)} draft(s)")
    promoted = 0
    for p in draft_files:
        try:
            cmd_promote(str(p))
            promoted += 1
        except SystemExit as exc:
            if exc.code and exc.code != 0:
                print(f"\nABORT: cohort promote falló en {p}")
                raise
    print(f"\n=== Cohort {namespace}: {promoted}/{len(draft_files)} promoted ===")


def cmd_promote(draft_path_str, *, review_path_str=None):
    draft_path = Path(draft_path_str).resolve()
    review_root = (SCRIPTORIUM_ROOT / "REVIEW").resolve()
    review_path = Path(review_path_str).expanduser().resolve() if review_path_str else None

    # Verify the file is in SCRIPTORIUM/REVIEW/
    if review_root not in draft_path.parents and draft_path.parent != review_root:
        print(f"ERROR: {draft_path_str} no esta en artifacts/knowledge/_SCRIPTORIUM/REVIEW/")
        print(f"  Ubicacion esperada: artifacts/knowledge/_SCRIPTORIUM/REVIEW/{{ns}}/...")
        raise SystemExit(1)

    if not draft_path.exists():
        print(f"ERROR: File not found: {draft_path_str}")
        raise SystemExit(1)

    # Load and validate frontmatter
    frontmatter, body = load_markdown_parts(draft_path)
    if not isinstance(frontmatter, dict):
        print(f"ERROR: Cannot parse frontmatter in {draft_path_str}")
        raise SystemExit(1)

    manifest = frontmatter.get("_manifest", {})
    urn = manifest.get("urn", "")
    if not urn:
        print(f"ERROR: No _manifest.urn found in {draft_path_str}")
        raise SystemExit(1)

    bundle_paths = _atomic_bundle_paths(draft_path, frontmatter)
    if resolve_document_family(frontmatter) == "atomic":
        valid_review, message, resolved_review_path = validate_atomic_acceptance_review(
            draft_path,
            review_path=review_path,
            bundle_paths=bundle_paths,
        )
        if not valid_review:
            print(f"ERROR: {message}")
            print(
                "Run review_atomic_acceptance.py with --decision accept after finishing bundle and semantic review."
            )
            raise SystemExit(1)
        print(f"ACCEPTANCE REVIEW: {_display_review_path(resolved_review_path)}")

    bundle_frontmatters = {}
    bundle_bodies = {}
    promoted_pairs = []

    for bundle_path in bundle_paths:
        bundle_frontmatter, bundle_body = load_markdown_parts(bundle_path)
        if not isinstance(bundle_frontmatter, dict):
            print(f"ERROR: Cannot parse frontmatter in {bundle_path}")
            raise SystemExit(1)

        bundle_status = bundle_frontmatter.get("status", "")
        if bundle_status != "draft":
            print(f"ERROR: Expected status: draft, found status: {bundle_status}")
            print(f"  Only draft artifacts can be promoted.")
            raise SystemExit(1)

        failures = lint_kora_markdown_parts(bundle_frontmatter, bundle_body, path=bundle_path)
        if failures:
            print(f"ERROR: Lint failures prevent promotion of {bundle_path.name}:")
            for failure in failures[:10]:
                print(f"  - {failure}")
            print(f"\nFix lint issues first, then retry promotion.")
            raise SystemExit(1)

        bundle_frontmatters[bundle_path] = bundle_frontmatter
        bundle_bodies[bundle_path] = bundle_body

    for bundle_path in bundle_paths:
        bundle_frontmatter = bundle_frontmatters[bundle_path]
        bundle_body = bundle_bodies[bundle_path]
        rel_to_drafts = bundle_path.relative_to(review_root)
        dest_path = KNOWLEDGE_ROOT / rel_to_drafts

        if dest_path.exists():
            print(f"WARNING: Target already exists: {dest_path.relative_to(KORA_ROOT)}")
            print(f"  This will overwrite the existing file.")

        bundle_frontmatter["status"] = "published"
        dest_path.parent.mkdir(parents=True, exist_ok=True)
        dump_yaml_frontmatter_and_body(dest_path, bundle_frontmatter, bundle_body, lint_guard=False)
        bundle_path.unlink()
        promoted_pairs.append(
            (
                bundle_frontmatter.get("_manifest", {}).get("urn", ""),
                bundle_path.relative_to(KORA_ROOT),
                dest_path.relative_to(KORA_ROOT),
            )
        )

    try:
        draft_path.parent.rmdir()
    except OSError:
        pass

    for promoted_urn, source_rel, dest_rel in promoted_pairs:
        print(f"PROMOTED: {promoted_urn}")
        print(f"  {source_rel} → {dest_rel}")
        print(f"  status: draft → published")
    print(f"\nRun 'python3 toolchain/kora index' to update the catalog.")


# ---------------------------------------------------------------------------
# Deprecate — dual de promote (gobernanza §5)
# ---------------------------------------------------------------------------

# Mapa lifecycle por tipo de artefacto (conceptual vs agentico) —
# regimen conceptual: borrador -> publicado -> deprecado
# regimen agentico:   borrador -> activo    -> deprecado -> retirado
_CONCEPTUAL_DEPRECATION = {"publicado": "deprecado"}
_AGENTIC_DEPRECATION = {"activo": "deprecado", "deprecado": "retirado"}


def _find_reverse_dependents(target_urn: str):
    """Encuentra artefactos productivos que citan/dependen del target_urn.

    Retorna lista de (urn_fuente, relation_type, file_path).
    """
    from .kb_graph import collect_knowledge_nodes

    dependents = []
    # Knowledge nodes
    for n in collect_knowledge_nodes():
        relations = n.get("relations") or {}
        if not isinstance(relations, dict):
            continue
        for rel_type in ("cites", "depends", "supersedes", "refines", "traces_requirements"):
            targets = relations.get(rel_type) or []
            if isinstance(targets, str):
                targets = [targets]
            if target_urn in targets:
                dependents.append((n["urn"], rel_type, n.get("file", "")))
    return dependents


def cmd_deprecate(path_str: str, *, supersedes: str = None, force: bool = False, retire: bool = False):
    """Marca un artefacto productivo como deprecado (o retirado).

    Pipeline:
    1. Carga frontmatter y valida status actual.
    2. Verifica dependencias reversas si not force: si algo activo depende,
       aborta con lista.
    3. Aplica transicion: activo/publicado -> deprecado, o deprecado -> retirado
       si --retire.
    4. Si supersedes pasado, lo registra en relations.supersedes del nuevo
       artefacto que suplanta (contrato: supersedes se declara en el NUEVO,
       no aqui — se valida que existe).
    5. Reescribe el archivo.
    """
    path = Path(path_str).resolve()
    if not path.exists():
        print(f"ERROR: File not found: {path_str}")
        raise SystemExit(1)

    frontmatter, body = load_markdown_parts(path)
    if not isinstance(frontmatter, dict):
        print(f"ERROR: Cannot parse frontmatter in {path_str}")
        raise SystemExit(1)

    manifest = frontmatter.get("_manifest") or {}
    urn = manifest.get("urn", "")
    if not urn:
        print(f"ERROR: No _manifest.urn in {path_str}")
        raise SystemExit(1)

    current_status = frontmatter.get("status", "")
    # Regimen por urn kind
    is_agentic = ":artefacto:" in urn
    transitions = _AGENTIC_DEPRECATION if is_agentic else _CONCEPTUAL_DEPRECATION

    if retire:
        if current_status != "deprecado":
            print(f"ERROR: --retire requiere status: deprecado actual, encontrado: '{current_status}'")
            raise SystemExit(1)
        new_status = "retirado"
    else:
        new_status = transitions.get(current_status)
        if new_status is None:
            valid_from = list(transitions.keys())
            print(f"ERROR: Cannot deprecate from status '{current_status}'. Valid source states: {valid_from}")
            raise SystemExit(1)

    # Dependencias reversas
    dependents = _find_reverse_dependents(urn)
    active_dependents = [(u, t, f) for u, t, f in dependents if u != urn]
    if active_dependents and not force:
        print(f"ERROR: {len(active_dependents)} artefacto(s) referencian a {urn}:")
        for u, t, f in active_dependents[:10]:
            print(f"  - {u} --{t}--> {urn}  ({f})")
        print(f"\nUsa --force para deprecar de todas formas, o actualiza los dependientes primero.")
        raise SystemExit(1)

    # Validar supersedes si presente
    if supersedes:
        from .catalog import build_catalog_lookup, load_catalog, urn_is_known
        doc = load_catalog()
        if doc and "Catalog" in doc:
            known_urns, _ = build_catalog_lookup(doc)
            if not urn_is_known(supersedes, known_urns):
                print(f"ERROR: supersedes URN '{supersedes}' no existe en catalogo")
                raise SystemExit(1)
        # Notifica: supersedes debe declararse en el NUEVO, no aqui
        print(f"NOTE: --supersedes {supersedes} asumes that artefact declares "
              f"'supersedes: [{urn}]' in its relations. Verificalo.")

    frontmatter["status"] = new_status
    dump_yaml_frontmatter_and_body(path, frontmatter, body, lint_guard=False)

    print(f"DEPRECATED: {urn}")
    print(f"  status: {current_status} -> {new_status}")
    print(f"  file: {path.relative_to(KORA_ROOT) if KORA_ROOT in path.parents else path}")
    if active_dependents:
        print(f"  WARNING: {len(active_dependents)} dependent(s) still reference this artifact")
    print(f"\nRun 'python3 toolchain/kora index' to update the catalog.")
