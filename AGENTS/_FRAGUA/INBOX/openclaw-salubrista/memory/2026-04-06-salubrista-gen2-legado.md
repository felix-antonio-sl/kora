# Salubrista 2ª gen — legado absorbido

**Fecha absorcion:** 2026-04-06
**Fuente:** paquete `salubrista-hah-reconstruction-full` (kora, Docker)

## Que valia

- FSM completa de 11 estados con transiciones priorizadas (WF-SALUBRISTA-HAH)
- Especializacion profunda en hospitalizacion integrada + HD/HaH
- 17 reglas duras con scope explicito
- Checklist de co-induccion de 17 items
- Protocolo de correccion por item
- 9 skills operativas (4 absorber como nuevas, 5 ya existian)
- Memoria historica del proyecto HODOM HSC
- 21 pacientes con historias y sintesis

## Skills absorbidas (nuevas)

| Skill | Origen | Destino |
|-------|--------|---------|
| `clarifier` | legado | `skills/clarifier/` |
| `hah-specialist` | legado | `skills/hah-specialist/` |
| `hospital-system-analyst` | legado | `skills/hospital-system-analyst/` |
| `intent-hospitalization` | legado | `skills/intent-hospitalization/` |

## Skills que ya existian (no duplicadas)

`epi-vigilance`, `implementation-planner`, `product-builder`, `quality-auditor`, `report-builder`

## Skills propias 3ª gen (conservadas)

`epi-analyst`, `intent-salubrista`, `network-analyst`, `opm-modeler`

## Total skills post-absorcion: 13

## Que no se absorbio

- Referencias a federacion kora (kora-personal, kora-steipete, hooks cross-gateway)
- Routing via hook URLs (reemplazado por sessions_send nativo)
- Terminologia Docker/node user paths
- Workspace convention legacy (reemplazada por convencion 3ª gen)

## Injertos realizados

- `SOUL.md`: identidad especializada del legado (6 figuras, 4 paradigmas, 4 ejes, 5 tensiones)
- `AGENTS.md`: FSM completa + reglas duras + co-induccion + protocolo correccion + contexto multi-turno
- `MEMORY.md`: anclas a HODOM HSC, skills, legado
- `reference/legacy-salubrista/`: archivos core + memoria historica preservada
