---
_manifest:
  urn: urn:gn:kb:manual-presupuesto
  provenance:
    created_by: gn_rebuild.py
    created_at: '2026-03-09'
    source: domains/gn/03_operacion/gestion/kb_gn_043_manual_presupuesto_koda.yml
version: 2.0.0
status: published
tags:
- gore-nuble
- gobierno-regional
- presupuesto
- sigfe
- fndr
- gn
lang: es
extensions:
  gn:
    source_paths:
    - domains/gn/03_operacion/gestion/kb_gn_043_manual_presupuesto_koda.yml
    source_hashes:
      domains/gn/03_operacion/gestion/kb_gn_043_manual_presupuesto_koda.yml: 2fd27082c96bc49473323ed93d8e54394b1e1d5a9fac13e69880c9abeec64e86
    source_type: koda_yaml
    transformation_mode: korafy_direct
    fs: 100
    cr: 1.74
    run_id: gn-smoke
    review_gate: auto
    scope_statement: null
    dependencies: []
    expected_sections:
    - Contenido
    document_family: generic
    publication_class: knowledge
    skeleton_count: 3
    meat_count: 250
    fat_count: 0
    evidence_path: build/gn-rebuild/gn-smoke/evidence/manuales__manual-presupuesto.md.json
---

# Manual 1.1: Formulación y Ejecución Presupuestaria

## Definiciones

### Organos y Unidades
| ID | Def |
| --- | --- |
| DEF-DIPRES | DIPRES (Dirección de Presupuestos): Ente rector que define instrucciones, techos y autoriza modificaciones mayores. |
| DEF-GOBERNADOR-REGIONAL | Gobernador Regional: Responsable de proponer el presupuesto al CORE y ejecutarlo. |
| DEF-CORE | Consejo Regional (CORE): Aprueba presupuesto inicial y modificaciones mayores; fiscaliza la ejecución. |
| DEF-DIPIR | División de Presupuesto e Inversión Regional (DIPIR): Unidad técnica responsable de gestión diaria del presupuesto, control de saldos y visación de gastos. |

### Sistemas y Codigos
| ID | Def |
| --- | --- |
| DEF-SIGFE | SIGFE: Sistema central (módulo formulación y registro ejecución) para gestión financiera del Estado. |
| DEF-BIP | BIP: Banco Integrado de Proyectos; código requerido para proyectos de inversión. |
| DEF-IDI | IDI: Iniciativa (proyecto) de inversión; se controla por código (BIP) y no se mezclan fondos entre proyectos. |

### Instrumentos y Fondos
| ID | Def |
| --- | --- |
| DEF-FNDR | FNDR: Principal fuente de recursos para inversiones; se subdivide en asignaciones regionales (decisión GORE) y provisiones (decisión central/mixta). |
| DEF-FRPD | FRPD: Recursos destinados a fomento productivo, ciencia e innovación. |
| DEF-PAC | PAC (Programación Anual de Caja): Proyecta flujo de ingresos y egresos para asegurar liquidez para cumplir obligaciones. |

### Cadena Presupuestaria
| ID | Def |
| --- | --- |
| DEF-CDP | CDP (Certificado de Disponibilidad Presupuestaria): Documento previo obligatorio que certifica saldo; ningún proceso de compra o convenio inicia sin CDP. |
| DEF-COMPROMISO | Compromiso: Acto administrativo (OC/Contrato/Resolución Convenio) que afecta el presupuesto; reserva recursos definitivamente para un tercero. |
| DEF-DEVENGO | Devengo: Hito de recepción conforme; genera obligación de pago y pasivo contable; debe ser simultáneo a recepción de factura/bien. |
| DEF-PAGO | Pago: Egreso efectivo de fondos que extingue la obligación. |

### Cierre
| ID | Def |
| --- | --- |
| DEF-SIC | SIC: Saldo Inicial de Caja. |
| DEF-DEUDA-FLOTANTE | Deuda Flotante: Obligaciones devengadas al 31/12 pendientes de pago. |
| DEF-ITEM-DEUDA-FLOTANTE | Ítem 34.07 'Deuda Flotante': se crea en presupuesto del año siguiente para registrar financiamiento. |

## Manual 1 1 Formulacion y Ejecucion Presupuestaria

### Objetivos
- Estandarizar ciclo de vida de recursos financieros regionales.
- Asegurar cumplimiento Ley de Presupuestos del Sector Público y normativa SAF del Estado.

### Seccion I Marco Conceptual y Estructura

#### Clasificador Presupuestario

#### Contexto
Estructura presupuestaria GORE Ñuble.

#### Estructura

#### Partida
| Partida | Def |
| --- | --- |
| 31 | Identifica a los Gobiernos Regionales. |

#### Capitulos
| Capitulo | Def |
| --- | --- |
| 01 Gobierno Regional | Ejecución administrativa y operativa. |
| 02 Consejo Regional | Gastos funcionamiento CORE (dietas, viáticos, asesorías). |

