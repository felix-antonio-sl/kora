---
_manifest:
  urn: urn:gn:kb:gestion-prpto-2026
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-09'
    source: domains/gn/03_operacion/presupuesto/kb_gn_018_gestion_prpto_2026_koda.yml
version: 2.0.0
status: draft
tags:
- gore-nuble
- presupuesto-regional
- gestion-financiera
- ley-21796
- gn
lang: es
extensions:
  gn:
    source_paths:
    - domains/gn/03_operacion/presupuesto/kb_gn_018_gestion_prpto_2026_koda.yml
    source_hashes:
      domains/gn/03_operacion/presupuesto/kb_gn_018_gestion_prpto_2026_koda.yml: db858d287b9d9f249d02768786b20014521ff83e5d678bf3e6f3ff4f25932ba2
    source_type: koda_yaml
    transformation_mode: korafy_direct
    fs: 100
    cr: 1.85
    run_id: gn-smoke
    review_gate: auto
    scope_statement: null
    dependencies: []
    expected_sections:
    - Contenido
    document_family: generic
    publication_class: knowledge
    skeleton_count: 12
    meat_count: 872
    fat_count: 0
    evidence_path: build/gn-rebuild/gn-smoke/evidence/gestion__gestion-prpto-2026.md.json
  kora:
    shard_index: 1
    shard_count: 2
    shard_root_urn: urn:gn:kb:gestion-prpto-2026
---

# Gestión Financiera y Operativa del Presupuesto Regional 2026

## Glosario PPTO Clave
- **Proposito:** Definir conceptos y siglas presupuestarias clave utilizados en la guía.
### Terminos
| ID | Sigla | Nombre | Def |
| --- | --- | --- | --- |
| GN-PPTO-GLOS-GORE | GORE | Gobierno Regional | Entidad pública autónoma, con personalidad jurídica y patrimonio propio, encargada de la administración superior de la región. |
| GN-PPTO-GLOS-CORE | CORE | Consejo Regional | Órgano colegiado del GORE, con facultades normativas, resolutivas y fiscalizadoras. |
| GN-PPTO-GLOS-DAF | DAF | División de Administración y Finanzas | División responsable de la gestión administrativa interna, finanzas, presupuesto de funcionamiento y pagos del GORE. |
| GN-PPTO-GLOS-DIPIR | DIPIR | División de Presupuesto e Inversión Regional | División encargada del presupuesto de inversión, programación y seguimiento de iniciativas de inversión y programas regionales. |
| GN-PPTO-GLOS-DIPRES | DIPRES | Dirección de Presupuestos | Órgano técnico del Ministerio de Hacienda encargado de la formulación, ejecución y control del Presupuesto del Sector Público. |
| GN-PPTO-GLOS-CGR | CGR | Contraloría General de la República | Órgano de control que ejerce control de legalidad previo (Toma de Razón) y posterior sobre actos presupuestarios del GORE. |
| GN-PPTO-GLOS-MDSF | MDSF | Ministerio de Desarrollo Social y Familia | Organismo responsable de la evaluación técnico-económica de iniciativas de inversión en el SNI. |
| GN-PPTO-GLOS-SIGFE | SIGFE | Sistema de Información para la Gestión Financiera del Estado | Sistema contable-presupuestario oficial donde se registra la ejecución del presupuesto del GORE. |
| GN-PPTO-GLOS-BIP | BIP | Banco Integrado de Proyectos | Plataforma del SNI para el registro y seguimiento de iniciativas de inversión pública. |
| GN-PPTO-GLOS-SNI | SNI | Sistema Nacional de Inversiones | Marco y plataforma para la evaluación técnico-económica de proyectos de inversión pública. |
| GN-PPTO-GLOS-FNDR | FNDR | Fondo Nacional de Desarrollo Regional | Principal fuente de financiamiento de la inversión regional administrada por los GORE. |
| GN-PPTO-GLOS-FRIL | FRIL | Fondo Regional de Iniciativa Local | Fondo destinado a proyectos de infraestructura de menor escala, ejecutados principalmente por municipalidades. |
| GN-PPTO-GLOS-FRPD | FRPD | Fondo Regional para la Productividad y el Desarrollo | Fondo financiado con recursos del royalty minero para iniciativas de innovación, competitividad y desarrollo productivo. |
| GN-PPTO-GLOS-ARI | ARI | Anteproyecto Regional de Inversiones | Instrumento de planificación que estima la inversión pública en la región para el año siguiente. |
| GN-PPTO-GLOS-PROPIR | PROPIR | Programa Público de Inversión en la Región | Instrumento que organiza y monitorea el gasto público a ejecutar en la región en el año en curso. |
| GN-PPTO-GLOS-SISREC | SISREC | Sistema de Rendición Electrónica de Cuentas | Plataforma de la Contraloría General de la República para gestionar rendiciones de cuentas de transferencias. |

