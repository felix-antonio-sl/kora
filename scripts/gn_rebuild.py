#!/usr/bin/env python3
"""GN rebuild pipeline aligned with KORA/MD v6.1."""

import argparse
import csv
import hashlib
import json
import math
import itertools
import os
import re
import shutil
import subprocess
import sys
from copy import deepcopy
from datetime import datetime, timezone
from pathlib import Path

import yaml


SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from kora_lib.artifacts import dump_yaml_frontmatter_and_body, load_markdown_parts, load_yaml_safe
from kora_lib.gn_validation import slugify_heading, validate_gn_tree
from kora_lib.gn_semantics import (
    BulletListBlock,
    DocumentIR,
    ParagraphBlock,
    RecordSetIR,
    ReferenceIR,
    ReferenceListBlock,
    SectionIR,
    TableIR,
    document_facts,
    render_document,
)


DEFAULT_REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MAP_PATH = DEFAULT_REPO_ROOT / "scripts" / "gn_rebuild_map.yml"
DEFAULT_SOURCE_ROOT = Path("/Users/felixsanhueza/Developer/gorenuble/knowledge")
DEFAULT_CONTROL_DRAFT_ROOT = Path("drafts/gn-control")
DEFAULT_CONTROL_ROOT = Path("docs/reports/gn-control")
TOP_LEVEL_KODA_TECHNICAL_KEYS = {
    "_manifest",
    "_meta",
    "ID",
    "Version",
    "Status",
    "Format",
    "Human-Creator",
    "Human-Editor",
    "Model-Collaborator",
    "AI-Remediator",
    "Creation-Date",
    "Modification-Date",
    "Source_ID",
    "Primary-Source",
    "Authoritative-Source",
    "Authoritative-Sources",
    "Authoritative_Sources",
    "Last-Validated",
    "Source-Hierarchy",
    "Ref-STS-Guide",
    "Ctx",
    "LLM_Parsing_Instructions",
}
NESTED_KODA_TECHNICAL_KEYS = {
    "LLM_Parsing_Instructions",
}
KODA_BODY_EXCLUDED_KEYS = {
    "ID",
    "Version",
    "Status",
    "Format",
    "Human-Creator",
    "Human-Editor",
    "Model-Collaborator",
    "AI-Remediator",
    "Creation-Date",
    "Modification-Date",
    "Source_ID",
    "Primary-Source",
    "Authoritative-Source",
    "Authoritative-Sources",
    "Authoritative_Sources",
    "Last-Validated",
    "Source-Hierarchy",
    "Ref-STS-Guide",
    "LLM_Parsing_Instructions",
    "_meta",
}
SEMANTIC_FIELD_LABELS = {
    "Act": "Acciones",
    "Alcance": "Alcance",
    "Asunto": "Asunto",
    "Columns": "Columnas",
    "Cond": "Condiciones",
    "Content": "Contenido",
    "Definitions": "Definiciones",
    "Definition": "Definición",
    "Ctx_Optional": "Contexto opcional",
    "Ctx_Required": "Contexto requerido",
    "Contexto": "Contexto",
    "Ctx": "Contexto",
    "Def": "Definicion",
    "Dependencia": "Dependencia",
    "Destinatarios": "Destinatarios",
    "Fnd": "Fundamento",
    "Headers": "Encabezados",
    "Intro": "Introduccion",
    "Mech": "Mecanismo",
    "Mssn": "Mision",
    "Obj": "Objetivos",
    "Proc": "Proceso",
    "Prohib": "Prohibiciones",
    "Purp": "Proposito",
    "Ref": "Referencias",
    "Ref_Fuente": "Referencias",
    "Relacion": "Relacion",
    "Req": "Requisitos",
    "Res": "Resultados",
    "Resp": "Responsables",
    "Rows": "Filas",
    "Sections": "Secciones",
    "Src": "Fuentes",
    "Titulo": "Titulo",
    "Title": "Titulo",
    "Unidad_Monetaria": "Unidad monetaria",
    "Warn": "Advertencias",
}
BULLET_FIELD_KEYS = {
    "Act",
    "Columns",
    "Cond",
    "Ctx",
    "Ctx_Optional",
    "Ctx_Required",
    "Def",
    "Dependencia",
    "Destinatarios",
    "Fnd",
    "Headers",
    "Intro",
    "Mech",
    "Mssn",
    "Obj",
    "Proc",
    "Prohib",
    "Purp",
    "Ref",
    "Relacion",
    "Req",
    "Res",
    "Resp",
    "Rows",
    "Sections",
    "Src",
    "Warn",
}
FIELD_HEADING_KEYS = {
    "Act",
    "Columns",
    "Cond",
    "Ctx",
    "Ctx_Optional",
    "Ctx_Required",
    "Def",
    "Dependencia",
    "Destinatarios",
    "Fnd",
    "Headers",
    "Mech",
    "Obj",
    "Proc",
    "Prohib",
    "Ref",
    "Relacion",
    "Req",
    "Res",
    "Resp",
    "Rows",
    "Sections",
    "Src",
    "Warn",
}
URN_TOKEN_PATTERN = re.compile(r"urn:[A-Za-z0-9:_\-\.#]+")
LEGACY_TARGET_ALIASES = {
    "cuentas-publicas-2021-2024": ["cuentas-publicas"],
    "flujos-aprobacion-documentos": ["aprobaciones"],
    "gestion-info-geoespacial": ["gestion-informacion-geoespacial"],
    "guia-circular-33-sts": ["guia-circ33"],
    "guia-fril-2025-sts": ["guia-fril"],
    "guia-frpd-nuble": ["guia-frpd"],
    "guia-idi-sni-sts": ["guia-idi-sni"],
    "guia-programas-directos-gore": ["guia-programas"],
    "instructivo-subvencion-8-2025-sts": ["instructivo-subvencion-8"],
    "ley-presupuestos-2026-normas-generales": ["ley-presupuestos-2026-normas"],
    "ley-presupuestos-2026-partida-31": ["ley-presupuestos-2026-p31"],
    "manual-induccion-gore-nuble-2026": ["manual-induccion"],
    "nuble-250": ["nuble250"],
}
STATIC_URN_ALIASES = {
    "urn:knowledge:gorenuble:core:gestion:lean6:1.0.1": "urn:mgmt:kb:lean6",
    "urn:knowledge:gorenuble:core:gestion:meyer-org-structure:1.0.0": "urn:mgmt:kb:meyer-org-structure",
    "urn:knowledge:gorenuble:estadocl:estructura-estado-chile:1.0.0": "urn:mgmt:kb:estructura-estado-chile",
}
UNRESOLVABLE_URN_LABELS = {
    "urn:goreos:omega:schema:2.0.0": "Omega schema 2.0.0",
    "urn:knowledge:koda:core:spec:1.0.0": "KODA Core Spec 1.0.0",
}
FRAGMENTLESS_TARGET_URNS = {
    "urn:gn:kb:glosas-gores-2026",
    "urn:gn:kb:ley-presupuestos-2026-normas-generales",
    "urn:gn:kb:ley-presupuestos-2026-partida-31",
}
ENGLISH_SCAFFOLD_LABELS = {
    "Scope": "Alcance",
    "Summary": "Resumen",
    "Sources": "Fuentes",
    "Source": "Fuente",
    "Content": "Contenido",
    "References": "Referencias",
    "Question": "Pregunta",
}
CONTROL_PUBLICATION_CLASS = "control"
KNOWLEDGE_PUBLICATION_CLASS = "knowledge"
TITLE_LIKE_KEYS = {"Title", "Titulo", "title", "titulo", "Name", "Nombre", "name", "nombre"}
SOURCE_TEXT_REFERENCE_ALIASES = (
    (
        re.compile(r"ley org[áa]nica constitucional.*gobierno y administraci[oó]n regional|locgar|ley\s*n[°º]?\s*19\.175", re.IGNORECASE),
        "urn:gn:kb:loc-gore",
        "LOC GORE",
    ),
)


