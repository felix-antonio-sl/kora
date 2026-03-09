import json
import re
from copy import deepcopy

import yaml


def dump_yaml_frontmatter_and_body(path, frontmatter, body):
    urn = frontmatter.get("_manifest", {}).get("urn", "") if isinstance(frontmatter, dict) else ""
    write_report = {
        "autofix": {"applied": False},
        "split": {"applied": False, "shard_count": 1, "shard_paths": [str(path)]},
    }

    if isinstance(urn, str) and ":kb:" in urn:
        from .validation import (
            auto_fix_published_kora_markdown_parts_with_report,
            lint_kora_markdown_parts,
            split_kora_markdown_parts,
        )

        body, autofix_report = auto_fix_published_kora_markdown_parts_with_report(frontmatter, body)
        write_report["autofix"] = autofix_report
        shard_bodies, split_report = split_kora_markdown_parts(frontmatter, body)
        write_report["split"] = split_report

        shard_paths = [path] + [path.with_name(f"{path.stem}--p{index:02d}{path.suffix}") for index in range(2, len(shard_bodies) + 1)]
        for stale in sorted(path.parent.glob(f"{path.stem}--p*{path.suffix}")):
            if stale not in shard_paths[1:]:
                stale.unlink()

        shard_urns = [urn] + [f"{urn}-p{index:02d}" for index in range(2, len(shard_bodies) + 1)]
        write_report["split"]["shard_paths"] = [str(item) for item in shard_paths]
        write_report["split"]["shard_urns"] = shard_urns

        for index, (shard_path, shard_body, shard_urn) in enumerate(zip(shard_paths, shard_bodies, shard_urns), start=1):
            shard_frontmatter = deepcopy(frontmatter)
            shard_frontmatter.setdefault("_manifest", {})["urn"] = shard_urn
            extensions = shard_frontmatter.setdefault("extensions", {})
            kora_ext = extensions.setdefault("kora", {})
            if isinstance(kora_ext, dict):
                kora_ext["shard_index"] = index
                kora_ext["shard_count"] = len(shard_bodies)
                kora_ext["shard_root_urn"] = urn

            failures = lint_kora_markdown_parts(shard_frontmatter, shard_body)
            if failures:
                joined = "; ".join(failures[:8])
                raise ValueError(f"KORA/MD blocked by lint: {joined}")

            content = "---\n"
            content += yaml.safe_dump(shard_frontmatter, sort_keys=False, allow_unicode=True).strip()
            content += "\n---\n\n"
            content += shard_body.rstrip() + "\n"
            shard_path.write_text(content, encoding="utf-8")
        return write_report

    content = "---\n"
    content += yaml.safe_dump(frontmatter, sort_keys=False, allow_unicode=True).strip()
    content += "\n---\n\n"
    content += body.rstrip() + "\n"
    path.write_text(content, encoding="utf-8")
    return write_report


def load_markdown_parts(path):
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", text, re.DOTALL)
    if not match:
        return None, text
    frontmatter = yaml.safe_load(match.group(1))
    body = match.group(2)
    return frontmatter, body


def load_yaml_safe(path):
    try:
        with open(path, "r", encoding="utf-8") as handle:
            content = handle.read()

        if path.suffix == ".json":
            return json.loads(content), None

        if path.suffix == ".md":
            match = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", content, re.DOTALL)
            if match:
                frontmatter, body = match.groups()
                doc = yaml.safe_load(frontmatter)
                if isinstance(doc, dict):
                    doc["_md_body"] = body.strip()
                return doc, None
            return None, "No YAML frontmatter found"

        try:
            return yaml.safe_load(content), None
        except yaml.composer.ComposerError:
            docs = list(yaml.safe_load_all(content))
            if docs:
                return docs[0], None
            return None, "Empty multi-document"
    except Exception as exc:
        return None, str(exc)


def get_artifact_title(doc, file_path):
    if not isinstance(doc, dict):
        return file_path.name

    body = doc.get("_md_body", "")
    if body:
        for line in body.split("\n"):
            line = line.strip()
            if line.startswith("# ") and not line.startswith("## "):
                return line[2:].strip()

    if "ID" in doc:
        return str(doc["ID"])

    try:
        return doc["agent_identity_and_global_configuration"][
            "primary_role_objective_and_audience"
        ]["role"]
    except (KeyError, TypeError):
        return file_path.name