#### Programas
| Programa | Def |
| --- | --- |
| 01 Funcionamiento | Gastos administrativos (Personal; Bienes y Servicios). |
| 02 Inversión Regional | Ejecución FNDR y otros fondos de capital. |

#### Subtitulos Relevantes
- 21 Gastos en Personal.
- 22 Bienes y Servicios de Consumo.
- 24 Transferencias Corrientes.
- 29 Adquisición de Activos No Financieros.
- 31 Iniciativas de Inversión.
- 33 Transferencias de Capital.

#### Roles Presupuestarios

#### Roles
| Ref |
| --- |
| DEF-DIPRES |
| DEF-GOBERNADOR-REGIONAL |
| DEF-CORE |
| DEF-DIPIR |

### Seccion II Ciclo de Formulacion Presupuestaria

#### Fase Exploratoria Marco Presupuestario

#### Calendario
Mayo-Junio del año anterior.

#### Actividad
DIPRES comunica 'Marco Exploratorio' (techo global estimado).

#### Analisis Interno
| Resp | Act | Res |
| --- | --- | --- |
| DIPIR | Proyectar 'Arrastres' (compromisos de años anteriores a pagar en año t+1). |  |
| DIPIR |  | Determinar 'Espacio Presupuestario' para nuevas iniciativas. |

#### Formulacion del Proyecto de Presupuesto

#### Programa 01 Funcionamiento

#### Proceso
- Formular en base a dotación efectiva (remuneraciones).
- Formular en base a contratos de servicios vigentes (luz, agua, seguridad, aseo).

#### Programa 02 Inversion

#### Prioridades
| Prioridad | Req |
| --- | --- |
| 1. Continuidad (Arrastre). | Asegurar financiamiento de obras en ejecución. |
| 2. Nuevas Iniciativas. | ['Seleccionar proyectos con recomendación técnica favorable (RS).', 'Alinear con Estrategia Regional de Desarrollo (ERD).'] |

#### Ingreso SIGFE

#### Acciones
Cargar formulación en módulo de formulación del sistema central.

#### Discusion y Aprobacion

#### Proceso
| Etapa | Act |
| --- | --- |
| 1. Interna | DIPIR presenta propuesta consolidada a Gobernador y Administrador Regional. |
| 2. CORE | Gobernador presenta proyecto al CORE (comisión y aprobación en pleno). |
| 3. DIPRES/Congreso |  |
| 4. Promulgación |  |

### Seccion III Ejecucion y Control Presupuestario

#### Distribucion Inicial

#### Proceso
- Promulgada la Ley: emitir Decreto de Identificación Presupuestaria.
- Desagregar montos globales en asignaciones específicas e Iniciativas de Inversión (códigos BIP).

#### Niveles de Ejecucion y Grados de Afectacion

#### Requisitos
Todo gasto debe seguir estrictamente la cadena de afectación en SIGFE para asegurar trazabilidad y control financiero.

#### Cadena Estandar
| Etapa | Ref | Act |
| --- | --- | --- |
| 0. Pre-afectación |  |  |
| 1. CDP | DEF-CDP | Emisión del certificado que bloquea el saldo presupuestario. |
| 2. Compromiso | DEF-COMPROMISO | Registro del acto administrativo (OC, Contrato, Resolución) que formaliza la obligación con un tercero. |
| 3. Devengo | DEF-DEVENGO | Reconocimiento de la obligación exigible tras recepción conforme o cumplimiento de hito. |
| 4. Pago | DEF-PAGO | Extinción de la obligación mediante transferencia electrónica. |

#### Reglas Especificas de Devengo para Transferencias

#### Casos
| Caso | Regla |
| --- | --- |
| Transferencias Extrapresupuestarias (Subt. 24.03, 33.03) a Instituciones Ley Ppto | El devengo ocurre al aprobarse técnicamente la rendición de cuentas, no al momento de la transferencia. |
| Transferencias a Municipios y Otros Servicios (Consolidables) | El devengo ocurre cuando la obligación es exigible según el acto administrativo o convenio tramitado. |
| Transferencias a Entidades Privadas (Subt. 24.01, 33.01) | El devengo ocurre al cumplirse las condiciones de exigibilidad pactadas en el convenio formal. |

#### Modificaciones Presupuestarias

#### Niveles
| Nivel | Nombre | Alcance |
| --- | --- | --- |
| 1 | Resolución GORE | Reasignaciones entre ítems del mismo subtítulo (con restricciones). |
| 2 | Resolución GORE con Toma de Razón | Reasignaciones entre subtítulos de misma naturaleza. |
| 3 | Decreto de Hacienda | ['Suplementos de fondos.', 'Transferencias entre programas.', 'Creación de asignaciones.'] |

#### Excepciones Sin Acuerdo CORE Glosa 01

#### Contexto
Modificaciones que el Gobernador puede autorizar vía Resolución sin acuerdo CORE (Glosa 01, Circular 11).

#### Casos
- Incorporación de Mayores Ingresos Propios percibidos.
- Distribución de Saldos Iniciales de Caja (SIC) para Deuda Flotante.
- Reasignaciones por aplicación de leyes de Reajuste.
- Cumplimiento de sentencias ejecutoriadas.
- Desagregación de recursos para Transferencias Consolidadas.
- Distribución de Provisiones de la Partida Tesoro Público.