def sha256_file(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def deep_merge_dicts(base, patch):
    result = deepcopy(base)
    for key, value in patch.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge_dicts(result[key], value)
        else:
            result[key] = deepcopy(value)
    return result


def load_yaml_merged(path):
    text = path.read_text(encoding="utf-8")
    docs = [doc for doc in yaml.safe_load_all(text) if doc is not None]
    if not docs:
        return None
    merged = {}
    non_dict_docs = []
    for doc in docs:
        if isinstance(doc, dict):
            merged = deep_merge_dicts(merged, doc)
        else:
            non_dict_docs.append(doc)
    if merged:
        if non_dict_docs:
            merged["_extra_documents"] = non_dict_docs
        return merged
    if len(non_dict_docs) == 1:
        return non_dict_docs[0]
    return {"_extra_documents": non_dict_docs}


def utc_today():
    return datetime.now(timezone.utc).date().isoformat()


def now_run_id():
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def title_from_slug(slug):
    return slug.replace("-", " ").replace("_", " ").strip().title()


def headingify(key):
    text = key.replace("_", " ").replace("-", " ").strip()
    if not text:
        return "Contenido"
    return text[0].upper() + text[1:]


def field_label(key):
    return SEMANTIC_FIELD_LABELS.get(key, headingify(str(key)))


def normalize_scalar(value):
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    text = str(value)
    if "BEGIN_LLM_INSTRUCTIONS" in text:
        text = re.sub(r"BEGIN_LLM_INSTRUCTIONS.*?(END_LLM_INSTRUCTIONS|$)", "", text, flags=re.DOTALL)
        text = text.strip()
    text = re.sub(r"(?m)^(#{1,6}\s)", r"\\\1", text)
    return text


def escape_markdown_table_cell(value):
    if isinstance(value, list) and all(not isinstance(item, (dict, list)) for item in value):
        value = ", ".join(normalize_scalar(item) for item in value)
    return normalize_scalar(value).replace("|", "\\|").replace("\n", "<br>")


def legacy_namespace_from_source_path(source_path):
    parts = Path(source_path).parts
    try:
        domains_index = parts.index("domains")
    except ValueError:
        return None
    if len(parts) <= domains_index + 4:
        return None
    return parts[domains_index + 3]


def legacy_slug_from_source_path(source_path):
    stem = Path(source_path).stem
    for suffix in ("_koda", "_master", "_catalog", "_index"):
        if stem.endswith(suffix):
            stem = stem[: -len(suffix)]
            break
    parts = stem.split("_")
    if len(parts) >= 4 and parts[0] == "kb" and parts[2].isdigit():
        stem = "_".join(parts[3:])
    elif len(parts) >= 5 and parts[0] == "kb" and parts[1] == "core" and parts[3].isdigit():
        stem = "_".join(parts[4:])
    return stem.replace("_", "-")


def build_urn_alias_maps(map_doc):
    alias_map = dict(STATIC_URN_ALIASES)
    external_labels = dict(UNRESOLVABLE_URN_LABELS)
    for entry in map_doc.get("entries", []):
        target_urn = entry.get("target_urn")
        if not target_urn:
            continue
        target_slug = Path(entry["target_path"]).stem
        legacy_ids = {target_slug}
        legacy_ids.update(LEGACY_TARGET_ALIASES.get(target_slug, []))
        namespaces = set()
        for source_path in entry.get("source_paths", []):
            source_slug = legacy_slug_from_source_path(source_path)
            if source_slug:
                legacy_ids.add(source_slug)
                namespace = legacy_namespace_from_source_path(source_path)
                if namespace:
                    namespaces.add(namespace)
                    alias_map[f"urn:knowledge:gorenuble:{namespace}:{source_slug}:1.0.0"] = target_urn
        for legacy_id in legacy_ids:
            alias_map[f"urn:knowledge:gorenuble:gn:{legacy_id}:1.0.0"] = target_urn
            for namespace in namespaces:
                alias_map[f"urn:knowledge:gorenuble:{namespace}:{legacy_id}:1.0.0"] = target_urn
    return alias_map, external_labels


def build_urn_title_map(map_doc, knowledge_root):
    title_map = {}
    for entry in map_doc.get("entries", []):
        target_urn = entry.get("target_urn")
        if not target_urn:
            continue
        current_meta = resolve_current_target_metadata(knowledge_root, entry["target_path"])
        title_map[target_urn] = entry.get("target_title") or current_meta["title"]
    title_map.update(
        {
            "urn:gn:kb:loc-gore": "LOC GORE",
            "urn:mgmt:kb:estructura-estado-chile": "Estructura del Estado de Chile",
        }
    )
    return title_map


def english_to_spanish_scaffold(text):
    return ENGLISH_SCAFFOLD_LABELS.get(text, text)


def resolve_target_urn(base, urn_alias_map):
    if not base:
        return None
    if base in urn_alias_map:
        return urn_alias_map[base]
    if base.startswith("urn:gn:kb:"):
        return base
    legacy_match = re.match(r"^urn:knowledge:gorenuble:([^:]+):([^:]+):([^:]+)$", base)
    if legacy_match:
        namespace, legacy_id, _version = legacy_match.groups()
        candidates = (
            f"urn:knowledge:gorenuble:{namespace}:{legacy_id}:1.0.0",
            f"urn:knowledge:gorenuble:gn:{legacy_id}:1.0.0",
        )
        for candidate in candidates:
            if candidate in urn_alias_map:
                return urn_alias_map[candidate]
    return None


def render_reference_markdown(ref):
    if ref.kind == "internal":
        return f"[-> {ref.label}]"
    return f"[{ref.label}]({ref.target})"


def clean_joined_text(text):
    text = re.sub(r"\s+([,.;:)\]])", r"\1", text)
    text = re.sub(r"([(\[])\s+", r"\1", text)
    text = re.sub(r"\s{2,}", " ", text)
    return text.strip()


def render_inline_fragment(fragment, urn_alias_map, external_labels, urn_title_map):
    if fragment is None:
        return ""
    if isinstance(fragment, (str, int, float, bool)):
        return normalize_scalar(fragment)
    if isinstance(fragment, list):
        parts = [render_inline_fragment(item, urn_alias_map, external_labels, urn_title_map) for item in fragment]
        return clean_joined_text(" ".join(part for part in parts if part))
    if isinstance(fragment, dict):
        if not fragment:
            return ""
        if set(fragment.keys()) <= {"Ref"} and fragment.get("Ref") is not None:
            return normalize_scalar(fragment["Ref"])
        for key in ("XRef", "XRef_Required", "Src", "Source", "Ctx_Required", "Ctx_Optional", "Ref_Fuente"):
            if key in fragment:
                ref = source_text_to_reference(fragment.get(key), urn_alias_map, external_labels, urn_title_map)
                if ref:
                    return render_reference_markdown(ref)
                return ""
        for key in ("Content", "Contenido"):
            if key in fragment:
                return render_inline_fragment(fragment[key], urn_alias_map, external_labels, urn_title_map)
        parts = [render_inline_fragment(value, urn_alias_map, external_labels, urn_title_map) for value in fragment.values()]
        return clean_joined_text(" ".join(part for part in parts if part))
    return normalize_scalar(fragment)


def inline_text_from_value(value, urn_alias_map, external_labels, urn_title_map):
    text = render_inline_fragment(value, urn_alias_map, external_labels, urn_title_map)
    return text.strip()


def content_blocks_from_mapping(node, urn_alias_map, external_labels, urn_title_map):
    if not isinstance(node, dict):
        return None
    content_key = next((key for key in ("Content", "Contenido") if key in node), None)
    allowed_keys = {"ID", "Content", "Contenido", "Src", "Source", "Ref_Fuente", "XRef", "XRef_Required", "Ctx_Required", "Ctx_Optional"}
    if not content_key or any(key not in allowed_keys for key in node.keys()):
        return None
    text = inline_text_from_value(node.get(content_key), urn_alias_map, external_labels, urn_title_map)
    blocks = []
    if text:
        blocks.append(ParagraphBlock(text))
    refs_value = None
    for key in ("Src", "Source", "Ref_Fuente", "XRef", "XRef_Required", "Ctx_Required", "Ctx_Optional"):
        if key in node:
            refs_value = node.get(key)
            break
    refs = scalar_reference_list("Referencias", refs_value, urn_alias_map, external_labels, urn_title_map)
    if refs:
        blocks.append(refs)
    return blocks if blocks else None


def section_title_from_mapping(fallback_title, mapping):
    if not isinstance(mapping, dict):
        return fallback_title
    for key in ("Title", "Titulo"):
        value = mapping.get(key)
        if isinstance(value, str) and value.strip():
            return english_to_spanish_scaffold(normalize_scalar(value))
    return fallback_title


def strip_title_like_fields(mapping):
    if not isinstance(mapping, dict):
        return mapping
    return {key: value for key, value in mapping.items() if key not in TITLE_LIKE_KEYS}


def normalize_body_urns(body, urn_alias_map, external_labels, urn_title_map):
    bare_urn_pattern = re.compile(r"(?<!\()urn:[A-Za-z0-9:_\-\.#]+")

    def replace(match):
        token = match.group(0)
        suffix = ""
        while token and token[-1] in ".,;:":
            suffix = token[-1] + suffix
            token = token[:-1]

        base, fragment = token.split("#", 1) if "#" in token else (token, None)
        normalized = resolve_target_urn(base, urn_alias_map)
        if normalized:
            if fragment and normalized not in FRAGMENTLESS_TARGET_URNS:
                normalized = f"{normalized}#{fragment}"
            label = urn_title_map.get(normalized, normalized)
            return f"[{label}]({normalized})" + suffix
        if base in external_labels:
            return external_labels[base] + suffix
        return token + suffix

    return bare_urn_pattern.sub(replace, body)


def target_root_for_entry(roots, entry):
    publication_class = entry.get("publication_class", KNOWLEDGE_PUBLICATION_CLASS)
    if publication_class == CONTROL_PUBLICATION_CLASS:
        return roots["control_draft_root"]
    return roots["draft_root"]


def publication_output_root(roots, entry):
    publication_class = entry.get("publication_class", KNOWLEDGE_PUBLICATION_CLASS)
    if publication_class == CONTROL_PUBLICATION_CLASS:
        return roots["control_root"]
    return roots["knowledge_root"]


def entry_expected_meta(entry):
    return {
        "target_urn": entry.get("target_urn"),
        "document_family": entry.get("document_family", "generic"),
        "publication_class": entry.get("publication_class", KNOWLEDGE_PUBLICATION_CLASS),
    }


def looks_like_local_path(value):
    text = str(value).strip()
    return bool(re.search(r"(^|[\s`])(staging/|domains/|source/|sources/|build/|drafts/|knowledge/|\.\./)", text))


def source_text_to_reference(value, urn_alias_map, external_labels, urn_title_map):
    if value is None:
        return None
    text = normalize_scalar(value).strip()
    if not text or looks_like_local_path(text):
        return None
    if text.startswith("https://"):
        label = re.sub(r"^https://", "", text).strip("/")
        return ReferenceIR(kind="external", label=label or text, target=text)
    urn_match = URN_TOKEN_PATTERN.search(text)
    if urn_match:
        token = urn_match.group(0)
        base, fragment = token.split("#", 1) if "#" in token else (token, None)
        normalized = resolve_target_urn(base, urn_alias_map)
        if normalized:
            if fragment and normalized not in FRAGMENTLESS_TARGET_URNS:
                normalized = f"{normalized}#{fragment}"
            return ReferenceIR(kind="kora", label=urn_title_map.get(normalized, normalized), target=normalized)
        if base in external_labels:
            return None
    for pattern, urn, label in SOURCE_TEXT_REFERENCE_ALIASES:
        if pattern.search(text):
            return ReferenceIR(kind="kora", label=label, target=urn)
    return None


def normalize_editorial_phrasing(body):
    replacements = (
        ("A continuación se define su estructura detallada.", "Su estructura detallada es la siguiente."),
        ("A continuación se presentan ", "Se presentan "),
        ("A continuación, se describen ", "Se describen "),
        (
            "Por otro lado, existen diversas posibilidades de optar a actividades de capacitación,",
            "Existen diversas posibilidades de optar a actividades de capacitación,",
        ),
    )
    for old, new in replacements:
        body = body.replace(old, new)
    return body


def collect_tree_manifest_urns(tree_root):
    urns = set()
    if not tree_root.exists():
        return urns
    for path in tree_root.rglob("*.md"):
        frontmatter, _body = load_markdown_parts(path)
        if not isinstance(frontmatter, dict):
            continue
        urn = frontmatter.get("_manifest", {}).get("urn")
        if urn:
            urns.add(urn)
    return urns


def collect_tree_fragments(tree_root):
    fragments = {}
    if not tree_root.exists():
        return fragments
    for path in tree_root.rglob("*.md"):
        frontmatter, body = load_markdown_parts(path)
        if not isinstance(frontmatter, dict):
            continue
        urn = frontmatter.get("_manifest", {}).get("urn")
        if not urn:
            continue
        anchors = set()
        for line in (body or "").splitlines():
            match = re.match(r"^(#{1,6})\s+(.+)$", line.strip())
            if match:
                anchors.add(slugify_heading(match.group(2).strip()))
        for explicit in re.findall(r"\{#([^}]+)\}", body or ""):
            anchors.add(explicit.strip())
        fragments[urn] = anchors
    return fragments


def rewrite_tree_status(tree_root, status):
    for path in sorted(tree_root.rglob("*.md")):
        frontmatter, body = load_markdown_parts(path)
        if not isinstance(frontmatter, dict):
            continue
        frontmatter["status"] = status
        dump_yaml_frontmatter_and_body(path, frontmatter, body)


def validate_body_urn_resolution(tree_root, allowed_urns, fragment_catalog=None):
    failures = []
    for path in sorted(tree_root.rglob("*.md")):
        _frontmatter, body = load_markdown_parts(path)
        for token in URN_TOKEN_PATTERN.findall(body or ""):
            normalized = token.rstrip(".,;:")
            base, fragment = normalized.split("#", 1) if "#" in normalized else (normalized, None)
            if base not in allowed_urns:
                failures.append(f"{path.relative_to(tree_root)}: URN no resoluble en cuerpo: {base}")
                continue
            if fragment and fragment_catalog is not None:
                known_fragments = fragment_catalog.get(base, set())
                if fragment not in known_fragments:
                    failures.append(f"{path.relative_to(tree_root)}: fragmento URN no resoluble: {base}#{fragment}")
    return failures


def is_table_candidate(items):
    if not items or not all(isinstance(item, dict) for item in items):
        return False
    headers = dict_list_headers(items)
    return bool(headers)


def dict_list_headers(items):
    if not items or not all(isinstance(item, dict) for item in items):
        return []
    headers = []
    seen = set()
    scalar_header_count = {}
    for item in items:
        for key, value in item.items():
            if isinstance(value, dict):
                continue
            if isinstance(value, list) and any(isinstance(child, (dict, list)) for child in value):
                continue
            scalar_header_count[key] = scalar_header_count.get(key, 0) + 1
            if key not in seen:
                seen.add(key)
                headers.append(key)
    min_presence = max(1, math.ceil(len(items) * 0.5))
    return [header for header in headers if scalar_header_count.get(header, 0) >= min_presence]


def render_dict_table(items):
    headers = dict_list_headers(items)
    if not headers:
        return []
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for item in items:
        lines.append("| " + " | ".join(escape_markdown_table_cell(item.get(header, "")) for header in headers) + " |")
    return lines


def is_columns_rows_table(node):
    if not isinstance(node, dict):
        return False
    return isinstance(node.get("Columns"), list) and isinstance(node.get("Rows"), list)


def is_headers_rows_table(node):
    if not isinstance(node, dict):
        return False
    return isinstance(node.get("Headers"), list) and isinstance(node.get("Rows"), list)


def render_columns_rows_table(node):
    raw_headers = node.get("Columns") if "Columns" in node else node.get("Headers", [])
    headers = [escape_markdown_table_cell(item) for item in raw_headers]
    rows = node.get("Rows", [])
    if not headers:
        return []
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in rows:
        if not isinstance(row, list):
            continue
        padded = list(row) + [""] * max(0, len(headers) - len(row))
        lines.append("| " + " | ".join(escape_markdown_table_cell(item) for item in padded[: len(headers)]) + " |")
    return lines


def is_scalar_or_scalar_list(value):
    if isinstance(value, (str, int, float, bool)) or value is None:
        return True
    if isinstance(value, list):
        return all(not isinstance(item, (dict, list)) for item in value)
    return False


def render_field_block(label, value, level):
    heading_level = min(level + 1, 4)
    lines = [f"{'#' * heading_level} {label}"]
    if isinstance(value, list):
        if value and all(not isinstance(item, (dict, list)) for item in value):
            lines.extend(f"- {normalize_scalar(item)}" for item in value)
        elif is_table_candidate(value):
            lines.extend(render_dict_table(value))
        else:
            for item in value:
                if isinstance(item, dict):
                    lines.append("-")
                    for row in render_kora_node(item, heading_level):
                        lines.append(f"  {row}" if row else "")
                else:
                    lines.append(f"- {normalize_scalar(item)}")
    elif isinstance(value, dict):
        lines.extend(render_kora_node(value, heading_level))
    else:
        lines.append(normalize_scalar(value))
    return lines


def render_kora_node(node, level):
    lines = []
    if is_columns_rows_table(node) or is_headers_rows_table(node):
        lines.extend(render_columns_rows_table(node))
        return lines
    if isinstance(node, list) and is_table_candidate(node):
        lines.extend(render_dict_table(node))
        return lines

    if isinstance(node, dict):
        for key, value in node.items():
            if key in KODA_BODY_EXCLUDED_KEYS:
                continue
            if is_columns_rows_table(value) or is_headers_rows_table(value):
                lines.append(f"{'#' * min(level + 1, 4)} {field_label(key)}")
                lines.extend(render_columns_rows_table(value))
                continue
            if key in BULLET_FIELD_KEYS and is_scalar_or_scalar_list(value):
                lines.extend(render_field_block(field_label(key), value, level))
                continue
            if isinstance(value, list) and is_table_candidate(value):
                lines.append(f"{'#' * min(level + 1, 4)} {field_label(key)}")
                lines.extend(render_dict_table(value))
                continue

            heading_level = min(level + 1, 4)
            lines.append(f"{'#' * heading_level} {field_label(key)}")
            if isinstance(value, dict):
                lines.extend(render_kora_node(value, heading_level))
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, dict):
                        if is_table_candidate([item]):
                            lines.extend(render_dict_table([item]))
                        else:
                            lines.append("-")
                            rendered = render_kora_node(item, heading_level)
                            lines.extend(f"  {line}" if line else "" for line in rendered)
                    else:
                        lines.append(f"- {normalize_scalar(item)}")
            else:
                lines.append(normalize_scalar(value))
        return lines

    if isinstance(node, list):
        for item in node:
            if isinstance(item, dict):
                lines.append("-")
                rendered = render_kora_node(item, level)
                lines.extend(f"  {line}" if line else "" for line in rendered)
            else:
                lines.append(f"- {normalize_scalar(item)}")
        return lines

    lines.append(normalize_scalar(node))
    return lines


def canonical_scalar_facts(node, prefix="", facts=None):
    if facts is None:
        facts = []
    if isinstance(node, dict):
        for key in sorted(node.keys()):
            child_prefix = f"{prefix}.{key}" if prefix else str(key)
            canonical_scalar_facts(node[key], child_prefix, facts)
    elif isinstance(node, list):
        for index, item in enumerate(node):
            child_prefix = f"{prefix}[{index}]"
            canonical_scalar_facts(item, child_prefix, facts)
    else:
        facts.append(f"{prefix}={normalize_scalar(node)}")
    return facts


