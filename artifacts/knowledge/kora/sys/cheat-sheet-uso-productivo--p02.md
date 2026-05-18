---
_manifest:
  urn: urn:kora:kb:cheat-sheet-uso-productivo-p02
  provenance:
    created_by: Claude Opus 4.7
    created_at: '2026-05-19'
    source: Cheat sheet operativo derivado del estado vigente del repo tras refactors
      2026-05-17/18 (knowledge-spec v2.0, md-spec v9.0, agent-skill-construction-spec
      v1.1, autoria-conformance endurecido, relations-laws, coalgebra-conformance
      activable).
version: 1.0.0
status: publicado
tags:
- cheat-sheet
- productivo
- guia
- operativo
- kora
- cli
- lifecycle
lang: es
extensions:
  kora:
    family: guide
    shard_index: 2
    shard_count: 2
    shard_root_urn: urn:kora:kb:cheat-sheet-uso-productivo
relations:
  cites:
  - urn:kora:kb:gobernanza
  - urn:kora:kb:md-spec
  - urn:kora:kb:knowledge-spec
  - urn:kora:kb:autoria-spec
  - urn:kora:kb:harness-spec
  - urn:kora:kb:agent-skill-construction-spec
---

# Cheat Sheet — Uso productivo de KORA - Parte 02

## 10. Recuperacion de errores comunes

### 10.1 `kora check --strict` falla con `envelope-status-fuera-de-lugar`

```bash
# Auto-fix: codemod cubre los 4 codes de envelope hoist
python3 toolchain/kora migrate --perfil a-autoria
python3 toolchain/kora index
python3 toolchain/kora check --strict
```

### 10.2 `knowledge-zone` falla con `status: borrador en productivo`

Decidir:

- Si el artefacto **esta listo**: cambiar `status` a `publicado` y
 validar lint. Considerar mover via REVIEW si el contenido no fue
 auditado.
- Si **no esta listo**: mover a `_SCRIPTORIUM/REVIEW/{ns}/...`.

### 10.3 `relations-laws` detecta ciclo en `supersedes`

El check no auto-corrige (es decision editorial). Para romper el ciclo:

```bash
# Inspeccionar el ciclo
python3 toolchain/kora kb-graph --json | jq '.edges[] | select(.type=="supersedes")'

# Decidir: cual de las aristas elimina la cadena temporal.
# Editar el frontmatter del artefacto que tiene la arista invalida.
```

### 10.4 `coalgebra-conformance` falla con `verificacion_coalgebraica=true` pero `plan.fsm` ausente

```yaml
# En el AGENT.md, agregar bajo artefacto.plan:
artefacto:
 plan:
 estado_inicial: S-START
 estado_terminal: S-END
 estados:
 - id: S-START
 accion: "..."
 transiciones:
 - condicion: "ok"
 destino: S-END
 - id: S-END
 accion: "..."
 fsm:
 inicial: S-START
 terminales: [S-END]
 transiciones:
 S-START: [S-END]
 S-END: []
```

Reglas:
- `inicial` y todos los `terminales` deben existir en `estados`.
- Todo estado no terminal debe alcanzar algun terminal en finitos pasos.
- Si declaras `sub_coalgebra_segura`, sus estados deben cerrar bajo
 transiciones (cualquier transicion desde un estado seguro va a otro
 estado seguro).

### 10.5 Catalogo desincronizado tras git pull

```bash
python3 toolchain/kora index
python3 toolchain/kora check --strict
```

`catalog.yml` esta gitignored — siempre se regenera localmente.

## 11. Salida de sesion

Antes de cerrar sesion productiva:

```bash
python3 toolchain/kora index
python3 toolchain/kora check --strict # debe ser verde o solo LOWs trazables
python3 -m unittest discover -s tests # si tocaste toolchain/specs/tests
python3 toolchain/kora kb-graph --json --orphans # si tocaste knowledge

git status
git diff --cached --name-only | grep -v <archivos no propios>
git commit -m "..." # con Co-Authored-By si aplica
```

Reglas:

1. NO pushear sin que el operador autorice explicitamente.
2. NO incluir WIP del operador en el commit.
3. Handoff obligatorio cuando hay cambios doctrinales o de toolchain:
 `docs/handoffs/YYYY-MM-DD-{slug}.md`.

## 12. Atajos mentales

- **"Mi cambio tiene que ver con formato de markdown"** → `md-spec`.
- **"Mi cambio tiene que ver con pipeline/lifecycle de conocimiento"** → `knowledge-spec`.
- **"Mi cambio tiene que ver con shape de skill/agente"** → `autoria-spec` (en freeze; solo fixes).
- **"Mi cambio tiene que ver con como construir un skill/agente nuevo"** → `agent-skill-construction-spec`.
- **"Mi cambio tiene que ver con proyectar a un runtime"** → `transmutation-spec` (en freeze) + runtime-extension.
- **"Mi cambio tiene que ver con precedencia, lifecycle base o host"** → `gobernanza`.

Si dudo donde vive una regla: `gobernanza §3` (taxonomia) decide la
capa correcta.

## Referencias

- Constitucion: [Gobernanza](urn:kora:kb:gobernanza)
- Ontologia: [Harness Spec](urn:kora:kb:harness-spec) (freeze)
- Serializacion formato: [MD Spec](urn:kora:kb:md-spec)
- Serializacion knowledge: [Knowledge Spec](urn:kora:kb:knowledge-spec)
- Serializacion agentes/skills: [Autoria Spec](urn:kora:kb:autoria-spec) (freeze)
- Construccion pre-transmutacion: [Agent-Skill Construction Spec](urn:kora:kb:agent-skill-construction-spec)
- Runtime: [Transmutation Spec](urn:kora:kb:transmutation-spec) (freeze)
- Host roles: [Host Roles](urn:kora:kb:host-roles)
