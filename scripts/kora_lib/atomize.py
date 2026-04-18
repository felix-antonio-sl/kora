from __future__ import annotations

import os
import re
import unicodedata
from collections import Counter, OrderedDict
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path

from .artifacts import dump_yaml_frontmatter_and_body, load_markdown_parts
from .config import KORA_ROOT, SCRIPTORIUM_ROOT


ATOMIC_PRODUCER_URN = "urn:kora:artefacto:atomize"
ATOMIC_TYPES = (
    "requirement",
    "definition",
    "rule",
    "exclusion",
    "constraint",
    "obligation",
    "permission",
    "deadline",
    "tension",
    "fact",
    "scope",
)
SUPPORTED_EXTENSIONS = {".md", ".txt", ".rst"}
MAX_DISCOVERY_DEPTH = 3
SOFT_SEGMENT_TARGET_CHARS = 15000
HARD_SEGMENT_MAX_PROPOSITIONS = 200
INLINE_HEADING_PATTERN = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
BULLET_PATTERN = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+(.*\S.*)$")
TABLE_DIVIDER_PATTERN = re.compile(r"^\s*\|?(?:\s*:?-{2,}:?\s*\|)+\s*:?-{2,}:?\s*\|?\s*$")
MARKDOWN_LINK_PATTERN = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
MARKDOWN_FORMATTING_PATTERN = re.compile(r"[*_`~]+")
SENTENCE_BOUNDARY_PATTERN = re.compile(r"(?<=[.!?;])\s+(?=[A-ZÁÉÍÓÚÜÑ0-9])")
PLAIN_PAGE_NUMBER_PATTERN = re.compile(r"^(?:\d+|[ivxlcdm]{1,8})$", re.IGNORECASE)
PLAIN_TOC_ENTRY_PATTERN = re.compile(r"\.{3,}.*(?:\d+|[ivxlcdm]+)\s*$", re.IGNORECASE)
PLAIN_PART_HEADING_PATTERN = re.compile(r"^PART\s+[IVXLC]+\b.*$")
PLAIN_CHAPTER_ONLY_PATTERN = re.compile(r"^Chapter\s+\d+\s*$", re.IGNORECASE)
PLAIN_SECTION_HEADING_PATTERN = re.compile(r"^\d+\.\d+(?:\.\d+)?\s+[A-ZÁÉÍÓÚÜÑ(“\"].*$")
PLAIN_TOP_SECTION_HEADING_PATTERN = re.compile(r"^\d+\.\s+[A-ZÁÉÍÓÚÜÑ(“\"].*$")
PLAIN_HEADER_ROMAN_SUFFIX_PATTERN = re.compile(r"^[A-Za-z][A-Za-z\s'’:.-]{1,60}\s+[ivxlcdm]{1,8}$", re.IGNORECASE)
PLAIN_HEADER_ROMAN_PREFIX_PATTERN = re.compile(r"^[ivxlcdm]{1,8}\s+[A-Za-z][A-Za-z\s'’:.-]{1,60}$", re.IGNORECASE)
PLAIN_URL_ONLY_PATTERN = re.compile(r"^\d*\s*https?://\S+$", re.IGNORECASE)
PLAIN_FIGURE_CAPTION_PATTERN = re.compile(r"^(?:Fig\.|Figure)\s+\d+(?:\.\d+)?\b", re.IGNORECASE)
PLAIN_FOOTNOTE_PATTERN = re.compile(r"^\d{1,2}[A-ZÁÉÍÓÚÜÑ].+")
PLAIN_CONTINUED_PATTERN = re.compile(r"^(?:continued(?:\s+on\s+next\s+page)?|to be continued)\.?$", re.IGNORECASE)
DATE_OR_DURATION_PATTERN = re.compile(
    r"\b(?:\d{1,2}\s+de\s+[a-záéíóú]+(?:\s+de\s+\d{4})?|\d{4}-\d{2}-\d{2}|"
    r"\d+\s+(?:dias|días|semanas|meses|anos|años)|antes de|hasta el|dentro de)\b",
    re.IGNORECASE,
)
CONSTRAINT_PATTERN = re.compile(
    r"\b(?:maximo|minimo|mínimo|limite|límite|por ciento|%|\d+[.,]?\d*)\b",
    re.IGNORECASE,
)
NUMERIC_TOKEN_PATTERN = re.compile(r"\b\d+(?:[.,]\d+)?\b")
NEGATED_MODAL_PATTERN = re.compile(r"\b(may|must|should|shall|can|could|would|will)\s+not\b", re.IGNORECASE)
NEGATED_DO_PATTERN = re.compile(r"\b(do|does|did)\s+not\b", re.IGNORECASE)
NEGATED_BE_PATTERN = re.compile(r"\b(is|are|was|were)\s+not\b", re.IGNORECASE)
NEGATION_TOKEN_PATTERN = re.compile(r"\b(?:not|no|never|without|cannot)\b", re.IGNORECASE)
EXCEPTION_CLAUSE_PATTERN = re.compile(
    r"\b(?:except|excepto|salvo|unless|only if|only when|solo si|a menos que)\b.*$",
    re.IGNORECASE,
)


@dataclass
class SourceDoc:
    source_id: str
    path: Path
    title: str
    rel_to_output: str
    rel_to_corpus: str


@dataclass
class SourceCitation:
    source_id: str
    href: str
    line_start: int
    line_end: int

    @property
    def label(self) -> str:
        if self.line_start == self.line_end:
            return f"src:{self.source_id}:L{self.line_start}"
        return f"src:{self.source_id}:L{self.line_start}-L{self.line_end}"


