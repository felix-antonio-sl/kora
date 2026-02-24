#!/usr/bin/env python3
import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Tuple


FAR_PATTERNS = [
    re.compile(r"\bEn este documento veremos\b", re.IGNORECASE),
    re.compile(r"\bEn este documento se (?:presenta|aborda|describe)\b", re.IGNORECASE),
    re.compile(r"^\s*A continuación\b[:,]?\s*", re.IGNORECASE),
    re.compile(r"^\s*Por otro lado\b[:,]?\s*", re.IGNORECASE),
    re.compile(r"^\s*Habiendo visto lo anterior\b[:,]?\s*", re.IGNORECASE),
    re.compile(r"^\s*Cabe destacar que\b[:,]?\s*", re.IGNORECASE),
    re.compile(r"^\s*Es importante señalar que\b[:,]?\s*", re.IGNORECASE),
    re.compile(r"\bPodría ser que\b", re.IGNORECASE),
    re.compile(r"\bSuele ocurrir\b", re.IGNORECASE),
    re.compile(r"\bProbablemente\b", re.IGNORECASE),
]

FAR_PREFIX_PATTERNS = [
    re.compile(r"^\s*En este documento(?: se)? (?:veremos|presentamos|se presenta|se aborda|se describe)\s*", re.IGNORECASE),
    re.compile(r"^\s*A continuación[:,]?\s*", re.IGNORECASE),
    re.compile(r"^\s*Por otro lado[:,]?\s*", re.IGNORECASE),
    re.compile(r"^\s*Habiendo visto lo anterior[:,]?\s*", re.IGNORECASE),
    re.compile(r"^\s*Cabe destacar que[:,]?\s*", re.IGNORECASE),
    re.compile(r"^\s*Es importante señalar que[:,]?\s*", re.IGNORECASE),
]

# Facts we must preserve to reduce risk of information loss.
URL_RE = re.compile(r"https?://[^\s)>]+")
URN_RE = re.compile(r"\burn:[a-z0-9][a-z0-9:-]*", re.IGNORECASE)
DATE_RE = re.compile(r"\b\d{4}-\d{2}-\d{2}\b")
LAW_RE = re.compile(r"\b(?:Ley|Decreto|DS|DFL)\s*(?:N[°º]\s*)?\d+(?:\.\d+)?\b", re.IGNORECASE)
NUM_RE = re.compile(r"\b\d[\d.,]*\b")

LIST_RE = re.compile(r"^\s*(?:[-*+]\s+|\d+\.\s+)")
HEADING_RE = re.compile(r"^\s*#{1,6}\s+")
TABLE_RE = re.compile(r"^\s*\|.*\|\s*$|^\s*:?-{3,}:?\s*(?:\|\s*:?-{3,}:?\s*)+$")
BLOCKQUOTE_RE = re.compile(r"^\s*>\s*")


@dataclass
class FileAudit:
    file: str
    far_hits: int
    prose_blocks: int
    issues: List[Dict[str, object]]


def split_frontmatter(text: str) -> Tuple[str, str]:
    if text.startswith("---\n"):
        end = text.find("\n---\n", 4)
        if end != -1:
            return text[: end + 5], text[end + 5 :]
    return "", text


