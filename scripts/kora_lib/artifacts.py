import json
import re

import yaml


def dump_yaml_frontmatter_and_body(path, frontmatter, body):
    urn = frontmatter.get("_manifest", {}).get("urn", "") if isinstance(frontmatter, dict) else ""
    if isinstance(urn, str) and ":kb:" in urn:
        from .validation import auto_fix_published_kora_markdown_parts, lint_kora_markdown_parts

        body = auto_fix_published_kora_markdown_parts(frontmatter, body)
        failures = lint_kora_markdown_parts(frontmatter, body)
        if failures:
            joined = "; ".join(failures[:8])
            raise ValueError(f"KORA/MD blocked by lint: {joined}")

    content = "---\n"
    content += yaml.safe_dump(frontmatter, sort_keys=False, allow_unicode=True).strip()
    content += "\n---\n\n"
    content += body.rstrip() + "\n"
    path.write_text(content, encoding="utf-8")


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
