import re
from pathlib import Path

from .artifacts import load_markdown_parts


FAT_PATTERNS = (
    re.compile(r"\bEn este documento veremos\b", re.IGNORECASE),
    re.compile(r"(?m)^\s*(?:[-*]\s+)?A continuaci[oó]n\b", re.IGNORECASE),
    re.compile(r"(?m)^\s*(?:[-*]\s+)?Por otro lado\b", re.IGNORECASE),
    re.compile(r"\bprobablemente\b", re.IGNORECASE),
)

INTERNAL_REF_PATTERN = re.compile(r"\[->\s*([^\]]+)\]")
URN_REF_PATTERN = re.compile(r"\[[^\]]+\]\((urn:[^)]+)\)")


def slugify_heading(text):
    slug = text.strip().lower()
    slug = re.sub(r"[^\w\s-]", "", slug, flags=re.UNICODE)
    slug = re.sub(r"\s+", "-", slug)
    return slug.strip("-")


def _collect_headings(body):
    headings = []
    for line in body.splitlines():
        stripped = line.strip()
        match = re.match(r"^(#{1,6})\s+(.+)$", stripped)
        if match:
            headings.append((len(match.group(1)), match.group(2).strip()))
    return headings


def _resolve_internal_refs(body, headings):
    resolved = {title for _level, title in headings}
    resolved |= {slugify_heading(title) for _level, title in headings}
    failures = []
    for ref in INTERNAL_REF_PATTERN.findall(body):
        normalized = ref.strip()
        if normalized not in resolved and slugify_heading(normalized) not in resolved:
            failures.append(f"referencia interna no resoluble: [-> {normalized}]")
    return failures


def validate_gn_markdown(path, expected_rel_path=None, expected_urn=None):
    frontmatter, body = load_markdown_parts(path)
    failures = []
    warnings = []

    if not isinstance(frontmatter, dict):
        return {
            "failures": ["frontmatter YAML ausente o invalido"],
            "warnings": [],
            "urn": None,
            "fs": None,
            "cr": None,
            "review_gate": None,
        }

    manifest = frontmatter.get("_manifest", {})
    urn = manifest.get("urn")
    if not urn:
        failures.append("_manifest.urn ausente")
    elif expected_urn and urn != expected_urn:
        failures.append(f"urn inesperado: {urn} != {expected_urn}")

    if expected_rel_path:
        stem = Path(expected_rel_path).stem
        parts = urn.split(":") if isinstance(urn, str) else []
        urn_id = parts[3] if len(parts) >= 4 else None
        if urn_id and urn_id != stem:
            warnings.append(f"path/urn no alineados: {expected_rel_path} vs {urn}")

    if frontmatter.get("lang") != "es":
        warnings.append("lang distinto de 'es'")

    tags = frontmatter.get("tags")
    if not isinstance(tags, list) or len(tags) < 3:
        failures.append("tags debe contener al menos 3 tags")

    extensions = frontmatter.get("extensions")
    if not isinstance(extensions, dict):
        failures.append("extensions debe existir y ser un objeto")
        gn_ext = {}
    else:
        gn_ext = extensions.get("gn")
        if not isinstance(gn_ext, dict):
            failures.append("extensions.gn ausente")
            gn_ext = {}

    required_gn_fields = (
        "source_paths",
        "source_hashes",
        "source_type",
        "transformation_mode",
        "fs",
        "cr",
        "run_id",
        "review_gate",
    )
    for field in required_gn_fields:
        if field not in gn_ext:
            failures.append(f"extensions.gn.{field} ausente")

    fs = gn_ext.get("fs")
    if fs != 100:
        failures.append(f"FS invalido: {fs}; se requiere 100")

    cr = gn_ext.get("cr")
    if not isinstance(cr, (int, float)):
        failures.append("CR invalido o ausente")
    elif cr < 1.5 and not gn_ext.get("cr_justification"):
        failures.append(f"CR={cr} < 1.5 sin justificacion")

    source_paths = gn_ext.get("source_paths", [])
    source_hashes = gn_ext.get("source_hashes", {})
    if isinstance(source_paths, list):
        missing_hashes = [item for item in source_paths if item not in source_hashes]
        if missing_hashes:
            failures.append(f"source_hashes incompleto para {len(missing_hashes)} fuente(s)")
    else:
        failures.append("extensions.gn.source_paths debe ser lista")

    headings = _collect_headings(body or "")
    if not headings:
        failures.append("cuerpo sin headings")
    else:
        if headings[0][0] != 1:
            failures.append("el primer heading debe ser '#'")
        if any(level > 4 for level, _title in headings):
            failures.append("hay headings con profundidad mayor a ####")
        top_level_count = sum(1 for level, _title in headings if level == 1)
        if top_level_count != 1:
            failures.append("debe existir exactamente un heading nivel #")
        if not any(level == 2 for level, _title in headings):
            failures.append("debe existir al menos una seccion ## recuperable")

    for pattern in FAT_PATTERNS:
        if pattern.search(body or ""):
            warnings.append(f"posible grasa detectada: {pattern.pattern}")

    failures.extend(_resolve_internal_refs(body or "", headings))

    for urn_ref in URN_REF_PATTERN.findall(body or ""):
        if not urn_ref.startswith("urn:"):
            failures.append(f"referencia URN invalida: {urn_ref}")

    return {
        "failures": failures,
        "warnings": warnings,
        "urn": urn,
        "fs": fs,
        "cr": cr,
        "review_gate": gn_ext.get("review_gate"),
    }


def validate_gn_tree(tree_root, expected_targets=None):
    expected_targets = expected_targets or {}
    failures = []
    warnings = []
    urn_to_path = {}

    for rel_path, meta in sorted(expected_targets.items()):
        file_path = tree_root / rel_path
        if not file_path.exists():
            failures.append(f"target faltante: {rel_path}")
            continue
        result = validate_gn_markdown(
            file_path,
            expected_rel_path=rel_path,
            expected_urn=meta.get("target_urn"),
        )
        failures.extend(f"{rel_path}: {item}" for item in result["failures"])
        warnings.extend(f"{rel_path}: {item}" for item in result["warnings"])
        urn = result["urn"]
        if urn:
            if urn in urn_to_path:
                failures.append(f"URN duplicado: {urn} en {urn_to_path[urn]} y {rel_path}")
            else:
                urn_to_path[urn] = rel_path

    return {
        "failures": failures,
        "warnings": warnings,
        "urns": urn_to_path,
    }
