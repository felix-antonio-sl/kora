"""Promote a draft artifact from OPERATIONS/drafts/ to KNOWLEDGE/.

The promote functor:
1. Verifies the artifact has valid _manifest with status: draft
2. Runs lint checks on the artifact
3. Changes status: draft -> published
4. Moves the file to KNOWLEDGE/{ns}/... (mirroring the drafts/ path)
5. Triggers kora index to update the catalog
"""

import shutil
from pathlib import Path

from .artifacts import load_yaml_safe, dump_yaml_frontmatter_and_body
from .config import KORA_ROOT, KNOWLEDGE_ROOT, resolve_operational_dir
from .validation import lint_kora_markdown_parts, load_markdown_parts


def cmd_promote(draft_path_str):
    draft_path = Path(draft_path_str).resolve()
    drafts_root = resolve_operational_dir("drafts").resolve()

    # Verify the file is in drafts/
    if drafts_root not in draft_path.parents and draft_path.parent != drafts_root:
        print(f"ERROR: {draft_path_str} is not inside the drafts/ zone.")
        print(f"  Expected location: OPERATIONS/drafts/{{ns}}/...")
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

    # Compute destination path (mirror drafts/ structure to KNOWLEDGE/)
    rel_to_drafts = draft_path.relative_to(drafts_root)
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
