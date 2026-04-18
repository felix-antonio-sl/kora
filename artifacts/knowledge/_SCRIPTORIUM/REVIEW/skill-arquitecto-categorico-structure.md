# Estructura de la Skill `arquitecto-categorico`

Documento de diseno: estructura, frontmatter y decisiones arquitectonicas para la skill KORA `arquitecto-categorico`.

---

## 1. Analisis de patrones de las 3 skills existentes

### 1.1 Frontmatter

Las tres skills usan el formato agentskills.io-compatible, NO el formato KORA/MD con `_manifest`:

| Campo | data-modeling | graphic-design | ux-design |
|-------|--------------|----------------|-----------|
| `name` | `data-modeling` | `graphic-design` | `ux-design` |
| `description` | 1 linea funcional (EN) | 3 lineas detalladas con triggers (ES) | 2 lineas con triggers (ES) |
| `allowed-tools` | `Read, Glob, Grep, Task, Skill` | `[Read, Write, Edit, Grep, Glob, Bash, Agent]` | `[Read, Write, Edit, Grep, Glob, Bash, Agent, WebFetch, WebSearch]` |
| Otros campos | ninguno | ninguno | ninguno |

Observaciones:

- Solo 3 campos en el frontmatter: `name`, `description`, `allowed-tools`. Nada mas.
- No usan `_manifest`, `version`, `status`, `tags`, ni `lang`. Esto es coherente con la spec (skill-spec-md S3.1 regla 1: identidad `skill`, S3.2 regla 1: `_manifest.type = lazy_load_endofunctor`) pero las skills reales en SKILLS/ siguen el formato agentskills.io, no el formato KORA/MD con frontmatter `_manifest`. Esto implica que SKILLS/ opera con un formato distinto al de `AGENTS/{ns}/{name}/skills/`.
- `description` en `graphic-design` y `ux-design` incluye frases trigger ("Usar cuando...") que orientan la delegacion. `data-modeling` no las incluye.
- `allowed-tools` varia segun capacidades: read-only para data-modeling, read-write+agents para graphic-design y ux-design.
- Formato: `data-modeling` usa CSV sin brackets; las otras dos usan array YAML `[...]`. Inconsistencia menor.

### 1.2 Secciones del body

Patron comun extraido de las 3 skills:

| Seccion | data-modeling | graphic-design | ux-design | Patron |
|---------|--------------|----------------|-----------|--------|
| Titulo H1 | Nombre limpio | Nombre + subtitulo | Nombre limpio | Obligatorio |
| Cuando usar / When to Use | S | S | S | **Obligatorio** — triggers de delegacion |
| Distincion con otras skills | No | S | S | Recomendado si hay confusion posible |
| Overview / descripcion | S (What is...) | S (1 parrafo intro) | S (1 parrafo intro) | **Obligatorio** |
| Modos de operacion | No (implicito en Workflow) | S (create/audit/adapt/tokenize) | S (auditoria/diseno) | **Obligatorio** — define los flujos |
| Contenido de dominio | S (niveles, ERD, notacion) | S (operadores visuales) | S (heuristicas, checklist, patrones) | **Core** — aqui vive el conocimiento |
| Workflow / Procedimiento | S (Phase 1-5) | S (9 pasos en create) | S (Auditoria 6 pasos, Diseno 7 pasos) | **Obligatorio** — mapea a CM Core |
| Output Formats / Artefactos | S (Mermaid, YAML, Dict, Narrative) | S (JSON, CSS, Tailwind, SVG) | S (formato reporte MD) | **Obligatorio** — Signature Output |
| Modelo interno / Referencia interna | No | S (Modelo Categorico) | No | Opcional — mecanica de razonamiento |
| Guardrails | No | S | No | Recomendado |
| Anti-patrones | No | S (tabla NO/SI) | No | Recomendado |
| Self-check | No | S (checklist) | No | Recomendado |
| Integracion / Related Skills | S (upstream/downstream + related) | No | No | Recomendado |
| Recursos / Referencias | No | No | S (URLs externas) | Opcional |
| Version History | S | No | No | Opcional |

### 1.3 Hallazgos de estilo

