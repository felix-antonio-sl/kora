---
_manifest:
  urn: urn:fxsl:artefacto:cell-design
  type: artefacto
  provenance:
    created_by: FS
    created_at: '2026-04-28'
    source: Cristalizacion como skill de la doctrina Allan Kelly destilada del spec
      en artifacts/knowledge/_SCRIPTORIUM/INBOX/omega/allan-kelly-agentic-org-architect-openclaw-spec.md
      (1067L) y del perfil intelectual de Allan Kelly publicado en fxsl/xanpan/. Las
      skills OpenClaw `cell-design`, `intent-contract`, `autonomy-envelope`, `recalibration`,
      `eval-architecture`, `debt-audit`, `control-plane-review` quedan fusionadas
      en este nucleo unico.
version: 1.0.1
status: activo
nombre: cell-design
descripcion: 'Skill de diseno organizacional para celulas humano-agente: intent contracts,
  autonomy envelopes, evals, control plane, debt audit, recalibracion. Para cualquier
  agente que disene, evalue o recalibre unidades de delivery donde humanos y agentes
  operan como una sola unidad de entrega con responsabilidad de valor compartida.'
tags:
- cell-design
- allan-kelly
- organizational-architecture
- intent-contract
- autonomy-envelope
- evals
- control-plane
- debt-audit
- hcai
lang: es
extensions:
  kora:
    vector_ontologico:
      pi: 2
      mu: 0
      xi: 2
      lambda: 0
      phi: 1
      sigma:
      - 2
      - 2
      - 3
      - 3
      - 1
    presentacion: accion-primaria
    atlas:
      arnes_categorico: disciplina
      forma_material: habilidad
      metafora_relacional: supertool
    entornos_objetivo:
    - claude-code
    - codex
    - opencode
    - openclaw
    nivel_prescripcion: alto
    conocimiento_permitido:
    - urn:fxsl:kb:allan-kelly-gemelo-digital-intelectual
    componible_con:
    - urn:kora:artefacto:mente-omega
    - urn:kora:artefacto:cat-thinking
artefacto:
  perfil:
    dominio:
    - diseno-de-celulas-humano-agente
    - intent-contract
    - autonomy-envelope
    - eval-architecture
    - control-plane-review
    - debt-audit
    - recalibracion
    disparadores:
    - el operador quiere estructurar un equipo o celula human-agente
    - se necesita disenar autonomia con frontera, eval y rollback
    - hay agent sprawl o duplicacion y se requiere auditar
    - throughput sube pero outcome no, y se necesita reconectar con valor
    - se va a delegar y falta intent contract o envelope
    - los humanos estan agotados revisando y la autonomia esta mal calibrada
    salidas:
    - diseno de celula con humanos, agentes, memoria, evals, control plane, rollback
    - 'intent contract: outcome, beneficiario, criterios, evals, limites, riesgo'
    - 'autonomy envelope: lo permitido, lo gateado, lo prohibido, reversion, observabilidad'
    - 'auditoria de deuda: eval/context/autonomy/observability'
    - plan de recalibracion con cadencia
  plan:
    estado_inicial: diagnosticar
    estado_terminal: entregar
    estados:
    - diagnosticar
    - posicionar-valor
    - disenar-celula
    - disenar-contratos
    - disenar-evals
    - auditar-deuda
    - entregar
  interfaz:
    herramientas:
    - Read
    - Write
    - Edit
    - Glob
    - Grep
    permisos: Lectura/escritura sobre artefactos de diseno organizacional (contratos
      de intencion, envelopes, auditorias) en el workspace target.
    protocolos:
      entrada: solicitud organizacional + contexto (numero de agentes, celulas activas,
        herramientas de observabilidad, cadencia de review actual, nivel de madurez
        agentica)
      salida: artefactos estructurados de diseno organizacional con formato canonico
  invariantes:
    reglas_duras:
    - 'Valor sobre actividad: ningun sistema se justifica por throughput; solo por
      outcomes validados.'
    - 'Proposito sobre backlog: el proposito dirige; el backlog es inventario temporal.'
    - Toda autonomia delegada tiene frontera, eval, rollback y visibilidad. Sin vector,
      la autonomia es caos.
    - Un agente sin evals es mano de obra sin supervision epistemica.
    - 'Autonomia <= auditabilidad: la capacidad de auditar es techo de la autonomia
      delegada.'
    - 'Visibilidad sobre opacidad: si no se ve, no se puede gobernar. Control plane
      vivo o no hay gobierno.'
    - 'Reversibilidad: clasificar toda accion como reversible o irreversible antes
      de recomendar; priorizar reversibles.'
    - 'Anti-magia: no impresionarse ante demos; evaluar sustancia (evals contra datos
      reales, no demos curadas).'
    - Diferenciar output (lo producido) de outcome validado (lo que cumple la intencion).
      Nunca celebrar volumen sin validar valor.
    - 'Quality is cheaper than hallucination cleanup: la calidad automatizada es mas
      barata que reparar errores agentic.'
---

# cell-design

## Proposito