@dataclass
class CandidateProposition:
    group_title: str
    text: str
    prop_type: str
    citation: SourceCitation


@dataclass
class Proposition:
    proposition_id: str
    group_title: str
    text: str
    prop_type: str
    sources: list[SourceCitation] = field(default_factory=list)


@dataclass
class SectionChunk:
    group_title: str
    propositions: list[Proposition]
    part_index: int = 1
    part_count: int = 1

    @property
    def display_title(self) -> str:
        if self.part_count <= 1:
            return self.group_title
        return f"{self.group_title} (Parte {self.part_index:02d})"


def _slugify(text: str) -> str:
    normalized = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    normalized = re.sub(r"[^a-zA-Z0-9\s-]", "", normalized).strip().lower()
    normalized = re.sub(r"\s+", "-", normalized)
    normalized = re.sub(r"-+", "-", normalized)
    return normalized.strip("-") or "atomic"


def _clean_inline_text(text: str) -> str:
    text = MARKDOWN_LINK_PATTERN.sub(r"\1", text)
    text = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", r"\1", text)
    text = MARKDOWN_FORMATTING_PATTERN.sub("", text)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def _strip_frontmatter(text: str) -> str:
    if not text.startswith("---\n"):
        return text
    match = re.match(r"^---\s*\n.*?\n---\s*\n?", text, flags=re.DOTALL)
    if not match:
        return text
    return text[match.end():]


def _detect_source_title(path: Path, text: str) -> str:
    body = _strip_frontmatter(text)
    for line in body.splitlines():
        stripped = line.strip()
        match = INLINE_HEADING_PATTERN.match(stripped)
        if match and len(match.group(1)) == 1:
            return _clean_inline_text(match.group(2)) or path.stem
    return path.stem.replace("-", " ").replace("_", " ").strip() or path.name


def _is_plain_text_noise_line(text: str) -> bool:
    stripped = text.strip()
    if not stripped:
        return False
    if PLAIN_PAGE_NUMBER_PATTERN.match(stripped):
        return True
    if PLAIN_HEADER_ROMAN_SUFFIX_PATTERN.match(stripped) and len(stripped.split()) <= 4:
        return True
    if PLAIN_HEADER_ROMAN_PREFIX_PATTERN.match(stripped) and len(stripped.split()) <= 4:
        return True
    if PLAIN_URL_ONLY_PATTERN.match(stripped):
        return True
    if PLAIN_FIGURE_CAPTION_PATTERN.match(stripped):
        return True
    if PLAIN_FOOTNOTE_PATTERN.match(stripped):
        return True
    if PLAIN_CONTINUED_PATTERN.match(stripped):
        return True
    lowered = stripped.lower()
    if "doi 10." in lowered:
        return True
    if lowered.startswith("© "):
        return True
    if "springer science+business media" in lowered:
        return True
    if " – " in stripped or " - " in stripped:
        words = stripped.split()
        if len(words) <= 12 and not stripped.endswith((".", "!", "?")):
            return True
    return False


def _collect_repeated_noise_lines(lines: list[str]) -> set[str]:
    counts: Counter[str] = Counter()
    for raw_line in lines:
        stripped = raw_line.strip()
        if not stripped or len(stripped) > 70:
            continue
        if stripped.endswith((".", "!", "?", ";", ":")):
            continue
        if not any(char.isalpha() for char in stripped):
            continue
        if (
            PLAIN_PART_HEADING_PATTERN.match(stripped)
            or PLAIN_CHAPTER_ONLY_PATTERN.match(stripped)
            or PLAIN_SECTION_HEADING_PATTERN.match(stripped)
            or PLAIN_TOP_SECTION_HEADING_PATTERN.match(stripped)
            or PLAIN_TOC_ENTRY_PATTERN.search(stripped)
        ):
            continue
        counts[stripped] += 1
    return {line for line, count in counts.items() if count >= 2}


def _looks_like_plain_heading_continuation(text: str) -> bool:
    stripped = text.strip()
    if not stripped or len(stripped) > 80:
        return False
    if _is_plain_text_noise_line(stripped):
        return False
    if PLAIN_TOC_ENTRY_PATTERN.search(stripped):
        return False
    if PLAIN_SECTION_HEADING_PATTERN.match(stripped):
        return False
    if PLAIN_TOP_SECTION_HEADING_PATTERN.match(stripped):
        return False
    if stripped.startswith(("…", "...", '"', "'", "“", "”", "‘", "’")):
        return False
    words = stripped.split()
    if len(words) > 8:
        return False
    if stripped.endswith(".") and len(words) > 3:
        return False
    return True


def _looks_like_short_plain_title_line(text: str) -> bool:
    stripped = text.strip()
    if not stripped or len(stripped) > 80:
        return False
    if stripped.endswith((".", "!", "?", ";", ":")):
        return False
    if _is_plain_text_noise_line(stripped):
        return False
    words = stripped.split()
    if len(words) > 8:
        return False
    return any(char.isalpha() for char in stripped)


def _looks_like_epigraph_line(text: str) -> bool:
    stripped = text.strip()
    if not stripped or len(stripped) > 120:
        return False
    if stripped.startswith(("…", "...", "\"", "“", "”", "‘", "’")):
        return True
    if re.search(r"\(\d{4}\)\s*$", stripped):
        return True
    if stripped.count(" ") <= 6 and any(char.isdigit() for char in stripped):
        return True
    return False


def _chapter_short_title(heading: str) -> str:
    return re.sub(r"^Chapter\s+\d+\s+", "", heading, flags=re.IGNORECASE).strip()