1. **Las skills NO tienen CM Core explicito** (no hay H2 `## Proposito`, `## Input/Output`, `## Procedimiento`, `## Signature Output`). El CM Core esta implicito en la estructura: la description cubre Proposito, las secciones de modo/dominio cubren Procedimiento, los formatos de output cubren Signature Output. Esto diverge de la spec (skill-spec-md S3 dice "DEBE preservar el mismo CM Core"). Las skills en SKILLS/ siguen la convencion agentskills.io, no la convencion interna de AGENTS/{ns}/{name}/skills/.

2. **Estilo narrativo**: `graphic-design` es la mas madura — tiene axioma estetico, modelo categorico interno, guardrails, anti-patrones y self-check. Es el benchmark de calidad.

3. **Longitud**: data-modeling 537 lineas (exhaustivo, step-by-step), graphic-design 353 lineas (sistema + tokens), ux-design 185 lineas (frameworks compactos). La longitud escala con la complejidad del dominio, no es fija.

4. **Idioma**: data-modeling en ingles, graphic-design y ux-design en espanol. Las dos mas recientes estan en espanol, lo que sugiere que espanol es la convencion actual.

---

## 2. Decisiones de diseno para `arquitecto-categorico`

### D1: Forma — Skill extendido

**Decision**: Skill extendido con directorio `SKILLS/arquitecto-categorico/`.

**Justificacion**: El corpus tiene 24 documentos (~360KB, ~3200 lineas). Un skill degenerado de archivo unico seria inmanejable. La spec (S3.2) permite directorio con `SKILL.md` entrypoint + `references/` como fibra adjunta.

**Estructura**:

```
SKILLS/
  arquitecto-categorico/
    SKILL.md                    # Entrypoint con CM Core implicito
    references/                 # Fibra adjunta: corpus
      00-sintesis.md -> ../../KNOWLEDGE/fxsl/cat/corpus-categorico-[...]/00-sintesis.md
      01-composicion.md -> ...
      ...
      20-infraestructura-autonoma.md -> ...
```

### D2: Referencia al corpus — Symlinks

**Decision**: Symlinks relativos desde `references/` al corpus en KNOWLEDGE/.

**Justificacion**:
- El corpus ya existe y es tracked en `KNOWLEDGE/fxsl/cat/corpus-categorico-arquitecto-sistemas-categorial-agentico/`.
- Duplicar 360KB viola DRY y crea riesgo de drift.
- La spec (S3.2 regla 4) dice que `references/` es fibra adjunta sin identidad propia — symlinks cumplen.
- Symlinks relativos sobreviven clones si la estructura de directorio se preserva.
- La alternativa (instrucciones de lectura tipo "lee el path X") es fragil y no es composable con el ciclo Discover/Activate/Execute.

**Path relativo del symlink**: `../../KNOWLEDGE/fxsl/cat/corpus-categorico-arquitecto-sistemas-categorial-agentico/{archivo}` (desde `SKILLS/arquitecto-categorico/references/`).

Nota: si git tracking de symlinks es problematico, la alternativa es un `INDEX.md` en `references/` que liste los paths como tabla de referencia, y la instruccion en SKILL.md de leer desde esos paths. Pero symlinks es la opcion preferida.

### D3: Organizacion del conocimiento — Indice por capitulo + instruccion de carga lazy

**Decision**: El SKILL.md NO internaliza el contenido de los 24 documentos. En su lugar:
- Contiene un indice estructurado de las 13 partes del ICAS-BoK con sus capitulos.
- Cada capitulo lista los documentos de `references/` que lo cubren.
- El procedimiento indica "lee el documento de references/ pertinente al problema" antes de operar.
- Esto preserva lazy-load: la skill tiene ~300-400 lineas operativas, no 5000.

**Justificacion**: La spec (S5) dice que Execute PUEDE montar fibras adjuntas solo si la activacion lo requiere. Cargar los 24 documentos siempre seria una violacion de lazy-load.

### D4: Frontmatter — Formato agentskills.io

**Decision**: Seguir el formato de las 3 skills existentes (agentskills.io-compatible), no el formato KORA/MD con `_manifest`.

```yaml
---
name: arquitecto-categorico
description: [ver D5]
allowed-tools: [ver D6]
---
```

