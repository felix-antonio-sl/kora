---
_manifest:
  urn: urn:gn:kb:selector-ipr-p02
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-10'
    source: domains/gn/03_operacion/ipr/kb_gn_011_selector_ipr_koda.yml
version: 2.0.0
status: draft
tags:
- gore-nuble
- gobierno-regional
- inversion-publica
- financiamiento
- gn
lang: es
extensions:
  gn:
    source_paths:
    - domains/gn/03_operacion/ipr/kb_gn_011_selector_ipr_koda.yml
    source_hashes:
      domains/gn/03_operacion/ipr/kb_gn_011_selector_ipr_koda.yml: 578cc776ec61c76afff987ab3acf43017fdd85346ae42deb18396e79a6321050
    source_type: koda_yaml
    transformation_mode: korafy_direct
    fs: 100
    cr: 1.98
    run_id: gn-smoke
    review_gate: auto
    scope_statement: null
    dependencies: []
    expected_sections:
    - Contenido
    document_family: generic
    publication_class: knowledge
    skeleton_count: 6
    meat_count: 582
    fat_count: 0
    evidence_path: build/gn-rebuild/gn-smoke/evidence/ris__selector-ipr.md.json
  kora:
    shard_index: 2
    shard_count: 2
    shard_root_urn: urn:gn:kb:selector-ipr
---

# Selector de Vías de Financiamiento — IPR GORE Ñuble - Parte 02