def _merge_wrapped_text(parts: list[str]) -> str:
    merged: list[str] = []
    for part in parts:
        stripped = part.strip()
        if not stripped:
            continue
        if merged and merged[-1].endswith("-") and stripped[:1].islower():
            merged[-1] = f"{merged[-1][:-1]}{stripped}"
            continue
        merged.append(stripped)
    return " ".join(merged).strip()


def _normalize_plain_text_lines(lines: list[str]) -> list[tuple[int, str]]:
    normalized: list[tuple[int, str]] = []
    repeated_noise_lines = _collect_repeated_noise_lines(lines)
    in_toc = False
    start_index = 0
    current_h2 = ""
    current_chapter_short = ""
    skip_epigraph = False
    epigraph_lines = 0
    in_footnote = False
    footnote_seen_page_break = False
    for offset, raw_line in enumerate(lines):
        stripped = raw_line.strip()
        if (
            stripped == "Preface"
            or stripped.startswith("Table of Contents")
            or PLAIN_PART_HEADING_PATTERN.match(stripped)
            or PLAIN_CHAPTER_ONLY_PATTERN.match(stripped)
        ):
            start_index = offset
            break
    index = start_index

    while index < len(lines):
        stripped = lines[index].strip()
        if not stripped:
            if normalized and normalized[-1][1] != "":
                normalized.append((index + 1, ""))
            if in_footnote:
                in_footnote = False
                footnote_seen_page_break = False
            skip_epigraph = False
            epigraph_lines = 0
            index += 1
            continue

        if PLAIN_FOOTNOTE_PATTERN.match(stripped):
            in_footnote = True
            footnote_seen_page_break = False
            index += 1
            continue

        if in_footnote:
            if _is_plain_text_noise_line(stripped):
                footnote_seen_page_break = True
                index += 1
                continue
            if footnote_seen_page_break:
                in_footnote = False
                footnote_seen_page_break = False
            else:
                index += 1
                continue

        if _is_plain_text_noise_line(stripped):
            index += 1
            continue

        if stripped in repeated_noise_lines:
            index += 1
            continue

        if stripped == "Table of Contents" or stripped.startswith("Table of Contents "):
            in_toc = True
            index += 1
            continue

        if in_toc:
            if PLAIN_CHAPTER_ONLY_PATTERN.match(stripped):
                in_toc = False
            else:
                index += 1
                continue

        if stripped == "Preface":
            if current_h2 == "Preface":
                index += 1
                continue
            if normalized and normalized[-1][1] != "":
                normalized.append((index + 1, ""))
            normalized.extend([(index + 1, "## Preface"), (index + 1, "")])
            current_h2 = "Preface"
            current_chapter_short = ""
            skip_epigraph = False
            epigraph_lines = 0
            index += 1
            continue

        if PLAIN_PART_HEADING_PATTERN.match(stripped):
            if normalized and normalized[-1][1] != "":
                normalized.append((index + 1, ""))
            normalized.extend([(index + 1, f"## {stripped}"), (index + 1, "")])
            current_h2 = stripped
            current_chapter_short = ""
            skip_epigraph = False
            epigraph_lines = 0
            index += 1
            continue

        if PLAIN_CHAPTER_ONLY_PATTERN.match(stripped):
            title_parts = [stripped]
            cursor = index + 1
            while cursor < len(lines):
                candidate = lines[cursor].strip()
                if not candidate:
                    break
                if not _looks_like_plain_heading_continuation(candidate):
                    break
                title_parts.append(candidate)
                cursor += 1
                if title_parts[-1].endswith(("?", "!")):
                    break
            chapter_heading = _merge_wrapped_text(title_parts)
            if normalized and normalized[-1][1] != "":
                normalized.append((index + 1, ""))
            normalized.extend([(index + 1, f"## {chapter_heading}"), (index + 1, "")])
            current_h2 = chapter_heading
            current_chapter_short = _chapter_short_title(chapter_heading)
            skip_epigraph = True
            epigraph_lines = 0
            index = cursor
            continue

        if PLAIN_TOP_SECTION_HEADING_PATTERN.match(stripped):
            if normalized and normalized[-1][1] != "":
                normalized.append((index + 1, ""))
            normalized.extend([(index + 1, f"### {stripped}"), (index + 1, "")])
            skip_epigraph = False
            epigraph_lines = 0
            index += 1
            continue

        if PLAIN_SECTION_HEADING_PATTERN.match(stripped):
            lowered = stripped.lower()
            if lowered.endswith(" summary") or lowered.endswith(" problems"):
                index += 1
                while index < len(lines):
                    candidate = lines[index].strip()
                    if not candidate:
                        index += 1
                        continue
                    if (
                        PLAIN_CHAPTER_ONLY_PATTERN.match(candidate)
                        or PLAIN_PART_HEADING_PATTERN.match(candidate)
                        or PLAIN_SECTION_HEADING_PATTERN.match(candidate)
                    ):
                        break
                    index += 1
                continue
            if normalized and normalized[-1][1] != "":
                normalized.append((index + 1, ""))
            normalized.extend([(index + 1, f"### {stripped}"), (index + 1, "")])
            skip_epigraph = False
            epigraph_lines = 0
            index += 1
            continue

        if not current_h2 and _looks_like_short_plain_title_line(stripped):
            title_parts = [stripped]
            cursor = index + 1
            while cursor < len(lines):
                candidate = lines[cursor].strip()
                if not candidate:
                    break
                if not _looks_like_plain_heading_continuation(candidate):
                    break
                title_parts.append(candidate)
                cursor += 1
            next_non_empty = ""
            lookahead = cursor
            while lookahead < len(lines):
                candidate = lines[lookahead].strip()
                if candidate:
                    next_non_empty = candidate
                    break
                lookahead += 1
            if next_non_empty and (
                PLAIN_TOP_SECTION_HEADING_PATTERN.match(next_non_empty)
                or PLAIN_SECTION_HEADING_PATTERN.match(next_non_empty)
                or PLAIN_CHAPTER_ONLY_PATTERN.match(next_non_empty)
            ):
                title_heading = _merge_wrapped_text(title_parts)
                if normalized and normalized[-1][1] != "":
                    normalized.append((index + 1, ""))
                normalized.extend([(index + 1, f"## {title_heading}"), (index + 1, "")])
                current_h2 = title_heading
                current_chapter_short = ""
                index = cursor
                continue

        if PLAIN_TOC_ENTRY_PATTERN.search(stripped):
            index += 1
            continue

        if current_chapter_short and stripped == current_chapter_short:
            index += 1
            continue

        if skip_epigraph:
            if _looks_like_epigraph_line(stripped) and epigraph_lines < 8:
                epigraph_lines += 1
                index += 1
                continue
            skip_epigraph = False

        normalized.append((index + 1, stripped))
        index += 1

    while normalized and normalized[-1][1] == "":
        normalized.pop()
    return normalized


