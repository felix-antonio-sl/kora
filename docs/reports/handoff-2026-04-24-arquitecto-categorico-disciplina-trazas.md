---
_manifest:
  urn: "urn:kora:kb:handoff-2026-04-24-arquitecto-categorico-disciplina-trazas"
  provenance:
    created_by: "Codex GPT-5"
    created_at: "2026-04-24"
    source: "Cierre de remediacion categorial para arquitecto-categorico y disciplina de trazas formales."
version: "1.0.0"
status: publicado
tags: [handoff, arquitecto-categorico, formal-layer, trazas, toolchain]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:kora:kb:operational-memory-2026-04-24-arquitecto-categorico-disciplina-trazas"
    - "urn:kora:kb:next-session-prompt-2026-04-24-arquitecto-categorico-disciplina-trazas"
    - "urn:kora:kb:cat-fxsl-bridge"
    - "urn:kora:kb:cat-audit-invariants"
---

# Handoff explicito - arquitecto-categorico y disciplina de trazas

## Estado actual

La remediacion solicitada quedo aplicada en `master` para elevar el cumplimiento
categorial de `artifacts/skills/_TALLER/REVIEW/arquitecto-categorico`.

La sesion previa tambien dejo una limpieza estructural ya commiteada y empujada:

- `c8de240 chore(artifacts): reubica staging por capa y namespace`
- `38ce1e9 chore(artifacts): elimina duplicados seguros de inbox`
- `1cd6c13 chore(agents): elimina skills legacy duplicadas`

Con eso se removieron duplicados exactos de INBOX, skills legacy byte-a-byte
duplicadas y ubicaciones de staging fuera de namespace/capa.

El cambio principal fue cerrar la ambiguedad entre fuente formal normativa y
corpus auxiliar:

- `Traces to:` queda reservado para la Formal Layer oficial KORA:
  `artifacts/knowledge/kora/categorical-foundations/`.
- ICAS/FXSL queda permitido como `Rationale:` o soporte editorial, no como traza
  normativa oficial.
- El skill declara el corpus permitido completo: 7 URNs `urn:kora:kb:cat-*` y
  24 URNs `urn:fxsl:kb:icas-*`.
- La toolchain ahora ejecuta el check `formal-trace-discipline` dentro de
  `check --strict`.

## Decisiones tomadas

1. No adoptar la taxonomia atomos/moleculas/compuestos como criterio estructural
   para este cierre. La peticion vigente fue fortalecer principios categoriales.
2. Mantener ICAS/FXSL como corpus auxiliar valioso, pero sin darle autoridad
   formal directa por medio de `Traces to:`.
3. Codificar la regla en la toolchain para evitar que dependa solo de disciplina
   humana.
4. Actualizar referencias stale del skill en vez de promover el skill, porque el
   pedido fue remediacion de cumplimiento, no publicacion.

## Artefactos modificados

- `artifacts/skills/_TALLER/REVIEW/arquitecto-categorico/SKILL.md`
- `artifacts/skills/_TALLER/REVIEW/arquitecto-categorico/referencias/icas-bok-indice.md`
- `artifacts/skills/_TALLER/REVIEW/arquitecto-categorico/referencias/skill-arquitecto-categorico-spec.md`
- `artifacts/skills/_TALLER/REVIEW/arquitecto-categorico/referencias/skill-arquitecto-categorico-structure.md`
- `artifacts/knowledge/kora/categorical-foundations/03-ecosystem-2cat.md`
- `artifacts/knowledge/kora/categorical-foundations/08-fxsl-cat-bridge.md`
- `toolchain/kora_lib/checks.py`
- `tests/test_artifacts.py`
- `tests/test_check_pipeline.py`

## Verificacion ejecutada

```bash
python3 toolchain/kora check --strict
python3 toolchain/kora validate --profile strict
python3 -m unittest discover -s tests
python3 toolchain/kora kb-graph --json --orphans
```

Resultados observados:

- `check --strict`: 20/20 checks verdes.
- `validate --profile strict`: 17 workspaces validos, 0 invalidos.
- `unittest discover`: suite completa verde, 2 skipped.
- `kb-graph`: 531 nodos, 676 edges, 0 broken edges, 0 ciclos `depends`, 3
  huerfanos reales.

## Pendientes

1. Si se desea llevar `arquitecto-categorico` a productivo, ejecutar el flujo de
  promocion normal desde `_TALLER/REVIEW/`.
2. Revisar si otros documentos fuera del alcance del check deben adoptar
  explicitamente la misma convencion editorial.
3. Decidir si `formal-trace-discipline` debe ampliarse a `docs/reports/` cuando
  esos reportes quieran operar como conocimiento normativo y no solo memoria
  operativa.
4. Limpieza fuera de artefactos:
   - remover `.pyc` trackeados bajo `toolchain/__pycache__` y
     `toolchain/legacy_migration/__pycache__`
   - evaluar `toolchain/file_movement_map.json`
   - mover o absorber `HANDOFF-2026-04-23.md` desde la raiz a `docs/reports/`
5. Limpieza media en artefactos:
   - ajustar provenance de agentes productivos ya migrados
   - luego evaluar borrar workspaces legacy completos en `_FRAGUA/INBOX`

## Supuestos

- La Formal Layer oficial sigue siendo exclusivamente
  `artifacts/knowledge/kora/categorical-foundations/`.
- `artifacts/knowledge/fxsl/cat/` conserva estatus auxiliar.
- El estado correcto para el skill en esta entrega es REVIEW, no publicacion.
- `docs/generated/` sigue siendo derivado, regenerable e ignorado por git.

## Riesgos

- El nuevo check puede revelar deuda futura si algun artefacto productivo usa
  `Traces to:` hacia URNs auxiliares o externas.
- La disciplina actual no inspecciona `docs/reports/`, por diseno conservador
  para no convertir memorias operativas en normativa.
- La promocion posterior del skill podria requerir validaciones adicionales no
  cubiertas por esta remediacion.
- Borrar workspaces legacy completos sin ajustar provenance dejaria rutas
  historicas no resolubles en agentes productivos.
- El corpus OPM tiene drafts y productivos con URNs duplicadas pero contenido
  distinto; requiere promocion/deprecacion, no limpieza mecanica.

## Handoff operativo

Para continuar:

1. leer este handoff y la memoria operativa compañera;
2. verificar `git status --short --branch`;
3. correr `python3 toolchain/kora check --strict`;
4. si se busca publicacion, inspeccionar primero el contrato de promocion para
   skills en `_TALLER/REVIEW/`.