def project_yaml_structured(doc):
    return {
        "kind": "structured",
        "facts": canonical_scalar_facts(doc),
        "skeleton": sorted(doc.keys()) if isinstance(doc, dict) else [],
        "meat_count": len(canonical_scalar_facts(doc)),
        "fat_count": 0,
        "data": doc,
        "raw_data": doc,
    }


def project_koda_structured(doc):
    semantic_doc = strip_koda_technical_fields(doc)
    facts = canonical_scalar_facts(semantic_doc)
    skeleton = sorted(semantic_doc.keys()) if isinstance(semantic_doc, dict) else []
    return {
        "kind": "koda_structured",
        "facts": facts,
        "skeleton": skeleton,
        "meat_count": len(facts),
        "fat_count": 0,
        "data": semantic_doc,
        "raw_data": doc,
    }


def project_ttl_scope(text, scope_statement):
    tokens = [token.lower() for token in scope_statement.split() if token.strip()]
    lines = []
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if not tokens or any(token in line.lower() for token in tokens):
            lines.append(line)
    if not lines:
        lines = [line.strip() for line in text.splitlines() if line.strip() and not line.strip().startswith("#")][:25]
    lines = sorted(dict.fromkeys(lines))
    return {
        "kind": "ttl_scope",
        "scope_statement": scope_statement,
        "facts": lines,
        "skeleton": ["scope", "triples"],
        "meat_count": len(lines),
        "fat_count": 0,
        "data": lines,
    }


def project_csv_scope(path, scope_statement):
    rows = []
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            rows.append(dict(row))
    facts = []
    for index, row in enumerate(rows):
        normalized_row = {}
        for key, value in row.items():
            normalized_key = str(key) if key is not None else "__extra__"
            normalized_row[normalized_key] = value
        rows[index] = normalized_row
        for key in sorted(normalized_row.keys()):
            facts.append(f"row[{index}].{key}={normalize_scalar(normalized_row[key])}")
    return {
        "kind": "csv_scope",
        "scope_statement": scope_statement,
        "facts": facts,
        "skeleton": list(rows[0].keys()) if rows else [],
        "meat_count": len(facts),
        "fat_count": 0,
        "data": rows,
    }


def project_markdown_source(path):
    frontmatter, body = load_markdown_parts(path)
    payload = {
        "frontmatter": frontmatter if isinstance(frontmatter, dict) else {},
        "body": body.strip(),
    }
    return {
        "kind": "markdown",
        "facts": canonical_scalar_facts(payload),
        "skeleton": ["frontmatter", "body"],
        "meat_count": len(canonical_scalar_facts(payload)),
        "fat_count": 0,
        "data": payload,
    }


def project_source(path, source_type, scope_statement=None):
    suffix = path.suffix.lower()
    if suffix in {".yml", ".yaml", ".json"}:
        if suffix in {".yml", ".yaml"}:
            doc = load_yaml_merged(path)
            err = None if doc is not None else "empty YAML"
        else:
            doc, err = load_yaml_safe(path)
        if err:
            raise ValueError(f"no fue posible parsear {path}: {err}")
        if source_type in {"koda_yaml", "ontology_yaml", "mixed"} and isinstance(doc, dict):
            return project_koda_structured(doc)
        return project_yaml_structured(doc)
    if suffix == ".ttl":
        return project_ttl_scope(path.read_text(encoding="utf-8"), scope_statement or "")
    if suffix == ".csv":
        return project_csv_scope(path, scope_statement or "")
    if suffix == ".md":
        return project_markdown_source(path)
    return {
        "kind": "raw_text",
        "facts": [line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()],
        "skeleton": ["raw"],
        "meat_count": 0,
        "fat_count": 0,
        "data": path.read_text(encoding="utf-8"),
    }


def render_markdown_value(value, level):
    if is_columns_rows_table(value):
        return render_columns_rows_table(value)
    lines = []
    if isinstance(value, dict):
        for key, child in value.items():
            if key in KODA_BODY_EXCLUDED_KEYS:
                continue
            heading_level = min(level + 1, 4)
            lines.append(f"{'#' * heading_level} {field_label(str(key))}")
            lines.extend(render_markdown_value(child, heading_level))
    elif isinstance(value, list):
        if is_table_candidate(value):
            headers = list(value[0].keys())
            lines.append("| " + " | ".join(headers) + " |")
            lines.append("| " + " | ".join("---" for _ in headers) + " |")
            for item in value:
                lines.append("| " + " | ".join(escape_markdown_table_cell(item.get(header, "")) for header in headers) + " |")
        else:
            for item in value:
                if isinstance(item, (dict, list)):
                    lines.append("-")
                    rendered = render_markdown_value(item, min(level + 1, 4))
                    lines.extend(f"  {line}" if line else "" for line in rendered)
                else:
                    lines.append(f"- {normalize_scalar(item)}")
    else:
        lines.append(normalize_scalar(value))
    return lines


def render_direct_body(title, projection):
    lines = [f"# {title}"]
    data = projection["data"]
    if isinstance(data, dict):
        top_keys = [key for key in data.keys() if key != "_manifest"]
        if not top_keys:
            top_keys = list(data.keys())
        for key in top_keys:
            if key in KODA_BODY_EXCLUDED_KEYS:
                continue
            if len(top_keys) == 1 and isinstance(data[key], dict):
                lines.extend(render_kora_node(data[key], 1))
                lines.append("")
                continue
            lines.append(f"## {field_label(str(key))}")
            lines.extend(render_kora_node(data[key], 2))
            lines.append("")
    else:
        lines.append("## Contenido")
        lines.extend(render_kora_node(data, 2))
    return "\n".join(line for line in lines if line is not None).strip() + "\n"


def strip_koda_technical_fields(node, depth=0):
    if isinstance(node, dict):
        cleaned = {}
        semantic_siblings = []
        for key in node.keys():
            if depth == 0 and key in TOP_LEVEL_KODA_TECHNICAL_KEYS:
                continue
            if depth > 0 and key in NESTED_KODA_TECHNICAL_KEYS:
                continue
            semantic_siblings.append(key)
        for key, value in node.items():
            if depth == 0 and key in TOP_LEVEL_KODA_TECHNICAL_KEYS:
                continue
            if depth > 0 and key in NESTED_KODA_TECHNICAL_KEYS:
                continue
            if (
                key == "Content"
                and isinstance(value, dict)
                and ("Body_MD" in value or "Content" in value)
                and any(sibling != "Content" for sibling in semantic_siblings)
            ):
                continue
            cleaned[key] = strip_koda_technical_fields(value, depth + 1)
        return cleaned
    if isinstance(node, list):
        return [strip_koda_technical_fields(item, depth + 1) for item in node]
    return node


def find_embedded_markdown(node):
    if isinstance(node, dict):
        for key, value in node.items():
            candidate = find_embedded_markdown(value)
            if candidate:
                return candidate
            if isinstance(value, str):
                text = value.strip()
                if re.search(r"(?m)^#\s+", text) and len(text.splitlines()) >= 5:
                    return text
    elif isinstance(node, list):
        for item in node:
            candidate = find_embedded_markdown(item)
            if candidate:
                return candidate
    elif isinstance(node, str):
        text = node.strip()
        if re.search(r"(?m)^#\s+", text) and len(text.splitlines()) >= 5:
            return text
    return None


def embedded_markdown_looks_kora_like(text):
    banned_patterns = (
        r"(?m)^##\s+ID\b",
        r"(?m)^##\s+Version\b",
        r"(?m)^##\s+Status\b",
        r"(?m)^##\s+Format\b",
        r"(?m)^##\s+LLM Parsing Instructions\b",
        r"(?m)^#{2,4}\s+(Id|Urn|Path|Tipo)\b",
        r"BEGIN_LLM_INSTRUCTIONS",
        r"END_LLM_INSTRUCTIONS",
    )
    if any(re.search(pattern, text) for pattern in banned_patterns):
        return False
    if len(re.findall(r"(?m)^\s*###\s+Nombre\s*$", text)) >= 2 and len(re.findall(r"(?m)^\s*###\s+Def\s*$", text)) >= 2:
        return False
    return True


def render_koda_hybrid_body(title, projection):
    data = strip_koda_technical_fields(projection["data"])
    embedded_body = find_embedded_markdown(data)
    if embedded_body and embedded_markdown_looks_kora_like(embedded_body):
        return embedded_body.rstrip() + "\n"

    if isinstance(data, dict):
        semantic_keys = list(data.keys())
        if len(semantic_keys) == 1 and isinstance(data[semantic_keys[0]], dict):
            data = data[semantic_keys[0]]

    hybrid_projection = dict(projection)
    hybrid_projection["data"] = data
    return render_direct_body(title, hybrid_projection)


def render_composite_body(title, item, projections):
    lines = [f"# {title}", "", "## Alcance", item.get("scope_statement") or "Vista compuesta con procedencia explicita."]
    items = list(projections.items())
    if not items:
        return "\n".join(lines).strip() + "\n"

    primary_source, primary_projection = items[0]
    if str(primary_source).endswith((".yml", ".yaml", ".json")):
        primary_body = render_koda_hybrid_body(title, primary_projection).splitlines()
        filtered = [line for line in primary_body if not line.startswith("# ")]
        lines.extend(filtered)
    else:
        lines.extend(render_markdown_value(primary_projection["data"], 2))

    if len(items) > 1:
        lines.extend(["", "## Fuentes derivadas"])
        for source_path, projection in items[1:]:
            lines.extend(render_secondary_source_summary(source_path, projection))
    return "\n".join(lines).strip() + "\n"


def render_ttl_body(title, item, projection):
    data = projection["data"]
    if isinstance(data, dict):
        if data.get("_meta", {}).get("type") == "Ω-Ontology":
            return render_omega_body(title, item, data)
        return render_cqs_catalog_body(title, item, data)

    lines = [f"# {title}", "", "## Scope", item["scope_statement"], "", "## Triples"]
    for triple in projection["data"]:
        lines.append(f"- `{triple}`")
    return "\n".join(lines).strip() + "\n"


def render_csv_body(title, item, projection):
    lines = [
        f"# {title}",
        "",
        "## Scope",
        item["scope_statement"],
        "",
        "## Resumen",
        f"- Filas: {len(projection['data'])}",
        f"- Columnas: {len(projection['skeleton'])}",
    ]
    if projection["data"]:
        headers = list(projection["data"][0].keys())
        sample_rows = projection["data"][: min(10, len(projection["data"]))]
        lines.extend(["", "## Muestra"])
        lines.append("| " + " | ".join(headers) + " |")
        lines.append("| " + " | ".join("---" for _ in headers) + " |")
        for row in sample_rows:
            lines.append("| " + " | ".join(normalize_scalar(row.get(header, "")) for header in headers) + " |")
    return "\n".join(lines).strip() + "\n"


def render_index_body(title, item):
    lines = [f"# {title}", "", "## Entradas"]
    for dependency in item.get("dependencies", []):
        dep_path = str(dependency).replace(".md", "")
        label = headingify(Path(dep_path).stem)
        lines.append(f"- `{dep_path}` - {label}")
    return "\n".join(lines).strip() + "\n"


def render_secondary_source_summary(source_path, projection):
    lines = [f"### {headingify(Path(source_path).stem)}", f"- Fuente: `{source_path}`"]
    if projection["kind"] == "ttl_scope":
        lines.append(f"- Tipo: TTL derivado")
        lines.append(f"- Hechos capturados: {len(projection['facts'])}")
        lines.append("- Presentacion: resumen de soporte derivado; detalles completos en evidence.")
        return lines

    data = projection["data"]
    if isinstance(data, dict):
        keys = list(data.keys())[:10]
        lines.append(f"- Tipo: estructurado")
        if keys:
            lines.append(f"- Claves: {', '.join(keys)}")
    elif isinstance(data, list):
        lines.append(f"- Tipo: lista")
        lines.append(f"- Elementos: {len(data)}")
    else:
        lines.append(f"- Tipo: texto")
    return lines


def render_cqs_catalog_body(title, item, data):
    type_labels = {
        "Existenciales": "Existencial",
        "Relacionales": "Relacional",
        "Temporales": "Temporal",
        "Agregacion": "Agregación",
    }
    stats = data.get("_manifest", {}).get("statistics", {})
    lines = [f"# {title}", "", "## Scope", item["scope_statement"], "", "## Resumen"]
    if stats:
        if "total_cqs" in stats:
            lines.append(f"- Total CQs: {stats['total_cqs']}")
        if "domains" in stats:
            lines.append(f"- Dominios: {stats['domains']}")
        if isinstance(stats.get("types"), dict):
            for key, value in stats["types"].items():
                lines.append(f"- {headingify(str(key))}: {value}")

    domain_keys = [key for key in data.keys() if key.startswith("Dom_")]
    for domain_key in domain_keys:
        domain = data.get(domain_key, {})
        lines.extend(["", f"## {headingify(domain_key.replace('Dom_', '').replace('_', ' '))}"])
        counts = []
        for bucket in ("Existenciales", "Relacionales", "Temporales", "Agregacion"):
            values = domain.get(bucket, [])
            if isinstance(values, list):
                counts.append(f"{bucket}: {len(values)}")
        if counts:
            lines.append("- " + " | ".join(counts))
        for bucket in ("Existenciales", "Relacionales", "Temporales", "Agregacion"):
            values = domain.get(bucket, [])
            if not values:
                continue
            lines.extend(["", f"### {field_label(bucket)}"])
            lines.append("| ID | Pregunta |")
            lines.append("| --- | --- |")
            for item_value in values:
                if isinstance(item_value, dict):
                    lines.append(
                        f"| {escape_markdown_table_cell(item_value.get('ID', ''))} | {escape_markdown_table_cell(item_value.get('Q', ''))} |"
                    )
    return "\n".join(lines).strip() + "\n"


