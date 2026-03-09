---
_manifest:
  urn: urn:gn:kb:flujos-aprobacion-documentos
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-08'
    source: domains/gn/03_operacion/gestion/kb_gn_015_aprobaciones_koda.yml
version: 2.0.0
status: draft
tags:
- gore-nuble
- gobierno-regional
- gestion
- flujos-aprobacion
- inversion-publica
- gn
lang: es
extensions:
  gn:
    source_paths:
    - domains/gn/03_operacion/gestion/kb_gn_015_aprobaciones_koda.yml
    source_hashes:
      domains/gn/03_operacion/gestion/kb_gn_015_aprobaciones_koda.yml: 5751b9f208889c0fa25cf1c292dc97352525eaeabd3267d772a1939b7baafbea
    source_type: koda_yaml
    transformation_mode: korafy_koda_hybrid
    fs: 100
    cr: 1.25
    run_id: gn-smoke
    review_gate: auto
    scope_statement: Flujo de aprobacion documental operativo; revisar compresion
      editorial previa.
    dependencies: []
    expected_sections:
    - Contenido
    skeleton_count: 16
    meat_count: 291
    fat_count: 0
    cr_justification: Fuente altamente estructurada o derivacion de alcance acotado.
    evidence_path: build/gn-rebuild/gn-smoke/evidence/gestion__flujos-aprobacion-documentos.md.json
---

# Flujos de Aprobación de Documentos — GORE Ñuble
## ID
KB-GN-102-FLUJOS-APROBACION-CONTENT-01