def _discover_corpus_files(input_path: Path) -> list[Path]:
    if input_path.is_file():
        if input_path.suffix.lower() not in SUPPORTED_EXTENSIONS:
            raise ValueError(f"input extension not supported: {input_path.suffix}")
        return [input_path]

    files = []
    root_depth = len(input_path.resolve().parts)
    for candidate in sorted(input_path.rglob("*")):
        if not candidate.is_file() or candidate.suffix.lower() not in SUPPORTED_EXTENSIONS:
            continue
        if any(part.startswith(".") for part in candidate.relative_to(input_path).parts):
            continue
        depth = len(candidate.resolve().parts) - root_depth
        if depth > MAX_DISCOVERY_DEPTH:
            continue
        files.append(candidate)
    return files


def _build_source_docs(corpus_files: list[Path], corpus_root: Path, output_dir: Path) -> list[SourceDoc]:
    source_docs = []
    for index, path in enumerate(corpus_files, start=1):
        text = path.read_text(encoding="utf-8")
        try:
            rel_to_corpus = path.relative_to(corpus_root).as_posix()
        except ValueError:
            rel_to_corpus = path.name
        rel_to_output = os.path.relpath(path, output_dir).replace(os.sep, "/")
        source_docs.append(
            SourceDoc(
                source_id=f"S{index:02d}",
                path=path,
                title=_detect_source_title(path, text),
                rel_to_output=rel_to_output,
                rel_to_corpus=rel_to_corpus,
            )
        )
    return source_docs


def _split_sentences(text: str) -> list[str]:
    if len(text) < 90 and len(re.findall(r"[.!?;]", text)) <= 1:
        return [text]
    parts = [part.strip() for part in SENTENCE_BOUNDARY_PATTERN.split(text) if part.strip()]
    if len(parts) <= 1:
        return [text]
    merged = []
    for part in parts:
        if merged and len(part) < 45:
            merged[-1] = f"{merged[-1]} {part}".strip()
            continue
        merged.append(part)
    return merged or [text]


def _classify_proposition(text: str) -> str:
    lower = text.lower()
    if any(token in lower for token in ("contradice", "contradiccion", "conflicto", "tension", "ambiguedad", "ambiguedad")):
        return "tension"
    if any(
        token in lower
        for token in (
            "except",
            "excepto",
            "salvo",
            "unless",
            "only if",
            "only when",
            "no aplica",
            "no podra",
            "no podrá",
            "may not",
            "must not",
            "shall not",
            "cannot",
            "can not",
            "prohibido",
            "queda excluido",
            "se excluye",
            "does not apply",
            "prohibited",
            "excluded",
        )
    ):
        return "exclusion"
    if any(token in lower for token in ("podra", "podrá", "puede", "permitido", "permitted", "se permite", "autorizado", "may ")):
        return "permission"
    if DATE_OR_DURATION_PATTERN.search(lower):
        return "deadline"
    if any(token in lower for token in ("alcance", "aplica a", "applies to", "applies only to", "solo para", "únicamente para", "unicamente para", "within the scope", "dentro del ambito", "ámbito", "ambito")):
        return "scope"
    if any(token in lower for token in ("se entiende por", "define", "definition", "definicion", "definición", "means", "significa", "consiste en")):
        return "definition"
    if any(token in lower for token in ("debera", "deberá", "debe", "deben", "shall", "must")):
        if any(token in lower for token in ("presentar", "emitir", "entregar", "registrar", "remitir", "informar", "realizar", "mantener", "cumplir")):
            return "obligation"
        return "requirement"
    if CONSTRAINT_PATTERN.search(lower):
        return "constraint"
    if any(token in lower for token in ("procedimiento", "proceso", "se realiza", "se ejecuta", "consiste en los siguientes pasos", "flujo")):
        return "rule"
    return "fact"


def _group_title(source_doc: SourceDoc, heading_stack: dict[int, str]) -> str:
    h2 = heading_stack.get(2)
    h3 = heading_stack.get(3)
    if h2 and h3:
        return f"{source_doc.title} · {h2} / {h3}"
    if h2:
        return f"{source_doc.title} · {h2}"
    return source_doc.title


