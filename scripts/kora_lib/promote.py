"""Promote a draft artifact from staging to productivo.

Pipeline descentralizado (v8):
- Knowledge: KNOWLEDGE/_SCRIPTORIUM/REVIEW/{ns}/... → KNOWLEDGE/{ns}/...
- Agent: AGENTS/_FRAGUA/REVIEW/{name}/ → AGENTS/{ns}/{name}/
- Skill: SKILLS/_TALLER/REVIEW/{name}/ → SKILLS/{name}/

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


def cmd_promote(draft_path_str, *, review_path_str=None):
    draft_path = Path(draft_path_str).resolve()
    review_root = (SCRIPTORIUM_ROOT / "REVIEW").resolve()
    review_path = Path(review_path_str).expanduser().resolve() if review_path_str else None

    # Verify the file is in SCRIPTORIUM/REVIEW/
    if review_root not in draft_path.parents and draft_path.parent != review_root:
        print(f"ERROR: {draft_path_str} no esta en KNOWLEDGE/_SCRIPTORIUM/REVIEW/")
        print(f"  Ubicacion esperada: KNOWLEDGE/_SCRIPTORIUM/REVIEW/{{ns}}/...")
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
    print(f"\nRun 'python3 scripts/kora index' to update the catalog.")
