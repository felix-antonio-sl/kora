"""Intake report para el pipeline descentralizado (v8).

Muestra el estado de los tres staging areas:
- AGENTS/_FRAGUA/{INBOX,REVIEW}
- SKILLS/_TALLER/{INBOX,REVIEW}
- KNOWLEDGE/_SCRIPTORIUM/{INBOX,REVIEW}

El pipeline centralizado en OPERATIONS/ fue eliminado en v8; cada tipo de
artefacto tiene su propio pipeline local. Los subdirectorios de INBOX/ son
pre-categoriales: no tienen namespace KORA asignado hasta promoverse.
"""

import os
from pathlib import Path

from .artifacts import load_yaml_safe
from .catalog import load_catalog
from .config import (
    KORA_ROOT,
    FRAGUA_ROOT,
    TALLER_ROOT,
    SCRIPTORIUM_ROOT,
    STAGING_STAGES,
    physical_to_logical_repo_path,
)


def provenance_source_from_artifact(artifact):
    provenance = artifact.get("_manifest", {}).get("provenance", {})
    if isinstance(provenance, dict):
        source = provenance.get("source", "")
    elif isinstance(provenance, str):
        source = provenance
    else:
        source = ""
    if isinstance(source, list):
        return " + ".join(str(s) for s in source)
    return source


def _count_items(path: Path) -> tuple[int, int]:
    """Returns (top-level items, total files) in path."""
    if not path.exists():
        return (0, 0)
    top = sum(1 for _ in path.iterdir() if not _.name.startswith("."))
    files = sum(1 for p in path.rglob("*") if p.is_file() and not p.name.startswith("."))
    return (top, files)


def _report_staging_area(label: str, root: Path):
    print(f"\n=== {label} ===")
    if not root.exists():
        print(f"  (no existe: {root.relative_to(KORA_ROOT)})")
        return
    for stage in STAGING_STAGES:
        stage_dir = root / stage
        top, files = _count_items(stage_dir)
        rel = stage_dir.relative_to(KORA_ROOT)
        print(f"  [{stage:6s}] {rel}: {top} items top-level, {files} archivos totales")


def cmd_intake():
    print("=== KORA Intake Status (pipeline descentralizado v8) ===")
    _report_staging_area("Agentes (AGENTS/_FRAGUA)", FRAGUA_ROOT)
    _report_staging_area("Skills (SKILLS/_TALLER)", TALLER_ROOT)
    _report_staging_area("Knowledge (KNOWLEDGE/_SCRIPTORIUM)", SCRIPTORIUM_ROOT)

    # Detalle SCRIPTORIUM/INBOX: reporta sources no trackeados por catalogo
    scriptorium_inbox = SCRIPTORIUM_ROOT / "INBOX"
    if scriptorium_inbox.exists():
        print("\n=== SCRIPTORIUM/INBOX — items pendientes ===")
        for item in sorted(scriptorium_inbox.iterdir()):
            if item.name.startswith("."):
                continue
            kind = "dir" if item.is_dir() else item.suffix or "file"
            size = sum(f.stat().st_size for f in item.rglob("*") if f.is_file()) if item.is_dir() else item.stat().st_size
            size_str = f"{size // 1024}KB" if size > 1024 else f"{size}B"
            print(f"  [{kind:5s}] {item.name} ({size_str})")

    # Cross-reference: fuentes en catalogo que ya no existen en SCRIPTORIUM
    doc = load_catalog()
    if doc and "Catalog" in doc:
        orphans = []
        for category, items in doc["Catalog"].items():
            for item in items:
                if not isinstance(item, dict):
                    continue
                file_path = KORA_ROOT / item.get("file", "")
                artifact, _ = load_yaml_safe(file_path)
                if artifact and isinstance(artifact, dict) and "_manifest" in artifact:
                    prov_source = provenance_source_from_artifact(artifact)
                    if prov_source and prov_source.startswith(("source/", "KNOWLEDGE/_SCRIPTORIUM/")):
                        src_path = KORA_ROOT / prov_source
                        if not src_path.exists():
                            orphans.append((item.get("file", ""), prov_source))
        if orphans:
            print(f"\n=== Catalog orphans ({len(orphans)}) — artefactos publicados cuya fuente no existe ===")
            for artifact_file, src in orphans[:20]:
                print(f"  [ORPHAN] {artifact_file} → {src}")
            if len(orphans) > 20:
                print(f"  ... y {len(orphans) - 20} mas")

    print("\nTriage:")
    print("  - INBOX items: revisar, limpiar, convertir a formato KORA/MD, mover a REVIEW.")
    print("  - REVIEW items: validar con `kora check`, asignar URN final, promover con `kora promote`.")
