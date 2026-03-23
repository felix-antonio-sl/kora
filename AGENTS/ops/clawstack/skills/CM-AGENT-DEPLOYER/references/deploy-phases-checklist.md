# Deploy Phases Checklist

Verificacion para el pipeline de 16 fases de CM-AGENT-DEPLOYER. Marcar cada item al completar.

## Grupo A: Infraestructura

- [ ] P01: /srv/kora/ estructura creada, ownership correcta
- [ ] P02: Archivos bootstrap stripped y copiados, conteo coincide con fuente
- [ ] P02: Skills copiados (degenerados y extendidos con fibras)
- [ ] P02: config.json excluido del workspace (metadata KORA, principios P3)
- [ ] P03: KBs sincronizadas segun deployment_hints.kb_mounts, permisos RO
- [ ] P04: Imagen Docker base construida (openclaw-local:latest)
- [ ] P04: Imagen sidecar construida (solo caso-b)

## Grupo B: Bot (interactivo)

- [ ] P06: Token de bot obtenido de BotFather
- [ ] P06: User ID obtenido de @userinfobot (INTEGER)

## Grupo C: Configuracion

- [ ] P05: openclaw.json5 parametrizado con datos reales
- [ ] P05: docker-compose.yml valido (docker compose config --quiet)
- [ ] P05: kora-federation network: external si ya existe, create si primera vez (H3)
- [ ] P05: Port spacing minimo 20 entre gateways (principios P7)
- [ ] P07: .env generado con tokens, chmod 600
- [ ] P07: allowFrom actualizado como integer en openclaw.json5
- [ ] P08: Named volume inicializado, ownership uid 1000
- [ ] P08: Config copiado al volume

## Grupo D: Auth (interactivo)

- [ ] P09: Auth setup completado (OAuth o API key)

## Grupo E: Deploy

- [ ] P10: openclaw doctor reporta cero errores
- [ ] P11: Containers up y healthy
- [ ] P11: Logs muestran arranque exitoso

## Grupo F: Pairing (interactivo)

- [ ] P12: Pairing de Telegram aprobado
- [ ] P13: Verificacion e2e pasada (respuesta coherente)

## Grupo G: Lifecycle (on-demand)

- [ ] P14: Drift check completado (baseline establecido en primer deploy)
- [ ] P15: Backup realizado
- [ ] P16: Re-sync testeado (opcional en primer deploy)
