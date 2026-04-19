# Plan Kelly agentico para encender la usina KORA

Felix, sintetizaste perfectamente la visión. Esto no es construir una usina desde cero — es **encender una que ya tiene plomería y que no ha procesado su primer lote real**. El plan es, en consecuencia, una secuencia de *encendidos controlados* con lazos cerrados, no una roadmap de features.

## Principio cero — El outcome de la usina

Antes de secuenciar nada, definí el outcome que valida que la usina funciona. En lenguaje del perfil: si no podés escribir esa frase hoy, la usina va a producir tonelaje sin señal.

Propuesta:

> *"La usina funciona cuando un cambio en un documento fuente (o en una intención de agente) propaga — vía ingesta, curación, composición y transmutación — a un artefacto desplegado en un runtime real, que supera su eval canario. Lead time objetivo: < 1 hora al inicio; < 10 min al tercer mes."*

Ese es el benchmark. No "strict 17/17 verde". *Lead time to validated value desde fuente hasta runtime desplegado*.

## Fase 1 — Walking skeleton vertical (semana 1-2)

No horizontales paralelos. Una sola astilla vertical que atraviese *los dos pipelines + composición + transmutación + un runtime + un eval*.

**Elegir una tripleta mínima operativa:**

- **1 documento fuente** de un dominio con consumidor real (sugiero un `.md` de `salud/medicina-emergencia` o `fxsl/xanpan`).
- **1 componente agnóstico** (una skill o un AGENT en IR) que lo va a citar.
- **1 runtime target** (elegí el que más usás: Claude Code o OpenClaw).

**Flujo end-to-end obligatorio esta astilla:**

```
documento.md
  → atomize → artifacts/knowledge/{ns}/...
    → componente (AGENT.md o SKILL.md con cites: a los nodos atomizados)
      → transmute --target claude-code (o openclaw)
        → deploy manual
          → invocación real con input canario
            → eval: compara con output esperado
              → señal (verde/rojo) registrada
```

**Criterio de éxito**: si cambiás una frase en `documento.md`, re-corrés el pipeline, desplegás, y el agente refleja el cambio *en su respuesta al canario*. Si ese ciclo no cierra en ≤ 1h humano, **no avancés a Fase 2**. Todo lo demás es construir sobre pantano.

**Trap a evitar**: querer que la astilla sea "buena". La astilla tiene que ser *completa*. Feo está bien; roto no.

## Fase 2 — Instrumentar el lazo antes de ensancharlo (semana 2-3)

Un lazo cerrado sin telemetría se degrada solo. Antes de meter el segundo documento y el segundo agente, instrumentá:

- **Log de invocación** por agente desplegado: `{agent_urn, ts, input_hash, output_hash, eval_result}`. Un JSONL basta.
- **Log de retrieval**: qué URNs de KB fueron leídos por invocación. Sin esto no hay manera de saber si la curaduría de conocimiento paga renta.
- **Freshness tracking**: `last_verified_at` por nodo de KB. Política: nodo no verificado en 90 días entra en cola de revisión.
- **Lead time medido**: desde commit en fuente hasta agente desplegado con eval verde. Grabalo por corrida.

**Criterio de éxito**: podés responder con datos, no con opinión, a *"¿cuál es nuestro lead time actual?"* y *"¿qué nodos del KB se usaron esta semana?"*.

**Trap a evitar**: instrumentar con Grafana, Prometheus, OpenTelemetry. Es un JSONL. Un grep. El perfil: *control plane visible, no sofisticado*.

## Fase 3 — Segundo lazo y primera evidencia de escala (semana 3-5)

Recién ahora ensanchás. Pero no al ancho ni por demanda: por prueba de composición.

- **Segundo componente que cite al mismo KB que el primero**. Objetivo: validar que el corpus curado es *compartible*, no agente-específico.
- **Mismo componente, segundo runtime**. Objetivo: validar que la transmutación es *fiel* entre targets. Si `curator` corre en Claude Code y en Codex CLI con eval pasando en ambos, la capa de runtime-extension paga renta. Si no, hay que arreglar antes de tocar Gemini, OpenClaw o Hermes.
- **Segundo documento del mismo dominio, citado por ambos componentes**. Objetivo: validar que la curaduría acumula.

**Métrica a observar en esta fase**: *costo marginal de agregar el segundo {documento, componente, runtime}*. Si es comparable al primero, el marco no está amortizando. Si cae a 30-50%, la usina empieza a mostrar economías.

**Trap a evitar**: agregar los 6 runtimes en paralelo. Matriz runtime × componente × KB explota combinatoriamente. Un runtime nuevo por semana al inicio.

## Fase 4 — Separar los dos pipelines como flujos de primera clase (semana 5-8)