def _append_candidate(candidates: list[CandidateProposition], source_doc: SourceDoc, heading_stack: dict[int, str], text: str, line_start: int, line_end: int, split_sentences: bool = False):
    cleaned = _clean_inline_text(text)
    if not cleaned or len(cleaned.split()) < 3:
        return
    units = _split_sentences(cleaned) if split_sentences else [cleaned]
    for unit in units:
        if len(unit.split()) < 3:
            continue
        citation = SourceCitation(
            source_id=source_doc.source_id,
            href=f"{source_doc.rel_to_output}#L{line_start}" if line_start == line_end else f"{source_doc.rel_to_output}#L{line_start}-L{line_end}",
            line_start=line_start,
            line_end=line_end,
        )
        candidates.append(
            CandidateProposition(
                group_title=_group_title(source_doc, heading_stack),
                text=unit,
                prop_type=_classify_proposition(unit),
                citation=citation,
            )
        )


def _extract_candidates(source_doc: SourceDoc) -> list[CandidateProposition]:
    raw_text = source_doc.path.read_text(encoding="utf-8")
    body = _strip_frontmatter(raw_text)
    raw_lines = body.splitlines()
    if source_doc.path.suffix.lower() == ".txt":
        entries = _normalize_plain_text_lines(raw_lines)
    else:
        entries = [(index + 1, line) for index, line in enumerate(raw_lines)]
    candidates = []
    heading_stack: dict[int, str] = {}
    in_code_block = False
    index = 0

    while index < len(entries):
        line_number, line = entries[index]
        stripped = line.strip()

        if stripped.startswith("```"):
            in_code_block = not in_code_block
            index += 1
            continue
        if in_code_block:
            index += 1
            continue
        if not stripped:
            index += 1
            continue

        heading_match = INLINE_HEADING_PATTERN.match(stripped)
        if heading_match:
            level = len(heading_match.group(1))
            heading_stack = {lvl: value for lvl, value in heading_stack.items() if lvl < level}
            heading_stack[level] = _clean_inline_text(heading_match.group(2))
            index += 1
            continue

        if "|" in stripped and stripped.count("|") >= 2 and not TABLE_DIVIDER_PATTERN.match(stripped):
            cells = [_clean_inline_text(cell) for cell in stripped.strip("|").split("|")]
            cells = [cell for cell in cells if cell]
            if len(cells) >= 2:
                _append_candidate(
                    candidates,
                    source_doc,
                    heading_stack,
                    " | ".join(cells),
                    index + 1,
                    index + 1,
                    split_sentences=False,
                )
            index += 1
            continue

        bullet_match = BULLET_PATTERN.match(line)
        if bullet_match:
            chunk = [bullet_match.group(1).strip()]
            end_line_number = line_number
            cursor = index + 1
            while cursor < len(entries):
                candidate_line_number, candidate_line = entries[cursor]
                candidate_stripped = candidate_line.strip()
                if not candidate_stripped:
                    break
                if INLINE_HEADING_PATTERN.match(candidate_stripped) or BULLET_PATTERN.match(candidate_line):
                    break
                if candidate_stripped.startswith("```"):
                    break
                if "|" in candidate_stripped and candidate_stripped.count("|") >= 2:
                    break
                chunk.append(candidate_stripped)
                end_line_number = candidate_line_number
                cursor += 1
            _append_candidate(
                candidates,
                source_doc,
                heading_stack,
                _merge_wrapped_text(chunk),
                line_number,
                end_line_number,
                split_sentences=False,
            )
            index = cursor
            continue

        paragraph = [stripped]
        end_line_number = line_number
        cursor = index + 1
        while cursor < len(entries):
            candidate_line_number, candidate_line = entries[cursor]
            candidate_stripped = candidate_line.strip()
            if not candidate_stripped:
                break
            if INLINE_HEADING_PATTERN.match(candidate_stripped) or BULLET_PATTERN.match(candidate_line):
                break
            if candidate_stripped.startswith("```"):
                break
            if "|" in candidate_stripped and candidate_stripped.count("|") >= 2:
                break
            paragraph.append(candidate_stripped)
            end_line_number = candidate_line_number
            cursor += 1
        _append_candidate(
            candidates,
            source_doc,
            heading_stack,
            _merge_wrapped_text(paragraph),
            line_number,
            end_line_number,
            split_sentences=True,
        )
        index = cursor

    return candidates


def _normalize_for_dedup(text: str) -> str:
    lowered = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii").lower()
    lowered = re.sub(r"[^a-z0-9\s]", " ", lowered)
    lowered = re.sub(r"\s+", " ", lowered).strip()
    return lowered


def _prop_type_priority(prop_type: str) -> int:
    order = {
        "tension": 100,
        "deadline": 90,
        "constraint": 80,
        "obligation": 70,
        "requirement": 60,
        "exclusion": 50,
        "permission": 40,
        "scope": 30,
        "definition": 20,
        "rule": 10,
        "fact": 0,
    }
    return order.get(prop_type, 0)


def _normalize_for_conflict_signature(text: str) -> str:
    lowered = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii").lower()
    lowered = NUMERIC_TOKEN_PATTERN.sub("<num>", lowered)
    lowered = NEGATED_MODAL_PATTERN.sub(r"\1", lowered)
    lowered = NEGATED_DO_PATTERN.sub("", lowered)
    lowered = NEGATED_BE_PATTERN.sub(r"\1", lowered)
    lowered = EXCEPTION_CLAUSE_PATTERN.sub("", lowered)
    lowered = NEGATION_TOKEN_PATTERN.sub("", lowered)
    lowered = re.sub(r"\bapplies\b", "apply", lowered)
    lowered = re.sub(r"[^a-z0-9<>\s]", " ", lowered)
    lowered = re.sub(r"\s+", " ", lowered).strip()
    return lowered


