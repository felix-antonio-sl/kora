---
_manifest:
  urn: urn:gn:kb:manual-presupuesto
  provenance:
    created_by: FS
    created_at: '2026-02-24'
    source: "GORE Ñuble"
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
---

# Manual 1.1: Formulación y Ejecución Presupuestaria

Objetivo: Estandarizar el ciclo de vida de los recursos financieros regionales (planificación → formulación → aprobación → ejecución → control → cierre), asegurando el cumplimiento de la Ley de Presupuestos del Sector Público y la normativa SAF del Estado.

Siglas: DIPRES = Dirección de Presupuestos · CORE = Consejo Regional · DIPIR = División de Presupuesto e Inversión Regional · SIGFE = Sistema de Información para la Gestión Financiera del Estado · BIP = Banco Integrado de Proyectos · IDI = Iniciativa de inversión (proyecto) con código BIP · FNDR = Fondo Nacional de Desarrollo Regional · FRPD = Fondo Regional para la Productividad y el Desarrollo · CDP = Certificado de Disponibilidad Presupuestaria · PAC = Programación Anual de Caja · SIC = Saldo Inicial de Caja · ERD = Estrategia Regional de Desarrollo · CGR = Contraloría General de la República · MOP/SERVIU = entidades técnicas de ejecución.

## Marco Conceptual y Estructura

**Clasificador Presupuestario (Decreto N° 854 de 2004 de Hacienda):**

| Nivel | Código | Descripción |
|-------|--------|-------------|
| Partida | 31 | Gobiernos Regionales |
| Capítulo | 01 | Gobierno Regional |
| Capítulo | 02 | Consejo Regional (dietas, viáticos, asesorías) |
| Programa | 01 | Funcionamiento (gastos administrativos) |
| Programa | 02 | Inversión Regional (FNDR y otros fondos de capital) |

**Subtítulos relevantes:** 21 Gastos en Personal · 22 Bienes y Servicios de Consumo · 24 Transferencias Corrientes · 29 Adquisición de Activos No Financieros · 31 Iniciativas de Inversión · 33 Transferencias de Capital.

**Fuentes de financiamiento:** FNDR (principal fuente para inversiones; subdividido en asignaciones regionales y provisiones) · FRPD (recursos para fomento productivo, ciencia e innovación) · Ingresos Propios (venta de bienes, multas, servicios).

**Roles presupuestarios:** DIPRES: ente rector, define instrucciones, techos y autoriza modificaciones mayores. Gobernador Regional: propone presupuesto al CORE y lo ejecuta. CORE: aprueba presupuesto inicial y modificaciones mayores; fiscaliza la ejecución. DIPIR: unidad técnica responsable de gestión diaria del presupuesto, control de saldos y visación de gastos.

## Ciclo de Formulación Presupuestaria

**Marco exploratorio:** Mayo–Junio del año anterior. DIPRES comunica techo global estimado. DIPIR proyecta "Arrastres" (compromisos de años anteriores a pagar en año t+1) y determina "Espacio Presupuestario" para nuevas iniciativas.

**Formulación del proyecto de presupuesto:**

| Programa | Criterio de formulación |
|---------|------------------------|
| Programa 01 (Funcionamiento) | En base a dotación efectiva (remuneraciones) y contratos de servicios vigentes (luz, agua, seguridad, aseo) |
| Programa 02 (Inversión) | Prioridad 1: continuidad (arrastres); Prioridad 2: nuevas iniciativas con recomendación técnica favorable (RS) alineadas con ERD |

Ingreso al módulo de formulación de SIGFE.

**Discusión y aprobación:**

| Etapa | Descripción |
|-------|-------------|
| 1. Interna | DIPIR presenta propuesta consolidada a Gobernador y Administrador Regional |
| 2. CORE | Gobernador presenta proyecto al CORE (comisión y aprobación en pleno) |
| 3. DIPRES/Congreso | Discusión técnica con analistas DIPRES; trámite legislativo (septiembre–noviembre) |
| 4. Promulgación | Publicación Ley de Presupuestos (diciembre) |

## Ejecución y Control Presupuestario

**Distribución inicial:** Promulgada la Ley, emitir Decreto de Identificación Presupuestaria. Desagregar montos globales en asignaciones específicas e IDI (códigos BIP).

**Cadena de afectación en SIGFE (obligatoria para todo gasto):**

| Etapa | Descripción |
|-------|-------------|
| 0. Pre-afectación | Reserva preventiva de recursos al iniciar proceso de compra o solicitud de gasto (interno) |
| 1. CDP | Emisión del certificado que bloquea el saldo presupuestario. Ningún proceso de compra o convenio inicia sin CDP vigente |
| 2. Compromiso | Registro del acto administrativo (OC, Contrato, Resolución) que formaliza la obligación con un tercero; reserva recursos definitivamente |
| 3. Devengo | Reconocimiento de la obligación exigible tras recepción conforme o hito; debe ser simultáneo a recepción de factura/bien; genera pasivo contable |
| 4. Pago | Extinción de la obligación mediante transferencia electrónica |

