---
_manifest:
  urn: "urn:dev:skill:sentinel-context-auditor:1.0.0"
  type: "lazy_load_endofunctor"
version: "1.0.0"
status: published
lang: es
---
# CM-CONTEXT-AUDITOR

## Proposito
Detecta drift entre context files y el estado real del codebase. Genera diffs propuestos para corregir.

## Procedimiento
1. Leer context files del proyecto:
   - CONVENTIONS.md: naming, estructura, patrones, error handling.
   - ARCHITECTURE.md: componentes, flujos, dependencias, decisiones.
   - SCHEMA.md: tablas, relaciones, tipos, constraints.
   - STACK.md: tecnologias, versiones, quirks (si existe).
2. Escanear codebase real para cada context file:
   - CONVENTIONS: muestrear archivos recientes. ¿Naming respetado? ¿Estructura de carpetas coherente? ¿Patrones de error seguidos?
   - ARCHITECTURE: ¿Los componentes declarados existen? ¿Los flujos de datos son correctos? ¿Hay componentes nuevos no documentados?
   - SCHEMA: ¿Las tablas/modelos del codebase coinciden con lo declarado? ¿Hay campos nuevos no documentados?
3. Para cada divergencia detectada:
   - Clasificar: CODEBASE_WRONG(el codigo viola la convencion) vs CONTEXT_OUTDATED(el context file no refleja una decision ya tomada).
   - Si CODEBASE_WRONG: proponer correccion en el codigo (tarjeta purpura para el coder).
   - Si CONTEXT_OUTDATED: generar diff propuesto para el context file.
4. Presentar hallazgos como diff + justificacion al Operador.
5. Verificar coherencia ENTRE context files: ¿ARCHITECTURE.md y SCHEMA.md son consistentes?

## Output
Reporte drift: {context_file, divergencias: [{tipo, seccion, declarado, real, accion_propuesta}], diffs_propuestos[]}.
