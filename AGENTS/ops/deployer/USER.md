---
_manifest:
  urn: "urn:ops:agent-bootstrap:deployer-user:1.0.0"
  type: "bootstrap_user"
---

## Perfil

DevOps Engineers, SREs, Tech Leads que gestionan releases a produccion. Contexto: equipos que usan Xanpan con CI/CD pipeline y feature flags.

## Rutinas

Sesion de deploy: recibir PR/changeset → clasificar riesgo → seleccionar estrategia → ejecutar → verificar → reportar. Iterativa multi-turno con monitoreo post-deploy.

## Preferencias de Output

- Formato: Markdown con status y metricas
- Metricas: latencia (p50/p95/p99), tasa error, uso recursos
- Tablas: comparacion pre/post deploy
- Code blocks: configuracion feature flags, comandos deploy
- Idioma: es-CL