## Seccion 2 Principios y Actores del Proceso de Aprobacion
### ID
KB-GN-102-PRINCIPIOS-ACTORES-01
### Purp
Establecer el marco conceptual, jurídico y organizacional que sustenta todos los flujos de aprobación, definiendo los principios rectores y los roles de cada participante.
### Seccion 2 1 Fundamentos Juridico Procedimentales
#### ID
KB-GN-102-FUNDAMENTOS-01
#### Fnd
La totalidad de los flujos de aprobación del Gobierno Regional (GORE) de Ñuble se enmarcan en un estricto conjunto de principios jurídicos que garantizan su legalidad, probidad y eficiencia. La inobservancia de estos fundamentos puede acarrear la nulidad de los actos administrativos.
#### Principios
| Cpt | Def |
| --- | --- |
| Principio de Legalidad | Los órganos de la Administración del Estado, incluyendo el GORE, deben someter su acción a la Constitución y a las leyes, actuando exclusivamente dentro del ámbito de su competencia. Todo acto que exceda estas atribuciones es nulo y puede ser impugnado. |
| Principio de Escrituración Electrónica | La Ley N° 21.180 de Transformación Digital del Estado mandata que todos los procedimientos administrativos se realicen por medios electrónicos. El papel es la excepción. Esto implica que todo flujo de aprobación debe quedar registrado en un expediente electrónico único y accesible. |
| Principio de Impugnabilidad | Todo acto administrativo emanado del GORE es susceptible de ser impugnado a través de los recursos que establece la ley, como el recurso de reposición ante la misma autoridad o el recurso jerárquico, si procede. |
| Principio de Probidad y Transparencia | La función pública debe ejercerse con una conducta funcionaria intachable, anteponiendo siempre el interés general sobre el particular. Asimismo, los procedimientos, contenidos y fundamentos de las decisiones deben ser públicos y accesibles, promoviendo el control ciudadano. |
| Control Externo de Legalidad | La autonomía del GORE para administrar sus asuntos no lo exime del control superior de la Contraloría General de la República (CGR). La CGR fiscaliza la legalidad de los actos, el correcto uso de los fondos y ejerce un control preventivo a través de la Toma de Razón. |
### Seccion 2 2 Matriz de Actores y Responsabilidades Clave
#### ID
KB-GN-102-ACTORES-MATRIZ-01
#### Purp
Definir los roles y responsabilidades de las unidades y autoridades que intervienen en los flujos de aprobación, estableciendo una referencia única para la correcta derivación de documentos y tareas.
#### Fnd
La estructura de gobernanza del GORE se caracteriza por un sistema de control dual y múltiples puntos de veto, donde se separan las funciones ejecutivas (Gobernador), de fiscalización y financiamiento (CORE), y las de gestión técnica (DIPIR/DIPLADE) de las de gestión financiera (DAF). A esto se suman los controles externos obligatorios de CGR, DIPRES y MDSF, que actúan como compuertas indispensables en el proceso.
#### Table
#### Columns
- Actor_Unidad
- Rol_Principal_en_Aprobaciones
- Fuente_Normativa_Contextual
#### Rows
| Actor_Unidad | Rol_Principal_en_Aprobaciones | Fuente_Normativa_Contextual |
| --- | --- | --- |
| Gobernador/a Regional | Act: Firma ejecutiva final de actos adm. \| Act: Propone presupuesto y planes al CORE. \| Cpt: Representación judicial y extrajudicial del GORE. | GORE-GUIA-ESTRUCTURA-GOBERNADOR-01 |
| Consejo Regional (CORE) | Act: Aprueba presupuesto regional, planes de desarrollo (ERD), distribución de fondos (FNDR, 8%, FRIL) y mods. presupuestarias. \| Act: Ejerce fiscalización sobre gestión del Gobernador. | GORE-GUIA-ESTRUCTURA-CORE-01 |
| Administrador/a Regional | Act: Coordina gestión adm. interna. \| Act: Ejerce V°B° final antes de firma del Gobernador. \| Cpt: Subrogancia legal del Gobernador. | GORE-GUIA-ESTRUCTURA-ADM-REGIONAL-01 |
| DAF (Div. de Adm. y Finanzas) | Act: Ejecuta gestión financiera y contable. \| Act: Elabora convenios y resoluciones de pago. \| Act: Controla rendiciones de cuentas. \| Act: Registra operaciones en SIGFE. | KB-GN-CTX-AUTH-01-03, STS-KB-GN-RENDICION-ACTOR-DAF-01 |
| DIPIR (Div. de Presupuesto e Inv. Reg.) | Resp: Lidera formulación y mod. de presupuesto de inversión. \| Act: Evalúa técnicamente las Iniciativas de Inversión (IDI). \| Act: Monitorea avance físico-financiero en BIP. | KB-GN-CTX-AUTH-01-03, GORE-IPR-PHASE1-ENTRY-01 |
| DIPLADE (Div. de Planificación y Desarrollo) | Resp: Lidera elaboración y seguimiento de ERD. \| Resp: Actúa como secretaría ejecutiva en coordinación del gasto (ARI/PROPIR). | KB-GN-CTX-AUTH-01-03, GORE-FIN-FORM-ROL-DIPIR-01 |
| Asesoría Jurídica | Act: Realiza control de legalidad interno de actos y convenios. \| Act: Redacta y revisa borradores de resoluciones y decretos. |  |
| Unidad de Control | Act: Ejerce control preventivo y posterior de legalidad de actos y procedimientos. \| Dep: Dependencia técnica de CGR. \| Act: Audita selectivamente procesos. | STS-KB-GN-RENDICION-ACTOR-CONTROLINTERNO-01 |
| Oficina de Partes | Cpt: Punto único de ingreso formal de documentación externa. \| Act: Asigna número de registro (SGDOC). \| Act: Deriva a unidad competente. | GORE-IPR-PHASE1-RECEPTION-01 |
| Comité Directivo Regional (CDR) | Act: Realiza filtro estratégico y político-técnico de IPR pre-evaluación. \| Cpt: Compuesto por Jefaturas de División y Administrador/a Regional. | GORE-IPR-PHASE1-PERTINENCE-01 |
| Referente Técnico-Financiero (RTF) | Resp: Funcionario de división técnica. \| Act: Actúa como primera línea de revisión y seguimiento de proyecto/programa (técnico y financiero). | STS-KB-GN-RENDICION-ACTOR-RTF-01 |
| SEREMI de Desarrollo Social y Familia | Act: Evalúa técnicamente IDI para otorgar la Recomendación Satisfactoria (RS) o Admisibilidad (AD). \| Req: Indispensable para financiamiento de mayoría de proyectos de inversión. | GORE-IPR-PHASE2-TRACK-SNI-STANDARD-01 |
| Dirección de Presupuestos (DIPRES) | Act: Evalúa ex-ante Programas Públicos Regionales (Glosa 06). \| Act: Elabora resoluciones de presupuesto inicial. \| Act: Visa mods. presupuestarias que afectan Partida 31. | GORE-FIN-CTX-CAMBIOS-2025-01, GORE-IPR-PHASE2-TRACK-GLOSS06-01 |
| Contraloría General de la República (CGR) | Act: Ejerce control preventivo de legalidad (Toma de Razón) sobre actos que comprometen fondos públicos. \| Act: Fiscaliza a posteriori la legalidad de todos los actos adm. del GORE. | LAW-CGR-TOMA-RAZON-01, GORE-FIN-APROB-TRAM-CGR-01 |
### Seccion 2 3 El Expediente Electronico y la Firma Electronica Avanzada FEA
#### ID
KB-GN-102-EXPEDIENTE-FEA-01
#### Purp
Detallar los instrumentos tecnológicos que son pilares del procedimiento administrativo moderno y que garantizan la validez, integridad y trazabilidad de los flujos de aprobación.
#### Conceptos
| Cpt | Def |
| --- | --- |
| Expediente Electrónico | Conforme a la Ley N° 21.180, todo procedimiento debe constar en un expediente electrónico único que contenga el registro de todas las actuaciones, documentos, dictámenes e informes. Este expediente debe ser accesible para los interesados y garantiza la trazabilidad del flujo de aprobación. |
| Firma Electrónica Avanzada (FEA) | Mecanismo que sustituye la firma manuscrita, otorgando plena validez legal a los documentos electrónicos. Las resoluciones y decretos del Gobernador/a Regional, así como otros actos que la normativa especifique, deben ser firmados con FEA para ser válidos y ejecutorios. |

