---
_manifest:
  urn: "urn:ops:agent-bootstrap:security-user:1.0.0"
  type: "bootstrap_user"
---

## Perfil

Security Engineers, Tech Leads, DevOps Engineers que gestionan seguridad del enjambre. Contexto: equipos que usan Xanpan con swarm de agentes LLM, CI/CD pipeline, y necesitan seguridad contextual continua.

## Rutinas

Sesion de seguridad: recibir PR/alerta/solicitud → clasificar tipo (analisis PR, runtime, dependencias, adversarial, meta-eval) → ejecutar analisis con contexto arquitectonico → reportar hallazgos con evidencia → emitir veto si critico. Iterativa multi-turno con acumulacion de hallazgos.

## Preferencias de Output

- Formato: Markdown con hallazgos estructurados
- Hallazgos: severity | evidence (file:line) | attack_vector | real_impact | suggested_fix
- Tablas: resumen hallazgos por PR, CVEs por exposicion
- Code blocks: evidencia, vectores, payloads
- Idioma: es-CL
