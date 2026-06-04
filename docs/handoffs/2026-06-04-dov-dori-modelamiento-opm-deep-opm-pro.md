# Handoff — Dori, modelamiento-opm y deep-opm-pro

Fecha: 2026-06-04. Repositorio principal: `kora` (`master`). Repositorio
verificado/remediado: `~/projects/deep-opm-pro` (`main`).

## Estado actual

- `dov-dori` queda en `version: "1.2.1"`.
- `modelamiento-opm` queda en `version: "1.5.1"`.
- `modelamiento-opm` incorpora el estado operativo `re-elicitar` para consumir
  `deep-opm-pro.log-decisiones.v0`.
- `dov-dori` delega la mecanica de serializacion y re-elicitacion a
  `modelamiento-opm v1.5.1`, conservando la autoridad conceptual sobre el
  por-que del modelado.
- Despliegue KORA: `deploy-status` limpio, `ok:196 stale:0 missing:0 unsupported:0`.
- `deep-opm-pro` quedo limpio y pusheado en `main` con commit `b602609`
  (`test(canvas): cover automatic fan evidence`).

## Decisiones

- La exigencia de `deep-opm-pro` era correcta: un `LogDecisiones v0` sin
  consumidor KORA habria sido ceremonia write-only. Se absorbio el consumidor en
  la skill antes de habilitar cualquier exportador de log.
- `re-elicitar` es acto de modelado E0-E2, no marca de UI. La app registra;
  `modelamiento-opm` muta la fuente solo cuando existe
  `transicion.a == "ratificado-con-fuente"` y `fuente`.
- `anotado-en-mesa` no muta proto ni bundle.
- El match de anclas usa `claveAncla`/`claveProto`, nunca ids posicionales del
  bundle.
- `AnclaNormativa` es extension meta declarada: no es cuarta primitiva OPM y no
  emite OPL nuclear.
- En OpenClaw, `modelamiento-opm` se instalo tambien en el workspace `dov-dori`,
  porque Dori es su invocador experto natural.
- En `deep-opm-pro`, no se bajo el umbral de calidad: se agrego evidencia real
  de store para HU-15.008 y se re-sincronizo el dashboard.

## Artefactos relevantes

- `artifacts/agents/fxsl/dov-dori/AGENT.md`
- `artifacts/skills/kora/modelamiento-opm/SKILL.md`
- `artifacts/skills/kora/modelamiento-opm/referencias/bundle-deep-opm-pro.md`
- `artifacts/skills/kora/modelamiento-opm/referencias/*.md`
- `artifacts/skills/kora/modelamiento-opm/recursos/ejemplo-minimo-sd.md`
- `~/projects/deep-opm-pro/docs/proto-modelo/diseno-ancla-normativa.md`
- `~/projects/deep-opm-pro/docs/auditorias/2026-06-04-acta-mesa-flujo-canonico-dominio-opforja.md`
- `~/projects/deep-opm-pro/docs/HANDOFF.md`

## Verificacion

KORA:

- `python3 toolchain/kora check --strict --path artifacts/skills/kora/modelamiento-opm` -> 34/34.
- `python3 toolchain/kora check --strict --path artifacts/agents/fxsl/dov-dori` -> 34/34.
- `python3 toolchain/kora lint-md ...` sobre los tres archivos editados clave -> 0 issues.
- `python3 toolchain/kora deploy-status` -> `ok:196 stale:0 missing:0 unsupported:0`.

`deep-opm-pro`:

- `bun test src/store.test.ts` -> 86/0.
- `bun run check` -> typecheck + 2135 tests, 0 fail.
- `bun run lint` -> OK.
- `bun run build` -> OK.
- `bun run design:governance` -> OK.
- `bun run quality:gate` -> PASS, 73/105 reglas automaticas.

## Pendientes

- KORA: ninguno bloqueante para `dov-dori`/`modelamiento-opm`.
- `deep-opm-pro`: W5.2/W5.3 siguen pendientes: compilar anclas desde el proto y
  procedencia/staleness L6.
- `deep-opm-pro`: W6/W6.5 puede exportar logs cuando el consumidor KORA ya
  comprometido se use efectivamente.
- Material salud sin trackear en KORA queda fuera de este corte.

## Supuestos

- "El otro repo" referido por el operador es `~/projects/deep-opm-pro`.
- El contrato normativo vigente para esta ronda es el de
  `diseno-ancla-normativa.md` y las actas de mesa del 2026-06-04.
- Los cambios previos en referencias de `modelamiento-opm` eran parte del corte
  OPM/Forja y se preservaron; no se revirtio trabajo ajeno.

## Riesgos

- `LogDecisiones v0` ya tiene consumidor KORA, pero el exportador/log UX de la
  app aun depende de W6.5.
- OpenClaw fleet queda modificado por despliegue runtime externo; KORA lo
  verifica por `deploy-status`, pero no se versiona aqui.
- Los documentos salud sin trackear pueden confundir futuros `git add`; deben
  seguir excluidos salvo orden explicita.

## Prompt breve de continuacion

Retomar desde `docs/handoffs/2026-06-04-dov-dori-modelamiento-opm-deep-opm-pro.md`.
Estado: `dov-dori v1.2.1` y `modelamiento-opm v1.5.1` desplegados a
`claude-code`, `codex`, `opencode` y `openclaw`; `re-elicitar` absorbe
`LogDecisiones v0`; `deep-opm-pro` esta verde y pusheado en `b602609`. Siguiente
frente natural: W5.2/W5.3 en `deep-opm-pro` o pruebas vivas de re-elicitacion
con un proto/bundle real.
