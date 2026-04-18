#!/usr/bin/env python3
"""
Actualiza las rutas `file:` en catalog_master_kora.yml para reflejar
la refactorización física (agrupación de agentes y macro-dominios de conocimiento).
"""
import yaml
import os

CATALOG_PATH = "/Users/felixsanhueza/Developer/kora/catalog/catalog_master_kora.yml"
KORA_ROOT = "/Users/felixsanhueza/Developer/kora"


def main():
    with open(CATALOG_PATH, "r", encoding="utf-8") as f:
        catalog_raw = yaml.safe_load(f)

    # Usaremos string replacement directamente para preservar comentarios y formato (ruamel.yaml es mejor pero str replace basta aquí)
    with open(CATALOG_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    changes = 0
    # Update Agents
    # Buscamos las carpetas reales para no adivinar
    for root, dirs, files in os.walk(os.path.join(KORA_ROOT, "agents")):
        for file in files:
            if file.endswith(".yaml") or file.endswith(".yml"):
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, KORA_ROOT)
                # old_path was simple: agents/<name>/agent_<name>.yaml
                agent_name = os.path.basename(os.path.dirname(full_path))
                old_path = f"agents/{agent_name}/{file}"

                if old_path != rel_path:
                    # found a moved agent
                    content = content.replace(f"file: {old_path}", f"file: {rel_path}")
                    content = content.replace(
                        f'file: "{old_path}"', f"file: {rel_path}"
                    )
                    content = content.replace(
                        f"file: '{old_path}'", f"file: {rel_path}"
                    )
                    changes += 1

    # Update Knowledge
    for root, dirs, files in os.walk(os.path.join(KORA_ROOT, "knowledge")):
        for file in files:
            if (
                file.endswith(".yaml")
                or file.endswith(".yml")
                or file.endswith(".json")
                or file.endswith(".md")
                or file.endswith(".ttl")
            ):
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, KORA_ROOT)

                # Knowledge old paths were: knowledge/domains/<domain>/<file>
                # Encontrar de dónde venía:
                # Si ahora está en knowledge/applied/tde/file.yml, antes estaba en knowledge/domains/gov/file.yml o legal/...
                filename = os.path.basename(full_path)

                # Check possible old paths
                for old_dom in ["core", "cat", "sys", "gn", "gov", "legal", "mgmt"]:
                    old_path = f"knowledge/domains/{old_dom}/{filename}"
                    if old_path in content:
                        content = content.replace(
                            f"file: {old_path}", f"file: {rel_path}"
                        )
                        content = content.replace(
                            f'file: "{old_path}"', f"file: {rel_path}"
                        )
                        content = content.replace(
                            f"file: '{old_path}'", f"file: {rel_path}"
                        )
                        changes += 1

    if changes > 0:
        with open(CATALOG_PATH, "w", encoding="utf-8") as f:
            f.write(content)
        print(
            f"✅ Catálogo maestro actualizado: {changes} rutas file: reemplazadas con éxito."
        )
    else:
        print("No se encontraron rutas para reemplazar o ya están actualizadas.")


if __name__ == "__main__":
    main()