## Marco Regulatorio
- **Proposito:** Detallar fundamento jurídico y normativo cada vía financiamiento, establecer jerarquía reglas gobiernan asignación recursos
### Marco Transversal
- **Definicion:** Normas carácter general proveen marco fundamental toda inversión regional
#### Pilares Normativos
#### LOC GORE
- **Nombre:** Ley Orgánica Constitucional Gobiernos Regionales (DFL 1-19.175)
- **Fundamento:** Otorga GORE facultad "Decidir inversión" (Art.16f), "Ejecutar programas regionales" (Art.20k)
- **Requisitos:** Conecta administración fondos (FNDR) con obligación evaluación técnica (Art.75)
#### DL 1263
- **Nombre:** Decreto Ley N°1.263 (Adm. Financiera Estado)
- **Fundamento:** Establece base SNI, exige informe favorable iniciativas inversión (Art.19bis)
- **Referencias:** DEF-SNI, DEF-MDSYF
#### Ley Presupuestos
- **Nombre:** Ley Presupuestos Sector Público (Anual)
- **Fundamento:** Instrumento operativo asigna recursos, establece reglas específicas (Glosas)
- **Referencias:** DEF-FNDR, DEF-FRPD
#### Glosa 03
- **Prohibiciones:** Usar recursos inversión regional para financiar préstamos o gastos en personal o bienes y servicios de consumo de entidades receptoras, ni para constituir/efectuar aportes/comprar sociedades o empresas, salvo autorizaciones expresas en glosas.
- **Contexto:** kb_gn_210_ley_presupuestos_2026_partida_31_koda.yml#GN-LEY-PPTO-2026-P31-GLO-03
#### Normas Generales 2026
- **Nombre:** Ley de Presupuestos 2026 - Normas Generales
- **Fundamento:** Reglas transversales (licitación por umbrales, decretos/transferencias, autorizaciones previas DIPRES).
- **Contexto:** kb_gn_211_ley_presupuestos_2026_normas_generales_koda.yml#GN-LEY-PPTO-2026-ART06, kb_gn_211_ley_presupuestos_2026_normas_generales_koda.yml#GN-LEY-PPTO-2026-ART07, kb_gn_211_ley_presupuestos_2026_normas_generales_koda.yml#GN-LEY-PPTO-2026-ART12
### Base SNI C33
- **Ref Mecanismos:** MEC-SNI-GENERAL, MEC-C33
#### Fundamentos
#### SNI
- **Fuentes:** DL 1.263 Art.19bis, Ley 20.530 (Rol SES/MDSyF)
- **Requisitos:** Evaluación técnico-económica todo proyecto capital
- **Referencias:** DEF-FNDR, DEF-FRPD
#### Circular 33
- **Fuentes:** Acto administrativo MINHAC, Circular N°33/2009
- **Requisitos:** Provee vía simplificada evaluación IPRs específicas
- **Referencias:** DEF-IPR, DEF-ANF
### Base Glosa06 Directa
- **Ref Mecanismo:** MEC-G06-DIRECTA
#### Fundamentos
#### Glosa 06
- **Fuentes:** Ley de Presupuestos 2026 Partida 31 Glosa 06 (GN-LEY-PPTO-2026-P31-GLO-06).
- **Req Habilitacion:** Habilita uso recursos inversión programas ejecución directa
- **Referencias:** DEF-SUBT24, DEF-GORE, RATE-RF, DEF-DIPRES, DEF-SES
- **Req Evaluacion:** Exige RF programas nuevos o reformulados
#### Circular 22
- **Fuentes:** Acto administrativo, Oficio Circular N°22 (o vigente)
- **Ref DIPRES:** DEF-DIPRES
- **Ref RF:** RATE-RF
- **Requisitos:** Detalla procedimiento evaluación ex-ante (Perfil y Diseño) obtener RF
### Base Transferencia Publico
- **Ref Mecanismo:** MEC-TRANSFER-PUB
#### Fundamentos
#### Glosa 06 Letra C
- **Fuentes:** Ley de Presupuestos 2026 Partida 31 Glosa 06 (GN-LEY-PPTO-2026-P31-GLO-06).
- **Requisitos:** Exime explícitamente "transferencias otras entidades públicas y gobierno central" evaluación ex-ante
- **Referencias:** DEF-DIPRES, DEF-SES
- **Contexto:** kb_gn_211_ley_presupuestos_2026_normas_generales_koda.yml#GN-LEY-PPTO-2026-ART24, kb_gn_211_ley_presupuestos_2026_normas_generales_koda.yml#GN-LEY-PPTO-2026-ART25
#### Guia GORE
- **Fuentes:** Documento normativo interno
- **Ref GORE:** DEF-GORE
- **Contexto:** kb_gn_001_guia-transferencia-programas.md
- **Requisitos:** Establece procedimiento postulación, admisibilidad, evaluación técnica/financiera interna reemplaza evaluación Circular 22
### Base FRIL
- **Ref Mecanismo:** MEC-FRIL
#### Fundamentos
#### Glosa 12
- **Fuentes:** Ley de Presupuestos 2026 Partida 31 Glosa 12 (GN-LEY-PPTO-2026-P31-GLO-12).
- **Req Transferencias:** Regula transferencias municipalidades proyectos infraestructura menor
- **Referencias:** DEF-FNDR, ORG-MUNICIPALIDAD, RATE-RS, DEF-UTM
#### Req Exencion
- **Referencias:** FRIL-EXENCION-RS, FRIL-TOPE-COSTO
#### Guia FRIL
- **Fuentes:** Lineamientos operativos detallados SUBDERE
- **Ref SUBDERE:** ORG-SUBDERE
### Base Subvencion 8pct
- **Ref Mecanismo:** MEC-SUBV8
#### Fundamentos
#### Glosa 07
- **Fuentes:** Ley de Presupuestos 2026 Partida 31 Glosa 07 (GN-LEY-PPTO-2026-P31-GLO-07).
- **Req Asignacion:** Regula asignación hasta 8% inversión FNDR subvencionar actividades
- **Req Concurso:** Establece concurso público como regla general asignación
- **Req Exencion:** Exime iniciativas evaluación Glosa 06 y SNI
### Base FRPD
- **Ref Mecanismo:** MEC-FRPD
#### Fundamentos
#### Ley Royalty
- **Fuentes:** Ley N°21.591 (Royalty Minero), ley permanente
- **Requisitos:** Crea FRPD, define propósito exclusivo inversión productiva y desarrollo económico
#### Glosa 13
- **Fuentes:** Ley de Presupuestos 2026 Partida 31 Glosa 13 (GN-LEY-PPTO-2026-P31-GLO-13).
- **Req Operativo:** Norma uso operativo recursos FRPD año
- **Req Transferencia:** Faculta transferencia directa iniciativas seleccionadas CORFO/ANID
#### Resolucion SUBCTCI
- **Fuentes:** Resolución Exenta N°33/2024 MinCiencia y sus modificaciones; Resolución Exenta N°08/2025 Subsecretaría de Economía y sus modificaciones; Decreto N°1699/2025 MH.
- **Requisitos:** Define lineamientos, ámbitos acción, instituciones habilitadas ejecutar fondos FRPD I+D+i

