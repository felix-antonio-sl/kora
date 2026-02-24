---
_manifest:
  urn: "urn:kora:skill:architect-validation-engine:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-VALIDATION-ENGINE

## Proposito

Validar artefactos KORA (KBs, agentes, manifiestos) contra el schema y los principios P1-P7 para garantizar conformidad con la especificacion.

## Procedimiento

1. Recibir artefacto a validar e identificar su tipo: KB (KORA/MD) | agente (workspace) | manifiesto YAML
2. Ejecutar validacion de sintaxis: estructura YAML/Markdown valida, campos requeridos presentes, tipos correctos
3. Verificar compliance con P1-P7: encapsulacion, abstraccion, federacion, minimalismo, trazabilidad, separacion concerns, evolucion controlada
4. Revisar seguridad: block_instructions present, forbid_internal_jargon, process steps <= 5
5. Si agente: verificar componentes KORA presentes (AGENTS.md, SOUL.md, USER.md, TOOLS.md, config.json)
6. Generar reporte con hallazgos por categoria: ERROR (bloquea uso) | WARNING (degradacion) | INFO (sugerencia)
7. Para cada ERROR: proporcionar correccion especifica

## Output

Reporte de validacion con hallazgos clasificados (ERROR | WARNING | INFO) + correcciones especificas para cada ERROR + metricas de compliance.
