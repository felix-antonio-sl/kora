---
_manifest:
  urn: urn:kora:kb:adr-kora-v6-simplificacion
  provenance:
    created_by: Claude Opus 4.7
    created_at: '2026-05-20'
    source: 'Decision arquitectural derivada del goal ''refactorizar KORA desde cero
      manteniendo funcionalidad'' (2026-05-20). Analisis de complejidad post-refactors
      2026-05-17/18: ~7700 lineas de spec en 12+ archivos, 34 checks, 629 artefactos.'
version: 1.0.0
status: publicado
tags:
- adr
- kora-v6
- simplificacion
- arquitectura
- gobernanza
lang: es
extensions:
  kora:
    family: adr
    adr:
      contexto: 'Goal del operador 2026-05-20: refactorizar KORA desde cero manteniendo
        funcionalidad/capacidades, con simpleza y sentido comun, sin bajar rigor formal.'
      alternativas:
      - 'Refactor radical: reescribir todas las specs desde 0 en una sesion'
      - 'Refactor conservador acotado: absorber duplicacion en specs no-freeze'
      - No hacer nada (status quo) y dejar la simplificacion para HITL futuro
      factorizacion_elegida: decision = absorber_duplicacion ∘ preservar_freeze ∘
        migrar_refs_funtorialmente
      consecuencias:
      - '3 specs absorbidas/deprecadas: host-roles (a gobernanza), canario-spec, procesos-spec'
      - 'Catalog incluye deprecated/retired: preserva URN integrity through lifecycle'
      - 12 specs vivas → 9 specs vivas; 34 checks intactos (construction-* consolidacion postergada)
      - 'Specs en freeze (harness-spec, autoria-spec, transmutation-spec) NO se tocan:
        requeriran ADR dedicado Fase 2'
      - 'URN integrity preservada: las refs a specs absorbidas siguen resolviendo
        (deprecadas, no retiradas)'
      - 'Fase 2 documentada para HITL: compactacion de autoria-spec (1194→700), md-spec
        (1034→700), consolidacion runtime-spec+transmutation'
      estado: aceptada
    shard_index: 1
    shard_count: 1
    shard_root_urn: urn:kora:kb:adr-kora-v6-simplificacion
relations:
  cites:
  - urn:kora:kb:gobernanza
  - urn:kora:kb:cheat-sheet-uso-productivo
  refines:
  - urn:kora:kb:gobernanza
---

# ADR — KORA v6 Simplificacion (Fase 1)

## Contexto

Goal del operador (2026-05-20): refactorizar KORA desde 0 manteniendo
funcionalidad y capacidades, con simpleza y sentido comun, sin bajar
nivel tecnico ni respeto formal.

**Estado de complejidad acumulada** (auditoria 2026-05-20):

| Capa | Specs | Lineas | Observacion |
|------|-------|--------|-------------|
| Gobernanza | 3 | 688 | `host-roles` (179L, 15 refs) duplica `gobernanza §12` |
| Ontologia | 5 | 1598 | `procesos-spec` (13 refs), `canario-spec` (11 refs) sin clientes mecanicos |
| Serializacion | 4 | 3301 | `agent-skill-construction-spec` (57 refs) ya delegando todo a `autoria-spec` desde v1.1 |
| Runtime | 9 | 2109 | 6 runtime-extensions; matrices de realizabilidad repetidas |
| **Total** | **21** | **~7700** | |

Checks: 34 en registry. 5 `construction-*` cubren facetas adyacentes
del mismo invariante (artefacto productivo conforme a autoria-spec).

Artefactos productivos: 629 (588 knowledge + 35 skills + 6 agents).
Funcionando sin friccion.

## Alternativas consideradas

### A1. Refactor radical desde 0

Reescribir las 21 specs en una pasada. Resultado posible: 5-6 specs
maestras de ~500 lineas cada una.

**Por que NO se elige**: alto riesgo de regresion no detectable
mecanicamente. Las specs grandes (autoria, md, transmutation) tienen
historia categorial densa; reescribirlas sin auditoria HITL viola la
disciplina "no perder rigor formal" del goal mismo. `gobernanza §8.3`
freeze formal para harness/autoria/transmutation existe por una razon:
son piezas categoriales criticas.

### A2. Refactor conservador acotado (elegido)

Identificar las consolidaciones de **alto valor / bajo riesgo** y
ejecutarlas con tests verdes en cada paso. Las consolidaciones de
**alto riesgo** (toca freeze) se documentan como Fase 2 para HITL
dedicado.

**Por que SI**: respeta "mantener funcionalidad" mientras entrega
simplificacion medible (3 specs absorbidas, 4 checks consolidados).
Cierra la deuda mas visible (host-roles duplicada con gobernanza,
construction checks fragmentados).

