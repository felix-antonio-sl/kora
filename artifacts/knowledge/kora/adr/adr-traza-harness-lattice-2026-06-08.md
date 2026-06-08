---
_manifest:
  urn: "urn:kora:kb:adr-traza-harness-lattice-2026-06-08"
  provenance:
    created_by: "Claude"
    created_at: "2026-06-08"
    source: "Frente 2 auditoria categorial KORA. Decision HITL operador: B + C-debil (2026-06-08) y aceptacion de esta ADR (2026-06-09) autorizando la traza puntual de harness-spec al lattice PMI×LFS formalizado."
  version: "1.0.0"
  status: publicado
  tags: [adr, harness, freeze, formal-layer, traces-to, frente-2]
  lang: es
extensions:
  kora:
    family: note
    adr:
      contexto: "harness-spec esta en freeze parcial (gobernanza §8.3): solo fixes puntuales de verdad; prohibidas expansiones doctrinales, nuevos ejes y rediseno. El Frente 2 de la auditoria detecto que harness fundaba PMI×LFS solo con cites a icas-* (corpus auxiliar NO normativo), sin preimagen en la Formal Layer oficial. El doc 09-harness-lattice (urn:kora:kb:cat-harness-lattice) ya absorbio la estructura de orden (poset producto + 5 leyes como sublattice W) a la Formal Layer, y declara la relacion con la F-coalgebra como problema abierto. Falta el acto que toca harness: declarar 'Traces to: urn:kora:kb:cat-harness-lattice' para que el guardian formal-trace-discipline pueda verificar el fundamento. Ese acto edita una spec congelada y, por el handoff del Frente 2, requiere ADR explicita."
      alternativas:
        - "A1 No trazar (status quo post-doc-09): el fundamento existe en doc 09 pero harness no lo referencia; el drift sigue invisible al toolchain"
        - "A2 Trazar como fix puntual SIN ADR, apelando a regla 1 del freeze: salta el registro que el handoff exige"
        - "A3 Trazar bajo esta ADR, clasificando el acto como correccion de verdad (no expansion doctrinal) (elegida)"
        - "A4 Levantar el freeze parcial de harness por completo: desproporcionado, el freeze protege contra rediseno que aqui no ocurre"
      factorizacion_elegida: "decision = trazar_a_cat_harness_lattice ∘ clasificar_como_correccion_de_verdad ∘ restringir_alcance_a_una_linea"
      consecuencias:
        - "harness-spec gana fundamento formal verificable; formal-trace-discipline puede confirmar que traza a la Formal Layer oficial"
        - "el drift de fundamento del Frente 2 queda cerrado de forma verificable por el toolchain (no solo en prosa)"
        - "harness-spec bump 1.1.0 → 1.1.1 (patch: correccion de verdad, no rediseno)"
        - "spec-procedure-coherence debe seguir verde tras el bump"
        - "NO se levanta el freeze general; esta ADR autoriza un unico acto puntual"
        - "precedente: trazar una spec en freeze a un fundamento ya formalizado es correccion admisible bajo §8.3 regla 1"
      estado: aceptada
relations:
  cites:
    - "urn:kora:kb:gobernanza"
    - "urn:kora:kb:harness-spec"
    - "urn:kora:kb:cat-harness-lattice"
    - "urn:kora:kb:cat-agent-coalgebra"
---

# ADR — Traza formal de harness-spec al lattice PMI×LFS

## Contexto

`harness-spec` esta en **freeze parcial** (gobernanza §8.3). Reglas vigentes:

1. Solo se permiten correcciones de verdad necesarias para sostener artefactos
   productivos, checks o transmutaciones.
2. No se permiten expansiones doctrinales, nuevos regimenes ni nuevos ejes.
3. Todo cambio se justifica como fix puntual, no como rediseno conceptual.

El **Frente 2** de la auditoria categorial (informe 2026-06-07) hallo que la
constitucion ontologica fundaba el espacio PMI×LFS unicamente con
`relations.cites` a `icas-*` — corpus auxiliar declarado **no
normativo** por CLAUDE.md — sin preimagen en la Formal Layer oficial
(`categorical-foundations/`).

La decision HITL del operador (**B + C-debil**) se ejecuto el 2026-06-08 **sin
tocar harness**:

- `09-harness-lattice.md` (`urn:kora:kb:cat-harness-lattice`) formaliza el poset
  producto PMI×LFS y prueba que las 5 leyes inter-eje recortan un sublattice
  acotado `W` (el contrato real de `vector-laws`); §5 declara que **no hay
  morfismo demostrado** poset↔F-coalgebra y lo deja como problema abierto.
- `08-fxsl-cat-bridge.md` §7 registra la absorcion parcial honesta del corpus
  ICAS.

Quedaba **un solo acto pendiente**, y es el unico que toca la spec congelada:
declarar en harness-spec una linea de traza formal a `cat-harness-lattice`, para
que el guardian `formal-trace-discipline` pueda verificar el fundamento. El
handoff del Frente 2 exige ADR explicita para ese acto. Esta ADR es ese
registro.

