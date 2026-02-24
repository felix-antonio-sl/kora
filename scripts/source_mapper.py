#!/usr/bin/env python3
"""
source_mapper.py — KORA Phase 1 Source Mapping Generator
Generated: 2026-02-24

Reads all knowledge files from /Users/felixsanhueza/Developer/kora/knowledge/,
cross-references with known source locations, and outputs a YAML mapping to
/Users/felixsanhueza/Developer/kora/docs/plans/source-mapping.yml
"""

import os
import glob
from pathlib import Path
from datetime import date

KNOWLEDGE_ROOT = Path("/Users/felixsanhueza/Developer/kora/knowledge")
OUTPUT_FILE = Path("/Users/felixsanhueza/Developer/kora/docs/plans/source-mapping.yml")

WIKIGUIAS = Path("/Users/felixsanhueza/Developer/tde/sources/wikiguias_corpus")
POSIBLES = Path("/Users/felixsanhueza/posibles fuentes")
GORE = POSIBLES / "gore_desde_0"


def w(subdir, filename):
    """Return full path inside wikiguias corpus."""
    return str(WIKIGUIAS / subdir / filename)


def p(filename):
    """Return full path inside posibles fuentes."""
    return str(POSIBLES / filename)


def g(filename):
    """Return full path inside gore_desde_0."""
    return str(GORE / filename)


def file_exists(path):
    if path is None:
        return False
    return Path(path).exists()


# ---------------------------------------------------------------------------
# Mapping definitions
# Each entry: (relative_kb_path, source_path_or_None, strategy, notes)
# ---------------------------------------------------------------------------

TDE_BASE = "knowledge/tde"
GN_BASE = "knowledge/gn"
FXSL_BASE = "knowledge/fxsl"
LEGAL_BASE = "knowledge/legal"
GOV_BASE = "knowledge/gov"
ORKO_BASE = "knowledge/orko"
MGMT_BASE = "knowledge/mgmt"
KORA_BASE = "knowledge/kora"

