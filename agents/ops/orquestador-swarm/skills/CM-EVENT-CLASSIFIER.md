---
_manifest:
  urn: "urn:ops:skill:orquestador-swarm-event-classifier:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Clasificar eventos entrantes al sistema nervioso del enjambre. Determinar tipo de evento, nivel de riesgo y golden path correspondiente. Cada evento es un estimulo que el orquestador debe rutear.

## Input/Output

- **Input:** event: {type: string, payload: EventPayload, source: string, timestamp: ISO8601}
- **Output:** classification: {event_type: commit|pr|alert|config_change|sentinel_proposal|eval_result|heartbeat, risk: lectura|escritura|destructiva, golden_path: estandar|destructiva|infraestructura|hotfix, priority: 1-5, affected_systems: string[], requires_human: boolean}

## Procedimiento

1. **Identificar tipo de evento**:
   - Commit/PR → analizar diff y metadata
   - Alerta produccion → analizar severidad y sistema afectado
   - Config change → analizar scope del cambio
   - Sentinel proposal → evaluar propuesta de auditoria
   - Eval result → analizar pass/fail y cobertura
   - Heartbeat → registrar latido y verificar salud agente

2. **Clasificar riesgo** (para eventos con cambios de codigo/config):
   - .md, .yml (config), docs/ → lectura
   - Nuevos endpoints, features, mutacion datos → escritura
   - Schema migration, auth changes, data deletion → destructiva
   - Principio conservador: IF cualquier archivo destructivo → toda la clasificacion es destructiva

3. **Asignar golden path**:
   - Lectura/escritura PR → historia estandar
   - Destructiva PR → historia destructiva
   - Cambios infraestructura/IaC → infraestructura
   - Alerta produccion / bug report → hotfix
   - Heartbeat → no requiere golden path, solo registro

4. **Calcular prioridad** (1=maxima, 5=minima):
   - Alerta produccion CRITICAL → 1
   - Cambio destructivo → 2
   - Escritura (feature) → 3
   - Lectura (config/docs) → 4
   - Heartbeat/status → 5

5. **Determinar intervencion humana**:
   - IF destructiva → requires_human = true
   - IF alerta CRITICAL → requires_human = true
   - IF sentinel_proposal con cambio de politica → requires_human = true
   - ELSE → requires_human = false

## Signature Output

```yaml
classification:
  event_type: "pr"
  risk: "escritura"
  golden_path: "estandar"
  priority: 3
  affected_systems: ["api-gateway", "orders-service"]
  requires_human: false
  source: "github/PR#245"
  timestamp: "2026-02-24T10:00:00Z"
```
