#!/usr/bin/env python3
"""Mirror OPCloud sandbox graphics resources and graphics-related bundles.

The deploy is an Angular single-page app. There is no public directory listing,
so this script downloads the HTML entrypoint, same-origin CSS/JS bundles, and
static graphic/font assets that those files reference directly. Template paths
such as ``assets/SVG/${handle}.svg`` are recorded as dynamic patterns instead of
being treated as real URLs.
"""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import time
import csv
from pathlib import Path
from urllib.parse import unquote, urljoin, urlparse
from urllib.request import Request, urlopen


BASE_URL = "https://opcloud-sandbox.web.app/"
ROOT = Path(__file__).resolve().parent
MIRROR = ROOT / "mirror_static"

ASSET_EXTENSIONS = {
    ".avif",
    ".bmp",
    ".css",
    ".eot",
    ".gif",
    ".ico",
    ".jpeg",
    ".jpg",
    ".js",
    ".json",
    ".mjs",
    ".otf",
    ".png",
    ".svg",
    ".ttf",
    ".webp",
    ".woff",
    ".woff2",
}

GRAPHIC_EXTENSIONS = {
    ".avif",
    ".bmp",
    ".gif",
    ".ico",
    ".jpeg",
    ".jpg",
    ".png",
    ".svg",
    ".webp",
}

FONT_EXTENSIONS = {".eot", ".otf", ".ttf", ".woff", ".woff2"}
TEXT_EXTENSIONS = {".css", ".html", ".js", ".json", ".mjs", ".svg"}

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X) "
        "AppleWebKit/537.36 Chrome/120 Safari/537.36 Codex OPCloud audit"
    )
}


def is_same_origin(url: str) -> bool:
    return urlparse(url).netloc == urlparse(BASE_URL).netloc


def normalize(ref: str, base: str) -> str | None:
    ref = ref.strip().strip("\"'")
    if not ref or ref.startswith(("data:", "blob:", "javascript:", "mailto:", "#")):
        return None
    if any(token in ref for token in ("${", "{{", "}}", "}", "{", "+")):
        return None
    if ref.count("assets/") > 1:
        return None
    if ref.startswith("assets/"):
        ref = "/" + ref
    url = urljoin(base, ref.replace("\\/", "/"))
    parsed = urlparse(url)
    if not is_same_origin(url):
        return None
    if parsed.query:
        parsed = parsed._replace(query="")
    return parsed._replace(fragment="").geturl()


def local_path(url: str) -> Path:
    parsed = urlparse(url)
    path = unquote(parsed.path.lstrip("/")) or "index.html"
    if path.endswith("/"):
        path += "index.html"
    return MIRROR / path


def classify(path: str, content_type: str) -> str:
    suffix = Path(urlparse(path).path).suffix.lower()
    if "text/html" in content_type and suffix not in {"", ".html"}:
        return "asset_reference_fallback"
    if suffix in GRAPHIC_EXTENSIONS:
        return "graphic_asset"
    if suffix in FONT_EXTENSIONS:
        return "font_asset"
    if suffix == ".css":
        return "style_bundle"
    if suffix in {".js", ".mjs"}:
        return "script_bundle"
    if suffix == ".json":
        return "data_or_config"
    if suffix in {".html", ""} or "text/html" in content_type:
        return "html_entry"
    return "other"


def fetch(url: str) -> tuple[bytes, dict[str, object]]:
    request = Request(url, headers=HEADERS)
    with urlopen(request, timeout=30) as response:
        data = response.read()
        content_type = response.headers.get("content-type", "")
        last_modified = response.headers.get("last-modified")
        etag = response.headers.get("etag")
    path = local_path(url)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(data)
    meta = {
        "url": url,
        "path": str(path.relative_to(ROOT)),
        "bytes": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
        "content_type": content_type,
        "last_modified": last_modified,
        "etag": etag,
        "kind": classify(url, content_type),
    }
    return data, meta


def references_from_text(text: str, base: str) -> set[str]:
    refs: set[str] = set()

    patterns = [
        r"""(?:src|href)=["']([^"']+)["']""",
        r"""url\(([^)]+)\)""",
        r"""sourceMappingURL=([^\s*]+)""",
        r"""["'`]((?:/?assets/)[^"'`\s),;]+)["'`]""",
        r"""\b([A-Za-z0-9_-]+\.[a-f0-9]{8,}\.(?:css|js))\b""",
    ]

    for pattern in patterns:
        for match in re.finditer(pattern, text, re.IGNORECASE):
            raw = match.group(1).strip().strip("\"'")
            if pattern.startswith(r"""\b("""):
                raw = "/" + raw
            url = normalize(raw, base)
            if not url:
                continue
            suffix = Path(urlparse(url).path).suffix.lower()
            if suffix in ASSET_EXTENSIONS or url.rstrip("/") == BASE_URL.rstrip("/"):
                refs.add(url)
    return refs


