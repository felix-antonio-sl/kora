"""Canonical lifecycle helpers for KORA artifacts.

KORA v5 canoniza estados en espanol, pero la toolchain todavia convive con
material legacy en ingles. Este modulo centraliza la normalizacion para evitar
drift entre catalogo, lint, promote, reports y checks.
"""

from __future__ import annotations


_STATUS_ALIASES = {
    "active": "activo",
    "activo": "activo",
    "deprecated": "deprecado",
    "deprecado": "deprecado",
    "draft": "borrador",
    "borrador": "borrador",
    "published": "publicado",
    "publicado": "publicado",
    "retired": "retirado",
    "retirado": "retirado",
}


def canonicalize_status(status) -> str:
    """Return the canonical KORA status token for a raw value."""
    if not isinstance(status, str):
        return ""
    normalized = status.strip().lower()
    if not normalized:
        return ""
    return _STATUS_ALIASES.get(normalized, normalized)


def read_declared_status(doc, default: str = "") -> str:
    """Extract and canonicalize the declared lifecycle status from a document."""
    if isinstance(doc, dict):
        manifest = doc.get("_manifest")
        if isinstance(manifest, dict):
            status = canonicalize_status(manifest.get("status"))
            if status:
                return status
        for key in ("status", "Status"):
            status = canonicalize_status(doc.get(key))
            if status:
                return status
    return canonicalize_status(default)


def is_status(status, *canonical_values: str) -> bool:
    return canonicalize_status(status) in set(canonical_values)


def is_active_status(status) -> bool:
    return is_status(status, "activo")


def is_draft_status(status) -> bool:
    return is_status(status, "borrador")


def is_published_status(status) -> bool:
    return is_status(status, "publicado")


def is_deprecated_status(status) -> bool:
    return is_status(status, "deprecado")


def is_retired_status(status) -> bool:
    return is_status(status, "retirado")