## Procesos Evaluacion
- **Proposito:** Detallar procesos validación técnica/económica IPR debe superar antes obtener financiamiento según vía escogida
### Evaluacion SNI
- **Ref Mecanismos:** MEC-SNI-GENERAL, MEC-FRIL, MEC-C33
#### Proceso General
#### Responsable
- **Referencias:** DEF-MDSYF
#### Objetivo
- **Definicion:** Analizar rentabilidad socioeconómica iniciativa inversión
#### Resultado
- **Definicion:** Recomendación Satisfactoria (RS) o Admisibilidad (AD), "pase" obtener financiamiento
- **Referencias:** RATE-RS, RATE-AD
#### Metodologias
- **Definicion:** Metodologías específicas SNI (ej. VAN, CAE)
#### Plataforma
- **Referencias:** PLAT-BIP
#### Excepciones Vias Simplificadas
#### Exencion FRIL
- **Condiciones:** Proyectos municipales <5.000 UTM
- **Resultados:** No requieren informe favorable MDSyF, pero deben ingresar información necesaria al SNI para control/registro.
- **Referencias:** MEC-FRIL
#### Procedimientos Especiales C33
- **Condiciones:** IPRs Conservación, Estudios Básicos, ANF, Emergencias
- **Resultados:** Utilizan procedimientos evaluación agilizados o simplificados
- **Referencias:** MEC-C33
### Evaluacion Glosa06 Directa
- **Ref Mecanismo:** MEC-G06-DIRECTA
#### Proceso General
#### Responsable
- **Referencias:** DEF-DIPRES, DEF-SES
#### Objetivo
- **Definicion:** Analizar calidad diseño (coherencia, pertinencia) programa nuevo o reformulado
#### Resultado
- **Definicion:** Recomendación Favorable (RF) habilita solicitud recursos
#### Metodologia
- **Definicion:** Marco Lógico
#### Plataforma
- **Definicion:** Formularios Perfil y Diseño
#### Fundamento
- **Referencias:** REG-FND-CIRC22
### Evaluacion Transferencia Publico
- **Ref Mecanismo:** MEC-TRANSFER-PUB
#### Proceso General
#### Fundamento Habilitacion
- **Definicion:** Habilitado exención Glosa 06 letra c
- **Referencias:** REG-FND-GLOSA06-C
#### Responsable
- **Definicion:** Unidades técnicas GORE (Departamento Análisis y Evaluación - DAE, Comité Pertinencia)
#### Objetivo
- **Definicion:** Asegurar pertinencia estratégica y factibilidad técnica/financiera propuesta
#### Proceso 3 Fases
- **Referencias:** REQ-TRANSFER-EVAL-GORE
#### Resultado
- **Definicion:** Emisión Informe Técnico Favorable (ITF) habilita gestión financiamiento
#### Calificaciones Posibles
- **Items:** Recomendado Favorablemente, Recomendado con Observaciones, No Recomendado
#### Warn No RS
- **Definicion:** Resultado NO es Recomendación Satisfactoria (RS) SNI
#### Metodologia
- **Definicion:** Marco Lógico y criterios definidos guía GORE
- **Ref MML:** DEF-MML
#### Plataforma
- **Definicion:** Plataforma postulación GORE (ej. GESDOC)
#### Fuente
- **Contexto:** kb_gn_001_guia-transferencia-programas.md
### Evaluacion Especial Exenta
#### Subvenciones 8pct
- **Referencias:** MEC-SUBV8, REQ-SUBV8-EVAL-COMPETITIVA, SUBV8-RES-EXENCION
#### Iniciativas FRPD
- **Referencias:** MEC-FRPD
- **Proceso:** Pueden tener mecanismos propios concurso o asignación, especialmente si alinean convocatorias CORFO/ANID

