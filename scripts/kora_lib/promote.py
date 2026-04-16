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

import shutil
from pathlib import Path

from .artifacts import load_yaml_safe, dump_yaml_frontmatter_and_body
from .config import KORA_ROOT, KNOWLEDGE_ROOT, SCRIPTORIUM_ROOT
from .validation import lint_kora_markdown_parts, load_markdown_parts


def cmd_promote(draft_path_str):
    draft_path = Path(draft_path_str).resolve()
    review_root = (SCRIPTORIUM_ROOT / "REVIEW").resolve()

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

    status = frontmatter.get("status", "")
    if status != "draft":
        print(f"ERROR: Expected status: draft, found status: {status}")
        print(f"  Only draft artifacts can be promoted.")
        raise SystemExit(1)

    # Run lint checks
    failures = lint_kora_markdown_parts(frontmatter, body)
    if failures:
        print(f"ERROR: Lint failures prevent promotion:")
        for f in failures[:10]:
            print(f"  - {f}")
        print(f"\nFix lint issues first, then retry promotion.")
        raise SystemExit(1)

    # Compute destination path (mirror REVIEW structure to KNOWLEDGE/)
    rel_to_drafts = draft_path.relative_to(review_root)
    dest_path = KNOWLEDGE_ROOT / rel_to_drafts

    if dest_path.exists():
        print(f"WARNING: Target already exists: {dest_path.relative_to(KORA_ROOT)}")
        print(f"  This will overwrite the existing file.")

    # Change status to published
    frontmatter["status"] = "published"

    # Ensure destination directory exists
    dest_path.parent.mkdir(parents=True, exist_ok=True)

    # Write to destination
    dump_yaml_frontmatter_and_body(dest_path, frontmatter, body, lint_guard=False)

    # Remove the draft
    draft_path.unlink()

    # Clean up empty directories
    try:
        draft_path.parent.rmdir()
    except OSError:
        pass  # Directory not empty, that's fine

    rel_dest = dest_path.relative_to(KORA_ROOT)
    print(f"PROMOTED: {urn}")
    print(f"  {draft_path.relative_to(KORA_ROOT)} → {rel_dest}")
    print(f"  status: draft → published")
    print(f"\nRun 'python3 scripts/kora index' to update the catalog.")
