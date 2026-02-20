#!/usr/bin/env python3
"""
kora-cleanup-global: Reemplazo bruto de todos los namespaces legacy restantes.
Transforma urn:knowledge:{fxsl|gorenuble|tde|orko|korvo}: -> urn:knowledge:koda:
"""
from pathlib import Path

KORA_ROOT = Path("/Users/felixsanhueza/Developer/kora")
LEGACY_NAMESPACES = ["fxsl", "gorenuble", "tde", "orko", "korvo", "moltbot"]


def cleanup_global():
    files = (
        list(KORA_ROOT.rglob("*.yaml"))
        + list(KORA_ROOT.rglob("*.yml"))
        + list(KORA_ROOT.rglob("*.md"))
        + list(KORA_ROOT.rglob("*.json"))
    )

    total_fixes = 0
    files_fixed = 0

    for fpath in files:
        try:
            with open(fpath, "r", encoding="utf-8") as f:
                content = f.read()
        except:
            continue

        new_content = content
        for ns in LEGACY_NAMESPACES:
            old = f"urn:knowledge:{ns}:"
            new = "urn:knowledge:koda:"
            new_content = new_content.replace(old, new)

        if new_content != content:
            fixes = sum(
                content.count(f"urn:knowledge:{ns}:") for ns in LEGACY_NAMESPACES
            )
            total_fixes += fixes
            files_fixed += 1
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"  🔧 {fpath.relative_to(KORA_ROOT)} ({fixes} reemplazos)")

    print(
        f"\n✅ Limpieza global completada: {total_fixes} reemplazos en {files_fixed} archivos."
    )


if __name__ == "__main__":
    cleanup_global()