def _conflict_group_title(propositions: list[Proposition]) -> str:
    suffixes = []
    for proposition in propositions:
        parts = [part.strip() for part in proposition.group_title.split("·")]
        suffixes.append(parts[-1] if parts else proposition.group_title)
    unique_suffixes = []
    for suffix in suffixes:
        if suffix not in unique_suffixes:
            unique_suffixes.append(suffix)
    if len(unique_suffixes) == 1:
        return f"Tensiones entre fuentes · {unique_suffixes[0]}"
    return "Tensiones entre fuentes"


def _build_tension_propositions(propositions: list[Proposition]) -> list[Proposition]:
    grouped: OrderedDict[str, list[Proposition]] = OrderedDict()
    for proposition in propositions:
        if proposition.prop_type == "tension":
            continue
        conflict_signature = _normalize_for_conflict_signature(proposition.text)
        grouped.setdefault(conflict_signature, []).append(proposition)

    tensions: list[Proposition] = []
    for _signature, variants in grouped.items():
        if len(variants) < 2:
            continue
        distinct_texts = []
        for proposition in variants:
            if proposition.text not in distinct_texts:
                distinct_texts.append(proposition.text)
        if len(distinct_texts) < 2:
            continue
        sources: list[SourceCitation] = []
        seen_hrefs = set()
        for proposition in variants:
            for source in proposition.sources:
                if source.href in seen_hrefs:
                    continue
                sources.append(source)
                seen_hrefs.add(source.href)
        joined_positions = " / ".join(f'"{text.rstrip(".!?;:")}"' for text in distinct_texts)
        tensions.append(
            Proposition(
                proposition_id="",
                group_title=_conflict_group_title(variants),
                text=f"Sources disagree on the same claim: {joined_positions}.",
                prop_type="tension",
                sources=sources,
            )
        )
    return tensions


def _deduplicate_candidates(candidates: list[CandidateProposition]) -> list[Proposition]:
    grouped: OrderedDict[str, Proposition] = OrderedDict()
    for candidate in candidates:
        dedup_key = _normalize_for_dedup(candidate.text)
        if dedup_key not in grouped:
            grouped[dedup_key] = Proposition(
                proposition_id="",
                group_title=candidate.group_title,
                text=candidate.text,
                prop_type=candidate.prop_type,
                sources=[candidate.citation],
            )
            continue

        proposition = grouped[dedup_key]
        if _prop_type_priority(candidate.prop_type) > _prop_type_priority(proposition.prop_type):
            proposition.prop_type = candidate.prop_type
        if candidate.citation.href not in {source.href for source in proposition.sources}:
            proposition.sources.append(candidate.citation)

    propositions = list(grouped.values())
    propositions.extend(_build_tension_propositions(propositions))

    total = len(propositions)
    width = max(3, len(str(total)))
    numbered = []
    for index, proposition in enumerate(propositions, start=1):
        proposition.proposition_id = f"P{index:0{width}d}"
        numbered.append(proposition)
    return numbered


def _group_propositions(propositions: list[Proposition]) -> list[tuple[str, list[Proposition]]]:
    groups: OrderedDict[str, list[Proposition]] = OrderedDict()
    for proposition in propositions:
        groups.setdefault(proposition.group_title, []).append(proposition)
    return list(groups.items())


def _render_source_index_lines(source_docs: list[SourceDoc]) -> list[str]:
    lines = ["## Indice de fuentes", ""]
    for source_doc in source_docs:
        lines.append(
            f"- `{source_doc.source_id}` · [{source_doc.rel_to_corpus}]({source_doc.rel_to_output}) · {source_doc.title}"
        )
    return lines


def _render_summary_lines(corpus_path: Path, proposition_count: int, source_count: int, segmented: bool, role: str, segment_index: int | None = None, segment_count: int | None = None) -> list[str]:
    lines = ["## Resumen", ""]
    lines.append(f"- Productor canonico: `{ATOMIC_PRODUCER_URN}`")
    lines.append(f"- Corpus fuente: `{corpus_path}`")
    lines.append(f"- Proposiciones: `{proposition_count}`")
    lines.append(f"- Fuentes: `{source_count}`")
    lines.append(f"- Segmentado: `{'si' if segmented else 'no'}`")
    if segmented and role == "segment" and segment_index is not None and segment_count is not None:
        lines.append(f"- Segmento: `{segment_index:02d}/{segment_count:02d}`")
    if segmented and role == "index" and segment_count is not None:
        lines.append(f"- Artefactos segmentados: `{segment_count}`")
    return lines


def _render_proposition_lines(proposition: Proposition) -> list[str]:
    if len(proposition.sources) == 1:
        source = proposition.sources[0]
        return [
            f"- **{proposition.proposition_id}** · `{proposition.prop_type}` · {proposition.text} · [{source.label}]({source.href})"
        ]

    lines = [f"- **{proposition.proposition_id}** · `{proposition.prop_type}` · {proposition.text}"]
    for source in proposition.sources:
        lines.append(f"  - [{source.label}]({source.href})")
    return lines


def _render_section_lines(group_title: str, propositions: list[Proposition]) -> list[str]:
    lines = [f"## {group_title}", ""]
    for proposition in propositions:
        lines.extend(_render_proposition_lines(proposition))
    return lines


def _estimate_section_chars(section: SectionChunk) -> int:
    lines = _render_section_lines(section.display_title, section.propositions)
    return len("\n".join(lines)) + 2


