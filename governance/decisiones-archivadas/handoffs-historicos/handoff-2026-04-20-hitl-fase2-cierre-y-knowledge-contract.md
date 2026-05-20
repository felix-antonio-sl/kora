---
_manifest:
  urn: "urn:kora:kb:handoff-2026-04-20-hitl-fase2-cierre-y-knowledge-contract"
  provenance:
    created_by: "Codex GPT-5 (encarnando steipete)"
    created_at: "2026-04-20"
    source: "Cierre operativo posterior a Fase 0, Fase 1, Fase 2 y cierre del knowledge contract explícito en transmutación."
version: "1.0.0"
status: publicado
tags: [handoff, hitl, fase-2, urgenciologo, knowledge-contract, transmutacion, deploy-status]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:kora:kb:operational-memory-2026-04-20-hitl-fase2-cierre-y-knowledge-contract"
    - "urn:kora:kb:next-session-prompt-2026-04-20-hitl-fase2-cierre-y-knowledge-contract"
  refines:
    - "urn:kora:kb:handoff-2026-04-19-portabilidad-asegurada"
---

# Handoff explícito — cierre HITL, Fase 2 y knowledge contract explícito

## Resumen ejecutivo

Al cierre del **20 de abril de 2026**, KORA quedó con:

1. **Fase 0** cerrada en lo reversible.
2. **Decisiones HITL pendientes** ya resueltas en gobernanza:
   - `_perfiles` baja a drafts en `artifacts/agents/_FRAGUA/INBOX/perfiles/`
   - `Hermes` queda bloqueado fuera del critical path
   - `harness-spec`, `autoria-spec` y `transmutation-spec` quedan en freeze formal hasta cerrar Fase 3
3. **Fase 1** cerrada con la primera astilla clínica real:
   - consumidor: `salud/urgenciologo`
   - KB foco: `urn:salud:kb:me-dolor-toracico`
   - runtime: `claude-code`
   - canario real ejecutado con cambio de respuesta tras editar el nodo KB
4. **Fase 2** cerrada:
   - `invocations.jsonl`
   - `retrieval.jsonl`
   - `lead-time.jsonl`
   - `verified_at`
   - `deploy-status`
   - `bundle-coherence`
5. **Gap de transmutación resuelto**:
   - el `knowledge_contract` ya no queda implícito; ahora se proyecta explícitamente a `_transmutation.yml`
   - el bundle Claude renderiza `## Knowledge Contract` con URNs, rutas y paths locales

## Commits funcionales relevantes

Cadena útil reciente:

- `30efbdc` — spec Fase 1 `urgenciologo`
- `a32990c` — skeleton clínico inicial
- `88ff391` — cierre HITL pendiente + endurecimiento Fase 2
- `a5a9765` — automatización de telemetría Fase 2
- `dbc6ba1` — knowledge contract explícito en transmutación

Todo eso ya está en `origin/master`.

## Estado actual del sistema

### Gobernanza

- `governance/gobernanza.md` en `v4.5.0`
- `_perfiles` desformalizado
- `Hermes` removido del target activo y fuera de `harness-spec`
- freeze formal declarado hasta cierre de Fase 3

### Checks y tests

Verificación fresca corrida en esta sesión:

```bash
python3 toolchain/kora check --strict
python3 -m unittest discover -s tests
python3 toolchain/kora deploy-status
```

Resultado:

- `check --strict` → `Checks run: 18`, `Passed: 18`, `Failed: 0`
- `unittest` → `Ran 320 tests`, `OK (skipped=2)`
- `deploy-status`:
  - `salud/urgenciologo` en `claude-code` = `ok`
  - otros agentes Claude = `missing`
  - `stale = 0`

### Astilla clínica viva

Artefactos clave:

