---
_manifest:
  urn: urn:gn:kb:bpmn-d04-compras-contrataciones
  provenance:
    created_by: FS
    created_at: '2026-01-29'
    source: "GORE Ñuble"
version: 2.0.0
status: published
tags:
- gore-nuble
- gobierno-regional
- compras-publicas
- bpmn
- gn
lang: es
---

# BPMN D04: Compras Públicas y Contrataciones

## Metadatos del Dominio

| Atributo | Valor |
| :--- | :--- |
| ID | DOM-COMPRAS |
| Criticidad | Alta |
| Dueño | Unidad de Abastecimiento |
| Procesos | 4 (PAC, Licitación, OC, Contratos) |
| Subprocesos | ~12 |

## Mapa General

P1 Plan Anual de Compras → P2 Licitación Pública → P3 Órdenes de Compra → P4 Gestión de Contratos.
Desde P1 también se puede ir directamente a P3 vía Convenio Marco.

## P1: Plan Anual de Compras (PAC)

**Período:** Anual (Diciembre–Enero).

### Flujo

1. Divisiones identifican necesidades → unidades envían requerimientos
2. Abastecimiento consolida
3. Clasificar por mecanismo: Convenio Marco / Licitación / Compra Directa
4. Validación presupuestaria (DAF)
5. Aprobación Gobernador/a
6. Publicar PAC en Mercado Público
7. Monitoreo y ajustes trimestrales

### Contenido del PAC

| Elemento | Descripción |
| :--- | :--- |
| Producto/Servicio | Descripción detallada |
| Cantidad estimada | Unidades requeridas |
| Monto estimado | Valor en pesos |
| Período | Trimestre de adquisición |
| Mecanismo | CM / LP / CD / TDP |

## P2: Licitación Pública

**Umbral:** > 1.000 UTM.

### Mecanismos de Compra

| Monto | Mecanismo |
| :--- | :--- |
| > 1.000 UTM | Licitación Pública |
| 100–1.000 UTM | Licitación Privada |
| < 100 UTM | Compra Directa |
| Existe Convenio Marco | Convenio Marco (prioridad) |

### Flujo

**Preparación:**
1. Elaborar bases técnicas y administrativas
2. Revisión jurídica
3. Resolución que aprueba bases

**Publicación:**
4. Publicar en Mercado Público
5. Período de consultas → respuestas y aclaraciones
6. Recepción de ofertas

**Evaluación:**
7. Comisión evaluadora revisa ofertas
8. Aplicar criterios: precio, calidad, experiencia
9. Acta de evaluación → propuesta de adjudicación

**Adjudicación:**
10. Resolución de adjudicación
11. Publicar resultado → notificar a oferentes
12. Período de impugnación

## P3: Ejecución de Órdenes de Compra

**Sistema:** Mercado Público.

### Flujo

1. Adjudicación/Contrato vigente
2. Abastecimiento genera OC
3. Asociar CDP y partida presupuestaria
4. Firma jefatura respectiva
5. Enviar OC a proveedor → proveedor acepta OC
6. Recepción de bienes/servicios → ¿Conforme?
   - Sí → Acta de recepción → facturación → pago
   - No → Rechazo/devolución

### Estados de la OC

| Estado | Descripción |
| :--- | :--- |
| Generada | OC creada en el sistema |
| Enviada | Notificada al proveedor |
| Aceptada | Proveedor confirma |
| Recepcionada | Bienes/servicios entregados |
| Pagada | Proceso completado |

## P4: Gestión de Contratos

**Responsable:** Administrador de Contrato.

### Flujo

**Formalización:**
1. Elaborar contrato → revisión jurídica → firma de partes
2. Resolución aprobatoria
3. Garantías: fiel cumplimiento, anticipo

**Ejecución:**
4. Designar administrador de contrato
5. Seguimiento de hitos
6. Verificar cumplimiento
7. Estados de pago parciales

**Cierre:**
8. Recepción definitiva → acta de cierre
9. Devolución garantías
10. Evaluación proveedor

### Funciones del Administrador de Contrato

| Función | Descripción |
| :--- | :--- |
| Supervisión | Verificar cumplimiento técnico |
| Comunicación | Enlace con proveedor |
| Documentación | Mantener expediente |
| Hitos | Certificar avances |
| Pagos | Autorizar estados de pago |

## Control y Transparencia

### Obligaciones de Publicación

| Información | Plataforma |
| :--- | :--- |
| PAC | Mercado Público |
| Licitaciones | Mercado Público |
| Adjudicaciones | Mercado Público |
| Contratos | Transparencia Activa |
| Órdenes de Compra | Mercado Público |

### Prohibiciones

- Fraccionamiento prohibido: no dividir compras para eludir umbrales.
- Conflicto de intereses: funcionarios deben declarar inhabilidades.

## Sistemas Involucrados

| Sistema | Función |
| :--- | :--- |
| ORG-CHILECOMPRA | Mercado Público, OC, licitaciones |
| SYS-SIGFE | CDP, compromisos, pagos |
| SYS-DOCDIGITAL | Contratos, resoluciones |

## Normativa Aplicable

| Norma | Alcance |
| :--- | :--- |
| Ley 19.886 | Compras públicas |
| Reglamento D.S. 250 | Procedimientos |
| Directivas ChileCompra | Operativas |
| Ley 20.730 | Lobby y conflictos de interés |

## Referencias Cruzadas

| Dominio | Vínculo |
| :--- | :--- |
| D02 Ciclo Presupuestario | CDP, compromisos |
| D05 Inventarios | Recepción de bienes |
| D01 Actos Administrativos | Resoluciones de adjudicación |