def count_nested_items(node):
    if isinstance(node, list):
        return len(node)
    if isinstance(node, dict):
        total = 0
        for value in node.values():
            if isinstance(value, list):
                total += len(value)
            elif isinstance(value, dict):
                total += count_nested_items(value)
        return total
    return 0


def render_omega_body(title, item, data):
    lines = [f"# {title}", "", "## Alcance", item["scope_statement"], "", "## Resumen"]
    meta = data.get("_meta", {})
    if meta:
        if meta.get("type"):
            lines.append(f"- Tipo: {meta['type']}")
        if meta.get("schema"):
            lines.append(f"- Esquema: {meta['schema']}")
        based_on = meta.get("based_on", [])
        if based_on:
            lines.append(f"- Basado en: {len(based_on)} artefactos")
    if data.get("omega_objects"):
        lines.append(f"- Objetos Ω: {len(data['omega_objects'])}")

    for obj in data.get("omega_objects", []):
        if not isinstance(obj, dict):
            continue
        obj_id = obj.get("id", "Ω-Object")
        obj_type = obj.get("type", "")
        lines.extend(["", f"## {obj_id}", f"- Tipo: {obj_type}" if obj_type else "- Tipo: objeto"])
        if obj.get("description"):
            lines.append(f"- Descripción: {obj['description']}")

        section_map = {
            "subtypes": "Subtipos",
            "fiber_proyectos": "Fibras proyectos",
            "fiber_programas": "Fibras programas",
            "systems": "Sistemas",
            "autoridades_gore": "Autoridades GORE",
            "divisiones_gore": "Divisiones GORE",
            "instancias_colegiadas": "Instancias colegiadas",
            "organismos_externos": "Organismos externos",
            "ejecutores": "Ejecutores",
            "roles_operativos": "Roles operativos",
            "instances": "Instancias",
        }
        for key, label in section_map.items():
            value = obj.get(key)
            if not value:
                continue
            if isinstance(value, list):
                lines.append(f"- {label}: {len(value)}")
                for row in value[:5]:
                    if isinstance(row, dict):
                        rid = row.get("id", "")
                        name = row.get("name") or row.get("role") or row.get("description") or ""
                        lines.append(f"  - `{rid}` {name}".rstrip())
                    else:
                        lines.append(f"  - {normalize_scalar(row)}")
            elif isinstance(value, dict):
                lines.append(f"- {label}: {len(value)}")
                for subkey, subvalue in list(value.items())[:5]:
                    if isinstance(subvalue, dict):
                        name = subvalue.get("name") or subvalue.get("source") or subvalue.get("description") or ""
                        lines.append(f"  - `{subkey}` {name}".rstrip())
                    else:
                        lines.append(f"  - `{subkey}` {normalize_scalar(subvalue)}")

    body = "\n".join(lines)
    body = body.replace("### Id", "### Identificador")
    body = body.replace("### Type", "### Tipo")
    body = body.replace("### Schema", "### Esquema")
    body = body.replace("## Omega objects", "## Objetos Ω")
    body = body.replace("## Omega processes", "## Procesos Ω")
    body = body.replace("## Omega coalgebra", "## Coalgebra Ω")
    return body.strip() + "\n"


def unwrap_single_semantic_root(data):
    if isinstance(data, dict):
        keys = [key for key in data.keys() if key != "_manifest"]
        if len(keys) == 1 and isinstance(data[keys[0]], dict):
            return data[keys[0]]
    return data


def table_ir_from_columns_rows(title, node):
    raw_headers = node.get("Columns") if "Columns" in node else node.get("Headers", [])
    headers = [normalize_scalar(item) for item in raw_headers]
    rows = []
    for row in node.get("Rows", []):
        if not isinstance(row, list):
            continue
        rows.append([normalize_scalar(item) for item in row])
    return TableIR(title=english_to_spanish_scaffold(title), headers=headers, rows=rows)


def table_ir_from_dict_list(title, items):
    headers = [normalize_scalar(header) for header in dict_list_headers(items)]
    rows = []
    for item in items:
        rows.append([normalize_scalar(item.get(header, "")) for header in headers])
    return TableIR(title=english_to_spanish_scaffold(title), headers=headers, rows=rows)


def scalar_reference_list(title, value, urn_alias_map, external_labels, urn_title_map):
    candidates = list(iter_reference_candidates(value))
    refs = []
    for candidate in candidates:
        ref = source_text_to_reference(candidate, urn_alias_map, external_labels, urn_title_map)
        if ref:
            refs.append(ref)
    if not refs:
        return None
    return ReferenceListBlock(title=english_to_spanish_scaffold(title), items=refs)


def iter_reference_candidates(value):
    if isinstance(value, dict):
        for child in value.values():
            yield from iter_reference_candidates(child)
        return
    if isinstance(value, list):
        for child in value:
            yield from iter_reference_candidates(child)
        return
    if value is not None:
        yield value


def generic_blocks_from_mapping(mapping, urn_alias_map, external_labels, urn_title_map):
    blocks = []
    for key, value in mapping.items():
        if key in KODA_BODY_EXCLUDED_KEYS:
            continue
        if key in TITLE_LIKE_KEYS and isinstance(value, str):
            continue
        label = english_to_spanish_scaffold(field_label(key))
        if key in {"Src", "Ref", "Ctx_Required", "Ctx_Optional", "Source", "Ref_Fuente"} or label in {"Fuentes", "Referencias", "Contexto requerido", "Contexto opcional", "Fuente"}:
            ref_block = scalar_reference_list(label, value, urn_alias_map, external_labels, urn_title_map)
            if ref_block:
                blocks.append(ref_block)
            continue
        if key in {"Content", "Contenido"}:
            text = inline_text_from_value(value, urn_alias_map, external_labels, urn_title_map)
            if text:
                blocks.append(ParagraphBlock(text))
            continue
        if is_columns_rows_table(value) or is_headers_rows_table(value):
            blocks.append(table_ir_from_columns_rows(label, value))
            continue
        if isinstance(value, list) and is_table_candidate(value):
            if label in {"Fuentes", "Referencias"}:
                ref_block = scalar_reference_list(label, value, urn_alias_map, external_labels, urn_title_map)
                if ref_block:
                    blocks.append(ref_block)
                continue
            blocks.append(table_ir_from_dict_list(label, value))
            continue
        if isinstance(value, list) and all(not isinstance(item, (dict, list)) for item in value):
            blocks.append(BulletListBlock(title=label, items=[normalize_scalar(item) for item in value]))
            continue
        if isinstance(value, dict):
            content_blocks = content_blocks_from_mapping(value, urn_alias_map, external_labels, urn_title_map)
            if content_blocks:
                if label == "Contenido":
                    blocks.extend(content_blocks)
                else:
                    blocks.append(SectionIR(title=section_title_from_mapping(label, value), blocks=content_blocks))
                continue
            section = SectionIR(
                title=section_title_from_mapping(label, value),
                blocks=generic_blocks_from_mapping(strip_title_like_fields(value), urn_alias_map, external_labels, urn_title_map),
            )
            if section.blocks:
                blocks.append(section)
            continue
        if isinstance(value, list):
            child_section = SectionIR(title=label)
            for index, item in enumerate(value, start=1):
                if isinstance(item, dict):
                    content_blocks = content_blocks_from_mapping(item, urn_alias_map, external_labels, urn_title_map)
                    child_title = item.get("titulo") or item.get("Title") or item.get("Titulo") or item.get("nombre") or item.get("Nombre") or f"Elemento {index}"
                    child_blocks = content_blocks or generic_blocks_from_mapping(strip_title_like_fields(item), urn_alias_map, external_labels, urn_title_map)
                    child_section.blocks.append(SectionIR(title=english_to_spanish_scaffold(headingify(str(child_title))), blocks=child_blocks))
                else:
                    child_section.blocks.append(BulletListBlock(items=[normalize_scalar(item)]))
            if child_section.blocks:
                blocks.append(child_section)
            continue
        blocks.append(SectionIR(title=label, blocks=[ParagraphBlock(normalize_scalar(value))]))
    return blocks


def build_generic_document_ir(title, item, primary_projection, urn_alias_map, external_labels, urn_title_map):
    data = unwrap_single_semantic_root(primary_projection["data"])
    sections = []
    if isinstance(data, dict):
        for key, value in data.items():
            if key in KODA_BODY_EXCLUDED_KEYS:
                continue
            section_title = section_title_from_mapping(english_to_spanish_scaffold(field_label(key)), value if isinstance(value, dict) else None)
            if isinstance(value, dict):
                content_blocks = content_blocks_from_mapping(value, urn_alias_map, external_labels, urn_title_map)
                blocks = content_blocks or generic_blocks_from_mapping(strip_title_like_fields(value), urn_alias_map, external_labels, urn_title_map)
            else:
                blocks = generic_blocks_from_mapping({key: value}, urn_alias_map, external_labels, urn_title_map)
                if len(blocks) == 1 and isinstance(blocks[0], SectionIR) and blocks[0].title == section_title:
                    sections.append(blocks[0])
                    continue
            sections.append(SectionIR(title=section_title, blocks=blocks))
    else:
        sections.append(SectionIR(title="Contenido", blocks=[ParagraphBlock(normalize_scalar(data))]))
    return DocumentIR(
        title=title,
        family=item.get("document_family", "generic"),
        publication_class=item.get("publication_class", KNOWLEDGE_PUBLICATION_CLASS),
        sections=[section for section in sections if section.blocks],
    )


def make_normative_item_section(item_name, node, urn_alias_map, external_labels, urn_title_map):
    title = headingify(item_name.replace("_", " "))
    if isinstance(node, dict) and node.get("Asunto"):
        title = f"{title} - {normalize_scalar(node['Asunto'])}"
    elif re.fullmatch(r"(?:Glosa|Articulo|Artículo|Programa|Capitulo|Capítulo)\s+\d+", title):
        derived_subject = derive_normative_subject(node, urn_alias_map, external_labels, urn_title_map)
        if derived_subject:
            title = f"{title} - {derived_subject}"
    section = SectionIR(title=title)
    if not isinstance(node, dict):
        section.blocks.append(ParagraphBlock(normalize_scalar(node)))
        return section

    if node.get("Asunto"):
        section.blocks.append(ParagraphBlock(normalize_scalar(node["Asunto"])))
    if node.get("Purp"):
        section.blocks.append(ParagraphBlock(normalize_scalar(node["Purp"])))
    if node.get("Unidad_Monetaria"):
        section.blocks.append(BulletListBlock(title="Datos clave", items=[f"Unidad monetaria: {normalize_scalar(node['Unidad_Monetaria'])}"]))

    for key, value in node.items():
        if key in {"ID", "Asunto", "Purp", "Src", "Unidad_Monetaria"}:
            continue
        label = english_to_spanish_scaffold(field_label(key))
        if is_columns_rows_table(value) or is_headers_rows_table(value):
            section.blocks.append(table_ir_from_columns_rows(label, value))
        elif key in {"Content", "Contenido"}:
            text = inline_text_from_value(value, urn_alias_map, external_labels, urn_title_map)
            if text:
                section.blocks.append(ParagraphBlock(text))
        elif isinstance(value, dict) and "Content" in value and isinstance(value["Content"], str):
            child_blocks = [ParagraphBlock(normalize_scalar(value["Content"]))]
            refs = scalar_reference_list("Referencias", value.get("Src"), urn_alias_map, external_labels, urn_title_map)
            if refs:
                child_blocks.append(refs)
            section.blocks.append(SectionIR(title=label, blocks=child_blocks))
        elif isinstance(value, list) and is_table_candidate(value):
            section.blocks.append(table_ir_from_dict_list(label, value))
        elif isinstance(value, list) and all(not isinstance(item, (dict, list)) for item in value):
            section.blocks.append(BulletListBlock(title=label, items=[normalize_scalar(item) for item in value]))
        elif isinstance(value, list):
            text = inline_text_from_value(value, urn_alias_map, external_labels, urn_title_map)
            if text:
                if label == "Contenido":
                    section.blocks.append(ParagraphBlock(text))
                else:
                    section.blocks.append(SectionIR(title=label, blocks=[ParagraphBlock(text)]))
        elif isinstance(value, dict):
            content_blocks = content_blocks_from_mapping(value, urn_alias_map, external_labels, urn_title_map)
            if content_blocks:
                if label == "Contenido":
                    section.blocks.extend(content_blocks)
                else:
                    section.blocks.append(SectionIR(title=section_title_from_mapping(label, value), blocks=content_blocks))
                continue
            child = SectionIR(
                title=section_title_from_mapping(label, value),
                blocks=generic_blocks_from_mapping(strip_title_like_fields(value), urn_alias_map, external_labels, urn_title_map),
            )
            if child.blocks:
                section.blocks.append(child)
        else:
            section.blocks.append(SectionIR(title=label, blocks=[ParagraphBlock(normalize_scalar(value))]))

    refs = scalar_reference_list("Referencias", node.get("Src"), urn_alias_map, external_labels, urn_title_map)
    if refs:
        section.blocks.append(refs)
    return section