#### Rol CORE

#### Requisitos
CORE debe aprobar modificaciones que impliquen cambios en distribución de inversión o creación de nuevos programas.

### Seccion IV Gestion de la Inversion Regional FNDR

#### Identificacion de Iniciativas IDI

#### Requisitos
Cada proyecto de inversión debe tener código BIP.

#### Apertura IDI

#### Responsables
DIPIR

#### Acciones
Crear 'ficha IDI' en sistema presupuestario; cargar presupuesto anual y total.

#### Control por Codigo

#### Requisitos
Ejecución se controla a nivel de IDI; no usar fondos de proyecto A para pagar proyecto B.

#### Gestion de Convenios de Transferencia

#### Definicion
Mecanismo principal para ejecutar proyectos donde GORE no es unidad técnica.

#### Tipos
| Tipo | Def | Req |
| --- | --- | --- |
| Convenio Mandato | GORE encarga ejecución a tercero (MOP, SERVIU, Municipalidad); transfiere recursos contra avance (Estados de Pago). |  |
| Convenio de Transferencia | Entrega recursos para ejecución directa del beneficiario (subvenciones, fondos concursables). | Rendición estricta (SISREC/Contraloría). |

#### Contexto
- Unidades técnicas posibles: MOP, SERVIU, Municipalidad.
- Estados de Pago: transferencia contra avance.

#### Programas Directos Glosa 06

#### Definicion
Oferta programática ejecutada directamente por el GORE.

#### Evaluacion Ex Ante

#### Requisitos
Programas nuevos o sustancialmente reformulados requieren evaluación favorable DIPRES/MDSF antes de financiamiento.

#### Metodologia Marco Logico

#### Requisitos
Diseñar programas con objetivos, componentes, actividades e indicadores verificables.

#### Gasto Administrativo

#### Requisitos
Hasta 5% del monto del programa para gastos de administración del GORE (Subtítulos 21, 22, 29).

#### Exencion

#### Requisitos
Exentos de evaluación ex-ante: programas 8% FNDR (Glosa 07) y tipologías FRPD de Innovación.

#### Restricciones Glosas 2025

#### Normas
| Glosa | Req |
| --- | --- |
| 03 (Gastos en Personal) |  |
| 06 (Programas GORE) | Ejecución directa requiere unidad técnica interna competente y resolución fundada. |
| 07 (Subvenciones 8%) | Máximo 8% del presupuesto inversional. Asignación directa solo a entidades públicas o privadas sin fines de lucro, con justificación fundada. |
| 12 (FRIL) | Proyectos menores a 5.000 UTM exentos de evaluación MDSyF (solo requieren elegibilidad técnica regional). |

#### Programacion Financiera

#### Coordinacion
DIPIR-Tesorería.

#### PAC de Inversiones

#### Definicion
PAC vinculada a avance físico de obras.

#### Devengamiento Oportuno

#### Requisitos
- Evitar devengamiento masivo en diciembre.
- Procesar estados de pago mensualmente para reflejar ejecución real.

### Seccion V Informes y Evaluacion

#### Reporteria Oficial

#### Informe de Ejecucion Mensual

#### Proceso
- Enviar a DIPRES y CORE dentro de primeros días del mes siguiente.
- Mostrar presupuesto vigente vs devengado.

#### Informes Trimestrales Glosas

#### Definicion
Reportes exigidos por Ley de Presupuestos (ej.: gastos en publicidad, viáticos, convenios directos).

#### Proceso
- Enviar al Congreso.
- Publicar en transparencia activa.

#### Cierre Presupuestario

#### Regla 31 Diciembre

#### Requisitos
- Presupuesto expira al 31/12.
- Saldos no comprometidos no se acumulan para el año siguiente (salvo norma expresa de saldo inicial de caja).

#### Deuda Flotante

#### Financiamiento
| Cond | Res |
| --- | --- |
| SIC suficiente | Financiar íntegramente con SIC (solo Resolución GORE). |
| SIC insuficiente | Usar todo SIC disponible + diferencia con mayor aporte fiscal (Resolución GORE + Decreto DIPRES). |

#### Prioridad

#### Requisitos
Pago Deuda Flotante es primera prioridad al inicio del nuevo ejercicio.

#### Registro

#### Acciones
Crear Ítem 34.07 'Deuda Flotante' en presupuesto del año siguiente.

### Ctx Related Knowledge

#### XRef
- [Partida 31: Gobiernos Regionales - Ley de Presupuestos 2026](urn:gn:kb:ley-presupuestos-2026-partida-31)
- [Ley de Presupuestos 2026: Normas Generales](urn:gn:kb:ley-presupuestos-2026-normas-generales)
- [Gestión Financiera y Operativa del Presupuesto Regional (GORE)](urn:gn:kb:gestion-prpto)

## Just
Manual orientado a disciplina fiscal y cumplimiento de metas de ejecución del Gobierno Regional.
