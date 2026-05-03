---
_manifest:
  urn: "urn:kora:kb:canario-spec"
  provenance:
    created_by: "FS"
    created_at: "2026-04-22"
    source: "Cierre del piloto urgenciologo/claude-code el 2026-04-22; formaliza el patron de canario vivido para que pueda escalarse sin idiosincrasias por artefacto. v1.1 aclara que canario es evidencia runtime condicional, no cohort productivo ni gate de construccion."
version: "1.1.0"
status: publicado
tags: [spec, canario, verificacion-runtime, gate, propagacion, trazabilidad]
lang: es
extensions:
  kora:
    family: spec
relations:
  depends:
    - "urn:kora:kb:gobernanza"
    - "urn:kora:kb:harness-spec"
    - "urn:kora:kb:qa-spec"
    - "urn:kora:kb:transmutation-spec"
  cites:
    - "urn:kora:kb:runtime-spec-md"
    - "urn:kora:kb:autoria-spec"
---

# KORA/Canario-Spec v1.1.0

## 1. Definicion

Un **canario** es un artefacto ejecutable y reproducible que verifica que un
artefacto agentico proyectado a un runtime concreto (i) respeta su contrato
de knowledge, (ii) aplica su razonamiento declarado, (iii) preserva la
propagacion de cambios desde el source hasta el punto de consumo, y
(iv) deja evidencia auditable de todo lo anterior.

Un canario **NO** es una prueba unitaria ni un linter. Es una prueba de
integracion end-to-end que atraviesa el ciclo completo
`source → transmute → deploy → invoke → trace` para un par concreto
`(artefacto, runtime)`.

Decision constitucional de esta spec:

> Un runtime **NO DEBE** declararse endurecido para un artefacto agentico
> sin al menos un canario que haya cerrado en `pasa-estricto` y cuyo
> artefacto, knowledge contract y trace esten documentados como fixture
> reproducible.

Rationale: sin canario ejecutable, la calidad declarada en `qa-spec` es
una promesa unilateral. El canario es el instrumento minimo que convierte
compromiso ontologico en evidencia runtime.

## 2. Definiciones

| Termino | Definicion |
|---------|------------|
| Canario | Contrato ejecutable del triple `(artefacto, runtime, prompt)` con evidencia auditable. |
| Prompt canonico | Entrada fija del canario. Lo redacta el autor una vez; el resto del ciclo debe ser determinista. |
| Knowledge contract | Conjunto de URNs y paths que el artefacto declara consumir. |
| Gate | Conjunto de criterios que el output del canario debe satisfacer. Multinivel: no es binario. |
| Marca canaria | Cadena detectable insertada en un KB para comprobar propagacion de cambios hasta el runtime. |
| Lazo Kelly | Ciclo completo `edit KB → redeploy → invocar → verificar via trace`. |
| Trace | Registro persistente de tool calls y mensajes internos durante la invocacion. |
| Nivel de cierre | Veredicto global del canario: `pasa-estricto`, `pasa-con-deuda`, `parcial` o `falla`. |
| Fixture | Archivo commiteado en `tests/fixtures/canarios/` que documenta el canario y su baseline. |

## 3. Estructura canonica

Un canario **DEBE** declarar los siguientes componentes. Los cinco son
obligatorios; omitir cualquiera de ellos invalida el canario como
instrumento de verificacion.

### 3.1 Input canonico

1. Prompt literal (texto reproducible, sin variables).
2. Modo de invocacion (delegacion, agente directo, headless, interactivo).
3. Contexto ambiental minimo necesario (variables, permisos, cwd).

El input **NO DEBE** cambiar entre corridas del mismo canario. Si cambia,
es un canario distinto.

### 3.2 Knowledge contract esperado

Lista de URNs y paths que el artefacto declara consumir. Viene del
`AGENT.md` fuente del artefacto y del subset que la pregunta del canario
ejerce.

El canario **PUEDE** restringir el contract esperado a un subconjunto
justificado por la pregunta.

### 3.3 Gate multinivel

Tabla de criterios, cada uno con:

1. Nombre operativo.
2. Pregunta verificable (no ambigua).
3. Regla de evidencia (que cuenta como "cumplido").

Criterios tipicos:

- Trazabilidad al KB (mencion textual + tool call `Read` sobre el path).
- Aplicacion del razonamiento declarado (orden, precedencia, estructura).
- Respeto del knowledge contract (no inventa fuera del subset permitido).
- Declaracion honesta de limites (el artefacto reconoce lo que no sabe).

El gate **DEBE** ser multinivel (ver §4), no binario.

### 3.4 Output de referencia

El output que el canario produjo en su corrida baseline. Se conserva tal
cual devuelto por el runtime. **NO** es la respuesta canonica: es el
punto de comparacion para regresiones de contenido y estructura.

### 3.5 Evidencia y trace

Registro de que el canario efectivamente consumio el knowledge contract:

1. Tool calls reales con paths (extraidos del trace segun
   `transmutation-spec §7.3 trace_fidelity`).
2. Session id / transcript path de la corrida baseline.
3. Si hay marca canaria (§5), constancia de que la marca aparece en el
   trace del subagente.

Sin esta seccion, el canario puede cerrar como `parcial` pero no como
`pasa-estricto`.

## 4. Niveles de cierre

Un canario **DEBE** cerrar en uno de cuatro niveles. No existe el nivel
"binario pasa/falla" que se uso en el piloto; esta spec lo reemplaza.

| Nivel | Significado | Implicacion operativa |
|-------|-------------|------------------------|
| `pasa-estricto` | Todos los criterios del gate cumplen con la regla de evidencia estricta. Trace incluye tool calls reales. | Runtime puede declararse endurecido para el artefacto. |
| `pasa-con-deuda` | Todos los criterios se satisfacen funcionalmente pero alguno depende de lectura funcional (no literal) y la deuda esta declarada. | Runtime se declara endurecido con deuda registrada. Debe cerrarse en la siguiente iteracion del canario. |
| `parcial` | Algun criterio no tiene evidencia suficiente. El output puede ser clinicamente/funcionalmente solido pero el gate no cierra. | Runtime **NO** se declara endurecido. Se agenda re-invocacion con el mecanismo de captura correspondiente. |
| `falla` | Criterio estructural violado (el artefacto inventa contenido fuera del contract, contradice su razonamiento declarado, o la transmutacion violo las leyes functoriales). | Runtime se declara no-endurecido. El artefacto fuente o el functor requieren correccion antes de reintentar. |

Reglas:

1. Un canario **NO DEBE** cerrarse con veredicto cualitativo fuera de
   estos cuatro niveles.
2. `pasa-con-deuda` **DEBE** registrar la deuda explicita y un criterio
   de salida. Una deuda sin criterio de salida equivale a `parcial`.
3. `falla` **DEBE** enumerar las leyes violadas con referencia a la spec
   correspondiente.

## 5. Marca canaria y propagacion

El lazo Kelly verifica que un edit del knowledge source propaga hasta el
runtime. La marca canaria es el mecanismo minimo para probarlo.

### 5.1 Marca detectable en el KB

Un canario **PUEDE** insertar una cadena unica y detectable en el KB del
knowledge contract. La marca:

1. **DEBE** ser unica por version del canario (ej.
   `<!-- kora-canario-marker: 2026-04-22-dolor-toracico-baseline-v1 -->`).
2. **NO DEBE** alterar el contenido operativo del KB (usar comentarios
   HTML o metadatos que no se rendericen ni cambien semantica).
3. **DEBE** documentarse en el fixture del canario.

### 5.2 Verificacion via trace

Tras la invocacion, el canario **DEBE** verificar que la marca aparece
en el trace del subagente (es decir, en el JSONL que registra los tool
calls internos, no solo en el JSONL del main).

Evidencia material:

1. `grep` de la marca en el transcript del subagente devuelve >=1.
2. El `Read` sobre el path del KB aparece en los tool calls del
   subagente.

Los dos juntos confirman propagacion: el subagente leyo el archivo
editado, no una copia cacheada ni una version previa.

