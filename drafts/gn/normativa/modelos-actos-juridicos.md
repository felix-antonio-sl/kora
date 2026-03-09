---
_manifest:
  urn: urn:gn:kb:modelos-actos-juridicos
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-09'
    source: domains/gn/03_operacion/juridico/kb_gn_100_modelos_actos_juridicos_koda.yml
version: 2.0.0
status: draft
tags:
- gore-nuble
- gobierno-regional
- actos-juridicos
- modelos
- normativa
- gn
lang: es
extensions:
  gn:
    source_paths:
    - domains/gn/03_operacion/juridico/kb_gn_100_modelos_actos_juridicos_koda.yml
    source_hashes:
      domains/gn/03_operacion/juridico/kb_gn_100_modelos_actos_juridicos_koda.yml: 63a74477a9a3046a2beb52b9397eb26e459067d657e3d0016e32d4216b4a96f1
    source_type: koda_yaml
    transformation_mode: korafy_direct
    fs: 100
    cr: 1.81
    run_id: gn-smoke
    review_gate: auto
    scope_statement: null
    dependencies: []
    expected_sections:
    - Contenido
    skeleton_count: 1
    meat_count: 303
    fat_count: 0
    evidence_path: build/gn-rebuild/gn-smoke/evidence/normativa__modelos-actos-juridicos.md.json
---

# Modelos de Actos Jurídicos GORE Ñuble
## Titulo
Modelos de Actos Jurídicos GORE Ñuble
## Secciones
### S 1 executive summary and usage guide
#### Titulo
1. Executive Summary and Usage Guide
#### Contenido

ID: KB-GN-100-SUMMARY-01
#### Secciones
#### S 1 1 artifact purpose
#### Titulo
1.1. Artifact Purpose
#### Contenido

ID: KB-GN-100-PURPOSE-01
Purp: Serve as a fundamental knowledge artifact for the AI Agent "Administrative Documentation Generator" (ID: AGENT-GORE-DOCGEN-V1.0).
Fnd: Provides a structured knowledge base, not just templates.
Mssn: Enable the agent to generate administrative acts that are formally correct, legally valid, and contextually coherent.
Dep: Adherence to SFD and STS standards is critical for AI interpretation and population.
Ref: Ley N° 19.880.
Obj: Achieve GORE Ñuble modernization goals (reduce errors, standardize documents, increase efficiency and probity).
#### S 1 2 model structure sfd sts
#### Titulo
1.2. Model Structure (SFD/STS)
#### Contenido

ID: KB-GN-100-STRUCTURE-01
Fnd: Each model is structured with a rigorous syntax for human and machine readability.
Cpt: `BEGIN_EMBEDDED_BLOCK:: GUIDE-SFD-STS-MASTER-01 ...`.

- Def: Directive that encapsulates a form model, signaling that its content is governed by the SFD standard.
Cpt: `### Form-Section`.
- Def: Defines a main structural section of an administrative act (e.g., METADATA, HEADER, VISTOS, CONSIDERANDO, RESUELVO).
- Ref: Reflects the canonical legal logic of an act's construction.
Cpt: `#### Form-Field`.
- Def: Represents a variable data field for the AI agent to populate (e.g., dates, names, file numbers).
- Cpt: SFD-Lexicon.
  - Def: Each field is described by functional keys (`Field-Label`, `Field-Type`, `Field-Instr`, `Field-Constraint`).
  - Purp: Provide context, legal justification, operational instructions, and critical validations to guide the AI agent.
#### S 1 3 index of legal act models
#### Titulo
1.3. Index of Legal Act Models
#### Contenido

ID: KB-GN-100-INDEX-01
Purp: Provides a quick reference index of the models included in this artifact.

|Form ID|Description|Version|Status|
|-|-|-|-|
|`FORM-MODIF-CONV-01`|Resolución que Aprueba Modificación de Convenio|1.0.0|Complete|
|`FORM-RECTIF-ACTO-01`|Resolución que Rectifica Acto Administrativo|1.0.0|Complete|
|`FORM-RESCIL-CONV-01`|Resolución que Aprueba Resciliación de Convenio|1.0.0|Complete|
|`FORM-REVOCA-ACTO-01`|Resolución que Revoca un Acto Administrativo|1.0.0|Complete|
|`FORM-ESCRITO-INICIO-01`|Escrito de Inicio de Procedimiento|1.0.0|Complete|
|`FORM-ESCRITO-REPO-01`|Escrito de Recurso de Reposición|1.0.0|Complete|
### S 2 legal act models sfd format
#### Titulo
2. Legal Act Models (SFD Format)
#### Contenido

ID: KB-GN-100-MODELS-CONTAINER-01

