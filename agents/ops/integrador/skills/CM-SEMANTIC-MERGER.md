---
_manifest:
  urn: "urn:ops:skill:integrador-semantic-merger:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Verificar coherencia semantica de un PR contra el estado actual de main. No es merge textual — es validacion de que los cambios combinados preservan coherencia arquitectonica, contractual y de naming.

## Input/Output

- **Input:** pr: {diff: string, files: string[], branch: string, metadata: PRInfo}, main_state: {architecture: ArchInfo, conventions: ConventionSet, active_interfaces: InterfaceMap}
- **Output:** merge_analysis: {status: coherent|incoherent, issues: SemanticIssue[], severity: low|medium|high, recommendation: merge|hold|reject}

## Procedimiento

1. **Analizar tipos**:
   - Extraer tipos nuevos/modificados del PR
   - Verificar alineacion con tipos existentes en main
   - IF tipo nuevo contradice tipo existente → incoherent, severity high
   - IF tipo nuevo extiende tipo existente → verificar compatibilidad

2. **Analizar imports**:
   - Listar imports nuevos del PR
   - Verificar: no hay imports circulares, no hay imports duplicados, imports apuntan a modulos existentes
   - IF import a modulo inexistente → incoherent (posible dependencia no mergeada aun)

3. **Verificar convenciones naming**:
   - Extraer nombres nuevos (funciones, clases, variables, endpoints)
   - Comparar contra convenciones del proyecto (camelCase, snake_case, prefijos)
   - IF convencion violada → issue severity low, auto-fixable

4. **Verificar contratos de interfaz**:
   - Identificar interfaces publicas modificadas
   - Verificar que consumers existentes no se rompen
   - IF breaking change en interfaz publica → incoherent, severity high

5. **Verificar patrones arquitectonicos**:
   - Comparar estructura del cambio contra patrones existentes (layers, modules, dependency direction)
   - IF cambio introduce dependencia en direccion inversa → incoherent, severity medium
   - IF cambio duplica logica existente en otro modulo → issue severity medium

6. **Verificar CI + evals**:
   - Confirmar CI verde
   - Confirmar evals passed
   - IF CI rojo OR evals fallidos → reject inmediato

7. **Compilar resultado**: agregar todos los issues, calcular severidad maxima, emitir recomendacion.

## Signature Output

```yaml
merge_analysis:
  pr: "#205"
  status: "coherent"
  issues: []
  severity: "low"
  recommendation: "merge"
  checks:
    types_aligned: true
    imports_valid: true
    naming_conventions: true
    interfaces_preserved: true
    architecture_consistent: true
    ci_green: true
    evals_passed: true
```
