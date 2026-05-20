---
_manifest:
  urn: "urn:kora:kb:handoff-2026-04-28-openclaw-salubrista-urgenciologo"
  provenance:
    created_by: "Codex GPT-5"
    created_at: "2026-04-28"
    source: "Cierre de sesion: transmutacion salubrista a Claude Code, Codex y OpenClaw; actualizacion OpenClaw de urgenciologo; contrato permanente de repo KORA vivo para agentes OpenClaw."
version: "1.0.0"
status: publicado
tags: [handoff, openclaw, salubrista, urgenciologo, transmutacion, kora-repo]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:kora:kb:operational-memory-2026-04-27-openclaw-kora-live-kb"
    - "urn:agengai:kb:openclaw-runtime-extension"
    - "urn:ops:kb:principios-transmutacion-kora-openclaw"
    - "urn:salud:artefacto:salubrista"
    - "urn:salud:artefacto:urgenciologo"
---

# Handoff — OpenClaw Salubrista/Urgenciologo

## Estado actual

`salud/salubrista` quedo declarado para `claude-code`, `codex` y `openclaw`.
La transmutacion local genero:

- `artifacts/agents/salud/salubrista/_BUILD/claude-code/`
- `artifacts/agents/salud/salubrista/_BUILD/codex/`
- `artifacts/agents/salud/salubrista/_BUILD/openclaw/`

`salud/urgenciologo` mantiene su agente productivo y se actualizo su contrato
OpenClaw para usar el repo KORA vivo. Su build local queda en:

- `artifacts/agents/salud/urgenciologo/_BUILD/openclaw/`

Los directorios `_BUILD/` son derivados y gitignored; no forman parte del
commit salvo decision explicita futura.

## Decisiones

1. Todo agente OpenClaw KORA se despliega en maquinas con KORA local clonado y
   actualizado.
2. `KORA_REPO` es precondicion de deploy; por defecto apunta a
   `/home/felix/kora`.
3. El repo se monta read-only en `/home/node/repos/kora`.
4. Los aliases `/home/node/knowledge/{namespace}/{corpus}` pueden existir, pero
   deben apuntar al mismo clon KORA y no a copias desacopladas.
5. `_transmutation.yml` OpenClaw ahora emite `kora_repo_access` para que el
   contrato sea verificable por toolchain/deploy.
6. `salubrista-hah` no revive como agente separado; sus capacidades viven en
   `salubrista` mediante modos hospitalista y hospitalizacion domiciliaria.

## Artefactos versionados relevantes

- `artifacts/agents/salud/salubrista/AGENT.md`
- `artifacts/agents/salud/urgenciologo/AGENT.md`
- `runtime/openclaw-runtime-extension.md`
- `artifacts/knowledge/ops/principios-transmutacion-kora-openclaw.md`
- `docs/reports/operational-memory-2026-04-27-openclaw-kora-live-kb.md`
- `toolchain/kora_lib/transmute.py`
- `tests/test_openclaw_kora_live_repo.py`

## Memoria consolidada

La memoria permanente esta en
`docs/reports/operational-memory-2026-04-27-openclaw-kora-live-kb.md`.
Ese documento generaliza el patron desde `urgenciologo` y `salubrista` a
nuevos agentes OpenClaw KORA.

## Verificacion ejecutada

- `python3 toolchain/kora index`: OK, 664 artefactos indexados.
- `python3 toolchain/kora check --strict`: 20/20 OK.
- `python3 -m unittest tests.test_openclaw_kora_live_repo`: 4 OK.
- `python3 -m unittest tests.test_salubrista_hodom`: 7 OK.
- `python3 -m unittest discover -s tests`: 353 OK, 1 skipped.
- `python3 toolchain/kora kb-graph --json --orphans`: 0 broken edges, 0 ciclos;
  11 huerfanos reales reportados por la herramienta.

## Pendientes

1. Desplegar los builds OpenClaw reales con `kora/clawforge` o el proceso
   operacional vigente.
2. Ejecutar `openclaw doctor` en la maquina de destino.
3. Probar E2E por Telegram:
   - `salubrista`: HODOM, hospitalista, fuera de corpus.
   - `urgenciologo`: dolor toracico, fuera de corpus, paciente inestable.
4. Decidir si se limpia de forma separada el staging
   `artifacts/agents/_FRAGUA/INBOX/salubrista`.

## Supuestos

- La maquina de destino tendra KORA clonado, actualizado y accesible por
  `KORA_REPO`.
- Los tokens Telegram, auth profiles, pairing stores y sesiones siguen siendo
  runtime state, no artefactos KORA.
- `web_search` para `salubrista` se limita a vigencia normativa o datos
  fecha-dependientes; `urgenciologo` permanece sin web.

## Riesgos

- `_BUILD/` es local y derivado; si se borra, debe regenerarse con
  `python3 toolchain/kora transmute`.
- Si el deploy monta una copia de knowledge en vez del clon KORA vivo, puede
  aparecer drift semantico.
- Si `KORA_REPO` no esta actualizado, el agente puede resolver URNs contra
  corpus obsoleto.
- La validacion runtime OpenClaw real aun no se ejecuto en esta sesion.
