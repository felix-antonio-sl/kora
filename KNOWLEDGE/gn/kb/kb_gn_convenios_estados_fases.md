---
_manifest:
  urn: urn:gn:kb:convenios-estados-fases
  provenance:
    created_by: kora/curator
    created_at: '2026-03-16'
    source: ssot-convenios v1.2.0 + goreNubleApprovalData.ttl + goreNubleReferenceData.ttl
      + ssot-relaciones-dominio v2.0.0
version: 1.0.0
status: published
tags:
- convenios
- estados
- ciclo-vida
- transferencias
- cuotas
- gore-nuble
- fsm
- formalización
lang: es
extensions:
  gn:
    family: guide
relations:
  cites:
  - urn:gn:kb:gestion-rendiciones
---


# Convenios GORE Ñuble — Estados y Ciclo de Vida

## Resumen

Máquina de estados del convenio GORE Ñuble: 6 tipos de convenio, 7 estados canónicos ontológicos + 6 extensiones GORE_OS (13 total), flujo de transferencia en 3 fases, sistema de cuotas/installments, verificación Art. 18 Res. 30 CGR y cardinalidades del triángulo IPR–Convenio–Resolución.

---

## Tipos de convenio (6)

Consistentes entre ReferenceData.ttl (`gnub:AgreementType`, 6 instancias) y GORE_OS (`agreement_type` scheme).

| Código | Tipo | Descripción |
|--------|------|-------------|
| TRANS | Convenio de Transferencia | Transferencia de recursos a entidad ejecutora. Rendición SISREC posterior. Subtipo: `TransferAgreement` |
| MAND | Convenio Mandato | GORE encarga ejecución a tercero técnico. Pago contra estados de avance de obra. Subtipo: `MandateAgreement` |
| PROG | Convenio de Programación | Acuerdo plurianual GORE–Ministerio |
| MARCO | Convenio Marco | Convenio general que establece condiciones para convenios específicos |
| COLAB | Convenio de Colaboración | Colaboración interinstitucional |
| INTER | Convenio Interinstitucional | Convenio entre instituciones públicas |

### Subtipos disjuntos

`TransferAgreement` ⊥ `MandateAgreement` (`owl:disjointWith` en TBox).

| Subtipo | Mecanismo de pago | Rendición |
|---------|------------------|-----------|
| Transferencia | Recursos upfront | SISREC posterior |
| Mandato | Estados de pago contra avance | Contra hitos de obra |

---

## Estados de convenio — Modelo canónico (7)

Fuente autoritativa: ApprovalData.ttl (`gnub:AgreementState`, 7 instancias secuenciadas). Mayor granularidad que ReferenceData.ttl (5 estados).

| Seq | Estado | Actor responsable | Descripción |
|-----|--------|------------------|-------------|
| 1 | Borrador | División técnica proponente | Elaboración inicial del convenio |
| 2 | En Revisión Jurídica | Asesoría Jurídica | Verificación de legalidad |
| 3 | En Revisión Financiera | DAF | Verificación de cláusulas financieras y rendición |
| 4 | Visado Internamente | — | Aprobación interna completa (Jurídica + DAF) |
| 5 | Firmado | Gobernador/a + representante legal contraparte | Firma bilateral |
| 6 | Toma de Razón Pendiente | CGR | Control preventivo de legalidad |
| 7 | Formalizado (Tramitado) | — | TdR obtenida, convenio vigente y habilitado para transferencia |

### Reconciliación ontológica

| Aspecto | ApprovalData.ttl (canónico) | ReferenceData.ttl (descartado) |
|---------|----------------------------|-------------------------------|
| Instancias | 7 secuenciadas | 5 (Draft, Reviewed, Signed, TdR, Formalized) |
| Granularidad | Distingue Revisión Jurídica y Financiera | Solo "Reviewed" genérico |
| Resolución | Adoptado como canónico | Menos granular — no refleja flujo interno |

Doble declaración ABox: 12 instancias `gnub:AgreementState` totales (7 en ApprovalData + 5 en ReferenceData) sin `owl:sameAs`. Mismo patrón que RenditionState/AccountabilityState. Pendiente: consolidar en ontología.

---

## Extensiones GORE_OS (13 estados totales)

GORE_OS extiende los 7 ontológicos con 6 estados operativos adicionales.