```plaintext
BEGIN_EMBEDDED_BLOCK:: GUIDE-SFD-STS-MASTER-01 FORM-MODIF-CONV-01
#### Secciones
#### Form metadata
#### Titulo
Form Metadata
#### Contenido

ID: FORM-MODIF-CONV-01-S0-METADATA-01
#### Secciones
#### Form description
#### Titulo
Form Description
#### Contenido

ID: FORM-MODIF-CONV-01-S0-DESC-01
Field-Label: "Descripción del Formulario"
Field-Type: Static-Text
Field-Instr: "Propósito: Resolución Exenta que aprueba la modificación de un convenio de colaboración o transferencia de recursos. Formaliza la alteración de las cláusulas de un acuerdo preexistente, requiriendo la voluntad de las partes o una habilitación contractual expresa."
#### Applicable regulations
#### Titulo
Applicable Regulations
#### Contenido

ID: FORM-MODIF-CONV-01-S0-NORMATIVA-01
Field-Label: "Normativa Aplicable"
Field-Type: Static-Text
Field-Instr: "Marco Legal: Referencias normativas clave que rigen la competencia para celebrar convenios y la forma de los actos administrativos."
Field-Placeholder: "Ley N° 19.880; Ley N° 18.575, Orgánica Constitucional de Bases Generales de la Administración del Estado; Ley N° 19.175, Orgánica Constitucional sobre Gobierno y Administración Regional."
#### Header
#### Titulo
Header
#### Contenido

ID: FORM-MODIF-CONV-01-S1-HEADER-01
#### Secciones
#### Act type
#### Titulo
Act Type
#### Contenido

ID: FORM-MODIF-CONV-01-S1-TIPO-01
Field-Label: "Tipo de Acto"
Field-Type: Static-Text
Field-Placeholder: "RESOLUCIÓN EXENTA"
Field-Instr: "Naturaleza: Acto administrativo que no requiere trámite de toma de razón por la Contraloría General de la República, salvo que comprometa recursos de ejercicios futuros o supere ciertos montos."
#### Resolution number
#### Titulo
Resolution Number
#### Contenido

ID: FORM-MODIF-CONV-01-S1-NUMERO-01
Field-Label: "Número de Resolución"
Field-Type: Text
Field-Placeholder: "N° [numero_resolucion]/[año]"
Field-Instr: "El agente debe solicitar el número correlativo asignado por la Oficina de Partes o unidad correspondiente."
Field-Constraint: "Req: mandatory."
#### Place and date
#### Titulo
Place and Date
#### Contenido

ID: FORM-MODIF-CONV-01-S1-LUGARFECHA-01
Field-Label: "Lugar y Fecha"
Field-Type: Text
Field-Placeholder: "CHILLÁN, [dia] de [mes] de [año]."
Field-Instr: "Formalidad: Lugar y fecha de emisión del acto."
Field-Constraint: "Req: mandatory."
#### Vistos
#### Titulo
Vistos
#### Contenido

ID: FORM-MODIF-CONV-01-S2-VISTOS-01
#### Secciones
#### Authority attributions
#### Titulo
Authority Attributions
#### Contenido

ID: FORM-MODIF-CONV-01-S2-ATRIBUCIONES-01
Field-Label: "Vistos: Atribuciones de la Autoridad"
Field-Type: Static-Text
Field-Placeholder: "VISTOS: Lo dispuesto en la Constitución Política de la República; la Ley N° 19.880, que Establece Bases de los Procedimientos Administrativos que rigen los Actos de los Órganos de la Administración del Estado; la Ley N° 18.575, Orgánica Constitucional de Bases Generales de la Administración del Estado; la Ley N° 19.175, Orgánica Constitucional sobre Gobierno y Administración Regional, y sus modificaciones; y la Resolución N° 7, de 2019, de la Contraloría General de la República."
Field-Instr: "Competencia: Fundamenta la potestad del Gobernador Regional para dictar actos administrativos. Es un requisito esencial para la validez del acto."
#### Original agreement
#### Titulo
Original Agreement
#### Contenido

ID: FORM-MODIF-CONV-01-S2-CONVENIO-01
Field-Label: "Vistos: Convenio Original"
Field-Type: Text
Field-Placeholder: "El Convenio [nombre_convenio], de fecha [fecha_convenio], suscrito entre el Gobierno Regional de Ñuble y [nombre_contraparte], aprobado mediante Resolución Exenta N° [numero_res_aprobatoria], de fecha [fecha_res_aprobatoria]."
Field-Instr: "Objeto: Individualización inequívoca del acuerdo de voluntades a modificar. La precisión evita ambigüedades y potenciales vicios de nulidad."
Field-Constraint: "Req: mandatory."
#### Modification request
#### Titulo
Modification Request
#### Contenido

ID: FORM-MODIF-CONV-01-S2-SOLICITUD-01
Field-Label: "Vistos: Solicitud de Modificación"
Field-Type: Text
Field-Placeholder: "La solicitud de modificación presentada por [entidad_solicitante] mediante Oficio N° [numero_oficio_solicitud], de fecha [fecha_oficio_solicitud], y/o el acuerdo de las partes manifestado en [documento_acuerdo]."
Field-Instr: "Inicio Procedimiento: Documenta el acto que da origen a la modificación, ya sea una solicitud formal o un acuerdo mutuo."
Field-Constraint: "Req: mandatory."
#### Considerando
#### Titulo
Considerando
#### Contenido

ID: FORM-MODIF-CONV-01-S3-CONSIDERANDO-01
#### Secciones
#### Agreement context
#### Titulo
Agreement Context
#### Contenido

ID: FORM-MODIF-CONV-01-S3-CONTEXTO-01
Field-Label: "Considerando: Contexto del Convenio"
Field-Type: Text
Field-Placeholder: "1°. Que, con fecha [fecha_convenio], el Gobierno Regional de Ñuble suscribió el convenio individualizado en los Vistos, con el objeto de [objeto_del_convenio]."
Field-Instr: "Contexto: Reitera el propósito original del convenio para enmarcar la modificación."
Field-Constraint: "Req: mandatory."
#### Modification rationale
#### Titulo
Modification Rationale
#### Contenido

ID: FORM-MODIF-CONV-01-S3-FUNDAMENTO-01
Field-Label: "Considerando: Fundamento de la Modificación"
Field-Type: TextArea
Field-Placeholder: "2°. Que, por razones de [tipo_razon: hecho, técnicas, operativas, fuerza mayor], se ha hecho necesario y conveniente para el interés público modificar las cláusulas [numeros_clausulas] del referido convenio, en lo relativo a [descripcion_breve_modificacion]."
Field-Instr: "Motivación: Cumple con el deber de fundamentación (Art. 11 y 41, Ley 19.880). El acto debe expresar sus razones de hecho y de derecho. El agente IA debe solicitar al usuario que especifique y detalle estas razones de forma clara y suficiente."
Field-Constraint: "Req: mandatory."
#### Parties agreement
#### Titulo
Parties' Agreement
#### Contenido

ID: FORM-MODIF-CONV-01-S3-ACUERDO-01
Field-Label: "Considerando: Acuerdo de las Partes"
Field-Type: Static-Text
Field-Placeholder: "3°. Que existe pleno acuerdo entre las partes para llevar a cabo la modificación en los términos que se expondrán en la parte resolutiva del presente acto."
Field-Instr: "Voluntad: Refuerza el carácter consensual de la modificación, elemento clave en la estabilidad de los contratos administrativos."
#### Resuelvo
#### Titulo
Resuelvo
#### Contenido

ID: FORM-MODIF-CONV-01-S4-RESUELVO-01
#### Secciones
#### Article 1 approval
#### Titulo
Article 1: Approval
#### Contenido

ID: FORM-MODIF-CONV-01-S4-ART1-01
Field-Label: "Resuelvo: Artículo Primero (Aprobación)"
Field-Type: Text
Field-Placeholder: "1°. APRUÉBASE la modificación del Convenio \"[nombre_convenio]\", suscrito entre el Gobierno Regional de Ñuble y [nombre_contraparte], en los términos del texto que se adjunta como Anexo N°1 y que se entiende formar parte integrante de la presente resolución."
Field-Instr: "Decisión: Núcleo del acto administrativo. Contiene la declaración de voluntad formal del órgano. La referencia a un anexo es una buena práctica para modificaciones complejas."
Field-Constraint: "Req: mandatory."
#### Article 2 consolidated text
#### Titulo
Article 2: Consolidated Text
#### Contenido

ID: FORM-MODIF-CONV-01-S4-ART2-01
Field-Label: "Resuelvo: Artículo Segundo (Texto Refundido)"
Field-Type: Static-Text
Field-Placeholder: "2°. APRUÉBASE, en consecuencia, el texto refundido del Convenio, que incorpora las modificaciones aprobadas en el artículo anterior."
Field-Instr: "Seguridad Jurídica: Opcional pero recomendado. La generación de un texto refundido consolida el acuerdo vigente en un único documento, facilitando su comprensión y ejecución futura."
#### Article 3 validity
#### Titulo
Article 3: Validity
#### Contenido

ID: FORM-MODIF-CONV-01-S4-ART3-01
Field-Label: "Resuelvo: Artículo Tercero (Vigencia)"
Field-Type: Static-Text
Field-Placeholder: "3°. DÉJASE constancia que todas las demás cláusulas del convenio original que no han sido modificadas por el presente acto, mantienen su plena vigencia."
Field-Instr: "Principio de Conservación: Clarifica que la modificación es parcial y no afecta la totalidad del acuerdo, preservando la estabilidad contractual."
#### Cierre
#### Titulo
Cierre
#### Contenido

ID: FORM-MODIF-CONV-01-S5-CIERRE-01
#### Secciones
#### Signature block
#### Titulo
Signature Block
#### Contenido

ID: FORM-MODIF-CONV-01-S5-FIRMA-01
Field-Label: "Firma y Timbre"
Field-Type: Static-Text
Field-Placeholder: "ANÓTESE, COMUNÍQUESE Y ARCHÍVESE.\n\n\n[Nombre Autoridad]\nGOBERNADOR REGIONAL DE ÑUBLE"
Field-Instr: "Formalización: Cierre del acto con las fórmulas de tramitación y la firma de la autoridad competente."

END_EMBEDDED_BLOCK:: FORM-MODIF-CONV-01
```

