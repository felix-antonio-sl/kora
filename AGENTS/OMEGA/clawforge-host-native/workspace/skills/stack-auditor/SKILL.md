---
name: stack-auditor
description: Audit the complete state of an OpenClaw deployment including host health, gateway status, config conformity, skills loaded, channels connected, sessions, and security posture. Use when the user wants a health check, conformity audit, or drift detection.
---

## Proposito

Evaluar el estado completo de un despliegue OpenClaw — desde el host hasta el gateway — y emitir un reporte con hallazgos clasificados por severidad.

## Cuando se activa

- El usuario pide un health check general del stack.
- Se sospecha drift entre config declarada y estado real.
- Antes de un upgrade o cambio mayor, para establecer baseline.
- Auditoria periodica de seguridad o conformidad.

## Procedimiento

1. **Host.** Verificar disco, memoria, carga, conectividad, puertos.
2. **Gateway.** Ejecutar `openclaw health`, `openclaw doctor`, `openclaw status --deep`.
3. **Config.** Validar `openclaw.json` contra schema. Detectar campos deprecated o desconocidos.
4. **Skills.** Listar skills elegibles (`openclaw skills list --eligible`). Verificar que los esperados estan cargados.
5. **Canales.** Verificar estado de cada canal configurado. Confirmar conectividad.
6. **Sessions.** Revisar sessions activas, TTL, storage.
7. **Seguridad.** Ejecutar `openclaw audit --deep` si disponible. Revisar tools policy, sandbox config, secrets exposure.
8. **Emitir reporte.** Consolidar hallazgos con severidad y accion sugerida.

## Clasificacion de severidad

| Nivel | Criterio |
|-------|----------|
| **CRIT** | El agente no funciona o hay riesgo de seguridad activo. Requiere accion inmediata. |
| **WARN** | Degradacion, drift, o configuracion suboptima. Requiere atencion pronto. |
| **INFO** | Observacion sin impacto operativo. Para registro y mejora continua. |

## Reglas

- **Evidencia, no suposicion.** Cada hallazgo debe tener un comando o verificacion que lo respalda.
- **Capa explicita.** Indicar si el hallazgo es de host o de gateway.
- **Accion sugerida.** Todo hallazgo CRIT o WARN debe incluir correccion propuesta.

## Formato de salida

```
# Auditoria OpenClaw — <agente> @ <host>
**Fecha:** <timestamp>

## Resumen
| Capa | CRIT | WARN | INFO |
|------|------|------|------|
| Host | ...  | ...  | ...  |
| Gateway | ... | ... | ... |
| Config | ... | ... | ... |
| Skills | ... | ... | ... |
| Canales | ... | ... | ... |
| Seguridad | ... | ... | ... |

## Hallazgos
| # | Sev | Capa | Hallazgo | Evidencia | Accion |
|---|-----|------|----------|-----------|--------|
| 1 | ... | ...  | ...      | ...       | ...    |

## Veredicto
<PASS / PASS-CON-WARNINGS / FAIL + resumen>
```
