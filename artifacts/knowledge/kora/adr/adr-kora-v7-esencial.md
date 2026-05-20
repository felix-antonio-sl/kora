---
_manifest:
  urn: urn:kora:kb:adr-kora-v7-esencial
  provenance:
    created_by: Claude Opus 4.7
    created_at: '2026-05-20'
    source: 'Directiva HITL del operador 2026-05-20: KORA es un sistema que gestiona
      con specs estrictas la generacion, mantenimiento, catalogo y ciclo de vida de
      artefactos de conocimiento, agentes y skills, en formato agnostico, transmutables
      a claude-code, codex, openclaw y hermes. Maxima simpleza, manteniendo rigor
      y potencia.'
version: 1.0.0
status: publicado
tags:
- adr
- kora-v7
- esencial
- vision-arquitectonica
- hermes
- runtimes
- freeze
lang: es
extensions:
  kora:
    family: adr
    adr:
      contexto: 'Directiva HITL del operador 2026-05-20: convergir KORA a su lectura
        minima — sistema que gestiona ciclo de vida (generacion, mantenimiento, catalogo)
        de 3 tipos de artefacto (conocimiento, agentes, skills) en IR agnostico, transmutables
        a 4 runtimes (claude-code, codex, openclaw, hermes). Implica: activar hermes
        (bloqueado por gobernanza §8.2), bajar freeze formal de §8.3 para autoria-spec/transmutation-spec,
        mantener archivados los 4 runtimes no-canonicos (gemini, mastra, opencode,
        agentskills).'
      alternativas:
      - 'Status quo: 3 runtimes activos + 4 pausados + hermes bloqueado'
      - 'Aceptar todos los runtimes vigentes (claude-code, codex, openclaw, gemini,
        mastra, opencode, agentskills, hermes): mantener fragmentacion'
      - 'Lectura minima HITL: 4 runtimes canonicos (claude-code, codex, openclaw,
        hermes); resto archivado'
      factorizacion_elegida: decision = activar_hermes ∘ archivar_no_canonicos ∘ bajar_freeze_serializacion_runtime
        ∘ preservar_freeze_harness
      consecuencias:
      - Hermes pasa de bloqueado (gobernanza §8.2) a runtime canonico con stub hermes-runtime-extension.md
      - 'gemini, mastra, opencode, agentskills permanecen archivados en governance/decisiones-archivadas/specs-en-pausa/
        con status: retirado'
      - 'entornos_objetivo: solo {claude-code, codex, openclaw, hermes}; drift en
        5 skills productivos se limpia'
      - Freeze formal §8.3 se baja para autoria-spec y transmutation-spec; harness-spec
        permanece en freeze como core categorial
      - 'transmute.py: PRESERVATION_MATRIX, TARGET_ADAPTERS, SUPPORTED_TARGETS reducidos
        a 4; PAUSED_TARGETS eliminados del runtime activo'
      - Compactacion de autoria-spec y transmutation-spec queda autorizada como Fase
        2b en sesion dedicada (no esta sesion)
      estado: aceptada
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:kora:kb:adr-kora-v7-esencial
relations:
  cites:
  - urn:kora:kb:gobernanza
  - urn:kora:kb:adr-kora-v6-simplificacion
  - urn:kora:kb:cheat-sheet-uso-productivo
  refines:
  - urn:kora:kb:adr-kora-v6-simplificacion
---

# ADR — KORA Esencial v7

## Contexto

Directiva HITL del operador (2026-05-20):

> "lo que necesitamos en el fondo es un sistema que gestione con specs
> estrictas la generacion, mantenimiento, catalogo y todo el ciclo de
> vida de artefactos de conocimiento, agentes y skills (en formato
> agnostico y generico) que se transmuten a las diferentes plataformas:
> claude code, codex, openclaw, hermes. Maxima simpleza, manteniendo
> rigor y potencia."

Esta declaracion captura la **lectura minima** del proposito de KORA.
Tres cambios doctrinales sobre el estado vigente al 2026-05-20:

1. **Hermes vuelve al canon**: gobernanza §8.2 vigente al 2026-05-20
 declara `Hermes NO es runtime target vigente`. La directiva HITL
 levanta ese bloqueo.
2. **Lista de runtimes canonicos reducida a 4**: `claude-code`,
 `codex`, `openclaw`, `hermes`. Los otros (`gemini`, `mastra`,
 `opencode`, `agentskills`) ya estan archivados en
 `governance/decisiones-archivadas/specs-en-pausa/` desde la poda
 2026-05-07; ahora se confirma su archivo como **definitivo** salvo
 nuevo HITL.
3. **Freeze formal §8.3 parcialmente bajado**: `autoria-spec` y
 `transmutation-spec` quedan editables (compactacion Fase 2b).
 `harness-spec` permanece en freeze porque su ontologia PMI × LFS es
 el core categorial; cualquier cambio requiere HITL dedicado por
 separado.

## Alternativas consideradas

### A1. Status quo (no hacer nada)

Mantener gobernanza §8.2 (hermes bloqueado), §8.3 (3 specs en freeze),
runtimes activos = 3 (claude-code, codex, openclaw).

**Por que NO**: contradice la directiva HITL explicita. El operador
acaba de declarar que hermes es runtime canonico.