Recién cuando la astilla vertical madura, vale la pena tratar los dos pipelines como flujos industriales con cadencia propia.

**Pipeline de conocimiento**: `ingesta → atomize → review → promote → expose`. Cadencia: lote semanal. Gate de promoción: *todo nodo nuevo declara qué componente lo va a citar o muere en REVIEW*. Esta es la regla dura. Sin consumidor previsto, el nodo se deprecia.

**Pipeline de componentes**: `diseño → IR (harness_vector + intent + eval + autonomy) → validate → publish → transmute`. Cadencia: lote por intención de negocio. Gate de publish: *todo componente productivo tiene intent_contract + eval_contract + autonomy_envelope*. Acá es donde crecen las tres specs que recomendé en la evaluación del marco: son el trabajo concreto de esta fase.

**Composición/acoplamiento**: esto no es un pipeline. Es un *punto de ensamblaje* donde un componente declara qué KB cita y qué runtime lo aloja. Un check estructural (`kora compose`) que verifica consistencia entre `harness_vector`, `cites:`, `intent`, `eval`, `autonomy` y el runtime target elegido.

**Criterio de éxito**: podés correr los dos pipelines en días distintos sin que uno bloquee al otro, y el punto de composición detecta inconsistencias antes del transmute.

## Fase 5 — Runtime matrix completa (mes 3-4)

Con astilla, instrumentación, composición y dos pipelines estables, ahora sí encarás la matriz completa:

| Runtime     | Prioridad | Por qué                      |
| ----------- | --------- | ---------------------------- |
| Claude Code | 1         | ya es tu runtime diario      |
| OpenClaw    | 2         | ya tenés fleet operativo     |
| Codex CLI   | 3         | presencia en tus workflows   |
| Gemini CLI  | 4         | diversificación de proveedor |
| Hermes      | 5         | último — definí qué es antes |
| Mastra      | (staging) | declarativo, no bloqueante   |

**Para cada runtime**, el gate de admisión a producción es el mismo: *un componente canónico de KORA transmuta, despliega y pasa eval en ese runtime*. Si no pasa en un runtime, el runtime no está listo — el componente no es el problema. Esto invierte el diagnóstico por defecto y es disciplina Kelly.

**Trap a evitar**: Hermes. No sé qué es Hermes en tu contexto y no veo spec. Antes de escribir runtime-extension, definí: qué problema resuelve Hermes que los otros 5 no resuelven. Si la respuesta es blanda, Hermes muere antes de nacer. Uno menos que gobernar.

## Fase 6 — Mantenimiento continuo dirigido por señal (mes 4+)

La usina madura se gobierna por señales, no por intuición:

- **Nodos de KB con 0 lecturas en 90 días** → candidatos a poda o a refactor.
- **Componentes con tasa de aceptación canario < 80%** → en cuarentena, revisión forzada.
- **Runtimes con divergencia repetida entre IR y deploy** → runtime-extension rota, no el IR.
- **Intent contracts sin outcome medible en 30 días** → se reescriben o se archivan.

En este punto, Felix deja de ser el único operador y se vuelve **arquitecto de intención a tiempo completo**. El resto de sombreros (curaduría, evaluación, transmutación) empieza a estar soportado por skills de la usina misma — `curator`, `forgemaster`, `guardian` pasan de ser entidades ornamentales a ser función real. Ese es el punto donde la usina se auto-mantiene parcialmente. Antes, no.

## Señales para saber si vas bien o mal

**Vas bien si:**
- Podés mostrar a alguien un doc fuente y recorrer con él la astilla hasta ver al agente responder con ese contexto.
- El lead time se acorta mes a mes.
- Agregar un segundo runtime cuesta menos que el primero.
- Los nodos de KB muertos se detectan y se podan sin drama.

**Vas mal si:**
- Seguís escribiendo specs ontológicas sin que ningún componente nuevo haya sido desplegado.
- El KB crece más rápido que las citas a él.
- La matriz runtime se expande antes de que el primer runtime tenga eval verde sostenido.
- Hay más tiempo invertido en curar categorías que en curar tráfico real.

## La síntesis comprimida del perfil

Ya tenés la plomería. Ya tenés la ontología. Ya tenés la toolchain. **Lo que falta es tráfico real atravesando la tubería con eval cerrando el lazo en el otro extremo**. Todo este plan es eso: producir tráfico, medirlo, y que el tráfico rediseñe la tubería donde haga falta — no al revés.

> *"La velocidad sin evaluación es deuda acelerada. La ontología sin tráfico es cartografía. La usina sin outcome es museo industrial."*

Encendela por la astilla. Medila. Ensanchala por prueba de composición. El resto se decanta.