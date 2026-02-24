---
_manifest:
  urn: "urn:ops:agent-bootstrap:verificador-user:1.0.0"
  type: "bootstrap_user"
---

## Perfil

DevOps Engineers, SREs, Tech Leads que operan enjambres de agentes IA bajo Xanpan::Agents. Contexto: equipos donde agentes generan codigo y tests, requiriendo verificacion multi-capa para compensar la perdida de independencia evaluador/evaluado.

## Rutinas

Sesion de verificacion: recibir PR/changeset → clasificar riesgo → ejecutar capas secuencialmente → reportar verdict. Iterativa multi-turno. Capas individuales pueden ejecutarse aisladamente para diagnostico.

## Preferencias de Output

- Formato: Markdown con status por capa y evidencia
- Tablas: resumen de capas (capa, estado, detalle, evidencia)
- Code blocks: outputs de lint, tests, evals
- Veredictos: APROBADO | RECHAZADO con capa fallida y razon
- Idioma: es-CL
