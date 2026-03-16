---
_manifest:
  urn: urn:ops:skill:clawstack-version-manager:1.0.0
  type: lazy_load_endofunctor
---

# CM-VERSION-MANAGER

## Proposito
Gestiona versiones del stack completo: host packages, Docker engine/images, OpenClaw releases. Pre-analysis, ejecucion segura, verificacion post-upgrade.

## Input/Output
- **Input:** target_layer: string (host|docker|openclaw|all), target_version: string | latest
- **Output:** UpgradeReport (ver Signature Output)

## Procedimiento
1. INVENTARIAR VERSIONES ACTUALES:
   - Host: `cat /etc/os-release`, `uname -r`, `apt list --upgradable`
   - Docker: `docker version`, `docker compose version`
   - OpenClaw: `openclaw --version`
2. PRE-UPGRADE ANALYSIS:
   - Leer changelogs y release notes
   - Identificar breaking changes
   - Evaluar impacto en config actual (campos deprecated, nuevos required, behavior changes)
   - Verificar compatibilidad entre capas (ej: OpenClaw new version requiere Node >= X?)
   - Para OpenClaw: consultar `openclaw update status` y definir canal/tag objetivo antes de ejecutar cambios
3. BACKUP:
   - Host: snapshot si disponible (LVM/ZFS), o backup configs criticos
   - Docker: tag images actuales antes de pull
   - OpenClaw: `openclaw backup create --verify` y registrar path del archivo generado
   - Si la config esta invalida y el backup completo falla: `openclaw backup create --no-include-workspace`
4. EJECUTAR UPGRADE (con confirmacion):
   - Host: `apt update && apt upgrade` (o selectivo)
   - Docker: `apt install docker-ce` (o Docker Desktop update)
   - OpenClaw: `openclaw update --dry-run` para preflight
   - OpenClaw: `openclaw update` para canal actual, o `openclaw update --channel <stable|beta|dev>` / `openclaw update --tag <dist-tag|version>` si se requiere cambio de destino
   - No usar `npm update -g openclaw` / `npm install -g openclaw@...` como path primario; el comando canonico es `openclaw update`
5. POST-UPGRADE VERIFICATION:
   - `openclaw --version`
   - `openclaw status --deep`
   - `openclaw security audit`
   - `openclaw doctor`
   - Si doctor detecta drift reparable y el usuario aprueba: `openclaw doctor --fix`
   - Verificar canales conectados, agentes respondiendo
6. ROLLBACK si verificacion falla:
   - Restaurar snapshot/tag/archive correspondiente (host, Docker, OpenClaw)
   - Para OpenClaw: usar el artefacto generado por `openclaw backup create` y documentar canal/version fallida
   - Documentar causa del fallo y evidencia post-mortem

## Signature Output
| Campo | Tipo | Descripcion |
|-------|------|-------------|
| versiones_anteriores | {host, docker, openclaw} | Versiones pre-upgrade |
| versiones_nuevas | {host, docker, openclaw} | Versiones post-upgrade |
| breaking_changes | string[] | Breaking changes detectados |
| migraciones | string[] | Migraciones aplicadas automaticamente |
| verificacion | PASS|FAIL | Verificacion post-upgrade |
| rollback_disponible | bool | Si hay backup para rollback |
