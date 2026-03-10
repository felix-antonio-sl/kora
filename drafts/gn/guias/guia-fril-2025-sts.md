---
_manifest:
  urn: urn:gn:kb:guia-fril-2025-sts
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-09'
    source: domains/gn/03_operacion/ipr/kb_gn_026_guia_fril_koda.yml
version: 2.0.0
status: draft
tags:
- gore-nuble
- gobierno-regional
- fril
- infraestructura
- inversion-publica
- gn
lang: es
extensions:
  gn:
    source_paths:
    - domains/gn/03_operacion/ipr/kb_gn_026_guia_fril_koda.yml
    source_hashes:
      domains/gn/03_operacion/ipr/kb_gn_026_guia_fril_koda.yml: 3aca0ba1ca44ad48be392f8c310805f0410020dcd31808b08db83934122ed97e
    source_type: koda_yaml
    transformation_mode: korafy_direct
    fs: 100
    cr: 2.38
    run_id: gn-smoke
    review_gate: auto
    scope_statement: null
    dependencies: []
    expected_sections:
    - Contenido
    document_family: generic
    publication_class: knowledge
    skeleton_count: 4
    meat_count: 798
    fat_count: 0
    evidence_path: build/gn-rebuild/gn-smoke/evidence/guias__guia-fril-2025-sts.md.json
  kora:
    shard_index: 1
    shard_count: 7
    shard_root_urn: urn:gn:kb:guia-fril-2025-sts
---

# Instructivo FRIL 2025 – Región de Ñuble

## Source
- **Contexto requerido:** Guía Operativa FRIL – Resolución Exenta N° 15.051/2023 SUBDERE, Ley N° 21.796 – Ley de Presupuestos del Sector Público 2026 (Glosa 12, Programa 02, Subtítulo 33), DFL 1-19.175 – Ley Orgánica Constitucional de Gobierno y Administración Regional (LOC GORE), Ley N° 18.575 – Bases Generales de la Administración del Estado, Ley N° 19.880 – Bases de los Procedimientos Administrativos, Ley N° 21.074 – Fortalecimiento de la Regionalización, Circular N° 11/2025 del Ministerio de Hacienda (Glosas GORE), Resolución N° 36/2024 de la Contraloría General de la República (Exención Toma de Razón)

## Glosario FRIL Conceptos Clave
- **Proposito:** Definir conceptos, siglas y actores clave utilizados en el instructivo FRIL 2025.
### Terminos
| ID | Sigla | Cpt | Def |
| --- | --- | --- | --- |
| GN-FRIL-GLOS-FNDR | FNDR | Fondo Nacional de Desarrollo Regional | Principal fuente de financiamiento de la inversión regional administrada por los Gobiernos Regionales. |
| GN-FRIL-GLOS-FRIL | FRIL | Fondo Regional de Iniciativa Local | Fondo FNDR destinado a proyectos de infraestructura comunal de menor escala, ejecutados principalmente por municipalidades. |
| GN-FRIL-GLOS-GORE | GORE | Gobierno Regional | Institución descentralizada, con personalidad jurídica y patrimonio propio, a cargo de la administración superior de la región. |
| GN-FRIL-GLOS-CORE | CORE | Consejo Regional | Órgano colegiado del GORE con facultades normativas, resolutivas y fiscalizadoras; aprueba instructivos y marcos de asignación FRIL. |
| GN-FRIL-GLOS-SUBDERE | SUBDERE | Subsecretaría de Desarrollo Regional y Administrativo | Organismo del Ministerio del Interior que emite la Guía Operativa FRIL y visa metodologías regionales de evaluación. |
| GN-FRIL-GLOS-MDSF | MDSF | Ministerio de Desarrollo Social y Familia | Responsable de la evaluación técnico-económica de iniciativas de inversión en el SNI. |
| GN-FRIL-GLOS-BIP | BIP | Banco Integrado de Proyectos | Plataforma del SNI para registro, evaluación y seguimiento de iniciativas de inversión, incluyendo proyectos FRIL. |
| GN-FRIL-GLOS-GESDOC | GESDOC | Sistema de Gestión Documental del GORE | Plataforma electrónica para el registro de oficios, resoluciones y anexos asociados a proyectos FRIL. |
| GN-FRIL-GLOS-RS | RS | Recomendado Satisfactoriamente | Resultado de evaluación técnica-económica que acredita que la iniciativa cumple requisitos normativos y de admisibilidad. |
| GN-FRIL-GLOS-IDI | IDI | Iniciativa de Inversión | Unidad de análisis del SNI que agrupa estudios, proyectos y programas de inversión pública. |
| GN-FRIL-GLOS-BNUP | BNUP | Bien Nacional de Uso Público | Terreno o espacio de dominio público destinado al uso de toda la comunidad (calles, plazas, áreas verdes, etc.). |
| GN-FRIL-GLOS-ITO | ITO | Inspector Técnico de Obra | Profesional responsable de supervisar técnicamente la ejecución de la obra financiada con FRIL. |

