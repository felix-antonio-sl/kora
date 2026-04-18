---
_manifest:
  urn: "urn:kora:kb:next-session-prompt-2026-04-18-toolchain-wave1-closeout"
  provenance:
    created_by: "Codex"
    created_at: "2026-04-18"
    source: "Prompt operativo para retomar la siguiente deuda despues del cierre post-ola 1 y la integracion core de atomize."
version: "1.0.0"
status: publicado
tags: [prompt, next-session, toolchain, agentskills, atomize, runtime-extensions]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:kora:kb:handoff-2026-04-18-toolchain-wave1-closeout"
    - "urn:kora:kb:operational-memory-2026-04-18-toolchain-wave1-closeout"
---

# Prompt próxima sesión — cierre de interop `habilidad`

```text
Retoma el repo /home/felix/kora desde el estado consolidado en:

- docs/reports/operational-memory-2026-04-18-toolchain-wave1-closeout.md
- docs/reports/handoff-2026-04-18-toolchain-wave1-closeout.md

Estado que debes asumir como vigente:

- Los 7 AGENT.md productivos ya estan migrados a autoria-spec v1.0 y pasan autoria_validate.
- python3 scripts/kora check --strict esta en verde (12/12) al 18 de abril de 2026.
- scripts/kora_lib/promote.py ya absorbe el acceptance gate de atomic; publish_atomic.py delega al mismo predicado.
- La deuda restante ya no es de shape ni de enforcement base.

Objetivo principal:

- cerrar fidelidad-agentskills de extremo a extremo para forma_material=habilidad.

Subobjetivos:

1. inspecciona autoria-spec §5.5 y §15.3, codex-runtime-extension.md,
   claude-code-runtime-extension.md y transmutation-spec.md
2. implementa o completa el flujo:
   python3 scripts/kora transmute --artefacto <ns>/<nombre> --target agentskills
3. agrega el check `fidelidad-agentskills` para validar paquete
   agentskills.io byte-identical o, si la byte-identidad estricta no es
   posible, documenta con precision el residual y reduce el gap al minimo
4. usa SKILLS/kora/atomize como caso real de referencia para habilidad
   productiva
5. solo despues evalua la deuda secundaria:
   - actualizar runtime extensions v1.1+ para exponer la matriz
     (arnes_categorico × forma_material × runtime)
   - decidir si conviene regenerar los bundles historicos
     atomic-opm-libro* que aun mencionan el URN legacy de atomize

Restricciones:

- no arrastres docs/generated/* ni catalog/catalog_master_kora.yml al
  commit salvo que tu sesion haga una pasada explicita de sync-docs/index
- mantén el commit acotado a la linea de interop habilidad/agentskills
- preserva la perspectiva categorial y el lenguaje declarativo del
  toolchain
```