**Reglas específicas de devengo para transferencias** (Minuta CGR-AGORECHI-DIPRES marzo 2025; Dictamen CGR N°E583841/2024):

| Tipo de transferencia | Regla de devengo |
|----------------------|-----------------|
| Extrapresupuestarias (Subt. 24.03, 33.03) a Instituciones Ley Ppto | Ocurre al aprobarse técnicamente la rendición de cuentas, no al momento de la transferencia |
| A Municipios y Otros Servicios (Consolidables) | Cuando la obligación es exigible según el acto administrativo o convenio tramitado |
| A Entidades Privadas (Subt. 24.01, 33.01) | Al cumplirse las condiciones de exigibilidad pactadas en el convenio formal |

**Modificaciones presupuestarias:**

| Nivel | Instrumento | Alcance | Aprobación |
|-------|-------------|---------|-----------|
| 1 | Resolución GORE | Reasignaciones entre ítems del mismo subtítulo (con restricciones) | Gobernador |
| 2 | Resolución GORE con Toma de Razón | Reasignaciones entre subtítulos de misma naturaleza | Gobernador |
| 3 | Decreto de Hacienda | Suplementos de fondos, transferencias entre programas, creación de asignaciones | DIPRES |

**Modificaciones sin acuerdo CORE (Glosa 01, Circular 11):** Incorporación de Mayores Ingresos Propios · distribución de SIC para Deuda Flotante · reasignaciones por leyes de Reajuste · cumplimiento de sentencias ejecutoriadas · desagregación de recursos para Transferencias Consolidadas · distribución de Provisiones de la Partida Tesoro Público.

CORE debe aprobar modificaciones que impliquen cambios en distribución de inversión o creación de nuevos programas (Ley 19.175).

## Gestión de la Inversión Regional (FNDR)

**Apertura de IDI:** Cada proyecto requiere código BIP. DIPIR crea "ficha IDI" en sistema presupuestario con presupuesto anual y total. Control por código: no usar fondos del proyecto A para pagar proyecto B.

**Gestión de convenios de transferencia:**

| Tipo | Descripción |
|------|-------------|
| Convenio Mandato | GORE encarga ejecución a tercero (MOP, SERVIU, Municipalidad); transfiere recursos contra avance (Estados de Pago) |
| Convenio de Transferencia | Entrega recursos para ejecución directa del beneficiario (subvenciones, fondos concursables); rendición estricta vía SISREC/Contraloría |

**Programas directos (Glosa 06):** Ejecución directa por el GORE. Programas nuevos o sustancialmente reformulados requieren evaluación favorable DIPRES/MDSF antes del financiamiento. Metodología Marco Lógico: objetivos, componentes, actividades e indicadores verificables. Gasto administrativo: hasta 5% del monto del programa (Subtítulos 21, 22, 29). Exentos de evaluación ex-ante: programas 8% FNDR (Glosa 07) y tipologías FRPD de Innovación.

**Restricciones de Glosas** (Circular 11 DIPRES):

| Glosa | Norma |
|-------|-------|
| 03 (Gastos en Personal) | No imputar a inversión (Subt. 31) gastos en personal (Subt. 21), salvo contratación de inspección técnica de obras |
| 06 (Programas GORE) | Ejecución directa requiere unidad técnica interna competente y resolución fundada |
| 07 (Subvenciones 8%) | Máximo 8% del presupuesto inversional; asignación directa solo a entidades públicas o privadas sin fines de lucro con justificación fundada |
| 12 (FRIL) | Proyectos < 5.000 UTM exentos de evaluación MDSyF (solo requieren elegibilidad técnica regional) |

**Programación de caja (DIPIR-Tesorería):** PAC de Inversiones vinculada a avance físico de obras. Devengamiento oportuno: evitar concentración masiva en diciembre; procesar estados de pago mensualmente.

## Informes y Evaluación

**Informe de Ejecución Mensual:** Enviar a DIPRES y CORE dentro de los primeros días del mes siguiente. Mostrar presupuesto vigente vs. devengado.

**Informes trimestrales (Glosas):** Reportes exigidos por Ley de Presupuestos (ej. gastos en publicidad, viáticos, convenios directos). Enviar al Congreso y publicar en transparencia activa.

**Cierre presupuestario:**
- Presupuesto expira al 31/12; saldos no comprometidos no se acumulan (salvo norma expresa de SIC).
- Deuda Flotante (obligaciones devengadas no pagadas al 31/12):
  - Si SIC suficiente: financiar íntegramente con SIC (solo Resolución GORE).
  - Si SIC insuficiente: usar todo SIC disponible + diferencia con mayor aporte fiscal (Resolución GORE + Decreto DIPRES).
- Pago Deuda Flotante: primera prioridad al inicio del nuevo ejercicio.
- Registro: crear Ítem 34.07 "Deuda Flotante" en presupuesto del año siguiente.

Documentos relacionados: `urn:gn:kb:ley-presupuestos-2026-partida-31` · `urn:gn:kb:ley-presupuestos-2026-normas-generales` · `urn:gn:kb:gestion-prpto`.