## Normativa FRIL Clave
- **Proposito:** Registrar las normas principales usadas como fundamento del instructivo FRIL 2025.
### Normas
| ID | Cpt | Def |
| --- | --- | --- |
| GN-FRIL-NORM-CPR-01 | Constitución Política de la República | Norma suprema del ordenamiento jurídico chileno; establece organización del Estado y principios de probidad, responsabilidad y control. |
| GN-FRIL-NORM-LOC-GORE-01 | Ley N° 19.175 (LOC GORE) | Ley Orgánica Constitucional sobre Gobierno y Administración Regional, texto refundido en DFL 1-19.175. |
| GN-FRIL-NORM-LEY-18575-01 | Ley N° 18.575 | Ley Orgánica Constitucional de Bases Generales de la Administración del Estado. |
| GN-FRIL-NORM-LEY-19880-01 | Ley N° 19.880 | Establece Bases de los Procedimientos Administrativos. |
| GN-FRIL-NORM-LEY-21796-01 | Ley N° 21.796 – Presupuesto 2026 | Ley de Presupuestos del Sector Público para el año 2026; incluye Glosa 12 de FNDR para FRIL. |
| GN-FRIL-NORM-LEY-21074-01 | Ley N° 21.074 | Ley de Fortalecimiento de la Regionalización del País. |
| GN-FRIL-NORM-DL575-01 | Decreto Ley N° 575 – Regionalización del País | Norma que establece principios y reglas de regionalización y FNDR. |
| GN-FRIL-NORM-RES36-CGR-2024-01 | Resolución N° 36/2024 CGR | Fija normas sobre exención del trámite de Toma de Razón para ciertos actos administrativos. |
| GN-FRIL-NORM-CIRC11-HACIENDA-2025-01 | Circular N° 11/2025 Ministerio de Hacienda | Imparte instrucciones sobre aplicación de glosas presupuestarias de Gobiernos Regionales. |
| GN-FRIL-NORM-RES15051-SUBDERE-2023-01 | Resolución Exenta N° 15.051/2023 SUBDERE | Fija Guía Operativa FRIL a nivel nacional. |

## Instructivo FRIL 2025
- **Titulo:** Instructivo FRIL 2025 – Región de Ñuble
- **Proposito:** Establecer reglas, requisitos, procesos y documentación para la formulación,
evaluación, adjudicación, ejecución y rendición de proyectos FRIL financiados
con recursos FNDR del GORE Ñuble durante el año presupuestario 2025.

- **Destinatarios:** Municipalidades de la Región de Ñuble., Equipos técnicos de SECPLA y DOM comunales., Equipos de la División de Presupuesto e Inversión Regional (DIPIR)., Equipos de la División de Desarrollo Social y Humano, Infraestructura y otras divisiones del GORE vinculadas a FRIL.
- **Alcance:** Aplica a iniciativas FRIL 2025 financiadas con cargo a Subtítulo 33 FNDR., Complementa y particulariza la Guía Operativa FRIL emitida por SUBDERE., Vigente mientras no existan modificaciones relevantes en Ley de Presupuestos o normativa relacionada.

## Estructura Secciones
| ID | Cpt |
| --- | --- |
| GN-FRIL-SEC-1-RESOLUCION | Resolución Exenta que aprueba el instructivo FRIL 2025. |
| GN-FRIL-SEC-2-INTRO | Introducción, objetivos del programa y marco legal. |
| GN-FRIL-SEC-3-MONTO-MARCO | Montos máximos/mínimos, marco por comuna y prioridades. |
| GN-FRIL-SEC-4-LINEAMIENTOS | Lineamientos de postulación, categorías y reglas especiales. |
| GN-FRIL-SEC-5-PROHIBICIONES | Prohibiciones y restricciones a la postulación. |
| GN-FRIL-SEC-6-TERRENOS | Situaciones especiales de terrenos y documentación legal. |
| GN-FRIL-SEC-7-PLAZOS | Períodos y plazos de difusión, postulación, evaluación y asesoría. |
| GN-FRIL-SEC-8-PROCESO | Etapas y procesos: ingreso, admisibilidad, revisión y resultados. |
| GN-FRIL-SEC-9-DOC-POSTULACION | Documentación requerida para la postulación (checklist). |
| GN-FRIL-SEC-10-OTRAS-CONSID | Otras consideraciones de postulación y autorizaciones. |
| GN-FRIL-SEC-11-REEVALUACIONES | Reglas para reevaluaciones de proyectos FRIL. |
| GN-FRIL-SEC-12-TRANSFERENCIAS | Transferencia de recursos, convenios y flujos de pago. |
| GN-FRIL-SEC-13-EJECUCION | Ejecución, licitación, adjudicación, contratación y garantías. |
| GN-FRIL-SEC-14-RENDICIONES-INFORMES | Rendiciones, informes y proyectos sin adjudicación. |
| GN-FRIL-SEC-15-MODIFICACIONES-TERMINO | Modificaciones de contrato, término de proyecto y vigencia del instructivo. |
| GN-FRIL-SEC-16-ANEXOS | Anexos operativos: checklist, planillas tipo y certificados. |