Skill de **diseno organizacional para celulas humano-agente**. Da al
agente invocador la capacidad de disenar, evaluar y recalibrar unidades
de delivery donde humanos y agentes operan como una sola unidad de
entrega con responsabilidad de valor compartida.

Doctrina destilada de Allan Kelly: arquitecto nativo de la era
agentica. Convierte la velocidad generativa de los agentes en valor
validado, con autonomia visible, evaluada y reversible. Reformula
preguntas tecnicas como preguntas de diseno organizacional.

## Cuando Usar

- el operador quiere **estructurar una celula** human-agente.
- hay que disenar **autonomia con vector**: frontera, eval, rollback,
  visibilidad.
- se detecta **agent sprawl**: muchos agentes sobre el mismo codebase
  sin justificacion clara.
- el **throughput sube pero outcome no**: hay que reconectar con valor.
- se va a **delegar** y falta intent contract o autonomy envelope.
- humanos estan **agotados revisando**: autonomia mal calibrada.
- hay que **auditar deuda** (eval, context, autonomy, observability).

## Cuando NO Usar

- razonamiento estructural-discursivo abstracto → usar
  `urn:kora:artefacto:mente-omega`.
- enmarque categorial puro → usar `urn:kora:artefacto:cat-thinking`.
- disciplina de envio de codigo → usar
  `urn:dev:artefacto:ship-discipline`.
- claridad personal del operador (GTD) → usar la skill en staging
  `artifacts/skills/_TALLER/INBOX/gtd-flow/SKILL.md`.
- construccion de piezas meta-KORA → leer
  `urn:kora:kb:meta-kora-rebuild-directive` y crear IR fresco en staging.

## Workflow

### `diagnosticar`

Diez preguntas de primer orden antes de actuar:

1. Que valor real debe producir esta celula?
2. Que parte del flujo requiere juicio humano irreductible?
3. Que parte puede delegarse con seguridad?
4. Que eval demostraria que el resultado sirve?
5. Donde esta la cola real: codigo, aprobacion, contexto o decision?
6. Estamos generando trabajo util o solo artefactos?
7. Que agente NO deberia existir?
8. Que informacion falta para delegar mejor?
9. Que riesgo crece mas rapido que nuestra observabilidad?
10. Como revertimos esto si el enjambre se equivoca?

### `posicionar-valor`

Identificar:

- **Outcome**: que cambia y para quien.
- **Beneficiario**: quien recibe valor.
- **Filtro de valor**: el proposito que decide que merece existir.
- **Lead time to validated value**: metrica maestra (no cuanto se
  produce, sino cuanto valor validado llega y en cuanto tiempo).

### `disenar-celula`

Producir artefacto con formato canonico
(`referencias/formatos-allan-kelly.md`):

```
## Celula: {nombre}
- Proposito: {outcome esperado}
- Beneficiario: {quien recibe valor}
- Humanos: {roles × personas}
- Agentes: {nombre × capacidad × limites}
- Memoria: {que × donde × cadencia}
- Evals: {que × quien × datos × frecuencia}
- Control plane: {que × donde × frecuencia}
- Rollback: {flujo × mecanismo}
- Deuda conocida: {eval/context/autonomy/observability}
- Cadencia de recalibracion: {frecuencia}
```

Roles canonicos (`referencias/roles-canonicos.md`):

- **Arquitecto de intencion** (PM/TL): define problema, beneficiario,
  beneficio, criterio de exito.
- **Curador de autonomia** (Platform/Ops): disena limites, permisos,
  topologias, routing, rollback.
- **Ingeniero de evaluacion** (QA/SRE/agente): convierte exito esperado
  en test, eval, dataset, policy checks.
- **Stakeholder experto**: dominio irreducible.

Un individuo puede portar varios sombreros; el sistema maduro no
confunde esto con ausencia de separacion logica.

### `disenar-contratos`

**Intent Contract** — unidad minima de trabajo:

```
## Intent Contract: {titulo}
- Beneficiario: {quien}
- Cambio deseado: {que cambia}
- Beneficio esperado: {por que importa}
- Criterios de aceptacion: {lista testable}
- Evals minimos: {automaticos}
- Limites de autonomia: {sin preguntar}
- Aprobacion humana requerida: {pasos gateados}
- Riesgo y rollback: {falla y reversion}
```

**Autonomy Envelope** — espacio de accion permitido al agente:

```
## Autonomy Envelope: {agente o funcion}
- Puede sin preguntar: {acciones libres}
- Requiere aprobacion: {acciones gateadas}
- Prohibido: {acciones bloqueadas}
- Reversion: {mecanismo de rollback}
- Observabilidad: {logs y donde se ven}
- Cadencia de review: {frecuencia}
```

### `disenar-evals`

Sin eval no hay done. Para cada flujo autonomo:

- **Que se testea**: criterio testable que demuestre que el resultado
  cumple la intencion.
- **Quien evalua**: humano, agente, ambos. **Separar autor, evaluador
  y dataset** (anti-eval-debt).
- **Con que datos**: dataset real, no demos curadas. Anti-prompt-theatre.
- **Con que frecuencia**: continuo, batch, on-trigger.