def classify_plain_line(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return False
    if HEADING_RE.match(line):
        return False
    if LIST_RE.match(line):
        return False
    if TABLE_RE.match(line):
        return False
    if BLOCKQUOTE_RE.match(line):
        return False
    return True


def split_sentences(text: str) -> List[str]:
    # Conservative split keeping technical tokens mostly intact.
    chunks = re.split(r"(?<=[.!?;:])\s+(?=[A-ZÁÉÍÓÚÑ0-9(])", text)
    if len(chunks) == 1:
        chunks = re.split(r"\s*;\s*", text)
    return [c.strip() for c in chunks if c.strip()]


def strip_far_prefixes(sentence: str) -> str:
    out = sentence
    for pat in FAR_PREFIX_PATTERNS:
        out = pat.sub("", out)
    out = re.sub(r"\bProbablemente\b[:,]?\s*", "", out, flags=re.IGNORECASE)
    out = re.sub(r"\bSuele ocurrir\b[:,]?\s*", "", out, flags=re.IGNORECASE)
    out = re.sub(r"\bPodría ser que\b[:,]?\s*", "", out, flags=re.IGNORECASE)
    return out.strip()


def normalize_spaces(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def extract_facts(text: str) -> Dict[str, List[str]]:
    return {
        "urls": sorted(set(URL_RE.findall(text))),
        "urns": sorted(set(URN_RE.findall(text))),
        "dates": sorted(set(DATE_RE.findall(text))),
        "laws": sorted(set(LAW_RE.findall(text))),
        "numbers": sorted(set(NUM_RE.findall(text))),
    }


def missing_facts(before: Dict[str, List[str]], after: Dict[str, List[str]]) -> Dict[str, List[str]]:
    out = {}
    for k in before.keys():
        miss = sorted(set(before[k]) - set(after[k]))
        if miss:
            out[k] = miss
    return out


def audit_content(path: Path, text: str) -> FileAudit:
    _, body = split_frontmatter(text)
    lines = body.splitlines()
    in_code = False
    far_hits = 0
    prose_blocks = 0
    issues: List[Dict[str, object]] = []

    i = 0
    while i < len(lines):
        line = lines[i]
        if line.strip().startswith("```"):
            in_code = not in_code
            i += 1
            continue

        if in_code:
            i += 1
            continue

        # FAR scan line-by-line
        for pat in FAR_PATTERNS:
            if pat.search(line):
                far_hits += 1
                issues.append({"line": i + 1, "code": "far_phrase", "text": line.strip()[:200]})
                break

        # Prose block detection
        if classify_plain_line(line):
            prose_blocks += 1
            j = i + 1
            while j < len(lines) and classify_plain_line(lines[j]):
                j += 1
            i = j
            continue

        i += 1

    return FileAudit(file=str(path), far_hits=far_hits, prose_blocks=prose_blocks, issues=issues[:30])


def telegraphize_body(body: str) -> str:
    lines = body.splitlines(keepends=True)
    out: List[str] = []
    in_code = False
    i = 0

    while i < len(lines):
        line = lines[i]
        if line.strip().startswith("```"):
            in_code = not in_code
            out.append(line)
            i += 1
            continue

        if in_code:
            out.append(line)
            i += 1
            continue

        if LIST_RE.match(line):
            m = re.match(r"^(\s*(?:[-*+]\s+|\d+\.\s+))(.*?)(\n?)$", line)
            if m:
                prefix, content, nl = m.group(1), m.group(2), m.group(3)
                cleaned = strip_far_prefixes(normalize_spaces(content))
                out.append(f"{prefix}{cleaned}{nl if nl else ''}")
            else:
                out.append(line)
            i += 1
            continue

        if not classify_plain_line(line):
            out.append(line)
            i += 1
            continue

        # Gather paragraph block
        block = [line.rstrip("\n")]
        i += 1
        while i < len(lines) and classify_plain_line(lines[i]):
            block.append(lines[i].rstrip("\n"))
            i += 1

        text = normalize_spaces(" ".join(s.strip() for s in block if s.strip()))
        if not text:
            out.append("\n")
            continue

        sentences = split_sentences(text)
        cleaned: List[str] = []
        for s in sentences:
            s2 = strip_far_prefixes(normalize_spaces(s))
            if s2:
                cleaned.append(s2)

        if not cleaned:
            continue

        for s in cleaned:
            out.append(f"- {s}\n")
        out.append("\n")

    return "".join(out)


def process_file(path: Path, do_repair: bool) -> Tuple[FileAudit, bool, Dict[str, List[str]]]:
    original = path.read_text(encoding="utf-8", errors="replace")
    before = audit_content(path, original)
    if not do_repair:
        return before, False, {}

    fm, body = split_frontmatter(original)
    fixed_body = telegraphize_body(body)
    candidate = fm + fixed_body
    if not candidate.endswith("\n"):
        candidate += "\n"

    # Fact-preservation guardrail
    missing = missing_facts(extract_facts(original), extract_facts(candidate))
    if missing:
        return before, False, missing

    changed = candidate != original
    if changed:
        path.write_text(candidate, encoding="utf-8")
    return before, changed, {}


def run_audit(base: Path) -> Dict[str, object]:
    files = sorted(base.rglob("*.md"))
    audits = []
    for f in files:
        a = audit_content(f, f.read_text(encoding="utf-8", errors="replace"))
        audits.append(a)

    files_with_issues = [a for a in audits if (a.far_hits + a.prose_blocks) > 0]
    return {
        "path": str(base),
        "files_total": len(files),
        "files_with_issues": len(files_with_issues),
        "far_hits_total": sum(a.far_hits for a in audits),
        "prose_blocks_total": sum(a.prose_blocks for a in audits),
        "top_files": [
            {"file": a.file, "issues": a.far_hits + a.prose_blocks, "far_hits": a.far_hits, "prose_blocks": a.prose_blocks}
            for a in sorted(files_with_issues, key=lambda x: (x.far_hits + x.prose_blocks), reverse=True)[:50]
        ],
        "sample_issues": [{"file": a.file, "issues": a.issues} for a in files_with_issues[:40]],
    }


def run_repair(base: Path) -> Dict[str, object]:
    files = sorted(base.rglob("*.md"))
    changed = 0
    fact_blocked = []
    for f in files:
        _, c, missing = process_file(f, do_repair=True)
        if c:
            changed += 1
        if missing:
            fact_blocked.append({"file": str(f), "missing_facts": missing})
    return {"files_total": len(files), "files_changed": changed, "fact_blocked": fact_blocked}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("path")
    ap.add_argument("--mode", choices=["audit", "repair"], default="audit")
    args = ap.parse_args()

    base = Path(args.path)
    if args.mode == "audit":
        print(json.dumps(run_audit(base), ensure_ascii=False, indent=2))
    else:
        print(json.dumps(run_repair(base), ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
