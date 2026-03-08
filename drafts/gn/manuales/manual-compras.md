---
_manifest:
  urn: urn:gn:kb:manual-compras
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-08'
    source: domains/gn/03_operacion/gestion/kb_gn_046_manual_compras_koda.yml
version: 2.0.0
status: draft
tags:
- gore-nuble
- gobierno-regional
- compras-publicas
- chilecompra
- mercado-publico
- gn
lang: es
extensions:
  gn:
    source_paths:
    - domains/gn/03_operacion/gestion/kb_gn_046_manual_compras_koda.yml
    source_hashes:
      domains/gn/03_operacion/gestion/kb_gn_046_manual_compras_koda.yml: d8a0c38e5fb27d0017067ea4a3c0dd66fe3f89a0fcc7326e03e4ade56d084b96
    source_type: koda_yaml
    transformation_mode: korafy_direct
    fs: 100
    cr: 1.14
    run_id: gn-smoke
    review_gate: auto
    scope_statement: null
    dependencies: []
    expected_sections:
    - Contenido
    skeleton_count: 18
    meat_count: 261
    fat_count: 0
    cr_justification: Fuente altamente estructurada o derivacion de alcance acotado.
    evidence_path: build/gn-rebuild/gn-smoke/evidence/manuales__manual-compras.md.json
---

# Manual 2.1: Compras Públicas y Contrataciones
## ID
MANUAL-COMPRAS-CONTRATACIONES-01

## Version
1.0.0

## Status
Draft

## Format
KODA/Spec

## Human Creator
GORE Ñuble

## Human Editor
FS

## Model Collaborator
IA-CASCADE

## AI Remediator
KODA-TRANSFORMER

## Creation Date
2025-12-14

## Modification Date
2025-12-16

## Primary Source
staging/brow_speculativo/manual_2_1_compras.md

## Ctx
Manual: Compras Públicas y Contrataciones (GORE Ñuble).

## Authoritative Source
### Path
staging/temp/brutos ordenados/04_adquisiciones_activos/Manual-de-Adquisiciones-GORE_Ñuble_3R.md
### Priority
1
### Type
Official-Manual-DAF
### Last Validated
2025-12-18