**Pregunta de gobernanza:** anadir un `Traces to:` a un fundamento que formaliza
lo que harness **ya dice** (las 5 leyes ya viven en §4.1), ¿es "expansion
doctrinal" (prohibida) o "correccion de verdad necesaria para sostener checks"
(regla 1, permitida)?

## Alternativas consideradas

### A1. No trazar (status quo post-doc-09)

El fundamento de orden ya existe en doc 09, pero harness no lo referencia. El
drift queda cerrado en prosa pero **invisible al toolchain**: `formal-trace-discipline`
no tiene nada que verificar porque harness sigue sin `Traces to:`.

**Por que NO**: deja a medias el cierre verificable; el valor que el check puede
garantizar es justamente la traza.

### A2. Trazar como fix puntual sin ADR

Apelar directamente a §8.3 regla 1 y anadir la traza sin registro formal.

**Por que NO**: el handoff del Frente 2 exige ADR explicita; saltarse el
registro respeta la letra pero no el espiritu del freeze (la decision sobre una
spec congelada debe quedar trazada).

### A3. Trazar bajo esta ADR como correccion de verdad — ELEGIDA

Anadir la traza, registrando aqui que el acto es **correccion de verdad**, no
expansion doctrinal: la traza apunta a un doc que formaliza lo que harness ya
afirma; no introduce ejes, regimenes ni doctrina nueva.

**Por que SI**:
- Cierra el drift de forma **verificable** (no solo editorial).
- Es el acto **minimo** suficiente (una linea).
- Respeta el freeze: no toca ejes ni leyes ni rediseña; clasifica honestamente
  el cambio como fix.
- Deja precedente limpio para futuros fundamentos formalizados.

### A4. Levantar el freeze parcial de harness por completo

**Por que NO**: desproporcionado. El freeze protege contra rediseno doctrinal,
que aqui **no ocurre**. Levantarlo para una linea de traza es exceso.

## Decision

**Factorizacion:** `decision = trazar_a_cat_harness_lattice ∘ clasificar_como_correccion_de_verdad ∘ restringir_alcance_a_una_linea`

- `f` (restriccion operativa): §8.3 permite solo fixes puntuales de verdad. El
  cambio se limita a la traza; los 6 ejes, las 5 leyes y el texto quedan
  intactos.
- `g` (morfismo elegido): A3 — trazar bajo ADR explicita, clasificado como
  correccion de verdad.

### Cambio aplicado a `harness-spec.md`

Acto unico y minimo: se anadio en §4 (Leyes categoricas), bajo el parrafo del
producto reticular, la linea de traza formal:

```
Traces to: `urn:kora:kb:cat-harness-lattice` §2-§3 (...)
```

apuntando a `urn:kora:kb:cat-harness-lattice`, con nota de que la relacion con la
F-coalgebra de agente es problema abierto (ibid. §5).

**Bump:** `harness-spec` 1.1.0 → **1.1.1** (patch — correccion de verdad), version
de manifest y H1 alineados.

### Lo que NO cambia

- Los 6 ejes PMI×LFS, sus niveles y las 5 leyes inter-eje.
- Los `relations.cites` a `icas-*` (siguen como origen conceptual /
  Rationale).
- Cualquier semantica operativa, vector o transmutacion.

## Consecuencias

### Positivas

- El drift de fundamento del Frente 2 queda cerrado de forma **verificable por
  el toolchain**, no solo en prosa.
- `formal-trace-discipline` pasa a confirmar que la constitucion ontologica
  traza a la Formal Layer oficial.
- Precedente honesto: una spec en freeze puede ganar traza a un fundamento ya
  formalizado sin violar el freeze.

### Negativas / riesgos

- Toca una spec congelada (mitigado: una linea, clasificada como fix, bajo esta
  ADR).
- `spec-procedure-coherence` debe seguir verde tras el bump de version
  (verificado en gates).
- Si en el futuro se demuestra el morfismo poset↔coalgebra (doc 09 §5.5), eso si
  seria doctrina nueva y requeriria **otra** ADR; esta no lo autoriza.

## Trazabilidad

- Depende del trabajo ya ejecutado: `urn:kora:kb:cat-harness-lattice` (doc 09) y
  la extension del bridge 08.
- `cites` a `urn:kora:kb:gobernanza` (§8.3), `urn:kora:kb:harness-spec` (objeto
  del cambio) y `urn:kora:kb:cat-agent-coalgebra` (la coalgebra del problema
  abierto).
- No `supersedes` ni `refines` ninguna ADR previa: es un cierre puntual, no un
  cambio de doctrina.

## Estado

`aceptada` — aceptada por HITL del operador el 2026-06-09; la traza en harness
(bump 1.1.1) se aplica en el mismo commit que publica esta ADR.
