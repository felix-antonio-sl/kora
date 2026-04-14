---
title: Docker Docs Map
status: internal
lang: es
source_policy: official_docs_only
---

# Docker Docs Map

Usar este mapa para consultas de Docker. Citar siempre el documento oficial indicado, no este archivo.

## Routing

| Tema | Documento oficial | URL |
|------|-------------------|-----|
| Arquitectura agentic con Compose, modelos y tools separados | Agentic AI applications | https://docs.docker.com/guides/agentic-ai/ |
| Docker daemon attack surface y baseline de seguridad | Security | https://docs.docker.com/engine/security/ |
| Proteccion del socket/daemon remoto | Protect the Docker daemon socket | https://docs.docker.com/engine/security/https/ |
| Acceso remoto a `dockerd` y conflicto `systemd` vs `daemon.json` | Configure remote access for Docker daemon | https://docs.docker.com/engine/daemon/remote-access/ |
| Rootless mode | Rootless mode | https://docs.docker.com/engine/security/rootless/ |
| `userns-remap` | Isolate containers with a user namespace | https://docs.docker.com/engine/security/userns-remap/ |
| Build secrets / BuildKit | Secrets | https://docs.docker.com/build/building/secrets/ |
| Secrets en Compose | Secrets in Compose | https://docs.docker.com/compose/how-tos/use-secrets/ |
| Orden de arranque, `depends_on`, healthchecks, restart behavior | Control startup order | https://docs.docker.com/compose/how-tos/startup-order/ |
| Referencia de `services`, `healthcheck`, `read_only`, `secrets` | Services | https://docs.docker.com/reference/compose-file/services/ |
| Modelos como dependencia declarativa en Compose | Use AI models in Compose | https://docs.docker.com/ai/compose/models-and-compose/ |

## Reglas de uso

- Para hallazgos sobre aislamiento, socket o privilegios, priorizar `Security`, `Protect the Docker daemon socket`, `Rootless mode` y `userns-remap`.
- Para preguntas de Compose operativo, priorizar `Secrets in Compose`, `Control startup order` y `Services`.
- Si un tema no aparece en el mapa, declarar gap de referencia y no responderlo como hecho factual cerrado.