## Seccion 3 Flujos de Aprobacion para Actos Administrativos de Tramitacion General
### ID
KB-GN-102-FLUJOS-GENERALES-01
### Purp
Modelar el flujo de trabajo estándar para la creación y aprobación de actos administrativos que no conllevan una imputación presupuestaria directa, como el nombramiento de comisiones, la aprobación de reglamentos internos o la respuesta a solicitudes ciudadanas. Este flujo sirve como base para procesos más complejos.
### Seccion 3 1 Flujo para Resoluciones Exentas y Decretos Sin Imputacion Presupuestaria Directa
#### ID
KB-GN-102-FLUJO-RES-EXENTA-01
#### Fnd
Este procedimiento se deduce de la aplicación de los principios de la Ley N° 19.880 y la estructura organizacional del GORE. La cadena de aprobación es tanto jerárquica como funcional, asegurando que un acto sea validado por la unidad con competencia técnica, la unidad con supervisión legal y la unidad con control procedimental antes de la firma ejecutiva.
#### Flujo
-
  #### Cpt
  Paso 1: Iniciación y Borrador
  #### Resp
  Unidad GORE competente (ej. DAF, DIDESOH, etc.).
  #### Ref
  KB-GN-102-ACTORES-MATRIZ-01
  #### Act
  La unidad identifica la necesidad y elabora el borrador del acto administrativo (ej. Resolución Exenta), fundamentando debidamente las razones de hecho y de derecho que lo motivan.
-
  #### Cpt
  Paso 2: Revisión Jurídica
  #### Resp
  Asesoría Jurídica.
  #### Ref
  KB-GN-102-ACTORES-MATRIZ-01
  #### Act
  El borrador se remite a la Asesoría Jurídica para un control de legalidad, verificando que el acto se ajuste a la normativa vigente y a las competencias del GORE.
-
  #### Cpt
  Paso 3: Visto Bueno (V°B°) de Control Interno
  #### Resp
  Unidad de Control.
  #### Ref
  KB-GN-102-ACTORES-MATRIZ-01
  #### Act
  La Unidad de Control revisa el borrador para asegurar su conformidad con los procedimientos internos y los principios de buena administración.
-
  #### Cpt
  Paso 4: V°B° de Jefaturas y Administrador/a Regional
  #### Resp
  Jefatura de División iniciadora; Administrador/a Regional.
  #### Ref
  KB-GN-102-ACTORES-MATRIZ-01
  #### Act
  El acto es visado por la jefatura de la división que lo origina. Posteriormente, es revisado y visado por el/la Administrador/a Regional, quien actúa como el último filtro de coordinación administrativa.
