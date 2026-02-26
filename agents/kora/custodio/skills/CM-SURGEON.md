---
_manifest:
  urn: "urn:kora:skill:custodio-surgeon:1.0.0"
  type: "lazy_load_endofunctor"
version: "1.0.0"
status: published
lang: es
---
# CM-SURGEON

## Proposito
Aplica reparaciones quirurgicas a componentes del repo KORA: minima modificacion, preservar invariantes, no romper dependencias.

## I/O

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
5. Presentar fix al usuario: {archivo, cambio_propuesto, impacto}.
6. ESPERAR CONFIRMACION. No proceder sin aprobacion explicita.
7. Aplicar fix. Verificar resultado (re-leer archivo, re-ejecutar health si aplica).
8. Documentar: que se cambio, por que, cuando.

## Signature Output

| Campo | Tipo | Descripcion |
|-------|------|-------------|
| archivos_modificados | string[] | Archivos que fueron modificados |
| cambios | {antes, despues, justificacion}[] | Cambios realizados |
| verificacion_post | enum(PASS\|FAIL) | Resultado de verificacion post-fix |
