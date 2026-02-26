---
_manifest:
  urn: "urn:fxsl:skill:refactorer-refactor-executor:1.0.0"
  type: "lazy_load_endofunctor"
version: "1.0.0"
status: published
lang: es
---
# CM-REFACTOR-EXECUTOR

## Proposito
Ejecuta refactorings atomicos preservando comportamiento, usando tests como red de seguridad. Nucleo del refactorer.

## Input/Output
- **Input:** Oportunidad de refactoring (tipo, target, justificacion). Tests existentes para la zona. CONVENTIONS.md.
- **Output:** Codigo refactorizado, tests verdes, metricas antes/despues, diff.

## Procedimiento

### Paso 0: Verificar Red de Seguridad
- Verificar que existen tests para la zona afectada.
- IF no existen tests → escribir tests de caracterizacion ANTES de tocar codigo.
  - Test de caracterizacion: captura el comportamiento actual tal como es (no como deberia ser).
  - Cubrir: inputs tipicos, edge cases observados, outputs actuales.
  - Los tests DEBEN pasar con el codigo actual. Si no pasan, el test esta mal.
- Ejecutar tests existentes. Confirmar baseline verde.
- IF tests rojos antes de empezar → ABORTAR. Reportar: "Tests rojos pre-refactoring. Corregir primero."

### Paso 1: Medir Antes
- Registrar metricas pre-refactoring de la zona afectada:
  - Complejidad ciclomatica de funciones tocadas.
  - Lineas de codigo.
  - % duplicacion (si aplica).
  - Numero de parametros (si aplica).

### Paso 2: Aplicar Refactoring Atomico
Ejecutar UN refactoring a la vez. Tipos soportados:

- **extract_function:** Extraer bloque de codigo a funcion con nombre descriptivo. Parametros: nombre, lineas a extraer, parametros de la nueva funcion.
- **rename:** Renombrar variable/funcion/clase/archivo. Actualizar todas las referencias. Nombre nuevo DEBE seguir CONVENTIONS.md.
- **simplify_conditional:** Reducir complejidad de condicional: early return, guard clauses, tabla de lookup, polimorfismo.
- **remove_duplication:** Extraer codigo duplicado a funcion/componente compartido. Reemplazar todas las ocurrencias.
- **extract_component:** Extraer fragmento de UI a componente reutilizable (React/Vue). Props tipadas.
- **improve_types:** Reemplazar `any`/`object` con tipos especificos. Agregar Zod schemas / Pydantic models en boundaries.
- **inline_temp:** Eliminar variable temporal innecesaria. Usar expresion directamente si mejora legibilidad.
- **replace_magic_number:** Extraer numero magico a constante con nombre semantico.
- **decompose_conditional:** Descomponer condicional complejo en funciones con nombres que expresan la intencion.
- **consolidate_duplicate_conditional:** Unificar ramas condicionales duplicadas.

### Paso 3: Verificar Tests
- Ejecutar tests despues del refactoring.
- IF tests verdes → continuar.
- IF tests rojos → REVERTIR refactoring inmediatamente. Diagnosticar causa:
  - Efecto colateral no cubierto por tests de caracterizacion?
  - Refactoring incorrecto (cambio de comportamiento)?
  - Test fragil (depende de implementacion, no de comportamiento)?
- Reportar diagnostico. NO continuar con tests rojos.

### Paso 4: Medir Despues
- Registrar metricas post-refactoring.
- Calcular delta: mejora o degradacion en cada metrica.
- IF degradacion en alguna metrica → evaluar si el trade-off es aceptable (ej: +2 lineas pero -5 complejidad).

### Paso 5: Documentar
- Generar diff legible.
- Registrar: tipo de refactoring, justificacion, metricas antes/despues, archivos afectados.

## Invariantes
- NUNCA cambiar comportamiento observable. Tests lo verifican.
- NUNCA refactorizar sin tests verdes como baseline.
- NUNCA aplicar multiples refactorings sin verificar tests entre cada uno.
- SIEMPRE revertir si tests fallan post-refactoring.

## Signature Output

```markdown
## Refactoring: {tipo}

### Target
{archivo:funcion/componente}

### Justificacion
{por que este refactoring mejora el codigo}

### Metricas
| Metrica | Antes | Despues | Delta |
|---------|-------|---------|-------|
| Complejidad ciclomatica | {n} | {n} | {-n} |
| Lineas | {n} | {n} | {+/-n} |
| Duplicacion | {n}% | {n}% | {-n}% |

### Tests
- Baseline: {n} tests verdes
- Post-refactor: {n} tests verdes
- Tests de caracterizacion agregados: {n}

### Diff
{diff del cambio}
```
