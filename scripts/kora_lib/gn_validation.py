import re
from pathlib import Path

from .artifacts import load_markdown_parts
from .validation import find_field_like_markdown_headings, find_truncated_markdown_headings


FAT_PATTERNS = (
    re.compile(r"\bEn este documento veremos\b", re.IGNORECASE),
    re.compile(r"(?m)^\s*(?:[-*]\s+)?A continuaci[oó]n\b", re.IGNORECASE),
    re.compile(r"(?m)^\s*(?:[-*]\s+)?Por otro lado\b", re.IGNORECASE),
    re.compile(r"\bprobablemente\b", re.IGNORECASE),
)

INTERNAL_REF_PATTERN = re.compile(r"\[->\s*([^\]]+)\]")
URN_REF_PATTERN = re.compile(r"\[[^\]]+\]\((urn:[^)]+)\)")
MARKDOWN_LINK_PATTERN = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
BARE_URN_PATTERN = re.compile(r"urn:[A-Za-z0-9:_\-\.#]+")
LOCAL_PATH_PATTERN = re.compile(r"(?m)(^|[\s`])(staging/|domains/|source/|sources/|drafts/|build/|knowledge/|\.\./)")
KODA_RESIDUE_HEADING_TITLES = {
    "id",
    "version",
    "status",
    "format",
    "human creator",
    "human editor",
    "model collaborator",
    "ai remediator",
    "creation date",
    "modification date",
    "llm parsing instructions",
    "primary source",
}
ENGLISH_SCAFFOLD_TITLES = {
    "scope",
    "summary",
    "references",
    "reference",
    "sources",
    "source",
    "content",
}
FIELD_HEADING_TITLES_BY_FAMILY = {
    "inventory": {"id", "urn", "path", "tipo", "titulo", "artefactos"},
    "normative": {"contenido", "fuentes"},
    "glossary": {"nombre", "def"},
}
CONTAINER_ONLY_TITLES_BY_FAMILY = {
    "normative": {"glosas", "programas", "capitulos", "capítulos", "articulos", "artículos"},
}
REQUIRED_PRIMARY_TITLES_BY_FAMILY = {
    "cq_catalog": {"resumen"},
}
KODA_RESIDUE_PATTERNS = (
    re.compile(r"BEGIN_LLM_INSTRUCTIONS"),
    re.compile(r"END_LLM_INSTRUCTIONS"),
    re.compile(r"\bLLM_Parsing_Instructions\b"),
)
NONRECOVERABLE_PRIMARY_PATTERNS_BY_FAMILY = {
    "normative": (
        re.compile(r"^(?:glosa|articulo|artículo|programa|capitulo|capítulo)\s+\d+$", re.IGNORECASE),
    ),
}


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


def _collect_primary_sections(body):
    lines = body.splitlines()
    headings = []
    for index, line in enumerate(lines):
        match = re.match(r"^(#{1,6})\s+(.+)$", line.strip())
        if match:
            headings.append((index, len(match.group(1)), match.group(2).strip()))
    sections = []
    for idx, (line_index, level, title) in enumerate(headings):
        if level != 2:
            continue
        end = len(lines)
        for next_index, next_level, _next_title in headings[idx + 1 :]:
            if next_level <= 2:
                end = next_index
                break
        sections.append({"title": title, "lines": lines[line_index + 1 : end]})
    return sections


def _section_has_substance(lines):
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("#"):
            continue
        return True
    return False


