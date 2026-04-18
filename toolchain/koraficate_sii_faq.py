#!/usr/bin/env python3
"""
Koraficacion batch: SII FAQ -> KORA/MD

Lee questions.json del scrapper SII, agrupa por subcategoria (breadcrumbs L3),
convierte HTML->Markdown, aplica compresion mecanica y genera artefactos KORA/MD
en KNOWLEDGE/sii/kb/.

Uso:
    python3 scripts/koraficate_sii_faq.py [--dry-run] [--max-per-group N]
"""

import json
import re
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

from markdownify import markdownify as md

# -- Paths ------------------------------------------------------------------

KORA_ROOT = Path(__file__).resolve().parents[1]
SOURCE_PATH = KORA_ROOT / "artifacts" / "knowledge" / "_SCRIPTORIUM" / "INBOX" / "sii" / "questions.json"
OUTPUT_DIR = KORA_ROOT / "artifacts" / "knowledge" / "sii" / "kb"

# Importar toolchain KORA para escribir con lint+autofix+split
sys.path.insert(0, str(KORA_ROOT / "toolchain"))
from kora_lib.artifacts import dump_yaml_frontmatter_and_body

# -- Config ------------------------------------------------------------------

MAX_QUESTIONS_PER_ARTIFACT = 0  # 0 = sin split manual, dejar al toolchain (family faq: 50 sections, 800 lines)
CREATED_AT = "2026-03-23"
CREATED_BY = "kora/curator"
ARTIFACT_VERSION = "2.0.0"  # v2: telegrafización agresiva (léxica + legal + estructural)

# Frases introductorias tipo grasa
INTRO_FAT = re.compile(
    r"^(?:Respuesta:\s*|R:\s*|Resp\.:\s*)", re.IGNORECASE
)

# Boilerplate SII: frases genéricas de remisión al sitio web
SII_BOILERPLATE = re.compile(
    r"(?:Puede|Para)\s+(?:obtener|consultar|conocer|revisar|ver)\s+más\s+información"
    r"[^.]*(?:sitio\s+[Ww]eb\s+del\s+SII|www\.sii\.cl|sii\.cl)[^.]*\.\s*",
    re.IGNORECASE | re.DOTALL,
)

# Muletilla final tipo "Puede obtener más información relativa a este tema en..."
SII_BOILERPLATE_2 = re.compile(
    r"(?:Puede\s+obtener\s+más\s+información\s+relativa\s+a\s+este\s+tema\s+en\s+el\s+sitio\s+[Ww]eb\s+del\s+SII[^.]*\.?\s*)",
    re.IGNORECASE,
)

# Frase generica sin info util
SII_GENERIC_REFS = re.compile(
    r"(?:Puede\s+obtener\s+más\s+información[^.]*(?:en\s+el\s+sitio|menú|sección|opción)[^.]*\.?\s*)",
    re.IGNORECASE,
)


