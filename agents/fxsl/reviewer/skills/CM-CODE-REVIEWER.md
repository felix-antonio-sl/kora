---
_manifest:
  urn: "urn:fxsl:skill:reviewer-code-reviewer:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-CODE-REVIEWER

## Proposito
Revisa un PR en profundidad: calidad de codigo, convenciones, tipos, tests, estructura. Nucleo del reviewer.

## Procedimiento
1. Leer PR completo: titulo, descripcion, diff, archivos modificados, tests agregados.
2. Verificar que el PR tiene formato correcto (What/Why/How/Tests).
3. Revisar contra checklist por archivo modificado:

### Convenciones (CONVENTIONS.md)
- [ ] Naming correcto (camelCase TS, snake_case Python).
- [ ] Estructura de archivos respetada.
- [ ] Patrones de error handling del proyecto.
- [ ] Imports organizados.

### Tipos (Type Safety)
- [ ] Zero `any`. Todo tipado explicito.
- [ ] Zod schema en todo boundary de entrada (formularios, API inputs, server actions).
- [ ] Pydantic model en todo boundary de entrada Python.
- [ ] No `as` casts innecesarios.
- [ ] Return types explicitos en funciones publicas.

### Tests (TDD Compliance)
- [ ] Cada funcion publica nueva tiene test unitario.
- [ ] Cada AC de la historia tiene test de aceptacion.
- [ ] Tests escritos con Arrange-Act-Assert.
- [ ] Tests verifican comportamiento, no implementacion.
- [ ] No hay codigo nuevo sin test.

### Calidad
- [ ] Funciones < 30 lineas (preferible).
- [ ] Complejidad ciclomatica razonable.
- [ ] Sin duplicacion obvia.
- [ ] Nombres descriptivos (la funcion dice lo que hace).
- [ ] Comments solo donde la logica no es obvia.

4. Registrar cada hallazgo con: severidad, archivo:linea, descripcion, sugerencia de fix.
5. Si hay >3 hallazgos CRITICOS: detener review y recomendar REJECT inmediato.

## Output
Hallazgos: tabla [{severidad, archivo:linea, hallazgo, sugerencia}]. Conteo por severidad.