def _reference_section_failures(body):
    failures = []
    lines = body.splitlines()
    headings = []
    for index, line in enumerate(lines):
        match = re.match(r"^(#{1,6})\s+(.+)$", line.strip())
        if match:
            headings.append((index, len(match.group(1)), match.group(2).strip()))
    for idx, (line_index, level, title) in enumerate(headings):
        normalized = slugify_heading(title).replace("-", " ")
        if normalized not in {"fuentes", "referencias"}:
            continue
        end = len(lines)
        for next_index, next_level, _next_title in headings[idx + 1 :]:
            if next_level <= level:
                end = next_index
                break
        for line in lines[line_index + 1 : end]:
            stripped = line.strip()
            if not stripped or stripped.startswith("#"):
                continue
            candidate = re.sub(r"^[-*]\s*", "", stripped)
            if candidate.startswith("[-> "):
                continue
            link_match = MARKDOWN_LINK_PATTERN.search(candidate)
            if link_match:
                target = link_match.group(1)
                if target.startswith("urn:") or target.startswith("https://"):
                    continue
            failures.append(f"referencia invalida en seccion {title}: {stripped}")
    return failures


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
        "document_family",
        "publication_class",
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
    document_family = gn_ext.get("document_family", "generic")
    publication_class = gn_ext.get("publication_class", "knowledge")
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
        residue_headings = [title for _level, title in headings if slugify_heading(title).replace("-", " ") in KODA_RESIDUE_HEADING_TITLES]
        if residue_headings:
            failures.append(f"residuo KODA en headings: {', '.join(sorted(dict.fromkeys(residue_headings))[:8])}")
        truncated_headings = find_truncated_markdown_headings(body or "")
        if truncated_headings:
            failures.append(f"heading truncado no permitido: {', '.join(sorted(dict.fromkeys(truncated_headings))[:8])}")
        if frontmatter.get("lang") == "es":
            english_headings = [title for _level, title in headings if slugify_heading(title).replace("-", " ") in ENGLISH_SCAFFOLD_TITLES]
            if english_headings:
                failures.append(f"heading scaffold no español: {', '.join(sorted(dict.fromkeys(english_headings))[:8])}")

    for pattern in FAT_PATTERNS:
        if pattern.search(body or ""):
            warnings.append(f"posible grasa detectada: {pattern.pattern}")

    for pattern in KODA_RESIDUE_PATTERNS:
        if pattern.search(body or ""):
            failures.append(f"residuo KODA en cuerpo: {pattern.pattern}")

    failures.extend(_resolve_internal_refs(body or "", headings))
    failures.extend(_reference_section_failures(body or ""))

    if publication_class == "knowledge":
        if LOCAL_PATH_PATTERN.search(body or ""):
            failures.append("referencia local o path operativo en cuerpo")

        primary_sections = _collect_primary_sections(body or "")
        present_primary_titles = {slugify_heading(section["title"]).replace("-", " ") for section in primary_sections}
        for section in primary_sections:
            normalized_title = slugify_heading(section["title"]).replace("-", " ")
            if not _section_has_substance(section["lines"]):
                failures.append(f"seccion primaria vacia o contenedor sin sustancia: {section['title']}")
            if normalized_title in CONTAINER_ONLY_TITLES_BY_FAMILY.get(document_family, set()):
                failures.append(f"seccion primaria contenedora no permitida para {document_family}: {section['title']}")
            for pattern in NONRECOVERABLE_PRIMARY_PATTERNS_BY_FAMILY.get(document_family, ()):
                if pattern.fullmatch(section["title"].strip()):
                    failures.append(f"heading primario no recuperable para {document_family}: {section['title']}")
        required_titles = REQUIRED_PRIMARY_TITLES_BY_FAMILY.get(document_family, set())
        missing_titles = sorted(required_titles - present_primary_titles)
        if missing_titles:
            failures.append(f"secciones primarias obligatorias ausentes para {document_family}: {', '.join(missing_titles)}")

        field_titles = FIELD_HEADING_TITLES_BY_FAMILY.get(document_family, set())
        if field_titles:
            field_headings = find_field_like_markdown_headings(body or "", field_titles)
            if field_headings:
                failures.append(f"heading-campo no permitido para {document_family}: {', '.join(sorted(dict.fromkeys(field_headings))[:8])}")

        if document_family == "glossary" and gn_ext.get("glossary_conflicts", 0):
            failures.append(f"conflictos de glosario sin resolver: {gn_ext.get('glossary_conflicts')}")

    for urn_ref in URN_REF_PATTERN.findall(body or ""):
        if not urn_ref.startswith("urn:"):
            failures.append(f"referencia URN invalida: {urn_ref}")
    if publication_class == "knowledge":
        body_without_links = MARKDOWN_LINK_PATTERN.sub("", body or "")
        if BARE_URN_PATTERN.search(body_without_links):
            failures.append("URN desnudo en cuerpo; usar referencia KORA con markdown")

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