## Source Hierarchy
| Level | Description |
| --- | --- |
| 1 | Fuentes Brutas Ordenadas (staging/temp/brutos ordenados/*) |
| 2 | Pseudo-manuales KB (knowledge/domains/gn/gestion/pseudo_manuales_operativos/*) |
| 3 | Fuentes Especulativas (staging/brow_speculativo/*) |

## LLM Parsing Instructions
### ID
KODA-LLM-PARSER-01
### Req
Mandatory block following Metadata.
### Prohib
Using for artifact creation or translation.
### Content
BEGIN_LLM_INSTRUCTIONS
You are an AI agent consuming a KODA artifact. Parse with absolute fidelity.

FIDELITY: Preserve meat (essential information) and skeleton (structure: headers, IDs, lists, tables) with zero loss. Ignore fat (filler words, rhetoric, stylistic prose).

LEXICON (expand before processing): Act->Action, Cond->Condition, Ctx->Context, Ctx_Required->Required External Reference, Ctx_Optional->Optional External Reference, Def->Definition, Ex->Example, Mssn->Mission, Obj->Objective, Proc->Process, Purp->Purpose, Ref->Reference, XRef->Cross-Artifact Reference, XRef_Required->Mandatory Cross-Artifact Reference, Req->Requirement, Res->Result, Src->Source, Prohib->Prohibition, Warn->Warning, Just->Justification, Rec->Recommendation

REFERENCE POLICY: Ref: is internal only—must point to existing ID within THIS document. XRef/XRef_Required: are external only—must point to a URN (optionally with #ID fragment) in another artifact. External documents without specific ID use Ctx:, Ctx_Required:, or Ctx_Optional:.

LANGUAGE POLICY: Keywords in English (and abbreviated forms as listed), content in original language (Spanish). Never translate content.
END_LLM_INSTRUCTIONS


## Manual 2 1 Compras Publicas y Contrataciones
### ID
MANUAL-COMPRAS-CONTRATACIONES-CONTENT-01
### Obj
Normar la adquisición de bienes y servicios garantizando transparencia, eficiencia y cumplimiento de la Ley N° 19.886 de Compras Públicas y su Reglamento.
### Seccion I Marco Normativo y Principios Rectores
#### ID
MANUAL-COMPRAS-SEC-I-01
#### 1 Fundamentos Legales
#### ID
MANUAL-COMPRAS-SEC-I-FUND-01
#### Ctx
La gestión de compras del GORE se rige por:
#### Fuentes
| Src |
| --- |
| Ley N° 19.886 y Modificación Ley 21.634 (Compras 2.0): Moderniza la gestión de compras públicas. |
| Decreto N° 661 (2024): Nuevo Reglamento de la Ley de Compras (vigencia 12/2024). |
| Ley de Presupuestos (Partida 31). |
| Directivas ChileCompra. |
| Ley 21.180 (Transformación Digital). |
#### Nuevos Umbrales y Modalidades (Decreto 661/2024)
#### ID
MANUAL-COMPRAS-SEC-I-UMBRALES-01
#### Tabla Maestra
-
  #### Rango
  < 3 UTM
  #### Modalidad
  Fondos Globales (Caja Chica) o Portal Mercado Público.
-
  #### Rango
  3 a 100 UTM
  #### Modalidad
  Compra Ágil (Preferente). Mínimo 3 cotizaciones en el sistema.
-
  #### Rango
  100 a 1.000 UTM
  #### Modalidad
  Licitación Pública (Normas Simplificadas). Contrato opcional (puede formalizarse con OC).
-
  #### Rango
  > 1.000 UTM
  #### Modalidad
  Licitación Pública (Normas Generales). Contrato obligatorio y Garantía de Fiel Cumplimiento.
-
  #### Rango
  > 5.000 UTM
  #### Req
  Garantía de Seriedad de la Oferta obligatoria (máximo 3% del monto).
#### 2 Principios Rectores
#### ID
MANUAL-COMPRAS-SEC-I-PRINCIPIOS-01
#### Principios
| Principio | Req |
| --- | --- |
| Libre Concurrencia | Garantizar la participación de todos los proveedores que cumplan requisitos. |
| Igualdad de Trato | No discriminar entre oferentes por razones ajenas al mérito técnico-económico. |
| Transparencia | Publicar bases, aclaraciones, evaluaciones y adjudicaciones en www.mercadopublico.cl. |
| Eficiencia | Optimizar la relación calidad-precio en las adquisiciones. |
| Probidad | Evitar conflictos de interés y declarar inhabilidades. |
#### 3 Glosario de Terminos
#### ID
MANUAL-COMPRAS-SEC-I-GLOSARIO-01
#### Terminos
-
  #### ID
  MANUAL-COMPRAS-GLOS-PAC
  #### Sigla
  PAC
  #### Def
  Plan Anual de Compras.
-
  #### ID
  MANUAL-COMPRAS-GLOS-OC
  #### Sigla
  OC
  #### Def
  Orden de Compra emitida en Mercado Público.
-
  #### ID
  MANUAL-COMPRAS-GLOS-CONVENIO-MARCO
  #### Termino
  Convenio Marco
  #### Def
  Acuerdo suscrito por ChileCompra con proveedores para compras directas a precios predefinidos.
-
  #### ID
  MANUAL-COMPRAS-GLOS-CDP
  #### Sigla
  CDP
  #### Def
  Certificado de Disponibilidad Presupuestaria.
-
  #### ID
  MANUAL-COMPRAS-GLOS-RECEPCION-CONFORME
  #### Termino
  Recepción Conforme
  #### Def
  Acto formal que valida la entrega satisfactoria del bien o servicio.
### Seccion II Planificacion de Compras
#### ID
MANUAL-COMPRAS-SEC-II-01
#### 4 Plan Anual de Compras PAC
#### ID
MANUAL-COMPRAS-SEC-II-PAC-01
#### Def
El PAC es el instrumento de planificación que articula necesidades con presupuesto disponible.
#### Elaboracion
#### Responsable
Cada División/Departamento
#### Act
Envía requerimientos a la Unidad de Abastecimiento
#### Plazo
Antes del 15 de Noviembre del año anterior
#### Consolidacion
#### Responsable
Unidad de Abastecimiento
#### Act
Integra y prioriza las necesidades
#### Criterios de Priorizacion
| Criterio |
| --- |
| Criticidad operativa. |
| Disponibilidad presupuestaria. |
| Alineamiento con metas institucionales. |
#### Aprobacion
#### Responsable
Administrador Regional
#### Act
Aprueba el PAC consolidado
#### Ctx
Mediante Resolución Exenta.
#### Publicacion
#### Responsable
Unidad de Abastecimiento
#### Act
Publica en Mercado Público
#### Plazo
Dentro de los primeros 30 días del año calendario
#### Modificaciones
#### Cond
Durante el año
#### Req
Permitidas mediante resolución fundada
#### Req Actualizacion
| Req |
| --- |
| Actualizar la publicación en el portal. |
#### 5 Tipos de Requerimientos
#### ID
MANUAL-COMPRAS-SEC-II-REQS-01
#### Tipos
| Tipo | Def |
| --- | --- |
| Planificados (PAC) | Incluidos en la programación anual. |
| Extraordinarios | Necesidades imprevistas que requieren justificación escrita del área solicitante y visación DAF. |
| Urgentes | Situaciones de emergencia que permiten plazos abreviados según Reglamento (Art. 43). |
#### 6 Reserva Presupuestaria Previa
#### ID
MANUAL-COMPRAS-SEC-II-RESERVA-01
#### Prohib
Ningún proceso de compra inicia sin CDP vigente.
#### Reqs
| Req |
| --- |
| El CDP debe emitirse desde el sistema financiero antes de la publicación del llamado o emisión de la OC. |
| La pre-afectación bloquea los recursos hasta la adjudicación o desistimiento. |
### Seccion III Mecanismos de Compra
#### ID
MANUAL-COMPRAS-SEC-III-01
#### 7 Convenio Marco CM
#### ID
MANUAL-COMPRAS-SEC-III-CM-01
#### Def
Modalidad preferente para bienes y servicios estandarizados.
#### Catalogo ChileCompra
#### Ctx
Se accede vía tienda electrónica en www.mercadopublico.cl.
#### Proceso
#### Proc
| Act |
| --- |
| Selección de producto |
| Emisión de OC |
| Aceptación proveedor |
| Despacho/Prestación |
#### Ventaja
#### Res
No requiere proceso licitatorio individual.
#### Restriccion
#### Prohib
No aplica para bienes o servicios no catalogados.
#### 8 Licitacion Publica
#### ID
MANUAL-COMPRAS-SEC-III-LP-01
#### Req
Obligatoria para compras de bienes, servicios y ejecución de proyectos de inversión (Subtítulo 31) superiores a 1.000 UTM (salvo Convenio Marco).
#### Bases Administrativas
#### Ctx
Condiciones generales, plazos, garantías, causales de inadmisibilidad.
#### Bases Tecnicas
#### Ctx
Especificaciones del bien o servicio, criterios de evaluación técnica.
#### Publicacion
#### Plazos
- Mínimo 20 días corridos para ofertar (licitación normal).
- 10 días (licitación abreviada por monto < 100 UTM).
#### Criterios de Evaluacion
#### Req
Deben definirse en las bases con ponderaciones claras (Técnico, Económico, Plazos, etc.).
#### Comision Evaluadora
#### Reqs
| Req |
| --- |
| Mínimo 3 integrantes designados por resolución. |
| Incluye al menos un funcionario del área técnica requirente. |
#### Acta de Evaluacion
#### Req
Documento fundado que justifica la puntuación de cada oferente.
#### Adjudicacion
#### Req
Por Resolución Exenta del Gobernador Regional, publicada en el portal.
#### 9 Licitacion Privada y Trato Directo
#### ID
MANUAL-COMPRAS-SEC-III-EXCEPCIONES-01
#### Def
Modalidades excepcionales sujetas a causales legales taxativas.
#### Trato Directo Art 8 Ley 19886
#### ID
MANUAL-COMPRAS-SEC-III-TD-01
#### Causales
| Causal |
| --- |
| Proveedor único. |
| Emergencias calificadas. |
| Compras < 10 UTM. |
| Contratos de prórroga por continuidad de servicio (máximo 12 meses). |
#### Requisitos
| Req |
| --- |
| Resolución fundada que invoque la causal específica. |
| Publicación en Mercado Público (salvo montos menores). |
| Visación del Jefe DAF para montos > 100 UTM. |
#### 10 Grandes Compras Licitaciones mayores a 5000 UTM
#### ID
MANUAL-COMPRAS-SEC-III-GRANDES-01
#### Reqs
| Req |
| --- |
| Requieren visación previa de la División Jurídica sobre las bases. |
| Garantía de seriedad de la oferta obligatoria (generalmente 5% del presupuesto estimado). |
| Plazo de ofertas mínimo 30 días corridos. |
| Evaluación técnica puede incluir visitas a terreno o demostraciones. |
### Seccion IV Ejecucion de Ordenes de Compra
#### ID
MANUAL-COMPRAS-SEC-IV-01
#### 11 Generacion de la OC
#### ID
MANUAL-COMPRAS-SEC-IV-OC-01
#### Def
La OC es el acto administrativo que formaliza el compromiso con el proveedor.
#### Reqs
| Req |
| --- |
| Se emite en Mercado Público tras la adjudicación (licitaciones) o selección (CM/Trato Directo). |
#### Contenido Obligatorio
| Req |
| --- |
| Descripción detallada del bien/servicio. |
| Cantidad y precio unitario. |
| Plazo de entrega/ejecución. |
| Lugar de entrega. |
| Imputación presupuestaria (Subtítulo/Ítem/Asignación). |
#### 12 Aceptacion y Rechazo
#### ID
MANUAL-COMPRAS-SEC-IV-ACEPTACION-01
#### Plazo
48 horas hábiles
#### Req
El proveedor tiene 48 horas hábiles para aceptar la OC en el portal (salvo indicación distinta en bases).
#### Res
OC rechazada o no aceptada permite re-adjudicar al siguiente oferente mejor evaluado.
#### 13 Recepcion Conforme
#### ID
MANUAL-COMPRAS-SEC-IV-RECEPCION-01
#### Def
Hito crítico que habilita el devengo y posterior pago.
#### Bienes
#### Proc
| Act |
| --- |
| La bodega o área solicitante verifica cantidad, calidad y concordancia con OC. |
| Genera Acta de Recepción física o digital. |
#### Servicios
#### Proc
-
  #### Responsable
  Administrador del contrato
-
  #### Act
  Certifica el cumplimiento mediante Informe de Conformidad.
#### Integracion Contable
#### Res
La recepción conforme genera automáticamente el devengo presupuestario y el pasivo contable (Cuentas por Pagar).
#### Pago Electronico Obligatorio
#### ID
MANUAL-COMPRAS-SEC-IV-PAGO-ELECTRONICO-01
#### Src
Art. 8 de la Ley de Presupuestos
#### Req
Todos los pagos a proveedores deben realizarse exclusivamente mediante transferencia electrónica de fondos.
#### Prohib
Pago en efectivo o cheque, salvo excepciones legalmente autorizadas.
#### Nota Recepcion Fisica Bienes
#### Ctx Optional
Para el procedimiento detallado de recepción física de bienes, consulte el Manual 2.2: Inventarios (./manual_2_2_inventarios.md) §7.
#### 14 Devoluciones y Reclamos
#### ID
MANUAL-COMPRAS-SEC-IV-DEVOLUCIONES-01
#### Plazo
8 días corridos
#### Reqs
| Req |
| --- |
| Plazo de 8 días corridos desde la recepción para reclamar la factura electrónica en el SII. |
| Devoluciones por no conformidad deben documentarse con Acta de Rechazo indicando las causales. |
| El proveedor tiene plazo según contrato/OC para subsanar o reemplazar. |
### Seccion V Gestion de Contratos
#### ID
MANUAL-COMPRAS-SEC-V-01
#### 15 Formalizacion de Contratos
#### ID
MANUAL-COMPRAS-SEC-V-FORMALIZACION-01
#### Req
Obligatorio para:
#### Casos
| Caso |
| --- |
| Licitaciones > 100 UTM. |
| Servicios de tracto sucesivo. |
| Obras civiles. |
#### Contenido del Contrato
| Req |
| --- |
| Identificación de las partes. |
| Objeto y alcance. |
| Precio y modalidad de pago (hitos, mensualidades, etc.). |
| Plazos de ejecución. |
| Garantías exigidas. |
| Multas y sanciones. |
| Causales de término anticipado. |
#### 16 Administracion del Contrato
#### ID
MANUAL-COMPRAS-SEC-V-ADMIN-01
#### Administrador del Contrato
#### Req
Funcionario designado por resolución, responsable del seguimiento técnico y cumplimiento de hitos.
#### Libro de Obra Bitacora
#### Req
Registro de incidencias, instrucciones y acuerdos durante la ejecución (obligatorio en contratos de obra).
#### Estados de Pago
#### Def
Documentos que certifican el avance para liberar pagos parciales según hitos.
#### Modificaciones
#### Reqs
| Req |
| --- |
| Aumentos o disminuciones de hasta 30% del monto original requieren resolución fundada. |
| Sobre 30% requieren nueva licitación. |
#### 17 Garantias Contractuales
#### ID
MANUAL-COMPRAS-SEC-V-GARANTIAS-01
#### Tipos
| Tipo | Def |
| --- | --- |
| Seriedad de la Oferta | Devuelta tras adjudicación a oferentes no seleccionados. |
| Fiel Cumplimiento | Generalmente 5% del monto contratado, vigente hasta recepción final + plazo de responsabilidad. |
| Correcta Ejecución (Obras) | Puede exigirse por el plazo de responsabilidad post-recepción (típicamente 12 meses). |
#### Custodia
#### Ctx
Las garantías físicas (boletas, pólizas) se custodian en Tesorería. Las electrónicas se registran en el sistema de garantías.
#### 18 Multas y Sanciones
#### ID
MANUAL-COMPRAS-SEC-V-MULTAS-01
#### Reqs
| Req |
| --- |
| Deben estar contempladas en las bases y el contrato. |
| Causales típicas: Atraso en entrega, incumplimiento parcial, calidad deficiente. |
#### Procedimiento
#### Proc
-
  #### Act
  Informe del administrador
-
  #### Act
  Notificación al proveedor
-
  #### Plazo
  Plazo de descargos (5 días hábiles)
-
  #### Act
  Resolución que aplica o desestima la multa.
#### Cobro
#### Proc
| Act |
| --- |
| Descuento directo de estados de pago |
| Ejecución de garantía |
#### 19 Termino del Contrato
#### ID
MANUAL-COMPRAS-SEC-V-TERMINO-01
#### Tipos
| Tipo | Def |
| --- | --- |
| Término Natural | Cumplimiento del objeto en plazo. |
| Término Anticipado | Por incumplimiento grave, mutuo acuerdo, o causales de fuerza mayor. |
| Recepción Final | Acta que cierra el contrato y libera garantías (tras plazo de responsabilidad si aplica). |
### Seccion VI Control Transparencia y Evaluacion
#### ID
MANUAL-COMPRAS-SEC-VI-01
#### 20 Interoperabilidad con Mercado Publico
#### ID
MANUAL-COMPRAS-SEC-VI-INTEROP-01
#### Reqs
| Req |
| --- |
| Toda operación debe reflejarse en www.mercadopublico.cl. |
| El sistema institucional (SIGAS o equivalente) debe sincronizar OC, estados de pago y recepciones. |
| Descarga automática de actas de adjudicación para trazabilidad. |
#### 21 Portal de Proveedores
#### ID
MANUAL-COMPRAS-SEC-VI-PORTAL-01
#### Def
Herramienta de transparencia que permite a proveedores consultar:
#### Funcionalidades
| Funcionalidad |
| --- |
| Estado de sus órdenes de compra. |
| Estado de facturas y pagos. |
| Historial de transacciones. |
#### 22 Evaluacion de Proveedores
#### ID
MANUAL-COMPRAS-SEC-VI-EVAL-01
#### Frecuencia
- Al cierre de cada contrato
- Anualmente para contratos de tracto sucesivo
#### Criterios
- Cumplimiento de plazos
- Calidad del producto/servicio
- Respuesta ante incidencias
#### Registro
#### Req
La calificación se incorpora al Historial de Proveedores institucional.
#### Consecuencias
#### Res
Proveedores con evaluación deficiente pueden ser excluidos de futuras licitaciones (según bases).
#### 23 Reportes y Auditoria
#### ID
MANUAL-COMPRAS-SEC-VI-REPORTES-01
#### Reportes
- Informe Mensual de Compras: Resumen de OC emitidas, montos, mecanismos utilizados.
- Informe de Contratos Vigentes: Estado de avance, hitos pendientes, alertas de vencimiento.
#### Indicadores de Gestion
| Indicador |
| --- |
| % de compras vía Convenio Marco. |
| % de licitaciones declaradas desiertas. |
| Tiempo promedio de adjudicación. |
| Cumplimiento de plazos de pago a 30 días. |
### Nota Final
#### Ctx
Este manual establece los lineamientos para una gestión de compras eficiente, transparente y conforme a la normativa de contratación pública.

## Referencias Cruzadas
### ID
GN-MANUAL-COMPRAS-XREF-01
### Ctx Optional
- knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_1_1_presupuesto.yml
- knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_1_2_contabilidad.yml
- knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_1_3_tesoreria_koda.yml
- knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_2_2_inventarios.yml
- knowledge/domains/gn/gestion/pseudo_manuales_operativos/manual_3_2_remuneraciones.yml