**Justificacion**: Las 3 skills en SKILLS/ usan este formato. SKILLS/ es la libreria agentskills.io-compatible segun CLAUDE.md. Adoptar un formato distinto al de los peers crearia inconsistencia.

### D5: Description — Detallada con triggers

**Decision**: Description multi-linea, en espanol, con triggers de delegacion explicitos. Seguir el estilo de `graphic-design` (la mas madura).

```yaml
description: >-
  Aplica teoria de categorias como lenguaje operativo para disenar,
  auditar y refactorizar arquitecturas de sistemas. Opera con funtores,
  adjunciones, limites, monadas y propiedades universales como
  herramientas de ingenieria. Cubre composicion, preservacion,
  interaccion, escala, agencia, tiempo, procesos, calidad y patrones.
  Usar para modelar schemas categorialmente, disenar migraciones
  via adjunciones, auditar composicion de servicios, formalizar
  protocolos agenticos, o evaluar invariantes arquitectonicos.
```

### D6: Herramientas — Read-heavy con escritura

**Decision**: `allowed-tools: [Read, Write, Edit, Grep, Glob, Bash, Agent]`

**Justificacion**:
- `Read, Grep, Glob`: obligatorias — necesita leer el corpus de references/ y analizar codebase.
- `Write, Edit`: necesarias — produce artefactos (schemas, diagramas, specs) y puede corregir.
- `Bash`: necesaria — puede ejecutar validaciones, linters, herramientas de grafo.
- `Agent`: necesaria — puede delegar a sub-skills si hay composicion (e.g., pedir a data-modeling que materialice un schema).
- No incluye `WebFetch`/`WebSearch` — el corpus es autocontenido, no necesita busquedas externas.

### D7: Modos de operacion

Propuesta de 5 modos, derivados del analisis del corpus:

| Modo | Trigger | Entregable |
|------|---------|------------|
| `model` | Modelar un dominio, schema o sistema como categoria | Diagramas categoriales + ecuaciones + schema formal |
| `audit` | Evaluar composicion, invariantes o coherencia de un sistema | Reporte de hallazgos con propiedad categorica violada |
| `migrate` | Disenar migracion entre schemas/sistemas | Funtor de migracion + adjuncion Sigma/Delta/Pi + perdida declarada |
| `compose` | Componer servicios, agentes, pipelines | Diagrama de composicion + verificacion de conmutatividad |
| `formalize` | Capturar un patron o heuristica como construccion universal | Formulacion categorica + implementacion operativa |

### D8: Idioma

**Decision**: Espanol para todo el contenido, ingles para terminos tecnicos/categoricos (funtor, adjuncion, pullback, pushout, monad, etc.). Consistente con graphic-design y ux-design.

### D9: Modelo categorico interno

**Decision**: Incluir seccion de modelo categorico interno (como graphic-design), dado que esta skill ES el framework categorico. A diferencia de graphic-design que lo usa como mecanica de razonamiento privada, aqui el modelo categorico ES el dominio. La seccion describe como el ICAS-BoK se organiza como una categoria de conceptos con morfismos de dependencia.

---

## 3. Skeleton del SKILL.md