## Arbol Decision
- **Proposito:** Proveer secuencia lógica preguntas guiar formulador hacia mecanismo más probable y adecuado
- **Advertencias:** Guía orientación. Decisión final requiere consulta unidades técnicas GORE
### Paso1 Naturaleza IPR
- **Pregunta Guia:** ¿Propósito principal crear/mejorar activo físico o intangible durable ("cosa") o entregar servicio/prestación forma continua?
#### Decisiones
#### Si Activo Durable
- **Resultados:** Ir a Ruta PROYECTOS
- **Referencias:** TREE-RUTA-PROYECTOS
#### Si Servicio Prestacion
- **Resultados:** Ir a Ruta PROGRAMAS
- **Referencias:** TREE-RUTA-PROGRAMAS
### Ruta Proyectos
#### Pregunta 1 Municipal FRIL
- **Pregunta:** ¿Ejecutor Municipalidad, costo <5.000 UTM, proyecto infraestructura?
#### Si Cumple
- **Resultados:** Vía más probable FRIL
- **Referencias:** MEC-FRIL
#### Warn Recordar
- **Referencias:** FRIL-REQ-POSTULACION, FRIL-PROHIB, FRIL-EXENCION-RS, FRIL-REQ-SNI
#### Pregunta 2 Procedimientos Especiales
- **Pregunta:** ¿IPR es Conservación, Estudio Básico, Adquisición Activos Aislada, o Reconstrucción?
#### Si Cumple
- **Resultados:** Vía probable Procedimientos Especiales (Circular 33 / NIP)
- **Referencias:** MEC-C33
#### Warn Verificar
- **Referencias:** EVAL-SNI-EXCEP-C33
#### Pregunta 3 Foco Productivo
- **Pregunta:** ¿IPR foco principal productividad/innovación/competitividad económica, postulada entidad habilitada?
#### Si Cumple
- **Resultados:** Fuente fondos natural FRPD (Capital)
- **Referencias:** MEC-FRPD
#### Warn Recordar
- **Referencias:** REQ-FRPD-EVAL-MULTIFASICA, FRPD-CASO-FOMENTO
#### Pregunta 4 Ninguna Anterior
- **Pregunta:** ¿Ninguna anteriores (ej. construcción hospital, puente)?
#### Si Cumple
- **Resultados:** Vía obligatoria SNI General
- **Referencias:** MEC-SNI-GENERAL
#### Warn Recordar
- **Referencias:** PROC-MADURACION-SNI, PROC-NIVELES-EVAL-SNI
### Ruta Programas
#### Pregunta 1 Organizacion Comunitaria
- **Pregunta:** ¿Ejecutor organización comunitaria o privada sin fines lucro, IPR ajusta líneas Cultura/Deporte/Social?
#### Si Cumple
- **Resultados:** Vía más probable Subvención 8% FNDR (vía concurso)
- **Referencias:** MEC-SUBV8
#### Warn Recordar
- **Referencias:** SUBV8-COND-ASIG-DIR, SUBV8-REQ-CONVENIOS-ART24
#### Pregunta 2 Ejecucion GORE
- **Pregunta:** ¿Ejecutor propio GORE, entregará servicios directamente?
#### Si Cumple
- **Resultados:** Vía obligatoria Ejecución Directa GORE (Glosa 06)
- **Referencias:** MEC-G06-DIRECTA
#### Warn Recordar
- **Referencias:** REQ-G06-MML, REQ-G06-EVAL-BIFASICA, G06-REQ-TOPE-ADM-5PCT
#### Pregunta 3 Entidad Publica
- **Pregunta:** ¿Ejecutor otra entidad pública (Municipio, Servicio Público, U.Estatal)?
#### Si Cumple
- **Resultados:** Vía obligatoria Transferencia Entidad Pública
- **Referencias:** MEC-TRANSFER-PUB
#### Warn Recordar
- **Referencias:** REQ-TRANSFER-EVAL-GORE, TRANSFER-TOPE-PERSONAL, REG-GLOSA-03
#### Pregunta 4 Foco Productivo
- **Pregunta:** ¿IPR foco principal productividad/innovación/competitividad económica, postulada entidad habilitada?
#### Si Cumple
- **Resultados:** Fuente fondos natural FRPD (Programático)
- **Referencias:** MEC-FRPD
#### Warn Recordar
- **Referencias:** REQ-FRPD-EVAL-MULTIFASICA, FRPD-CASO-FOMENTO, FRPD-REQ-PROVISION-33-03, FRPD-REQ-TRANSFER-DIRECTA
### Criterios Validacion Complementarios
#### Alineamiento Estrategico
- **Requisitos:** IPR debe ser coherente Estrategia Regional Desarrollo (ERD) y otros planes regionales
#### Magnitud Complejidad
- **Requisitos:** IPRs gran envergadura y complejidad técnica sugieren robustez (y plazos) SNI General
#### Warn Licitacion Publica
- **Condiciones:** Si el monto supera umbrales de licitación pública obligatoria, ajustar estrategia de compras y plazos: Proyectos/Programas de inversión >1.000 UTM; Estudios Básicos >500 UTM (salvo emergencias según legislación).
- **Contexto:** kb_gn_211_ley_presupuestos_2026_normas_generales_koda.yml#GN-LEY-PPTO-2026-ART06
#### Urgencia
- **Condiciones:** Urgencia calificada puede activar procedimientos emergencia (vía proyectos) o asignaciones directas (vía subvenciones 8%)
- **Contexto:** kb_gn_210_ley_presupuestos_2026_partida_31_koda.yml#GN-LEY-PPTO-2026-P31-GLO-14, kb_gn_210_ley_presupuestos_2026_partida_31_koda.yml#GN-LEY-PPTO-2026-P31-GLO-07
#### Transparencia y Reporting
- **Requisitos:** Considerar obligaciones de publicación y reportes periódicos asociados a Subt. 24/31/33, umbrales (p.ej. 500 UTM) y transferencias del 8% y FRPD, según Ley de Presupuestos vigente.
- **Contexto:** kb_gn_210_ley_presupuestos_2026_partida_31_koda.yml#GN-LEY-PPTO-2026-P31-GLO-16
#### Disponibilidad Presupuestaria
- **Requisitos:** Selección final siempre supeditada disponibilidad fondos línea financiamiento correspondiente
