---
_manifest:
  urn: urn:kora:skill:custodio-surgeon:1.0.0
  type: lazy_load_endofunctor
version: 1.0.0
status: published
lang: es
---

# CM-SURGEON

## Proposito
Aplica reparaciones quirurgicas a componentes del repo KORA: minima modificacion, preservar invariantes, no romper dependencias.

## Input/Output
- **Input:** diagnostico: {componente: string, severidad: string, causa_raiz: string} (problema detectado por CM-HEALTH-INSPECTOR o CM-ESTRUCTURA-AUDITOR)
- **Output:** SurgicalReport (ver Signature Output)

## Procedimiento
1. Recibir diagnostico: componente afectado, severidad, causa raiz.
2. Leer el componente afectado completo (archivo, directorio, catalogo entry).
3. Clasificar tipo de fix: frontmatter(corregir YAML), URN(renombrar/redirigir), estructura(mover/renombrar), contenido(editar seccion).
4. Disenar fix quirurgico:
   - Identificar minimo cambio necesario.
   - Verificar que fix no rompe otros componentes (buscar referencias cruzadas).
   - Listar archivos que seran modificados.
5. Generar propuesta de fix estructurada: {archivo, cambio_propuesto, impacto, precondiciones}.
6. Aplicar fix quirurgico solo dentro del envelope operativo ya resuelto por el agente.
7. Verificar resultado (re-leer archivo, re-ejecutar health si aplica).
8. Documentar: que se cambio, por que, cuando.

## Signature Output
| Campo | Tipo | Descripcion |
|-------|------|-------------|
| archivos_modificados | string[] | Archivos que fueron modificados |
| cambios | {antes, despues, justificacion}[] | Cambios realizados |
| verificacion_post | enum(PASS\|FAIL) | Resultado de verificacion post-fix |