### 5.3 Lazo Kelly canonico

```
1. edit KB fuente con marca canaria unica
2. kora transmute --target <runtime> --agent <ns>/<nombre>
3. deploy bundle a la ubicacion runtime correspondiente
4. invocar canario en sesion nueva del runtime
5. capturar trace (hook o mecanismo equivalente)
6. verificar: (a) tool calls sobre el path del KB, (b) presencia de la marca
7. registrar veredicto en el fixture
```

Reglas:

1. El canario **DEBE** correr en sesion nueva del runtime. Sesiones
   existentes pueden tener el subagente cacheado en un estado previo.
2. Si el runtime no soporta redeploy programatico del subagente, el paso
   3 se realiza manualmente y se documenta.
3. La verificacion de propagacion **DEBE** dar resultado positivo antes
   de declarar cierre `pasa-estricto`.

## 6. Trazabilidad por runtime

Esta spec no define el mecanismo concreto de captura; ese vive en
`transmutation-spec §7.3 trace_fidelity` y en cada runtime-extension.

Reglas:

1. Un canario **DEBE** exigir el nivel de trace declarado por el runtime
   en su runtime-extension.
2. Si `trace_fidelity: nula` para el runtime, el canario **NO PUEDE**
   cerrar como `pasa-estricto` para el criterio de trazabilidad. Cierra
   como maximo `pasa-con-deuda` con la deuda "no hay forma de auditar
   tool calls en este runtime".
3. Si `trace_fidelity: media`, el canario **DEBE** depender de un
   mecanismo de captura instalado (hook, logger, etc.) y documentarlo.
4. Si `trace_fidelity: alta`, el canario **PUEDE** confiar en el
   mecanismo nativo del runtime sin instalar nada extra.

## 7. Formato del fixture

Un fixture de canario **DEBE** vivir en
`tests/fixtures/canarios/{nombre-del-canario}.md` con el siguiente
frontmatter minimo:

```yaml
---
canario: {identificador}
runtime: {claude-code|codex|openclaw|gemini|mastra|agentskills}
subagent: {nombre-runtime-del-subagente}
subagent_source: {ruta al artefacto runtime desplegado}
subagent_source_urn: {URN del source en KORA}
transmuted_at: {ISO8601}
baseline_captured_at: {YYYY-MM-DD}
baseline_status: {pasa-estricto|pasa-con-deuda|parcial|falla}
invocation_mode: {headless|interactivo|delegado}
capture_mechanism: {descripcion del hook/log/jsonl utilizado}
kb_edit_propagation: {verificado|pendiente|no-aplica}
canario_marker: {cadena unica o "no-aplica"}
---
```

El cuerpo del fixture **DEBE** incluir las cinco secciones del §3
(input, knowledge contract, gate, output de referencia, evidencia) y
las secciones de propagacion (§5.3) y deuda registrada.

## 8. Reglas operativas

### 8.0 Alcance operativo

`canario-spec` gobierna evidencia runtime para artefactos que declaran un
runtime target como endurecido. No gobierna la construccion ni promocion base
de artefactos agenticos; esa responsabilidad vive en `autoria-spec`,
`agent-skill-construction-spec`, `transmutation-spec` y la maintenance gate.

Reglas:

1. Un canario **NO ES** un workspace productivo ni una cohorte del operating
   core. El operating core se deriva del filesystem productivo.
2. Un artefacto productivo **PUEDE** existir sin canario mientras no declare
   un runtime target como endurecido.
3. Un canario **NO DEBE** usarse como sustituto de `check --strict`,
   `validate`, `lint-md`, `health` ni de la validacion de autoria.
4. Los fixtures historicos llamados "domain canary" **DEBEN** tratarse como
   memoria de migracion o muestras de contrato, no como obligacion viva.

### 8.1 Obligatorias

1. Todo artefacto agentico productivo **DEBE** tener al menos un canario
   por runtime target declarado como endurecido.
2. Todo canario **DEBE** ser reproducible: ejecutarlo dos veces con
   input identico debe producir el mismo nivel de cierre (el output
   puede variar en redaccion; el veredicto no).