def dynamic_patterns(text: str, source: str) -> list[dict[str, str]]:
    patterns: list[dict[str, str]] = []
    for match in re.finditer(r"""assets/[^"'`\s)]*(?:\$\{|{{)[^"'`\s)]*""", text):
        patterns.append({"source": source, "pattern": match.group(0)[:240]})
    return patterns


def write_inventory(entries: list[dict[str, object]], dynamic: list[dict[str, str]], errors: list[dict[str, str]]) -> None:
    by_kind: dict[str, list[dict[str, object]]] = {}
    for entry in entries:
        by_kind.setdefault(str(entry["kind"]), []).append(entry)

    lines = [
        "# OPCloud sandbox graphics download inventory",
        "",
        f"- Base URL: {BASE_URL}",
        f"- Generated at UTC: {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}",
        f"- Downloaded files: {len(entries)}",
        f"- Download errors: {len(errors)}",
        "",
    ]

    for kind in [
        "html_entry",
        "style_bundle",
        "script_bundle",
        "graphic_asset",
        "font_asset",
        "asset_reference_fallback",
        "data_or_config",
        "other",
    ]:
        rows = by_kind.get(kind, [])
        if not rows:
            continue
        lines.append(f"## {kind} ({len(rows)})")
        for entry in rows:
            lines.append(
                f"- `{entry['path']}` | {entry['bytes']} bytes | "
                f"`{str(entry['sha256'])[:16]}` | {entry['url']}"
            )
        lines.append("")

    if dynamic:
        lines.append("## Dynamic asset patterns not directly enumerable")
        for item in dynamic:
            lines.append(f"- `{item['source']}`: `{item['pattern']}`")
        lines.append("")

    if errors:
        lines.append("## Download errors")
        for error in errors:
            lines.append(f"- `{error['url']}`: {error['error']}")
        lines.append("")

    (ROOT / "download-inventory.md").write_text("\n".join(lines), encoding="utf-8")


def asset_dimensions_or_type(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix == ".svg":
        text = path.read_text(encoding="utf-8", errors="ignore")[:1000]
        match = re.search(
            r'<svg[^>]*(?:width="([^"]+)"[^>]*height="([^"]+)"|viewBox="([^"]+)")',
            text,
        )
        if not match:
            return ""
        if match.group(1):
            return f"{match.group(1)}x{match.group(2)}"
        return f"viewBox {match.group(3)}"
    if suffix in GRAPHIC_EXTENSIONS:
        try:
            return subprocess.check_output(["file", "-b", str(path)], text=True).strip()
        except Exception as exc:  # noqa: BLE001 - catalog keeps the failure value.
            return repr(exc)
    return ""


def write_asset_catalog(entries: list[dict[str, object]]) -> None:
    rows = []
    for entry in entries:
        if entry["kind"] not in {"graphic_asset", "font_asset", "asset_reference_fallback"}:
            continue
        path = ROOT / str(entry["path"])
        rows.append(
            {
                "path": str(entry["path"]).replace("mirror_static/", ""),
                "kind": entry["kind"],
                "extension": path.suffix.lower().lstrip("."),
                "bytes": entry["bytes"],
                "sha256": entry["sha256"],
                "dimensions_or_filetype": asset_dimensions_or_type(path),
                "content_type": entry["content_type"],
                "url": entry["url"],
            }
        )

    with (ROOT / "asset-catalog.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "path",
                "kind",
                "extension",
                "bytes",
                "sha256",
                "dimensions_or_filetype",
                "content_type",
                "url",
            ],
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)


def main() -> int:
    MIRROR.mkdir(parents=True, exist_ok=True)
    queue = [BASE_URL]
    seen: dict[str, dict[str, object]] = {}
    errors: list[dict[str, str]] = []
    dynamic: list[dict[str, str]] = []

    index = 0
    while index < len(queue):
        url = queue[index]
        index += 1
        if url in seen:
            continue
        try:
            data, meta = fetch(url)
        except Exception as exc:  # noqa: BLE001 - audit wants captured failures.
            errors.append({"url": url, "error": repr(exc)})
            continue
        seen[url] = meta

        suffix = Path(urlparse(url).path).suffix.lower()
        if suffix in TEXT_EXTENSIONS or meta["kind"] == "html_entry":
            text = data.decode("utf-8", errors="ignore")
            dynamic.extend(dynamic_patterns(text, str(meta["path"])))
            for ref in sorted(references_from_text(text, url)):
                if ref not in seen and ref not in queue:
                    queue.append(ref)

    entries = [seen[url] for url in sorted(seen)]
    manifest = {
        "base_url": BASE_URL,
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "downloaded_count": len(entries),
        "errors": errors,
        "dynamic_asset_patterns": dynamic,
        "entries": entries,
    }
    (ROOT / "download-manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    write_inventory(entries, dynamic, errors)
    write_asset_catalog(entries)
    print(json.dumps({
        "downloaded": len(entries),
        "errors": len(errors),
        "dynamic_asset_patterns": len(dynamic),
        "root": str(ROOT),
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