# ---------------------------------------------------------------------------
# CAPA 1: Grasa léxica — marcadores discursivos y muletillas (T4 md-spec)
# Cada tupla: (patrón, reemplazo)
# ---------------------------------------------------------------------------
LEXICO_RULES: list[tuple[re.Pattern, str]] = [
    # --- Marcadores discursivos puros (eliminar sin reemplazo) ---
    (re.compile(r"\b[Cc]abe (?:señalar|mencionar|destacar|indicar|precisar|agregar) que\s*,?\s*"), ""),
    (re.compile(r"\b[Ee]s importante (?:señalar|destacar|mencionar|indicar|tener en cuenta) que\s*,?\s*"), ""),
    (re.compile(r"\b[Ee]s necesario (?:señalar|precisar|tener en cuenta) que\s*,?\s*"), ""),
    (re.compile(r"\b[Hh]ay que tener (?:en cuenta|presente) que\s*,?\s*"), ""),
    (re.compile(r"\b[Ss]e debe tener presente que\s*,?\s*"), ""),
    (re.compile(r"\b[Ll]e recordamos que\s*,?\s*"), ""),
    (re.compile(r"\b[Aa] continuación\s*,?\s*"), ""),
    (re.compile(r"\b[Pp]or otro lado\s*,?\s*"), ""),
    (re.compile(r"\b[Ee]n este sentido\s*,?\s*"), ""),
    (re.compile(r"\b[Aa]simismo\s*,?\s*"), ""),
    (re.compile(r"\b[Aa]demás de lo anterior\s*,?\s*"), ""),
    (re.compile(r"\b[Ee]n relación (?:a|con) lo anterior\s*,?\s*"), ""),
    (re.compile(r"\b[Rr]especto de lo anterior\s*,?\s*"), ""),
    (re.compile(r"\b[Dd]e acuerdo (?:a|con) lo (?:señalado|anterior|indicado|expuesto)\s*,?\s*"), ""),
    (re.compile(r"\b[Tt]odo lo anterior\s*,?\s*"), ""),
    (re.compile(r"\b[Cc]omplementariamente\s*,?\s*"), ""),
    (re.compile(r"\b[Pp]or su parte\s*,?\s*"), ""),
    # --- Conectores lógicos eliminables cuando inician oración ---
    (re.compile(r"(?:^|\n)\s*[Ee]n consecuencia\s*,?\s*"), "\n"),
    (re.compile(r"(?:^|\n)\s*[Pp]or lo tanto\s*,?\s*"), "\n"),
    (re.compile(r"(?:^|\n)\s*[Pp]or consiguiente\s*,?\s*"), "\n"),
    (re.compile(r"(?:^|\n)\s*[Aa]dicionalmente\s*,?\s*"), "\n"),
    (re.compile(r"(?:^|\n)\s*[Ee]n primer lugar\s*,?\s*"), "\n"),
    (re.compile(r"(?:^|\n)\s*[Ee]n segundo lugar\s*,?\s*"), "\n"),
    (re.compile(r"(?:^|\n)\s*[Ff]inalmente\s*,?\s*"), "\n"),
    # --- Perífrasis legales comprimibles (T1: eliminar perífrasis) ---
    (re.compile(r"\bpara (?:estos|tales|dichos) efectos\s*,?\s*"), ""),
    (re.compile(r"\ben virtud de lo (?:dispuesto|establecido|señalado) en\b"), "según"),
    (re.compile(r"\bde conformidad (?:a|con) lo (?:dispuesto|establecido|señalado) en\b"), "según"),
    (re.compile(r"\bde acuerdo (?:a|con) lo (?:dispuesto|establecido) en\b"), "según"),
    (re.compile(r"\bconforme a lo (?:dispuesto|establecido|señalado) en\b"), "según"),
    (re.compile(r"\ben conformidad a las normas\b"), "según las normas"),
    (re.compile(r"\bcon el objeto de\b"), "para"),
    (re.compile(r"\bcon el fin de\b"), "para"),
    (re.compile(r"\ba objeto de\b"), "para"),
    (re.compile(r"\bcon la finalidad de\b"), "para"),
    (re.compile(r"\bse encuentran? (?:obligados?|afectos?|exentos?|sujetos?) a\b"), lambda m: m.group().replace("se encuentran ", "están ").replace("se encuentra ", "está ")),
    # --- Muletillas pronominales pesadas ---
    (re.compile(r"\b(?:el|la|los|las) (?:referidos?|mencionados?|señalados?|indicados?|citados?) (?:anteriormente|previamente|precedentemente)\b"), lambda m: m.group().split()[0] + " " + m.group().split()[1].replace("referidos", "referidos").replace("mencionados", "mencionados")),
    # --- Hedging eliminable ---
    (re.compile(r"\ben general\s*,?\s*", re.IGNORECASE), ""),
]