3. El fixture del canario **DEBE** commitearse en el repositorio.
4. La evidencia de trace **DEBE** ser verificable a posteriori, no solo
   durante la corrida viva.

### 8.2 Recomendadas

1. Los canarios **DEBERIAN** correr en CI cuando el runtime lo permita
   sin coste prohibitivo.
2. Un artefacto con multiples runtimes **DEBERIA** compartir el prompt
   canonico entre canarios y diferenciar solo el mecanismo de captura y
   el nivel esperado de trace.
3. El output de referencia **DEBERIA** actualizarse cuando cambie el
   source del artefacto; la version previa queda como history del
   fixture.

### 8.3 Prohibidas

1. Declarar un runtime endurecido sin canario cerrado.
2. Interpretar "output clinicamente/funcionalmente razonable" como
   sustituto de evidencia de tool calls.
3. Editar el output de referencia sin correr el canario nuevamente.
4. Reutilizar un canario con prompt adversarial (ej. inyectar
   "ignorar instrucciones previas") sin que el artefacto lo soporte
   explicitamente.

## 9. Relacion con otras specs

1. `qa-spec` declara los compromisos de calidad (`Σ`, `qa_budget`); un
   canario **PUEDE** verificar observacionalmente que esos compromisos
   se sostienen en runtime. La moneda canonica sigue siendo la de
   `qa-spec`.
2. `transmutation-spec` declara la fidelidad functorial y el campo
   `trace_fidelity` por runtime; el canario consume esas declaraciones
   y exige el nivel correspondiente.
3. `harness-spec` declara el vector ontologico del artefacto; el canario
   verifica que la proyeccion a runtime preserva las propiedades
   esperadas (naturalidad de Ξ, cierre de safety).
4. Cada `*-runtime-extension` declara su `trace_fidelity` y el
   mecanismo concreto de captura; el canario reusa esas declaraciones
   sin redefinirlas.
5. `autoria-spec` define el shape del source (AGENT.md) que el canario
   transmuta y consume.

## 10. Invariantes

1. Un canario sin input canonico fijo no es canario.
2. Un canario sin gate multinivel colapsa la verificacion a pasa/falla y
   pierde capacidad de graduar.
3. Un canario sin trace verificable no puede cerrar `pasa-estricto`.
4. Un canario que no recorre el lazo Kelly completo no prueba
   propagacion; solo prueba la proyeccion estatica.
5. Runtimes distintos requieren canarios distintos incluso para el
   mismo artefacto: la trace y el mecanismo de captura no son
   portables.

## 11. Validacion

| Check | Condicion | Enforcement |
|-------|-----------|-------------|
| `canario-fixture-presente` | Todo artefacto con runtime endurecido tiene fixture en `tests/fixtures/canarios/` | manual |
| `canario-frontmatter-completo` | Frontmatter del fixture incluye los campos obligatorios de §7 | lint |
| `canario-gate-multinivel` | Gate declara al menos dos criterios y regla de evidencia | manual |
| `canario-evidence-verificable` | Fixture incluye session id o path del trace | manual |
| `canario-marca-canaria-reciente` | Si `kb_edit_propagation: verificado`, la marca corresponde a un edit documentado | manual |
| `canario-nivel-coherente` | `baseline_status` coherente con la evidencia registrada en el cuerpo | manual |

## 12. Migracion

`canario-spec v1.1.0` es aditiva. No exige reescribir artefactos
existentes.

Reglas:

1. Artefactos runtime existentes **NO ESTAN** obligados a tener canario
   inmediatamente; solo los que declaren runtime endurecido.
2. El piloto `urgenciologo/claude-code` cerrado el `2026-04-22` es el
   fixture de referencia para el patron. Otros canarios **DEBERIAN**
   seguir su estructura.
3. Las evaluaciones de canario anteriores a esta spec con veredicto
   binario (`pasa`/`falla`) **DEBEN** re-expresarse en el gate
   multinivel de §4 cuando se revisiten.
