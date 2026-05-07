---
_manifest:
  urn: "urn:kora:kb:canario-pediatrico-postergado"
  provenance:
    created_by: "FS"
    created_at: "2026-05-07"
    source: "Decision operativa derivada del plan de poda KORA version A. Documenta postergacion del cierre del canario adversarial pediatrico de urgenciologo."
version: "1.0.0"
status: publicado
tags: [canario, urgenciologo, deuda, postergacion, poda-version-a]
lang: es
extensions:
  kora:
    family: note
relations:
  cites:
    - "urn:salud:artefacto:urgenciologo"
    - "urn:salud:kb:med-emergencia"
---

# Canario adversarial pediatrico — postergacion formal

## Resumen

El canario adversarial out-of-corpus de `urgenciologo` cerro `parcial` el 2026-05-04 (`docs/reports/handoff-2026-05-04-canario-adversarial-cierre.md`, `invocations.jsonl`). Tres deudas declaradas:

1. regla anti-shards-adultos no endurecida en el AGENT.md.
2. omision de cifras pediatricas sin fuente externa.
3. frase literal de derivacion pediatrica.

El plan de poda KORA version A (allan-kelly, 2026-05-07) asignaba como prioridad cero el cierre de esta deuda **antes** de cualquier poda estructural. Esa prioridad se posterga formalmente bajo las condiciones de esta nota.

## Razon de la postergacion

La poda version A se ejecuta con el contexto fresco del ciclo IFML cerrado limpio (commit `3f0ff6b`, segunda celula con loop eval cerrado). La evidencia operativa indica que las piezas core de KORA (specs, toolchain, transmute, deploy) estan pagando prima medible y soportan poda inmediata. Postergar la poda hasta cerrar el canario pediatrico extiende deuda compuesta (drift documental, runtimes sin uso, _FRAGUA hinchado) sin proteger el outcome de urgenciologo a corto plazo.

La deuda del canario pediatrico no impide a `urgenciologo` operar dentro de su corpus declarado; impide solo que sus respuestas en cohorte adversarial pediatrica cumplan el criterio `pasa-estricto`. Esa cohorte es out-of-corpus por diseño.

## Condiciones de la postergacion

| Condicion | Estado |
|---|---|
| `urgenciologo` no debe responder consultas pediatricas sin invocar la regla de fuera-de-alcance | Pendiente (regla anti-shards-adultos) |
| Ningun deploy nuevo del agente productivo `urgenciologo` debe permitirse hasta cerrar la deuda | Aplicable a partir de hoy |
| El canario adversarial debe cerrar `pasa-estricto` antes de declarar `urgenciologo v3.1.0` o superior | Aplicable |
| Esta nota se cita en cualquier handoff posterior que toque `urgenciologo` mientras la deuda este abierta | Aplicable |

## Plan de cierre

Sesion dedicada con tres pasos:

1. Editar `artifacts/agents/salud/urgenciologo/AGENT.md` con la regla anti-shards-adultos endurecida y los hooks de citacion para cifras pediatricas externas.
2. Re-transmutar a `claude-code` y `openclaw`.
3. Re-correr el canario adversarial pediatrico en sesion nueva. Registrar `record-invocation` con `--eval-result pasa-estricto`.

Sin estimacion de fecha — la sesion se agenda cuando Felix lo decida. Mientras tanto, la deuda esta nominada y trazable en este artefacto.

## Trazabilidad

- handoff que abrio la deuda: `docs/reports/handoff-2026-05-04-canario-adversarial-cierre.md`
- registro de invocacion `parcial`: `docs/generated/invocations.jsonl` (linea con timestamp `2026-05-04T17:09:24Z`)
- plan de poda que la posterga: este documento
- postura adoptada: opcion B del plan de allan-kelly (postergacion documentada vs cierre inmediato)
