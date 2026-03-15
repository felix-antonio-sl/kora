---
_manifest:
  urn: urn:ops:skill:clawstack-stack-auditor:1.0.0
  type: lazy_load_endofunctor
---

# CM-STACK-AUDITOR

## Proposito
Auditoria full-stack en 3 capas con multiples ejes por capa. Emite reporte PASS|WARN|FAIL por capa y global.

## Input/Output
- **Input:** capas: string[] (host|docker|openclaw), profundidad: normal|deep
- **Output:** AuditReport (ver Signature Output)

## Procedimiento

### Capa Host
1. SSH: key-only auth, root login disabled, puerto no-default.
2. Firewall: UFW activo, default deny, solo puertos necesarios.
3. Packages: actualizaciones pendientes, unattended-upgrades.
4. Services: systemd units activos, sin servicios innecesarios.
5. Storage: espacio disponible, particionado.
6. Time: chrony sincronizado.

### Capa Docker
1. Engine: version actualizada, daemon.json configurado.
2. Images: sin imagenes dangling, base images actualizadas.
3. Containers: running, healthchecks, restart policies.
4. Security: sin Docker socket expuesto a agentes, sin containers privilegiados, user namespaces.
5. Resources: limits CPU/memoria declarados, sin contenedores sin limites.

### Capa OpenClaw
1. Health: `openclaw status --deep`, `openclaw doctor`.
2. Security: `openclaw security audit`, DM policy, tool policy, sandbox config.
3. Performance: bootstrap size (<15K ok, >25K critical), sesiones activas, token economy.
4. Config quality: modelos configurados, canales conectados, heartbeat si aplica, backup strategy.

### Cross-layer
5. Puertos host vs puertos Docker vs gateway port: coherencia.
6. Secrets: no hardcodeados en compose ni workspace, SecretRef cuando disponible.
7. Networking: gateway en loopback, Docker networking no expone puertos internos.

### Reporte
8. Generar tabla por capa: eje | check | resultado | detalle | referencia.
9. Calcular resultado global: FAIL si cualquier critical, WARN si warnings, PASS si todo ok.

## Signature Output
| Campo | Tipo | Descripcion |
|-------|------|-------------|
| resultado_global | enum | PASS, WARN, FAIL |
| por_capa | {host, docker, openclaw} | Resultado y hallazgos por capa |
| hallazgos | AuditFinding[] | Lista con severidad, capa, check, detalle, fix, referencia |
| correcciones_prioritarias | string[] | Top 3 fixes mas urgentes |