-
  #### Cpt
  Paso 5: Firma del Gobernador/a
  #### Resp
  Gobernador/a Regional.
  #### Ref
  - KB-GN-102-ACTORES-MATRIZ-01
  - KB-GN-102-EXPEDIENTE-FEA-01
  #### Act
  Una vez completados todos los V°B° internos, el acto es presentado al Gobernador/a para su firma mediante FEA.
-
  #### Cpt
  Paso 6: Notificación y Archivo
  #### Resp
  Unidad GORE competente; Oficina de Partes.
  #### Ref
  - KB-GN-102-ACTORES-MATRIZ-01
  - KB-GN-102-EXPEDIENTE-FEA-01
  #### Act
  El acto firmado se notifica a los interesados, si los hubiere, y se archiva en el expediente electrónico correspondiente.
-
  #### Cpt
  Control Externo
  #### Resp
  Contraloría General de la República (CGR).
  #### Ref
  KB-GN-102-ACTORES-MATRIZ-01
  #### Ctx
  Por regla general, los actos que no comprometen recursos presupuestarios están exentos del trámite de Toma de Razón previo. Sin embargo, la CGR siempre conserva la facultad de ejercer un control de legalidad posterior sobre ellos.

## Seccion 4 Flujos de Aprobacion para Iniciativas de Inversion IDI y Programas
### ID
KB-GN-102-FLUJOS-INVERSION-01
### Purp
Detallar los flujos de trabajo específicos para la aprobación de iniciativas que implican gasto, los cuales están altamente segmentados según el tipo, monto y naturaleza de la intervención.
### Fnd
El primer paso crítico en este dominio es la correcta clasificación de la iniciativa para determinar la ruta de aprobación correspondiente, aplicando un principio de proporcionalidad en el control.
### Seccion 4 1 Flujo Estandar del Sistema Nacional de Inversiones SNI
#### ID
KB-GN-102-FLUJO-SNI-ESTANDAR-01
#### Fnd
Corresponde al proceso de evaluación para Iniciativas de Inversión (IDI) de mayor complejidad o envergadura que requieren una evaluación técnica y económica completa por parte del Ministerio de Desarrollo Social y Familia (MDSF) para obtener la Recomendación Satisfactoria (RS).
#### Table
#### Columns
- Paso
- Responsable
- Actividades_Clave
- Requisitos_Instrucciones
- Resultado_Entregable
- Ref_Normativa
#### Rows
| Paso | Responsable | Actividades_Clave | Requisitos_Instrucciones | Resultado_Entregable | Ref_Normativa |
| --- | --- | --- | --- | --- | --- |
| 1 | Analista GORE (DIPIR) | Revisión Previa y Preparación | Act: Realizar revisión de fondo. \| Act: Verificar cumplimiento metodologías SNI. \| Act: Elaborar "Acta de Admisibilidad" interna. | IDI ADMISIBLE PARA ENVÍO A MDSF | GORE-IPR-PHASE2-TRACK-SNI-STANDARD-01 |
| 2 | Jefatura DIPIR / Gobernador/a | Envío Formal a MDSF | Act: Elaborar y visar oficio conductor solicitando evaluación ex-ante. \| Cpt: Cadena de V°B° interna culmina con firma del Gobernador/a. | Oficio despachado a SEREMI MDSF. | GORE-IPR-PHASE2-TRACK-SNI-STANDARD-01 |
| 3 | Analista MDSF | Análisis Técnico-Económico (ATE) | Act: MDSF realiza análisis de mérito técnico, económico y social. \| Dln: 5 días para admisibilidad, 10 días para ATE. | RATE: RS (Recomendado Satisfactorio), FI (Observado) u OT (Otro). | GORE-IPR-PHASE2-TRACK-SNI-STANDARD-01 |
| 4 | Unidad Formuladora / Analista GORE | Gestión del Resultado | Cond: Si es RS, avanza a financiamiento. \| Cond: Si es FI u OT, subsanar observaciones. \| Dln: Plazo máx. 60 días hábiles. | IDI con APROBADO TÉCNICAMENTE (RS) | GORE-IPR-PHASE2-TRACK-SNI-STANDARD-01 |
| 5 | Jefatura DIPIR | Priorización para Financiamiento | Act: Monitorear BIP. \| Act: Comunicar cartera de proyectos con RS al Gobernador/a para su priorización y eventual envío al CORE. | Cartera RS disponible para priorización. | GORE-IPR-PHASE2-TRACK-SNI-STANDARD-01 |
### Seccion 4 2 Flujos Simplificados del SNI
#### ID
KB-GN-102-FLUJO-SNI-SIMPLIFICADO-01
#### Fnd
Para iniciativas de menor riesgo y costo, el sistema contempla vías de aprobación agilizadas que radican la responsabilidad de la aprobación técnica principalmente en el propio GORE.
#### Seccion 4 2 1 Proyectos de Inversion Menores a 5000 UTM Exentos de RS
#### Def
Proceso expedito donde la aprobación técnica no la otorga el MDSF, sino el propio GORE, tras verificar el cumplimiento de requisitos mínimos y enviar una "Carta de Responsabilidad" al MDSF informando que el proyecto no presenta impedimentos ni constituye un fraccionamiento.
#### Seccion 4 2 2 Proyectos de Conservacion
#### Def
Proceso específico para proyectos cuyo costo no supera el 30% del valor de reposición del activo. La evaluación del MDSF se limita a verificar la admisibilidad de la iniciativa como "Conservación", otorgando un resultado "AD" (Admisible para financiamiento), que es distinto y menos exigente que un RS completo.
### Seccion 4 3 Flujo para Programas Publicos Regionales Evaluacion DIPRES SES
#### ID
KB-GN-102-FLUJO-PPR-GLOSA06-01
#### Fnd
Los programas de gasto corriente o mixto, financiados a través de la Glosa 06 de la Ley de Presupuestos, siguen un carril de evaluación completamente distinto al SNI. La aprobación técnica es otorgada por el nivel central (DIPRES y Subsecretaría de Evaluación Social) en un proceso de dos etapas.
#### Filtros
| Cpt | Act |
| --- | --- |
| Filtro 1: Evaluación de Pertinencia del Perfil | El GORE presenta un "Formulario de Perfil" conciso. DIPRES/SES evalúan si la iniciativa es pertinente y corresponde a un programa. Si es aprobado, se solicita al GORE elaborar el diseño detallado. |
| Filtro 2: Evaluación de Fondo del Diseño | El GORE elabora un "Formulario de Diseño" con Metodología de Marco Lógico (MML). DIPRES/SES realizan una revisión iterativa, enviando observaciones hasta que el diseño es subsanado y calificado como "RF (Recomendado Favorablemente)", lo que habilita su financiamiento. |