# ---------------------------------------------------------------------------
# TDE — 29 KBs
# ---------------------------------------------------------------------------
TDE_MAPPINGS = [
    # estrategia
    (
        f"{TDE_BASE}/estrategia/gobierno_digital_2030.yml",
        w("EstrategiasEstrategias", "Estrategia_de_Gobierno_Digital_2030.md"),
        "FROM_SOURCE",
        None,
    ),
    (
        f"{TDE_BASE}/estrategia/principios_objetivos.yml",
        w("EstrategiasEstrategias", "Estrategia_de_identidad_digital.md"),
        "FROM_SOURCE",
        "Primary match; composite from multiple estrategias",
    ),
    # guias
    (
        f"{TDE_BASE}/guias/calidad_web.yml",
        w("Lineamientos_TécnicosGuías", "Guía_Calidad_WEB.md"),
        "FROM_SOURCE",
        None,
    ),
    (
        f"{TDE_BASE}/guias/anonimizacion_datos_v2.yml",
        w("Lineamientos_TécnicosGuías", "Guía_introductoria_a_la_anonimización_de_datos.md"),
        "FROM_SOURCE",
        None,
    ),
    (
        f"{TDE_BASE}/guias/diseno_servicios.yml",
        w("Plataformas_CompartidasManuales_de_Uso", "Recomendaciones_para_el_Diseño_de_Servicios_en_el_Estado.md"),
        "FROM_SOURCE",
        None,
    ),
    (
        f"{TDE_BASE}/guias/evaltic.yml",
        w("Lineamientos_TécnicosGuías", "Guía_Técnica_Marco_para_las_inversiones_y_el_gasto_en_gobierno_digital_EVALTIC.md"),
        "FROM_SOURCE",
        None,
    ),
    (
        f"{TDE_BASE}/guias/metadatos_documentos.yml",
        w("Lineamientos_TécnicosGuías", "Guía_Técnica_de_Metadatos_para_Documentos_y_Expedientes_Electrónicos.md"),
        "FROM_SOURCE",
        None,
    ),
    (
        f"{TDE_BASE}/guias/mgde.yml",
        w("Lineamientos_TécnicosGuías", "Guía_Técnica_aplicación_de_un_marco_de_referencia_de_gestión_de_datos_en_los_órganos_de_la_Administración_del_Estado.md"),
        "FROM_SOURCE",
        None,
    ),
    (
        f"{TDE_BASE}/guias/orientaciones_gestion_tic.yml",
        w("Lineamientos_TécnicosGuías", "Orientaciones_básicas_para_la_gestión_de_las_TIC.md"),
        "FROM_SOURCE",
        None,
    ),
    (
        f"{TDE_BASE}/guias/rat_datos_personales.yml",
        w("Protección_de_Datos_PersonalesPolítica_de_Tratamiento", "Registro_de_Actividades_de_Tratamiento.md"),
        "FROM_SOURCE",
        None,
    ),
    (
        f"{TDE_BASE}/guias/reglamento_tde_ds4.yml",
        w("RegulaciónLeyes_y_Reglamentos", "Decreto_4.md"),
        "FROM_SOURCE",
        None,
    ),
    (
        f"{TDE_BASE}/guias/seguridad_ciberseguridad_v1.yml",
        w("Lineamientos_TécnicosGuías", "Guía_Técnica_de_Seguridad_de_la_Información_y_Ciberseguridad.md"),
        "FROM_SOURCE",
        None,
    ),
    (
        f"{TDE_BASE}/guias/sistema_tde_2025.yml",
        w("Lineamientos_TécnicosGuías", "Guía_Metodológica_del_Sistema_de_Transformación_Digital_2025.md"),
        "FROM_SOURCE",
        None,
    ),
    (
        f"{TDE_BASE}/guias/catalogo_cpat_nuble.yml",
        w("Lineamientos_TécnicosGuías", "Guía_rápida_CPAT.md"),
        "FROM_SOURCE",
        None,
    ),
    (
        f"{TDE_BASE}/guias/cpat_completa.yml",
        w("Lineamientos_TécnicosGuías", "Guía_rápida_CPAT.md"),
        "FROM_SOURCE",
        "Same source as catalogo_cpat_nuble; full CPAT guide",
    ),
    # leyes
    (
        f"{TDE_BASE}/leyes/ley_19880_procedimientos.yml",
        w("RegulaciónLeyes_y_Reglamentos", "Ley_19880.md"),
        "FROM_SOURCE",
        None,
    ),
    (
        f"{TDE_BASE}/leyes/ley_21180_tde.yml",
        w("RegulaciónLeyes_y_Reglamentos", "Ley_Nº_21180_de_Transformación_Digital_del_Estado.md"),
        "FROM_SOURCE",
        None,
    ),
    # normas_tecnicas
    (
        f"{TDE_BASE}/normas_tecnicas/nt_autenticacion.yml",
        w("Lineamientos_TécnicosNormas", "Decreto_9__Norma_Técnica_de_Autenticación.md"),
        "FROM_SOURCE",
        None,
    ),
    (
        f"{TDE_BASE}/normas_tecnicas/nt_calidad_plataformas.yml",
        w("Lineamientos_TécnicosNormas", "Decreto_11__Plataformas_electrónicas_y__procedimientos_administrativos_en_los_Órganos_de_la_Administración_del_Estado.md"),
        "FROM_SOURCE",
        None,
    ),
    (
        f"{TDE_BASE}/normas_tecnicas/nt_documentos_expedientes.yml",
        w("Lineamientos_TécnicosNormas", "Decreto_10__Documentos_y_Expedientes_Electrónicos_para_la_gestión_de_procedimientos_administrativos.md"),
        "FROM_SOURCE",
        None,
    ),
    (
        f"{TDE_BASE}/normas_tecnicas/nt_interoperabilidad.yml",
        w("Lineamientos_TécnicosNormas", "Decreto_12___Interoperabilidad.md"),
        "FROM_SOURCE",
        None,
    ),
    (
        f"{TDE_BASE}/normas_tecnicas/nt_notificaciones.yml",
        w("Lineamientos_TécnicosNormas", "Decreto_8__Norma_técnica_de_notificaciones.md"),
        "FROM_SOURCE",
        None,
    ),
    (
        f"{TDE_BASE}/normas_tecnicas/nt_seguridad_ciberseguridad.yml",
        w("Lineamientos_TécnicosNormas", "Decreto_7___Norma_técnica_de_Seguridad_de_la_Información_y_ciberseguridad.md"),
        "FROM_SOURCE",
        None,
    ),
    # plataformas
    (
        f"{TDE_BASE}/plataformas/claveunica.yml",
        w("Plataformas_CompartidasManuales_de_Uso", "Manual_de_Integración__de_ClaveÚnica.md"),
        "FROM_SOURCE",
        None,
    ),
    (
        f"{TDE_BASE}/plataformas/claveunica_tyc.yml",
        w("Plataformas_CompartidasTérminos_y_Condiciones", "Términos_y_Condiciones_para_la_integración_y_el_uso_del_Sistema_de_ClaveÚnica.md"),
        "FROM_SOURCE",
        None,
    ),
    (
        f"{TDE_BASE}/plataformas/simple_saas.yml",
        w("Plataformas_CompartidasManuales_de_Uso", "Manual_de_uso_SIMPLE_en_modalidad_SaaS.md"),
        "FROM_SOURCE",
        None,
    ),
    (
        f"{TDE_BASE}/plataformas/simple_saas_oae.yml",
        w("Plataformas_CompartidasManuales_de_Uso", "Manual_de_uso_SIMPLE_en_modalidad_SaaS.md"),
        "FROM_SOURCE",
        "Same source as simple_saas; OAE variant",
    ),
    (
        f"{TDE_BASE}/plataformas/docdigital.yml",
        None,
        "FROM_YAML",
        "No clear single-source document found in wikiguias corpus",
    ),
    (
        f"{TDE_BASE}/plataformas/pisee.yml",
        None,
        "FROM_YAML",
        "No clear single-source document found in wikiguias corpus",
    ),
]