- **Asunto:** Guía técnico-operativa para gestión completa de presupuesto en GORE.
- **Proposito:** Proveer marco de referencia para la gestión presupuestaria regional en todas sus etapas (formulación -> cierre).
- **Dest:** Jefaturas División Administración y Finanzas (DAF)., Jefaturas División Presupuesto e Inversión Regional (DIPIR)., Equipos técnicos GORE y actores regionales vinculados a la gestión presupuestaria.
- **Referencias:** GN-PPTO-GLOS-GORE, GN-PPTO-GLOS-DAF, GN-PPTO-GLOS-DIPIR

## Contexto y Marco Normativo
- **Proposito:** Establecer propósito, alcance y marco normativo de la guía.
- **Requisitos:** Claridad operativa y precisión técnica para gestión diaria del presupuesto regional.
- **Cpt:** Aborda el ciclo presupuestario completo (formulación, aprobación, ejecución, modificaciones, control, cierre).
- **Fundamento:** D.F.L. N°1-19.175 (LOC GORE)., D.L. N°1.263/1975 (Administración Financiera del Estado)., Ley de Presupuestos del Sector Público (anual, ej. Ley 21.796 para 2026)., Normas DIPRES (oficios circulares, instructivos de ejecución)., Normas Contraloría General de la República (CGR) (resoluciones, instructivos)., Jerarquía normativa: Ley > Decreto > Resolución > Oficio Circular > Instructivo.
- **Referencias:** GN-PPTO-GLOS-GORE, GN-PPTO-GLOS-DIPRES, GN-PPTO-GLOS-CGR, GN-PPTO-GLOS-MDSF
### Cambios Presupuestarios 2025
- **Asunto:** Cambios estructurales en presupuesto GORE desde 2025 (vigentes en 2026).
- **Fuentes:** Oficio Circular N°11 DIPRES 2025 (última versión disponible en corpus).
- **Cpt:** Creación de 16 programas presupuestarios (uno por región) que integran funcionamiento e inversión., Creación de programa especial 'Asociatividad y Planes Especiales' para asociatividad regional, zonas extremas y territorios rezagados.
- **Cause:** Profundización del proceso de descentralización fiscal.
- **Resultados:** Requiere coordinación estrecha DAF-DIPIR para gestionar un solo programa integrado.
- **Contexto:** Mayor oferta programática regional (ejecución directa y transferencias), incluyendo 8% FNDR y programas Glosa 06., Dualidad de gestión: GORE debe administrar simultáneamente el Sistema Nacional de Inversiones (SNI) para proyectos de inversión y la evaluación ex-ante DIPRES/MDSF para programas.
### Ley Presupuestos 2026
- **Proposito:** Referencia normativa base (KODA) para gestión presupuestaria 2026: normas generales + glosas y requerimientos de información de Partida 31.
- **XRef Required:** [Ley de Presupuestos 2026: Normas Generales](urn:gn:kb:ley-presupuestos-2026-normas-generales), [Glosas y Requerimientos de Información GORES 2026](urn:gn:kb:glosas-gores-2026), [Glosas y Requerimientos de Información GORES 2026](urn:gn:kb:glosas-gores-2026)
- **Fuentes:** knowledge/domains/gn/presupuesto/kb_gn_211_ley_presupuestos_2026_normas_generales_koda.yml, knowledge/domains/gn/presupuesto/kb_gn_211_ley_presupuestos_2026_glosas_gores_2026_koda.yml
#### Ley
- **Numero:** 21.796
- **Titulo:** LEY DE PRESUPUESTOS DEL SECTOR PÚBLICO CORRESPONDIENTE AL AÑO 2026
#### Fuente
- **Fuentes:** DIARIO OFICIAL DE LA REPUBLICA DE CHILE
- **Fecha:** Viernes 12 de Diciembre de 2025
- **CVE:** 2741100

