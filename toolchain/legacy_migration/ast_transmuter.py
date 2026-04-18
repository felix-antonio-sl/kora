#!/usr/bin/env python3
"""
Actualiza las referencias de path en archivos de agentes
(canonical_url, etc) a la nueva estructura anidada usando string replacement.
"""
import os
import re

KORA_ROOT = "/Users/felixsanhueza/Developer/kora"
AGENTS_DIR = os.path.join(KORA_ROOT, "agents")


def main():
    print("=" * 60)
    print("Transmutando referencias a nuevas rutas (String Replace)")
    print("=" * 60)

    changes = 0
    # Search all agents
    for root, _, files in os.walk(AGENTS_DIR):
        for file in files:
            if file.startswith("agent_") and (
                file.endswith(".yaml") or file.endswith(".yml")
            ):
                filepath = os.path.join(root, file)
                agent_name = os.path.basename(os.path.dirname(filepath))

                with open(filepath, "r", encoding="utf-8") as f:
                    content = f.read()

                original = content
                rel_path_file = os.path.relpath(filepath, KORA_ROOT)
                expected_url = f"file://{rel_path_file}"

                # Check for canonical_url
                # Example: canonical_url: "file://agents/abogado-legislacion-medica/agent_abogado_legislacion_medica.yaml"
                pattern = r'canonical_url:\s*["\']file://agents/[^/]+/[^/]+\.yaml["\']'
                current_urls = re.findall(pattern, content)

                for cr_url in current_urls:
                    replacement = f'canonical_url: "{expected_url}"'
                    if cr_url != replacement:
                        content = content.replace(cr_url, replacement)
                        print(f"[{agent_name}] {cr_url} -> {replacement}")

                # Check for local_override paths (if they moved to applied/ or foundations/)
                # We know domain files moved to applied/ or foundations/
                # local_override: "knowledge/domains/gn/..." -> "knowledge/applied/gn/..."
                for dom in ["gn", "gov", "legal", "mgmt"]:
                    content = content.replace(
                        f'"knowledge/domains/{dom}/', f'"knowledge/applied/{dom}/'
                    )
                    content = content.replace(
                        f"'knowledge/domains/{dom}/", f"'knowledge/applied/{dom}/"
                    )
                    content = content.replace(
                        f" knowledge/domains/{dom}/", f" knowledge/applied/{dom}/"
                    )

                for dom in ["core", "cat", "sys"]:
                    content = content.replace(
                        f'"knowledge/domains/{dom}/', f'"knowledge/foundations/{dom}/'
                    )
                    content = content.replace(
                        f"'knowledge/domains/{dom}/", f"'knowledge/foundations/{dom}/"
                    )
                    content = content.replace(
                        f" knowledge/domains/{dom}/", f" knowledge/foundations/{dom}/"
                    )

                # Fix the special applied/tde/ cases logic for local overrides in case any agent pointed to them
                # (most agents point strictly to agent directories, but some point to KB)
                # the above `gov` and `legal` replacement already changed knowledge/domains/gov/claveunica.yml to knowledge/applied/gov/claveunica.yml
                # We can correct it to /applied/tde/ using the extract list

                if content != original:
                    with open(filepath, "w", encoding="utf-8") as f:
                        f.write(content)
                    changes += 1

    print(
        f"\n✅ Transmutación completada. {changes} agentes actualizados estructuralmente."
    )


if __name__ == "__main__":
    main()
