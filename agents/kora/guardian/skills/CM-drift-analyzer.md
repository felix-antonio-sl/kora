---
_manifest:
  urn: "urn:kora:agent-bootstrap:guardian-cm-drift-analyzer:1.0.0"
  type: "lazy_load_endofuntor"
---

## Proposito

Diagnosticar drift (desviacion) en artefactos KODA identificando causa raiz y proponiendo fix validable.

## Input/Output

- **Input:** Hallazgos ERROR/vulnerabilidad desde S-AUDITOR via S-DIAGNOSTICIAN
- **Output:** Diagnostico con causa raiz, fix propuesto, validacion del fix

## Procedimiento

1. Recibir hallazgo con severidad ERROR o vulnerabilidad
2. Clasificar tipo de drift:
   - LLM_Parsing outdated → Fix: Sync con guide_001
   - Catalog missing → Fix: Add URN entry al catalogo
   - Fallback unreachable → Fix: Update URL/path
   - Agent namespace missing → Fix: Agregar namespace faltante
   - Guard Set incomplete → Fix: Completar campos requeridos
   - Reference broken → Fix: Actualizar URN o path
3. Identificar causa raiz:
   - IF drift temporal → spec evoluciono, artefacto no
   - IF drift estructural → artefacto fue modificado sin validacion
   - IF drift referencial → recurso movido o eliminado
4. Proponer fix especifico y localizado
5. Validar fix (CM-FIX-VALIDATOR):
   - Fix addresses issue → verificar correccion
   - Re-run check → ejecutar verificacion post-fix
   - Residual risk → evaluar si el fix introduce nuevos problemas
6. IF fix validado → retornar a S-AUDITOR para re-auditoria
7. IF fix complejo → escalar a S-DISPATCHER

## Signature Output

```
**Drift detectado**: [tipo]
**Causa raiz**: [temporal|estructural|referencial]
**Artefacto**: [path]
**Fix propuesto**: [descripcion]
**Validacion**: [PASS|FAIL — detalle]
**Riesgo residual**: [NONE|LOW|MEDIUM|HIGH]
```