```plaintext
BEGIN_EMBEDDED_BLOCK:: GUIDE-SFD-STS-MASTER-01 FORM-RECTIF-ACTO-01
#### Form metadata 2
#### Titulo
Form Metadata
#### Contenido

ID: FORM-RECTIF-ACTO-01-S0-METADATA-01
#### Secciones
#### Form description
#### Titulo
Form Description
#### Contenido

ID: FORM-RECTIF-ACTO-01-S0-DESC-01
Field-Label: "Descripción del Formulario"
Field-Type: Static-Text
Field-Instr: "Propósito: Resolución Exenta que rectifica errores de hecho, numéricos o de transcripción en un acto administrativo previo. Permite a la Administración corregir sus propios errores materiales sin alterar la sustancia de la decisión original."
#### Applicable regulations
#### Titulo
Applicable Regulations
#### Contenido

ID: FORM-RECTIF-ACTO-01-S0-NORMATIVA-01
Field-Label: "Normativa Aplicable"
Field-Type: Static-Text
Field-Placeholder: "Artículo 62, Ley N° 19.880."
Field-Instr: "Marco Legal: La potestad rectificatoria se encuentra explícitamente consagrada en esta disposición."
#### Header 2
#### Titulo
Header
#### Contenido

ID: FORM-RECTIF-ACTO-01-S1-HEADER-01

- Field-Group: Contiene los mismos campos que FORM-MODIF-CONV-01-S1-HEADER-01
#### Vistos 2
#### Titulo
Vistos
#### Contenido

ID: FORM-RECTIF-ACTO-01-S2-VISTOS-01
#### Secciones
#### Authority attributions
#### Titulo
Authority Attributions
#### Contenido

ID: FORM-RECTIF-ACTO-01-S2-ATRIBUCIONES-01
Field-Label: "Vistos: Atribuciones de la Autoridad"
Field-Type: Static-Text
Field-Placeholder: "VISTOS: Lo dispuesto en el artículo 62 de la Ley N° 19.880, que Establece Bases de los Procedimientos Administrativos que rigen los Actos de los Órganos de la Administración del Estado; la Ley N° 19.175, Orgánica Constitucional sobre Gobierno y Administración Regional; y la Resolución N° 7, de 2019, de la Contraloría General de la República."
Field-Instr: "Competencia: Invoca directamente la norma que faculta la rectificación."
#### Original act
#### Titulo
Original Act
#### Contenido

ID: FORM-RECTIF-ACTO-01-S2-ACTOORIGINAL-01
Field-Label: "Vistos: Acto Original"
Field-Type: Text
Field-Placeholder: "La Resolución Exenta N° [numero_res_original] de fecha [fecha_res_original], dictada por esta Gobernación Regional."
Field-Instr: "Objeto: Identificación precisa del acto administrativo que contiene el error a subsanar."
Field-Constraint: "Req: mandatory."
#### Considerando 2
#### Titulo
Considerando
#### Contenido

ID: FORM-RECTIF-ACTO-01-S3-CONSIDERANDO-01
#### Secciones
#### Error type
#### Titulo
Error Type
#### Contenido

ID: FORM-RECTIF-ACTO-01-S3-TIPOERROR-01
Field-Label: "Tipo de Error"
Field-Type: Select
Field-Instr: "Causal: La potestad rectificatoria está limitada a errores materiales. No puede usarse para modificar el fondo de lo decidido (cambio de criterio) ni para subsanar vicios de legalidad (para lo cual procede la invalidación). El agente IA debe validar que el tipo de error seleccionado por el usuario corresponda a esta categoría."
Field-Constraint: "Req: mandatory."

- Field-Option: "material"
- Field-Option: "de hecho"
- Field-Option: "de transcripción"
- Field-Option: "numérico"
#### Error detection clause
#### Titulo
Error Detection Clause
#### Contenido

ID: FORM-RECTIF-ACTO-01-S3-DETECCION-01
Field-Label: "Considerando: Detección del Error"
Field-Type: Static-Text
Field-Placeholder: "1°. Que, se ha advertido la existencia de un error de [tipo_error] en el del acto administrativo individualizado en los Vistos."
Field-Instr: "El agente debe poblar '[tipo_error]' con la selección de FORM-RECTIF-ACTO-01-S3-TIPOERROR-01."
#### Error detail
#### Titulo
Error Detail
#### Contenido

ID: FORM-RECTIF-ACTO-01-S3-DETALLE-01
Field-Label: "Considerando: Detalle del Error"
Field-Type: TextArea
Field-Placeholder: "2°. Que, en efecto, en la sección indicada, donde dice: \"[texto_erroneo]\", debe decir: \"[texto_correcto]\"."
Field-Instr: "Especificidad: La rectificación debe ser concreta y precisa, identificando claramente el texto erróneo y el texto correcto. El formato 'dice/debe decir' es la forma canónica."
Field-Constraint: "Req: mandatory."
#### Need for rectification
#### Titulo
Need for Rectification
#### Contenido

ID: FORM-RECTIF-ACTO-01-S3-NECESIDAD-01
Field-Label: "Considerando: Necesidad de Rectificar"
Field-Type: Static-Text
Field-Placeholder: "3°. Que, en virtud de lo expuesto, y en uso de la facultad conferida por el artículo 62 de la Ley N° 19.880, resulta imperativo proceder a la rectificación del acto viciado para asegurar su correcta inteligencia y ejecución."
Field-Instr: "Justificación: Conecta la detección del error con la necesidad de ejercer la potestad legal para enmendarlo."
#### Resuelvo 2
#### Titulo
Resuelvo
#### Contenido

ID: FORM-RECTIF-ACTO-01-S4-RESUELVO-01
#### Secciones
#### Article 1 rectification
#### Titulo
Article 1: Rectification
#### Contenido

ID: FORM-RECTIF-ACTO-01-S4-ART1-01
Field-Label: "Resuelvo: Artículo Primero (Rectificación)"
Field-Type: Text
Field-Placeholder: "1°. RECTIFÍCASE el [seccion_del_acto] de la Resolución Exenta N° [numero_res_original], de fecha [fecha_res_original], en el sentido de reemplazar la expresión \"[texto_erroneo]\" por la siguiente: \"[texto_correcto]\"."
Field-Instr: "Decisión: Ejecuta la corrección. Es el núcleo del acto de rectificación."
Field-Constraint: "Req: mandatory."
#### Article 2 validity
#### Titulo
Article 2: Validity
#### Contenido

ID: FORM-RECTIF-ACTO-01-S4-ART2-01
Field-Label: "Resuelvo: Artículo Segundo (Vigencia)"
Field-Type: Static-Text
Field-Placeholder: "2°. ESTABLÉCESE que la presente rectificación forma parte integrante de la Resolución Exenta N° [numero_res_original], entendiéndose que sus efectos se retrotraen a la fecha de dictación de esta última."
Field-Instr: "Efecto: La rectificación tiene efecto retroactivo ('ex tunc'), pues se entiende que el acto original siempre debió contener el texto correcto. No crea un nuevo acto, sino que enmienda el preexistente."
#### Cierre 2
#### Titulo
Cierre
#### Contenido

ID: FORM-RECTIF-ACTO-01-S5-CIERRE-01
#### Secciones
#### Signature block
#### Titulo
Signature Block
#### Contenido

ID: FORM-RECTIF-ACTO-01-S5-FIRMA-01
Field-Label: "Firma y Timbre"
Field-Type: Static-Text
Field-Placeholder: "ANÓTESE, NOTIFÍQUESE Y ARCHÍVESE.\n\n\n[Nombre Autoridad]\nGOBERNADOR REGIONAL DE ÑUBLE"
Field-Instr: "Formalización: Cierre del acto. La notificación es crucial para que los interesados conozcan la versión corregida del acto."

END_EMBEDDED_BLOCK:: FORM-RECTIF-ACTO-01
```

