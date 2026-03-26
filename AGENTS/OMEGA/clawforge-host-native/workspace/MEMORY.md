# Memory

## Origen

- **2026-03-26**: Este agente fue destilado desde una encarnacion previa que operaba como gateway OpenClaw dockerizado dentro de una federacion multi-gateway.
- La destilacion extirpo toda referencia a: federacion kora, agentes hermanos (korax, steipete, salubrista, curator), Docker (containers, compose, bind mounts, imagenes, redes), framework KORA (specs, URNs, gobernanza, agent-spec, FSMs formales), paths de servidores previos, historia operacional anterior.
- Se preservo unicamente la esencia: identidad de forjador, paradigma cognitivo, capacidades de ciclo de vida OpenClaw, reglas duras, tono, y 33 skills operativos (32 originales + 1 server admin).
- La forma actual es la mas ligera y pura posible. Todo lo que este agente sabe sobre si mismo esta en los archivos bootstrap. No hay estado oculto ni dependencias implicitas.

## Decisiones

- **2026-03-26**: Forma pura adoptada. Sin FSM formal — comportamiento expresado en prosa natural. Sin co-induccion formal — guardrails simples. Sin routing de URNs — herramientas reales del runtime.
- **2026-03-26**: Skill `server` (clawhub.ai/ivangdavila/server v1.0.0) incorporado para administracion de servidores: nginx, Caddy, SSL, Docker Compose, process management, troubleshooting.
- **2026-03-26**: Topologia target: single-gateway multi-agent sobre host nativo. Agentes adicionales se agregan bajo el mismo gateway via `openclaw agents add`.
- **2026-03-26**: Auditoria de skills contra SSOT OpenClaw (manual-integral + manual-skills). Hallazgos criticos:
  - H-01 (CRIT): Ninguno de los 32 skills originales tenia frontmatter YAML — invisibles para OpenClaw runtime.
  - H-02 (CRIT): 18 skills eran archivos .md planos en raiz, no directorios con SKILL.md — formato invalido.
  - H-03 (HIGH): Nombres en MAYUSCULAS (CM-OPENCLAW-*) — spec exige lowercase con hyphens.
  - Accion: factorizacion completa. 32 skills no conformes → 12 skills nuevos + 1 server intacto = 13 skills totales.
  - Funciones absorbidas en AGENTS.md (no son skills): intent-classifier, context-manager, lifecycle-orchestrator, handoff.
  - Skills fusionados: 6 de contratos → agent-config. 3 de troubleshooting → troubleshooter. 2 de knowledge → openclaw-docs. designer+builder+topologist → agent-designer. operator+evolver+optimizer+configurator → operator.
  - Todos los 13 skills finales: directorio/SKILL.md, frontmatter valido, nombre lowercase, <100 lineas, cero contaminacion.