```markdown
---
name: arquitecto-categorico
description: >-
  Aplica teoria de categorias como lenguaje operativo para disenar,
  auditar y refactorizar arquitecturas de sistemas. Opera con funtores,
  adjunciones, limites, monadas y propiedades universales como
  herramientas de ingenieria. Cubre composicion, preservacion,
  interaccion, escala, agencia, tiempo, procesos, calidad y patrones.
  Usar para modelar schemas categorialmente, disenar migraciones
  via adjunciones, auditar composicion de servicios, formalizar
  protocolos agenticos, o evaluar invariantes arquitectonicos.
allowed-tools: [Read, Write, Edit, Grep, Glob, Bash, Agent]
---

# Arquitecto Categorico — Ingenieria de Sistemas via Teoria de Categorias

<!-- H1 sigue el patron de graphic-design: nombre + subtitulo descriptivo -->

Skill para disenar, auditar y refactorizar arquitecturas de sistemas
usando teoria de categorias como lenguaje operativo. El corpus de
referencia (24 documentos, references/) proporciona el conocimiento
de dominio; esta skill lo organiza como procedimiento ejecutable.

## Axioma de diseno

<!-- Patron tomado de graphic-design (Axioma Estetico). Define el
     principio rector que gobierna todas las decisiones. -->

> **Arquitectura = composicion correcta de partes que preservan estructura.**

Toda decision arquitectonica se evalua contra esta definicion. Un
componente se justifica solo si compone limpiamente (asociatividad),
preserva estructura al traducirse (functorialidad), y satisface la
propiedad universal que lo define (universalidad). Lo que no compone,
no preserva, o no es universal, es deuda arquitectonica con nombre
categorico.

## Cuando usar esta skill

<!-- Triggers de delegacion. Necesarios para que el agente padre
     sepa cuando activar esta skill. Patron comun a las 3 skills. -->

- Al modelar schemas, APIs o sistemas como categorias formales
- Al disenar migraciones de datos o schemas con preservacion de estructura
- Al auditar la composicion de servicios, pipelines o agentes
- Al formalizar un patron de diseno como construccion universal
- Al evaluar invariantes arquitectonicos (conmutatividad, adjuncion, limites)
- Al componer sistemas multi-agente con garantias de coherencia
- Cuando el usuario dice "modelar categorialmente", "funtor de migracion",
  "auditar composicion", "verificar invariantes", "formalizar patron"

## Distincion con otras skills

<!-- Patron de graphic-design y ux-design. Evita confusion con skills
     que tocan dominios adyacentes. -->

| Esta skill (arquitecto-categorico) | data-modeling | graphic-design |
|------------------------------------|---------------|----------------|
| POR QUE compone (fundamento) | QUE datos modelar | QUE se ve (visual) |
| Funtores, adjunciones, limites | ERDs, cardinalidad, normalizacion | Operadores, tokens, composicion visual |
| Produce la fundamentacion formal | Produce el schema | Produce la identidad visual |
| Agnostica de dominio | Dominio datos | Dominio visual |

`arquitecto-categorico` es **upstream** de `data-modeling`: primero se
formaliza la categoria, luego se materializa como schema relacional.

## Modos de operacion

<!-- Patron de graphic-design. Cada modo es un flujo con trigger,
     procedimiento y entregable. -->

**Seleccion de modo**: Al recibir un pedido, identificar el modo segun contexto:
- Dominio/schema sin formalizar -> `model`
- Sistema existente a evaluar -> `audit`
- Transicion entre schemas/sistemas -> `migrate`
- Servicios/agentes/pipelines a integrar -> `compose`
- Patron o heuristica a capturar -> `formalize`

### 1. `model` — Formalizar como categoria

<!-- Flujo para tomar un dominio, schema o sistema y producir su
     representacion categorial. Es el modo mas frecuente. -->

Flujo:
1. CAPTURAR — Identificar objetos (entidades), morfismos (relaciones), ecuaciones (constraints)
2. FORMALIZAR — Presentar como categoria finitamente presentada (generadores + ecuaciones)
3. VERIFICAR — Validar propiedades: completud, cocompleted, limites que existen
4. MATERIALIZAR — Emitir schema, diagrama o spec formal
5. TRAZAR — Referenciar documentos del corpus que fundamentan las decisiones

Documentos de referencia primarios: 00 (sintesis), 01 (composicion), 04 (identidad-relacion), 05 (universales).

Entregables: Categoria presentada (generadores + ecuaciones) + Diagrama conmutativo + Schema derivado.

### 2. `audit` — Evaluar composicion e invariantes

<!-- Flujo para auditar un sistema existente contra propiedades categoricas.
     Analogo al modo `audit` de graphic-design. -->

Flujo:
1. LEER — Obtener la arquitectura/schema/pipeline a auditar
2. CATEGORIZAR — Identificar la categoria implicita (objetos, morfismos)
3. VERIFICAR — Evaluar propiedades:
   - Composicion: asociatividad, identidades
   - Preservacion: functorialidad de traducciones
   - Universalidad: limites y colimites usados correctamente
   - Conmutatividad: diagramas que deben conmutar
4. CLASIFICAR — Hallazgos por severidad y propiedad violada
5. PROPONER — Correccion con justificacion categorica
6. TRAZAR — Documentos del corpus que fundamentan cada hallazgo

Documentos de referencia primarios: 02 (preservacion), 03 (comparacion), 18 (calidad-riesgo), 19 (patrones).

Entregables: Reporte de auditoria con propiedad violada + severidad + correccion.

### 3. `migrate` — Disenar migracion

<!-- Flujo especializado en migraciones de datos, schemas o sistemas.
     Usa la maquinaria de adjunciones Sigma/Delta/Pi del documento 06. -->

Flujo:
1. IDENTIFICAR — Schema origen (C) y schema destino (D)
2. FUNTOR — Definir el funtor F : C -> D que mapea la migracion
3. ADJUNCION — Derivar los adjuntos: Sigma_F (push), Delta_F (pull), Pi_F (push con join)
4. PERDIDA — Declarar explicitamente que informacion se pierde (non-fullness, non-faithfulness)
5. PLAN — Secuencia operativa de migracion derivada de la adjuncion
6. TRAZAR — Documentos del corpus que fundamentan la adjuncion

Documentos de referencia primarios: 02 (preservacion), 06 (adjunciones), 10 (extension).

Entregables: Funtor de migracion + adjuncion derivada + declaracion de perdida + plan operativo.

### 4. `compose` — Componer sistemas

<!-- Flujo para composicion de servicios, agentes, pipelines. Usa la
     maquinaria de escala, interaccion y agencia. -->

Flujo:
1. INVENTARIAR — Listar componentes (objetos) e interfaces (morfismos)
2. DIAGRAMA — Construir el diagrama de composicion
3. CONMUTAR — Verificar conmutatividad de todos los caminos
4. EFECTOS — Identificar monadas de efectos y composicion Kleisli
5. ESCALA — Evaluar composicion a escala (operads, double categories)
6. TRAZAR — Documentos del corpus que fundamentan la composicion

Documentos de referencia primarios: 07 (composicion con estructura), 09 (efectos), 11 (interaccion), 13 (escala), 14 (agencia).

Entregables: Diagrama de composicion + verificacion de conmutatividad + monadas de efectos.

### 5. `formalize` — Capturar patron

<!-- Flujo para tomar un patron de diseno, heuristica o practica
     y darle formulacion categorica. -->

Flujo:
1. OBSERVAR — Identificar el patron o heuristica
2. ABSTRAER — Extraer la estructura subyacente (objetos, morfismos, propiedad universal)
3. NOMBRAR — Identificar la construccion categorica correspondiente (limite, adjuncion, monada, etc.)
4. VERIFICAR — Confirmar que la identificacion preserva la semantica operativa
5. DOCUMENTAR — Formulacion categorica + implementacion operativa
6. TRAZAR — Documentos del corpus que fundamentan la formalizacion

Documentos de referencia primarios: 05 (universales), 06 (adjunciones), 19 (patrones).

Entregables: Formulacion categorica del patron + mapping a implementacion + documentos de soporte.

## Corpus de referencia — ICAS-BoK

<!-- Este indice es el corazon de la skill extendida. Organiza los 24
     documentos del corpus en una estructura navegable. El agente
     consulta este indice para saber que documento leer segun el
     problema. Los documentos viven en references/ como symlinks. -->

El corpus ICAS (Ingenieria Categorial Aplicada a Sistemas) se organiza
en 5 bloques tematicos. Cada entrada referencia el archivo en
`references/` que contiene el conocimiento completo.

### Bloque I: Fundamentos

| Doc | Archivo | Tema | Usar cuando |
|-----|---------|------|-------------|
| 00 | `00-sintesis.md` | ADN cognitivo del arquitecto categorial | Orientacion general, primer acercamiento |
| 01 | `01-composicion.md` | Composicion, asociatividad, identidades | Modelar cualquier sistema como categoria |
| 02 | `02-preservacion.md` | Functores, faithfulness, fullness | Evaluar traducciones entre sistemas |
| 03 | `03-comparacion.md` | Transformaciones naturales, equivalencia | Comparar dos disenos o implementaciones |

### Bloque II: Estructura universal

| Doc | Archivo | Tema | Usar cuando |
|-----|---------|------|-------------|
| 04 | `04-identidad-es-relacion.md` | Yoneda, representabilidad | Disenar APIs, interfaces, observabilidad |
| 05 | `05-universales.md` | Limites, colimites, pullback, pushout | JOINs, MERGEs, construcciones universales |
| 06 | `06-adjunciones.md` | Adjunciones, Free/Forget, Sigma/Delta/Pi | Migraciones, abstracciones, pares optimos |

### Bloque III: Composicion avanzada

| Doc | Archivo | Tema | Usar cuando |
|-----|---------|------|-------------|
| 07 | `07-composicion-con-estructura.md` | Productos monoidales, composicion con estructura | Componer con operacion tensor |
| 08 | `08-enriquecimiento.md` | Categorias enriquecidas | Hom-sets con estructura (metricas, ordenes) |
| 08b | `08b-higher-categories.md` | Categorias superiores (2-cat, n-cat) | Sistemas con morfismos entre morfismos |
| 09 | `09-efectos.md` | Monadas, Kleisli, efectos | Pipelines con efectos, composicion con estado |
| 10 | `10-extension.md` | Extensiones de Kan | Aproximar funtores, completar datos |

### Bloque IV: Sistemas

| Doc | Archivo | Tema | Usar cuando |
|-----|---------|------|-------------|
| 11 | `11-interaccion.md` | Poly, lentes, interaccion | APIs bidireccionales, protocolos |
| 12 | `12-topoi.md` | Topoi, logica interna | Feature flags, permisos, logica no-binaria |
| 12b | `12b-safety-alignment.md` | Safety y alignment | Seguridad, alineacion de agentes |
| 13 | `13-escala.md` | Operads, double categories, cospans | Composicion a escala, jerarquias |

### Bloque V: Agencia y operaciones

| Doc | Archivo | Tema | Usar cuando |
|-----|---------|------|-------------|
| 14 | `14-agencia.md` | Free monad, cofree comonad, pattern/matter | Disenar agentes, delegacion, planes |
| 14b | `14b-protocolos-coreografia.md` | Protocolos, coreografia | Comunicacion multi-agente |
| 15 | `15-tiempo.md` | Sheaves temporales, event sourcing | Modelar tiempo, consistencia eventual |
| 16 | `16-lifecycle.md` | Lifecycle, estados, transiciones | Ciclos de vida de sistemas |
| 17 | `17-procesos.md` | Procesos, workflows, orquestacion | Pipelines, CI/CD, procesos de negocio |
| 18 | `18-calidad-riesgo.md` | Calidad, riesgo, metricas | Auditar calidad, evaluar riesgo |
| 19 | `19-patrones.md` | Patrones como construcciones universales | Formalizar patrones de diseno |
| 20 | `20-infraestructura-autonoma.md` | Infraestructura autonoma | Kubernetes, IaC, self-healing |

**Instruccion de carga**: Antes de operar en cualquier modo, leer el
indice anterior para identificar los documentos pertinentes. Luego leer
los documentos especificos de `references/`. No cargar todo el corpus
de golpe — solo los documentos relevantes al problema.

## Procedimiento general

<!-- Corresponde al CM Core "Procedimiento". Aplica a todos los modos.
     Los modos anteriores lo especializan, pero este es el flujo
     meta que gobierna. -->

1. **RECIBIR** — Aceptar el pedido, identificar modo de operacion
2. **INDEXAR** — Consultar el indice del ICAS-BoK, seleccionar documentos pertinentes
3. **LEER** — Cargar los documentos seleccionados de `references/`
4. **OPERAR** — Ejecutar el flujo del modo seleccionado
5. **VERIFICAR** — Validar el output contra el axioma de diseno (compone, preserva, es universal)
6. **TRAZAR** — Citar documentos del corpus que fundamentan cada decision
7. **ENTREGAR** — Emitir artefacto en el formato del modo

## Formatos de output

<!-- Corresponde al CM Core "Signature Output". Define los formatos
     de artefacto que produce esta skill. -->

### Categoria presentada

Para modo `model`:

```
Categoria: <nombre>