## Seccion 5 Flujo de Aprobacion para Modificaciones Presupuestarias
### ID
KB-GN-102-FLUJOS-MOD-PPTO-01
### Purp
Describir el proceso para ajustar el presupuesto regional aprobado. El flujo y el instrumento legal requerido dependen críticamente del alcance de la modificación: si afecta solo al presupuesto interno del GORE o si impacta la estructura presupuestaria nacional (Partida 31).
### XRef Required
- urn:gn:kb:ley-presupuestos-2026-partida-31
- urn:gn:kb:ley-presupuestos-2026-partida-31
- urn:gn:kb:ley-presupuestos-2026-partida-31
### Restricciones Presupuesto 2026
#### ID
KB-GN-102-RESTR-PPTO-2026-SEC5-01
#### Glosa 10 Subt31 Excepcion Aprobacion CORE 10pct
#### ID
KB-GN-102-RESTR-PPTO-2026-SEC5-GLO10-10PCT-01
#### XRef Required
- urn:gn:kb:ley-presupuestos-2026-partida-31
#### Content
Las identificaciones presupuestarias de las iniciativas contratadas en años
anteriores en ejecución y aquellas creadas en el mismo año, no requerirán una
nueva aprobación del Consejo Regional, si los montos totales o resultantes son
iguales o menores al 10% de los costos totales ya aprobados por el Consejo
Regional, reajustados a la moneda del año en curso.