def _split_large_group(group_title: str, propositions: list[Proposition]) -> list[SectionChunk]:
    chunks = []
    current = []
    current_chars = 0
    for proposition in propositions:
        candidate_lines = _render_proposition_lines(proposition)
        candidate_chars = len("\n".join(candidate_lines)) + 1
        should_cut = bool(
            current
            and (
                len(current) >= HARD_SEGMENT_MAX_PROPOSITIONS
                or (current_chars + candidate_chars > SOFT_SEGMENT_TARGET_CHARS and current_chars >= int(SOFT_SEGMENT_TARGET_CHARS * 0.6))
            )
        )
        if should_cut:
            chunks.append(list(current))
            current = []
            current_chars = 0
        current.append(proposition)
        current_chars += candidate_chars
    if current:
        chunks.append(list(current))
    total_parts = len(chunks)
    return [
        SectionChunk(group_title=group_title, propositions=chunk, part_index=index, part_count=total_parts)
        for index, chunk in enumerate(chunks, start=1)
    ]


def _build_section_chunks(propositions: list[Proposition]) -> list[SectionChunk]:
    chunks = []
    for group_title, group_props in _group_propositions(propositions):
        estimated_chars = len("\n".join(_render_section_lines(group_title, group_props)))
        if len(group_props) > HARD_SEGMENT_MAX_PROPOSITIONS or estimated_chars > int(SOFT_SEGMENT_TARGET_CHARS * 1.2):
            chunks.extend(_split_large_group(group_title, group_props))
            continue
        chunks.append(SectionChunk(group_title=group_title, propositions=group_props))
    return chunks


def _pack_segments(section_chunks: list[SectionChunk]) -> list[list[SectionChunk]]:
    if not section_chunks:
        return []
    segments = []
    current = []
    current_chars = 0
    current_props = 0
    for chunk in section_chunks:
        chunk_chars = _estimate_section_chars(chunk)
        chunk_props = len(chunk.propositions)
        should_cut = bool(
            current
            and (
                current_props + chunk_props > HARD_SEGMENT_MAX_PROPOSITIONS
                or (current_chars + chunk_chars > SOFT_SEGMENT_TARGET_CHARS and current_chars >= int(SOFT_SEGMENT_TARGET_CHARS * 0.6))
            )
        )
        if should_cut:
            segments.append(list(current))
            current = []
            current_chars = 0
            current_props = 0
        current.append(chunk)
        current_chars += chunk_chars
        current_props += chunk_props
    if current:
        segments.append(list(current))
    return segments


def _render_atomic_body(title: str, corpus_path: Path, source_docs: list[SourceDoc], propositions: list[Proposition], section_chunks: list[SectionChunk], segmented: bool, role: str, segment_index: int | None = None, segment_count: int | None = None, segment_table_rows: list[dict] | None = None) -> str:
    lines = [f"# {title}", ""]
    lines.extend(
        _render_summary_lines(
            corpus_path=corpus_path,
            proposition_count=len(propositions),
            source_count=len(source_docs),
            segmented=segmented,
            role=role,
            segment_index=segment_index,
            segment_count=segment_count,
        )
    )
    lines.extend([""])
    lines.extend(_render_source_index_lines(source_docs))

    if role == "index":
        lines.extend(["", "## Segmentos", "", "| Segmento | Rango Pxxx | Dominios |", "| --- | --- | --- |"])
        for row in segment_table_rows or []:
            lines.append(
                f"| [{row['segment']:02d}](urn:kora:kb:atomic-{row['slug']}-{row['segment']:02d}) | {row['range']} | {row['domains']} |"
            )
        return "\n".join(lines).rstrip() + "\n"

    for chunk in section_chunks:
        lines.extend([""])
        lines.extend(_render_section_lines(chunk.display_title, chunk.propositions))

    return "\n".join(lines).rstrip() + "\n"


def _atomic_frontmatter(slug: str, corpus_path: Path, proposition_count: int, segmented: bool, role: str, segment_index: int | None = None, segment_count: int | None = None) -> dict:
    urn_suffix = slug
    if role == "index":
        urn_suffix = f"{slug}-index"
    elif role == "segment" and segment_index is not None:
        urn_suffix = f"{slug}-{segment_index:02d}"

    return {
        "_manifest": {
            "urn": f"urn:kora:kb:atomic-{urn_suffix}",
            "provenance": {
                "created_by": "atomize",
                "created_at": str(date.today()),
                "source": str(corpus_path),
            },
        },
        "version": "1.0.0",
        "status": "draft",
        "tags": ["atomic", "knowledge", slug],
        "lang": "es",
        "extensions": {
            "kora": {
                "family": "atomic",
                "atomic": {
                    "producer": ATOMIC_PRODUCER_URN,
                    "source_corpus": str(corpus_path),
                    "n_propositions": proposition_count,
                    "segmented": segmented,
                    "segment_role": role,
                    "segment_index": segment_index,
                    "segment_count": segment_count,
                    "hand_edited": False,
                    "soft_segment_target_chars": SOFT_SEGMENT_TARGET_CHARS,
                    "hard_segment_max_propositions": HARD_SEGMENT_MAX_PROPOSITIONS,
                },
            }
        },
    }


def _find_existing_atomic_files(output_dir: Path, slug: str) -> list[Path]:
    return sorted(output_dir.glob(f"atomic-{slug}*.md"))


def _assert_overwrite_allowed(existing_paths: list[Path]):
    for path in existing_paths:
        frontmatter, _body = load_markdown_parts(path)
        if not isinstance(frontmatter, dict):
            continue
        atomic_ext = (
            frontmatter.get("extensions", {})
            .get("kora", {})
            .get("atomic", {})
        )
        if isinstance(atomic_ext, dict) and atomic_ext.get("hand_edited"):
            raise ValueError(
                f"existing atomic artifact is marked hand_edited and cannot be overwritten: {path}"
            )


