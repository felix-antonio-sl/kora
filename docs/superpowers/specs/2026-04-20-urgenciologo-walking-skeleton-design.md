# Fase 1 Design: Urgenciologo Walking Skeleton

## Intento

Encender la primera astilla vertical real de KORA usando un consumidor clinico correcto del corpus `med-emergencia`, no un agente generico de infraestructura.

La astilla debe demostrar este lazo cerrado:

`artifacts/knowledge/salud/med-emergencia/dolor-toracico.md`
-> corpus enlazado por `toc-body-of-knowledge.md`
-> agente productivo `salud/urgenciologo`
-> `python3 toolchain/kora transmute --target claude-code`
-> bundle Claude Code deployable
-> pregunta canario
-> cambio puntual en el nodo KB
-> nueva respuesta coherente con el cambio

## Scope

Incluido:

- coser el corpus `med-emergencia` en el tramo minimo `toc-body-of-knowledge -> me-dolor-toracico`
- crear una version productiva minima de `urgenciologo`
- permitir transmutacion a `claude-code` con output deployable en `_BUILD/claude-code/`
- definir y ejecutar un canario clinico dependiente de `me-dolor-toracico`
- registrar la invocacion canario en `docs/generated/invocations.jsonl`

Excluido:

- normalizacion completa del workspace legacy `artifacts/agents/_FRAGUA/INBOX/urgenciologo/`
- expansion a otros nodos del body of knowledge
- despliegue automatico a `~/.claude/agents/`
- OpenClaw, Codex, Gemini o segundo runtime
- freeze formal de specs o decisiones HITL D0.1/D0.2/D0.3

## Decision

Se promovio una opcion de "promocion minima productiva" por sobre:

- wrapper temporal sobre staging legacy
- normalizacion completa previa del agente

Razon:

- conserva el valor semantico correcto: el consumidor es clinico
- mantiene el blast radius acotado a la astilla
- evita convertir Fase 1 en un proyecto de remediacion general

## Arquitectura

### 1. Corpus minimo cableado

`artifacts/knowledge/salud/med-emergencia/toc-body-of-knowledge.md` pasa a ser SSOT estructural del subconjunto probado en Fase 1.

Debe declarar una relacion explicita hacia `urn:salud:kb:me-dolor-toracico`. No basta con que ambos archivos existan bajo el mismo directorio. El objetivo es que el corpus probado deje de estar semanticamente suelto.

`artifacts/knowledge/salud/med-emergencia/dolor-toracico.md` sigue siendo el nodo clinico foco. No se reescribe doctrinalmente salvo que se necesite una edicion puntual para el canario.

### 2. Consumidor clinico productivo

Se crea `artifacts/agents/salud/urgenciologo/AGENT.md` como artefacto productivo actual.

No se migra todo el agente legacy. Se absorbe solo el nucleo necesario para la astilla:

- identidad y descripcion clinica
- FSM minima operable
- `entornos_objetivo: [claude-code]`
- `conocimiento_permitido` minimo
- cualquier campo estrictamente requerido por `serialization/autoria-spec.md` y `serialization/schemas/kora-artefacto.json`

El agente legacy en `_FRAGUA/INBOX/urgenciologo/` queda como referencia fuente, no como artefacto de ejecucion de Fase 1.

### 3. Knowledge contract minimo

La version productiva de `urgenciologo` declara solo este KB minimo:

- `urn:salud:kb:med-emergencia`
- `urn:salud:kb:me-toc-body-of-knowledge`
- `urn:salud:kb:me-razonamiento-clinico`
- `urn:salud:kb:me-evaluacion-primaria`
- `urn:salud:kb:me-dolor-toracico`

Esto reduce superficie y hace que el canario sea interpretable. Si la respuesta cambia, sabremos por que.

### 4. Transmutacion a Claude Code

`toolchain/kora_lib/transmute.py` hoy prepara `_transmutation.yml` y el directorio `_BUILD/claude-code/`, pero la astilla necesita un output Claude Code deployable dentro de ese directorio.

El diseno exige agregar el tramo faltante:

- bundle markdown final para Claude Code dentro de `artifacts/agents/salud/urgenciologo/_BUILD/claude-code/`
- metadata minima suficiente para deploy manual
- preservacion visible de `source_urn`, `source_hash` y `timestamp`

No se exige deploy automatico. En Fase 1 basta con que el output sea coherente, reproducible y manualmente instalable.

## Flujo

1. Resolver y validar URNs del corpus minimo.
2. Coser TOC y nodo `me-dolor-toracico`.
3. Crear `salud/urgenciologo` productivo minimo.
4. Validar repo:
   - `python3 toolchain/kora index`
   - `python3 toolchain/kora check --strict`
   - tests focalizados
5. Transmutar:
   - `python3 toolchain/kora transmute --target claude-code --agent salud/urgenciologo`
6. Deploy manual del bundle Claude a runtime local.
7. Ejecutar pregunta canario y registrar baseline.
8. Editar una frase puntual en `dolor-toracico.md`.
9. Repetir index -> transmute -> deploy -> pregunta canario.
10. Confirmar que la respuesta cambie de forma coherente con la edicion.

## Canario

El canario debe cumplir estas propiedades:

- depende de un hecho explicito y visible en `me-dolor-toracico`
- no exige inferencia medica compleja
- no depende de memoria previa ni de otros nodos del corpus
- permite verificar cambio semantico despues de editar una sola frase

Se recomienda una pregunta cerrada sobre foco doctrinal del documento, no sobre manejo clinico prescriptivo fino.

Canario fijado para Fase 1:

- pregunta: "Segun el nodo `me-dolor-toracico`, en que foco clinico se centra este material?"
- baseline esperado: el agente responde que el foco se centra en sindrome coronario agudo, porque eso esta declarado explicitamente en el nodo fuente
- edit de prueba: reemplazar esa frase foco por una variante controlada y semanticamente distinta, retransmutar y verificar cambio de respuesta

## Error Handling

- si `urgenciologo` productivo no valida contra autoria schema, se corrige el shape antes de seguir
- si el TOC no resuelve el nodo `me-dolor-toracico`, se aborta la transmutacion del skeleton
- si `transmute` no produce bundle Claude deployable, no se simula exito con `_transmutation.yml` solamente
- si el canario no cambia tras editar el nodo KB, la fase falla aunque el repo este verde
- si la edicion puntual del nodo produce efectos ambiguos, se restaura y se redefine una frase canario mas limpia

## Testing

Minimo requerido:

- tests focalizados para la extension de `transmute` a `claude-code`
- tests focalizados para cualquier helper nuevo de bundle/deploy metadata
- `python3 toolchain/kora check --strict`
- `python3 -m unittest discover -s tests`

Verificacion funcional obligatoria:

- bundle Claude generado en `_BUILD/claude-code/`
- deploy manual exitoso
- baseline canario registrado
- segunda corrida canario cambia despues de editar `dolor-toracico.md`

## Exit Criteria

La astilla cierra solo si todo esto es verdadero:

- existe `artifacts/agents/salud/urgenciologo/AGENT.md` productivo y validable
- `toc-body-of-knowledge.md` enlaza explicitamente `urn:salud:kb:me-dolor-toracico`
- `python3 toolchain/kora transmute --target claude-code --agent salud/urgenciologo` produce bundle deployable
- el bundle muestra `source_urn`, `source_hash` y `timestamp`
- una misma pregunta canario cambia de forma coherente tras editar una frase puntual en `dolor-toracico.md`
- la corrida queda registrada en `docs/generated/invocations.jsonl`

## Riesgos

- el staging legacy de `urgenciologo` puede contener mas doctrina de la que conviene absorber en Fase 1
- el runtime Claude puede introducir ruido si el prompt final queda demasiado abierto
- el canario puede resultar demasiado indirecto y generar falsos negativos
- el corpus `med-emergencia` hoy esta incompletamente cosido, por lo que conviene limitar alcance al tramo probado

## Siguiente paso

Si este diseno queda aprobado, el siguiente artefacto debe ser un plan de implementacion que divida el trabajo en:

- corpus wiring
- promocion minima de `urgenciologo`
- clausura de transmutacion Claude
- canario y registro