def build_normative_document_ir(title, item, primary_projection, urn_alias_map, external_labels, urn_title_map):
    data = unwrap_single_semantic_root(primary_projection["data"])
    document = DocumentIR(
        title=title,
        family="normative",
        publication_class=item.get("publication_class", KNOWLEDGE_PUBLICATION_CLASS),
    )
    if not isinstance(data, dict):
        document.sections.append(SectionIR(title="Contenido", blocks=[ParagraphBlock(normalize_scalar(data))]))
        return document

    summary = SectionIR(title="Resumen")
    if data.get("Purp"):
        summary.blocks.append(ParagraphBlock(normalize_scalar(data["Purp"])))
    summary_items = []
    if data.get("Unidad_Monetaria"):
        summary_items.append(f"Unidad monetaria: {normalize_scalar(data['Unidad_Monetaria'])}")
    if summary_items:
        summary.blocks.append(BulletListBlock(title="Datos clave", items=summary_items))
    if isinstance(data.get("Ley"), dict):
        ley = data["Ley"]
        ley_items = []
        for key in ("Numero", "Titulo"):
            if ley.get(key):
                ley_items.append(f"{english_to_spanish_scaffold(field_label(key))}: {normalize_scalar(ley[key])}")
        if ley_items:
            summary.blocks.append(BulletListBlock(title="Ley", items=ley_items))
    if isinstance(data.get("Definiciones_Reutilizables"), list) and data["Definiciones_Reutilizables"]:
        rows = []
        for item_value in data["Definiciones_Reutilizables"]:
            if isinstance(item_value, dict):
                rows.append([normalize_scalar(item_value.get("ID", "")), normalize_scalar(item_value.get("Def", ""))])
        if rows:
            summary.blocks.append(TableIR(title="Definiciones reutilizables", headers=["ID", "Definición"], rows=rows))
    for key in [key for key in data.keys() if key.startswith("Resumen")]:
        value = data[key]
        if isinstance(value, dict):
            for child_key, child_value in value.items():
                if child_key == "ID":
                    continue
                label = english_to_spanish_scaffold(field_label(child_key))
                if is_columns_rows_table(child_value) or is_headers_rows_table(child_value):
                    summary.blocks.append(table_ir_from_columns_rows(label, child_value))
                elif isinstance(child_value, str):
                    summary.blocks.append(SectionIR(title=label, blocks=[ParagraphBlock(normalize_scalar(child_value))]))
                else:
                    child_section = SectionIR(title=label, blocks=generic_blocks_from_mapping({child_key: child_value}, urn_alias_map, external_labels, urn_title_map))
                    if child_section.blocks:
                        summary.blocks.append(child_section)
    if summary.blocks:
        document.sections.append(summary)

    for container_name in ("Glosas", "Articulos", "Programas", "Capitulos"):
        container = data.get(container_name)
        if isinstance(container, dict):
            for item_name, item_value in container.items():
                document.sections.append(make_normative_item_section(item_name, item_value, urn_alias_map, external_labels, urn_title_map))

    for key, value in data.items():
        if key in {"ID", "Purp", "Unidad_Monetaria", "Ley", "Definiciones_Reutilizables", "Preambulo", "Glosas", "Articulos", "Programas", "Capitulos"} or key.startswith("Resumen"):
            continue
        section = make_normative_item_section(key, value, urn_alias_map, external_labels, urn_title_map)
        if section.blocks:
            document.sections.append(section)

    if isinstance(data.get("Preambulo"), dict) and data["Preambulo"].get("Contenido"):
        document.sections.insert(
            1 if document.sections else 0,
            SectionIR(title="Preámbulo", blocks=[ParagraphBlock(normalize_scalar(data["Preambulo"]["Contenido"]))]),
        )
    return document


def normalize_term_name(name):
    return re.sub(r"\s+", " ", str(name).strip())


def normalized_definition_signature(text):
    tokens = re.findall(r"[a-záéíóúñ0-9]+", str(text).casefold())
    return {token for token in tokens if len(token) > 2}


def definitions_are_equivalent(left, right):
    left_tokens = normalized_definition_signature(left)
    right_tokens = normalized_definition_signature(right)
    if not left_tokens or not right_tokens:
        return normalize_scalar(left).strip().casefold() == normalize_scalar(right).strip().casefold()
    return len(left_tokens & right_tokens) / max(len(left_tokens | right_tokens), 1) >= 0.5


def pick_preferred_term_name(names):
    unique = sorted(dict.fromkeys(names), key=lambda item: (0 if re.fullmatch(r"[A-Z0-9%/\-]+", item) else 1, len(item), item.casefold()))
    return unique[0] if unique else ""


def summarize_subject(text, max_words=10):
    cleaned = re.sub(r"\s+", " ", normalize_scalar(text)).strip(" .;:")
    if not cleaned:
        return ""
    first_clause = re.split(r"[.;:]", cleaned, maxsplit=1)[0].strip()
    words = first_clause.split()
    if len(words) <= max_words:
        return first_clause
    return " ".join(words[:max_words]).strip(" ,.;:")


def derive_normative_subject(node, urn_alias_map, external_labels, urn_title_map):
    if not isinstance(node, dict):
        return ""
    for key in ("Asunto", "Titulo", "Title", "Purp"):
        value = node.get(key)
        if isinstance(value, str) and value.strip():
            return summarize_subject(value)
    for key in ("Content", "Contenido", "Def", "Desc"):
        if key in node:
            text = inline_text_from_value(node.get(key), urn_alias_map, external_labels, urn_title_map)
            if text:
                return summarize_subject(text)
    for value in node.values():
        if isinstance(value, dict):
            for key in ("Content", "Contenido", "Def", "Desc"):
                if key in value:
                    text = inline_text_from_value(value.get(key), urn_alias_map, external_labels, urn_title_map)
                    if text:
                        return summarize_subject(text)
    return ""


def build_glossary_document_ir(title, item, primary_projection, urn_alias_map, external_labels, urn_title_map):
    data = unwrap_single_semantic_root(primary_projection["data"])
    terms = data.get("terminos") if isinstance(data, dict) else None
    if not isinstance(terms, list):
        return build_generic_document_ir(title, item, primary_projection, urn_alias_map, external_labels, urn_title_map)

    resolutions = {
        normalize_term_name(name).casefold(): payload
        for name, payload in (item.get("glossary_conflict_resolutions") or {}).items()
        if isinstance(payload, dict)
    }
    defs_by_name = {}
    for term in terms:
        if not isinstance(term, dict):
            continue
        name = normalize_term_name(term.get("nombre", ""))
        definition = normalize_scalar(term.get("def", "")).strip()
        if not name:
            continue
        defs_by_name.setdefault(name.casefold(), {"display": name, "definitions": []})
        defs_by_name[name.casefold()]["definitions"].append(definition)

    conflicts = 0
    groups_by_def = {}
    for normalized_name, payload in defs_by_name.items():
        definitions = [item for item in payload["definitions"] if item]
        if not definitions:
            continue
        resolution = resolutions.get(normalized_name)
        if resolution:
            canonical_definition = normalize_scalar(resolution.get("definition") or max(definitions, key=len)).strip()
            canonical_name = normalize_term_name(resolution.get("canonical_name") or payload["display"])
            aliases = [normalize_term_name(alias) for alias in resolution.get("aliases", []) if normalize_term_name(alias)]
            merged_names = [canonical_name, *aliases]
        else:
            canonical_definition = max(definitions, key=len)
            if any(not definitions_are_equivalent(canonical_definition, other) for other in definitions):
                conflicts += 1
            merged_names = [payload["display"]]
        groups_by_def.setdefault(canonical_definition, []).extend(merged_names)

    rows = []
    for definition, names in groups_by_def.items():
        preferred = pick_preferred_term_name(names)
        aliases = [name for name in dict.fromkeys(names) if name != preferred]
        row = {
            "término": preferred,
            "definición": definition,
            "aliases": ", ".join(aliases),
        }
        rows.append(row)
    rows.sort(key=lambda row: (row["término"][:1].casefold(), row["término"].casefold()))

    document = DocumentIR(
        title=title,
        family="glossary",
        publication_class=item.get("publication_class", KNOWLEDGE_PUBLICATION_CLASS),
        metadata={"glossary_conflicts": conflicts},
    )
    summary = SectionIR(
        title="Resumen",
        blocks=[
            BulletListBlock(
                title="Estadísticas",
                items=[
                    f"Entradas fuente: {len(terms)}",
                    f"Entradas canónicas: {len(rows)}",
                    f"Conflictos léxicos: {conflicts}",
                ],
            )
        ],
    )
    document.sections.append(summary)

    for letter, bucket_rows in itertools.groupby(rows, key=lambda row: re.sub(r"[^A-Z0-9]", "", row["término"].upper()[:1]) or "#"):
        materialized_rows = list(bucket_rows)
        headers = ["término", "definición", "aliases"]
        section_rows = [[row.get(header, "") for header in headers] for row in materialized_rows]
        document.sections.append(SectionIR(title=f"Términos {letter}", blocks=[TableIR(headers=headers, rows=section_rows)]))
    return document


def inventory_subsections(key, node):
    title = normalize_scalar(node.get("Titulo") or node.get("Title") or headingify(key))
    section = SectionIR(title=title)
    if node.get("Def"):
        section.blocks.append(ParagraphBlock(normalize_scalar(node["Def"])))
    if node.get("Purp"):
        section.blocks.append(ParagraphBlock(normalize_scalar(node["Purp"])))
    artefactos = node.get("Artefactos")
    if isinstance(artefactos, list) and is_table_candidate(artefactos):
        section.blocks.append(table_ir_from_dict_list("Artefactos", artefactos))
    for child_key, child_value in node.items():
        if child_key in {"ID", "Titulo", "Title", "Def", "Purp", "Artefactos"}:
            continue
        if isinstance(child_value, dict):
            child_section = inventory_subsections(child_key, child_value)
            if child_section.blocks:
                section.blocks.append(child_section)
    return section


def build_inventory_document_ir(title, item, primary_projection, urn_alias_map, external_labels, urn_title_map):
    data = primary_projection["data"]
    document = DocumentIR(
        title=title,
        family="inventory",
        publication_class=item.get("publication_class", CONTROL_PUBLICATION_CLASS),
    )
    taxonomy = data.get("Taxonomia_Conocimiento", {}) if isinstance(data, dict) else {}
    if isinstance(taxonomy, dict):
        taxonomy_section = SectionIR(title="Taxonomía")
        if taxonomy.get("Purp"):
            taxonomy_section.blocks.append(ParagraphBlock(normalize_scalar(taxonomy["Purp"])))
        for key, value in taxonomy.items():
            if key in {"ID", "Purp"} or not isinstance(value, dict):
                continue
            area_items = [normalize_scalar(item) for item in value.get("Areas", []) if not isinstance(item, (dict, list))]
            child = SectionIR(title=normalize_scalar(value.get("Def") or headingify(key)))
            if area_items:
                child.blocks.append(BulletListBlock(title="Áreas", items=area_items))
            taxonomy_section.blocks.append(child)
        if taxonomy_section.blocks:
            document.sections.append(taxonomy_section)

    index = data.get("Indice_Artefactos", {}) if isinstance(data, dict) else {}
    if isinstance(index, dict):
        index_section = SectionIR(title="Índice de artefactos")
        for key, value in index.items():
            if key == "ID" or not isinstance(value, dict):
                continue
            area_section = inventory_subsections(key, value)
            if area_section.blocks:
                index_section.blocks.append(area_section)
        if index_section.blocks:
            document.sections.append(index_section)
    return document


def add_organigram_unit(unit_name, node, top_section, parent_title, urn_alias_map, external_labels, urn_title_map):
    title = headingify(unit_name.replace("_", " "))
    section = SectionIR(title=title)
    if parent_title:
        section.blocks.append(ReferenceListBlock(title="Depende de", items=[ReferenceIR(kind="internal", label=parent_title, target=parent_title)]))
    if not isinstance(node, dict):
        section.blocks.append(ParagraphBlock(normalize_scalar(node)))
        top_section.blocks.append(section)
        return

    if node.get("Def"):
        section.blocks.append(SectionIR(title="Definición", blocks=[ParagraphBlock(normalize_scalar(node["Def"]))]))
    if node.get("Purp"):
        section.blocks.append(SectionIR(title="Propósito", blocks=[ParagraphBlock(normalize_scalar(node["Purp"]))]))
    if node.get("Mssn"):
        section.blocks.append(SectionIR(title="Misión", blocks=[ParagraphBlock(normalize_scalar(node["Mssn"]))]))
    for key in ("Act", "Obj", "Req", "Ctx", "Res", "Relacion", "Mech"):
        value = node.get(key)
        if isinstance(value, list) and value:
            section.blocks.append(BulletListBlock(title=english_to_spanish_scaffold(field_label(key)), items=[normalize_scalar(item) for item in value]))
        elif isinstance(value, str):
            section.blocks.append(SectionIR(title=english_to_spanish_scaffold(field_label(key)), blocks=[ParagraphBlock(normalize_scalar(value))]))

    refs = scalar_reference_list("Referencias", node.get("Src"), urn_alias_map, external_labels, urn_title_map)
    if refs:
        section.blocks.append(refs)

    dependent_titles = []
    for relation_key in ("Unidades_Dependientes", "Componentes"):
        relation_value = node.get(relation_key)
        if isinstance(relation_value, dict):
            for child_name, child_node in relation_value.items():
                dependent_titles.append(headingify(child_name.replace("_", " ")))
                add_organigram_unit(child_name, child_node, top_section, title, urn_alias_map, external_labels, urn_title_map)
    if dependent_titles:
        section.blocks.append(
            ReferenceListBlock(
                title="Unidades dependientes",
                items=[ReferenceIR(kind="internal", label=child_title, target=child_title) for child_title in dependent_titles],
            )
        )
    top_section.blocks.append(section)