# ---------------------------------------------------------------------------
# GN — 77 KBs
# ---------------------------------------------------------------------------

# Files with clear 1:1 source match
GN_WITH_SOURCE = [
    (
        f"{GN_BASE}/normativa/loc-gore.yml",
        g("ley_19175.txt"),
        "FROM_SOURCE",
        None,
    ),
    (
        f"{GN_BASE}/normativa/marco-legal-gores.yml",
        g("fx_ley_18575.md"),
        "FROM_SOURCE",
        None,
    ),
]

# All remaining GN files — FROM_YAML
GN_FROM_YAML = [
    # bpmn
    (f"{GN_BASE}/bpmn/bpmn-d01-actos-administrativos.yml", None, "FROM_YAML", "Process model, no clear single-document source"),
    (f"{GN_BASE}/bpmn/bpmn-d02-ciclo-presupuestario.yml", None, "FROM_YAML", "Process model, no clear single-document source"),
    (f"{GN_BASE}/bpmn/bpmn-d03-gestion-ipr.yml", None, "FROM_YAML", "Process model, no clear single-document source"),
    (f"{GN_BASE}/bpmn/bpmn-d04-compras-contrataciones.yml", None, "FROM_YAML", "Process model, no clear single-document source"),
    (f"{GN_BASE}/bpmn/bpmn-d05-inventarios-activo-fijo.yml", None, "FROM_YAML", "Process model, no clear single-document source"),
    (f"{GN_BASE}/bpmn/bpmn-d06-flota-vehicular.yml", None, "FROM_YAML", "Process model, no clear single-document source"),
    (f"{GN_BASE}/bpmn/bpmn-d07-rrhh.yml", None, "FROM_YAML", "Process model, no clear single-document source"),
    (f"{GN_BASE}/bpmn/bpmn-d08-rendiciones.yml", None, "FROM_YAML", "Process model, no clear single-document source"),
    (f"{GN_BASE}/bpmn/bpmn-d09-cies-sitia.yml", None, "FROM_YAML", "Process model, no clear single-document source"),
    (f"{GN_BASE}/bpmn/bpmn-d10-geoespacial-ide.yml", None, "FROM_YAML", "Process model, no clear single-document source"),
    (f"{GN_BASE}/bpmn/bpmn-index.yml", None, "FROM_YAML", "Index artifact, no clear single-document source"),
    # gestion
    (f"{GN_BASE}/gestion/flujos-aprobacion-documentos.yml", None, "FROM_YAML", "Composite from multiple normative sources"),
    (f"{GN_BASE}/gestion/gestion-info-geoespacial.yml", None, "FROM_YAML", "Composite from multiple sources"),
    (f"{GN_BASE}/gestion/gestion-ipr.yml", None, "FROM_YAML", "Composite from gore_desde_0 and fx_* files"),
    (f"{GN_BASE}/gestion/gestion-prpto-2026.yml", None, "FROM_YAML", "Composite from gore_desde_0 budget docs"),
    (f"{GN_BASE}/gestion/gestion-prpto.yml", None, "FROM_YAML", "Composite from gore_desde_0 budget docs"),
    (f"{GN_BASE}/gestion/gestion-rendiciones.yml", None, "FROM_YAML", "Composite from multiple normative sources"),
    (f"{GN_BASE}/gestion/glosas-gores-2026.yml", None, "FROM_YAML", "Composite from gore_desde_0 glosas docs"),
    (f"{GN_BASE}/gestion/transferencia-ppr.yml", None, "FROM_YAML", "Composite from multiple sources"),
    # gn-cqs-master
    (f"{GN_BASE}/gn-cqs-master.yml", None, "FROM_YAML", "Master index artifact"),
    # gobernanza
    (f"{GN_BASE}/gobernanza/aceleracion-regional.yml", None, "FROM_YAML", "No clear single-source document found"),
    (f"{GN_BASE}/gobernanza/cies-sitia.yml", None, "FROM_YAML", "No clear single-source document found"),
    (f"{GN_BASE}/gobernanza/comunicaciones-oc.yml", None, "FROM_YAML", "No clear single-source document found"),
    (f"{GN_BASE}/gobernanza/cuentas-publicas-2021-2024.yml", None, "FROM_YAML", "Composite from cuentas publicas documents"),
    (f"{GN_BASE}/gobernanza/erd-nuble-2024-2030.yml", None, "FROM_YAML", "No clear single-source document found"),
    (f"{GN_BASE}/gobernanza/estrategia-gestion.yml", None, "FROM_YAML", "No clear single-source document found"),
    (f"{GN_BASE}/gobernanza/estrategia-td-ia.yml", None, "FROM_YAML", "No clear single-source document found"),
    (f"{GN_BASE}/gobernanza/glosario-gore-nuble.yml", None, "FROM_YAML", "Composite glossary artifact"),
    (f"{GN_BASE}/gobernanza/glosario-ipr-consolidado.yml", None, "FROM_YAML", "Composite glossary artifact"),
    (f"{GN_BASE}/gobernanza/gore-ideal.yml", None, "FROM_YAML", "No clear single-source document found"),
    (f"{GN_BASE}/gobernanza/indicadores-nuble.yml", None, "FROM_YAML", "Composite from multiple indicator sources"),
    (f"{GN_BASE}/gobernanza/informe-estado-inicial-gore-pre-td.yml", None, "FROM_YAML", "No clear single-source document found"),
    (f"{GN_BASE}/gobernanza/intro-gores-nuble.yml", None, "FROM_YAML", "No clear single-source document found"),
    (f"{GN_BASE}/gobernanza/matriz-integracion-organica.yml", None, "FROM_YAML", "No clear single-source document found"),
    (f"{GN_BASE}/gobernanza/nuble-250.yml", None, "FROM_YAML", "No clear single-source document found"),
    (f"{GN_BASE}/gobernanza/omega-ipr-gestion-fusion.yml", None, "FROM_YAML", "Composite fusion artifact"),
    (f"{GN_BASE}/gobernanza/organigrama.yml", None, "FROM_YAML", "No clear single-source document found"),
    (f"{GN_BASE}/gobernanza/plan-potenciamiento-dgi.yml", None, "FROM_YAML", "No clear single-source document found"),
    (f"{GN_BASE}/gobernanza/problemas-sociales-cl.yml", None, "FROM_YAML", "No clear single-source document found"),
    (f"{GN_BASE}/gobernanza/vision-desarrollo-nuble.yml", None, "FROM_YAML", "No clear single-source document found"),
    # guias
    (f"{GN_BASE}/guias/guia-circular-33-sts.yml", None, "FROM_YAML", "Composite from gore_desde_0 instructivo_c33.md"),
    (f"{GN_BASE}/guias/guia-comunicaciones.yml", None, "FROM_YAML", "No clear single-source document found"),
    (f"{GN_BASE}/guias/guia-fril-2025-sts.yml", None, "FROM_YAML", "Composite from gore_desde_0 FRIL docs"),
    (f"{GN_BASE}/guias/guia-frpd-nuble.yml", None, "FROM_YAML", "Composite from gore_desde_0 FRPD docs"),
    (f"{GN_BASE}/guias/guia-idi-sni-sts.yml", None, "FROM_YAML", "Composite from gore_desde_0 IDI/SNI docs"),
    (f"{GN_BASE}/guias/guia-programas-directos-gore.yml", None, "FROM_YAML", "Composite from gore_desde_0 program docs"),
    (f"{GN_BASE}/guias/instructivo-subvencion-8-2025-sts.yml", None, "FROM_YAML", "Composite from gore_desde_0 instructivo docs"),
    # manuales
    (f"{GN_BASE}/manuales/manual-activo-fijo.yml", None, "FROM_YAML", "No clear single-source document found"),
    (f"{GN_BASE}/manuales/manual-asistencia.yml", None, "FROM_YAML", "No clear single-source document found"),
    (f"{GN_BASE}/manuales/manual-bienestar.yml", None, "FROM_YAML", "No clear single-source document found"),
    (f"{GN_BASE}/manuales/manual-ciclo-vida.yml", None, "FROM_YAML", "No clear single-source document found"),
    (f"{GN_BASE}/manuales/manual-compras.yml", None, "FROM_YAML", "No clear single-source document found"),
    (f"{GN_BASE}/manuales/manual-contabilidad.yml", None, "FROM_YAML", "No clear single-source document found"),
    (f"{GN_BASE}/manuales/manual-desarrollo-organizacional.yml", None, "FROM_YAML", "No clear single-source document found"),
    (f"{GN_BASE}/manuales/manual-flotas.yml", None, "FROM_YAML", "No clear single-source document found"),
    (f"{GN_BASE}/manuales/manual-induccion-gore-nuble-2026.yml", None, "FROM_YAML", "No clear single-source document found"),
    (f"{GN_BASE}/manuales/manual-inventarios-bodegas.yml", None, "FROM_YAML", "No clear single-source document found"),
    (f"{GN_BASE}/manuales/manual-operacional-dgi.yml", None, "FROM_YAML", "No clear single-source document found"),
    (f"{GN_BASE}/manuales/manual-presupuesto.yml", None, "FROM_YAML", "No clear single-source document found"),
    (f"{GN_BASE}/manuales/manual-remuneraciones.yml", None, "FROM_YAML", "No clear single-source document found"),
    (f"{GN_BASE}/manuales/manual-tesoreria.yml", None, "FROM_YAML", "No clear single-source document found"),
    # normativa (remaining)
    (f"{GN_BASE}/normativa/dictamenes-cgr-gore.yml", None, "FROM_YAML", "Composite from CGR dictamenes"),
    (f"{GN_BASE}/normativa/ley-presupuestos-2026-normas-generales.yml", None, "FROM_YAML", "Composite from gore_desde_0 budget law docs"),
    (f"{GN_BASE}/normativa/ley-presupuestos-2026-partida-31.yml", None, "FROM_YAML", "Composite from gore_desde_0 budget law docs"),
    (f"{GN_BASE}/normativa/modelos-actos-juridicos.yml", None, "FROM_YAML", "Composite from multiple normative sources"),
    # ris
    (f"{GN_BASE}/ris/ris-artcult.yml", None, "FROM_YAML", "Institutional info system, likely composite"),
    (f"{GN_BASE}/ris/ris-deportes.yml", None, "FROM_YAML", "Institutional info system, likely composite"),
    (f"{GN_BASE}/ris/ris-edpub.yml", None, "FROM_YAML", "Institutional info system, likely composite"),
    (f"{GN_BASE}/ris/ris-empub.yml", None, "FROM_YAML", "Institutional info system, likely composite"),
    (f"{GN_BASE}/ris/ris-index.yml", None, "FROM_YAML", "Institutional info system index, likely composite"),
    (f"{GN_BASE}/ris/ris-patrimonio.yml", None, "FROM_YAML", "Institutional info system, likely composite"),
    (f"{GN_BASE}/ris/ris-pmdt.yml", None, "FROM_YAML", "Institutional info system, likely composite"),
    (f"{GN_BASE}/ris/ris-proginv.yml", None, "FROM_YAML", "Institutional info system, likely composite"),
    (f"{GN_BASE}/ris/ris-proyinv.yml", None, "FROM_YAML", "Institutional info system, likely composite"),
    (f"{GN_BASE}/ris/selector-ipr.yml", None, "FROM_YAML", "Selector/routing artifact"),
]

