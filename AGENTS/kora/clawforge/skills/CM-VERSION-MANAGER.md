---
_manifest:
  urn: urn:kora:skill:clawforge-version-manager:1.1.0
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
   - OpenClaw (si instalado globalmente): `openclaw update --dry-run` para preflight, luego `openclaw update` para canal actual, o `openclaw update --channel <stable|beta|dev>` / `openclaw update --tag <dist-tag|version>` si se requiere cambio de destino. No usar `npm update -g openclaw` como path primario.
   - OpenClaw (si construido desde source en Docker — caso kora-federation): procedimiento de rebuild de imagen:
     a. Tag imagen actual para rollback: `docker tag openclaw-local:latest openclaw-local:v{old}` (y `kora-personal:latest` si es imagen separada: `docker tag kora-personal:latest kora-personal:v{old}`).
     b. Checkout version target en el repo operativo de OpenClaw: `cd {openclaw_repo_path} && git fetch --tags origin && git checkout v{new}`.
     c. Rebuild imagen: `cd {openclaw_repo_path} && docker build --build-arg OPENCLAW_INSTALL_BROWSER=1 -t openclaw-local:latest -t openclaw-local:v{new} .` (puede tomar 5-10 min).
     d. Si hay imagenes con nombre distinto (ej: kora-personal:latest): `docker tag openclaw-local:latest kora-personal:latest`.
     e. Rolling restart por criticidad (menor a mayor): para cada gateway, `docker compose -f /srv/kora/compose-{gw}/docker-compose.yml up -d` (recreate con nueva imagen). Esperar healthcheck entre cada uno.
     f. Verificar cada gateway: `docker exec {container} openclaw --version` == v{new} y `docker inspect {container} --format '{{.State.Health.Status}}'` == healthy.
     g. Si falla: `docker tag openclaw-local:v{old} openclaw-local:latest` + rolling restart para rollback.
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
