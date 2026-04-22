---
_manifest:
  urn: "urn:kora:kb:handoff-2026-04-22-hetzner289-kora-auditoria-entrega"
  provenance:
    created_by: "Codex GPT-5"
    created_at: "2026-04-22"
    source: "Auditoría e inventario del estado actual de KORA en el servidor hetzner2897261 para continuidad operativa."
version: "1.1.0"
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
- `HEAD == origin/master == 39c4cf4`
- `check --strict` verde (`18/18`)
- `deploy-status` sin stales (`1 ok`, `7 missing`)
- bundle de `jointjs-open-source` generado en `_BUILD/claude-code/`
- skill instalada en `~/.claude/skills/jointjs-open-source/SKILL.md`
- `python3 -m unittest discover -s tests` vuelve a verde
- existe drift local no commiteado: `artifacts/knowledge/_SCRIPTORIUM/REVIEW/kora/atomic/atomic-test-acceptance-review.md`

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
- HEAD: `39c4cf4`
- `origin/master`: `39c4cf4`

Commits visibles en punta:

- `39c4cf4` — `chore(docs): regenera generated/ tras canario-spec v1.0.0`
- `7790908` — `feat(canario): formaliza verificacion runtime de artefactos agenticos`
- `e07bb9a` — `docs(reports): agrega auditoria hetzner289`
- `4f5ddbc` — `chore(docs): regenera kb-graph y repo-graph con sync-docs`
- `6ff75a8` — `test(kb-graph): rescata regression guard de determinismo`

Importante:

- el server estaba por delante del checkout local previo
- se verificó eso y el checkout local quedó fast-forward a `39c4cf4` antes de reemitir esta auditoría

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
- `OK (skipped=2)`

Interpretación:

- la entrega del server volvió a verde a nivel suite completa
- el fallo observado en la auditoría previa ya no está presente

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

1. **La entrega está verde a nivel checks y suite**
   pero no todavía a nivel validación runtime real de Claude.

2. **No asumir que JointJS está probado end-to-end**
   La línea JointJS parece sana a nivel de bundle e instalación, pero no quedó
   demostrada todavía una invocación real del skill usando Claude en ese host.

3. **No asumir que Claude está operativo**
   solo porque existe `~/.claude/skills/jointjs-open-source/SKILL.md`.
   Hay que verificar binario/configuración real de `claude`.

4. **No commitear `artifacts/knowledge/_SCRIPTORIUM/REVIEW/kora/atomic/atomic-test-acceptance-review.md`**
   sin decidir si es evidencia canónica o residuo de la corrida de tests.

## Pendientes concretos

1. Decidir destino de `artifacts/knowledge/_SCRIPTORIUM/REVIEW/kora/atomic/atomic-test-acceptance-review.md`
2. Verificar si `claude` debe instalarse o si solo falta PATH/config en el server
3. Probar invocación real de la skill `jointjs-open-source`
4. Recién después abrir el siguiente gap (`skill -> codex`)

## Recomendación de orden

Orden más sano para el server:

1. decidir el destino del artefacto atomic suelto en `_SCRIPTORIUM/REVIEW/`
2. verificar runtime `claude`
3. probar la skill `jointjs-open-source` instalada
4. seguir con el próximo runtime o siguiente fase