### A2. Aceptar todos los runtimes vigentes

Mantener los 7 runtimes (3 activos + 4 pausados) + agregar hermes = 8.

**Por que NO**: directamente contradice la consigna "maxima simpleza".
La directiva nombra solo 4. El silencio sobre los otros es deliberado.

### A3. Lectura minima HITL (elegida)

4 runtimes canonicos = {claude-code, codex, openclaw, hermes}. Los otros
4 (gemini, mastra, opencode, agentskills) permanecen archivados con
`status: retirado` salvo nuevo HITL futuro.

**Por que SI**:
- Refleja exactamente la directiva del operador.
- Reduce superficie operativa (4 vs 8 runtimes a mantener).
- Preserva trazabilidad: los archivados conservan URN como nodos
 historicos.
- Permite que la compactacion de specs avance.

## Decision

KORA v7 **esencial**: el sistema converge a su lectura minima.

### Acciones inmediatas (esta sesion — Fase 2a)

| # | Accion | Artefacto |
|---|--------|-----------|
| A | Levantar bloqueo hermes | `gobernanza §8.2` → "Hermes es runtime canonico desde 2026-05-20" |
| B | Bajar freeze parcial | `gobernanza §8.3` → solo `harness-spec` queda en freeze; `autoria-spec` y `transmutation-spec` quedan editables |
| C | Crear stub hermes-runtime-extension | `runtime/hermes-runtime-extension.md` v0.1.0 con matriz de realizabilidad inicial + deuda explicita |
| D | Adaptar `transmute.py` | PRESERVATION_MATRIX + TARGET_ADAPTERS + SUPPORTED_TARGETS reducidos a 4 + hermes agregado; PAUSED_TARGETS desactivado |
| E | Limpiar `entornos_objetivo` en productivos | 5 skills (ship-discipline, gtd-flow, cell-design, ux-design, mente-omega) con drift gemini/mastra |
| F | Limpiar refs a runtime-extensions archivadas en `custodio-kora` | reapuntar a las 4 canonicas + hermes |
| G | Actualizar cheat-sheet | reflejar runtimes vigentes |
| H | gobernanza v5.0.0 → v6.0.0 | major bump justificado por cambio de freeze + activacion runtime |

### Acciones Fase 2b (NO esta sesion — requiere su propia)

- Compactar `autoria-spec v1.2 → v2.0` (1194 → ~700 lineas).
- Compactar `transmutation-spec` y consolidar con `runtime-spec-md`.
- Compactar `md-spec v9 → v10` (1034 → ~700 lineas).
- Producir contenido normativo completo de `hermes-runtime-extension`
 (matriz de realizabilidad final, fidelity claims, dominio de
 proyeccion validado, ejemplos).

### Lo que NO se toca (preservado)

- **`harness-spec`**: queda en freeze. Es el core ontologico PMI × LFS;
 cualquier cambio requiere HITL dedicado.
- **Tres tipos de artefacto**: conocimiento, agentes, skills. Se
 mantienen tal cual; la directiva los nombra explicitamente.
- **Pipelines de curacion**: `_SCRIPTORIUM`, `_TALLER`, `_FRAGUA`
 intactos.
- **Vector ontologico**: 6 ejes + 3 atlas. No se reduce.
- **Familias documentales**: 12 canonicas + 4 auxiliares.
- **Adjuncion Check ⊣ Fix**, leyes algebraicas de relations, coalgebra
 conformance: todo lo categorial vigente se preserva.

## Consecuencias

### Positivas

- **Convergencia con el proposito declarado**: KORA refleja
 exactamente lo que el operador necesita.
- **Hermes activado**: cuarto runtime canonico habilitado para
 transmutacion futura.
- **Drift limpiado**: 5 skills productivos que listaban runtimes
 archivados se actualizan.
- **Compactacion habilitada**: autoria-spec y transmutation-spec
 pueden compactarse en Fase 2b.

### Negativas

- **`hermes-runtime-extension.md` queda como stub**: el contenido
 normativo completo requiere otra sesion.
- **6 artefactos productivos** se modifican para limpiar drift;
 cualquier transmutacion previa apuntaba a runtimes que ya no son
 canonicos.

### Riesgos

- **Riesgo de re-introduccion de runtimes archivados**: futuras
 ediciones podrian agregar gemini/mastra/opencode/agentskills sin
 pasar por HITL. Mitigacion: schema/lint que rechaze esos slugs en
 `entornos_objetivo`.
- **Riesgo de transmutacion a hermes sin spec completa**: el stub no
 tiene matriz de realizabilidad madura. Mitigacion: marcar el target
 como `incompleto` en `PRESERVATION_MATRIX` hasta cerrar Fase 2b.

## Trazabilidad

Esta ADR refina y supersede aspectos de `urn:kora:kb:adr-kora-v6-simplificacion`:

- v6 mantuvo el freeze §8.3 vigente; v7 lo baja parcialmente.
- v6 documento la Fase 2 como "pendiente de HITL"; v7 cierra esa
 pendiente para autoria/transmutation.
- v6 mantuvo el bloqueo de hermes; v7 lo levanta.

## Estado

`aceptada` — implementacion en mismo commit que produce este ADR.
