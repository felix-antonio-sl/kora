#!/usr/bin/env python3
"""
Extrae los archivos TDE desde applied/gov/, applied/legal/, applied/gn/
y los mueve a applied/tde/ según el plan semántico.
"""
import os
import subprocess

TDE_FILES = [
    # gov
    "applied/gov/estrategia_gobierno_digital_2030.yml",  # might have different name
    "applied/gov/gobierno_digital_2030.yml",
    "applied/gov/principios_objetivos.yml",
    "applied/gov/ley_21180_tde.yml",  # from legal? check
    "applied/gov/docdigital.yml",
    "applied/gov/pisee.yml",
    "applied/gov/claveunica.yml",
    "applied/gov/claveunica_tyc.yml",
    "applied/gov/simple_saas.yml",
    "applied/gov/simple_saas_oae.yml",
    "applied/gov/evaltic.yml",
    "applied/gov/mgde.yml",
    "applied/gov/cpat_completa.yml",
    "applied/gov/catalogo_cpat_nuble.yml",
    "applied/gov/diseno_servicios.yml",
    "applied/gov/sistema_tde_2025.yml",
    "applied/gov/metadatos_documentos.yml",
    "applied/gov/orientaciones_gestion_tic.yml",
    "applied/gov/calidad_web.yml",
    "applied/gov/rat_datos_personales.yml",
    "applied/gov/reglamento_tde_ds4.yml",
    "applied/gov/seguridad_ciberseguridad_v1.yml",
    "applied/gov/anonimizacion_datos_v2.yml",
    # legal -> TDE
    "applied/legal/ley_21180_tde.yml",
    "applied/legal/ley_19880_procedimientos.yml",
    "applied/legal/nt_documentos_expedientes.yml",
    "applied/legal/nt_interoperabilidad.yml",
    "applied/legal/nt_notificaciones.yml",
    "applied/legal/nt_seguridad_ciberseguridad.yml",
    "applied/legal/nt_autenticacion.yml",
    "applied/legal/nt_calidad_plataformas.yml",
    # sys or gn? Let's check where they are using find. We'll use wildcards
]


def main():
    os.chdir("/Users/felixsanhueza/Developer/kora/knowledge")

    for f in TDE_FILES:
        if os.path.exists(f):
            # Mover a tde/
            target = f"applied/tde/{os.path.basename(f)}"
            print(f"Moving {f} -> {target}")
            subprocess.run(["git", "mv", f, target])
        else:
            print(f"Skipping (not found): {f}")


if __name__ == "__main__":
    main()