```plaintext
BEGIN_EMBEDDED_BLOCK:: GUIDE-SFD-STS-MASTER-01 FORM-RESCIL-CONV-01
#### Form metadata 3
#### Titulo
Form Metadata
#### Contenido

ID: FORM-RESCIL-CONV-01-S0-METADATA-01
#### Secciones
#### Form description
#### Titulo
Form Description
#### Contenido

ID: FORM-RESCIL-CONV-01-S0-DESC-01
Field-Label: "Descripción del Formulario"
Field-Type: Static-Text
Field-Instr: "Propósito: Resolución Exenta que aprueba la terminación de un convenio por mutuo acuerdo de las partes (resciliación o mutuo disenso). Formaliza la extinción de las obligaciones de un convenio, basada en la voluntad concordante de los suscriptores."
#### Applicable regulations
#### Titulo
Applicable Regulations
#### Contenido

ID: FORM-RESCIL-CONV-01-S0-NORMATIVA-01
Field-Label: "Normativa Aplicable"
Field-Type: Static-Text
Field-Placeholder: "Artículo 1545 y 1567 del Código Civil (aplicable supletoriamente); Ley N° 19.880; Ley N° 19.175."
Field-Instr: "Marco Legal: Se basa en el principio de autonomía de la voluntad, aplicable a los contratos de la Administración en lo que no contravenga el derecho público."
#### Header 3
#### Titulo
Header
#### Contenido

ID: FORM-RESCIL-CONV-01-S1-HEADER-01

- Field-Group: Contiene los mismos campos que FORM-MODIF-CONV-01-S1-HEADER-01
#### Vistos 3
#### Titulo
Vistos
#### Contenido

ID: FORM-RESCIL-CONV-01-S2-VISTOS-01
#### Secciones
#### Authority attributions
#### Titulo
Authority Attributions
#### Contenido

ID: FORM-RESCIL-CONV-01-S2-ATRIBUCIONES-01
Field-Label: "Vistos: Atribuciones de la Autoridad"
Field-Type: Static-Text
Field-Placeholder: "VISTOS: Lo dispuesto en la Ley N° 19.880; la Ley N° 19.175, Orgánica Constitucional sobre Gobierno y Administración Regional; y la Resolución N° 7, de 2019, de la Contraloría General de la República."
Field-Instr: "Competencia: Fundamenta la potestad del Gobernador para dictar el acto."
#### Original agreement
#### Titulo
Original Agreement
#### Contenido

ID: FORM-RESCIL-CONV-01-S2-CONVENIO-01
Field-Label: "Vistos: Convenio Original"
Field-Type: Text
Field-Placeholder: "El Convenio [nombre_convenio], de fecha [fecha_convenio], suscrito entre el Gobierno Regional de Ñuble y [nombre_contraparte], aprobado por Resolución Exenta N° [numero_res_aprobatoria]."
Field-Instr: "Objeto: Individualización del acuerdo de voluntades que se extinguirá."
Field-Constraint: "Req: mandatory."
#### Resciliation agreement
#### Titulo
Resciliation Agreement
#### Contenido

ID: FORM-RESCIL-CONV-01-S2-ACUERDO-01
Field-Label: "Vistos: Acuerdo de Resciliación"
Field-Type: Text
Field-Placeholder: "El acuerdo de resciliación suscrito por las partes con fecha [fecha_acuerdo_resciliacion], en el cual manifiestan su voluntad de poner término anticipado al referido convenio."
Field-Instr: "Documento Fundante: La resolución aprueba un acuerdo previo. Es esencial que este acuerdo exista y se cite."
Field-Constraint: "Req: mandatory."
#### Considerando 3
#### Titulo
Considerando
#### Contenido

ID: FORM-RESCIL-CONV-01-S3-CONSIDERANDO-01
#### Secciones
#### Agreement existence
#### Titulo
Agreement Existence
#### Contenido

ID: FORM-RESCIL-CONV-01-S3-EXISTENCIA-01
Field-Label: "Considerando: Existencia del Convenio"
Field-Type: Text
Field-Placeholder: "1°. Que, mediante el instrumento singularizado en los Vistos, las partes acordaron [objeto_del_convenio], estableciendo obligaciones recíprocas."
Field-Instr: "Contexto: Describe la relación contractual que se va a extinguir."
Field-Constraint: "Req: mandatory."
#### Mutual agreement
#### Titulo
Mutual Agreement
#### Contenido

ID: FORM-RESCIL-CONV-01-S3-MUTUOACUERDO-01
Field-Label: "Considerando: Mutuo Acuerdo"
Field-Type: Static-Text
Field-Placeholder: "2°. Que las partes, de común acuerdo y por así convenir a sus intereses, han decidido poner término anticipado al mencionado convenio, manifestando su voluntad expresa en el documento de resciliación citado en los Vistos."
Field-Instr: "Voluntad: La resciliación se fundamenta en el 'mutuo disenso'. Es el pilar de este acto. A diferencia de la revocación (unilateral por mérito) o la invalidación (por ilegalidad), este acto es bilateral y consensual."
#### Status of obligations
#### Titulo
Status of Obligations
#### Contenido

ID: FORM-RESCIL-CONV-01-S3-OBLIGACIONES-01
Field-Label: "Considerando: Estado de Obligaciones"
Field-Type: Select
Field-Instr: "Efectos Patrimoniales: Define el estado de situación final para evitar litigios futuros. El agente IA debe ofrecer ambas opciones al usuario."
Field-Constraint: "Req: mandatory."

- Field-Option: "no existen obligaciones pendientes entre las partes"
- Field-Option: "las obligaciones pendientes se regularán de la forma que se detalla en el acuerdo"
Field-Logic: "Cond: (Ref: SELF.Value) -> Visibility: show. Req: mandatory."
#### Resuelvo 3
#### Titulo
Resuelvo
#### Contenido

ID: FORM-RESCIL-CONV-01-S4-RESUELVO-01
#### Secciones
#### Article 1 approval
#### Titulo
Article 1: Approval
#### Contenido

ID: FORM-RESCIL-CONV-01-S4-ART1-01
Field-Label: "Resuelvo: Artículo Primero (Aprobación)"
Field-Type: Text
Field-Placeholder: "1°. APRUÉBASE la resciliación del Convenio \"[nombre_convenio]\", suscrito con fecha [fecha_convenio] entre el Gobierno Regional de Ñuble y [nombre_contraparte]."
Field-Instr: "Decisión: Formaliza la aprobación del mutuo disenso."
Field-Constraint: "Req: mandatory."
#### Article 2 effects
#### Titulo
Article 2: Effects
#### Contenido

ID: FORM-RESCIL-CONV-01-S4-ART2-01
Field-Label: "Resuelvo: Artículo Segundo (Efectos)"
Field-Type: Text
Field-Placeholder: "2°. DÉJASE constancia que, en virtud de la resciliación aprobada, el referido convenio se extingue a contar de [fecha_efectiva_termino], cesando todos sus efectos para el futuro."
Field-Instr: "Efecto Temporal: La resciliación, por regla general, opera 'ex nunc' (hacia el futuro), sin afectar los actos ya ejecutados."
Field-Constraint: "Req: mandatory."
#### Article 3 settlement
#### Titulo
Article 3: Settlement
#### Contenido

ID: FORM-RESCIL-CONV-01-S4-ART3-01
Field-Label: "Resuelvo: Artículo Tercero (Finiquito)"
Field-Type: Text
Field-Placeholder: "3°. DECLÁRASE que las partes se otorgan el más completo y total finiquito respecto de las obligaciones emanadas del convenio que se rescilia, [clausula_opcional_finiquito: con la sola excepción de las que se establecen en el propio acuerdo de resciliación]."
Field-Instr: "Finiquito: Cierra la relación contractual. El agente IA debe permitir la inclusión de excepciones si el acuerdo de resciliación así lo estipula."
Field-Constraint: "Req: mandatory."
#### Cierre 3
#### Titulo
Cierre
#### Contenido

ID: FORM-RESCIL-CONV-01-S5-CIERRE-01

- Field-Group: Contiene los mismos campos que FORM-MODIF-CONV-01-S5-CIERRE-01

END_EMBEDDED_BLOCK:: FORM-RESCIL-CONV-01
```