- KB foco: [dolor-toracico.md](/Users/felixsanhueza/Developer/kora/artifacts/knowledge/salud/med-emergencia/dolor-toracico.md)
- TOC: [toc-body-of-knowledge.md](/Users/felixsanhueza/Developer/kora/artifacts/knowledge/salud/med-emergencia/toc-body-of-knowledge.md)
- agente productivo: [artifacts/agents/salud/urgenciologo/AGENT.md](/Users/felixsanhueza/Developer/kora/artifacts/agents/salud/urgenciologo/AGENT.md)
- bundle Claude: [artifacts/agents/salud/urgenciologo/_BUILD/claude-code/urgenciologo.md](/Users/felixsanhueza/Developer/kora/artifacts/agents/salud/urgenciologo/_BUILD/claude-code/urgenciologo.md)
- manifest de transmutación: [artifacts/agents/salud/urgenciologo/_BUILD/claude-code/_transmutation.yml](/Users/felixsanhueza/Developer/kora/artifacts/agents/salud/urgenciologo/_BUILD/claude-code/_transmutation.yml)

La proyección ahora incluye:

- `knowledge_contract.allowed_urns`
- `knowledge_contract.routes`
- `knowledge_contract.resolved_paths`
- `knowledge_contract.unresolved_urns`

Y en el bundle Claude aparece visible:

- `## Knowledge Contract`
- cada URN permitido
- cada `kb_route`
- el path local correspondiente del artefacto

## Señales y artefactos operativos

### Telemetría viva

- [docs/generated/invocations.jsonl](/Users/felixsanhueza/Developer/kora/docs/generated/invocations.jsonl)
- [docs/generated/retrieval.jsonl](/Users/felixsanhueza/Developer/kora/docs/generated/retrieval.jsonl)
- [docs/generated/lead-time.jsonl](/Users/felixsanhueza/Developer/kora/docs/generated/lead-time.jsonl)

### Freshness

- [dolor-toracico.md](/Users/felixsanhueza/Developer/kora/artifacts/knowledge/salud/med-emergencia/dolor-toracico.md) ya tiene `extensions.kora.verified_at`

## Supuestos vigentes

1. `deploy-status` considera **error solo por `stale`**, no por `missing`.
2. El primer runtime realmente endurecido es `claude-code`; `openclaw` sigue ausente localmente.
3. El `knowledge_contract` ya se proyecta de forma explícita, pero la visualización runtime-visible solo está trabajada en el bundle Claude actual.
4. El KB `me-dolor-toracico` sigue shardeado en 2 partes y ese shape ya volvió a quedar consistente (`shard_count = 2`).

## Riesgos abiertos

1. **Ruido en telemetría**:
   `invocations.jsonl`, `retrieval.jsonl` y `lead-time.jsonl` acumulan corridas históricas repetidas; no hay deduplicación por canario.

2. **Cobertura runtime desigual**:
   Claude tiene knowledge contract visible; otros runtimes todavía no necesariamente exponen la misma claridad runtime-facing.

3. **Deploy incompleto del fleet**:
   `deploy-status` hoy muestra 7 agentes `missing` en Claude. No es falla roja, pero sí backlog operacional real.

4. **verified_at por artefacto puntual**:
   el stamping actual actualiza el path explicitado; no propaga automáticamente a todos los shards o nodos relacionados salvo que se los pase explícitamente.

## Pendientes concretos

### Pendiente 1 — Fase 3

Abrir Fase 3. Dos opciones racionales:

1. **P3.2 mismo componente, segundo runtime**
   - Recomendación: `salud/urgenciologo` en `codex`
   - Objetivo: validar que el `knowledge_contract` explícito también pague renta fuera de Claude

2. **P3.1 segundo componente sobre el mismo KB**
   - Promover otro consumidor clínico o curatorial que cite el mismo subcorpus `med-emergencia`

### Pendiente 2 — Telemetría

- decidir si `missing` en `deploy-status` debe mantenerse como warning operativo o endurecerse a failure
- si se quiere reporting limpio, agregar deduplicación o cohort tags a JSONL

## Handoff operativo

Si otra sesión retoma desde acá:

1. leer primero este handoff
2. leer la memoria operativa compañera
3. verificar:

```bash
python3 toolchain/kora check --strict
python3 -m unittest discover -s tests
python3 toolchain/kora deploy-status
```

Contrato esperado:

- 18/18 checks verdes
- 320 tests OK (`skipped=2`)
- `salud/urgenciologo` = `ok` en Claude

Si cualquiera falla, diagnosticar drift antes de continuar.