def build_organigram_document_ir(title, item, primary_projection, projections, urn_alias_map, external_labels, urn_title_map):
    data = unwrap_single_semantic_root(primary_projection["data"])
    document = DocumentIR(
        title=title,
        family="organigram",
        publication_class=item.get("publication_class", KNOWLEDGE_PUBLICATION_CLASS),
    )
    summary = SectionIR(title="Resumen")
    if isinstance(data, dict):
        if data.get("Purp"):
            summary.blocks.append(ParagraphBlock(normalize_scalar(data["Purp"])))
        if data.get("Ctx"):
            summary.blocks.append(BulletListBlock(title="Contexto", items=[normalize_scalar(item) for item in (data["Ctx"] if isinstance(data["Ctx"], list) else [data["Ctx"]])]))
    if summary.blocks:
        document.sections.append(summary)

    if not isinstance(data, dict):
        return document

    for top_key in ("Maxima_Autoridad", "Unidades_y_Organos", "Divisiones"):
        top_value = data.get(top_key)
        if not isinstance(top_value, dict):
            continue
        top_section = SectionIR(title=headingify(top_key.replace("_", " ")))
        for child_name, child_value in top_value.items():
            add_organigram_unit(child_name, child_value, top_section, None, urn_alias_map, external_labels, urn_title_map)
        if top_section.blocks:
            document.sections.append(top_section)

    secondary_sources = [path for path in projections.keys() if path != next(iter(projections.keys()))]
    ref_items = []
    for source_path in secondary_sources:
        ref = source_text_to_reference(source_path, urn_alias_map, external_labels, urn_title_map)
        if ref:
            ref_items.append(ref)
    if ref_items:
        document.sections[0].blocks.append(ReferenceListBlock(title="Referencias", items=ref_items))
    return document


def build_cq_catalog_document_ir(title, item, primary_projection):
    data = primary_projection["data"]
    stats = data.get("_manifest", {}).get("statistics", {}) if isinstance(data, dict) else {}
    document = DocumentIR(
        title=title,
        family="cq_catalog",
        publication_class=item.get("publication_class", KNOWLEDGE_PUBLICATION_CLASS),
    )
    domain_count = 0
    total_questions = 0
    bucket_totals = {"Existenciales": 0, "Relacionales": 0, "Temporales": 0, "Agregacion": 0}
    if isinstance(data, dict):
        for domain_key, domain in data.items():
            if not str(domain_key).startswith("Dom_") or not isinstance(domain, dict):
                continue
            domain_count += 1
            for bucket in bucket_totals:
                values = domain.get(bucket, [])
                if isinstance(values, list):
                    bucket_totals[bucket] += len(values)
                    total_questions += len(values)
    summary_items = []
    if "total_cqs" in stats:
        summary_items.append(f"Total de CQs: {stats['total_cqs']}")
    elif total_questions:
        summary_items.append(f"Total de CQs: {total_questions}")
    if "domains" in stats:
        summary_items.append(f"Dominios: {stats['domains']}")
    elif domain_count:
        summary_items.append(f"Dominios: {domain_count}")
    if isinstance(stats.get("types"), dict):
        for key, value in stats["types"].items():
            summary_items.append(f"{headingify(str(key))}: {value}")
    else:
        for key, value in bucket_totals.items():
            if value:
                summary_items.append(f"{field_label(key)}: {value}")
    summary_blocks = []
    if item.get("scope_statement"):
        summary_blocks.append(ParagraphBlock(normalize_scalar(item["scope_statement"])))
    if summary_items:
        summary_blocks.append(BulletListBlock(title="Estadísticas", items=summary_items))
    if not summary_blocks:
        summary_blocks.append(ParagraphBlock("Catálogo maestro de preguntas de competencia del dominio GN."))
    document.sections.append(SectionIR(title="Resumen", blocks=summary_blocks))

    if not isinstance(data, dict):
        return document

    for domain_key, domain in data.items():
        if not str(domain_key).startswith("Dom_") or not isinstance(domain, dict):
            continue
        section = SectionIR(title=headingify(domain_key.replace("Dom_", "").replace("_", " ")))
        for bucket in ("Existenciales", "Relacionales", "Temporales", "Agregacion"):
            values = domain.get(bucket, [])
            if not isinstance(values, list) or not values:
                continue
            rows = []
            for value in values:
                if isinstance(value, dict):
                    rows.append([normalize_scalar(value.get("ID", "")), normalize_scalar(value.get("Q", ""))])
            section.blocks.append(TableIR(title=english_to_spanish_scaffold(field_label(bucket)), headers=["ID", "Pregunta"], rows=rows))
        if section.blocks:
            document.sections.append(section)
    return document


def build_omega_document_ir(title, item, primary_projection, urn_alias_map, external_labels, urn_title_map):
    data = primary_projection["data"]
    raw_data = primary_projection.get("raw_data", data)
    meta = raw_data.get("_meta", {}) if isinstance(raw_data, dict) else {}
    document = DocumentIR(
        title=title,
        family="omega",
        publication_class=item.get("publication_class", KNOWLEDGE_PUBLICATION_CLASS),
    )
    summary_blocks = []
    if item.get("scope_statement"):
        summary_blocks.append(ParagraphBlock(normalize_scalar(item["scope_statement"])))
    if meta.get("description"):
        summary_blocks.append(ParagraphBlock(normalize_scalar(meta["description"])))
    summary_items = []
    if meta.get("type"):
        summary_items.append(f"Tipo: {normalize_scalar(meta['type'])}")
    if meta.get("date"):
        summary_items.append(f"Fecha: {normalize_scalar(meta['date'])}")
    if isinstance(data.get("omega_objects"), list):
        summary_items.append(f"Objetos Ω: {len(data['omega_objects'])}")
    if isinstance(data.get("omega_processes"), list):
        summary_items.append(f"Procesos Ω: {len(data['omega_processes'])}")
    if isinstance(data.get("omega_axioms"), list):
        summary_items.append(f"Axiomas Ω: {len(data['omega_axioms'])}")
    if summary_items:
        summary_blocks.append(BulletListBlock(title="Estadísticas", items=summary_items))
    based_on_refs = []
    for raw_ref in meta.get("based_on", []) if isinstance(meta.get("based_on"), list) else []:
        ref = source_text_to_reference(raw_ref, urn_alias_map, external_labels, urn_title_map)
        if ref:
            based_on_refs.append(ref)
    if based_on_refs:
        summary_blocks.append(ReferenceListBlock(title="Referencias", items=based_on_refs))
    if summary_blocks:
        document.sections.append(SectionIR(title="Resumen", blocks=summary_blocks))

    if isinstance(data.get("omega_objects"), list) and data["omega_objects"]:
        rows = []
        for obj in data["omega_objects"]:
            if not isinstance(obj, dict):
                continue
            rows.append(
                [
                    normalize_scalar(obj.get("id", "")),
                    normalize_scalar(obj.get("type", "")),
                    normalize_scalar(obj.get("description", "")),
                ]
            )
        if rows:
            document.sections.append(SectionIR(title="Objetos Ω", blocks=[TableIR(headers=["ID", "Tipo", "Descripción"], rows=rows)]))

    if isinstance(data.get("omega_processes"), list) and data["omega_processes"]:
        rows = []
        for proc in data["omega_processes"]:
            if not isinstance(proc, dict):
                continue
            rows.append(
                [
                    normalize_scalar(proc.get("id", "")),
                    normalize_scalar(proc.get("name", "")),
                    normalize_scalar(proc.get("type", "")),
                    normalize_scalar(proc.get("actor", "")),
                ]
            )
        if rows:
            document.sections.append(SectionIR(title="Procesos Ω", blocks=[TableIR(headers=["ID", "Nombre", "Tipo", "Actor"], rows=rows)]))

    coalgebra = data.get("omega_coalgebra") if isinstance(data, dict) else None
    if isinstance(coalgebra, dict):
        coalgebra_blocks = []
        if coalgebra.get("functor"):
            coalgebra_blocks.append(ParagraphBlock(f"Funtor: {normalize_scalar(coalgebra['functor'])}"))
        state_space = coalgebra.get("state_space")
        if isinstance(state_space, dict):
            rows = []
            for phase_name, states in state_space.items():
                if isinstance(states, list):
                    rows.append([headingify(str(phase_name).replace("_", " ")), ", ".join(normalize_scalar(state) for state in states)])
            if rows:
                coalgebra_blocks.append(TableIR(title="Espacio de estados", headers=["Fase", "Estados"], rows=rows))
        transitions = coalgebra.get("transitions")
        if isinstance(transitions, list):
            rows = []
            for transition in transitions:
                if not isinstance(transition, dict):
                    continue
                rows.append(
                    [
                        normalize_scalar(transition.get("from", "")),
                        normalize_scalar(transition.get("to", "")),
                        normalize_scalar(transition.get("event", "")),
                        normalize_scalar(transition.get("morphism", "")),
                    ]
                )
            if rows:
                coalgebra_blocks.append(TableIR(title="Transiciones", headers=["Desde", "Hacia", "Evento", "Morfismo"], rows=rows))
        if coalgebra_blocks:
            document.sections.append(SectionIR(title="Ciclo de vida Ω", blocks=coalgebra_blocks))

    if isinstance(data.get("omega_constructions"), list) and data["omega_constructions"]:
        rows = []
        for construction in data["omega_constructions"]:
            if not isinstance(construction, dict):
                continue
            rows.append(
                [
                    normalize_scalar(construction.get("id", "")),
                    normalize_scalar(construction.get("type", "")),
                    normalize_scalar(construction.get("name", "")),
                ]
            )
        if rows:
            document.sections.append(SectionIR(title="Construcciones Ω", blocks=[TableIR(headers=["ID", "Tipo", "Nombre"], rows=rows)]))

    if isinstance(data.get("omega_monads"), list) and data["omega_monads"]:
        rows = []
        for monad in data["omega_monads"]:
            if not isinstance(monad, dict):
                continue
            rows.append(
                [
                    normalize_scalar(monad.get("id", "")),
                    normalize_scalar(monad.get("name", "")),
                    normalize_scalar(monad.get("evaluator", "")),
                    normalize_scalar(monad.get("structure", "")),
                ]
            )
        if rows:
            document.sections.append(SectionIR(title="Mónadas Ω", blocks=[TableIR(headers=["ID", "Nombre", "Evaluador", "Estructura"], rows=rows)]))

    profunctor = data.get("omega_profunctor") if isinstance(data, dict) else None
    if isinstance(profunctor, dict):
        profunctor_blocks = []
        if profunctor.get("signature"):
            profunctor_blocks.append(ParagraphBlock(f"Signatura: {normalize_scalar(profunctor['signature'])}"))
        if profunctor.get("composition_law"):
            profunctor_blocks.append(ParagraphBlock(f"Ley de composición: {normalize_scalar(profunctor['composition_law'])}"))
        mappings = profunctor.get("mappings")
        if isinstance(mappings, list):
            rows = []
            for mapping in mappings:
                if not isinstance(mapping, dict):
                    continue
                gestion = mapping.get("gestion", {})
                rows.append(
                    [
                        normalize_scalar(mapping.get("selector", "")),
                        normalize_scalar(gestion.get("fase2", "")),
                        normalize_scalar(gestion.get("fase3", "")),
                        normalize_scalar(gestion.get("dictamen", "")),
                    ]
                )
            if rows:
                profunctor_blocks.append(TableIR(title="Mapeos", headers=["Selector", "Fase 2", "Fase 3", "Dictamen"], rows=rows))
        if profunctor_blocks:
            document.sections.append(SectionIR(title="Profuntor Ω", blocks=profunctor_blocks))

    if isinstance(data.get("omega_axioms"), list) and data["omega_axioms"]:
        rows = []
        for axiom in data["omega_axioms"]:
            if not isinstance(axiom, dict):
                continue
            rows.append([normalize_scalar(axiom.get("id", "")), normalize_scalar(axiom.get("statement", ""))])
        if rows:
            document.sections.append(SectionIR(title="Axiomas Ω", blocks=[TableIR(headers=["ID", "Enunciado"], rows=rows)]))
    return document


def build_document_ir(title, item, projections, urn_alias_map, external_labels, urn_title_map):
    document_family = item.get("document_family", "generic")
    primary_projection = next(iter(projections.values()))
    if document_family == "normative":
        return build_normative_document_ir(title, item, primary_projection, urn_alias_map, external_labels, urn_title_map)
    if document_family == "glossary":
        return build_glossary_document_ir(title, item, primary_projection, urn_alias_map, external_labels, urn_title_map)
    if document_family == "inventory":
        return build_inventory_document_ir(title, item, primary_projection, urn_alias_map, external_labels, urn_title_map)
    if document_family == "organigram":
        return build_organigram_document_ir(title, item, primary_projection, projections, urn_alias_map, external_labels, urn_title_map)
    if document_family == "cq_catalog":
        return build_cq_catalog_document_ir(title, item, primary_projection)
    if document_family == "omega":
        return build_omega_document_ir(title, item, primary_projection, urn_alias_map, external_labels, urn_title_map)
    return build_generic_document_ir(title, item, primary_projection, urn_alias_map, external_labels, urn_title_map)


def load_rebuild_map(map_path):
    data, err = load_yaml_safe(map_path)
    if err:
        raise SystemExit(f"Error cargando mapa GN: {err}")
    if not isinstance(data, dict):
        raise SystemExit("Mapa GN invalido")
    defaults = deepcopy(data.get("defaults", {}))
    defaults.setdefault("document_family", "generic")
    defaults.setdefault("publication_class", KNOWLEDGE_PUBLICATION_CLASS)
    normalized_entries = []
    for raw_entry in data.get("entries", []):
        entry = deepcopy(defaults)
        entry.update(raw_entry)
        entry["source_paths"] = [str(item).strip().strip("`") for item in entry.get("source_paths", [])]
        if "dependencies" in entry:
            entry["dependencies"] = [str(item).strip().strip("`") for item in entry.get("dependencies", [])]
        normalized_entries.append(entry)
    data["entries"] = normalized_entries
    data["exclusions"] = [str(item).strip().strip("`") for item in data.get("exclusions", [])]
    return data


def get_roots(repo_root, config):
    source_root = Path(config.get("source_root") or DEFAULT_SOURCE_ROOT)
    return {
        "repo_root": repo_root,
        "source_root": source_root,
        "inbox_root": repo_root / config.get("inbox_root", "inbox/gn"),
        "source_mirror_root": repo_root / config.get("source_mirror_root", "source/gn"),
        "draft_root": repo_root / config.get("draft_root", "drafts/gn"),
        "knowledge_root": repo_root / config.get("knowledge_root", "knowledge/gn"),
        "control_draft_root": repo_root / config.get("control_draft_root", str(DEFAULT_CONTROL_DRAFT_ROOT)),
        "control_root": repo_root / config.get("control_root", str(DEFAULT_CONTROL_ROOT)),
        "build_root": repo_root / "build" / "gn-rebuild",
    }


