---

# Reporte Post-Auditoría — Acciones Aplicadas

## Fixes Ejecutados

| # | Fix | Estado | Detalle |
|---|-----|--------|---------|
| H3 | X11Forwarding=no | **DONE** | `/etc/ssh/sshd_config` editado, `ssh.service` reloaded. Sesiones activas no afectadas |
| H9 | nftables upgrade | **DONE** | `libnftables1` + `nftables` 1.0.9-1ubuntu0.1 instalados |
| H11 | zram-config disabled | **DONE** | Deshabilitado via systemctl. Seguirá en `failed` hasta próximo reboot |
| H12 | CUPS cerrado | **DONE** | Era snap, no servicio nativo. `snap disable cups` aplicado. Puerto 631 cerrado |
| OC9 | hooks.allowedAgentIds | **DONE** | Configurado `["main"]` en `openclaw.json`. Security audit bajó de 2 warn a 1 warn |
| OC11 | Orphan transcripts | **DONE** | 431 archivos eliminados, 37.2 MB liberados. `sessions.json` backup en `.bak.2026-03-17` |
| OC13 | Agent dir perms | **DONE** | 4 dirs cambiados de 0775 a 0700 (clawmaster, pensador, salubrista, urgencista) |
| OC14 | Startup optimization | **DONE** | `NODE_COMPILE_CACHE` + `OPENCLAW_NO_RESPAWN` en `.zshenv` + drop-in systemd para gateway |
| D6 | Docker prune | **DONE** | 408 MB build cache liberado. 0 imágenes/containers/volumes restantes |

## Mejora de Seguridad

```
ANTES: 0 critical · 2 warn · 2 info
AHORA: 0 critical · 1 warn · 2 info
```

## Puertos Escuchando (post-fix)

| Puerto | Bind | Proceso | Justificación |
|--------|------|---------|---------------|
| 22 | 0.0.0.0 | sshd | SSH (pubkey-only, fail2ban) |
| 443 | 100.99.32.96 (Tailscale) | Tailscale Funnel | HTTPS via Tailscale — correcto |
| 18789 | 127.0.0.1 | openclaw-gateway | Gateway loopback — correcto |
| 18790 | * | caddy | Reverse proxy con WebSocket — **ojo: binds 0.0.0.0** |
| 18791-92 | 127.0.0.1 | openclaw-gateway | Puertos internos gateway |
| 8788 | 127.0.0.1 | gog | Gmail watch — loopback |
| 3737 | * | next-server | Urgencista app — **ojo: binds 0.0.0.0** |
| 53 | 127.0.0.x | systemd-resolved | DNS local |
| ~~631~~ | ~~eliminado~~ | ~~cupsd~~ | ~~CUPS snap deshabilitado~~ |

## Pendientes (requieren tu decisión)

### P1 — FAIL: Hook token de `gog` expuesto en process list
El proceso `gog` pasa `--hook-token` como argumento CLI, visible para cualquier usuario local via `ps aux`. No es servicio systemd — no encontré cómo se arranca. **Necesito que me indiques cómo se inicia `gog`** para migrar el token a variable de entorno.

### P2 — Caddy (:18790) y next-server (:3737) en 0.0.0.0
Ambos servicios escuchan en todas las interfaces. UFW los protege (no están en allow), pero el principio de mínima superficie (R3) dice que deberían bindear a `127.0.0.1` si solo atienden tráfico local/túnel.

### P3 — Kernel 6.8.0-106 disponible
El upgrade de nftables detectó que hay kernel 6.8.0-106 disponible (corriendo 6.8.0-100). Requiere **reboot** — cuando sea ventana de mantenimiento.

### P4 — zram-config.service
Deshabilitado pero sigue en `failed` hasta reboot. Se limpiará solo al reiniciar.

### P5 — Swap 90% usado
3.6G de 4G de swap usados. No es urgente (hay 4.6G RAM disponible por cache), pero indica presión histórica. Considerar investigar qué proceso llenó swap, o aumentar RAM si es recurrente.

### P6 — sandbox.mode=off
Según Cap 7 §7.3, `sandbox.mode` está en `off`. En tu setup single-operator no es riesgo inmediato, pero si agregas usuarios no confiables via Slack, debería subir a `agent` o `all`.