# ---------------------------------------------------------------------------
# CAPA 2: Compresión de prosa legal — sustituciones semánticas
# ---------------------------------------------------------------------------
LEGAL_COMPRESSIONS: list[tuple[re.Pattern, str]] = [
    # "deberá/deberán informar" → "Informe obligatorio" (T2: nominalizar)
    # Solo aplicable al inicio de oración — demasiado riesgoso en medio
    # En cambio, simplificar verbos modales pesados
    (re.compile(r"\bse (?:encontrará|encontrarán) (?:obligados?|afectos?) a\b"), "deberá"),
    (re.compile(r"\bno se encontrará obligado a\b"), "no deberá"),
    (re.compile(r"\bdeberá proceder a\b"), "deberá"),
    (re.compile(r"\bpodrá proceder a\b"), "podrá"),
    (re.compile(r"\bdebe proceder a\b"), "debe"),
    (re.compile(r"\bprocederá a\b"), ""),
    (re.compile(r"\btendrá(?:n)? (?:la )?obligación de\b"), "deberá"),
    (re.compile(r"\btendrá(?:n)? derecho a\b"), "podrá"),
    (re.compile(r"\bes(?:tá|tán) facultados? para\b"), "puede"),
    (re.compile(r"\bqueda(?:n)? facultados? para\b"), "puede"),
    # Simplificar referencias institucionales (case-insensitive donde aplica)
    (re.compile(r"\b[Ee]l Servicio de Impuestos Internos\b"), "el SII"),
    (re.compile(r"\b[Dd]el Servicio de Impuestos Internos\b"), "del SII"),
    (re.compile(r"\b[Aa]l Servicio de Impuestos Internos\b"), "al SII"),
    (re.compile(r"\bServicio de Impuestos Internos\b"), "SII"),
    (re.compile(r"\bLey [Ss]obre Impuesto a las Ventas y Servicios\b"), "LIVS"),
    (re.compile(r"\bLey [Ss]obre Impuesto a la Renta\b"), "LIR"),
    (re.compile(r"\bLey [Ss]obre Impuesto a las Herencias,? Asignaciones y Donaciones\b"), "Ley 16.271"),
    (re.compile(r"\bImpuesto al Valor Agregado\b"), "IVA"),
    (re.compile(r"\bImpuesto de Primera Categoría\b"), "IDPC"),
    (re.compile(r"\bImpuesto Global Complementario\b"), "IGC"),
    (re.compile(r"\bImpuesto Adicional\b"), "IA"),
    (re.compile(r"\bReglamento de la Ley [Ss]obre Impuestos? a las Ventas y Servicios\b"), "Reglamento LIVS"),
    (re.compile(r"\bCédula Nacional de Identidad\b"), "CI"),
    (re.compile(r"\bUnidades? Tributarias? (?:Mensual(?:es)?|Anual(?:es)?)\b"), lambda m: "UTM" if "ensual" in m.group() else "UTA"),
    (re.compile(r"\bDeclaración y Pago Simultáneo Mensual\b"), "F29"),
    (re.compile(r"\bFormulario 22 de Declaración de Renta\b"), "F22"),
]


# ---------------------------------------------------------------------------
# CAPA 3: Promoción estructural mecánica — detectar patrones en prosa
# ---------------------------------------------------------------------------
def promote_inline_enumerations(text: str) -> str:
    """Detectar enumeraciones a), b), c) o 1), 2), 3) en prosa y promover a lista."""
    # Patrón: texto con a) ... b) ... c) ... dentro de un párrafo
    def _promote_alpha(match):
        block = match.group(0)
        items = re.split(r"\s*[a-z]\)\s*", block)
        items = [item.strip().rstrip(";.,") for item in items if item.strip()]
        if len(items) < 2:
            return block
        result = "\n".join(f"- {item}" for item in items)
        return "\n" + result + "\n"

    # Solo promover si hay al menos 3 items a), b), c) en un bloque de prosa
    text = re.sub(
        r"(?:^|\n)([^\n]*?\ba\)\s+[^\n]*\bb\)\s+[^\n]*\bc\)\s+[^\n]*)",
        _promote_alpha,
        text,
        flags=re.MULTILINE,
    )
    return text