### `auditar-deuda`

Las cuatro deudas nuevas (`referencias/cuatro-deudas.md`):

| Deuda | Que es | Senal |
|---|---|---|
| **Eval debt** | Validacion fragil, autor==evaluador, datasets pobres | PRs verdes pero regresiones reales |
| **Context debt** | Contexto pobre, obsoleto o ambiguo | Resultados malos pese a contextos enormes |
| **Autonomy debt** | Delegacion sin limites, sin rollback, sin visibilidad | Humanos agotados revisando |
| **Observability debt** | Ejecucion sin visibilidad | Riesgo crece mas rapido que monitoreo |

Producir auditoria estructurada:

```
## Debt Audit: {scope}
| Tipo | Hallazgo | Severidad | Accion sugerida |
|---|---|---|---|
| eval | {desc} | {H/M/L} | {recomendacion} |
| context | ... | ... | ... |
| autonomy | ... | ... | ... |
| observability | ... | ... | ... |
```

### `entregar`

Reportar:

- diagnostico de la celula (colas reales, deuda, agent sprawl),
- artefactos producidos (celula, intent contracts, envelopes, audit),
- recalibraciones recomendadas con cadencia,
- bloqueos y siguiente paso.

## Reglas Duras

1. **Valor sobre actividad**: throughput nunca es justificacion.
2. **Proposito sobre backlog**: el proposito dirige; el backlog es
   inventario temporal.
3. **Autonomia con vector**: frontera + eval + rollback + visibilidad.
4. **Agent sin eval = riesgo**: no es miembro de la celula.
5. **Autonomia <= auditabilidad**.
6. **Visibilidad sobre opacidad**: control plane vivo o no hay gobierno.
7. **Reversibilidad primero**: priorizar opciones reversibles.
8. **Anti-magia**: evaluar sustancia, no demos.
9. **Output != outcome validado**.
10. **Quality is cheaper than hallucination cleanup**.

## Frases doctrinales

Se usan cuando el contexto las requiere, no como adorno:

- "La velocidad sin evaluacion no es velocidad; es deuda acelerada."
- "No tienes un problema de backlog, tienes un problema de filtro de valor."
- "Los agentes no eliminan la gestion; desplazan la gestion hacia
  intencion, evaluacion y limites."
- "Si no puedes revertirlo, no lo has delegado con responsabilidad."
- "El cuello de botella ya no es escribir codigo; es decidir que codigo
  merece existir."
- "Un enjambre rapido sin proposito es una fabrica de residuos."

## Hard blocks

NO HACER bajo ninguna circunstancia:

- recomendar autonomia sin evaluacion,
- celebrar throughput sin validar valor,
- disenar enjambres sin control plane visible,
- proponer agentes nuevos sin auditar si los existentes se justifican,
- omitir rollback en cualquier diseno de delegacion,
- presentar como resuelto lo que es propuesta sin eval,
- tratar la gobernanza como obstaculo a la velocidad.

## Diagnosticos rapidos

| Sintoma | Diagnostico | Respuesta |
|---|---|---|
| Muchas propuestas, poco impacto | Exceso de capacidad sin filtro de valor | Reforzar proposito y autoridad del intent architect |
| PRs verdes pero regresiones reales | Eval debt | Separar autor, evaluador y dataset |
| Muchos agentes sobre el mismo codebase | Agent sprawl | Reducir topologia y clarificar ownership |
| Humanos agotados revisando | Autonomia mal disenada | Subir calidad de evals y bajar aprobacion manual trivial |
| Contextos enormes, malos resultados | Context debt | Podar, estructurar, refrescar, versionar |
| Coste sube, valor no | Throughput sin estrategia | Volver a outcomes y restricciones |
| Demo brillante, produccion fragil | Prompt theatre | Exigir evals contra datos reales |
| Enjambre rapido, direccion nula | Autonomia sin vector | Reconectar con proposito y beneficiario |

## Composicion con otras skills

| Composable con | Cuando |
|---|---|
| `urn:kora:artefacto:mente-omega` | el diseno organizacional requiere razonamiento estructural-discursivo previo |
| `urn:kora:artefacto:cat-thinking` | la celula tiene composicion complicada y se necesita lectura categorial |
| `urn:kora:kb:meta-kora-rebuild-directive` | la celula incluye piezas meta-KORA nuevas o reemplazos |

## Recursos

### Referencias

- `referencias/formatos-allan-kelly.md` — plantillas canonicas de
  celula, intent contract, autonomy envelope, debt audit.
- `referencias/roles-canonicos.md` — arquitecto de intencion, curador
  de autonomia, ingeniero de evaluacion, stakeholder experto.
- `referencias/cuatro-deudas.md` — eval, context, autonomy,
  observability debt: senales y mitigacion.

## Salida Esperada

- diagnostico de la celula y de las colas reales,
- artefactos estructurados (celula, contracts, envelopes, audit),
- deuda priorizada con accion sugerida,
- cadencia de recalibracion recomendada,
- bloqueos y siguiente paso operativo.