#### Glosa 11 Subt33 Excepcion Aprobacion CORE 10pct
#### ID
KB-GN-102-RESTR-PPTO-2026-SEC5-GLO11-10PCT-01
#### XRef Required
- urn:gn:kb:ley-presupuestos-2026-partida-31
#### Content
Las identificaciones presupuestarias de las iniciativas contratadas en años
anteriores en ejecución y aquellas creadas en el mismo año, no requerirán una
nueva aprobación del Consejo Regional, si los montos totales o resultantes son
iguales o menores al 10% de los costos totales ya aprobados por el Consejo
Regional, reajustados a la moneda del año en curso.

#### Glosa 14 Emergencias 3pct y 2pct
#### ID
KB-GN-102-RESTR-PPTO-2026-SEC5-GLO14-EMERG-01
#### XRef Required
- urn:gn:kb:ley-presupuestos-2026-partida-31
#### Content
Se podrá traspasar hasta un 3% del presupuesto de inversión aprobado por el Congreso Nacional de cada Gobierno Regional, a requerimiento de la Subsecretaría del Interior a las asignaciones 24.03.002 y/o 33.03.001 del presupuesto de dicha Subsecretaría para enfrentar situaciones de emergencia.
La Subsecretaría del Interior informará semestralmente sobre el uso de esos recursos de emergencia a la Comisión Especial Mixta de Presupuestos y a los Gobiernos Regionales que aportaron a ese Fondo de Emergencia.
Asimismo, los gobiernos regionales podrán destinar hasta un 2% del presupuesto de Inversión Regional aprobado por el Congreso Nacional, para enfrentar situaciones de emergencia (en todas sus etapas) definidas mediante resolución por el Ministro o Subsecretario del Interior. Para materializar lo anterior, los gobiernos regionales deberán coordinarse con la Subsecretaría del Interior. La ejecución de estos recursos se podrá efectuar sin esperar la total tramitación del acto administrativo del Gobierno Regional.
Trimestralmente, los gobiernos regionales informarán a la Comisión Especial Mixta de Presupuestos y a la Dirección de Presupuestos, sobre el uso de estos recursos.

### Seccion 5 1 Tipologia de Modificaciones y Acto Administrativo Requerido
#### ID
KB-GN-102-MODPPTO-TIPOLOGIA-01
#### Fnd
La siguiente tabla clasifica los tipos de modificación presupuestaria y el acto administrativo que se requiere para su formalización, constituyendo una matriz de decisión clave para la gestión financiera.
#### Table
#### Columns
- Tipo_de_Modificacion
- Descripcion_Breve
- Afecta_Presupuesto_Partida_31
- Acto_Administrativo_Requerido
- Ref_Normativa
#### Rows
| Tipo_de_Modificacion | Descripcion_Breve | Afecta_Presupuesto_Partida_31 | Acto_Administrativo_Requerido | Ref_Normativa |
| --- | --- | --- | --- | --- |
| Reasignación Presupuestaria Interna | Cpt: Movimiento de fondos entre subtítulos dentro del presupuesto GORE. | No | Solo Resolución GORE | GORE-FIN-MOD-TIPOS-ACTOS-01 |
| Creación Iniciativas FRPD | Cpt: Asignación de fondos desde provisión FRPD a proyectos específicos. | No | Solo Resolución GORE | GORE-FIN-MOD-TIPOS-ACTOS-01 |
| Suplemento Presupuestario | Cpt: Aumento de presupuesto por mayor aporte fiscal. | Sí | Decreto Supremo (DIPRES) y Resolución GORE | GORE-FIN-MOD-TIPOS-ACTOS-01 |
| Transferencia a Otros Organismos | Cpt: Reasignación desde FNDR para transferir a ministerio (consolidable). | Sí | Decreto Supremo (DIPRES) y Resolución GORE | GORE-FIN-MOD-TIPOS-ACTOS-01 |
| Financiamiento Emergencias (3%) | Cpt: Uso de fondo de emergencia para transferir a otra entidad. | Sí | Decreto Supremo (DIPRES) y Resolución GORE | GORE-FIN-MOD-TIPOS-ACTOS-01 |
### Seccion 5 2 Proceso de Aprobacion Interna Rol del Consejo Regional CORE y sus Excepciones
#### ID
KB-GN-102-MODPPTO-CORE-01
#### Fnd
Por regla general, toda modificación que altere el presupuesto de inversión debe ser aprobada por el CORE. Sin embargo, la Ley de Presupuestos contempla excepciones para agilizar la gestión.
#### Elementos
-
  #### Cpt
  Aprobación CORE (Regla General)
  #### Proc
  La propuesta de modificación es preparada por DIPIR (inversión) y DAF (funcionamiento), presentada por el Gobernador y sometida a votación del CORE.
  #### Ref
  KB-GN-102-ACTORES-MATRIZ-01