Objetos: A, B, C, ...

Generadores:
  f : A -> B
  g : B -> C
  h : A -> C

Ecuaciones:
  g . f = h    -- (nombre de la constraint)

Limites:
  A x_C B      -- pullback de f y g sobre C

Instancia:
  I : <nombre> -> Set
  I(A) = {a1, a2, ...}
  I(f)(a1) = b3
```

### Reporte de auditoria

Para modo `audit`:

```markdown
## Auditoria Categorial: [nombre del sistema]

### Resumen
- Hallazgos: X criticos, Y altos, Z medios
- Propiedades evaluadas: composicion, preservacion, universalidad, conmutatividad

### Hallazgos

#### [SEVERIDAD] Propiedad violada: [nombre]
- **Estructura**: [que parte del sistema]
- **Violacion**: [que propiedad se rompe y como]
- **Fundamentacion**: [documento del corpus + seccion]
- **Correccion**: [accion concreta]
- **Esfuerzo**: Bajo/Medio/Alto
```

### Funtor de migracion

Para modo `migrate`:

```markdown
## Migracion: [origen] -> [destino]

### Funtor F : C -> D
- F(tabla_A) = tabla_X
- F(fk_f) = fk_g . fk_h

### Adjuncion
- Sigma_F: [descripcion operativa del push]
- Delta_F: [descripcion operativa del pull]
- Pi_F: [descripcion operativa del push con join]