GN_MAPPINGS = GN_WITH_SOURCE + GN_FROM_YAML

# ---------------------------------------------------------------------------
# FXSL — 24 YMLs + 6 MDs = 30 files total
# ---------------------------------------------------------------------------
FXSL_MAPPINGS = [
    # cat — 23 YMLs
    (
        f"{FXSL_BASE}/cat/seven-sketches.yml",
        None,
        "FROM_SOURCE",
        "Book: Seven Sketches in Compositionality (Fong & Spivak); Zotero academic paper",
    ),
    (f"{FXSL_BASE}/cat/action-primary-key.yml", None, "FROM_SOURCE", "Zotero academic paper"),
    (f"{FXSL_BASE}/cat/algebraic-databases.yml", None, "FROM_SOURCE", "Zotero academic paper"),
    (f"{FXSL_BASE}/cat/algebraic-model-management.yml", None, "FROM_SOURCE", "Zotero academic paper"),
    (f"{FXSL_BASE}/cat/audit-patterns.yml", None, "FROM_SOURCE", "Zotero academic paper"),
    (f"{FXSL_BASE}/cat/categorical-data-structures.yml", None, "FROM_SOURCE", "Zotero academic paper"),
    (f"{FXSL_BASE}/cat/categorical-systems-theory.yml", None, "FROM_SOURCE", "Zotero academic paper"),
    (f"{FXSL_BASE}/cat/coalgebras.yml", None, "FROM_SOURCE", "Zotero academic paper"),
    (f"{FXSL_BASE}/cat/cognitive-toolkit.yml", None, "FROM_SOURCE", "Zotero academic paper"),
    (f"{FXSL_BASE}/cat/constraint-logic.yml", None, "FROM_SOURCE", "Zotero academic paper"),
    (f"{FXSL_BASE}/cat/cql-data-integration.yml", None, "FROM_SOURCE", "Zotero academic paper"),
    (f"{FXSL_BASE}/cat/data-access-layers.yml", None, "FROM_SOURCE", "Zotero academic paper"),
    (f"{FXSL_BASE}/cat/data-lakes-ct.yml", None, "FROM_SOURCE", "Zotero academic paper"),
    (f"{FXSL_BASE}/cat/exploring-category-theoretic-approaches-to-databases.yml", None, "FROM_SOURCE", "Zotero academic paper"),
    (f"{FXSL_BASE}/cat/formal-framework-data-lakes-ct.yml", None, "FROM_SOURCE", "Zotero academic paper"),
    (f"{FXSL_BASE}/cat/formal-framework-multimodel-data-transformations.yml", None, "FROM_SOURCE", "Zotero academic paper"),
    (f"{FXSL_BASE}/cat/kb-category.yml", None, "FROM_SOURCE", "Zotero academic paper; likely fx_ctfp (Category Theory for Programmers)"),
    (f"{FXSL_BASE}/cat/mathematical-modelling.yml", None, "FROM_SOURCE", "Zotero academic paper"),
    (f"{FXSL_BASE}/cat/mbse-consistency.yml", None, "FROM_SOURCE", "Zotero academic paper"),
    (f"{FXSL_BASE}/cat/multicategory-multimodel-query-processing.yml", None, "FROM_SOURCE", "Zotero academic paper"),
    (f"{FXSL_BASE}/cat/schema-evolution.yml", None, "FROM_SOURCE", "Zotero academic paper"),
    (f"{FXSL_BASE}/cat/unified-multimodel.yml", None, "FROM_SOURCE", "Zotero academic paper"),
    (f"{FXSL_BASE}/cat/unified-representation-transformation-multimodel.yml", None, "FROM_SOURCE", "Zotero academic paper"),
    # gist — 1 YAML + 4 MDs
    (f"{FXSL_BASE}/gist/fx-guide-onto-gist-001-audit-protocol.yml", None, "FROM_YAML", "Already in YAML format"),
    (f"{FXSL_BASE}/gist/fx-address-guidance.md", None, "FROM_YAML", "Already in markdown format"),
    (f"{FXSL_BASE}/gist/fx-namespace.md", None, "FROM_YAML", "Already in markdown format"),
    (f"{FXSL_BASE}/gist/fx-readme.md", None, "FROM_YAML", "Already in markdown format"),
    (f"{FXSL_BASE}/gist/fx-uom-model.md", None, "FROM_YAML", "Already in markdown format"),
    # mbt — 2 MDs
    (f"{FXSL_BASE}/mbt/fx-rules.md", None, "FROM_YAML", "Already in markdown format"),
    (f"{FXSL_BASE}/mbt/fx-tensiones.md", None, "FROM_YAML", "Already in markdown format"),
]

