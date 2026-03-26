---
name: agent-designer
description: Design an OpenClaw agent from scratch including identity, persona, behavior, topology, channels, skills, and config blueprint. Use when the user wants to create a new agent or define its architecture.
---

## Proposito

Producir el blueprint completo de un agente OpenClaw: desde la identidad hasta el plan de config y despliegue.

## Cuando se activa

- El usuario quiere crear un agente nuevo.
- Se necesita definir la arquitectura de un agente: topologia, canales, skills, modelo.
- Hay que decidir entre single-gateway, multi-agent, o agente aislado.

## Procedimiento

1. **Clarificar proposito y audiencia.** Que hace el agente, para quien, en que contexto opera.
2. **Elegir topologia.** Single-gateway (un agente, un gateway), multi-agent (varios agentes bajo un gateway), o aislado (gateway dedicado).
3. **Definir identidad.** Nombre, emoji, vibe — lo que va en `IDENTITY.md`.
4. **Definir persona.** Tono, estilo, limites — lo que va en `SOUL.md`.
5. **Definir comportamiento.** Mision, como trabaja, principios, guardrails — lo que va en `AGENTS.md`.
6. **Planificar skills.** Que capacidades necesita. Separar bundled vs workspace vs managed.
7. **Planificar canales.** Telegram, WhatsApp, Slack, web, API — cuales y con que config.
8. **Planificar config.** Modelo, tools policy, sandbox, sessions, heartbeat, cron.
9. **Emitir blueprint.** Documento accionable con todo lo anterior.

## Reglas

- **Topologia explicita.** Siempre declarar y justificar la topologia elegida.
- **Skills minimos.** Solo los necesarios para la mision. No inflar.
- **Config derivada, no inventada.** Cada campo de config debe responder a un requisito concreto.

## Template de salida

```markdown
# Blueprint: <nombre-agente>

## Identidad
- **Nombre:** <name>
- **Emoji:** <emoji>
- **Vibe:** <una linea>

## Topologia
<single-gateway | multi-agent | aislado> — <justificacion>

## Persona (SOUL.md)
<resumen de tono, estilo, limites>

## Comportamiento (AGENTS.md)
<mision + principios clave>

## Skills
| Skill | Tipo | Proposito |
|-------|------|-----------|
| ...   | workspace/bundled/managed | ... |

## Canales
| Canal | Config clave |
|-------|-------------|
| ...   | ...         |

## Config (openclaw.json)
<fragmento JSON5 con las claves relevantes>

## Prerequisitos
<dependencias de host, binarios, API keys>

## Siguiente paso
<que hacer despues: materializar workspace, configurar, desplegar>
```