-
  #### Cpt
  Excepciones a la Aprobación CORE
  #### Def
  La Glosa 01 de la Ley de Presupuestos permite al Gobernador realizar ciertas modificaciones sin acuerdo previo del CORE, como aumentos de costo de proyectos en ejecución (hasta un 10% con tope de 7.000 UTM) o la aplicación del 3% para emergencias.
-
  #### Req
  Aunque no requieren aprobación previa, el GORE debe informar mensualmente al CORE sobre estas modificaciones.
### Seccion 5 3 Proceso de Aprobacion Externa Visacion DIPRES y Toma de Razon CGR
#### ID
KB-GN-102-MODPPTO-EXTERNO-01
#### Fnd
Las modificaciones presupuestarias, incluso las exentas de aprobación del CORE, deben pasar por un riguroso control externo antes de su vigencia.
#### Flujo
| Cpt | Act | Ref |
| --- | --- | --- |
| Paso 1: Visación por DIPRES | La resolución de modificación del GORE se envía a DIPRES para una revisión de cumplimiento normativo. DIPRES puede devolverla con observaciones para su corrección. | KB-GN-102-ACTORES-MATRIZ-01 |
| Paso 2: Toma de Razón por CGR | Una vez visada por DIPRES, la resolución se remite a la CGR para el control preventivo de legalidad. Solo después de la Toma de Razón, el acto entra en vigencia y la DAF puede ajustar el presupuesto en SIGFE. | KB-GN-102-ACTORES-MATRIZ-01 |

## Seccion 6 Flujo de Aprobacion para Convenios y Transferencias de Recursos
### ID
KB-GN-102-FLUJOS-CONVENIOS-01
### Purp
Detallar el flujo para la formalización de la entrega de recursos a terceros, un proceso altamente regulado para gestionar el riesgo fiscal y asegurar la probidad y la correcta rendición de cuentas.
### Fnd
La aprobación del convenio es un hito de control crítico que precede a cualquier desembolso.
### XRef Required
- urn:gn:kb:ley-presupuestos-2026-partida-31
- urn:gn:kb:ley-presupuestos-2026-normas-generales
### Restricciones Presupuesto 2026
#### ID
KB-GN-102-RESTR-PPTO-2026-SEC6-01
#### Glosa 03 Restricciones Generales Inversion Regional
#### ID
KB-GN-102-RESTR-PPTO-2026-SEC6-GLO03-01
#### XRef Required
- urn:gn:kb:ley-presupuestos-2026-partida-31
#### Content
Los recursos de los presupuestos de inversión regional no podrán financiar préstamos, gastos en personal, o gastos en bienes y servicios de consumo de las entidades receptoras. Asimismo, no podrán destinarse para constituir, efectuar aportes o comprar sociedades o empresas.

#### Articulo 07 Decretos Transferencias Subt24 33
#### ID
KB-GN-102-RESTR-PPTO-2026-SEC6-ART07-01
#### XRef Required
- urn:gn:kb:ley-presupuestos-2026-normas-generales
#### Content
Reglas para decretos con transferencias (Subtítulos 24 y 33).
Transferencias corrientes a Unidades o Programas del Servicio, ejecutados total o parcialmente por éste
Desc: Desglose previo a la ejecución presupuestaria en conceptos de gasto
Frecuencia: Mensual
Destinatario: DIPRES
Contenido:
  - Informe avance actividades
  - Información ejecución presupuestaria
