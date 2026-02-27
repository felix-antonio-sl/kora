---
_manifest:
  urn: "urn:dev:skill:refactorer-dependency-modernizer:1.0.0"
  type: "lazy_load_endofunctor"
version: "1.0.0"
status: published
lang: es
---
# CM-DEPENDENCY-MODERNIZER

## Proposito
Detecta dependencias outdated y patrones deprecados. Propone y ejecuta actualizaciones con tests como red de seguridad.

## Input/Output
- **Input:** Manifest del proyecto (package.json, pyproject.toml, requirements.txt). Codebase para deteccion de patrones deprecados.
- **Output:** Plan de modernizacion, actualizaciones aplicadas con verificacion de tests, reporte de migracion.

## Procedimiento

### Paso 1: Auditar Dependencias
- Leer manifest del proyecto.
- Comparar versiones actuales contra latest disponible.
- Clasificar updates: patch (seguro), minor (revisar changelog), major (breaking changes).
- Detectar dependencias con vulnerabilidades conocidas (CVE).
- Detectar dependencias deprecated (sin mantenimiento, archivadas).
- Listar alternativas para dependencias deprecated.

### Paso 2: Detectar Patrones Deprecados
- Escanear codebase por patrones que ya tienen mejor alternativa:
  - APIs deprecadas del runtime (Node.js, Python).
  - Patrones de la libreria que tienen version moderna (ej: class components→hooks, callbacks→async/await).
  - Utility functions con equivalente nativo (ej: lodash _.map→Array.map).
  - Sintaxis antigua con equivalente moderno (ej: var→const/let, require→import).
- Clasificar por esfuerzo de migracion y riesgo.

### Paso 3: Proponer Plan
- Generar plan de modernizacion ordenado por prioridad:
  1. Vulnerabilidades criticas (prioridad inmediata).
  2. Dependencias deprecated sin alternativa soportada.
  3. Major updates con breaking changes documentados.
  4. Patrones deprecados de alto impacto.
  5. Minor/patch updates (bajo riesgo).
- Presentar plan al Operador para aprobacion.

### Paso 4: Ejecutar Updates (con aprobacion)
- Aplicar UN update a la vez.
- Por cada update:
  1. Verificar tests verdes (baseline).
  2. Aplicar update en manifest.
  3. Instalar dependencias.
  4. Ejecutar tests.
  5. IF tests verdes → registrar exito.
  6. IF tests rojos → revertir. Diagnosticar breaking change. Reportar.
- Para migracion de patrones:
  1. Identificar todas las ocurrencias del patron antiguo.
  2. Migrar una ocurrencia como pilot.
  3. Verificar tests.
  4. Si exitoso → migrar el resto.

### Paso 5: Documentar
- Registrar cada update aplicado: dependencia, version anterior, version nueva, tests status.
- Registrar patrones migrados: patron antiguo, patron nuevo, archivos afectados.
- Generar changelog de modernizacion.

## Invariantes
- NUNCA actualizar sin tests verdes como baseline.
- NUNCA aplicar multiples updates simultaneamente.
- SIEMPRE revertir si tests fallan post-update.
- SIEMPRE obtener aprobacion del Operador para major updates.

## Signature Output

```markdown
## Modernizacion: {zona}

### Dependencias Actualizadas
| Dependencia | Antes | Despues | Tipo | Tests |
|-------------|-------|---------|------|-------|
| {nombre} | {v_old} | {v_new} | {patch|minor|major} | {pass|fail} |

### Patrones Migrados
| Patron Antiguo | Patron Nuevo | Ocurrencias | Archivos |
|----------------|--------------|-------------|----------|
| {antiguo} | {nuevo} | {n} | {archivos} |

### Pendientes
| Item | Razon | Accion Requerida |
|------|-------|-----------------|
| {nombre} | {breaking change / sin alternativa} | {descripcion} |
```
