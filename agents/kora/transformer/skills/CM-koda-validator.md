---
_manifest:
  urn: "urn:kora:agent-bootstrap:transformer-cm-koda-validator:1.0.0"
  type: "lazy_load_endofuntor"
---

## Proposito

Validar artefacto KODA contra especificacion completa y calcular metricas de calidad FS y CR.

## Input/Output

- **Input:** Artefacto KODA desde S-VALIDATOR o S-AUDITOR
- **Output:** Reporte de validacion con checklist, metricas calculadas, hallazgos y correcciones

## Procedimiento

1. **Syntax check:**
   - YAML valido (parseable sin errores)
   - Metadata block completo (Version, Status, Human-Creator, etc.)
   - LLM_Parsing_Instructions presente
2. **Keywords check:**
   - Keywords de lexicon oficial (Tier 1 + Tier 2)
   - IDs unicos dentro del artefacto
   - Referencias validas (todos los Ref apuntan a ID existente)
3. **Quality check:**
   - Fidelidad 100% (todo el meat preservado)
   - Cero redundancia (Ref usado para repeticiones)
   - Estructura preservada (jerarquias, tablas, listas)
4. **Metrics calculation:**
   - FS (Fidelity Score) = hechos preservados / hechos originales × 100
   - CR (Compression Ratio) = caracteres_original / caracteres_koda
   - Objetivo: FS=100%, CR>1.0
5. IF alguna verificacion falla → generar lista de correcciones especificas
6. IF todas pasan → artefacto validado, listo para uso

## Signature Output

```
**Validacion KODA**:
| Categoria | Resultado |
|-----------|-----------|
| Syntax | [PASS/FAIL — detalles] |
| Keywords | [PASS/FAIL — detalles] |
| Quality | [PASS/FAIL — detalles] |
| FS | [valor%] |
| CR | [valor] |
**Veredicto**: [VALID|NEEDS_CORRECTION]
```
