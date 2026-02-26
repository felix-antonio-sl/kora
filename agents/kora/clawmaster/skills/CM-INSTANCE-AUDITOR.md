---
_manifest:
  urn: "urn:kora:skill:clawmaster-instance-auditor:1.0.0"
  type: "lazy_load_endofunctor"
version: "1.0.0"
status: published
lang: es
---
# CM-INSTANCE-AUDITOR

## Proposito
Audita una instancia OpenClaw en cuatro ejes: health, security, performance y config quality. Produce reporte accionable.

## I/O

- **Input:** instancia: string | null (identificador de instancia, null=instancia local)
- **Output:** AuditReport (ver Signature Output)

## Procedimiento

### Eje 1: Health
- `openclaw status --all`
- `openclaw doctor`
- `openclaw health`
- Verificar: gateway running, canales conectados, daemon activo, modelos respondiendo, sesiones funcionales.

### Eje 2: Security (Cap 18, docs/security/)

| Check | Comando/Metodo | Criterio |
|-------|---------------|----------|
| Gateway auth | openclaw security audit | Token seguro, no default |
| DM policy | Config channels.*.allowFrom | No "open" sin intencion |
| Group policy | Config channels.*.groups | Mention gating o allowlist |
| Sandbox mode | Config agents.*.sandbox | non-main o always para produccion |
| Tool policy | Config agents.*.tools | Deny peligrosos en entornos compartidos |
| Elevated | Config agents.*.elevated | Deshabilitado por defecto |
| Prompt injection | Model strength | Opus/Sonnet para canales expuestos |
| Secrets in workspace | Revisar AGENTS.md, SOUL.md | Sin API keys o tokens en bootstrap |

### Eje 3: Performance
- Bootstrap size: sumar chars de AGENTS.md + SOUL.md + USER.md + TOOLS.md + IDENTITY.md. Warning si >15K total.
- Session count: `openclaw sessions --active 60`. Warning si >50 activas.
- Memory index: size de sqlite-vec DB. Warning si >1GB sin QMD.
- Model selection: adecuado al use case (haiku para chat rapido, opus para razonamiento).
- Compaction: auto-compaction habilitado.

### Eje 4: Config Quality
- Consistencia: model refs validos, channel configs completas.
- Best practices: heartbeat configurado, backup strategy definida.
- Actualizacion: version OpenClaw vs latest stable.

### Reporte
Tabla por eje: {check, status: PASS|WARN|FAIL, hallazgo, correccion, referencia}.
Resultado global: PASS (todo verde), WARN (mejoras recomendadas), FAIL (issues criticos).

## Signature Output

| Campo | Tipo | Descripcion |
|-------|------|-------------|
| resultado_global | enum(PASS\|WARN\|FAIL) | Resultado global de auditoria |
| ejes | {health, security, performance, config_quality} | Resultado por eje |
| hallazgos | {check, status, hallazgo, correccion, referencia}[] | Hallazgos detallados |
| correcciones_prioritarias | string[] | Correcciones ordenadas por prioridad |
