---
_manifest:
  urn: urn:kora:skill:clawforge-stack-auditor:1.1.0
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
7. Puertos host vs puertos Docker vs gateway port: coherencia.
8. Secrets: no hardcodeados en compose ni workspace, SecretRef cuando disponible.
9. Networking: `gateway.bind` coherente con topologia Docker (bind="lan" para kora-federation bridge; port mapping Docker en 127.0.0.1 protege del exterior).

### Federation
10. Hooks: `hooks.enabled: true` en cada gateway, token configurado en runtime segun el patron soportado, endpoint alcanzable desde otros containers y secreto nunca duplicado en bootstrap/docs del agente.
11. Bind: `gateway.bind: "lan"` en cada gateway (requerido para hooks cross-gateway en Docker bridge).
12. Shared storage: `/srv/kora/shared/federation/` montado RO en todos; directorio propio (`/srv/kora/shared/{agent_id}/`) montado RW en cada container.
13. Directorio de agentes: `/srv/kora/shared/federation/directorio-agentes.md` existe, es legible desde todos los containers, y lista todos los agentes desplegados con dominio, hook URL y canal.
14. Hooks bidireccional: test `curl POST /hooks/agent` entre cada par de gateways exitoso (HTTP 200 + runId).
15. Panel web: `kora-panel` container healthy, `https://kora.sanixai.com/api/health` retorna todos los gateways OK, registry.json actualizado.
16. Workspace docs del agente: no contienen overlays operacionales vivos ni secretos de federation; la metadata de derivacion vive en config runtime y `/srv/kora/shared/federation/directorio-agentes.md`.

### Drift Detection (agentes desplegados)
17. Workspace drift: para cada agente desplegado en /srv/kora/workspaces/, diff version stripped del repo KORA vs version desplegada. Clasificar: regla emergente (backport candidate), residuo (limpiar), memory (normal), heartbeat (normal).
18. Config drift: diff source en /srv/kora/config/{gateway}/openclaw.json5 vs config real en named volume.
19. Image drift: comparar SHA de imagen running vs ultima imagen built.

### Reporte
20. Generar tabla por capa: eje | check | resultado | detalle | referencia.
21. Calcular resultado global: FAIL si cualquier critical, WARN si warnings, PASS si todo ok.

## Signature Output
| Campo | Tipo | Descripcion |
|-------|------|-------------|
| resultado_global | enum | PASS, WARN, FAIL |
| por_capa | {host, docker, openclaw, cross_layer, federation} | Resultado y hallazgos por seccion |
| hallazgos | AuditFinding[] | Lista con severidad, capa, check, detalle, fix, referencia |
| correcciones_prioritarias | string[] | Top 3 fixes mas urgentes |
