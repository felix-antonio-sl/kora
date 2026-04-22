---
_manifest:
  urn: "urn:kora:kb:handoff-2026-04-22-hetzner289-kora-auditoria-entrega"
  provenance:
    created_by: "Codex GPT-5"
    created_at: "2026-04-22"
    source: "Auditoría e inventario del estado actual de KORA en el servidor hetzner2897261 para continuidad operativa."
version: "1.0.0"
status: publicado
tags: [handoff, auditoria, inventario, hetzner, entrega, server]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:kora:kb:operational-memory-2026-04-22-hetzner289-kora-auditoria-entrega"
    - "urn:kora:kb:next-session-prompt-2026-04-22-hetzner289-kora-auditoria-entrega"
  refines:
    - "urn:kora:kb:handoff-2026-04-21-jointjs-skill-y-transmutacion-claude"
---

# Handoff explícito — auditoría de entrega en `hetzner2897261`

## Resumen ejecutivo

Se auditó el servidor `hetzner2897261` y el resultado es:

- host accesible por SSH
- repo `kora` presente en `/home/felix/kora`
- branch `master`
- `HEAD == origin/master == 4f5ddbc`
- `check --strict` verde (`18/18`)
- `deploy-status` sin stales (`1 ok`, `7 missing`)
- bundle de `jointjs-open-source` generado en `_BUILD/claude-code/`
- skill instalada en `~/.claude/skills/jointjs-open-source/SKILL.md`
- **falla 1 test** en `python3 -m unittest discover -s tests`
- existe drift local no commiteado: `tests/fixtures/canarios/urgenciologo-baseline.md`

## Inventario factual

### Host

- alias SSH: `hetzner2897261`
- host real: `138.201.53.205`
- user: `felix`
- home: `/home/felix`

### Tooling disponible

- `python3`: presente
- `git`: presente
- `rg`: presente
- `claude`: **no aparece en PATH** al momento de la auditoría

### Paths relevantes

- repo: `/home/felix/kora`
- skills Claude: `/home/felix/.claude/skills/`
- bundle local de JointJS: `/home/felix/kora/artifacts/skills/kora/jointjs-open-source/_BUILD/claude-code/jointjs-open-source/SKILL.md`
- instalación actual de la skill JointJS: `/home/felix/.claude/skills/jointjs-open-source/SKILL.md`

## Estado Git del server

En `/home/felix/kora`:

- branch: `master`
- HEAD: `4f5ddbc`
- `origin/master`: `4f5ddbc`

Commits visibles en punta:

- `4f5ddbc` — `chore(docs): regenera kb-graph y repo-graph con sync-docs`
- `6ff75a8` — `test(kb-graph): rescata regression guard de determinismo`
- `18b9e92` — `docs(reports): agrega handoff skill jointjs`
- `b4db0f1` — `feat(transmute): soporta skill a claude code`
- `1b7352f` — `docs(plan): alinea spec skill jointjs con shape kora`

Importante:

- el server está **por delante** del checkout local desde el que veníamos trabajando antes del `fetch/ff-only`
- se verificó eso y el checkout local quedó fast-forward a `4f5ddbc` antes de escribir este handoff

## Verificación corrida en server

### 1. `check --strict`

Comando:

```bash
cd /home/felix/kora
python3 toolchain/kora check --strict
```

Resultado:

- `Checks run: 18`
- `Passed: 18`
- `Failed: 0`

### 2. `deploy-status`

Comando:

```bash
cd /home/felix/kora
python3 toolchain/kora deploy-status
```

Resultado:

- `salud/urgenciologo` en Claude = `ok`
- `gn/digitrans`, `gn/goreologo`, `kora/clawforge`, `kora/curator`,
  `kora/custodio`, `kora/forgemaster`, `kora/guardian` = `missing`
- `stale = 0`

Interpretación:

- no hay drift rojo por despliegues stale
- sí hay backlog operativo de despliegue incompleto del fleet Claude

### 3. `unittest discover`

Comando:

```bash
cd /home/felix/kora
python3 -m unittest discover -s tests
```

Resultado:

- `Ran 323 tests`
- `FAILED (failures=1, skipped=2)`

Fallo concreto:

- `test_publish_atomic_wrapper_requires_fresh_accepted_review`
- archivo: `tests/test_atomize.py`
- síntoma: `review_path.exists()` devuelve `False`

Interpretación:

- la entrega del server **no está verde** a nivel suite completa
- el bloqueo no es de toolchain base ni de la línea `jointjs`; es del flujo
  `atomize/publish_atomic`

## Estado de la línea JointJS

### Hecho

- la skill productiva existe:
  [artifacts/skills/kora/jointjs-open-source/SKILL.md](/Users/felixsanhueza/Developer/kora/artifacts/skills/kora/jointjs-open-source/SKILL.md)
- la transmutación `skill -> claude-code` existe
- el bundle se genera correctamente
- la skill está copiada en `~/.claude/skills/jointjs-open-source/SKILL.md`

### Falta

- validar uso real de la skill desde Claude **en el server**
- eso hoy está bloqueado parcialmente porque `claude` no apareció en PATH en la auditoría

Conclusión práctica:

- el server **tiene el artefacto instalado**
- pero no quedó demostrado que el runtime Claude esté utilizable ahí

## Estado de entrega que el server debe tener en cuenta

1. **La entrega no está totalmente verde**
   mientras exista el fallo de `test_atomize.py`.

2. **No asumir que JointJS es el problema**
   La línea JointJS parece sana; la falla observada es de `atomize/publish_atomic`.

3. **No asumir que Claude está operativo**
   solo porque existe `~/.claude/skills/jointjs-open-source/SKILL.md`.
   Hay que verificar binario/configuración real de `claude`.

4. **No commitear `tests/fixtures/canarios/urgenciologo-baseline.md`**
   sin decidir si es fixture canónica o residuo de trabajo.

## Pendientes concretos

1. Diagnosticar y reparar la falla de `test_publish_atomic_wrapper_requires_fresh_accepted_review`
2. Decidir destino de `tests/fixtures/canarios/urgenciologo-baseline.md`
3. Verificar si `claude` debe instalarse o si solo falta PATH/config en el server
4. Recién después retomar continuidad funcional de la skill JointJS o abrir el siguiente gap (`skill -> codex`)

## Recomendación de orden

Orden más sano para el server:

1. arreglar `test_atomize.py`
2. limpiar/decidir `tests/fixtures/canarios/`
3. verificar runtime `claude`
4. probar la skill `jointjs-open-source` instalada
5. seguir con el próximo runtime o siguiente fase
