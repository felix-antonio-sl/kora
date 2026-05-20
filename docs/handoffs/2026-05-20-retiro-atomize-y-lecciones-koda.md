---
_manifest:
  urn: "urn:kora:kb:handoff-2026-05-20-retiro-atomize-y-lecciones-koda"
  provenance:
    created_by: "Claude Opus 4.7"
    created_at: "2026-05-20"
    source: "Directiva HITL del operador 2026-05-20: sacar todo lo de atomize de knowledge; volver a la filosofia antigua KODA (/home/felix/_TEMP_BORRAR/koda) como referencia (no replicacion)."
version: "1.0.0"
status: publicado
tags: [handoff, retiro-atomize, lecciones-koda, simplificacion, knowledge, kora-v8]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:kora:kb:adr-retiro-atomize-y-lecciones-koda"
    - "urn:kora:kb:md-spec"
    - "urn:kora:kb:knowledge-spec"
---

# Handoff 2026-05-20 — Retiro de atomize + lecciones KODA antigua

## Resumen ejecutivo

Esta sesion implementa la directiva HITL del operador (2026-05-20):
sacar todo lo de atomize del dominio knowledge, usando la filosofia
antigua KODA como referencia (no replicacion) para simplificar y
fortalecer KORA.

Decision arquitectural en `urn:kora:kb:adr-retiro-atomize-y-lecciones-koda`.

## Volumen del retiro

| Componente | Antes | Despues |
|------------|-------|---------|
| Skill productivo `atomize` | `artifacts/skills/kora/atomize/` (25 archivos) | `governance/decisiones-archivadas/skills-retiradas/atomize/` (status retirado) |
| Artefactos `atomic-*` en REVIEW | 225 archivos en 4 namespaces (kora, pro, fxsl, hi) | `artifacts/knowledge/_SCRIPTORIUM/INBOX/_atomic-retirado-2026-05-20/` (material crudo) |
| Familia `atomic` en `md-spec §5.6` | tabla + §5.6.1 enum cerrado (11 tipos) + 9 reglas | eliminada |
| §6.5 r4-7 (segmentacion atomic blanda 15K / dura 200) | 4 reglas | eliminadas |
| §6.10 check atomic (Pxxx, tipos enum, fuentes) | 1 item | eliminado |
| §6.11 r9 (dedup atomic justification) | 1 regla | eliminada |
| §7.6 "Integridad familia atomic" | seccion | eliminada (§7.7 → §7.6) |
| §9 tabla de validacion: filas atomic | 6 filas | eliminadas |
| Productor canonico `atomize` en `knowledge-spec §9` | registro completo con reglas | seccion vacia + nota de retiro |
| CLI `kora atomize` | subcommand activo | retirado |
| `toolchain/kora_lib/atomize.py` | modulo productivo | movido a `toolchain/legacy_migration/atomize.py` |
| `tests/test_atomize.py` | suite dedicada | eliminada |
| `tests/test_artifacts.py` tests atomic | 3 tests | reemplazados por 3 tests de retiro |

### Versiones bumpeadas

- `md-spec v9.0.0 → v10.0.0` (major, removal de familia + §5.6.1
  renumerada).
- `knowledge-spec v2.0.0 → v3.0.0` (major, removal de productor
  canonico).

## Lo que se preserva

- **Termino "Proposicion atomica"** en `md-spec §2` (definiciones) como
  termino del lexico KORA, no como invariante de familia.
- **"Hechos atomicos"** como adjetivo en §2 (Meat) y §6.11 — el lexico
  sigue valido.
- **URN `urn:kora:artefacto:atomize`** sigue resolviendo (skill
  archivado, no retirado del catalogo).
- **Modulo `atomize.py`** preservado en `toolchain/legacy_migration/`
  como dead code referenciable si en el futuro se reactiva.
- **Constantes `ATOMIC_*`** en `validation.py` se mantienen como dead
  code (no hay artefactos atomic, pero las constantes no rompen nada).

## Lecciones KODA antigua aplicables a KORA (referencia, no replicacion)

Las 5 guides en `/home/felix/_TEMP_BORRAR/koda/guide_core_*.yml`
documentan una filosofia mas simple y concentrada. **No se replican**;
se anotan como **direccion futura** posible:

### L1. Vocabulario controlado Tier 1 / Tier 2

KODA usaba 19 keywords core (`Def`, `Req`, `Act`, `Cond`, `Ref`, `XRef`,
`Ctx`, `Purp`, `Mssn`, `Obj`, `Proc`, `Src`, `Prohib`, `Ex`, `Just`,
`Rec`, `Warn`, etc.) con semantica fija + vocabulario abierto
auto-explicativo. Si compactamos specs en Fase 2b, podriamos introducir
un perfil prescriptivo mas denso usando estos keywords como marcas
semanticas.

### L2. Cross-references estrictas (Ref interno vs XRef externo)

KODA distinguia explicitamente. KORA mezcla refs en `relations` con
citas en body. Aplicacion futura: distincion explicita.

### L3. Compactacion sin atomizacion

KODA producia documentos densos sin descomponer en proposiciones
individuales. La fidelidad FS=100% se alcanzaba por **telegrafizacion +
deduplicacion via Ref interno**, no por extraccion de items con IDs
Pxxx. KORA queda con `md-spec §6` (koraficacion) que ya captura este
metodo. La familia atomic era una **especializacion costosa** que el
operador declara innecesaria.

### L4. Anti-patterns explicitos en cada spec

