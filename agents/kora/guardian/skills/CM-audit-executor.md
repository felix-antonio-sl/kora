---
_manifest:
  urn: "urn:kora:agent-bootstrap:guardian-cm-audit-executor:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Ejecutar auditoria completa de artefactos KODA contra especificacion, reportando hallazgos con severidad.

## Input/Output

- **Input:** Artefacto KODA o conjunto de artefactos a auditar desde S-AUDITOR
- **Output:** Reporte de auditoria con hallazgos clasificados por severidad (ERROR|WARNING|INFO) y recomendaciones

## Procedimiento

1. **LLM Parsing check:**
   - LEXICON con Ctx/XRef presentes
   - REFERENCE POLICY ok
   - Keywords del lexicon oficial
2. **Catalog check:**
   - Files referenciados existen en filesystem
   - Manifest completo (urn, federation, compatibility, resolution, dependencies)
   - URNs resuelven correctamente via catalogo
3. **Federation check:**
   - .knowledge-resolver.yml presente si aplica
   - registry/namespaces.yml coherente
   - Cross-repo references validas
4. **Agent compliance check (si aplica):**
   - 7 namespaces presentes
   - Guard Set completo (scope_policy, rejection, block_instructions, forbid_jargon)
   - process<=5 por estado
   - CMs con expose:false
   - Transiciones apuntan a estados existentes
5. Clasificar hallazgos:
   - ERROR: Viola especificacion, rompe funcionalidad
   - WARNING: Desvio de mejores practicas, riesgo futuro
   - INFO: Sugerencia de mejora, estilo
6. Generar recomendaciones de accion por hallazgo

## Signature Output

```
**Auditoria**: [artefacto]
**Hallazgos**: [N total] — [E errors] [W warnings] [I info]
| Severidad | Categoria | Hallazgo | Recomendacion |
|-----------|-----------|----------|---------------|
| ERROR | [cat] | [desc] | [fix] |
| WARNING | [cat] | [desc] | [fix] |
**Veredicto**: [CONFORMING|NON-CONFORMING|NEEDS-REVIEW]
```