# ---------------------------------------------------------------------------
# Legal — 21 KBs
# ---------------------------------------------------------------------------
LEGAL_MAPPINGS = [
    (
        f"{LEGAL_BASE}/legislacion_ia_chile.yml",
        w("RegulaciónLeyes_y_Reglamentos", "Ley_Nº_21658.md"),
        "FROM_SOURCE",
        "Ley 21.658 from wikiguias corpus",
    ),
    (
        f"{LEGAL_BASE}/ley_21658_segdig.yml",
        w("RegulaciónLeyes_y_Reglamentos", "Ley_Nº_21658.md"),
        "FROM_SOURCE",
        None,
    ),
    (f"{LEGAL_BASE}/ley_21719_datos_personales.yml", None, "FROM_YAML", "Composite from multiple legal sources"),
    (f"{LEGAL_BASE}/ley_15076.yml", None, "FROM_YAML", "Specific medical law, no corpus match"),
    (f"{LEGAL_BASE}/ley_19664.yml", None, "FROM_YAML", "Specific medical law, no corpus match"),
    (f"{LEGAL_BASE}/ley_21643.yml", None, "FROM_YAML", "Specific labor law, no corpus match"),
    (f"{LEGAL_BASE}/acoso_laboral.yml", None, "FROM_YAML", "Composite from multiple legal sources"),
    (f"{LEGAL_BASE}/confianza_legitima.yml", None, "FROM_YAML", "Composite from multiple legal sources"),
    (f"{LEGAL_BASE}/contratacion_publica.yml", None, "FROM_YAML", "Composite from multiple legal sources"),
    (f"{LEGAL_BASE}/deberes_prohibiciones.yml", None, "FROM_YAML", "Composite from multiple legal sources"),
    (f"{LEGAL_BASE}/derechos_especiales.yml", None, "FROM_YAML", "Composite from multiple legal sources"),
    (f"{LEGAL_BASE}/feriados_permisos.yml", None, "FROM_YAML", "Composite from multiple legal sources"),
    (f"{LEGAL_BASE}/formacion_especialistas.yml", None, "FROM_YAML", "Composite from multiple legal sources"),
    (f"{LEGAL_BASE}/index.yml", None, "FROM_YAML", "Index artifact"),
    (f"{LEGAL_BASE}/ingreso_carrera.yml", None, "FROM_YAML", "Composite from multiple legal sources"),
    (f"{LEGAL_BASE}/intro_estatutos.yml", None, "FROM_YAML", "Composite from multiple legal sources"),
    (f"{LEGAL_BASE}/jornada_calificaciones.yml", None, "FROM_YAML", "Composite from multiple legal sources"),
    (f"{LEGAL_BASE}/maternidad.yml", None, "FROM_YAML", "Composite from multiple legal sources"),
    (f"{LEGAL_BASE}/remuneraciones.yml", None, "FROM_YAML", "Composite from multiple legal sources"),
    (f"{LEGAL_BASE}/responsabilidad_admin.yml", None, "FROM_YAML", "Composite from multiple legal sources"),
    (f"{LEGAL_BASE}/terminacion.yml", None, "FROM_YAML", "Composite from multiple legal sources"),
]