# -- Helpers -----------------------------------------------------------------


def slugify(text: str) -> str:
    slug = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    slug = slug.lower()
    slug = re.sub(r"[^a-z0-9\s-]", "", slug)
    slug = re.sub(r"\s+", "-", slug.strip())
    slug = re.sub(r"-+", "-", slug)
    return slug.strip("-")


def html_to_markdown(html: str) -> str:
    if not html or not html.strip():
        return ""
    result = md(
        html,
        heading_style="ATX",
        bullets="-",
        strip=["style", "script", "font", "center"],
    )
    # Limpiar artefactos de conversion
    result = re.sub(r"\n{3,}", "\n\n", result)
    result = re.sub(r"[ \t]+\n", "\n", result)
    result = re.sub(r"\n[ \t]+\n", "\n\n", result)
    return result.strip()


def clean_answer(text: str) -> str:
    # Fase 0: intro fat + boilerplate SII
    text = INTRO_FAT.sub("", text)
    text = SII_BOILERPLATE.sub("", text)
    text = SII_BOILERPLATE_2.sub("", text)
    text = SII_GENERIC_REFS.sub("", text)

    # Fase 1: grasa léxica (marcadores discursivos, muletillas, perífrasis)
    for pattern, replacement in LEXICO_RULES:
        if callable(replacement):
            text = pattern.sub(replacement, text)
        else:
            text = pattern.sub(replacement, text)

    # Fase 2: compresión prosa legal
    for pattern, replacement in LEGAL_COMPRESSIONS:
        text = pattern.sub(replacement, text)

    # Fase 3: promoción estructural
    text = promote_inline_enumerations(text)

    # Fase 4: fix artefactos de abreviación
    # Eliminar doble sigla: "IDPC (IDPC)" → "IDPC"
    text = re.sub(r"\b(IDPC|IGC|IVA|IA|LIR|LIVS|SII)\s*\(\1\)", r"\1", text)
    # Eliminar paréntesis redundante post-abreviación: "IVA (IVA)" variantes
    text = re.sub(r"\b(IDPC|IGC|IVA|IA|LIR|LIVS|SII)\s*\((?:Impuesto[^)]*|Ley[^)]*)\)", r"\1", text)
    # Eliminar fragmentos huérfanos: líneas que son solo "N° de año."
    text = re.sub(r"(?:^|\n)\s*\d{1,4}\s+de\s+\d{4}\.\s*(?:\n|$)", "\n", text)
    text = re.sub(r"(?:^|\n)\s*N[°ºo]\s*\d+\s+de\s+\d{4}\.\s*(?:\n|$)", "\n", text)

    # Fase 5: limpieza final
    text = re.sub(r"  +", " ", text)                              # espacios dobles
    text = re.sub(r" \n", "\n", text)                             # espacio antes de newline
    text = re.sub(r"\n{3,}", "\n\n", text)                        # líneas vacías excesivas
    text = re.sub(r"^\s*[,;]\s*$", "", text, flags=re.MULTILINE)  # puntuación huérfana
    text = re.sub(r"(?:^|\n)\s*\.\s*(?:\n|$)", "\n", text)        # puntos sueltos
    text = re.sub(r"\n\n\n+", "\n\n", text)                       # colapsar residual
    # Capitalizar inicio de oración tras eliminación de marcador
    text = re.sub(r"(?<=\. )([a-záéíóúñ])", lambda m: m.group(1).upper(), text)
    return text.strip()


