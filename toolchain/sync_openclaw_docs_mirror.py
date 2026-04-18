#!/usr/bin/env python3
from __future__ import annotations

import argparse
import os
import shutil
import subprocess
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

import yaml


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DEST = REPO_ROOT / "KNOWLEDGE/agengai/openclaw/documentacion-oficial"
SOURCE_REPO_ENV = "KORA_OPENCLAW_SOURCE_REPO"
SOURCE_DOCS_ENV = "KORA_OPENCLAW_SOURCE_DOCS"
DEST_ENV = "KORA_OPENCLAW_DEST"
CONTROL_FILES = {"_mirror.yml", "README.md"}
EXCLUDED_NAMES = {
    ".DS_Store",
}


@dataclass(frozen=True)
class SyncStats:
    copied_files: int
    deleted_files: int
    deleted_dirs: int


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Mirror OpenClaw official docs into KORA knowledge."
    )
    parser.add_argument(
        "--source-docs",
        default=None,
        help=f"Path to the upstream OpenClaw docs directory. Fallback: ${SOURCE_DOCS_ENV}.",
    )
    parser.add_argument(
        "--source-repo",
        default=None,
        help=f"Path to the upstream OpenClaw git clone. Fallback: ${SOURCE_REPO_ENV}.",
    )
    parser.add_argument(
        "--dest",
        default=str(DEFAULT_DEST),
        help=f"Destination mirror directory inside KORA. Fallback: ${DEST_ENV}.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Compute changes without copying files.",
    )
    return parser.parse_args()


def iter_source_files(root: Path):
    for path in sorted(root.rglob("*")):
        if path.name in EXCLUDED_NAMES:
            continue
        if path.is_file():
            yield path


def remove_stale_paths(dest_root: Path, expected_files: set[Path], dry_run: bool) -> tuple[int, int]:
    deleted_files = 0
    deleted_dirs = 0

    for path in sorted(dest_root.rglob("*"), reverse=True):
        rel = path.relative_to(dest_root)
        if rel.parts and rel.parts[0] in CONTROL_FILES:
            continue
        if path.is_file():
            if rel not in expected_files:
                deleted_files += 1
                if not dry_run:
                    path.unlink()
        elif path.is_dir():
            if rel.parts and rel.parts[0] in CONTROL_FILES:
                continue
            if not any(path.iterdir()):
                deleted_dirs += 1
                if not dry_run:
                    path.rmdir()

    return deleted_files, deleted_dirs


def mirror_tree(source_root: Path, dest_root: Path, dry_run: bool) -> SyncStats:
    expected_files: set[Path] = set()
    copied_files = 0

    for src in iter_source_files(source_root):
        rel = src.relative_to(source_root)
        if rel.parts and rel.parts[0] in CONTROL_FILES:
            raise RuntimeError(
                f"Upstream path collides with reserved control file: {rel}"
            )
        expected_files.add(rel)
        dest = dest_root / rel
        copied_files += 1
        if dry_run:
            continue
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dest)

    deleted_files, deleted_dirs = remove_stale_paths(dest_root, expected_files, dry_run)
    return SyncStats(
        copied_files=copied_files,
        deleted_files=deleted_files,
        deleted_dirs=deleted_dirs,
    )


def read_mirror_manifest(path: Path) -> dict:
    if not path.exists():
        return {}
    with open(path, "r", encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}


def git_commit(repo: Path) -> str | None:
    try:
        result = subprocess.run(
            ["git", "-C", str(repo), "rev-parse", "HEAD"],
            check=True,
            capture_output=True,
            text=True,
        )
        return result.stdout.strip() or None
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None


def update_manifest(
    manifest_path: Path,
    source_repo: Path,
    source_docs: Path,
    dest_root: Path,
    stats: SyncStats,
    dry_run: bool,
) -> None:
    doc = read_mirror_manifest(manifest_path)
    now = datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    commit = git_commit(source_repo)

    doc.setdefault("upstream", {})
    doc["upstream"]["repo"] = "https://github.com/openclaw/openclaw.git"
    doc["upstream"]["local_clone"] = str(source_repo)
    doc["upstream"]["root"] = str(source_docs.relative_to(source_repo))

    doc.setdefault("sync", {})
    doc["sync"]["mode"] = "mirror-1to1"
    doc["sync"]["excludes"] = sorted(EXCLUDED_NAMES)

    doc.setdefault("policy", {})
    doc["policy"]["knowledge_class"] = "external-mirror"
    doc["policy"]["per_file_frontmatter"] = False
    doc["policy"]["catalog_strategy"] = "collection-index"

    doc.setdefault("state", {})
    doc["state"]["last_sync_at"] = now
    doc["state"]["last_sync_commit"] = commit
    doc["state"]["dest_root"] = str(dest_root)
    doc["state"]["file_count"] = stats.copied_files
    doc["state"]["deleted_files"] = stats.deleted_files
    doc["state"]["deleted_dirs"] = stats.deleted_dirs
    doc["state"]["dry_run"] = dry_run

    with open(manifest_path, "w", encoding="utf-8") as handle:
        yaml.safe_dump(doc, handle, sort_keys=False, allow_unicode=True)


def main() -> int:
    args = parse_args()
    source_repo_raw = args.source_repo or None
    if source_repo_raw is None:
        source_repo_raw = os.environ.get(SOURCE_REPO_ENV)

    source_docs_raw = args.source_docs or None
    if source_docs_raw is None:
        source_docs_raw = os.environ.get(SOURCE_DOCS_ENV)
    if source_docs_raw is None and source_repo_raw is not None:
        source_docs_raw = str(Path(source_repo_raw).expanduser() / "docs")
    if source_docs_raw is None:
        raise SystemExit(
            f"Source docs directory not configured. Usa --source-docs, {SOURCE_DOCS_ENV} o --source-repo/{SOURCE_REPO_ENV}."
        )

    dest_raw = os.environ.get(DEST_ENV) or args.dest

    source_docs = Path(source_docs_raw).expanduser().resolve()
    source_repo = Path(source_repo_raw).expanduser().resolve() if source_repo_raw is not None else source_docs.parent
    dest_root = Path(dest_raw).expanduser().resolve()

    if not source_docs.exists():
        raise SystemExit(f"Source docs directory not found: {source_docs}")
    if not source_docs.is_dir():
        raise SystemExit(f"Source docs path is not a directory: {source_docs}")

    dest_root.mkdir(parents=True, exist_ok=True)
    stats = mirror_tree(source_docs, dest_root, args.dry_run)
    update_manifest(
        dest_root / "_mirror.yml",
        source_repo,
        source_docs,
        dest_root,
        stats,
        args.dry_run,
    )

    print(f"source: {source_docs}")
    print(f"dest:   {dest_root}")
    print(f"files mirrored: {stats.copied_files}")
    print(f"deleted files:  {stats.deleted_files}")
    print(f"deleted dirs:   {stats.deleted_dirs}")
    print(f"dry run:        {args.dry_run}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