```plaintext
BEGIN_EMBEDDED_BLOCK:: GUIDE-SFD-STS-MASTER-01 FORM-REVOCA-ACTO-01
#### Form metadata 4
#### Titulo
Form Metadata
#### Contenido

ID: FORM-REVOCA-ACTO-01-S0-METADATA-01
#### Secciones
#### Form description
#### Titulo
Form Description
#### Contenido

ID: FORM-REVOCA-ACTO-01-S0-DESC-01
Field-Label: "Descripción del Formulario"
Field-Type: Static-Text
Field-Instr: "Propósito: Resolución Exenta que deja sin efecto un acto administrativo anterior por razones de mérito, oportunidad o conveniencia. Potestad discrecional de la Administración para retirar un acto VÁLIDO por razones de interés público. No aplica a actos ilegales."
#### Applicable regulations
#### Titulo
Applicable Regulations
#### Contenido

ID: FORM-REVOCA-ACTO-01-S0-NORMATIVA-01
Field-Label: "Normativa Aplicable"
Field-Type: Static-Text
Field-Placeholder: "Artículo 61, Ley N° 19.880."
Field-Instr: "Marco Legal: Disposición clave que regula la potestad revocatoria y sus límites."
#### Header 4
#### Titulo
Header
#### Contenido

ID: FORM-REVOCA-ACTO-01-S1-HEADER-01

- Field-Group: Contiene los mismos campos que FORM-MODIF-CONV-01-S1-HEADER-01
#### Vistos 4
#### Titulo
Vistos
#### Contenido

ID: FORM-REVOCA-ACTO-01-S2-VISTOS-01
#### Secciones
#### Authority attributions
#### Titulo
Authority Attributions
#### Contenido

ID: FORM-REVOCA-ACTO-01-S2-ATRIBUCIONES-01
Field-Label: "Vistos: Atribuciones de la Autoridad"
Field-Type: Static-Text
Field-Placeholder: "VISTOS: Lo dispuesto en el artículo 61 de la Ley N° 19.880; la Ley N° 19.175; y la Resolución N° 7, de 2019, de la Contraloría General de la República."
Field-Instr: "Competencia: Invoca la norma que confiere la potestad revocatoria."
#### Act to be revoked
#### Titulo
Act to be Revoked
#### Contenido

ID: FORM-REVOCA-ACTO-01-S2-ACTOREVOCAR-01
Field-Label: "Vistos: Acto a Revocar"
Field-Type: Text
Field-Placeholder: "La Resolución Exenta N° [numero_res_original] de fecha [fecha_res_original], dictada por esta Gobernación Regional, que [descripcion_acto_original]."
Field-Instr: "Objeto: Identificación del acto administrativo válido que se pretende dejar sin efecto."
Field-Constraint: "Req: mandatory."
#### Considerando 4
#### Titulo
Considerando
#### Contenido

ID: FORM-REVOCA-ACTO-01-S3-CONSIDERANDO-01
#### Secciones
#### Merits rationale
#### Titulo
Merits Rationale
#### Contenido

ID: FORM-REVOCA-ACTO-01-S3-FUNDAMENTO-01
Field-Label: "Considerando: Fundamento de Mérito"
Field-Type: TextArea
Field-Placeholder: "1°. Que, por razones de mérito, oportunidad y conveniencia, sobrevinientes a la dictación del acto individualizado y fundadas en [descripcion_detallada_del_fundamento_de_interes_publico], se ha estimado necesario para el interés público dejar sin efecto el referido acto administrativo."
Field-Instr: "Causal: La revocación es discrecional pero no arbitraria. Debe fundarse en un cambio de circunstancias o una nueva apreciación del interés público. No puede fundarse en la ilegalidad del acto original. El agente IA debe exigir al usuario la explicitación de este fundamento."
Field-Constraint: "Req: mandatory."
#### No effect on rights
#### Titulo
No Effect on Rights
#### Contenido

ID: FORM-REVOCA-ACTO-01-S3-DERECHOS-01
Field-Label: "Considerando: No Afectación de Derechos Adquiridos"
Field-Type: Static-Text
Field-Placeholder: "2°. Que el acto que por este medio se revoca no ha generado derechos adquiridos por parte de los interesados, o bien, habiéndolos generado, estos han consentido expresamente en la revocación."
Field-Instr: "Límite Esencial: Condición crítica del artículo 61 de la Ley 19.880. La revocación es improcedente si lesiona derechos legítimamente adquiridos por los particulares. Este considerando es una declaración de cumplimiento legal y el agente IA debe tratarlo como una validación obligatoria."
#### Resuelvo 4
#### Titulo
Resuelvo
#### Contenido

ID: FORM-REVOCA-ACTO-01-S4-RESUELVO-01
#### Secciones
#### Article 1 revocation
#### Titulo
Article 1: Revocation
#### Contenido

ID: FORM-REVOCA-ACTO-01-S4-ART1-01
Field-Label: "Resuelvo: Artículo Único (Revocación)"
Field-Type: Text
Field-Placeholder: "1°. REVÓCASE, por las razones de mérito, oportunidad y conveniencia expuestas en la parte considerativa, la Resolución Exenta N° [numero_res_original], de fecha [fecha_res_original]."
Field-Instr: "Decisión: Contiene la declaración de voluntad que extingue el acto anterior."
Field-Constraint: "Req: mandatory."
#### Article 2 effects
#### Titulo
Article 2: Effects
#### Contenido

ID: FORM-REVOCA-ACTO-01-S4-ART2-01
Field-Label: "Resuelvo: Artículo Segundo (Efectos)"
Field-Type: Static-Text
Field-Placeholder: "2°. DÉJASE constancia que la presente revocación produce sus efectos a contar de la fecha de su total tramitación, sin afectar las situaciones jurídicas consolidadas bajo la vigencia del acto revocado."
Field-Instr: "Efecto Temporal: La revocación opera 'ex nunc' (hacia el futuro). No tiene efecto retroactivo, a diferencia de la invalidación. Esto protege la seguridad jurídica."
#### Cierre 4
#### Titulo
Cierre
#### Contenido

ID: FORM-REVOCA-ACTO-01-S5-CIERRE-01

- Field-Group: Contiene los mismos campos que FORM-RECTIF-ACTO-01-S5-CIERRE-01

END_EMBEDDED_BLOCK:: FORM-REVOCA-ACTO-01
```