Res: Desglose constituye autorización máxima de gasto por concepto
Proc_Modificacion: Modificaciones mediante igual procedimiento
Visacion: Puede efectuarse desde fecha publicación de esta ley
Desc: No incluir recursos para gastos en personal ni bienes y servicios de consumo
Cond: Salvo autorización por norma expresa en el respectivo presupuesto

### Seccion 6 1 Flujo para Convenios de Transferencia a Terceros Publicos y Privados
#### ID
KB-GN-102-FLUJO-CONVENIO-01
#### Fnd
Este flujo transforma una decisión de financiamiento (ej. un acuerdo del CORE) en una obligación legal ejecutable, estableciendo el marco que regirá el uso y la rendición de los fondos públicos.
#### Flujo
-
  #### Cpt
  Paso 1: Elaboración del Borrador del Convenio
  #### Resp
  División técnica proponente (ej. DIDESOH, DIPIR).
  #### Ref
  KB-GN-102-ACTORES-MATRIZ-01
  #### Act
  Se redacta el borrador del convenio, especificando claramente el objeto, monto, plazos, productos esperados, obligaciones de las partes y los mecanismos de rendición de cuentas.
-
  #### Cpt
  Paso 2: Revisión Jurídica y Financiera
  #### Resp
  Asesoría Jurídica; DAF.
  #### Ref
  KB-GN-102-ACTORES-MATRIZ-01
  #### Act
  El borrador es revisado por la Asesoría Jurídica para garantizar su legalidad (esp. transferencias a privados según Ley de Presupuestos: concurso, garantías, etc.). La DAF revisa las cláusulas financieras y de rendición.
-
  #### Cpt
  Paso 3: Firma del Convenio
  #### Resp
  Gobernador/a Regional; Representante Legal de la entidad receptora.
  #### Ref
  KB-GN-102-ACTORES-MATRIZ-01
  #### Act
  El convenio es firmado por ambas partes, formalizando el acuerdo de voluntades.
-
  #### Cpt
  Paso 4: Emisión de Resolución Aprobatoria y Toma de Razón
  #### Resp
  GORE; CGR.
  #### Ref
  KB-GN-102-ACTORES-MATRIZ-01
  #### Act
  El GORE emite una resolución que aprueba el convenio suscrito y autoriza la transferencia de fondos. Este acto, al comprometer gasto público, debe ser remitido obligatoriamente a CGR para su Toma de Razón.
  #### Warn
  La transferencia de fondos no puede realizarse hasta que la CGR tome razón de la resolución.

## Seccion 7 Conclusiones
### ID
KB-GN-102-CONCLUSIONES-01
### Purp
Sintetizar las características estructurales del sistema de aprobación del GORE Ñuble.
### Fnd
El análisis de los flujos de aprobación del GORE Ñuble revela un sistema de gobernanza complejo y multifacético, diseñado para equilibrar la autonomía regional con un estricto control de legalidad y probidad. Se identifican tres características estructurales clave:
### Caracteristicas Estructurales Clave
| Cpt | Def | Just |
| --- | --- | --- |
| Segmentación de Flujos por Proporcionalidad | El sistema no es monolítico; segmenta los flujos de trabajo basándose en la naturaleza, costo y riesgo de cada iniciativa. Actos de trámite general siguen una ruta ágil, mientras que las iniciativas de inversión y modificaciones presupuestarias se canalizan por vías diferenciadas y más rigurosas. | Este diseño aplica un principio de proporcionalidad, reservando los controles más exhaustivos y externos para las decisiones de mayor impacto fiscal y estratégico. |
| Gobernanza de Control Dual y Vetos Múltiples | La estructura de aprobación se fundamenta en una separación de poderes interna (Gobernador, CORE, Divisiones técnicas) y externa (CGR, DIPRES, MDSF). | Los organismos externos no son meros supervisores, sino "compuertas" obligatorias con poder de veto. Un flujo exitoso es la navegación a través de filtros políticos, técnicos, financieros y legales. |
| Centralidad del Control Externo y Preventivo | La Toma de Razón de la CGR constituye el hito de control preventivo más importante para todos los actos que comprometen el erario público. | Esta instancia asegura que ninguna obligación financiera se materialice sin un examen previo de su legalidad, actuando como el principal garante del buen uso de los recursos públicos antes del desembolso. |
