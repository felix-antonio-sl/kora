import json
from pathlib import Path

from .config import KNOWLEDGE_ROOT, KORA_ROOT, LEGACY_FXSL_SIGNALS


PROMOTED_FXSL_TARGETS = {}


def classify_fxsl_cat_file(path):
    stem = path.stem
    content = path.read_text(encoding="utf-8")
    promoted_targets = PROMOTED_FXSL_TARGETS.get(stem, [])
    legacy_signals = [signal for signal in LEGACY_FXSL_SIGNALS if signal.lower() in content.lower()]

    if promoted_targets:
        status = "promoted"
        reason = "Absorbido por la formal layer oficial via 08-fxsl-cat-bridge."
    elif legacy_signals:
        status = "legacy-noise"
        reason = "Contiene señales legacy o material desalineado con el régimen actual."
    else:
        status = "auxiliary"
        reason = "Permanece como apoyo conceptual no normativo."

    return {
        "file": str(path.relative_to(KORA_ROOT)),
        "stem": stem,
        "status": status,
        "canonical_targets": promoted_targets,
        "legacy_signals": legacy_signals,
        "reason": reason,
    }


def build_fxsl_cat_ledger():
    root = KNOWLEDGE_ROOT / "fxsl" / "cat"
    entries = [classify_fxsl_cat_file(path) for path in sorted(root.glob("*.md"))]
    counts = {}
    for item in entries:
        counts[item["status"]] = counts.get(item["status"], 0) + 1
    return {
        "meta": {
            "source_root": str(root.relative_to(KORA_ROOT)),
            "entry_count": len(entries),
        },
        "status_counts": dict(sorted(counts.items())),
        "entries": entries,
    }


def render_fxsl_cat_ledger_markdown(payload):
    lines = [
        "# FXSL/Cat Absorption Ledger",
        "",
        "Este documento es generado por `python3 toolchain/kora sync-docs`. Resume el estado institucional de `artifacts/knowledge/fxsl/cat`.",
        "",
        "## Resumen",
        "",
    ]
    for status, count in payload["status_counts"].items():
        lines.append(f"- {status}: {count}")
    lines.extend(
        [
            "",
            "## Entradas",
            "",
            "| Archivo | Estado | Targets canonicos | Motivo |",
            "|---------|--------|-------------------|--------|",
        ]
    )
    for entry in payload["entries"]:
        targets = ", ".join(entry["canonical_targets"]) if entry["canonical_targets"] else "-"
        lines.append(f"| {entry['file']} | {entry['status']} | {targets} | {entry['reason']} |")
    lines.append("")
    return "\n".join(lines)


def write_fxsl_cat_ledger_docs(output_dir):
    payload = build_fxsl_cat_ledger()
    json_path = output_dir / "fxsl-cat-ledger.json"
    md_path = output_dir / "fxsl-cat-ledger.md"
    json_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    md_path.write_text(render_fxsl_cat_ledger_markdown(payload), encoding="utf-8")
    return payload, json_path, md_path