def abbreviate_normative(text: str) -> str:
    """Aplicar abreviaciones estándar a referencias normativas."""
    text = re.sub(r"\bLey [Ss]obre Impuesto a la Renta\b", "LIR", text)
    text = re.sub(r"\bLey [Ss]obre Impuesto a las Ventas y Servicios\b", "LIVS", text)
    text = re.sub(r"\bLey [Ss]obre Impuesto a las Herencias,? Asignaciones y Donaciones\b", "Ley 16.271", text)
    text = re.sub(r"\bImpuesto al Valor Agregado\b", "IVA", text)
    text = re.sub(r"\bImpuesto de Primera Categoría\b", "IDPC", text)
    text = re.sub(r"\bImpuesto Global Complementario\b", "IGC", text)
    return text


def format_normatives(normatives: list) -> str:
    if not normatives:
        return ""
    labels = []
    for n in normatives:
        label = n.get("normative_label", "").strip() if isinstance(n, dict) else str(n).strip()
        if label:
            label = abbreviate_normative(label)
            if label not in labels:
                labels.append(label)
    if not labels:
        return ""
    return "**Base normativa:** " + "; ".join(labels)


def format_source(question_id: str, url: str) -> str:
    return f"**Fuente:** [{question_id}]({url})"


def categorize_questions(questions: list) -> dict:
    """Agrupar por categoría L2 (breadcrumb nivel 2). Un artefacto por categoría."""
    groups = defaultdict(list)
    for q in questions:
        bc = q.get("breadcrumbs", [])
        cat_l2 = bc[1].strip() if len(bc) >= 2 else "General"
        key = (cat_l2, cat_l2)  # L2 = L3 (sin subcategoría)
        groups[key].append(q)
    return dict(groups)


def split_group(questions: list, max_size: int) -> list:
    """Split manual. Si max_size=0, no splitear (dejar al toolchain)."""
    if max_size <= 0 or len(questions) <= max_size:
        return [questions]
    chunks = []
    for i in range(0, len(questions), max_size):
        chunks.append(questions[i : i + max_size])
    return chunks


def generate_tags(cat_l2: str, cat_l3: str) -> list:
    tags = ["sii", "faq"]
    cat_tag = slugify(cat_l2)
    if cat_tag and cat_tag not in tags:
        tags.append(cat_tag)
    if cat_l3 != cat_l2:
        sub_tag = slugify(cat_l3)
        if sub_tag and sub_tag not in tags:
            tags.append(sub_tag)
    # Asegurar minimo 3 tags
    if len(tags) < 3:
        tags.append("impuestos")
    return tags


def build_artifact(cat_l2: str, cat_l3: str, questions: list,
                   part_num: int = 0, total_parts: int = 1) -> tuple:
    slug_base = f"faq-{slugify(cat_l2)}"
    if cat_l3 != cat_l2:
        slug_base += f"-{slugify(cat_l3)}"
    if total_parts > 1:
        slug = f"{slug_base}-parte-{part_num}"
    else:
        slug = slug_base

    urn = f"urn:sii:kb:{slug}"

    title = cat_l3 if cat_l3 != cat_l2 else cat_l2
    if total_parts > 1:
        title += f" (Parte {part_num}/{total_parts})"
    title += " — Preguntas Frecuentes SII"

    frontmatter = {
        "_manifest": {
            "urn": urn,
            "provenance": {
                "created_by": CREATED_BY,
                "created_at": CREATED_AT,
                "source": f"SII Preguntas Frecuentes — {cat_l2} — {cat_l3}",
            },
        },
        "version": ARTIFACT_VERSION,
        "status": "published",
        "tags": generate_tags(cat_l2, cat_l3),
        "lang": "es",
        "extensions": {
            "sii": {
                "family": "faq",
                "source_category": cat_l2,
                "source_subcategory": cat_l3,
                "question_count": len(questions),
            }
        },
    }

    body_parts = [f"# {title}"]

    for q in questions:
        question_text = q.get("question", "").strip()
        answer_html = q.get("answer_html", "")
        question_id = q.get("question_id", "")
        url = q.get("url", "")
        normatives = q.get("normative_related", [])

        # Heading: pregunta original
        body_parts.append(f"\n## {question_text}\n")

        # Cuerpo: HTML -> Markdown -> limpieza
        answer_md = html_to_markdown(answer_html)
        answer_md = clean_answer(answer_md)

        # Demote headings internos de la respuesta (### -> ####, ## -> ###)
        answer_md = re.sub(r"^(#{1,2})\s", lambda m: "#" * (len(m.group(1)) + 2) + " ", answer_md, flags=re.MULTILINE)

        if answer_md:
            body_parts.append(answer_md)

        # Normativas
        norm_line = format_normatives(normatives)
        if norm_line:
            body_parts.append(f"\n{norm_line}")

        # Fuente
        if question_id and url:
            body_parts.append(f"\n{format_source(question_id, url)}")

    body = "\n".join(body_parts)
    filename = f"{slug}.md"

    return filename, frontmatter, body


