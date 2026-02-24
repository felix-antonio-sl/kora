---
_manifest:
  urn: "urn:gn:kb:omega-ipr-gestion-fusion"
  provenance:
    created_by: "FS"
    created_at: "2026-01-29"
    source: "GORE Ñuble"
version: "2.0.0"
status: published
tags: [gore-nuble, gobierno-regional, finanzas-publicas, gestion-ipr]
lang: es
---

# Ontología Ω-IPR: Gestión y Fusión de Financiamiento

## Entidades Fundamentales (Ω-Objects)

### Intervenciones Públicas Regionales (IPR)

| ID | Nombre | Descripción | Subtítulos | Vía/Condición |
| :--- | :--- | :--- | :--- | :--- |
| **Ω-IDI** | Iniciativa de Inversión | Proyectos de capital (activos) | 31, 33 | MDSF |
| **Ω-PPR** | Programa Público Regional | Gasto corriente o mixto | 24 | Glosa 06 / Transferencias |
| **Ω-ESTUDIO** | Estudio Básico | Análisis técnico previo | C33 | MEC-C33-ESTUDIOS |
| **Ω-ANF** | Activos No Financieros | Compra de activos aislados | C33 | Cofinanciamiento min. 20% |
| **Ω-CONSERVACION** | Proyecto de Conservación | Mantención de activos | C33 | Costo ≤ 30% reposición |
| **Ω-SUBVENCION** | Subvención 8% FNDR | Vinculación comunitaria | - | MEC-SUBV8 |

### Mecanismos de Financiamiento (Fibras)

#### Mecanismos para Proyectos
- **MEC-SNI-GENERAL**: Evaluación MDSF completa. Dictamen: RATE.
- **MEC-FRIL**: Infraestructura menor < 5000 UTM. Ejecutor: Municipal. Tope regional Ñuble: 4545 UTM. Dictamen: Aprobación Técnica.
- **MEC-C33-CONSERVACION**: Mantención activos. Requiere AD (MDSF). Costo ≤ 30% reposición.
- **MEC-C33-ANF**: Adquisición activos. Requiere AD (MDSF). Cofinanciamiento ≥ 20%.
- **MEC-C33-ESTUDIOS**: Estudios técnicos para terceros. Requiere AD (MDSF).
- **MEC-5000UTM**: Exento de RS por monto. Dictamen: Aprobación Técnica GORE.
- **MEC-FRPD-CAPITAL**: Royalty inversión productiva. Evaluador: Comité FRPD (CORFO, ANID, Universidades).

#### Mecanismos para Programas
- **MEC-G06-DIRECTA**: Glosa 06 Ejecución Directa GORE. Evaluador: DIPRES/SES. Dictamen: RF. Proceso: Bifásico (Perfil/Diseño).
- **MEC-TRANSFER-PUB**: Ejecución por otra entidad pública. Evaluador: GORE. Dictamen: ITF. Proceso: Trifásico (Admisibilidad/Pertinencia/Técnica). Exento de SNI/DIPRES.
- **MEC-SUBV8**: Vinculación comunitaria. Destinatarios: Organizaciones, Municipios, Privados SFL. Dictamen: Concurso.
- **MEC-FRPD-PROGRAMA**: Royalty programas fomento. Dictamen: Concurso.
- **MEC-EMERGENCIA**: Ayudas tempranas. Evaluador: GORE + Min. Interior. Dictamen: Exento (G06 ex-ante).

### Sistemas de Dictamen (Mónadas)

| Sistema | Fuente | Plataforma | Aplicación | Resultados (Outputs) |
| :--- | :--- | :--- | :--- | :--- |
| **RATE** | MDSF | BIP | SNI, C33 | RS, FI, OT, AD |
| **RF** | DIPRES/SES | Formularios | Glosa 06 | RF, FI, OT |
| **ITF** | GORE | GESDOC | Transferencias | ITF_OK, ITF_OBS, NO_REC (Paralelo a RS) |
| **CONCURSO** | Comité | - | 8%, FRPD | ELEGIBLE, NO_ELEGIBLE, LISTA_ESPERA |

### Actores del Sistema

#### Autoridades y Divisiones GORE
- **GOBERNADOR**: Firma actos administrativos.
- **ADMIN-REGIONAL**: Coordinación operativa.
- **DIPIR**: División de Presupuesto e Inversión Regional.
- **DIPLADE**: División de Planificación y Desarrollo Regional.
- **DAF**: División de Administración y Finanzas.
- **PREINVERSION**: Departamento DIPIR.
- **PRESUPUESTO**: Departamento DAF.
- **JURIDICO**: Visación legal.
- **CONTROL**: Control interno.

#### Instancias Colegiadas y Externos
- **CDR**: Comité Directivo Regional. Filtro de pertinencia estratégica.
- **CORE**: Consejo Regional. Aprobación financiera (Obligatorio > 7000 UTM).
- **MDSF/SES**: Evaluación técnico-económica (RATE/RF).
- **DIPRES**: Presupuestos y visaciones Glosa 06.
- **CGR**: Contraloría General. Toma de Razón y SISREC.
- **SUBDERE**: Administración FRIL.
- **UT-RECEPTORA**: Unidad Técnica ejecutora (Municipios, Servicios, Universidades, ONG).

