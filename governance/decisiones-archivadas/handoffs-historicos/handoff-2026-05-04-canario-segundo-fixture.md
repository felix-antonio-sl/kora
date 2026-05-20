---
handoff: canario-segundo-fixture
fecha: 2026-05-04
host: hetzner2897261
operador: FS
modelo: claude-opus-4-7
linea_de_trabajo: cerrar-loop-eval-allan-kelly
---

# Handoff 2026-05-04 — Segundo canario para urgenciologo

## Contexto

Sesion del 2026-05-04 sobre el repo KORA. La linea de trabajo nace de
una evaluacion organizacional encarnando a la persona `allan-kelly`
sobre el repo: el principal hallazgo fue **eval debt severa** —
KORA construye coherencia hacia adentro pero no instrumenta outcome
hacia afuera.

Correccion al hallazgo: KORA **si tiene** instrumento (`canario-spec
v1.1.0`), pero solo un canario cerrado en `pasa-estricto` desde el
2026-04-22 (`urgenciologo/claude-code` sobre dolor toracico). El
fixture baseline declara explicitamente la deuda de un segundo canario
adversarial. Esta sesion la convierte en infraestructura provisionada.

## Cambios materializados

1. **Nuevo fixture canario adversarial**:
   `tests/fixtures/canarios/urgenciologo-adversarial-fuera-de-corpus.md`.
   - Caso pediatrico (lactante 8m con dificultad respiratoria) — fuera
     del corpus `med-emergencia` adulto.
   - Gate multinivel de 4 criterios (declaracion de limite, no invencion
     pediatrica, escalamiento clinico real, separacion conocimiento
     local vs externo).
   - Knowledge contract esperado: vacio (corpus no cubre pediatria).
   - Lazo Kelly reproducible documentado paso a paso, incluyendo
     comando `kora record-invocation` listo para llenar tras corrida.
   - `baseline_status: pendiente` — la corrida real es responsabilidad
     del operador en sesion interactiva nueva (decision deliberada de
     blast radius: no se ejecuta `claude -p` recursivo desde la sesion
     actual).

2. **Update fixture baseline existente**:
   `tests/fixtures/canarios/urgenciologo-baseline.md`.
   - Marca como **resuelta provisionalmente** la deuda explicita de
     "segundo canario con prompt adversarial".
   - La fineza de "exigir cita del URN completo" sigue como deuda
     viva (no bloqueante).

## Cambios NO materializados (por decision de scope)

- `AGENT.md` urgenciologo: NO modificado. La regla dura "No inventar
  cobertura" ya esta en el artefacto. Si la corrida adversarial detecta
  debilidad, ahi se ajusta.
- `autoria-spec` / `canario-spec` / `qa-spec`: NO tocadas. El patron
  ya esta cubierto por `canario-spec v1.1.0`.
- Toolchain: NO se agrego check `canario-*` automatico. Spec los
  declara manuales. Cascada queda para segunda iteracion si la cadencia
  de canarios crece.
- Subagent claude-code desplegado: NO redeployado (deploy-status: ok,
  hashes coinciden).
- Specs ni IR alterados: zero impacto en `check --strict` (30/30 verde
  antes y despues).

## Cierre Allan-Kelly

- **Output**: 1 fixture provisionado + 1 fixture actualizado +
  documentacion del lazo Kelly reproducible.
- **Outcome validado**: NO. El cierre real depende de que el operador
  ejecute la corrida interactiva. Esta sesion ataca la deuda de
  *infraestructura de validacion*, no la deuda de *valor validado*.
- **Lead time to validated value**: queda contado desde 2026-04-22
  (ultimo cierre) hasta la primera corrida del segundo canario.

> Honestidad epistemica: declarar como resuelto lo que es propuesta sin
> eval seria violacion de las reglas duras de la persona allan-kelly.
> El segundo canario esta provisionado, no validado.

## Siguiente paso operativo

1. **Operador FS, sesion interactiva nueva**: ejecutar el lazo Kelly
   documentado en
   `tests/fixtures/canarios/urgenciologo-adversarial-fuera-de-corpus.md`
   seccion "Lazo Kelly reproducible". Tiempo estimado: 5-10 min.
2. Tras la corrida: completar las 4 secciones pendientes del fixture
   (`baseline_captured_at`, `baseline_status`, `Evaluacion baseline`,
   `Output de referencia`).
3. Si cierra `pasa-con-deuda` o peor: registrar deuda y abrir tarea de
   ajuste sobre `AGENT.md` urgenciologo.
4. `python3 toolchain/kora record-invocation` con `--eval-result` igual
   al `baseline_status` final.

## Pendientes mas amplios (no para esta sesion)

- Replicar el patron canario para los otros 3 agentes productivos
  (`steipete`, `allan-kelly`, `salubrista`). Hoy ninguno tiene fixture
  canario.
- Cerrar el deploy stale de los 3 agentes mencionados (`deploy-status`
  reporta 3 stale).
- Definir cadencia de re-corrida de canarios (mensual? cada release?).
- Considerar promover los checks `canario-*` de `manual` a `automatic`
  en el toolchain una vez que existan >= 3 fixtures.

## Gates ejecutados

```
python3 toolchain/kora index               -> 558 artifacts (sin cambio)
python3 toolchain/kora check --strict      -> 30/30 verde
python3 toolchain/kora lint-md tests/...   -> 0 issues
```

`tests/` discover no se ejecuto: no hay test nuevo, los fixtures son
markdown y los checks de canario son manuales por spec. Si en el futuro
se agregan checks automaticos de canario, esta cohorte sera el primer
input.

## Referencias

- `urn:kora:kb:canario-spec` v1.1.0 (governance del instrumento).
- `urn:kora:kb:qa-spec` v1.0.0 (puente sigma -> qa_budget).
- `tests/fixtures/canarios/urgenciologo-baseline.md` (fixture de
  referencia, piloto 2026-04-22).
- `urn:salud:artefacto:urgenciologo` v3.0.0 (artefacto bajo prueba).
- Memoria `project_bok_medicina_emergencia` confirma que el corpus
  excluye pediatria — base para elegir el prompt adversarial.
