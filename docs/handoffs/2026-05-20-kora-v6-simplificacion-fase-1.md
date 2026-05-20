---
_manifest:
  urn: "urn:kora:kb:handoff-2026-05-20-kora-v6-simplificacion-fase-1"
  provenance:
    created_by: "Claude Opus 4.7"
    created_at: "2026-05-20"
    source: "Goal del operador 2026-05-20: refactorizar KORA desde 0 manteniendo funcionalidad. Fase 1 ejecutada: absorber duplicacion en specs no-freeze, deprecar specs sin clientes mecanicos, preservar trazabilidad URN."
version: "1.0.0"
status: publicado
tags: [handoff, kora-v6, simplificacion, fase-1, gobernanza, host-roles, canario, procesos, deprecacion]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:kora:kb:gobernanza"
    - "urn:kora:kb:adr-kora-v6-simplificacion"
---

# Handoff sesion 2026-05-20 — KORA v6 Simplificacion Fase 1

## Resumen ejecutivo

Esta sesion ejecuta la **Fase 1 de la simplificacion KORA v6**:
absorber duplicacion en specs no-freeze, deprecar specs sin clientes
mecanicos, preservar trazabilidad URN. El goal "refactorizar desde 0
manteniendo funcionalidad" se interpreta doctrinalmente: pensar las
specs como si las escribieramos hoy, sin la deuda historica, pero **sin
tocar artefactos productivos** ni las **specs en freeze formal**
(harness-spec, autoria-spec, transmutation-spec) en esta fase.

Decision arquitectural en
[ADR KORA v6 Simplificacion](urn:kora:kb:adr-kora-v6-simplificacion).

## Alcance

### Specs absorbidas o deprecadas

| Spec | Estado nuevo | Razon |
|------|---------------|-------|
| `host-roles.md` (179L, 15 refs) | `deprecada`; contenido absorbido en `gobernanza §12.1-§12.9` | Era extension operacional; `gobernanza §12` ya la citaba con resumen. Fusion natural. |
| `canario-spec.md` (351L, 11 refs) | `deprecada` (preservada como referencia) | Sin clientes mecanicos; ningun check la referencia |
| `procesos-spec.md` (324L, 13 refs) | `deprecada` (preservada como referencia) | Sin clientes mecanicos; ningun check la referencia |

Total: **3 specs vivas → deprecadas** (12 vivas → 9 vivas).

### Gobernanza bumpeada a v5.0.0

`governance/gobernanza.md` v4.7.0 → v5.0.0:

- **§12 expandida** absorbe el contenido normativo de `host-roles v1.1`:
  - §12.1 Definiciones (host, primary, secondary, marker, default)
  - §12.2 Host primary canonico (hetzner2897261)
  - §12.3 Reglas de push y derivados
  - §12.4 Toolchain y verificacion (hooks)
  - §12.5 Marker de host (`~/.kora/host.yml`)
  - §12.6 Enforcement
  - §12.7 Cambio de host primary
  - §12.8 Runbook de recuperacion
  - §12.9 Invariantes de §12
- **§13 nueva**: migracion v4.7 → v5.0 documentada.
- `relations.supersedes` declarado: `urn:kora:kb:host-roles`.

### Toolchain — catalogo expone deprecated

`toolchain/kora_lib/catalog.py` modificado: artefactos con
`status: deprecado` o `status: retirado` ahora se **incluyen en el
catalogo** (antes se skipean silenciosamente). Razon categorial: la
identidad URN es estable durante todo el lifecycle. Si el catalogo no
expone el URN despues de deprecar, las refs `cites` validas se rompen y
se pierde trazabilidad.

Impacto cuantitativo: catalog count 627 → 638 (+11 deprecated/retired
ahora visibles). Las refs a URNs deprecados resuelven y son validas.

### ADR producido

`urn:kora:kb:adr-kora-v6-simplificacion` (familia `adr` — primera
instancia de la familia en el corpus productivo). Documenta:

- Contexto: 7700 lineas de spec, 34 checks, 629 artefactos.
- Alternativas: refactor radical / conservador / status quo.
- Decision: conservador acotado (esta Fase 1).
- Fase 2 declarada (NO esta sesion): compactacion de autoria/md,
  consolidacion runtime+transmutation. Requiere HITL que baje el freeze.

## Lo que NO se toca (deliberadamente)

### Specs en freeze formal (`gobernanza §8.3`)

- `harness-spec.md` (399L): core categorial PMI × LFS. Bajar el freeze
  requiere HITL dedicado.
- `autoria-spec.md` (1194L): shape unificado de artefactos. Idem.
- `transmutation-spec.md` (576L): leyes functoriales de proyeccion. Idem.

### Specs vivas con clientes (preservadas)

- `md-spec.md` (1034L): formato base. Compactacion en Fase 2.
- `knowledge-spec.md` (582L): pipeline + identidad. Compactacion menor;
  ya consolidada en v2.0 (2026-05-17).
- `qa-spec.md` (343L): quality attributes Sigma. Mantiene clientes.
- `risk-register-spec.md` (181L): risk register. Mantiene clientes
  (51 refs).
- `agent-skill-construction-spec.md` (491L, v1.1): metodologia
  pre-transmutacion. Ya refactorizada en v1.1 (2026-05-18) para no
  duplicar autoria-spec. Mantenerla.
- `multiagente-spec.md` (242L): choreography. Sin friccion visible.
- `runtime-spec-md.md` (190L) + 6 runtime-extensions: consolidacion en
  Fase 2.

### Construction checks (9, no consolidados)

