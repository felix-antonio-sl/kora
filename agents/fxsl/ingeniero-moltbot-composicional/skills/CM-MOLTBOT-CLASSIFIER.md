---
_manifest:
  urn: "urn:fxsl:agent-bootstrap:ingeniero-moltbot-composicional-cm-moltbot-classifier:1.0.0"
  type: "lazy_load_endofuntor"
---

## Proposito

Clasificar solicitudes del usuario en dominios Moltbot para enrutar al estado FSM apropiado. Emitir exactamente 1 etiqueta dominante con precedencia estricta.

## Input/Output

- **Input:** Solicitud del usuario (texto libre)
- **Output:** Etiqueta dominante: END | REQUIREMENTS | GATEWAY | CHANNELS | SESSIONS | TOOLS | OPERATIONS | CONSULT. Opcional: etiquetas secundarias para estados posteriores.

## Procedimiento

1. Evaluar precedencia estricta: END > REQUIREMENTS > GATEWAY > CHANNELS > SESSIONS > TOOLS > OPERATIONS > CONSULT
2. Clasificar por dimensiones:
   - END: usuario pide terminar/cerrar
   - REQUIREMENTS: nuevo proyecto/arquitectura o faltan datos base (plataforma/canales/acceso)
   - GATEWAY: configuracion, auth, Tailscale, bind, remote
   - CHANNELS: WhatsApp, Telegram, Discord, Slack, Signal, iMessage
   - SESSIONS: workspace, bootstrap, memoria, queue
   - TOOLS: browser, canvas, nodes, skills, cron
   - OPERATIONS: install, update, doctor, security
   - CONSULT: pregunta general sobre Moltbot
3. Cuando input es mixto, elegir dominante segun precedencia
4. Capturar etiquetas secundarias para ejecucion posterior

## Signature Output

```
DOMINANT: {etiqueta}
SECONDARY: [{etiquetas}] (opcional)
```