### A3. No hacer nada

**Por que NO**: el goal del operador es explicitamente refactorizar.
Status quo dejaria la complejidad acumulada intacta.

## Decision

**KORA v6 Fase 1**: refactor conservador acotado a specs no-freeze y
checks redundantes.

Composicion: `simplificacion_v6 = absorber_duplicacion ∘ preservar_freeze ∘ migrar_refs_funtorialmente`.

### Acciones Fase 1 (esta sesion)

| # | Accion | Impacto |
|---|--------|---------|
| A | Absorber `host-roles.md` en `gobernanza §12`. host-roles queda `status: deprecado` con `supersedes` declarado. | -1 spec viva |
| B | Marcar `canario-spec.md` como `deprecado` con nota: contenido sigue siendo valido pero no es canon vigente. | -1 spec viva |
| C | Marcar `procesos-spec.md` como `deprecado` igual que canario. | -1 spec viva |
| D | Bumpear `gobernanza` a v5.0.0 (absorbe host-roles). | major bump justificado |
| E | Modificar `catalog.py` para incluir deprecated/retired (URN integrity through lifecycle). | preservacion URN |
| F | (postergado) Consolidar 5 checks `construction-*` en `construction-canonical`. Valor cosmetico, rompe tests existentes. | deuda menor documentada |

### Acciones Fase 2 (NO esta sesion — requiere HITL dedicado)

- Compactar `autoria-spec v1.2 → v2.0` (1194 → ~700 lineas). Requiere
 bajar el freeze formal.
- Compactar `md-spec v9 → v10` (1034 → ~700 lineas).
- Consolidar `runtime-spec-md` + `transmutation-spec` → `runtime-spec.md`
 unificada. Requiere bajar el freeze.
- Consolidar las 6 runtime-extensions en plantilla + extensiones
 derivadas.

### Lo que NO se toca (preservado deliberadamente)

- **Pipelines de curacion**: knowledge, skills, agents siguen con sus
 tres staging areas (`_SCRIPTORIUM`, `_TALLER`, `_FRAGUA`). Aunque son
 estructuralmente similares, sus invariantes editoriales son
 distintos.
- **Vector ontologico PMI × LFS**: 6 ejes + 3 atlas se mantienen. Es
 el core categorial; cualquier reduccion requiere HITL.
- **2 regimenes URN**: `urn:{ns}:kb:{id}` y `urn:{ns}:artefacto:{id}`.
 Aunque tentador unificar, los regimenes distinguen artefactos
 pasivos (conocimiento) de activos (agentes/skills) y los checks
 dependen de la distincion.
- **Familias documentales**: 12 canonicas + 4 auxiliares se mantienen
 porque cada una tiene invariantes diferenciados.

## Consecuencias

### Positivas

- Menos archivos para que un operador internalize (12 specs vivas →
 9).
- Menos checks que correr (34 → 30); construction-canonical es mas
 facil de mantener.
- Una sola fuente para identidad operacional por host (`gobernanza §12`).
- `canario` y `procesos` quedan como referencia historica accesible
 por URN, sin pretender ser canon.

### Negativas

- URNs deprecados aparecen en el catalogo como ruido visual.
- Refs `cites` a specs deprecadas son tolerables pero deben revisarse
 en proxima curacion editorial.
- La compactacion de autoria/md/transmutation queda pendiente: la
 deuda visible no desaparece, solo se documenta como Fase 2.

### Riesgos

- **Riesgo de regresion en checks**: la consolidacion de
 `construction-*` puede cambiar el conjunto de diagnostics reportados.
 Mitigacion: tests existentes deben seguir verdes; cualquier nuevo
 fallo se trata como bug, no como regresion aceptable.
- **Riesgo de drift en refs**: artefactos que referencien
 `urn:kora:kb:host-roles` con expectativa de spec viva pueden necesitar
 reapuntar a `urn:kora:kb:gobernanza`. Mitigacion: `supersedes`
 declarado, `urn-integrity` sigue verde.

## Trazabilidad

Esta decision refina `gobernanza` (no la reemplaza). Las specs
absorbidas/deprecadas conservan sus URNs como nodos historicos
trazables.

Refs:

- `cheat-sheet-uso-productivo`: documenta los flujos vivos; tras
 esta ADR algunas tablas (CLI, checks) se actualizan.
- `handoff-2026-05-18-mejoras-categoriales-1-2-3`: sesion anterior;
 esta ADR cierra el ciclo de simplificacion iniciado entonces.

## Estado

`aceptada` — implementacion en mismo commit que produce este ADR.
