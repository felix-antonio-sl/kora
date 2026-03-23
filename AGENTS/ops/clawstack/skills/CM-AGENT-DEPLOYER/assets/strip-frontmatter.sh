#!/usr/bin/env bash
# Strip KORA YAML frontmatter from markdown files
# Fuente: urn:ops:kb:deploy-agente-kora-en-openclaw §4.2
#
# Uso:
#   strip-frontmatter.sh <source> <destination>
#   strip-frontmatter.sh --dir <source-dir> <dest-dir>
#
# El frontmatter KORA tiene formato: ---\n_manifest:\n...\n---
# Este script lo remueve, dejando solo el contenido operacional.

set -euo pipefail

strip_one() {
    local src="$1" dst="$2"
    python3 -c "
content = open('$src').read()
if content.startswith('---'):
    parts = content.split('---', 2)
    if len(parts) >= 3:
        open('$dst', 'w').write(parts[2].lstrip('\n'))
        return
open('$dst', 'w').write(content)
"
}

if [ "${1:-}" = "--dir" ]; then
    SRC_DIR="${2:?Falta source directory}"
    DST_DIR="${3:?Falta destination directory}"
    mkdir -p "$DST_DIR"

    for file in "$SRC_DIR"/*.md; do
        [ -f "$file" ] && strip_one "$file" "$DST_DIR/$(basename "$file")"
    done

    # Skills degenerados
    if [ -d "$SRC_DIR/skills" ]; then
        mkdir -p "$DST_DIR/skills"
        for skill in "$SRC_DIR"/skills/CM-*.md; do
            [ -f "$skill" ] && strip_one "$skill" "$DST_DIR/skills/$(basename "$skill")"
        done

        # Skills extendidos (directorios CM-*/)
        for skill_dir in "$SRC_DIR"/skills/CM-*/; do
            [ -d "$skill_dir" ] || continue
            skill_name=$(basename "$skill_dir")
            mkdir -p "$DST_DIR/skills/$skill_name"
            [ -f "$skill_dir/SKILL.md" ] && strip_one "$skill_dir/SKILL.md" "$DST_DIR/skills/$skill_name/SKILL.md"
            # Copiar fibras sin modificar
            for fiber in scripts references assets; do
                [ -d "$skill_dir/$fiber" ] && cp -r "$skill_dir/$fiber" "$DST_DIR/skills/$skill_name/"
            done
        done
    fi

    echo "Stripped $(find "$DST_DIR" -name '*.md' | wc -l) files to $DST_DIR"
else
    SRC="${1:?Uso: $0 <source> <destination> | $0 --dir <src-dir> <dst-dir>}"
    DST="${2:?Falta destination}"
    strip_one "$SRC" "$DST"
fi
