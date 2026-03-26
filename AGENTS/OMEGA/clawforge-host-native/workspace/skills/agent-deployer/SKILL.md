---
name: agent-deployer
description: Deploy an OpenClaw agent to a server by syncing workspace, applying config, configuring auth and channels, starting the gateway, and verifying health. Use when the user wants to deploy a new agent or redeploy an existing one.
---

## Proposito

Llevar un agente OpenClaw desde workspace local hasta produccion en un servidor, dejandolo funcionando y verificado.

## Cuando se activa

- El usuario quiere desplegar un agente nuevo en un servidor.
- Se necesita redesplegar un agente existente tras cambios en workspace o config.
- Hay que promover un agente de staging a produccion.

## Checklist de promocion (antes de desplegar)

- [ ] Workspace completo: AGENTS.md, SOUL.md, IDENTITY.md existen y son coherentes.
- [ ] Config validada: `openclaw.json` pasa validacion contra schema.
- [ ] Credenciales disponibles: API keys y tokens listos (no hardcodeados).
- [ ] Canales configurados: tokens de Telegram/WhatsApp/Slack listos.
- [ ] Skills verificados: todos los skills requeridos presentes en workspace o managed.
- [ ] Host preparado: Node.js instalado, OpenClaw instalado, puertos disponibles.

## Procedimiento

1. **Verificar prerequisitos.** Node.js >= 18, OpenClaw instalado, conectividad, puertos libres.
2. **Copiar workspace.** Sincronizar archivos del agente al servidor destino.
3. **Aplicar config.** Colocar `openclaw.json` en la ubicacion correcta. Configurar provider y modelo.
4. **Configurar credenciales.** Inyectar API keys via env vars o `openclaw config set`. Nunca en archivos planos.
5. **Configurar canales.** Aplicar tokens y webhooks para cada canal habilitado.
6. **Instalar como daemon.** Configurar systemd service o pm2 para persistencia y auto-restart.
7. **Verificar health.** Ejecutar `openclaw health` y `openclaw doctor` desde el servidor.
8. **Smoke test.** Enviar un mensaje de prueba por el canal principal y verificar respuesta.

## Reglas

- **Checklist antes de deploy.** No desplegar sin pasar la checklist de promocion.
- **Secrets nunca en disco.** Usar variables de entorno o secret refs.
- **Evidencia de vida.** No declarar exito sin health check + smoke test exitosos.
- **Rollback plan.** Siempre tener claro como revertir si algo falla.

## Formato de salida

```
**Servidor:** <host>
**Agente:** <nombre>
**Checklist de promocion:** <PASS/FAIL por item>
**Pasos ejecutados:** <lista con resultado de cada paso>
**Health:** <resultado de openclaw health>
**Smoke test:** <resultado>
**Estado final:** <LIVE / FALLIDO + causa>
```