# ---------------------------------------------------------------------------
# Gov — 9 KBs
# ---------------------------------------------------------------------------
GOV_MAPPINGS = [
    (
        f"{GOV_BASE}/cloud_publica.yml",
        w("Lineamientos_TécnicosGuías", "Recomendaciones_Técnicas_para_la_adquisición_de_servicios_de_Cloud_Pública_en_los_Órganos_de_la_Administración_del_Estado.md"),
        "FROM_SOURCE",
        None,
    ),
    (
        f"{GOV_BASE}/capacitaciones_tde.yml",
        w("EstrategiasEstrategias", "Estrategia_de_capacitaciones_para_la_Transformación_Digital_del_Estado.md"),
        "FROM_SOURCE",
        None,
    ),
    (
        f"{GOV_BASE}/datos_administracion_estado.yml",
        w("EstrategiasEstrategias", "Estrategia_de_Datos_de_la_Administración_del_Estado.md"),
        "FROM_SOURCE",
        None,
    ),
    (
        f"{GOV_BASE}/identidad_digital.yml",
        w("EstrategiasEstrategias", "Estrategia_de_identidad_digital.md"),
        "FROM_SOURCE",
        None,
    ),
    (f"{GOV_BASE}/datosgob.yml", None, "FROM_YAML", "No clear single-source document found"),
    (f"{GOV_BASE}/intro_tde.yml", None, "FROM_YAML", "Composite introductory artifact"),
    (f"{GOV_BASE}/lexicon_wikiguias.yml", None, "FROM_YAML", "Composite lexicon artifact"),
    (
        f"{GOV_BASE}/metodologia_proyectos_tic.yml",
        w("Lineamientos_TécnicosGuías", "Metodología_para_la_gestión_de_proyectos.md"),
        "FROM_SOURCE",
        None,
    ),
    (f"{GOV_BASE}/notificaciones.yml", None, "FROM_YAML", "Composite from multiple notification platform sources"),
]