### Documentos y Artefactos
- **CDP**: Certificado de Disponibilidad Presupuestaria.
- **CERTIFICADO_CORE**: Documento de acuerdo del Consejo.
- **CONVENIO**: Contrato de transferencia de fondos.
- **RESOLUCION**: Acto administrativo que aprueba el convenio.
- **DECRETO**: Modificación presupuestaria oficial.
- **RENDICION**: Cuentas en plataforma SISREC.

## Ciclo de Vida y Procesos (Ω-Processes)

### Fases del Proceso Operativo

#### Fase 1: Ingreso y Admisibilidad
- **P-INGRESAR**: Registro en Oficina de Partes.
- **P-FILTRAR-CDR**: Evaluación de coherencia ERD y viabilidad preliminar.
- **P-REVISAR-FORMAL**: Revisión de admisibilidad documental por DIPIR.

#### Fase 2: Evaluación
- **P-EVALUAR-SNI**: Evaluación MDSF. Plazos: 5 días admisibilidad, 10 días ATE. Subsanación: 60 días hábiles.
- **P-EVALUAR-PPR**: Evaluación DIPRES/SES para Glosa 06 (Perfil y Diseño).
- **P-EVALUAR-TRANSFER**: Evaluación interna GORE (ITF).

#### Fase 3: Financiamiento y Formalización
- **P-APROBAR-CORE**: Aprobación política. Obligatorio si IDI > 7000 UTM.
- **P-EMITIR-CDP**: Reserva presupuestaria por Depto. Presupuesto.
- **P-FORMALIZAR-CONVENIO**: Firma bilateral GORE-Unidad Técnica.
- **P-TRAMITAR-RESOLUCION**: Resolución aprobatoria y Toma de Razón CGR.

#### Fase 4: Ejecución y Cierre
- **P-EJECUTAR**: Transferencia de fondos y seguimiento físico-financiero.
- **P-MODIFICAR**: Gestión de cambios (puede requerir CORE/SNI).
- **P-CERRAR-TECNICO**: Acta de recepción por Supervisor GORE.
- **P-CERRAR-FINANCIERO**: Rendición de cuentas final aprobada por DAF.

### Estados del Ciclo de Vida (Ω-Coalgebra)

- **Ingreso**: FORMULACION → POSTULADA → PRE_ADMISIBLE_CDR → ADMISIBLE.
- **Evaluación**: ENVIADO_MDSF/DIPRES → RS / RF / AD / FI / OT → APROBADO_TECNICO.
- **Financiamiento**: CARTERA_CORE → APROBADO_CORE → CDP_EMITIDO.
- **Formalización**: CONVENIO_FIRMADO → CONVENIO_TRAMITADO → TRANSFERENCIA_PROGRAMADA.
- **Ejecución**: EN_EJECUCION → LICITACION / CONTRATO / OBRA.
- **Cierre**: CIERRE_TECNICO → CIERRE_FINANCIERO → CERRADO.
- **Terminales**: CERRADO, INADMISIBLE_INFORMADO, OT (Objetado), RECHAZADO_CORE, NO_PRE_ADMISIBLE.

## Mapeo y Axiomas (Ω-Profunctor)

### Mapeo Selector ↔ Gestión (Profunctor Π)

| Selector (Mecanismo) | Gestión Fase 2 (Track) | Gestión Fase 3 (Financiamiento) | Dictamen |
| :--- | :--- | :--- | :--- |
| MEC-SNI-GENERAL | Track A (SNI) | Con CORE | RATE (RS) |
| MEC-FRIL | Track C (FRIL) | Sin CORE | Aprobación Técnica |
| MEC-G06-DIRECTA | Track B (PPR) | Con CORE | RF |
| MEC-TRANSFER-PUB | Eval. Interna GORE | Con CORE | ITF |
| MEC-SUBV8 | Concurso Competitivo | Concurso/Directa | CONCURSO |
| MEC-FRPD-CAPITAL | FRPD-FASE3-GORE | Según Tipo | CONCURSO |

### Axiomas e Invariantes Categóricos

- **AX-DETERMINISMO**: El mecanismo de financiamiento determina unívocamente el track de evaluación.
- **AX-7000-UTM**: Toda Iniciativa de Inversión (IDI) > 7000 UTM requiere aprobación obligatoria del CORE.
- **AX-PULLBACK**: La admisibilidad es un límite estricto; el cumplimiento de requisitos sobre documentos presentados es binario.
- **AX-MONAD-BIND**: Los estados FI (Falta Información) y OT (Objetado) detienen el flujo; RS/RF/AD/ITF habilitan la fase siguiente.
- **AX-TRANSPORT**: Cambiar de mecanismo (ej. FRIL a SNI por exceso de monto) requiere reevaluación completa bajo las nuevas reglas.
- **AX-EXENTO**: La exención de evaluación centralizada (SNI/DIPRES) NO implica ausencia de evaluación técnica rigurosa por parte del GORE.
- **AX-EXCLUSIVIDAD**: Cada mecanismo tiene exactamente un sistema de dictamen aplicable.
