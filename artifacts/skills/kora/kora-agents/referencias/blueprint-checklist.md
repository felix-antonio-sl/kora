# Blueprint checklist

Mapa operativo para construir y verificar el blueprint de un agente
KORA conforme a `agent-skill-construction-spec §3` + `autoria-spec §5`
+ `harness-spec §4`.

## Fases A→H del metodo

### Fase A — Intake

Capturar requerimientos minimos:

| Campo | Pregunta | Salida en IR |
| --- | --- | --- |
| identidad | que rol cumple y para quien | `perfil.dominio`, `descripcion`, `tags` |
| objetivo | que resultado observable entrega | `perfil.salidas`, `plan.estado_terminal` |
| forma | subagente, agente o plataforma | `atlas.forma_material` |
| conocimiento | que URNs puede consultar | `conocimiento_permitido` |
| interaccion | que entradas, herramientas, permisos | `interfaz` |
| estado | que memoria o materia necesita | `vector_ontologico.mu`, `contexto.memoria_config` |
| riesgo | que puede salir mal y como se mitiga | `invariantes`, `qa_budget`, `risk_register` |

Campos no aplicables se omiten o declaran vacios; **nunca** placeholder
decorativo.

### Fase B — Enmarque categorial

Traducir intake a vector PMI x LFS:

| Eje | Lectura |
| --- | --- |
| Π | que plan ejecuta (free monad) |
| Μ | sobre que materia corre (cofree comonad) |
| Ξ | como interactua (lente, protocolo, operad) |
| Λ | a que escala opera |
| Φ | como se acopla al humano |
| Σ | compromisos eticos (vector enriched) |

### Fase C — Forma material

Tabla rapida de dominios:

| Forma | Π | Μ | Ξ | Λ | Φ |
| --- | --- | --- | --- | --- | --- |
| `subagente` | {1,2,3} | {0,1,2} | {1,2,3} | {0,1} | {1,2} |
| `agente-propiamente-tal` | {2,3} | {2,3} | {2,3,4} | {0,1,2} | {1,2,3} |
| `agente-plataforma` | {2,3} | 3 | {3,4} | {1,2,3} | {1,2,3} |

Regla: la forma material **mas baja** que satisface el objetivo.

### Fase D — Contrato de conocimiento

- `conocimiento_permitido` con URNs resolubles, jamas paths duros.
- Lista vacia o omitida solo si la spec lo permite y si realmente no
  hay KB.
- Sin retrieval implicito por similitud cuando el contrato exige
  fuente gobernada.

### Fase E — Nucleo conductual

Cuando `verificacion_coalgebraica: true`, declarar `artefacto.plan.fsm`
con:

- `inicial` y `terminales` no vacios.
- `transiciones` apuntan a estados existentes.
- todo estado no terminal alcanza un terminal en finitos pasos.
- ciclos con salida finita.
- `invariantes.sub_coalgebra_segura` cierra bajo transiciones cuando se
  declara.

### Fase F — Interfaz y capacidades

Declarar:

- entradas esperadas,
- salidas emitidas,
- `herramientas` y `permisos`,
- limites de autoridad,
- handoffs cuando Ξ≥3,
- `interfaz.api_observable` cuando `componible_con` no esta vacio.

Las capacidades **DEBEN** vivir en `interfaz`, `extensions.{runtime}` o
en la runtime-extension correspondiente; **nunca** asumirse por
ambiente.

### Fase G — Invariantes, seguridad y riesgo

- `invariantes.reglas_duras` suficientes para impedir drift de
  objetivo (no slogans).
- `invariantes.compromisos_eticos` obligatorios en
  `agente-propiamente-tal` y `agente-plataforma`.
- `contexto.qa_budget` y `contexto.risk_register` cuando el riesgo no es
  trivial.
- Criterio de verificacion runtime cuando habra transmutacion.

### Fase H — Materializacion

