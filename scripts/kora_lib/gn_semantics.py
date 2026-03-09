from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterable, Union


@dataclass
class ReferenceIR:
    kind: str
    label: str
    target: str


@dataclass
class ParagraphBlock:
    text: str


@dataclass
class BulletListBlock:
    items: list[str]
    title: str | None = None


@dataclass
class ReferenceListBlock:
    items: list[ReferenceIR]
    title: str | None = None


@dataclass
class TableIR:
    headers: list[str]
    rows: list[list[str]]
    title: str | None = None


@dataclass
class RecordSetIR:
    headers: list[str]
    rows: list[dict[str, str]]
    title: str | None = None


BlockIR = Union["SectionIR", ParagraphBlock, BulletListBlock, ReferenceListBlock, TableIR, RecordSetIR]


@dataclass
class SectionIR:
    title: str
    blocks: list[BlockIR] = field(default_factory=list)
    metadata: dict = field(default_factory=dict)


@dataclass
class DocumentIR:
    title: str
    family: str
    publication_class: str
    sections: list[SectionIR] = field(default_factory=list)
    metadata: dict = field(default_factory=dict)


def _escape_table_cell(value: str) -> str:
    return str(value).replace("|", "\\|").replace("\n", "<br>")


def _render_reference(ref: ReferenceIR) -> str:
    if ref.kind == "internal":
        return f"[-> {ref.label}]"
    return f"[{ref.label}]({ref.target})"


def _render_table(headers: list[str], rows: Iterable[Iterable[str]]) -> list[str]:
    lines = [
        "| " + " | ".join(_escape_table_cell(header) for header in headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    for row in rows:
        row_values = list(row)
        padded = row_values + [""] * max(0, len(headers) - len(row_values))
        lines.append("| " + " | ".join(_escape_table_cell(cell) for cell in padded[: len(headers)]) + " |")
    return lines


def render_document(document: DocumentIR) -> str:
    lines = [f"# {document.title}"]
    for section in document.sections:
        lines.extend(["", *_render_section(section, 2)])
    return "\n".join(lines).strip() + "\n"


def _render_section(section: SectionIR, level: int) -> list[str]:
    heading = "#" * min(level, 4)
    lines = [f"{heading} {section.title}"]
    for block in section.blocks:
        if isinstance(block, SectionIR):
            lines.extend(["", *_render_section(block, level + 1)])
            continue
        if isinstance(block, ParagraphBlock):
            lines.extend([line for line in block.text.splitlines() if line.strip()])
            continue
        if isinstance(block, BulletListBlock):
            if block.title:
                lines.extend(["", f"{'#' * min(level + 1, 4)} {block.title}"])
            lines.extend(f"- {item}" for item in block.items)
            continue
        if isinstance(block, ReferenceListBlock):
            if block.title:
                lines.extend(["", f"{'#' * min(level + 1, 4)} {block.title}"])
            lines.extend(f"- {_render_reference(item)}" for item in block.items)
            continue
        if isinstance(block, TableIR):
            if block.title:
                lines.extend(["", f"{'#' * min(level + 1, 4)} {block.title}"])
            lines.extend(_render_table(block.headers, block.rows))
            continue
        if isinstance(block, RecordSetIR):
            if block.title:
                lines.extend(["", f"{'#' * min(level + 1, 4)} {block.title}"])
            rows = [[row.get(header, "") for header in block.headers] for row in block.rows]
            lines.extend(_render_table(block.headers, rows))
    return lines


def document_facts(document: DocumentIR) -> list[str]:
    facts = [f"document.title={document.title}", f"document.family={document.family}", f"document.publication_class={document.publication_class}"]
    for index, section in enumerate(document.sections):
        facts.extend(_section_facts(section, f"section[{index}]"))
    return facts


def _section_facts(section: SectionIR, prefix: str) -> list[str]:
    facts = [f"{prefix}.title={section.title}"]
    for index, block in enumerate(section.blocks):
        child_prefix = f"{prefix}.block[{index}]"
        if isinstance(block, SectionIR):
            facts.extend(_section_facts(block, child_prefix))
        elif isinstance(block, ParagraphBlock):
            facts.append(f"{child_prefix}.paragraph={block.text}")
        elif isinstance(block, BulletListBlock):
            if block.title:
                facts.append(f"{child_prefix}.title={block.title}")
            for item_index, item in enumerate(block.items):
                facts.append(f"{child_prefix}.bullet[{item_index}]={item}")
        elif isinstance(block, ReferenceListBlock):
            if block.title:
                facts.append(f"{child_prefix}.title={block.title}")
            for item_index, item in enumerate(block.items):
                facts.append(f"{child_prefix}.ref[{item_index}]={item.kind}:{item.label}->{item.target}")
        elif isinstance(block, TableIR):
            if block.title:
                facts.append(f"{child_prefix}.title={block.title}")
            facts.append(f"{child_prefix}.headers={'|'.join(block.headers)}")
            for row_index, row in enumerate(block.rows):
                facts.append(f"{child_prefix}.row[{row_index}]={'|'.join(row)}")
        elif isinstance(block, RecordSetIR):
            if block.title:
                facts.append(f"{child_prefix}.title={block.title}")
            facts.append(f"{child_prefix}.headers={'|'.join(block.headers)}")
            for row_index, row in enumerate(block.rows):
                for header in block.headers:
                    facts.append(f"{child_prefix}.row[{row_index}].{header}={row.get(header, '')}")
    return facts