def ensure_dir(path):
    path.mkdir(parents=True, exist_ok=True)


def copy_tree(source_root, target_root):
    if target_root.exists():
        shutil.rmtree(target_root)
    ensure_dir(target_root.parent)
    shutil.copytree(source_root, target_root, dirs_exist_ok=False)


def write_yaml(path, data):
    ensure_dir(path.parent)
    with path.open("w", encoding="utf-8") as handle:
        yaml.safe_dump(data, handle, sort_keys=False, allow_unicode=True)


def read_source_lock(lock_path):
    doc, err = load_yaml_safe(lock_path)
    if err:
        raise SystemExit(f"Error leyendo source lock {lock_path}: {err}")
    return doc


def list_source_files(root):
    paths = []
    for current_root, _dirs, files in os.walk(root):
        for file_name in files:
            if file_name.startswith("."):
                continue
            paths.append(Path(current_root) / file_name)
    return sorted(paths)


def create_intake_artifact(intake_path, run_id, roots, map_path):
    payload = {
        "_manifest": {
            "urn": f"urn:gn:kb:rebuild-intake-{run_id}",
            "provenance": {
                "created_by": "gn_rebuild.py",
                "created_at": utc_today(),
                "source": str(roots["source_root"]),
            },
        },
        "version": "1.0.0",
        "status": "draft",
        "tags": ["gn", "rebuild", "intake"],
        "lang": "es",
        "extensions": {
            "gn": {
                "run_id": run_id,
                "map_path": str(map_path),
                "source_root": str(roots["source_root"]),
            }
        },
    }
    body = "\n".join(
        [
            f"# GN Rebuild Intake {run_id}",
            "",
            "## Fuente",
            f"- Root: `{roots['source_root']}`",
            f"- Mapa: `{map_path}`",
        ]
    )
    dump_yaml_frontmatter_and_body(intake_path, payload, body)


