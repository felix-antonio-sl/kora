#!/usr/bin/env python3
"""
kora-cleanup: Segundo pase de limpieza para URNs legacy residuales.
Busca todas las URNs que aún no son koda:* y las reemplaza.
"""
import re
from pathlib import Path

KORA_ROOT = Path("/Users/felixsanhueza/Developer/kora")

# Patrones de reemplazo dirigidos
REPLACEMENTS = {
    # === fxsl:med-legislacion:* -> koda:legal:* ===
    "fxsl:med-legislacion:index": "koda:legal:index",
    "fxsl:med-legislacion:intro-estatutos": "koda:legal:intro_estatutos",
    "fxsl:med-legislacion:deberes-prohibiciones": "koda:legal:deberes_prohibiciones",
    "fxsl:med-legislacion:ingreso-carrera": "koda:legal:ingreso_carrera",
    "fxsl:med-legislacion:jornada-calificaciones": "koda:legal:jornada_calificaciones",
    "fxsl:med-legislacion:remuneraciones": "koda:legal:remuneraciones",
    "fxsl:med-legislacion:acoso-laboral": "koda:legal:acoso_laboral",
    "fxsl:med-legislacion:responsabilidad-admin": "koda:legal:responsabilidad_admin",
    "fxsl:med-legislacion:terminacion": "koda:legal:terminacion",
    "fxsl:med-legislacion:maternidad": "koda:legal:maternidad",
    "fxsl:med-legislacion:contratacion-publica": "koda:legal:contratacion_publica",
    "fxsl:med-legislacion:feriados-permisos": "koda:legal:feriados_permisos",
    "fxsl:med-legislacion:derechos-especiales": "koda:legal:derechos_especiales",
    "fxsl:med-legislacion:formacion-especialistas": "koda:legal:formacion_especialistas",
    "fxsl:med-legislacion:ley-21643": "koda:legal:ley_21643",
    "fxsl:med-legislacion:ley-15076": "koda:legal:ley_15076",
    "fxsl:med-legislacion:ley-19664": "koda:legal:ley_19664",
    "fxsl:med-legislacion:confianza-legitima": "koda:legal:confianza_legitima",
    # === gorenuble:* -> koda:* ===
    "gorenuble:agents:gestor-ipr-360": "koda:agents:gestor-ipr-360",
    "gorenuble:gn:estado-inicio-tics": "koda:gn:estado-inicio-tics",
    "gorenuble:gn:bpmn-c4": "koda:gn:bpmn-c4",
    "gorenuble:gn:manual-servicios-flotas": "koda:gn:manual-flotas",
    "gorenuble:normativa:circular-33": "koda:legal:circular-33",
    "gorenuble:core:intro": "koda:core:gn-intro",
    "gorenuble:procurement:circular-33": "koda:legal:circular-33",
    "gorenuble:guia-circ33": "koda:gn:guia-circ33",
    "gorenuble:guia-fril": "koda:gn:guia-fril",
}


def cleanup():
    files = (
        list(KORA_ROOT.rglob("*.yaml"))
        + list(KORA_ROOT.rglob("*.yml"))
        + list(KORA_ROOT.rglob("*.md"))
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
        for old_fragment, new_fragment in REPLACEMENTS.items():
            new_content = new_content.replace(
                f"urn:knowledge:{old_fragment}", f"urn:knowledge:{new_fragment}"
            )

        if new_content != content:
            fixes = sum(content.count(f"urn:knowledge:{old}") for old in REPLACEMENTS)
            total_fixes += fixes
            files_fixed += 1
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"  🔧 {fpath.relative_to(KORA_ROOT)} ({fixes} reemplazos)")

    print(
        f"\n✅ Limpieza completada: {total_fixes} reemplazos en {files_fixed} archivos."
    )


if __name__ == "__main__":
    cleanup()