### Perdida declarada
| Aspecto | Que se pierde | Por que | Mitigacion |
```

### Diagrama de composicion

Para modo `compose`:

```markdown
## Composicion: [nombre del sistema]

### Componentes
| Componente | Rol | Interfaz |

### Diagrama
[Mermaid o texto con flechas]

### Conmutatividad
| Camino 1 | Camino 2 | Conmuta? | Evidencia |

### Efectos
| Componente | Monada | Composicion Kleisli |
```

### Formalizacion de patron

Para modo `formalize`:

```markdown
## Patron: [nombre]

### Observacion
[Descripcion del patron o heuristica]

### Construccion categorica
[Formulacion formal: limite, adjuncion, monada, etc.]

### Mapping operativo
| Concepto categorico | Concepto de implementacion |

### Verificacion
[Como confirmar que la identificacion preserva semantica]

### Corpus
[Documentos del ICAS-BoK que fundamentan]
```

## Guardrails

<!-- Patron de graphic-design. Restricciones operativas. -->

- Toda decision arquitectonica debe justificarse contra el axioma de diseno (compone, preserva, es universal)
- Declarar explicitamente cuando una traduccion/migracion pierde informacion (perdida de faithfulness o fullness)
- No afirmar adjuncion sin verificar la propiedad universal (unit/counit + triangle identities)
- No confundir analogia disciplinada con identificacion formal — declarar explicitamente cual es
- Citar siempre los documentos del corpus que fundamentan cada decision
- No cargar todo el corpus de golpe — lazy-load por documento segun relevancia
- Espanol para documentacion, ingles para terminos categoricos cuando sean mas precisos
- Los artefactos producidos deben ser operativos (implementables), no solo teoricos

## Anti-patrones

<!-- Patron de graphic-design. Errores comunes a evitar. -->

| NO hacer | SI hacer |
|----------|---------|
| Usar vocabulario categorico sin operatividad | Cada termino debe tener traduccion a accion concreta |
| Afirmar "esto es un funtor" sin verificar leyes | Verificar preservacion de composicion e identidad |
| Modelar todo como categoria sin ganancia | Usar categoria solo cuando la composicion importa |
| Cargar los 24 documentos del corpus a la vez | Indexar, seleccionar, leer solo lo pertinente |
| Formalizar por formalizar | La formalizacion debe resolver un problema real |
| Ignorar la dualidad | Todo concepto tiene un dual — evaluarlo sistematicamente |
| Imponer teoria sin traducir a practica | Cada output debe tener seccion de mapping operativo |
| Suponer que el usuario domina la teoria | Explicar terminos en la primera aparicion |

## Self-check

<!-- Patron de graphic-design. Checklist antes de entregar. -->

Antes de entregar cualquier artefacto, verificar:

```
[ ] El axioma de diseno se satisface? (compone, preserva, es universal)
[ ] Las construcciones usadas son las correctas? (no analogias forzadas)
[ ] Los documentos del corpus citados son pertinentes?
[ ] El output es operativo (implementable), no solo teorico?
[ ] La perdida de informacion esta declarada donde aplique?
[ ] Los diagramas conmutan donde deben conmutar?
[ ] El vocabulario categorico se tradujo a practica?
[ ] El modo de operacion es el correcto para el pedido?
```

## Integracion

<!-- Patron de data-modeling. Relaciones con otras skills. -->

### Upstream
- Esta skill es upstream de casi todo: proporciona la fundamentacion formal

### Downstream
- `data-modeling` — materializa categorias como schemas relacionales
- `graphic-design` — usa su propio modelo categorico interno (VisId)
- `ux-design` — evalua la experiencia resultante

### Composicion
- `data-modeling` puede invocar esta skill para formalizar un dominio antes de modelar
- Esta skill puede invocar `data-modeling` para materializar un schema derivado de una categoria
```