## Conceptos Presupuestarios Fundamentales
- **Proposito:** Establecer conceptos básicos del sistema presupuestario chileno que dan contexto a la gestión GORE.
- **Fuentes:** DL N°1.263/1975, Decreto N°854/2004 Hacienda y normativa presupuestaria general.
### Presupuesto Sector Publico
- **Definicion:** Estimación financiera de ingresos y gastos del sector público para un año, que compatibiliza recursos disponibles con metas y objetivos preestablecidos.
- **Fundamento:** Art. 11, DL N°1.263/1975.
- **Nat:** Instrumento de política fiscal que refleja prioridades de gobierno y gestión; conjuga dimensión jurídica (Ley), técnica (clasificadores) y contable (recursos financieros).
### Principios Presupuestarios
- **Asunto:** Principios rectores del presupuesto público.
- **Cpt:** Principio de Universalidad: todos los ingresos y gastos del Estado deben reflejarse en el presupuesto (Art. 4°, DL N°1.263/1975)., Principio de Anualidad: el ejercicio presupuestario coincide con el año calendario (Art. 12, DL N°1.263/1975).
### Clasificadores Presupuestarios
#### Clasificacion Institucional
- **Proposito:** Agrupar presupuestariamente los organismos incluidos en la Ley de Presupuestos.
- **Cpt:** Estructura jerárquica: Partida → Capítulo → Programa.
- **Detalle:** Partida: nivel superior de agrupación (Presidencia, Congreso, Ministerios, Partida 50 Tesoro Público). Ejemplo: Partida 31 - Gobiernos Regionales., Capítulo: subdivisión de la Partida; corresponde a cada organismo con presupuesto directo en la Ley. Ejemplo: un capítulo por cada uno de los 16 GORE., Programa: división presupuestaria del Capítulo, asociada a funciones u objetivos específicos (ej. Programa 01 Funcionamiento, 02 Inversión Regional, 03 Asociatividad y Planes Especiales).
#### Clasificacion Por Objeto
- **Proposito:** Ordenar las transacciones según su origen (ingresos) o destino (gastos).
- **Cpt:** Estructura jerárquica: Subtítulo → Ítem → Asignación → Sub-asignación.
- **Ejemplos:** Subtítulos de gasto: 21 Gastos en Personal, 22 Bienes y Servicios de Consumo, 33 Transferencias de Capital., Subtítulos de ingreso: 08 Otros Ingresos Corrientes, 09 Aporte Fiscal, 15 Saldo Inicial de Caja., Ítem: motivo significativo de ingreso o gasto (ej. Ítem 01 Personal de Planta)., Asignación: motivo específico (ej. Asignación 22.04.001 Materiales de Oficina)., Sub-asignación: desglose más particular (ej. 21.01.001-001 Sueldos Bases).
#### Clasificacion Por Grado Afectacion
- **Proposito:** Registrar y controlar instancias previas al devengo en la ejecución del presupuesto.
- **Objetivos:** Conocer avance en la aplicación de los recursos y la calidad del compromiso fiscal.
- **Etapas:** Preafectación: intenciones de gasto sin obligación a terceros (llamados a licitación, cotizaciones)., Afectación: obligación sujeta a perfeccionamiento (adjudicación, selección de proveedor)., Compromiso Cierto: obligación recíproca formalizada (orden de compra, contrato, nombramiento)., Compromiso Implícito: gasto y devengo ocurren simultáneamente (servicios básicos, peajes).

## Ciclo Presupuestario
- **Referencias:** GN-PPTO-GLOS-GORE, GN-PPTO-GLOS-DAF, GN-PPTO-GLOS-DIPIR, GN-PPTO-GLOS-CORE

## Etapas Generales
- **Proposito:** Describir las etapas del ciclo presupuestario y roles de DAF y DIPIR.
- **Cpt:** Etapas: 1) Formulación, 2) Aprobación / Distribución Inicial, 3) Ejecución, 4) Modificaciones, 5) Control y Seguimiento, 6) Cierre., Rol general DAF: financiero-administrativo., Rol general DIPIR: estratégico-programático de inversión (complementariedad de roles).

