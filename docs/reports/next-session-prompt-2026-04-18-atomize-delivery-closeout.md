---
_manifest:
  urn: "urn:kora:kb:next-session-prompt-2026-04-18-atomize-delivery-closeout"
  provenance:
    created_by: "Codex"
    created_at: "2026-04-18"
    source: "Prompt operativo para continuar despues del cierre completo de atomize."
version: "1.0.0"
status: publicado
tags: [prompt, next-session, atomize, agentskills, runtime-extensions]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:kora:kb:operational-memory-2026-04-18-atomize-delivery-closeout"
    - "urn:kora:kb:handoff-2026-04-18-atomize-delivery-closeout"
---

# Prompt próxima sesión — interop posterior a `atomize`

```text
Retoma el repo /home/felix/kora desde el estado consolidado en:

- docs/reports/operational-memory-2026-04-18-atomize-delivery-closeout.md
- docs/reports/handoff-2026-04-18-atomize-delivery-closeout.md

Estado que debes asumir como vigente:

- `atomize` ya esta cerrado como productor canonico de la familia `atomic`.
- `SKILLS/kora/atomize/SKILL.md` ya conforma `autoria-spec v1.0` con
  URN `urn:kora:artefacto:atomize`.
- `scripts/kora_lib/promote.py` ya exige acceptance review fresca y
  aceptada para bundles `atomic`.
- `SKILLS/kora/atomize/scripts/publish_atomic.py` ya delega en el mismo
  predicado del core.
- `python3 -m unittest tests.test_atomize tests.test_check_pipeline`
  estaba en verde al 18 de abril de 2026.
- `python3 scripts/kora check --path SKILLS/kora/atomize` estaba en
  verde al 18 de abril de 2026.

Objetivo principal:

- cerrar la deuda de interop para `forma_material: habilidad`, empezando
  por `fidelidad-agentskills`.

Secuencia recomendada:

1. inspecciona `autoria-spec §5.5`, `autoria-spec §15.3`,
   `transmutation-spec.md`, `claude-code-runtime-extension.md` y
   `codex-runtime-extension.md`
2. usa `SKILLS/kora/atomize` como caso real de habilidad productiva
3. implementa o endurece el flujo de proyeccion a `agentskills`
4. agrega o cierra el check `fidelidad-agentskills`
5. solo despues evalua si conviene abrir la deuda secundaria:
   - runtime extensions v1.1+
   - armonizacion documental de `atomic-opm-libro*`

Restricciones:

- no arrastres `docs/generated/*`, `catalog/catalog_master_kora.yml` ni
  `KNOWLEDGE/_SCRIPTORIUM/INBOX/opm-libro-curado/` al commit
- mantén el commit acotado a interop/proyeccion de habilidades
- no reabras la linea `atomize` salvo que encuentres una regresion real
```