| Estado GORE_OS | Tipo | Mapeo ontológico | Descripción |
|----------------|------|-----------------|-------------|
| BORRADOR | Base | Borrador (seq 1) | Equivalente directo |
| EN_NEGOCIACION | Nuevo | — (entre seq 1 y 2) | Negociación con contraparte previo a revisión jurídica |
| EN_REVISION_JURIDICA | Base | En Revisión Jurídica (seq 2) | Equivalente directo |
| EN_REVISION_FINANCIERA | Base | En Revisión Financiera (seq 3) | Equivalente directo |
| VISADO | Base | Visado Internamente (seq 4) | Equivalente directo |
| FIRMADO_GORE | Split | Firmado (seq 5) — parcial | Firma unilateral GORE |
| FIRMADO_CONTRAPARTE | Split | Firmado (seq 5) — parcial | Firma contraparte (antes de TdR) |
| TDR_PENDIENTE | Alias | Toma de Razón Pendiente (seq 6) | Alias de implementación, no estado nuevo |
| FORMALIZADO | Base | Formalizado (seq 7) | Equivalente directo |
| VIGENTE | Nuevo | — (post seq 7) | Post-formalización, durante período de vigencia |
| VENCIDO | Nuevo | — | Plazo cumplido sin renovación |
| TERMINADO | Nuevo | — | Cumplimiento total de obligaciones |
| RESCILIADO | Nuevo | — | Término anticipado por acuerdo de partes |

Aritmética: 7 ontológicos − 1 reemplazado (Firmado) + 2 splits (FIRMADO_GORE, FIRMADO_CONTRAPARTE) + 5 nuevos (EN_NEGOCIACION, VIGENTE, VENCIDO, TERMINADO, RESCILIADO) = 13 estados.

FSM implementada en `convenios.py`, scheme `agreement_state`.

---

## Flujo del convenio de transferencia (3 fases)

### Fase 1 — Elaboración

División técnica elabora borrador → Asesoría Jurídica controla legalidad → DAF revisa cláusulas de rendición y aspectos financieros.

### Fase 2 — Firma

DAF presenta a Gobernador/a → Firma bilateral (GORE + representante legal de la entidad ejecutora).

### Fase 3 — Formalización

Gobernador/a emite Resolución Aprobatoria → Envío a CGR → Toma de Razón → Transferencia habilitada.

La Resolución Aprobatoria **autoriza** el Convenio; el Convenio **no es** un acto administrativo — es un contrato bilateral. La Resolución no es parte del Convenio, lo autoriza externamente (PE-1: `approvesAct ∘ emit_resolution = authorize ∘ isExecutedVia`).

---

## Etapas de aprobación de actos administrativos (8)

Fuente: ApprovalData.ttl (`gnub:ApprovalFlowStage`, 8 instancias). Aplica a Resoluciones Exentas y Afectas que acompañan al convenio.

| Seq | Etapa | Responsable |
|-----|-------|-------------|
| 1 | Elaboración (Borrador) | Unidad competente |
| 2 | V°B° Jurídico | Asesoría Jurídica |
| 3 | V°B° Control | Unidad de Control |
| 4 | V°B° Jefatura División | Jefatura de la división que origina el acto |
| 5 | V°B° Administrador/a Regional | Último filtro de coordinación administrativa |
| 6 | Firma Gobernador/a (FEA) | Gobernador/a Regional |
| 7 | Toma de Razón CGR | CGR (solo actos que comprometen fondos o por exigencia normativa) |
| 8 | Notificación y Archivo | Notificación a interesados + archivo en expediente electrónico |

---

## Cuotas e installments

Aplicable a convenios de transferencia. Gestión inline en drawer del convenio.

### Operaciones

| Operación | Endpoint | Parámetros |
|-----------|----------|-----------|
| Crear cuota individual | `POST /api/convenios/{id}/cuotas` | `installment_number`, `amount`, `due_date`, `payment_status_id` |
| Crear cuotas masivas | `POST /api/convenios/{id}/cuotas/bulk` | `total_amount`, `num_installments`, `start_date`, `frequency_months` (default 1) |

### Verificación Art. 18 Res. 30 CGR

Antes de transferir nueva cuota: verificar que la entidad ejecutora **no tenga rendiciones exigibles pendientes**. Si existen rendiciones pendientes, la transferencia queda bloqueada hasta que se resuelvan. Vinculación: [→ Gestión de Rendiciones](urn:gn:kb:gestion-rendiciones).

---

## Cardinalidades

| Relación | Cardinalidad | Nota |
|----------|:------------:|------|
| IPR → GOREAgreement | 0..N | Una IPR puede tener múltiples convenios (cuotas, mandatos parciales). Parcial: solo aplica a IPRs con mecanismo de transferencia |
| GOREAgreement → Resolution | 1..1 | Todo convenio tiene exactamente 1 Resolución Aprobatoria |
| GOREAgreement → Rendition | 1..N | Un convenio puede tener múltiples rendiciones (parciales, mensuales) |
| IPR → BudgetaryCommitment | 1..N | CDPs múltiples por año o línea |

### Morfismo parcial isExecutedVia

`isExecutedVia: IPR → GOREAgreement` solo está definido para IPRs con mecanismo de transferencia.

| Modo ejecución | isExecutedVia | Formalización |
|----------------|:-------------:|---------------|
| Transferencia (FRIL, Transfer, Subv8) | Definido → GOREAgreement | Convenio bilateral |
| Ejecución directa (SNI, C33, Glosa 06) | ∅ (no aplica) | Solo Resolución + CDP |
