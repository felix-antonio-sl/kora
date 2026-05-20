---
_manifest:
  urn: "urn:kora:kb:next-session-prompt-2026-04-19-portabilidad-asegurada"
  provenance:
    created_by: "Claude Opus 4.7 (encarnando cat-thinking)"
    created_at: "2026-04-19"
    source: "Prompt autocontenido para continuar KORA en la proxima sesion."
version: "1.0.0"
status: publicado
tags: [next-session-prompt, portabilidad, h2-artifacts]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:kora:kb:handoff-2026-04-19-portabilidad-asegurada"
    - "urn:kora:kb:operational-memory-2026-04-19-portabilidad-asegurada"
---

# Prompt de proxima sesion

Copiar el bloque en `<prompt>` como mensaje inicial del proximo Claude Code
en `/home/felix/kora`.

<prompt>
Encarnate en artifacts/skills/_TALLER/INBOX/cat-thinking y opera
sobre KORA (/home/felix/kora, rama master, HEAD posterior al commit de
portabilidad asegurada del 2026-04-19).

Contexto:

- El cierre estructural mayor del 2026-04-19 ya esta en origin/master
  (qa-spec, procesos-spec, multiagente-spec, risk-register-spec,
  mastra-runtime-extension, curacion KB sin huerfanos reales).
- El bloque de portabilidad del 2026-04-19 (segunda parte) ya esta en
  origin/master: helpers kappa en tests/common.py, check
  portabilidad-tests, CI matrix Linux+macOS, runtime guard Python >=3.11,
  4 scripts one-shot movidos a toolchain/legacy_migration/, politica en
  CLAUDE.md §Portabilidad.

Leer primero:

- docs/reports/handoff-2026-04-19-portabilidad-asegurada.md
- docs/reports/operational-memory-2026-04-19-portabilidad-asegurada.md

Verificacion minima obligatoria antes de tocar nada:

    python3 toolchain/kora check --strict
    python3 -m unittest discover -s tests
    python3 toolchain/kora kb-graph --json --orphans

Contrato esperado al arranque:

- check --strict = 17/17 verde
- unittest = 299 OK (skipped=2)
- kb-graph = 0 huerfanos reales y 0 aristas rotas

Si cualquiera falla, diagnosticar drift antes de avanzar. Orden:
1. git status (buscar residuos tipo AGENTS/ legacy o tmp/).
2. git log --oneline -5 (confirmar HEAD incluye portabilidad).
3. Correr el test especifico con -v si falla uno solo.
No parchar sintomas.

Backlog recomendado ahora que estructura y portabilidad estan cerradas:

1. H2-artifacts: clasificar los 168 CM-* embebidos en agentes productivos en:
   - promover a artifacts/skills/ los reutilizables
   - absorber al AGENT.md los de uso unico
   - descartar legacy no justificable

2. Promocion staging:
   - 21 agentes en artifacts/agents/_FRAGUA/INBOX/
   - 7 skills en artifacts/skills/_TALLER/INBOX/

3. Menores diferibles:
   - H9 TracesRequirement
   - H17 catalogo de patrones de skills
   - H20 wiring diagrams Mermaid
   - H22 modelo organizacional Part IX

Metodologia:

- modo audit + formalize
- sin romanticismo por lo legacy
- no mezclar cambios ajenos de artifacts/knowledge/fxsl/opm/opm-ssot-es/*
- cualquier cambio debe dejar check --strict verde antes de commit
- toda asercion test que compare path vs output CLI debe usar
  assert_path_in_output (politica CLAUDE.md §Portabilidad)
- paths literales tipo /tmp/ /Users/ /home/ /var/folders/ /private/var/ son
  anti-patron en tests/ y toolchain/ excepto dentro de legacy_migration/

Primera pregunta al usuario:

¿Arrancamos por deuda de artefactos (168 CM-*), por promocion de staging,
o por uno de los menores (H9/H17/H20/H22)?
</prompt>