def freeze_source(args):
    repo_root = Path(args.repo_root).resolve()
    config = load_rebuild_map(Path(args.map_path).resolve())
    roots = get_roots(repo_root, config.get("config", {}))
    run_id = args.run_id or now_run_id()

    intake_path = roots["inbox_root"] / f"{run_id}.md"
    mirror_root = roots["source_mirror_root"] / run_id / "mirror"
    projections_root = roots["source_mirror_root"] / run_id / "projections"
    lock_path = roots["source_mirror_root"] / run_id / "source-lock.yml"

    ensure_dir(roots["inbox_root"])
    ensure_dir(roots["source_mirror_root"] / run_id)
    copy_tree(roots["source_root"], mirror_root)

    files_payload = []
    for source_file in list_source_files(mirror_root):
        rel = str(source_file.relative_to(mirror_root))
        projection = project_source(source_file, "auto")
        projection_path = projections_root / f"{rel}.json"
        ensure_dir(projection_path.parent)
        projection_payload = deepcopy(projection)
        projection_payload.pop("data", None)
        projection_payload.pop("raw_data", None)
        projection_payload["path"] = rel
        projection_payload["sha256"] = sha256_file(source_file)
        projection_path.write_text(
            json.dumps(projection_payload, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        files_payload.append(
            {
                "path": rel,
                "sha256": sha256_file(source_file),
                "projection": str(projection_path.relative_to(roots["source_mirror_root"] / run_id)),
            }
        )

    lock = {
        "run_id": run_id,
        "source_root": str(roots["source_root"]),
        "frozen_at": datetime.now(timezone.utc).isoformat(),
        "mirror_root": str(mirror_root.relative_to(repo_root)),
        "files": files_payload,
    }
    write_yaml(lock_path, lock)
    create_intake_artifact(intake_path, run_id, roots, Path(args.map_path).resolve())
    print(str(lock_path.relative_to(repo_root)))


def resolve_current_target_metadata(knowledge_root, target_rel_path):
    target_path = knowledge_root / target_rel_path
    if not target_path.exists():
        stem = Path(target_rel_path).stem
        return {
            "urn": f"urn:gn:kb:{stem}",
            "version": "1.0.0",
            "status": "draft",
            "tags": ["gn", "knowledge", stem],
            "lang": "es",
            "title": title_from_slug(stem),
        }
    frontmatter, body = load_markdown_parts(target_path)
    title = title_from_slug(Path(target_rel_path).stem)
    if body:
        for line in body.splitlines():
            if line.startswith("# "):
                title = line[2:].strip()
                break
    return {
        "urn": frontmatter.get("_manifest", {}).get("urn", f"urn:gn:kb:{Path(target_rel_path).stem}"),
        "version": frontmatter.get("version", "1.0.0"),
        "status": frontmatter.get("status", "draft"),
        "tags": frontmatter.get("tags", ["gn", "knowledge", Path(target_rel_path).stem]),
        "lang": frontmatter.get("lang", "es"),
        "title": title,
    }


def build_artifact(item, current_meta, mirrored_sources, source_hashes, run_id, urn_alias_map, external_labels, urn_title_map):
    transform_class = item["transform_class"]
    title = item.get("target_title") or current_meta["title"]
    projections = {}
    for source_path, source_file in mirrored_sources.items():
        projections[source_path] = project_source(
            source_file,
            item["source_type"],
            item.get("scope_statement"),
        )

    document_family = item.get("document_family", "generic")
    semantic_families = {"generic", "normative", "glossary", "inventory", "organigram", "cq_catalog", "omega"}
    document = None
    if document_family in semantic_families and transform_class != "index_only":
        document = build_document_ir(title, item, projections, urn_alias_map, external_labels, urn_title_map)
        body = render_document(document)
    elif transform_class == "index_only":
        body = render_index_body(title, item)
    else:
        if transform_class == "korafy_direct":
            body = render_direct_body(title, next(iter(projections.values())))
        elif transform_class == "korafy_koda_hybrid":
            body = render_koda_hybrid_body(title, next(iter(projections.values())))
        elif transform_class == "korafy_composite":
            body = render_composite_body(title, item, projections)
        elif transform_class == "derive_ttl_scope":
            body = render_ttl_body(title, item, next(iter(projections.values())))
        elif transform_class == "derive_csv_scope":
            body = render_csv_body(title, item, next(iter(projections.values())))
        else:
            raise ValueError(f"transform_class no soportada: {transform_class}")
    body = normalize_body_urns(body, urn_alias_map, external_labels, urn_title_map)
    body = normalize_editorial_phrasing(body)

    combined_facts = []
    skeleton_count = 0
    meat_count = 0
    fat_count = 0
    semantic_source_len = 0
    for projection in projections.values():
        skeleton_count += len(projection.get("skeleton", []))
        meat_count += projection.get("meat_count", 0)
        fat_count += projection.get("fat_count", 0)
        semantic_source_len += len("\n".join(projection["facts"]))

    if document is not None:
        combined_facts = document_facts(document)
        semantic_source_len = len("\n".join(combined_facts))
    else:
        for projection in projections.values():
            combined_facts.extend(projection["facts"])

    body_len = max(len(body), 1)
    source_len = max(semantic_source_len, 1)
    cr = round(source_len / body_len, 2)
    gn_ext = {
        "source_paths": list(item["source_paths"]),
        "source_hashes": source_hashes,
        "source_type": item["source_type"],
        "transformation_mode": transform_class,
        "fs": 100,
        "cr": cr,
        "run_id": run_id,
        "review_gate": item.get("review_gate", "auto"),
        "scope_statement": item.get("scope_statement"),
        "dependencies": item.get("dependencies", []),
        "expected_sections": item.get("expected_sections", []),
        "document_family": document_family,
        "publication_class": item.get("publication_class", KNOWLEDGE_PUBLICATION_CLASS),
        "skeleton_count": skeleton_count,
        "meat_count": meat_count,
        "fat_count": fat_count,
    }
    if document is not None and document_family == "glossary":
        gn_ext["glossary_conflicts"] = document.metadata.get("glossary_conflicts", 0)
    if cr < 1.5:
        gn_ext["cr_justification"] = "Fuente altamente estructurada o derivacion de alcance acotado."

    frontmatter = {
        "_manifest": {
            "urn": item.get("target_urn") or current_meta["urn"],
            "provenance": {
                "created_by": "gn_rebuild.py",
                "created_at": utc_today(),
                "source": "; ".join(item["source_paths"]),
            },
        },
        "version": current_meta["version"],
        "status": "draft",
        "tags": current_meta["tags"][:],
        "lang": current_meta["lang"],
        "extensions": {"gn": gn_ext},
    }
    if len(frontmatter["tags"]) < 3:
        frontmatter["tags"] = (frontmatter["tags"] + ["gn", "rebuild", Path(item["target_path"]).stem])[:3]

    return frontmatter, body, gn_ext, combined_facts


def locate_lock(roots, run_id):
    if run_id:
        lock_path = roots["source_mirror_root"] / run_id / "source-lock.yml"
        if not lock_path.exists():
            raise SystemExit(f"run_id desconocido: {run_id}")
        return lock_path
    candidates = sorted((roots["source_mirror_root"]).glob("*/source-lock.yml"))
    if not candidates:
        raise SystemExit("No hay source-locks. Ejecuta freeze-source primero.")
    return candidates[-1]


def evidence_relpath_for(target_path):
    return f"{target_path.replace('/', '__')}.json"


def validate_build_evidence(knowledge_draft_root, control_draft_root, evidence_root, expected_targets):
    failures = []
    warnings = []
    repo_root = knowledge_draft_root.parents[1]
    banned_fact_prefixes = (
        "LLM_Parsing_Instructions",
        "Format=",
        "Version=",
        "Status=",
        "Human-Creator=",
        "Human-Editor=",
        "Model-Collaborator=",
        "AI-Remediator=",
        "Creation-Date=",
        "Modification-Date=",
        "Primary-Source=",
    )

    for rel_path, meta in sorted(expected_targets.items()):
        draft_root = control_draft_root if meta.get("publication_class") == CONTROL_PUBLICATION_CLASS else knowledge_draft_root
        draft_path = draft_root / rel_path
        evidence_path = evidence_root / evidence_relpath_for(rel_path)
        if not evidence_path.exists():
            failures.append(f"evidence faltante: {evidence_path}")
            continue

        try:
            evidence = json.loads(evidence_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            failures.append(f"evidence invalida {evidence_path.name}: {exc}")
            continue

        if evidence.get("target_path") != rel_path:
            failures.append(f"evidence target_path inconsistente: {evidence_path.name}")

        if "target_urn" in evidence:
            failures.append(f"evidence expone target_urn publico antes de cutover: {evidence_path.name}")

        if evidence.get("catalog_state") != "draft_unindexed":
            failures.append(f"evidence catalog_state invalido en {evidence_path.name}")
        if evidence.get("document_family") != meta.get("document_family"):
            failures.append(f"evidence document_family inconsistente en {evidence_path.name}")
        if evidence.get("publication_class") != meta.get("publication_class"):
            failures.append(f"evidence publication_class inconsistente en {evidence_path.name}")
        if "autofix" not in evidence:
            failures.append(f"evidence autofix ausente en {evidence_path.name}")
        if "split" not in evidence:
            failures.append(f"evidence split ausente en {evidence_path.name}")

        for fact in evidence.get("preserved_facts", []):
            if isinstance(fact, str) and fact.startswith(banned_fact_prefixes):
                failures.append(f"evidence preserva residuo KODA tecnico en {evidence_path.name}: {fact}")
                break

        if not draft_path.exists():
            continue

        frontmatter, _body = load_markdown_parts(draft_path)
        draft_urn = None
        if isinstance(frontmatter, dict):
            draft_urn = frontmatter.get("_manifest", {}).get("urn")

        if evidence.get("draft_urn") != draft_urn:
            failures.append(f"evidence draft_urn inconsistente con draft en {evidence_path.name}")

        if meta.get("target_urn") and draft_urn != meta["target_urn"]:
            warnings.append(f"{rel_path}: draft_urn no alineada con target_urn esperada")

        split_meta = evidence.get("split", {}) if isinstance(evidence.get("split"), dict) else {}
        if split_meta.get("applied"):
            shard_paths = split_meta.get("shard_paths", [])
            if not shard_paths:
                failures.append(f"evidence split aplicado sin shard_paths en {evidence_path.name}")
            for shard_path in shard_paths:
                candidate = repo_root / shard_path
                if not candidate.exists():
                    failures.append(f"shard inexistente declarado en evidence {evidence_path.name}: {shard_path}")

    return {"failures": failures, "warnings": warnings}


def build(args):
    repo_root = Path(args.repo_root).resolve()
    map_doc = load_rebuild_map(Path(args.map_path).resolve())
    roots = get_roots(repo_root, map_doc.get("config", {}))
    lock_path = locate_lock(roots, args.run_id)
    lock = read_source_lock(lock_path)
    run_id = lock["run_id"]
    mirror_root = repo_root / lock["mirror_root"]
    draft_root = roots["draft_root"]
    if args.clean and draft_root.exists():
        shutil.rmtree(draft_root)
    ensure_dir(draft_root)
    if args.clean and roots["control_draft_root"].exists():
        shutil.rmtree(roots["control_draft_root"])
    ensure_dir(roots["control_draft_root"])

    evidence_root = roots["build_root"] / run_id / "evidence"
    ensure_dir(evidence_root)
    urn_alias_map, external_labels = build_urn_alias_maps(map_doc)
    urn_title_map = build_urn_title_map(map_doc, roots["knowledge_root"])

    for item in map_doc.get("entries", []):
        current_meta = resolve_current_target_metadata(roots["knowledge_root"], item["target_path"])
        mirrored_sources = {}
        source_hashes = {}
        for source_path in item["source_paths"]:
            full_path = mirror_root / source_path
            if not full_path.exists():
                raise SystemExit(f"fuente congelada faltante: {source_path}")
            mirrored_sources[source_path] = full_path
            source_hashes[source_path] = sha256_file(full_path)

        frontmatter, body, gn_ext, combined_facts = build_artifact(
            item,
            current_meta,
            mirrored_sources,
            source_hashes,
            run_id,
            urn_alias_map,
            external_labels,
            urn_title_map,
        )
        target_path = target_root_for_entry(roots, item) / item["target_path"]
        ensure_dir(target_path.parent)
        evidence_relpath = evidence_relpath_for(item["target_path"])
        gn_ext["evidence_path"] = f"build/gn-rebuild/{run_id}/evidence/{evidence_relpath}"
        write_report = dump_yaml_frontmatter_and_body(target_path, frontmatter, body)

        split_report = dict(write_report.get("split", {}))
        shard_paths = split_report.get("shard_paths", [])
        if shard_paths:
            normalized_paths = []
            for raw_path in shard_paths:
                raw = Path(raw_path)
                if raw.is_absolute():
                    try:
                        normalized_paths.append(str(raw.relative_to(repo_root)))
                    except ValueError:
                        normalized_paths.append(str(raw))
                else:
                    normalized_paths.append(str(raw))
            split_report["shard_paths"] = normalized_paths

        evidence_payload = {
            "target_path": item["target_path"],
            "draft_urn": frontmatter["_manifest"]["urn"],
            "catalog_state": "draft_unindexed",
            "run_id": run_id,
            "transform_class": item["transform_class"],
            "source_paths": item["source_paths"],
            "fs": gn_ext["fs"],
            "cr": gn_ext["cr"],
            "review_gate": gn_ext["review_gate"],
            "skeleton_count": gn_ext["skeleton_count"],
            "meat_count": gn_ext["meat_count"],
            "fat_count": gn_ext["fat_count"],
            "scope_statement": gn_ext.get("scope_statement"),
            "expected_sections": gn_ext.get("expected_sections", []),
            "document_family": gn_ext.get("document_family"),
            "publication_class": gn_ext.get("publication_class"),
            "autofix": write_report.get("autofix", {}),
            "split": split_report,
            "preserved_facts": combined_facts,
            "non_equivalence_decisions": item.get("non_equivalence_decisions", []),
        }
        if "glossary_conflicts" in gn_ext:
            evidence_payload["glossary_conflicts"] = gn_ext["glossary_conflicts"]
        evidence_path = evidence_root / evidence_relpath
        evidence_path.write_text(json.dumps(evidence_payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(str(draft_root.relative_to(repo_root)))


def validate(args):
    repo_root = Path(args.repo_root).resolve()
    map_doc = load_rebuild_map(Path(args.map_path).resolve())
    roots = get_roots(repo_root, map_doc.get("config", {}))
    lock_path = locate_lock(roots, args.run_id)
    lock = read_source_lock(lock_path)

    expected_targets = {entry["target_path"]: entry_expected_meta(entry) for entry in map_doc.get("entries", [])}
    knowledge_targets = {path: meta for path, meta in expected_targets.items() if meta.get("publication_class") != CONTROL_PUBLICATION_CLASS}
    control_targets = {path: meta for path, meta in expected_targets.items() if meta.get("publication_class") == CONTROL_PUBLICATION_CLASS}
    tree_result = validate_gn_tree(roots["draft_root"], expected_targets=knowledge_targets)
    if control_targets:
        control_result = validate_gn_tree(roots["control_draft_root"], expected_targets=control_targets)
        tree_result["failures"].extend(control_result["failures"])
        tree_result["warnings"].extend(control_result["warnings"])
    evidence_root = roots["build_root"] / lock["run_id"] / "evidence"
    evidence_result = validate_build_evidence(roots["draft_root"], roots["control_draft_root"], evidence_root, expected_targets)
    tree_result["failures"].extend(evidence_result["failures"])
    tree_result["warnings"].extend(evidence_result["warnings"])
    allowed_urns = collect_tree_manifest_urns(repo_root / "knowledge")
    allowed_urns.difference_update(collect_tree_manifest_urns(roots["knowledge_root"]))
    allowed_urns.update(meta.get("target_urn") for meta in expected_targets.values() if meta.get("target_urn"))
    fragment_catalog = collect_tree_fragments(repo_root / "knowledge")
    for urn in collect_tree_manifest_urns(roots["knowledge_root"]):
        fragment_catalog.pop(urn, None)
    fragment_catalog.update(collect_tree_fragments(roots["draft_root"]))
    if control_targets:
        fragment_catalog.update(collect_tree_fragments(roots["control_draft_root"]))
    tree_result["failures"].extend(validate_body_urn_resolution(roots["draft_root"], allowed_urns, fragment_catalog))
    if control_targets:
        tree_result["failures"].extend(validate_body_urn_resolution(roots["control_draft_root"], allowed_urns, fragment_catalog))

    lock_paths = {item["path"] for item in lock.get("files", [])}
    mapped_paths = {source_path for entry in map_doc.get("entries", []) for source_path in entry.get("source_paths", [])}
    exclusions = set(map_doc.get("exclusions", []))
    uncovered = sorted(path for path in mapped_paths if path not in lock_paths)
    if uncovered:
        tree_result["failures"].extend(f"source_path no congelado: {path}" for path in uncovered)

    unused_frozen = sorted(path for path in lock_paths if path not in mapped_paths and path not in exclusions)
    if args.strict_lock_coverage and unused_frozen:
        tree_result["failures"].extend(f"fuente congelada sin decision explicita: {path}" for path in unused_frozen)

    for failure in tree_result["failures"]:
        print(f"[FAIL] {failure}")
    for warning in tree_result["warnings"]:
        print(f"[WARN] {warning}")
    if tree_result["failures"]:
        raise SystemExit(1)
    print("GN validation passed.")


def validate_promoted_knowledge_tree(knowledge_root, expected_targets):
    tree_result = validate_gn_tree(knowledge_root, expected_targets=expected_targets)
    for failure in tree_result["failures"]:
        print(f"[FAIL] {failure}")
    for warning in tree_result["warnings"]:
        print(f"[WARN] {warning}")
    if tree_result["failures"]:
        raise SystemExit(1)
    print("GN promoted-tree validation passed.")


def structural_diff(knowledge_root, draft_root):
    current = sorted(str(path.relative_to(knowledge_root)) for path in knowledge_root.rglob("*.md"))
    staged = sorted(str(path.relative_to(draft_root)) for path in draft_root.rglob("*.md"))
    current_set = set(current)
    staged_set = set(staged)
    added = sorted(staged_set - current_set)
    removed = sorted(current_set - staged_set)
    changed = []
    for rel in sorted(current_set & staged_set):
        if (knowledge_root / rel).read_text(encoding="utf-8") != (draft_root / rel).read_text(encoding="utf-8"):
            changed.append(rel)
    return {"added": added, "removed": removed, "changed": changed}


def report(args):
    repo_root = Path(args.repo_root).resolve()
    map_doc = load_rebuild_map(Path(args.map_path).resolve())
    roots = get_roots(repo_root, map_doc.get("config", {}))
    lock_path = locate_lock(roots, args.run_id)
    lock = read_source_lock(lock_path)
    run_id = lock["run_id"]
    diff = structural_diff(roots["knowledge_root"], roots["draft_root"])
    control_diff = structural_diff(roots["control_root"], roots["control_draft_root"]) if roots["control_root"].exists() and roots["control_draft_root"].exists() else {"added": [], "removed": [], "changed": []}
    mapped_paths = {source_path for entry in map_doc.get("entries", []) for source_path in entry.get("source_paths", [])}
    lock_paths = {item["path"] for item in lock.get("files", [])}
    unused = sorted(path for path in lock_paths if path not in mapped_paths and path not in set(map_doc.get("exclusions", [])))
    pending_review = [entry["target_path"] for entry in map_doc.get("entries", []) if entry.get("review_gate") != "auto"]
    missing_targets = []
    for entry in map_doc.get("entries", []):
        target_root = target_root_for_entry(roots, entry)
        if not (target_root / entry["target_path"]).exists():
            missing_targets.append(entry["target_path"])
    non_equivalence = {
        entry["target_path"]: entry.get("non_equivalence_decisions", [])
        for entry in map_doc.get("entries", [])
        if entry.get("non_equivalence_decisions")
    }

    report_root = roots["build_root"] / run_id
    ensure_dir(report_root)
    report_path = report_root / "report.md"
    lines = [
        f"# GN Rebuild Report {run_id}",
        "",
        "## Boundary",
        "- build/ queda fuera de index, graph y health por diseno; su coherencia se gobierna por esta suite y por la semantica de evidence.",
        "- drafts/gn representa artefactos no promovidos; su evidencia usa catalog_state `draft_unindexed` hasta cutover.",
        "",
        "## Structural Diff",
        f"- Added: {len(diff['added'])}",
        f"- Removed: {len(diff['removed'])}",
        f"- Changed: {len(diff['changed'])}",
        "",
        "## Control Diff",
        f"- Added: {len(control_diff['added'])}",
        f"- Removed: {len(control_diff['removed'])}",
        f"- Changed: {len(control_diff['changed'])}",
        "",
        "## Review Gates",
    ]
    if pending_review:
        lines.extend(f"- {item}" for item in pending_review)
    else:
        lines.append("- none")
    lines.extend(["", "## Unused Frozen Sources"])
    if unused:
        lines.extend(f"- {item}" for item in unused[:200])
    else:
        lines.append("- none")
    lines.extend(["", "## Missing Targets"])
    if missing_targets:
        lines.extend(f"- {item}" for item in missing_targets)
    else:
        lines.append("- none")
    lines.extend(["", "## Intentional Non-Equivalence"])
    if non_equivalence:
        for target, items in non_equivalence.items():
            lines.append(f"- {target}: {'; '.join(items)}")
    else:
        lines.append("- none")
    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(str(report_path.relative_to(repo_root)))


def run_kora_command(repo_root, *args):
    command = [sys.executable, str(repo_root / "scripts" / "kora"), *args]
    return subprocess.run(command, cwd=str(repo_root), capture_output=True, text=True)


def cutover(args):
    repo_root = Path(args.repo_root).resolve()
    map_doc = load_rebuild_map(Path(args.map_path).resolve())
    roots = get_roots(repo_root, map_doc.get("config", {}))
    expected_targets = {entry["target_path"]: entry_expected_meta(entry) for entry in map_doc.get("entries", [])}
    knowledge_targets = {path: meta for path, meta in expected_targets.items() if meta.get("publication_class") != CONTROL_PUBLICATION_CLASS}

    validate(
        argparse.Namespace(
            repo_root=str(repo_root),
            map_path=args.map_path,
            run_id=args.run_id,
            strict_lock_coverage=args.strict_lock_coverage,
        )
    )

    pending_review = [entry["target_path"] for entry in map_doc.get("entries", []) if entry.get("review_gate") != "auto"]
    if pending_review:
        raise SystemExit(f"cutover bloqueado; review_gate pendiente: {', '.join(pending_review)}")

    if roots["knowledge_root"].exists():
        shutil.rmtree(roots["knowledge_root"])
    shutil.copytree(roots["draft_root"], roots["knowledge_root"])
    rewrite_tree_status(roots["knowledge_root"], "published")
    if roots["control_root"].exists():
        shutil.rmtree(roots["control_root"])
    if roots["control_draft_root"].exists():
        shutil.copytree(roots["control_draft_root"], roots["control_root"])
        rewrite_tree_status(roots["control_root"], "published")

    index_result = run_kora_command(repo_root, "index")
    if index_result.returncode != 0:
        raise SystemExit(index_result.stderr or index_result.stdout)
    health_result = run_kora_command(repo_root, "health", "--strict")
    if health_result.returncode != 0:
        raise SystemExit(health_result.stderr or health_result.stdout)
    validate_promoted_knowledge_tree(roots["knowledge_root"], knowledge_targets)
    print("cutover complete")


def make_parser():
    parser = argparse.ArgumentParser(description="GN rebuild pipeline")
    parser.add_argument("--repo-root", default=str(DEFAULT_REPO_ROOT), help="KORA repo root")
    parser.add_argument("--map-path", default=str(DEFAULT_MAP_PATH), help="GN rebuild map")

    subparsers = parser.add_subparsers(dest="command", required=True)

    p_freeze = subparsers.add_parser("freeze-source", help="Freeze external source tree")
    p_freeze.add_argument("--run-id", default=None, help="Optional explicit run id")
    p_freeze.set_defaults(func=freeze_source)

    p_build = subparsers.add_parser("build", help="Build drafts from frozen source")
    p_build.add_argument("--run-id", default=None, help="Run id to build")
    p_build.add_argument("--clean", action="store_true", help="Remove drafts/gn before build")
    p_build.set_defaults(func=build)

    p_validate = subparsers.add_parser("validate", help="Validate drafts/gn")
    p_validate.add_argument("--run-id", default=None, help="Run id to validate")
    p_validate.add_argument(
        "--strict-lock-coverage",
        action="store_true",
        help="Fail when a frozen source file lacks explicit decision in the map/exclusions",
    )
    p_validate.set_defaults(func=validate)

    p_report = subparsers.add_parser("report", help="Generate rebuild report")
    p_report.add_argument("--run-id", default=None, help="Run id to report")
    p_report.set_defaults(func=report)

    p_cutover = subparsers.add_parser("cutover", help="Promote drafts/gn to knowledge/gn")
    p_cutover.add_argument("--run-id", default=None, help="Run id to promote")
    p_cutover.add_argument(
        "--strict-lock-coverage",
        action="store_true",
        help="Require explicit decision for every frozen source file",
    )
    p_cutover.set_defaults(func=cutover)

    return parser


def main():
    parser = make_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