---

## 4. Estructura de directorio propuesta

```
SKILLS/
  arquitecto-categorico/
    SKILL.md                              # Entrypoint (~350-400 lineas)
    references/                           # Fibra adjunta: symlinks al corpus
      00-sintesis.md                      # -> KNOWLEDGE/fxsl/cat/corpus-.../00-sintesis.md
      01-composicion.md                   # -> KNOWLEDGE/fxsl/cat/corpus-.../01-composicion.md
      02-preservacion.md                  # -> ...
      03-comparacion.md
      04-identidad-es-relacion.md
      05-universales.md
      06-adjunciones.md
      07-composicion-con-estructura.md
      08-enriquecimiento.md
      08b-higher-categories.md
      09-efectos.md
      10-extension.md
      11-interaccion.md
      12-topoi.md
      12b-safety-alignment.md
      13-escala.md
      14-agencia.md
      14b-protocolos-coreografia.md
      15-tiempo.md
      16-lifecycle.md
      17-procesos.md
      18-calidad-riesgo.md
      19-patrones.md
      20-infraestructura-autonoma.md
```

Total: 1 archivo de entrypoint + 24 symlinks en references/.

El directorio NO tiene `scripts/` ni `assets/` — no son necesarios para esta skill.
El directorio NO tiene metadata adicional — toda la metadata vive en el frontmatter del SKILL.md.