# -- Main --------------------------------------------------------------------


def main():
    dry_run = "--dry-run" in sys.argv

    print(f"[curator] Leyendo fuentes: {SOURCE_PATH}")
    questions = json.loads(SOURCE_PATH.read_text(encoding="utf-8"))
    print(f"[curator] Total preguntas: {len(questions)}")

    # Agrupar por subcategoria
    groups = categorize_questions(questions)
    print(f"[curator] Subcategorias detectadas: {len(groups)}")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    artifacts_written = 0
    questions_processed = 0
    warnings = []
    lint_failures = []

    for (cat_l2, cat_l3), qs in sorted(groups.items()):
        parts = split_group(qs, MAX_QUESTIONS_PER_ARTIFACT)
        total_parts = len(parts)

        for part_idx, part_qs in enumerate(parts, start=1):
            filename, frontmatter, body = build_artifact(
                cat_l2, cat_l3, part_qs,
                part_num=part_idx, total_parts=total_parts,
            )
            path = OUTPUT_DIR / filename

            if dry_run:
                print(f"  [DRY] {filename} ({len(part_qs)} preguntas)")
                artifacts_written += 1
                questions_processed += len(part_qs)
                continue

            try:
                report = dump_yaml_frontmatter_and_body(path, frontmatter, body)
                artifacts_written += 1
                questions_processed += len(part_qs)

                shard_count = report.get("split", {}).get("shard_count", 1)
                if shard_count > 1:
                    print(f"  [SPLIT] {filename} -> {shard_count} shards")
                else:
                    print(f"  [OK] {filename} ({len(part_qs)} preguntas)")

            except ValueError as e:
                error_msg = str(e)
                lint_failures.append((filename, error_msg))
                print(f"  [LINT-FAIL] {filename}: {error_msg}")
                # Escribir sin lint como fallback para diagnostico
                content = "---\n"
                import yaml
                content += yaml.safe_dump(frontmatter, sort_keys=False, allow_unicode=True).strip()
                content += "\n---\n\n"
                content += body.rstrip() + "\n"
                path.write_text(content, encoding="utf-8")
                artifacts_written += 1
                questions_processed += len(part_qs)
                warnings.append(f"{filename}: lint fallido, escrito sin autofix")

    # Reporte
    print(f"\n{'='*60}")
    print(f"[curator] REPORTE KORAFICACION SII FAQ")
    print(f"{'='*60}")
    print(f"  Preguntas procesadas: {questions_processed}/{len(questions)}")
    print(f"  Artefactos generados: {artifacts_written}")
    print(f"  Subcategorias: {len(groups)}")
    if lint_failures:
        print(f"  Lint failures: {len(lint_failures)}")
        for fname, err in lint_failures[:10]:
            print(f"    - {fname}: {err[:120]}")
    if warnings:
        print(f"  Warnings: {len(warnings)}")
        for w in warnings[:10]:
            print(f"    - {w}")
    print(f"  Output: {OUTPUT_DIR}")
    print(f"{'='*60}")

    return 0 if not lint_failures else 1


if __name__ == "__main__":
    sys.exit(main())