# ---------------------------------------------------------------------------
# Orko — 8 KBs
# ---------------------------------------------------------------------------
ORKO_MAPPINGS = [
    (f"{ORKO_BASE}/impl-orko-toolkit.yml", None, "FROM_YAML", "Expansion deferred per plan"),
    (f"{ORKO_BASE}/orko-arquitectura.yml", None, "FROM_YAML", "Expansion deferred per plan"),
    (f"{ORKO_BASE}/orko-fases.yml", None, "FROM_YAML", "Expansion deferred per plan"),
    (f"{ORKO_BASE}/orko-fundamentos.yml", None, "FROM_YAML", "Expansion deferred per plan"),
    (f"{ORKO_BASE}/orko-metodologia.yml", None, "FROM_YAML", "Expansion deferred per plan"),
    (f"{ORKO_BASE}/orko-playbooks.yml", None, "FROM_YAML", "Expansion deferred per plan"),
    (f"{ORKO_BASE}/orko-tejidos.yml", None, "FROM_YAML", "Expansion deferred per plan"),
    (f"{ORKO_BASE}/orko-toolkit.yml", None, "FROM_YAML", "Expansion deferred per plan"),
]

# ---------------------------------------------------------------------------
# Mgmt — 4 KBs
# ---------------------------------------------------------------------------
MGMT_MAPPINGS = [
    (
        f"{MGMT_BASE}/estructura-estado-chile.yml",
        p("fx_estructura_administracion_estado_chile.txt"),
        "FROM_SOURCE",
        None,
    ),
    (
        f"{MGMT_BASE}/mw-waissbluth.yml",
        p("fx_weisbluth_manual_coordinacion_estrategica_sector_publico_2024.txt"),
        "FROM_SOURCE",
        None,
    ),
    (f"{MGMT_BASE}/lean6.yml", None, "FROM_YAML", "No clear single-source document found"),
    (f"{MGMT_BASE}/meyer-org-structure.yml", None, "FROM_YAML", "No clear single-source document found"),
]

# ---------------------------------------------------------------------------
# Kora — 30 files (27 MDs + 3 YAMLs)
# ---------------------------------------------------------------------------
KORA_MANUAL_MDS = [
    "00-fundamentos-previos.md",
    "00-toc.md",
    "01-arquitectura-gateway.md",
    "02-agente-unidad-fundamental.md",
    "03-sesiones.md",
    "04-modelos-failover.md",
    "05-memoria.md",
    "06-multi-agent-routing.md",
    "07-aislamiento-seguridad.md",
    "08-patrones-multitenant.md",
    "09-sub-agentes.md",
    "10-sub-agentes-anidados.md",
    "11-comunicacion-inter-sesion.md",
    "12-heartbeats.md",
    "13-cron-jobs.md",
    "14-cron-vs-heartbeat.md",
    "15-hooks.md",
    "16-webhooks.md",
    "17-lobster.md",
    "18-modelo-seguridad.md",
    "19-operaciones.md",
    "20-patrones-diseno.md",
    "21-decisiones-arquitectura.md",
    "22-multi-gateway-docker-federation.md",
    "apendices.md",
    "CHEATSHEET.md",
    "README.md",
]