| Forma | Fuente primaria | Fibras |
| --- | --- | --- |
| `subagente` | `artifacts/agents/{ns}/{id}/AGENT.md` | `memoria/` si Μ≥2, `_BUILD/` derivado |
| `agente-propiamente-tal` | `artifacts/agents/{ns}/{id}/AGENT.md` | `memoria/`, `skills/`, recursos, `_BUILD/`, `_transmutation.yml` |
| `agente-plataforma` | `artifacts/agents/{ns}/{id}/AGENT.md` + extension | materia ambiental |

Body explica solo lo que ayuda a operar el artefacto; detalle voluminoso
va a `referencias/` o `recursos/`.

## Leyes inter-eje (harness-spec §4.1)

Vector valido **DEBE** cumplir:

1. Π≥3 ⟹ Μ≥1 (recursion necesita estado).
2. Ξ=4 ⟹ Λ≥1 (operad dinamica requiere multi-actor).
3. Φ≥2 ⟹ Μ≥1 (acoplamiento observable necesita estado).
4. Σ.accountability ≥ 2 ⟹ Σ.transparency ≥ 2.
5. Λ=3 ⟹ Σ.i ≥ 2 ∀i.

Vector que viola estas leyes es mal-formado y debe rechazarse.

## Tabla de checks aplicables

Por forma material, ademas de los checks universales del envelope:

| Check | `subagente` | `agente-propiamente-tal` | `agente-plataforma` |
| --- | --- | --- | --- |
| `vector-ontologico-presente` | si | si | si |
| `vector-rango-valido` | si | si | si |
| `leyes-inter-eje` | si | si | si |
| `forma-material-declarada` | si | si | si |
| `dominio-forma-material` | si | si | si |
| `arnes-compatible-con-forma` | si | si | si |
| `shape-condicional` | si | si | si |
| `topologia-valida` | si | si | si |
| `memoria-declarada` (si Μ≥2) | si | si | obligatorio |
| `compromisos-eticos` | opcional | obligatorio | obligatorio |
| `extension-runtime-plataforma` | no | no | obligatorio |
| `coalgebra-conformance` (si plan.fsm) | si | si | si |
| `fidelidad-mastra` | si | si | si |
| `entornos-objetivo-soportan` | si | si | si |
| `construction-source-primary` | si | si | si |
| `construction-vector-fit` | si | si | si |
| `construction-knowledge-explicit` | si | si | si |
| `construction-fsm-valid` | si | si | si |
| `construction-interface-typed` | si | si | si |
| `construction-risk-declared` | si | si | si |
| `construction-runtime-separation` | si | si | si |
| `construction-categorical-minimality` | si | si | si |
| `construction-authoring-shape` | si | si | si |

## Comandos de verificacion

```bash
python3 toolchain/kora index
python3 toolchain/kora check --strict
python3 toolchain/kora validate --profile strict --cohort meta-kora
python3 toolchain/kora kb-graph --json --orphans
python3 toolchain/kora transmute --target mastra --agent {ns}/{nombre} --dry-run
python3 toolchain/kora roundtrip-check
python3 -m unittest discover -s tests   # cuando se toca toolchain, specs o behavior compartido
```

## Antipatrones a rechazar

| Antipatron | Falla | Correccion |
| --- | --- | --- |
| runtime-first | el output target suplanta IR | crear `AGENT.md` y transmutar despues |
| envelope transplantado | se copia un envelope externo como shape KORA | traducir a `autoria-spec` |
| KB por path | knowledge no resoluble por URN | usar `conocimiento_permitido` |
| vector decorativo | PMI x LFS no deriva del comportamiento | rehacer enmarque categorial |
| agente sin materia | declara agente donde basta skill | bajar forma material o revisar Μ |
| guardrail retorico | seguridad sin regla verificable | escribir regla dura, qa o riesgo |
| over-formalizacion | 2-cat / operad sin necesidad | volver a la lectura mas debil suficiente |

## Severidad y outcome

| Severidad de hallazgos | Outcome sugerido |
| --- | --- |
| sin hallazgos | `ready` |
| solo media o baja, no bloqueantes | `needs_repair` con deuda residual declarada |
| al menos una alta | `needs_repair` o `processing` segun disponibilidad del operador |
| dependencia faltante o decision editorial pendiente | `blocked` |