## Sec 1 Resolucion Exenta
### Encabezado
- **Cpt:** Resolución Exenta que aprueba instructivo FRIL 2025.
- **Numero:** 4A/00894/16.05.2025
- **Proposito:** Aprobar instructivo para formulación y evaluación de iniciativas FRIL, año presupuestario 2025.
### Vistos
- **Cpt:** Marco normativo que sustenta la resolución.
### Fundamento
| Ref |
| --- |
| GN-FRIL-NORM-CPR-01 |
| GN-FRIL-NORM-LOC-GORE-01 |
| GN-FRIL-NORM-LEY-21074-01 |
| GN-FRIL-NORM-LEY-18575-01 |
| GN-FRIL-NORM-LEY-21796-01 |
| GN-FRIL-NORM-LEY-19880-01 |
| GN-FRIL-NORM-DL575-01 |
| GN-FRIL-NORM-RES36-CGR-2024-01 |
| GN-FRIL-NORM-CIRC11-HACIENDA-2025-01 |
| GN-FRIL-NORM-RES15051-SUBDERE-2023-01 |
| |
| |
### Considerandos
- **Cpt:** Razones que justifican la emisión del instructivo FRIL 2025.
- **Just:** El presupuesto de Inversión Regional es instrumento fundamental para el desarrollo social, cultural y económico regional., Acuerdo del CORE para aprobar el Instructivo del Fondo Regional de Iniciativa Local (FRIL) 2025 (Sesión N°158, 09/04/2025, Certificado N°1177/2025)., Visación de la metodología de evaluación FRIL por parte de SUBDERE (Oficio N°1667/2025)., Acuerdo del CORE para modificar el plazo de postulación de proyectos FRIL 2025 (Sesión N°86, 14/05/2025, Certificado N°1198/2025)., Necesidad de orientaciones técnicas y administrativas para optimizar el trabajo con eficiencia y eficacia., Necesidad de unificar normas vigentes para el buen uso de los recursos públicos.
### Vigencia Instructivo
- **Nat:** Indefinida hasta modificación por nueva resolución exenta.
### Resuelvo
- **Acciones:** Aprobar el texto del Instructivo Concurso Postulación FRIL 2025 para financiamiento FNDR., Adjuntar certificados del CORE y oficio de visación de SUBDERE como parte integrante de la resolución., Ordenar la publicación de la resolución e instructivo en el sitio web del GORE Ñuble y en el portal de transparencia activa.

## Sec 2 Introduccion y Marco Programa
### Introduccion Programa FRIL
- **Cpt:** Programa FRIL.
- **Definicion:** Mecanismo de financiamiento para proyectos de inversión en infraestructura comunal de menor escala.
- **Objetivos:** Elevar la calidad de vida de los habitantes de las comunas de la Región de Ñuble (urbano y rural).
- **Mecanismo:** Transferencia de recursos FNDR a municipalidades para ejecución de proyectos.
### Fundamento
| Ref | Ctx |
| --- | --- |
| GN-FRIL-NORM-LEY-21796-01 | Asignación presupuestaria anual en Ley de Presupuestos. |
### Proceso
| Act |
| --- |
| Municipios formulan y presentan iniciativas. |
| GORE evalúa iniciativas según Guía Operativa SUBDERE y lineamientos del instructivo regional. |
| |
### Objetivo Fondo FRIL
- **Objetivos:** Financiar proyectos de infraestructura comunal de menor tamaño que mejoren la calidad de vida de la población, tanto en zonas urbanas
como rurales, priorizando iniciativas con alto impacto social y territorial.