```plaintext
BEGIN_EMBEDDED_BLOCK:: GUIDE-SFD-STS-MASTER-01 FORM-ESCRITO-INICIO-01
#### Form metadata 5
#### Titulo
Form Metadata
#### Contenido

ID: FORM-ESCRITO-INICIO-01-S0-METADATA-01
#### Secciones
#### Form description
#### Titulo
Form Description
#### Contenido

ID: FORM-ESCRITO-INICIO-01-S0-DESC-01
Field-Label: "Descripción del Formulario"
Field-Type: Static-Text
Field-Instr: "Propósito: Modelo de escrito para que un particular o interesado inicie un procedimiento administrativo ante el GORE Ñuble. Estructura una solicitud formal de un administrado, asegurando que contenga los elementos mínimos para ser acogida a trámite."
#### Applicable regulations
#### Titulo
Applicable Regulations
#### Contenido

ID: FORM-ESCRITO-INICIO-01-S0-NORMATIVA-01
Field-Label: "Normativa Aplicable"
Field-Type: Static-Text
Field-Placeholder: "Artículos 18, 21, 30 de la Ley N° 19.880."
Field-Instr: "Marco Legal: Rige el derecho de los interesados a iniciar procedimientos y los requisitos de sus solicitudes."
#### Header 5
#### Titulo
Header
#### Contenido

ID: FORM-ESCRITO-INICIO-01-S1-HEADER-01
#### Secciones
#### Summary
#### Titulo
Summary
#### Contenido

ID: FORM-ESCRITO-INICIO-01-S1-SUMILLA-01
Field-Label: "Sumilla"
Field-Type: Text
Field-Placeholder: "EN LO PRINCIPAL: [descripcion_breve_solicitud]; EN EL OTROSÍ: Acompaña documentos."
Field-Instr: "Claridad: La sumilla resume la petición principal y las secundarias para una rápida identificación por parte de la Oficina de Partes."
Field-Constraint: "Req: mandatory."
#### Addressee
#### Titulo
Addressee
#### Contenido

ID: FORM-ESCRITO-INICIO-01-S1-DESTINATARIO-01
Field-Label: "Destinatario"
Field-Type: Static-Text
Field-Placeholder: "S.S. EL GOBERNADOR REGIONAL DE ÑUBLE"
Field-Instr: "Autoridad: Identifica al órgano ante el cual se presenta la solicitud."
#### Body
#### Titulo
Body
#### Contenido

ID: FORM-ESCRITO-INICIO-01-S2-BODY-01
#### Secciones
#### Applicant identification
#### Titulo
Applicant Identification
#### Contenido

ID: FORM-ESCRITO-INICIO-01-S2-IDENTIFICACION-01
Field-Label: "Identificación del Solicitante"
Field-Type: TextArea
Field-Placeholder: "[nombre_completo], Cédula de Identidad N° [rut], profesión u oficio [profesion_oficio], domiciliado para estos efectos en [direccion], comuna de [comuna], correo electrónico [email], a US. respetuosamente digo:"
Field-Instr: "Legitimación: Identifica al interesado conforme al Art. 21 de la Ley 19.880. La indicación de un medio electrónico es fundamental bajo la nueva normativa de procedimiento administrativo electrónico."
Field-Constraint: "Req: mandatory."
#### Optional representation
#### Titulo
Optional Representation
#### Contenido

ID: FORM-ESCRITO-INICIO-01-S2-REPRESENTACION-01
Field-Label: "Representación (Opcional)"
Field-Type: TextArea
Field-Placeholder: "(Opcional) Actúo en representación de [nombre_representado], C.I./RUT N° [rut_representado], domiciliado en [direccion_representado], calidad que acredito con [documento_poder], que se acompaña."
Field-Instr: "Apoderamiento: Permite la actuación a través de un apoderado, conforme al Art. 22 de la Ley 19.880."
Field-Constraint: "Req: optional."
#### Facts
#### Titulo
Facts
#### Contenido

ID: FORM-ESCRITO-INICIO-01-S2-HECHOS-01
Field-Label: "Hechos"
Field-Type: TextArea
Field-Placeholder: "1. Que, con fecha [fecha_hechos], [descripcion_clara_y_circunstanciada_de_los_hechos]."
Field-Instr: "Fundamento Fáctico: Base fáctica de la petición. Los hechos deben ser expuestos con claridad y precisión para que la Administración pueda comprender la solicitud."
Field-Constraint: "Req: mandatory."
#### Law
#### Titulo
Law
#### Contenido

ID: FORM-ESCRITO-INICIO-01-S2-DERECHO-01
Field-Label: "Derecho"
Field-Type: TextArea
Field-Placeholder: "2. Que, en virtud de lo dispuesto en [normativa_aplicable_al_caso], y en atención a los hechos expuestos, me asiste el derecho a [descripcion_del_derecho_o_interes_legitimo]."
Field-Instr: "Fundamento Jurídico: Conecta los hechos con la norma que ampara la solicitud. Aunque no es estrictamente obligatorio para el particular, su inclusión facilita la tramitación."
Field-Constraint: "Req: optional."
#### Specific request
#### Titulo
Specific Request
#### Contenido

ID: FORM-ESCRITO-INICIO-01-S2-PETICION-01
Field-Label: "Petición Concreta"
Field-Type: TextArea
Field-Placeholder: "3. Que, en mérito de lo expuesto, solicito a US. se sirva dictar el acto administrativo que [lista_de_peticiones_claras_y_concretas]."
Field-Instr: "Petitorio: Debe ser claro, preciso y específico. La Administración debe resolver sobre lo pedido (Principio Conclusivo, Art. 8, Ley 19.880)."
Field-Constraint: "Req: mandatory."
#### Cierre 5
#### Titulo
Cierre
#### Contenido

ID: FORM-ESCRITO-INICIO-01-S3-CIERRE-01
#### Secciones
#### Por tanto
#### Titulo
Por Tanto
#### Contenido

ID: FORM-ESCRITO-INICIO-01-S3-PORTANTO-01
Field-Label: "Por Tanto"
Field-Type: Static-Text
Field-Placeholder: "POR TANTO,\n\nRUEGO A US. acceder a lo solicitado."
Field-Instr: "Fórmula de cierre de la petición principal."
#### Otrosi
#### Titulo
Otrosí
#### Contenido

ID: FORM-ESCRITO-INICIO-01-S3-OTROSI-01
Field-Label: "Otrosí"
Field-Type: TextArea
Field-Placeholder: "OTROSÍ: Ruego a US. tener por acompañados los siguientes documentos:\n\n1. [lista_documentos_adjuntos]."
Field-Instr: "Prueba: Permite adjuntar los antecedentes que sustentan la petición, conforme al Art. 30 de la Ley 19.880."
Field-Constraint: "Req: optional."
#### Signature
#### Titulo
Signature
#### Contenido

ID: FORM-ESCRITO-INICIO-01-S3-FIRMA-01
Field-Label: "Firma"
Field-Type: Static-Text
Field-Placeholder: "\n\n\n[Firma]\nC.I. N° [RUT]"
Field-Instr: "Autenticación: El escrito debe ser firmado por el interesado o su apoderado."

END_EMBEDDED_BLOCK:: FORM-ESCRITO-INICIO-01
```