def _cleanup_stale_atomic_files(existing_paths: list[Path], retained_paths: set[Path]):
    for path in existing_paths:
        if path in retained_paths:
            continue
        path.unlink()


def cmd_atomize(input_path: str, slug: str | None = None, output: str | None = None):
    source_path = Path(input_path).expanduser().resolve()
    if not source_path.exists():
        print(f"ERROR: input path not found: {input_path}")
        raise SystemExit(1)

    output_dir = Path(output).expanduser().resolve() if output else (SCRIPTORIUM_ROOT / "REVIEW" / "kora" / "atomic").resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    corpus_root = source_path if source_path.is_dir() else source_path.parent
    corpus_files = _discover_corpus_files(source_path)
    if not corpus_files:
        print(f"ERROR: no supported corpus files found in {input_path}")
        raise SystemExit(1)

    artifact_slug = slug or _slugify(source_path.stem if source_path.is_file() else source_path.name)
    source_docs = _build_source_docs(corpus_files, corpus_root=corpus_root, output_dir=output_dir)

    candidates = []
    for source_doc in source_docs:
        candidates.extend(_extract_candidates(source_doc))
    if not candidates:
        print(f"ERROR: could not extract atomic propositions from {input_path}")
        raise SystemExit(1)

    propositions = _deduplicate_candidates(candidates)
    section_chunks = _build_section_chunks(propositions)
    segments = _pack_segments(section_chunks)
    segmented = len(segments) > 1 or len(propositions) > HARD_SEGMENT_MAX_PROPOSITIONS

    existing_paths = _find_existing_atomic_files(output_dir, artifact_slug)
    _assert_overwrite_allowed(existing_paths)
    if existing_paths:
        _cleanup_stale_atomic_files(existing_paths, set())
        existing_paths = []

    written_paths = []
    if not segmented:
        title = f"Atomic {artifact_slug}"
        body = _render_atomic_body(
            title=title,
            corpus_path=source_path,
            source_docs=source_docs,
            propositions=propositions,
            section_chunks=section_chunks,
            segmented=False,
            role="single",
        )
        frontmatter = _atomic_frontmatter(
            slug=artifact_slug,
            corpus_path=source_path,
            proposition_count=len(propositions),
            segmented=False,
            role="single",
        )
        target_path = output_dir / f"atomic-{artifact_slug}.md"
        dump_yaml_frontmatter_and_body(target_path, frontmatter, body)
        written_paths.append(target_path)
    else:
        index_rows = []
        for segment_number, segment_chunks in enumerate(segments, start=1):
            segment_propositions = [proposition for chunk in segment_chunks for proposition in chunk.propositions]
            segment_source_ids = {source.source_id for proposition in segment_propositions for source in proposition.sources}
            segment_sources = [source_doc for source_doc in source_docs if source_doc.source_id in segment_source_ids]
            segment_body = _render_atomic_body(
                title=f"Atomic {artifact_slug} - Segmento {segment_number:02d}",
                corpus_path=source_path,
                source_docs=segment_sources,
                propositions=segment_propositions,
                section_chunks=segment_chunks,
                segmented=True,
                role="segment",
                segment_index=segment_number,
                segment_count=len(segments),
            )
            segment_frontmatter = _atomic_frontmatter(
                slug=artifact_slug,
                corpus_path=source_path,
                proposition_count=len(segment_propositions),
                segmented=True,
                role="segment",
                segment_index=segment_number,
                segment_count=len(segments),
            )
            segment_path = output_dir / f"atomic-{artifact_slug}-{segment_number:02d}.md"
            dump_yaml_frontmatter_and_body(segment_path, segment_frontmatter, segment_body)
            written_paths.append(segment_path)
            index_rows.append(
                {
                    "segment": segment_number,
                    "range": f"{segment_propositions[0].proposition_id}-{segment_propositions[-1].proposition_id}",
                    "domains": "; ".join(chunk.display_title for chunk in segment_chunks[:3]),
                    "slug": artifact_slug,
                }
            )

        index_body = _render_atomic_body(
            title=f"Atomic {artifact_slug} - Index",
            corpus_path=source_path,
            source_docs=source_docs,
            propositions=[],
            section_chunks=[],
            segmented=True,
            role="index",
            segment_count=len(segments),
            segment_table_rows=index_rows,
        )
        index_frontmatter = _atomic_frontmatter(
            slug=artifact_slug,
            corpus_path=source_path,
            proposition_count=len(propositions),
            segmented=True,
            role="index",
            segment_count=len(segments),
        )
        index_path = output_dir / f"atomic-{artifact_slug}-index.md"
        dump_yaml_frontmatter_and_body(index_path, index_frontmatter, index_body)
        written_paths.insert(0, index_path)

    retained_paths = set(written_paths)
    if existing_paths:
        _cleanup_stale_atomic_files(existing_paths, retained_paths)

    rel_written_paths = []
    for path in written_paths:
        try:
            rel_written_paths.append(path.relative_to(KORA_ROOT))
        except ValueError:
            rel_written_paths.append(path)

    print(f"ATOMIZED: {source_path}")
    print(f"  slug: {artifact_slug}")
    print(f"  sources: {len(source_docs)}")
    print(f"  propositions: {len(propositions)}")
    print(f"  segmented: {'yes' if segmented else 'no'}")
    print("  outputs:")
    for path in rel_written_paths:
        print(f"    - {path}")
