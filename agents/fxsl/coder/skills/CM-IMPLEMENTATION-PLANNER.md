---
_manifest:
  urn: "urn:fxsl:skill:coder-implementation-planner:1.0.0"
  type: "lazy_load_endofunctor"
version: "1.0.0"
status: published
lang: es
---
# CM-IMPLEMENTATION-PLANNER

## Proposito
Genera plan de implementacion descompuesto en tareas tecnicas ordenadas, respetando el ciclo TDD y type-first development.

## Procedimiento
1. Recibir historia validada del CM-STORY-CONSUMER.
2. Descomponer en tareas tecnicas. Orden obligatorio por bloque funcional:
   a. **Tipos/Interfaces:** Definir tipos TypeScript o modelos Pydantic.
   b. **Tests:** Escribir tests unitarios que fallan (red).
   c. **Implementacion:** Codigo minimo para pasar tests (green).
   d. **Tests de aceptacion:** Derivar de ACs de la historia.
   e. **Integracion:** Conectar con componentes existentes.
   f. **Refactor:** Limpiar sin romper tests (refactor).
3. Para cada tarea listar:
   - Descripcion concreta.
   - Archivos afectados (path esperado segun CONVENTIONS.md).
   - Tipo: type|test|code|refactor|integration.
   - Dependencia con tareas anteriores.
4. Estimar complejidad total y tier de modelo recomendado.
5. Si historia clasificada como destructiva: marcar que requiere aprobacion humana pre-ejecucion.
6. Presentar plan al Operador para aprobacion.
7. NO PROCEDER sin aprobacion.

## Output
Plan: {tareas: [{orden, descripcion, archivos[], tipo, depende_de[]}], tier_recomendado, requiere_aprobacion_humana: bool}. Listo para aprobacion.