### Acciones Financiables
- Ejecución de infraestructura pública.
- Mantenimiento de infraestructura pública.
- Conservación de infraestructura pública.
| Ctx |
| --- |
| Incluye infraestructura social y deportiva. |
### Fundamento
| Ref | Ctx |
| --- | --- |
| GN-FRIL-NORM-LEY-21796-01 | Glosa 12, Subtítulo 33, Programa 02. |
### Marco Legal Programa
- **Cpt:** Normativa que rige el programa FRIL 2025.
### Fundamento
| Ref |
| --- |
| GN-FRIL-NORM-LOC-GORE-01 |
| GN-FRIL-NORM-LEY-18575-01 |
| GN-FRIL-NORM-LEY-21796-01 |
| GN-FRIL-NORM-RES15051-SUBDERE-2023-01 |
| GN-FRIL-NORM-CIRC11-HACIENDA-2025-01 |

## Sec 3 Monto y Marco a Postular
### Monto Maximo Proyecto
- **Requisitos:** Monto máximo por proyecto: igual o inferior a 4.545 UTM (valorizada al 01.01.2025)., Equivalente aproximado: $306.464.805 CLP.
- **Just:** Se descuenta un 10% del máximo normativo de 5.000 UTM para cubrir posibles aumentos de obra.
### Monto Minimo Proyecto
- **Requisitos:** Monto mínimo por proyecto: $100.000.000 CLP.
### Marco Por Comuna
- **Requisitos:** Postulación habilitada para las 21 comunas de la Región de Ñuble., Cada comuna puede postular hasta 5 iniciativas en el período regular., Monto total máximo a postular por comuna en período regular: M$1.000.000.
### Llamados Extraordinarios
- **Condiciones:** El GORE podrá desarrollar llamados extraordinarios por áreas temáticas o por emergencias.
- **Mecanismo:** Los llamados se informan a las municipalidades por oficio., Requieren resolución exenta previa que defina marco, montos, justificación y plazos.
### Prioridades GORE
- **Rec:** Priorizar proyectos con alto impacto social y territorial., Priorizar proyectos integrados con otras soluciones presentes en el territorio.

## Sec 4 Lineamientos de Postulacion
### Acciones Financiables
- **Cpt:** Obras civiles FRIL.
- **Acciones:** Construcción., Reposición., Mejoramiento., Habilitación., Normalización., Ampliación.
### Categorias Proyecto
- **Requisitos:** Cada proyecto debe definirse en una sola categoría (la más relevante)., Cada comuna debe presentar al menos un proyecto asociado a los ejes regionales de Salud, Seguridad o Reactivación Económica.
### Tabla Categorias
- **Contexto:** Resumen estructurado de categorías y subcategorías del instructivo.
### Grupos
| Cpt |
| --- |
| A - Desarrollo Territorial |
| B - Servicios |
| C - Desarrollo Social y Económico |
| D - Medio Ambiente |
### Reglas Especiales Postulacion
### Excepcion Conteo Proyectos
- **Cpt:** Excepción al máximo de 5 iniciativas por comuna.
- **Condiciones:** Proyectos en categorías A2 (Acceso al Agua) y A3 (Vial) no se contabilizan dentro del máximo de 5 proyectos.
- **Just:** El acceso al agua y el mejoramiento de caminos son fundamentales para el desarrollo regional.
- **Dep:** Aplicación sujeta a disponibilidad de revisión por parte de la unidad revisora FRIL del GORE.
### Proyectos Multiubicacion
- **Condiciones:** Un proyecto puede considerar múltiples ubicaciones dentro de la comuna.
- **Requisitos:** Las ubicaciones deben compartir naturaleza, alcance y objetivo., Debe existir un solo presupuesto y una sola licitación para el conjunto.

## Sec 5 Prohibiciones Postulacion
### Prohibiciones Generales
- **Prohibiciones:** Financiar gastos en personal, bienes y servicios de consumo de municipalidades., Adquirir o reponer activos no financieros que no formen parte de un proyecto de obras civiles., Financiar proyectos de servicios básicos que incluyan instalaciones domiciliarias privadas., Financiar proyectos con fines de lucro., Financiar proyectos por etapas (fraccionamiento de obras)., Financiar dos o más proyectos en un mismo terreno o mismo tramo de BNUP en el mismo año presupuestario., Financiar dos o más proyectos para la misma actividad/uso en un mismo terreno en años distintos, si el primero no está ejecutado totalmente.
### Criterios Terreno y Tramo
- **Cpt:** Definición administrativa de terreno y tramo.
- **Contexto:** El terreno se identifica por el mismo rol de avalúo., El tramo vial se verifica con coordenadas y archivos KMZ, a criterio del GORE.
### Vinculo ERD
- **Prohibiciones:** Postular proyectos que no indiquen su relación con la Estrategia Regional de Desarrollo de Ñuble 2020–2028 en el oficio conductor.
