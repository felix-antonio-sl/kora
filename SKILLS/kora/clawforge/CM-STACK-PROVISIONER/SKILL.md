---
_manifest:
  urn: urn:kora:skill:clawforge-stack-provisioner:1.1.0
  type: lazy_load_endofunctor
extensions:
  ops:
    skill:
      form: extended
      allowed_tools:
        - host_exec
        - docker_exec
        - oc_cli
      requires: []
      references:
        - references/provision-checklist.md
      assets:
        - assets/compose-templates.md
---

# CM-STACK-PROVISIONER

## Proposito
Ejecuta provisioning full-stack desde cero: host Ubuntu hardened -> Docker con aislamiento -> OpenClaw operacional. Cada fase verifica exito antes de avanzar.

## Input/Output
- **Input:** plataforma: string (ubuntu-vps|ubuntu-cloud), config_deseada: {canales, agentes, modelo}
- **Output:** ProvisionReport (ver Signature Output)

## Procedimiento

0. VALIDAR ALCANCE:
   - Este skill cubre provisioning host-based sobre Ubuntu Server.
   - Si el operador ya trae un host Docker existente o esta en otra plataforma Unix, NO improvisar provisioning. Emitir: "Provisioning inicial no soportado por este skill en esta plataforma. Continuar por path de consulta/configuracion/auditoria/troubleshooting segun corresponda." y terminar procedimiento.

### Capa Host Ubuntu
1. Verificar acceso SSH y version OS: `cat /etc/os-release`, `uname -r`.
2. Actualizar sistema: `apt update && apt upgrade -y`.
3. Configurar SSH hardened: deshabilitar root login, solo key auth, puerto custom si aplica.
4. Configurar firewall: `ufw default deny incoming`, `ufw allow ssh`, `ufw enable`.
5. Configurar chrony para sincronizacion horaria.
6. Verificar: `systemctl status ssh`, `ufw status`, `chronyc tracking`.

### Capa Docker
1. Instalar Docker Engine (repo oficial, no snap): `apt install docker-ce docker-ce-cli containerd.io`.
2. Configurar Docker: daemon.json con log rotation, storage driver, userns-remap si aplica.
3. Instalar Docker Compose v2.
4. Verificar: `docker info`, `docker compose version`.
5. Si deploy via compose: generar docker-compose.yml desde template (ver assets/compose-templates.md).

### Capa OpenClaw
1. Instalar Node.js >= 22.12.0 (via NodeSource o nvm).
2. Instalar OpenClaw: `npm install -g openclaw`.
3. Ejecutar onboarding: `openclaw onboard`.
4. Configurar gateway: loopback-first, auth, canales iniciales.
5. Verificar: `openclaw status`, `openclaw doctor`.
6. Si systemd: instalar daemon persistente con `openclaw gateway install`.

### Servicios complementarios (Docker apps con Traefik)

Para servicios complementarios al stack OpenClaw (panel web, bridges, dashboards), no gateways:

1. El codigo fuente DEBE vivir en `~/projects/{nombre}/` (nunca en /srv/kora/).
2. docker-compose.yml con labels Traefik para exposicion HTTPS:
   - `traefik.http.routers.{name}.rule=Host(\`{subdominio}.sanixai.com\`)`
   - `traefik.http.routers.{name}.entrypoints=websecure`
   - `traefik.http.routers.{name}.tls.certresolver=myresolver`
   - `traefik.docker.network=web`
3. Si requiere acceso a gateways OpenClaw: agregar red `kora-federation` (external: true).
4. Si requiere acceso a Docker: montar `/var/run/docker.sock:ro`.
5. Auth: basic auth via middleware Traefik (`traefik.http.middlewares.{name}-auth.basicauth.users={htpasswd}`). Generar con `htpasswd -nb user password`.
6. Verificar: `curl -s -o /dev/null -w "%{http_code}" https://{subdominio}.sanixai.com -u user:password` == 200.
7. Let's Encrypt genera cert automaticamente via TLS-ALPN-01. No requiere restart de Traefik.

### Verificacion Final
7. Ejecutar audit cross-layer: host (SSH+UFW) x Docker (engine+images) x OpenClaw (gateway+channels).
8. Consultar references/provision-checklist.md para validar completitud.

## Signature Output
| Campo | Tipo | Descripcion |
|-------|------|-------------|
| plataforma | string | Plataforma provisionada |
| fases | {host, docker, openclaw} | Estado de cada fase (ok|error|skipped) |
| servicios | string[] | Servicios activos post-provision |
| audit_result | PASS|WARN|FAIL | Resultado de audit final |
| proximos_pasos | string[] | Configuraciones pendientes |
