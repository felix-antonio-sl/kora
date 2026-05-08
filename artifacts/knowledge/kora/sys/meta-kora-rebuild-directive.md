---
_manifest:
  urn: "urn:kora:kb:meta-kora-rebuild-directive"
  provenance:
    created_by: "OpenAI Codex"
    created_at: "2026-05-03"
    source: "Decision operativa FS: reconstruir desde cero el stack meta-KORA (custodio, guardian, curator y auxiliares) sin usar los artefactos existentes como fuente."
version: "1.1.0"
status: publicado
tags: [meta-kora, rebuild, governance, agents, skills, runtime]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:kora:kb:gobernanza"
    - "urn:kora:kb:harness-spec"
    - "urn:kora:kb:autoria-spec"
    - "urn:kora:kb:agent-skill-construction-spec"
---

# Directiva de reconstruccion meta-KORA

## 1. Decision

Desde el `2026-05-03`, los artefactos operativos meta-KORA existentes para
custodia, guardiania, curaduria, construccion de agentes/skills y conduccion de
knowledge quedan fuera del canon operativo. Se conservan solo como memoria
historica o cuarentena de auditoria.

No deben usarse como fuente de diseno, prompt, transmutacion, runtime activo,
blueprint ni derivacion incremental para la siguiente generacion.

## 2. Alcance

La directiva cubre, como minimo:

- agentes: `kora/custodio`, `kora/guardian`, `kora/clawforge` y cualquier
  reemplazo historico de `kora/curator` o `kora/forgemaster`
- skills: `artifact-curator`, `curation-conductor`, `knowledge-curator`,
  `kora-agents`, `kora-skills`, `intent-classifier` y
  `lifecycle-orchestrator` cuando operen como piezas de ese stack viejo
- bundles runtime desplegados desde esos artefactos en Claude Code, Codex u
  OpenCode

Quedan fuera de esta directiva las skills de pensamiento o dominio que no son
operadores meta-KORA, por ejemplo `cat-thinking`, `mente-omega`,
`modelamiento-opm` y `jointjs-open-source`.

## 3. Regla operativa

Para construir la nueva generacion:

1. partir de specs vigentes, no de la implementacion vieja
2. declarar requisitos antes de escribir `AGENT.md` o `SKILL.md`
3. crear drafts nuevos en `_FRAGUA/REVIEW/` o `_TALLER/REVIEW/`
4. validar contra `autoria-spec` y `agent-skill-construction-spec`
5. transmutar solo despues de que el IR nuevo sea canonico

Los artefactos viejos pueden consultarse unicamente para inventario negativo:
que no debe reintroducirse, que deuda dejo y que runtime activo hay que retirar.

## 4. Criterio de salida

La reconstruccion se considera cerrada solo cuando existan nuevos artefactos
canonicos, con URN y runtime derivados frescos, y los bundles viejos hayan sido
retirados de los directorios activos bajo `/home/felix`.

## 5. Estado de cierre por artefacto (2026-05-08, v1.1)

| Artefacto legacy | Estado | Reemplazo canonico | URN |
|---|---|---|---|
| `kora-agents` (skill) | **CERRADO** | reconstruccion fresca | `urn:kora:artefacto:kora-agents` v0.1.0 (productivo) |
| `kora-skills` (skill) | **CERRADO** | reconstruccion fresca | `urn:kora:artefacto:kora-skills` v0.1.0 (productivo) |
| `custodio-kora` (skill, ex `kora/custodio` agente) | **CERRADO** | habilidad nueva tras retirar agente | `urn:kora:artefacto:custodio-kora` v1.0.0 (productivo) |
| `artifact-curator` (skill) | **ARCHIVADA SIN REEMPLAZO** | sin cliente nombrado; queda cubierto parcialmente por kora-agents/kora-skills/atomize | — |
| `curation-conductor` (skill) | **ARCHIVADA SIN REEMPLAZO** | sin cliente nombrado; orquestacion humana + custodio-kora cubren el flujo en uso | — |
| `knowledge-curator` (skill) | **ARCHIVADA SIN REEMPLAZO** | sin cliente nombrado; atomize cubre family=atomic | — |
| `intent-classifier` (skill) | **ARCHIVADA SIN REEMPLAZO** | sin cliente nombrado | — |
| `lifecycle-orchestrator` (skill) | **ARCHIVADA SIN REEMPLAZO** | sin cliente nombrado; toolchain CLI cubre lifecycle mecanico | — |
| `kora/guardian` (agente) | **ARCHIVADA SIN REEMPLAZO** | sin cliente nombrado; auditoria cubierta por skills nuevas (custodio-kora) | — |
| `kora/clawforge` (agente) | **ARCHIVADA SIN REEMPLAZO** | sin cliente nombrado; toolchain transmute + deploy cubren la mecanica | — |
| `kora/curator`, `kora/forgemaster` (agentes) | **CERRADO** | retirados como agentes; funcion absorbida por skills (kora-agents, kora-skills, custodio-kora) | — |

Las skills marcadas **ARCHIVADA SIN REEMPLAZO** permanecen en cuarentena
bajo `artifacts/skills/_TALLER/INBOX/_rebuild_required/2026-05-03/kora/`
con `status: retirado` y `extensions.kora.rebuild.current_is_source:
false`. No se transmutan ni deployan. Su reactivacion requiere cliente
nombrado con valor validado, segun la postura version A
(`docs/plans/2026-05-07-politica-handoffs.md` y plan de poda asociado).

Los agentes legacy quedan registrados con
`status: rebuild_required` en `META_KORA_STATUS` de
`toolchain/kora_lib/config.py` para que el reporte de coherencia los
mantenga visibles como deuda archivada.

## 6. Conclusion operativa

La directiva v1.0 (2026-05-03) cumple para los 3 items con cliente
real (kora-agents, kora-skills, custodio-kora). Para el resto, la
postura version A de la poda (2026-05-07) cierra el alcance de
reconstruccion: no se construyen meta-skills sin demanda concreta. La
cuarentena queda viva como inventario negativo (que NO debe
reintroducirse).