KODA enumeraba `Wrong:` / `Right:` / `Why_Wrong:`. `md-spec §5.4.2` ya
tiene 7 contraejemplos. Cada spec KORA podria cerrar con mini-seccion
de anti-patterns.

### L5. Categorial foundations sin sobre-formalizacion

KODA usaba "functor, monad, morphism" solo cuando aportaban claridad.
KORA tiene muchos artefactos con notacion categorial. La leccion: la
formalizacion sirve si materializa enforcement; cuando es decorativa,
daña.

### L6. Knowledge cartography explicita

KODA tenia `CM-KB-GUIDANCE` (mapeo query→artefacto). KORA tiene
`kora kb-graph`. La leccion: el grafo debe ser navegable, no solo
auditable.

### L7. Token economy LLM-first

KODA principle: eliminate explanatory verbosity, CR>1.0. KORA tiene
FS=100% y CR>1.5. La leccion: en Fase 2b (compactacion de
autoria-spec, md-spec, transmutation-spec) este principio debe guiar
las decisiones de poda.

## Validacion ejecutada

| Comando | Resultado |
|---------|-----------|
| `python3 toolchain/kora index` | 641 artefactos indexados (post: 225 atomic eliminados de catalogo activo + 1 skill archivado + 2 ADRs nuevos) |
| `python3 toolchain/kora check --strict` | 28/29 verdes; 1 HIGH preexistente en `HANDOFF.md` del WIP del operador |
| `python3 -m unittest discover -s tests` | resultado en commit |

## Estado consolidado

### Que cerramos

- Atomize retirado del dominio knowledge en una operacion coordinada:
  skill archivado, 225 artefactos movidos a INBOX, familia atomic
  eliminada de md-spec, productor canonico eliminado de
  knowledge-spec, CLI limpio, tests actualizados.
- ADR producido (familia adr) documentando decision + alternativas +
  consecuencias.
- Lecciones KODA antigua anotadas como direccion futura, no
  implementadas.

### Que queda como deuda

1. **Constantes `ATOMIC_*`** en `validation.py` quedan como dead code.
   Pueden retirarse en mantenimiento futuro sin urgencia.
2. **`legacy_migration/atomize.py`** queda como referencia historica.
   Si el operador confirma retiro definitivo, puede eliminarse
   physicamente en commit posterior.
3. **Familias auxiliares `bok`, `source`, `source-alias`, `generic`**
   en md-spec §5.6 siguen documentadas; siguen vivas (el toolchain las
   usa).
4. **Aplicar lecciones KODA en Fase 2b**: cuando se compacte
   autoria-spec / md-spec / transmutation-spec, considerar L1-L7 como
   guias.

### Que NO debe asumirse

- No asumir que el skill atomize esta disponible: esta en archive
  con `status: retirado`. URN resuelve pero el corpus productivo no lo
  expone.
- No asumir que la familia atomic puede regresar facilmente: requiere
  HITL + ADR + reescribir tabla §5.6 + reactivar productor.
- No asumir que los 225 artefactos en INBOX seran procesados
  automaticamente: vuelven a ser material crudo sin URN canonico. Si
  el operador quisiera koraficarlos, debe usar el metodo de md-spec §6
  (sin descomponer en proposiciones).

## Artefactos dejados versionados

### Specs
- `serialization/md-spec.md` v10.0.0 (familia atomic eliminada).
- `serialization/knowledge-spec.md` v3.0.0 (productor canonico vaciado).

### Toolchain
- `toolchain/kora_lib/cli.py` (subcommand atomize retirado).
- `toolchain/legacy_migration/atomize.py` (renamed desde
  `toolchain/kora_lib/`).

### Tests
- `tests/test_atomize.py` eliminado.
- `tests/test_artifacts.py` actualizado (3 tests atomic eliminados, 3
  tests de retiro agregados).

### Knowledge
- `artifacts/knowledge/kora/adr/adr-retiro-atomize-y-lecciones-koda.md`
  (familia adr).

### Archive
- `governance/decisiones-archivadas/skills-retiradas/atomize/` (skill
  completo con status: retirado).
- `artifacts/knowledge/_SCRIPTORIUM/INBOX/_atomic-retirado-2026-05-20/`
  (225 artefactos atomic ahora crudos).

### Docs
- `docs/handoffs/2026-05-20-retiro-atomize-y-lecciones-koda.md` (este).

## Prompt de continuacion

```text
Retoma KORA en /home/felix/kora desde el estado consolidado en
`docs/handoffs/2026-05-20-retiro-atomize-y-lecciones-koda.md`.

Contexto vigente:

- Familia `atomic` retirada del corpus normativo. md-spec v10.0,
  knowledge-spec v3.0.
- Skill `atomize` archivado en governance/decisiones-archivadas/
  skills-retiradas/. URN urn:kora:artefacto:atomize sigue resolviendo.
- 225 artefactos atomic-* movidos a _SCRIPTORIUM/INBOX/
  _atomic-retirado-2026-05-20/ como material crudo (sin URN canonico).
- toolchain/legacy_migration/atomize.py preserva el modulo historico.
- Subcommand `kora atomize` retirado del CLI.
- ADR: urn:kora:kb:adr-retiro-atomize-y-lecciones-koda.

Para Fase 2b (compactacion autoria-spec, md-spec, transmutation-spec):
considerar las 7 lecciones KODA antigua documentadas en el ADR como
guias de poda — especialmente L7 (token economy LLM-first) y L4
(anti-patterns explicitos).

Mantener disciplina de no reintroducir atomize sin HITL + ADR
dedicado.
```