---

## 5. Observaciones y riesgos

### Observaciones

1. **Divergencia formato SKILLS/ vs AGENTS/.../skills/**: Las skills en SKILLS/ usan formato agentskills.io (3 campos), no el formato KORA/MD con `_manifest.urn` y `_manifest.type = lazy_load_endofunctor`. Si se quiere conformidad estricta con skill-spec-md S3.1/S3.2, habria que agregar el `_manifest` al frontmatter. Pero hacerlo romperia la consistencia con las 3 skills existentes. Recomendacion: mantener formato agentskills.io por consistencia con peers, documentar la divergencia, y resolver en un futuro pass de armonizacion.

2. **Naming convention**: La spec S3.1 regla 5 dice SCREAMING_CASE (`CM-NOMBRE-DESCRIPTIVO`). Las skills en SKILLS/ no siguen esta convencion (usan lowercase-hyphen). Esto sugiere que SKILLS/ opera con convenciones agentskills.io, no con las convenciones de skills internas de workspaces KORA. Recomendacion: mantener `arquitecto-categorico` (lowercase-hyphen) por consistencia con peers.

3. **CM Core implicito vs explicito**: La spec exige 4 secciones (`Proposito`, `Input/Output`, `Procedimiento`, `Signature Output`). Ninguna de las 3 skills existentes las tiene como H2 literales. El contenido esta distribuido en secciones con nombres mas descriptivos. Recomendacion: mantener nombres descriptivos por consistencia con peers, y mapear mentalmente: description = Proposito, modos/cuando-usar = Input/Output, procedimiento-general = Procedimiento, formatos-de-output = Signature Output.

### Riesgos

1. **Symlinks y git**: Git trackea symlinks como archivos de texto con el target path. Esto funciona bien en Linux/macOS pero puede fallar en Windows. Para un repo que se clona principalmente en Linux (como KORA), no es un riesgo practico.

2. **Tamano del corpus**: 360KB de referencia es grande. Si algun runtime carga todo references/ de golpe, sera costoso. La instruccion de lazy-load en SKILL.md mitiga esto, pero depende de que el consumidor la respete.

3. **Mantenimiento de symlinks**: Si el corpus se mueve o renombra, los symlinks se rompen. Mitigacion: un check en el linter que verifique que todos los symlinks en references/ resuelven.
