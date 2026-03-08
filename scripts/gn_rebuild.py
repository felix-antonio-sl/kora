#!/usr/bin/env python3
"""GN rebuild pipeline under KORA/MD v5."""

import argparse
import csv
import hashlib
import json
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
from kora_lib.gn_validation import validate_gn_tree


DEFAULT_REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MAP_PATH = DEFAULT_REPO_ROOT / "scripts" / "gn_rebuild_map.yml"
DEFAULT_SOURCE_ROOT = Path("/Users/felixsanhueza/Developer/gorenuble/knowledge")
TOP_LEVEL_KODA_TECHNICAL_KEYS = {
    "_manifest",
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
    "Primary-Source",
    "Authoritative-Source",
    "Source-Hierarchy",
    "Ref-STS-Guide",
    "Ctx",
    "LLM_Parsing_Instructions",
}
NESTED_KODA_TECHNICAL_KEYS = {
    "LLM_Parsing_Instructions",
}


def sha256_file(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


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


def normalize_scalar(value):
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    text = str(value)
    text = re.sub(r"(?m)^(#{1,6}\s)", r"\\\1", text)
    return text


def is_table_candidate(items):
    if not items or not all(isinstance(item, dict) for item in items):
        return False
    key_sets = [tuple(item.keys()) for item in items if item]
    return bool(key_sets) and all(keys == key_sets[0] for keys in key_sets)


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
        doc, err = load_yaml_safe(path)
        if err:
            raise ValueError(f"no fue posible parsear {path}: {err}")
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
    lines = []
    if isinstance(value, dict):
        for key, child in value.items():
            heading_level = min(level + 1, 4)
            lines.append(f"{'#' * heading_level} {headingify(str(key))}")
            lines.extend(render_markdown_value(child, heading_level))
    elif isinstance(value, list):
        if is_table_candidate(value):
            headers = list(value[0].keys())
            lines.append("| " + " | ".join(headers) + " |")
            lines.append("| " + " | ".join("---" for _ in headers) + " |")
            for item in value:
                lines.append("| " + " | ".join(normalize_scalar(item.get(header, "")) for header in headers) + " |")
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
            lines.append(f"## {headingify(str(key))}")
            lines.extend(render_markdown_value(data[key], 2))
            lines.append("")
    else:
        lines.append("## Contenido")
        lines.extend(render_markdown_value(data, 2))
    return "\n".join(line for line in lines if line is not None).strip() + "\n"


def strip_koda_technical_fields(node, depth=0):
    if isinstance(node, dict):
        cleaned = {}
        for key, value in node.items():
            if depth == 0 and key in TOP_LEVEL_KODA_TECHNICAL_KEYS:
                continue
            if depth > 0 and key in NESTED_KODA_TECHNICAL_KEYS:
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


def render_koda_hybrid_body(title, projection):
    data = strip_koda_technical_fields(projection["data"])
    embedded_body = find_embedded_markdown(data)
    if embedded_body:
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
    lines.extend(["", "## Fuente principal", f"- `{primary_source}`"])
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
        sample = projection["data"][: min(8, len(projection["data"]))]
        if sample:
            lines.append("- Muestra:")
            lines.extend(f"  - `{item}`" for item in sample)
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

        sample_rows = []
        for bucket in ("Existenciales", "Relacionales", "Temporales", "Agregacion"):
            values = domain.get(bucket, [])
            for item_value in values[:2]:
                if isinstance(item_value, dict):
                    sample_rows.append(
                        {
                            "Tipo": type_labels.get(bucket, bucket),
                            "ID": item_value.get("ID", ""),
                            "Pregunta": item_value.get("Q", ""),
                        }
                    )
        if sample_rows:
            lines.append("| Tipo | ID | Pregunta |")
            lines.append("| --- | --- | --- |")
            for row in sample_rows:
                lines.append(
                    f"| {normalize_scalar(row['Tipo'])} | {normalize_scalar(row['ID'])} | {normalize_scalar(row['Pregunta'])} |"
                )
    return "\n".join(lines).strip() + "\n"


def load_rebuild_map(map_path):
    data, err = load_yaml_safe(map_path)
    if err:
        raise SystemExit(f"Error cargando mapa GN: {err}")
    if not isinstance(data, dict):
        raise SystemExit("Mapa GN invalido")
    defaults = deepcopy(data.get("defaults", {}))
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


def build_artifact(item, current_meta, mirrored_sources, source_hashes, run_id):
    transform_class = item["transform_class"]
    title = item.get("target_title") or current_meta["title"]
    projections = {}
    for source_path, source_file in mirrored_sources.items():
        projections[source_path] = project_source(
            source_file,
            item["source_type"],
            item.get("scope_statement"),
        )

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
    elif transform_class == "index_only":
        body = render_index_body(title, item)
    else:
        raise ValueError(f"transform_class no soportada: {transform_class}")

    combined_facts = []
    skeleton_count = 0
    meat_count = 0
    fat_count = 0
    for projection in projections.values():
        combined_facts.extend(projection["facts"])
        skeleton_count += len(projection.get("skeleton", []))
        meat_count += projection.get("meat_count", 0)
        fat_count += projection.get("fat_count", 0)

    body_len = max(len(body), 1)
    source_len = sum(len(path.read_text(encoding="utf-8")) for path in mirrored_sources.values())
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
        "skeleton_count": skeleton_count,
        "meat_count": meat_count,
        "fat_count": fat_count,
    }
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

    evidence_root = roots["build_root"] / run_id / "evidence"
    ensure_dir(evidence_root)

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

        frontmatter, body, gn_ext, combined_facts = build_artifact(item, current_meta, mirrored_sources, source_hashes, run_id)
        target_path = draft_root / item["target_path"]
        ensure_dir(target_path.parent)
        evidence_relpath = f"{item['target_path'].replace('/', '__')}.json"
        gn_ext["evidence_path"] = f"build/gn-rebuild/{run_id}/evidence/{evidence_relpath}"
        dump_yaml_frontmatter_and_body(target_path, frontmatter, body)

        evidence_payload = {
            "target_path": item["target_path"],
            "target_urn": frontmatter["_manifest"]["urn"],
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
            "preserved_facts": combined_facts,
            "non_equivalence_decisions": item.get("non_equivalence_decisions", []),
        }
        evidence_path = evidence_root / evidence_relpath
        evidence_path.write_text(json.dumps(evidence_payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(str(draft_root.relative_to(repo_root)))


def validate(args):
    repo_root = Path(args.repo_root).resolve()
    map_doc = load_rebuild_map(Path(args.map_path).resolve())
    roots = get_roots(repo_root, map_doc.get("config", {}))
    lock_path = locate_lock(roots, args.run_id)
    lock = read_source_lock(lock_path)

    expected_targets = {
        entry["target_path"]: {"target_urn": entry.get("target_urn")}
        for entry in map_doc.get("entries", [])
    }
    tree_result = validate_gn_tree(roots["draft_root"], expected_targets=expected_targets)

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
    mapped_paths = {source_path for entry in map_doc.get("entries", []) for source_path in entry.get("source_paths", [])}
    lock_paths = {item["path"] for item in lock.get("files", [])}
    unused = sorted(path for path in lock_paths if path not in mapped_paths and path not in set(map_doc.get("exclusions", [])))
    pending_review = [entry["target_path"] for entry in map_doc.get("entries", []) if entry.get("review_gate") != "auto"]
    missing_targets = [entry["target_path"] for entry in map_doc.get("entries", []) if not (roots["draft_root"] / entry["target_path"]).exists()]
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
        "## Structural Diff",
        f"- Added: {len(diff['added'])}",
        f"- Removed: {len(diff['removed'])}",
        f"- Changed: {len(diff['changed'])}",
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

    index_result = run_kora_command(repo_root, "index")
    if index_result.returncode != 0:
        raise SystemExit(index_result.stderr or index_result.stdout)
    health_result = run_kora_command(repo_root, "health", "--strict")
    if health_result.returncode != 0:
        raise SystemExit(health_result.stderr or health_result.stdout)
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