Los 9 checks `construction-*` (`construction-source-primary`,
`construction-vector-fit`, etc.) cubren facetas de un mismo invariante,
pero su consolidacion en `construction-canonical` se evaluo y se
**posterga**: el valor para el operador es cosmetico (el reporte unificado
del pipeline ya los agrupa) y rompe tests existentes. Documentado en el
ADR como deuda menor.

### Artefactos productivos

NO se tocaron los 629 artefactos. La Fase 1 es estrictamente doctrinal +
toolchain.

## Validacion ejecutada

| Comando | Resultado |
|---------|-----------|
| `python3 toolchain/kora index` | 638 artefactos indexados (+11 vs antes: los deprecated ahora visibles) |
| `python3 toolchain/kora check --strict` | 28/29 verdes; 1 HIGH preexistente en `HANDOFF.md` del WIP del operador (status: handoff no canonico, no es mi cambio) |
| `python3 -m unittest discover -s tests` | (en background; resultado en commit) |

## Estado consolidado

### Que cerramos

- 1 spec absorbida en su contenedor natural (host-roles → gobernanza §12).
- 2 specs deprecadas con preservacion de URN y contenido como referencia.
- Catalogo categorialmente correcto: identidad URN estable a traves del
  lifecycle.
- ADR canonico producido — primera instancia de la familia `adr` en
  productivo.
- Gobernanza ahora declara explicitamente la disciplina de Fase 2
  (§13).

### Que queda como deuda — Fase 2 (requiere HITL)

1. **Compactar `autoria-spec` v1.2 → v2.0** (1194 → ~700 lineas).
   Requiere bajar freeze.
2. **Compactar `md-spec` v9 → v10** (1034 → ~700 lineas).
3. **Consolidar `runtime-spec-md` + `transmutation-spec`** en
   `runtime-spec` unificada. Requiere bajar freeze.
4. **Consolidar 6 runtime-extensions** en plantilla + extensiones
   derivadas.
5. **Refs `cites`** a host-roles/canario/procesos siguen apuntando a
   los URNs deprecados. Validas pero la proxima curacion editorial
   **DEBERIA** reapuntar a `urn:kora:kb:gobernanza` (para host-roles) o
   eliminar la cite (para canario/procesos cuando no aporta).
6. **Construction-* checks consolidados** en `construction-canonical`
   (cosmetico, postergado).

### Que NO debe asumirse

- No asumir que `host-roles` esta retirada: esta **deprecada**. El URN
  resuelve, el archivo existe, el contenido sigue siendo referencia
  valida.
- No asumir que `canario-spec` y `procesos-spec` no aportan valor:
  fueron deprecadas por **falta de clientes mecanicos**, no por
  contenido pobre. Si en el futuro un check las necesita, se reactivan.
- No asumir que la simplificacion v6 termino: la Fase 1 es solo el
  primer paso. La Fase 2 (compactacion de specs en freeze) es donde
  vive la mayor reduccion de lineas.

## Artefactos dejados versionados

### Specs
- `governance/gobernanza.md` v5.0.0 (absorbe host-roles).
- `governance/host-roles.md` v1.1.0 status: deprecado.
- `ontology/canario-spec.md` v1.1.0 status: deprecado.
- `ontology/procesos-spec.md` v1.0.0 status: deprecado.

### Toolchain
- `toolchain/kora_lib/catalog.py` — incluye deprecated/retired en catalogo.

### Knowledge
- `artifacts/knowledge/kora/adr/adr-kora-v6-simplificacion.md` (familia adr).

### Docs
- `docs/handoffs/2026-05-20-kora-v6-simplificacion-fase-1.md` (este).

## Prompt de continuacion

```text
Retoma KORA en /home/felix/kora desde el estado consolidado en
`docs/handoffs/2026-05-20-kora-v6-simplificacion-fase-1.md`.

Contexto vigente:

- `gobernanza v5.0.0` absorbe host-roles como §12. URN
  `urn:kora:kb:host-roles` esta deprecado pero resuelve.
- `canario-spec` y `procesos-spec` estan deprecadas (contenido
  referencia valida, sin canon).
- `catalog.py` expone deprecated/retired (preserva URN integrity).
- ADR `urn:kora:kb:adr-kora-v6-simplificacion` documenta la decision.
- Specs en freeze (harness-spec, autoria-spec, transmutation-spec)
  intactas. Su compactacion es Fase 2 con HITL dedicado.

Para Fase 2 (HITL requerido):

1. Bajar el freeze formal de §8.3 para las 3 specs criticas.
2. Compactar `autoria-spec` (1194 → ~700 lineas): consolidar atlas,
   reducir ejemplos redundantes con cheat-sheet, separar shape de
   transmutacion.
3. Compactar `md-spec` (1034 → ~700): mover §5.4.1 contraejemplos a
   referencias/, compactar §5.6 familias.
4. Consolidar `runtime-spec-md` + `transmutation-spec` en `runtime-spec`
   unificada con seccion de transmutation laws.
5. Refactorizar las 6 runtime-extensions con template comun.

Para mantenimiento continuo:

A. **Curar refs deprecadas**: artefactos que citen
   `urn:kora:kb:host-roles` pueden reapuntar a `urn:kora:kb:gobernanza`
   en su proxima edicion.
B. **Activar mas coalgebras**: medico-hospitalista, gtd-integral,
   steipete, allan-kelly tienen estados narrativos. Reconstruir como
   FSM real activa `coalgebra-conformance`.
C. **Construction-* consolidacion**: solo si el valor justifica el
   cost de migrar tests.

Mantener commits acotados por linea. NO tocar specs en freeze sin ADR
dedicado.
```