```plaintext
BEGIN_EMBEDDED_BLOCK:: GUIDE-SFD-STS-MASTER-01 FORM-ESCRITO-REPO-01
#### Form metadata 6
#### Titulo
Form Metadata
#### Contenido

ID: FORM-ESCRITO-REPO-01-S0-METADATA-01
#### Secciones
#### Form description
#### Titulo
Form Description
#### Contenido

ID: FORM-ESCRITO-REPO-01-S0-DESC-01
Field-Label: "Descripción del Formulario"
Field-Type: Static-Text
Field-Instr: "Propósito: Modelo de escrito para interponer un recurso de reposición en contra de un acto administrativo del GORE Ñuble. Es el principal medio de impugnación en sede administrativa, permitiendo que la misma autoridad que dictó el acto revise su legalidad."
#### Applicable regulations
#### Titulo
Applicable Regulations
#### Contenido

ID: FORM-ESCRITO-REPO-01-S0-NORMATIVA-01
Field-Label: "Normativa Aplicable"
Field-Type: Static-Text
Field-Placeholder: "Artículo 59, Ley N° 19.880."
Field-Instr: "Marco Legal: Regula el recurso de reposición y el recurso jerárquico."
#### Header 6
#### Titulo
Header
#### Contenido

ID: FORM-ESCRITO-REPO-01-S1-HEADER-01

- Field-Group: Contiene los campos `Sumilla` y `Destinatario` de forma similar a FORM-ESCRITO-INICIO-01.
#### Body 2
#### Titulo
Body
#### Contenido

ID: FORM-ESCRITO-REPO-01-S2-BODY-01
#### Secciones
#### Appellant identification
#### Titulo
Appellant Identification
#### Contenido

ID: FORM-ESCRITO-REPO-01-S2-IDENTIFICACION-01
Field-Label: "Identificación del Recurrente"
Field-Type: Text
Field-Placeholder: "[nombre_completo], Cédula de Identidad N° [rut], en mi calidad de interesado en el procedimiento [identificacion_expediente], a US. respetuosamente digo:"
Field-Instr: "Legitimación: Identifica al recurrente como parte interesada en el procedimiento."
Field-Constraint: "Req: mandatory."
#### Contested act
#### Titulo
Contested Act
#### Contenido

ID: FORM-ESCRITO-REPO-01-S2-ACTOIMPUGNADO-01
Field-Label: "Acto Impugnado"
Field-Type: TextArea
Field-Placeholder: "Que, por este acto, y encontrándome dentro del plazo legal de cinco días hábiles establecido en el artículo 59 de la Ley N° 19.880, vengo en interponer recurso administrativo de reposición en contra de la Resolución Exenta N° [numero_res_impugnada], de fecha [fecha_res_impugnada], que me fuera notificada con fecha [fecha_notificacion], y que resolvió [resumen_decision_impugnada]."
Field-Instr: "Objeto y Plazo: Identifica el acto recurrido y declara expresamente la oportunidad del recurso. El plazo de 5 días hábiles desde la notificación es fatal. El agente IA debe calcular o advertir sobre este plazo."
Field-Constraint: "Req: mandatory."
#### Grounds for illegality
#### Titulo
Grounds for Illegality
#### Contenido

ID: FORM-ESCRITO-REPO-01-S2-FUNDAMENTOS-01
Field-Label: "Fundamentos de Ilegalidad"
Field-Type: TextArea
Field-Placeholder: "El acto recurrido adolece de los siguientes vicios de ilegalidad que lo hacen impugnable:\n\n1. [Vicio 1: descripción del vicio, norma infringida y argumento jurídico].\n2. [Vicio 2:...]."
Field-Instr: "Causa de Pedir: El recurso debe fundarse en vicios de legalidad del acto (incompetencia, vicios de forma, desviación de poder, ilegalidad en el contenido, falta de fundamentación), no en meros desacuerdos de mérito. La argumentación debe ser precisa."
Field-Constraint: "Req: mandatory."
#### Specific request
#### Titulo
Specific Request
#### Contenido

ID: FORM-ESCRITO-REPO-01-S2-PETICION-01
Field-Label: "Petición Concreta"
Field-Type: TextArea
Field-Placeholder: "En mérito de los fundamentos de hecho y de derecho expuestos, solicito a US. tener por interpuesto el presente recurso de reposición y, en definitiva, acogerlo, y en consecuencia, proceder a [peticion: dejar sin efecto, modificar, reemplazar] el acto recurrido, dictando en su lugar el acto que en derecho corresponda."
Field-Instr: "Petitorio: Define el alcance de la impugnación. La solicitud debe ser coherente con los vicios alegados."
Field-Constraint: "Req: mandatory."
#### Cierre 6
#### Titulo
Cierre
#### Contenido

ID: FORM-ESCRITO-REPO-01-S3-CIERRE-01

- Field-Group: Contiene los campos `Por Tanto`, `Otrosí` y `Firma` de forma similar a FORM-ESCRITO-INICIO-01.

END_EMBEDDED_BLOCK:: FORM-ESCRITO-REPO-01
```
## Contenido
\# Modelos de Actos Jurídicos GORE Ñuble

ID: KB-GN-100-MODELOS-ACTOS-JURIDICOS-STS-V3
Version: 3.0.0
Status: Draft
Human-Creator: FS
Human-Editor: FS
Model-Collaborator: IA-GEMINI
Creation-Date: 2025-07-10
Modification-Date: 2025-07-10
Ref-STS-Guide: GUIDE-STS-MASTER-01
