---
_manifest:
  urn: "urn:kora:kb:operational-memory-2026-04-28-salubrista-corpus-skills"
  provenance:
    created_by: "Codex GPT-5"
    created_at: "2026-04-28"
    source: "Memoria operativa compacta del cierre salubrista corpus fisico + skills Hospitalista/HODOM/FIRS."
version: "1.0.0"
status: publicado
tags: [operational-memory, salubrista, hospitalista, hodom, firs, corpus]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:kora:kb:handoff-2026-04-28-salubrista-corpus-skills"
    - "urn:salud:artefacto:salubrista"
    - "urn:salud:artefacto:hospitalista"
    - "urn:salud:artefacto:hospitalizacion-domiciliaria"
    - "urn:salud:artefacto:firs-razonamiento-sanitario"
---

# Memoria Operativa - Salubrista Corpus y Skills

## Snapshot

| Item | Estado |
|------|--------|
| Repo | `/home/felix/kora` |
| Rama | `master` |
| Agente productivo | `artifacts/agents/salud/salubrista/AGENT.md` |
| Agente subsumido | `artifacts/agents/salud/salubrista-hah/AGENT.md` deprecado |
| Corpus canonico | `artifacts/knowledge/salud/salubrista/` |
| Skill nueva | `artifacts/skills/salud/hospitalista/SKILL.md` |
| Skill HODOM | `artifacts/skills/salud/hospitalizacion-domiciliaria/SKILL.md` |
| Skill FIRS | `artifacts/skills/salud/firs-razonamiento-sanitario/SKILL.md` |
| Regla central | conocimiento en KB; razonamiento/perfil en agente o skill |

## Hechos Durables

1. `salubrista` es el unico agente productivo para salubrista general,
   hospitalista y hospitalista a domicilio.
2. `salubrista-hah` no debe evolucionar como agente separado; queda subsumido.
3. El corpus de conocimiento salubrista vive fisicamente en
   `artifacts/knowledge/salud/salubrista`.
4. Las fuentes canonicas son salud publica global, management engineering y
   continuidad post-aguda/LTSS.
5. `publihealth` es alias deprecado de Oxford; no es una fuente independiente.
6. FIRS es metodo/skill, no KB de dominio.
7. Hospitalista intrahospitalario es skill propia, no solo modo textual.
8. HODOM se coordina con Hospitalista cuando hay camas, altas, boarding,
   reingresos o continuidad de red.

## Validacion Base

- `python3 toolchain/kora check --strict`: 20 checks OK.
- `python3 -m unittest discover -s tests`: 349 OK, 1 skipped.
- `python3 toolchain/kora kb-graph --json --orphans`: 0 broken edges, 0 ciclos.

## Continuidad

Toda sesion posterior debe partir del handoff
`docs/reports/handoff-2026-04-28-salubrista-corpus-skills.md`.

Invariante a conservar: no volver a autorizar
`urn:salud:kb:firs-framework-integrado-razonamiento-salud` ni perfiles
salubristas deprecados como `conocimiento_permitido` de agente/skill.