KORA_MAPPINGS = [
    (f"{KORA_BASE}/manual-openclaw/{f}", None, "FROM_YAML", "Already in final markdown format")
    for f in KORA_MANUAL_MDS
] + [
    (f"{KORA_BASE}/sys/hub_agentes.yml", None, "FROM_YAML", "System configuration artifact"),
    (f"{KORA_BASE}/sys/test_strategy.yml", None, "FROM_YAML", "System configuration artifact"),
    (f"{KORA_BASE}/sys/workflow_wikiguias.yml", None, "FROM_YAML", "System configuration artifact"),
]


# ---------------------------------------------------------------------------
# Assemble all mappings
# ---------------------------------------------------------------------------
ALL_MAPPINGS = {
    "tde": TDE_MAPPINGS,
    "gn": GN_MAPPINGS,
    "fxsl": FXSL_MAPPINGS,
    "legal": LEGAL_MAPPINGS,
    "gov": GOV_MAPPINGS,
    "orko": ORKO_MAPPINGS,
    "mgmt": MGMT_MAPPINGS,
    "kora": KORA_MAPPINGS,
}


def validate_sources(mappings_dict):
    """Check which source paths actually exist on disk."""
    missing = []
    for ns, entries in mappings_dict.items():
        for kb, source, strategy, notes in entries:
            if source is not None and not file_exists(source):
                missing.append((ns, kb, source))
    return missing


def count_strategies(mappings_dict):
    counts = {"FROM_SOURCE": 0, "FROM_YAML": 0}
    for entries in mappings_dict.values():
        for _, _, strategy, _ in entries:
            counts[strategy] = counts.get(strategy, 0) + 1
    return counts


def yaml_str(value):
    """Return a YAML-safe quoted string or null."""
    if value is None:
        return "null"
    # Escape double quotes in value
    escaped = value.replace('"', '\\"')
    return f'"{escaped}"'


def write_output(mappings_dict, output_path, strategy_counts, total):
    lines = []
    lines.append("# Source Mapping — KORA Phase 1")
    lines.append("# Generated: 2026-02-24")
    lines.append(f"# Total KBs: {total}")
    from_source = strategy_counts.get("FROM_SOURCE", 0)
    from_yaml = strategy_counts.get("FROM_YAML", 0)
    lines.append(f"# Strategy counts: FROM_SOURCE: {from_source}, FROM_YAML: {from_yaml}")
    lines.append("")
    lines.append("mappings:")

    namespace_order = ["gn", "tde", "fxsl", "legal", "gov", "orko", "mgmt", "kora"]

    for ns in namespace_order:
        entries = mappings_dict.get(ns, [])
        if not entries:
            continue
        lines.append(f"  {ns}:")
        for kb, source, strategy, notes in entries:
            lines.append(f"    - kb: {kb}")
            if source is None:
                lines.append(f"      source: null")
            else:
                lines.append(f"      source: {yaml_str(source)}")
            lines.append(f"      strategy: {strategy}")
            if notes:
                escaped_notes = notes.replace('"', '\\"')
                lines.append(f'      notes: "{escaped_notes}"')
        lines.append("")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main():
    print("KORA Source Mapper — Phase 1")
    print(f"Knowledge root: {KNOWLEDGE_ROOT}")
    print()

    # Validate source paths
    missing = validate_sources(ALL_MAPPINGS)
    if missing:
        print(f"WARNING: {len(missing)} source file(s) not found on disk:")
        for ns, kb, src in missing:
            print(f"  [{ns}] {kb}")
            print(f"       -> {src}")
        print()
    else:
        print("All FROM_SOURCE paths verified on disk.")
        print()

    # Count totals
    total = sum(len(v) for v in ALL_MAPPINGS.values())
    counts = count_strategies(ALL_MAPPINGS)

    print(f"Total entries: {total}")
    print(f"  FROM_SOURCE: {counts.get('FROM_SOURCE', 0)}")
    print(f"  FROM_YAML:   {counts.get('FROM_YAML', 0)}")
    print()

    # Count by namespace
    for ns in ["gn", "tde", "fxsl", "legal", "gov", "orko", "mgmt", "kora"]:
        entries = ALL_MAPPINGS.get(ns, [])
        ns_from_source = sum(1 for _, _, s, _ in entries if s == "FROM_SOURCE")
        ns_from_yaml = sum(1 for _, _, s, _ in entries if s == "FROM_YAML")
        print(f"  {ns:8s}: {len(entries):3d} entries  (FROM_SOURCE={ns_from_source}, FROM_YAML={ns_from_yaml})")

    print()
    write_output(ALL_MAPPINGS, OUTPUT_FILE, counts, total)
    print(f"Output written to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