## Formulacion
### Rol DIPIR Proyecto Presupuesto
- **Responsables:** DIPIR lidera elaboración del proyecto de presupuesto del GORE.
- **Contexto:** Foco en inversión regional y oferta programática.
- **Cpt Tareas Inversion:** Elaborar proyecto de presupuesto de inversiones., Asesorar al Gobernador en selección de proyectos., Coordinar ARI (Anteproyecto Regional de Inversiones) y PROPIR (Programa de Inversión Regional)., Recopilar iniciativas de servicios públicos (plataforma Chileindica)., Asegurar alineación con la Estrategia Regional de Desarrollo (ERD) y coordinar con DIPLADE.
- **Referencias:** GN-PPTO-GLOS-DIPIR
### Rol DIPIR Oferta Programatica
- **Cpt Tareas:** Diseñar programas públicos ejecutados por el GORE usando Metodología de Marco Lógico., Preparar antecedentes para evaluación ex-ante (DIPRES/MDSF) de programas Glosa 06., Identificar programas nuevos o sustancialmente reformulados que requieren evaluación obligatoria., Coordinar con DIPLADE y otras divisiones técnicas.
- **Fundamento:** Glosa 06 Partida 31 Ley 21.796, Oficio Circular N°22 DIPRES.
- **Referencias:** GN-PPTO-GLOS-DIPIR, GN-PPTO-GLOS-DIPRES, GN-PPTO-GLOS-MDSF
### Rol DAF Proyecciones y Clasificacion
- **Responsables:** DAF aporta información financiera y administrativa a la formulación.
- **Cpt Tareas Funcionamiento:** Proyectar gastos de funcionamiento (Subtítulos 21 y 22) con base en dotación vigente y gastos recurrentes., Cumplir restricciones legales de gasto en personal y viáticos (ej. Art. 04 Ley 21.796).
- **Cpt Tareas Clasificacion:** Verificar correcta aplicación del clasificador presupuestario (Decreto N°854/2004)., Asegurar nivel de detalle adecuado (Subtítulo, Ítem, Asignación), especialmente en transferencias (Subt. 24 y 33)., Respetar principio de legalidad del gasto.
- **Referencias:** GN-PPTO-GLOS-DAF
### Coordinacion DIPIR DAF
- **Responsables:** Responsabilidad compartida entre DIPIR y DAF.
- **Cpt Tareas Glosas:** Identificar y explicitar glosas aplicables (dotaciones, vehículos, viáticos, etc.)., Ejemplo: glosas de la Partida 31 en Ley de Presupuestos 2026.
- **Cpt Tareas Provisiones:** Crear provisiones específicas (ej. FRPD en ítem 33.03, FRIL, provisiones 8% FNDR).
- **Cpt Tareas Justificacion Inversiones:** Justificar técnica y socialmente las inversiones propuestas., Obtener Recomendación Satisfactoria (RS) de MDSF para inclusión en presupuesto (salvo excepciones como FRIL)., Mantener todos los proyectos en SNI con código BIP para formulación y seguimiento físico-financiero.
- **Referencias:** GN-PPTO-GLOS-DIPIR, GN-PPTO-GLOS-DAF, GN-PPTO-GLOS-FNDR, GN-PPTO-GLOS-FRIL, GN-PPTO-GLOS-FRPD, GN-PPTO-GLOS-SNI, GN-PPTO-GLOS-BIP
### Coordinacion ARI PROPIR
- **Asunto:** Coordinación regional del gasto público vía ARI y PROPIR.
- **Fuentes:** Instructivo Coordinación Gasto Público ARI 2026 y PROPIR (año en curso; versión 2025 no disponible en este corpus).
- **Definicion:** ARI: estimación de inversión de GORE, ministerios y servicios para el año siguiente., PROPIR: planificación y seguimiento del gasto público regional del año en curso.
- **Mecanismo:** Ambos se gestionan en plataforma Chileindica (https://www.chileindica.cl).
- **Resp GORE:** Gobernador conduce el proceso (puede delegar en Jefe DIPLADE)., DIPLADE lidera Secretaría Ejecutiva de la Coordinación Regional del Gasto Público (SEREMI y jefes de servicios)., Admisión de iniciativas, fijación de plazos de postulación ARI (máx. primeros 4 meses)., Informe trimestral PROPIR al CORE y envío ARI aprobado a ministerios.
- **Resp Servicios Publicos:** Ingresar iniciativas a Chileindica con desglose comunal, montos, fuente, beneficiarios y alineación con ERD., Informar ejecución financiera mensual PROPIR y comunicar ausencia de inversión cuando aplique.
- **Proc Discrepancias:** Resolución en instancia regional., Si persisten, tratamiento en comisiones técnicas de formulación presupuestaria a nivel central.
- **Referencias:** GN-PPTO-GLOS-ARI, GN-PPTO-GLOS-PROPIR

## Aprobacion y Distribucion Inicial
### Procedimiento Legal
- **Asunto:** Procedimiento legal para aprobación de presupuesto inicial del GORE.
- **Fuentes:** Glosa 01 Partida 31 Ley 21.796; Instructivo CGR Aprobación Presupuesto Inicial (vigente).
- **Proc Fases y Plazos:** Propuesta del Gobernador: presenta distribución inicial al CORE (10 días desde publicación de la Ley)., Aprobación CORE: se pronuncia en 10 días desde recepción., Envío a DIPRES: Gobernador remite acuerdo aprobado en 5 días., Resoluciones DIPRES: elabora resoluciones de presupuesto de funcionamiento e inversión (10 días)., Toma de Razón CGR: 15 días desde recepción (prorrogable por 15).
### Contenido y Requisitos
- **Fuentes:** Instructivo CGR Aprobación Presupuesto Inicial (vigente).
- **Req Generales:** Desagregación según clasificador presupuestario a nivel de Subtítulo e Ítem., Transferencias desagregadas a nivel de Asignación (Subt. 24 y 33)., Clasificaciones coherentes con naturaleza del gasto y receptor (legalidad del gasto)., Equilibrio entre ingresos y gastos; montos coinciden con Ley de Presupuestos., Coherencia entre propuesta Gobernador, acuerdo CORE y resoluciones DIPRES.
- **Req Presupuesto Funcionamiento:** Incluir glosas obligatorias (dotación, vehículos, viáticos, gasto CORE en el extranjero)., Monto del Subtítulo 21 debe coincidir con lo autorizado en glosa específica.
- **Req Presupuesto Inversion:** Incluir arrastres de años anteriores conservando número de asignación y código BIP., Incorporar nuevas iniciativas cumpliendo requisitos de glosas., Para nuevas transferencias a privados: acreditar selección por concurso o causal de excepción y personalidad jurídica vigente., Crear asignación para FRPD en ítem 33.03 y otras provisiones (FRIL, 8% FNDR).
- **Req Acuerdo CORE:** Voluntad del CORE debe ser clara en conceptos y montos y certificada por Secretario Ejecutivo.
### Rol CORE en Aprobacion
- **Acciones:** Propuesta de distribución se somete al CORE para aprobación, modificación o sustitución (Art. 25 LOC GORE).
- **Dln:** 10 días corridos para pronunciarse.
- **Fundamento:** Dictamen E548580/2024 CGR: decisiones informadas, razonadas y alineadas con intereses regionales.
- **Proc Exposicion:** DIPIR expone presupuesto de inversiones., DAF expone presupuesto de funcionamiento., Ambas divisiones responden consultas y ajustan propuesta si corresponde.
### Tramite DIPRES y CGR
- **Acciones:** Gobernador remite distribución aprobada a DIPRES.
- **Dln:** 5 días desde aprobación CORE.
- **Responsables:** DAF prepara oficio conductor y antecedentes.
- **Req Documentos:** Oficio firmado por Gobernador titular o subrogante con acto de delegación., Contacto formal., Acuerdo CORE certificado.
- **Act DIPRES:** Revisar y elaborar resoluciones de presupuesto inicial (10 días)., Subsanar errores materiales y reclasificar ingresos y gastos informando a GORE y CGR.
### ID Resolucion CGR
- **Acciones:** DIPRES remite resoluciones a CGR para Toma de Razón.
- **Nat:** Control previo obligatorio de legalidad.
- **Dln:** 15 días (prorrogable por 15).
- **Contexto:** CGR verifica clasificación presupuestaria, cumplimiento de glosas, conformidad normativa y coincidencia GORE-CORE-DIPRES., Toma de Razón deja acto vigente; Representa rechaza por ilegalidad o formula alcances.
- **Resultados:** DAF carga presupuesto en SIGFE (GORE-FIN-HERRAM-SIGFE-01).

## Ejecucion
### Programacion Ejecucion y Caja
- **Asunto:** Programación de ejecución y de caja.
- **Fuentes:** Instructivo DIPRES Ejecución Presupuestaria (vigente).
- **Cpt:** DIPRES elabora programa de ejecución inicial mensualizado; GORE propone su programa., GORE remite actualizaciones mensuales a más tardar el día 15, detallando aporte fiscal y fuentes., Programa de Caja Mensual se basa en ejecución programada menos saldos disponibles para calcular necesidades de aporte fiscal y evitar recursos ociosos.
- **Referencias:** GN-PPTO-GLOS-GORE, GN-PPTO-GLOS-DIPRES
### Rol DAF en Ejecucion
- **Responsables:** DAF lidera administración financiera diaria.
- **Cpt Gestion Financiera:** Garantizar gasto dentro de montos y clasificaciones autorizadas., Registrar preafectación, compromiso, devengo y pago en SIGFE., Supervisar programación de caja con DIPRES.
- **Cpt Pagos y Contabilidad:** Tramitar órdenes de compra, afectar gastos y realizar pagos (obligatoriamente vía transferencia electrónica, Art. 08 Ley 21.796)., Cumplir normativa de compras públicas y rendición de cuentas., Elaborar informes financieros periódicos para DIPRES., Identificar mensualmente iniciativas de inversión (Subt. 31) por código BIP.
- **Cpt Control Interno:** Resguardar respaldo legal de cada desembolso., Asegurar respeto al destino de fondos según glosas., Certificar disponibilidad presupuestaria y límites legales con coordinación de Unidad de Control.
- **Referencias:** GN-PPTO-GLOS-DAF, GN-PPTO-GLOS-SIGFE, GN-PPTO-GLOS-DIPRES
### Rol DIPIR en Ejecucion
- **Responsables:** DIPIR lidera seguimiento físico y presupuestario de la inversión.
- **Cpt Monitoreo Proyectos:** Revisar avance físico de obras e iniciativas (Subt. 31 y 33)., Detectar atrasos o desviaciones y proponer acciones correctivas., Evaluar cumplimiento de hitos de convenios (trimestral) y preparar informes para instancias externas.
- **Cpt Coord Externa:** Articular con SEREMI, servicios públicos sectoriales y municipios beneficiarios.
- **Cpt Uso Herramientas:** Actualizar estados en BIP y cargar ejecución físico-financiera (primeros 8 días del mes siguiente)., Verificar vigencia técnica (RS) y usar SIGFE para seguimiento financiero., Referencias: GORE-FIN-HERRAM-BIP-01, GORE-FIN-HERRAM-SIGFE-01.
- **Referencias:** GN-PPTO-GLOS-DIPIR, GN-PPTO-GLOS-BIP, GN-PPTO-GLOS-SIGFE, GN-PPTO-GLOS-SNI
### Regla Devengo Por Tipo Transferencia
- **Asunto:** Reglas de devengo diferenciadas según tipo de transferencia.
- **Fuentes:** Minuta CGR-AGORECHI-DIPRES marzo 2025; Dictamen CGR N°E583841/2024.
- **Fundamento:** Momento del devengo varía según receptor y modalidad; impacta metas de ejecución.
- **Casos:** Transferencias extrapresupuestarias (Subt. 24-03, 33-03) a instituciones de la Ley de Presupuestos: devengo al aprobarse la rendición (no al transferir)., Transferencias presupuestarias consolidables o a municipios (Subt. 24-02, 33-02; 24-03, 33-03): regla general, devengo cuando la obligación es exigible (acto o convenio tramitado)., Transferencias a entidades privadas (Subt. 24-01, 33-01): devengo cuando la obligación es exigible conforme al convenio/acto.
- **Referencias:** GN-PPTO-GLOS-CGR
### Coordinacion DAF DIPIR
- **Fundamento:** Comunicación constante DAF-DIPIR es esencial para gestionar modificaciones y ejecución.
- **Ejemplos:** DIPIR informa a DAF proyectos retrasados para evaluar modificación presupuestaria., DAF alerta a DIPIR sobre partidas en agotamiento o riesgo de sobregiro.

## Modificaciones Presupuestarias
### Motivaciones y Plazos
- **Cause:** Reubicar recursos, incorporar nuevos ingresos, ajustar costos o financiar imprevistos.
- **Dln:** Solicitudes a DIPRES hasta 31 de octubre del año (según Instructivo DIPRES de ejecución).
- **Responsables:** DIPIR lidera modificaciones de inversión (reasignar fondos de proyectos retrasados, usar ingresos adicionales)., DAF lidera modificaciones de funcionamiento (suplementar partidas, incorporar Saldo Inicial de Caja).
- **Advertencias:** Evitar solicitudes para regularizar hechos consumados, salvo excedibilidades legales.
### Tipos de Modificacion y Actos
- **Asunto:** Tipología de modificaciones y actos administrativos requeridos.
- **Fuentes:** Oficio Circular N°11 DIPRES 2025 (última versión disponible en corpus).
- **Fundamento:** Naturaleza del acto depende si afecta presupuesto de la Partida 31 o solo el presupuesto interno del GORE.
- **Tipos:** Suplemento Presupuestario: aumenta presupuesto por mayor aporte fiscal; requiere Decreto Supremo DIPRES + Resolución GORE., Incorporación/Reducción de Ingresos Ley: distribución de fondos concursables o de contingencia; requiere Decreto Supremo DIPRES + Resolución GORE., Reasignación Presupuestaria Interna: movimientos entre subtítulos dentro del presupuesto del GORE; solo Resolución GORE., Transferencias a otros organismos (consolidable): reasignación desde FNDR en beneficio de un ministerio; Decreto Supremo DIPRES + Resolución GORE., Financiamiento de emergencias (3%): uso fondo de emergencia; Decreto Supremo DIPRES + Resolución GORE., Creación de iniciativas FRPD: uso de provisión en ítem 33.03; solo Resolución GORE., Incorporación Deuda Flotante: si se financia con SIC basta Resolución GORE; si requiere mayor aporte fiscal, se suma Decreto DIPRES.
### Aprobacion Interna y Excepciones
- **Requisitos:** Modificaciones que alteran presupuesto de inversión requieren acuerdo CORE, salvo excepciones explícitas.
- **Cpt:** Glosa 01 y otros marcos definen casos sin acuerdo CORE (GORE-FIN-MOD-EXCEPCIONES-01).
- **Responsables:** DIPIR prepara propuesta técnica de modificación para CORE., DAF provee respaldo financiero.
### Tramite Externo DIPRES CGR
- **Acciones:** GORE emite resolución de modificación firmada por Gobernador y sujeta a visación DIPRES y Toma de Razón CGR.
- **Proceso:** Visación DIPRES: verifica cumplimiento normativo y devuelve si hay errores., Toma de Razón CGR: revisa fundamento legal., Post-TDR: DAF ajusta presupuesto en SIGFE y DIPIR notifica a unidades ejecutoras.
### Documentos Requeridos
- **Fuentes:** Oficio Circular N°11 DIPRES 2025 (última versión disponible en corpus).
- **Cpt:** Certificado de acuerdo CORE cuando aplica., Minuta explicativa (justificación, origen/destino fondos, glosa habilitante)., Informe favorable MDSF/DIPRES si financia programas directos nuevos., Otros documentos de respaldo (certificados de disponibilidad, convenios, etc.).
### Excepciones sin Acuerdo CORE
- **Asunto:** Casos de modificaciones de inversión sin acuerdo CORE.
- **Fuentes:** Glosa 01 Partida 31 Ley 21.796; Oficio Circular N°11 DIPRES 2025 (última versión disponible en corpus).
- **Cpt Casos:** Aplicación de leyes generales (reajustes, sentencias, deuda flotante)., Regularización de ingresos sin incidencia en gastos., Variaciones de tipo de cambio en activos no financieros., Uso del 3% para emergencias (Glosa 14)., Aumento de costo de proyectos en ejecución hasta 10% del monto RS (tope 7.000 UTM)., Adjudicación de licitaciones con variación hasta 10% sobre RS (tope 7.000 UTM).
- **Advertencias:** Aunque no requieran CORE, sí exigen visación DIPRES, Toma de Razón CGR e información mensual al CORE.
### Detalle Emergencias Glosa14 2026
- **Fundamento:** Glosa 14 Partida 31 (GN-LEY-PPTO-2026-P31-GLO-14).
- **Cpt:** Se podrá traspasar hasta un 3% del presupuesto de inversión aprobado por el Congreso Nacional de cada GORE, a requerimiento de la Subsecretaría del Interior, a asignaciones 24.03.002 y/o 33.03.001 del presupuesto de dicha Subsecretaría para enfrentar situaciones de emergencia., Los GORE podrán destinar hasta un 2% del presupuesto de Inversión Regional aprobado por el Congreso Nacional para enfrentar situaciones de emergencia (todas sus etapas), definidas mediante resolución por el Ministro o Subsecretario del Interior, previa coordinación., La ejecución de estos recursos se podrá efectuar sin esperar la total tramitación del acto administrativo del GORE., Trimestralmente, los GORE informarán a la Comisión Especial Mixta de Presupuestos y a DIPRES sobre el uso de estos recursos.
### Sintesis Roles en Modificaciones
- **Responsables:** DIPIR lidera modificaciones de inversión (racionalidad técnico-programática)., DAF lidera modificaciones de funcionamiento (racionalidad financiero-legal).
- **Cpt:** Trabajo conjunto: DIPIR provee detalle de proyectos, DAF estructura modificación formal.
- **Advertencias:** Antes de enviar, verificar que la modificación no vulnere normas (ej. prohibición de traspasar desde inversión a Subtítulo 22).
### Limites y Flexibilidades TrasPasos
- **Fundamento:** Fondos de inversión no deben utilizarse para financiar gastos corrientes de funcionamiento salvo habilitación legal expresa.
- **Fuentes:** DL N°1.263, Art. 04 Ley 21.796.
### Reglas Claves Glosas
- **Cpt:** Glosa 03: prohíbe usar inversión para préstamos, gasto en personal o bienes y servicios de consumo de entidades receptoras., Glosa 04: permite traspasos entre subtítulos de inversión, excluyendo explícitamente al Subtítulo 22 como receptor., Glosa 01 de Ley de Reajuste: habilita excepcionalmente uso de fondos de inversión para gasto en personal cuando otra ley lo mande., Glosa 06: permite usar hasta 5% del monto del programa para gastos de administración del GORE (Subt. 21, 22, 29) y hasta 5% para honorarios de la entidad receptora., Art. 07 Ley 21.796: refuerza necesidad de habilitación legal expresa para financiar gastos operativos con recursos de transferencia.
### Limites Incremento Gastos 2026
- **Fundamento:** Art. 04 Ley 21.796.
- **Req Gastos Corrientes:** Se requiere autorización legal para incrementar la suma del valor neto de los gastos corrientes.
- **Excepciones Gastos Corrientes:** Ítems legalmente excedibles (art. 28 DL N°1.263/1975)., Glosa 01 Programa Operaciones Complementarias., Mayores saldos iniciales de caja (excepto Partida Tesoro Público)., Venta de activos financieros., Ingresos propios asignables., Recursos de fondos concursables de entes públicos., Art. 21 DL N°1.263/1975.
- **Req Gastos Capital:** Se requiere autorización legal para aumentar en más de 10% la suma aprobada en el Art. 1 de la Ley de Presupuestos para gastos de capital.
- **Excepciones Gastos Capital:** Reasignaciones presupuestarias desde gastos corrientes., Mayores saldos iniciales de caja (excepto Partida Tesoro Público)., Venta de activos., Fondos concursables., Recuperación de anticipos.
### Transferencias Consolidables
- **Definicion:** Transferencias desde un GORE a otras instituciones del Presupuesto del Sector Público para evitar doble contabilización del gasto.
- **Fundamento:** Oficio Circular N°11 DIPRES 2025 (última versión disponible en corpus), Glosa 01 Partida 31, Art. 26 Ley 21.796.
- **Proceso:** GORE solicita formalmente a DIPRES la creación de la transferencia., GORE emite resolución interna con rebaja presupuestaria., Adjunta acuerdo CORE, justificación y aceptación del receptor., DIPRES elabora Decreto Supremo que modifica presupuesto GORE; pasa a CGR para Toma de Razón., Transferencias pueden efectuarse sin convenio formal si se cumple procedimiento presupuestario.
### Ejemplo
- **Asunto:** Ejemplo de flujo para transferencia consolidable desde GORE X al Ministerio de Salud.
- **Contexto:** CORE aprueba; GORE envía oficio a DIPRES; emite resolución de rebaja. DIPRES emite Decreto que crea asignación y reasigna fondos, ajustando tanto presupuesto GORE como del ministerio.

## Control y Seguimiento
### Control Interno GORE
- **Responsables:** Unidad de Control o auditoría interna del GORE.
- **Acciones:** Revisar actos administrativos de contenido financiero (control ex-ante)., Visar resoluciones, verificar respaldos y revisar rendiciones.
- **Requisitos:** DAF colabora para subsanar observaciones.
### Control CGR
- **Responsables:** Contraloría General de la República (CGR).
- **Cpt:** Control previo vía Toma de Razón de resoluciones y decretos presupuestarios., Control posterior mediante auditorías e investigaciones especiales.
- **Requisitos:** DIPIR y DAF deben mantener antecedentes ordenados para fiscalizaciones.
### Seguimiento DIPRES
- **Responsables:** Dirección de Presupuestos (DIPRES).
- **Acciones:** Monitorea ejecución presupuestaria mensual de los GORE mediante informes, reuniones y alertas de baja ejecución.
- **Requisitos:** GORE debe gestionar un calendario de hitos para asegurar cumplimiento.
### Transparencia y Control Social
- **Nat:** Control social sobre inversión regional.
- **Fundamento:** Ley N° 21.796 (Normas Generales) + Requerimientos de información Partida 31 (ver INFO-REQS-2026-GORES-01 en artefacto glosas GORES 2026).
- **Requisitos:** Publicar mensualmente en sitio web del GORE la cartera de proyectos financiados con inversión regional., Publicar acuerdos del CORE en máximo 5 días hábiles., Informar trimestralmente el uso de recursos de inversión regional: listado de beneficiarios, comuna, instituciones receptoras, monto, productos del convenio y su aplicación a nivel regional., Informar y publicar trimestralmente el destino de recursos FNDR a proyectos de desarrollo económico y los proyectos adjudicados por sectores según actividad económica., Publicar trimestralmente e informar a senadores y diputados de la región todos los proyectos adjudicados o contratados con cargo a Subt. 24 (oferta programática) y Subt. 31 y 33, incluyendo nombre del proyecto, monto estimado, postulantes, pauta de evaluación, seleccionado, presupuesto aprobado y votación del CORE., Informar trimestralmente transferencias con cargo al Fondo de Vinculación con la Comunidad (8%): beneficiario, comuna, objeto del financiamiento, montos totales y fecha de cada transferencia., Informar trimestralmente iniciativas y proyectos de inversión que superen 500 UTM: proyecto, antecedentes para aprobación, montos, plazo de ejecución e identidad del receptor de recursos., Informar trimestralmente la disponibilidad presupuestaria para que universidades reconocidas por el Estado accedan a asignaciones directas de recursos FRPD y las solicitudes recibidas., Publicar acuerdos del CORE en máximo 5 días hábiles e información de corporaciones financiadas., Publicar información en formato digital legible y procesable, que no consista solamente en imágenes., Publicar en transparencia activa las actas de evaluación emitidas por comisiones evaluadoras de licitaciones y compras públicas (Ley N°19.886)., Procurar lenguaje claro y vincular el presupuesto a orientaciones estratégicas, objetivos prioritarios y resultados esperados., Publicar de forma permanente en transparencia activa (literal k) art. 7 Ley N°20.285) los montos recibidos y ejecución presupuestaria del FRPD, incluyendo detalle de transferencias efectuadas.
- **Responsables:** DIPIR compila información, DAF valida cifras.
