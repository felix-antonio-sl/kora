---
_manifest:
  urn: "urn:kora:kb:autoria-spec"
  provenance:
    created_by: "FS"
    created_at: "2026-04-17"
    source: "Fusiona agentfile-spec v2.0.0 + skill-overlay-spec v2.0.0 bajo la ontologia PMI × LFS de harness-spec v1.0.0. Unifica regimen URN, shape de authoring, y validacion condicional por forma material. v1.1 agrega shape coalgebraico opcional (§3.5). v1.2 agrega risk_register y soporte declarativo para target Mastra."
version: "1.2.0"
status: publicado
tags: [autoria, artefacto-agentico, serializacion, proyeccion, unificada]
lang: es
extensions:
  kora:
    family: spec
relations:
  depends:
    - "urn:kora:kb:gobernanza"
    - "urn:kora:kb:harness-spec"
  cites:
    - "urn:kora:kb:md-spec"
    - "urn:kora:kb:qa-spec"
    - "urn:kora:kb:runtime-spec-md"
    - "urn:kora:kb:transmutation-spec"
  supersedes:
    - "urn:kora:kb:agentfile-spec"
    - "urn:kora:kb:skill-overlay-spec"
---

# Especificacion de Autoria de Artefactos Agenticos v1.2.0

## 1. Definicion

Esta especificacion define el **shape de autoria unificado** para todo
artefacto agentico productivo de KORA. Un artefacto agentico es cualquier
objeto que habita el espacio PMI × LFS definido por `harness-spec`: desde
una habilidad portable de una sola funcion hasta un agente de plataforma
always-on con materia persistente.

La spec **reemplaza y retira** `agentfile-spec v2.0.0` y
`skill-overlay-spec v2.0.0`, que trataban tipos de artefactos previamente
separados (agentes y skills) como si vivieran en ontologias distintas.
En PMI × LFS no lo son: son regiones del mismo espacio. La unificacion
refleja esa realidad ontologica.

**No hay periodo de coexistencia.** Desde la adopcion de esta spec,
los artefactos agenticos productivos se escriben unicamente con el
shape unificado. Los artefactos pre-existentes se migran en una sola
pasada (ver §13).

### 1.1 Principios rectores

1. **Ontologia unica** — todo artefacto agentico se describe por un mismo
   vector de 6 ejes (`vector_ontologico`).
2. **Forma material como discriminante** — el campo `atlas.forma_material`
   decide que subset del shape aplica, no una spec separada.
3. **Tres atlas ortogonales** — arnes categorico, forma material, metafora
   relacional: ejes independientes que conjuntamente caracterizan el punto
   del artefacto en el espacio.
4. **Proyeccion fiel al estandar externo** — los artefactos con
   `forma_material: habilidad` deben transmutar byte-identical a paquetes
   agentskills.io-compatibles. Interop por construccion.
5. **Promocion entre formas** — un artefacto puede evolucionar de
   habilidad a subagente a agente-propiamente-tal sin cambiar identidad
   (URN), solo cambiando `forma_material`.

### 1.2 Lo que NO es esta spec

- No define la ontologia PMI × LFS (eso lo hace `harness-spec`).
- No define las reglas de proyeccion a runtimes (eso lo hace
  `transmutation-spec` y las `runtime-extensions`).
- No define los formatos de distribucion externa (`plugin.json`,
  `marketplace.json` son capa 4).
- No gobierna artefactos de conocimiento pasivo (eso lo hace
  `knowledge-spec`).

### 1.3 Glosario de terminos

| Termino | Definicion |
|---------|------------|
| Artefacto agentico | Objeto que habita el espacio PMI × LFS; posee plan, materia o interaccion no triviales. |
| Forma material | Valor de `atlas.forma_material`; enum cerrado {habilidad, subagente, agente-propiamente-tal, agente-plataforma}. |
| Arnes categorico | Valor de `atlas.arnes_categorico`; clase estructural del artefacto (atlas A de `harness-spec §5.1`). |
| Metafora relacional | Valor de `atlas.metafora_relacional`; lectura HCAI del artefacto (atlas C de `harness-spec §5.3`). |
| Promocion | Transicion de un artefacto a una forma material superior en la cadena `habilidad → subagente → agente-propiamente-tal → agente-plataforma` (§8). |
| Democion | Operacion prohibida: descender en la cadena de formas materiales (§8.2). |
| Shape | Estructura de campos `artefacto.{perfil, plan, interfaz, contexto, composicion, invariantes}` (§3.4). |
| Proyeccion fiel | Transmutacion byte-identical a un target externo, sin perdida declarada (§5.5). |
| Matriz de realizabilidad | Tabla `(arnes_categorico × forma_material × runtime)` que declara fidelidad por combinacion (§12). |

El glosario de **identificadores YAML y topologia** vive en §15.

## 2. Ubicacion en la arquitectura

Segun `gobernanza §3` (capas):

- Capa 1 — Ontologia: `harness-spec` (fuente de verdad).
- Capa 2 — **Serializacion: esta spec** (`autoria-spec`) + `md-spec` + `knowledge-spec`.
- Capa 3 — Runtime: `runtime-spec-md`, `transmutation-spec`, runtime-extensions.
- Capa 4 — Distribucion: externa.

`autoria-spec` es **serializacion de autoria**: un shape concreto,
conveniente para escribir artefactos a mano, que proyecta sobre el vector
ontologico. El vector es autoritativo; el shape es proyeccion.

## 3. Frontmatter canonico

Todo artefacto agentico productivo **DEBE** declarar el siguiente
frontmatter:

```yaml
---
_manifest:
  urn: "urn:{namespace}:artefacto:{id}"
  type: artefacto
  provenance:
    created_by: "identificador-humano"
    created_at: "YYYY-MM-DD"
    source: "..."
version: "semver"
status: activo
nombre: "NombreArtefacto"
descripcion: "Una linea descriptiva — disparador y uso."
tags: [...]
lang: es
extensions:
  kora:
    vector_ontologico:
      pi: 2
      mu: 2
      xi: 2
      lambda: 0
      phi: 1
      sigma: [2,2,2,2,1]
    presentacion: estado-primario
    atlas:
      arnes_categorico: persona
      forma_material: agente-propiamente-tal
      metafora_relacional: centro-de-control
    entornos_objetivo: [claude-code, codex, opencode, openclaw]
    nivel_prescripcion: medio
    conocimiento_permitido:
      - "urn:kora:kb:..."
    componible_con:
      - "urn:kora:artefacto:..."
  claude_code: { ... }
  codex: { ... }
  openclaw: { ... }
artefacto:
  perfil: { ... }
  plan: { ... }
  interfaz: { ... }
  contexto: { ... }
  composicion: { ... }
  invariantes: { ... }
---
```

### 3.1 Campos del envelope

| Campo | Tipo | Obligatorio | Proposito |
|-------|------|-------------|-----------|
| `_manifest.urn` | string | si | Identidad canonica (ver §10). |
| `_manifest.type` | enum | si | Kind estructural. Para esta spec: `artefacto` (ver `gobernanza §4.2`). |
| `_manifest.provenance` | objeto | si | Trazabilidad de origen. |
| `version` | semver | si | Version del artefacto (fuera del URN). |
| `status` | enum | si | Ciclo de vida (`borrador\|activo\|deprecado\|retirado`, ver §11). |
| `nombre` | string | si | Identificador humano. |
| `descripcion` | string | si | Disparador y uso (1 linea). |
| `tags` | lista | no | Descriptores libres. |
| `lang` | string | si | `es` o `en` (default `es`). |

### 3.2 Campos del overlay KORA (`extensions.kora`)

| Campo | Obligatorio | Proposito |
|-------|-------------|-----------|
| `vector_ontologico` | si | Los 6 ejes PMI × LFS. Ver §4. |
| `presentacion` | si | `estado-primario` o `accion-primaria`. |
| `atlas.arnes_categorico` | si | Slug del atlas A. Ver §4.2. |
| `atlas.forma_material` | si | Slug del atlas B. Ver §5. |
| `atlas.metafora_relacional` | no | Slug del atlas C (opcional). |
| `entornos_objetivo` | si | Runtimes soportados (lista no vacia). |
| `nivel_prescripcion` | condicional | `alto`, `medio`, `bajo`. Obligatorio cuando `forma_material=habilidad`. |
| `conocimiento_permitido` | no | Lista de URNs de conocimiento referenciable. |
| `componible_con` | no | Lista de URNs de artefactos componibles. |

### 3.3 Campos de encaje runtime (`extensions.{runtime}`)

Cada runtime declara su propio namespace bajo `extensions`. El contenido
es runtime-especifico y gobernado por la runtime-extension
correspondiente. Ejemplos: `extensions.claude_code.model`,
`extensions.openclaw.bot_handler`.

Estos campos son fibras del runtime y no proyectan al vector ontologico;
son metadata de realizacion.

### 3.4 Shape del artefacto (`artefacto.*`)

El objeto `artefacto` expresa el refinamiento agentico en seis
dimensiones. Cuales son obligatorias y cuales no depende de
`atlas.forma_material`:

| Dimension | Contenido | Proyecta sobre |
|-----------|-----------|-----------------|
| `perfil` | descripcion operativa, dominio, disparadores, salidas, narrativa | descriptivo (no proyecta) |
| `plan` | estado inicial, estado terminal, estados (FSM) | Π |
| `interfaz` | herramientas, permisos, protocolos | Ξ |
| `contexto` | identidad, perfil del operador, configuracion de memoria, `qa_budget`, `risk_register`, pistas runtime | Μ, Φ, knowledge refs, budgets, riesgos |
| `composicion` | sub-agentes, rutas doradas, cortacircuitos, ruteo de eventos | Ξ=4, Λ si delega |
| `invariantes` | reglas duras, invariantes coinductivas, guardrails, compromisos eticos | Σ + safety estructural derivable |

El campo `perfil` es descriptivo puro — no tiene peso ontologico. Sirve
para documentacion humana y descubrimiento.

### 3.5 Shape coalgebraico (opcional, v1.1+)

Un artefacto **PUEDE** declarar estructura coalgebraica explicita bajo
`artefacto.plan.fsm` (free monad serializable) y `artefacto.interfaz.polinomio`
(interface functor como polynomial P(U) = Σ_{p ∈ Positions} U^{Directions(p)}).

Cuando presentes, estos campos **DEBEN** cumplir:

- `plan.fsm.estados`: lista de estados con id unico.
- `plan.fsm.inicial`: id de estado inicial (DEBE estar en `estados`).
- `plan.fsm.terminales`: lista no vacia de ids terminales (DEBEN estar en `estados`).
- `plan.fsm.transiciones`: mapa `{estado_id: [estado_id_siguiente, ...]}`.
- **Invariante de termination**: desde `inicial`, TODOS los caminos deben
  poder alcanzar un terminal en finitos pasos (no hay ciclos infinitos
  sin salida). Esto materializa Π monotonicity + termination de `harness-spec §4`.

- `interfaz.polinomio.posiciones`: lista de posiciones (inputs disponibles).
- `interfaz.polinomio.direcciones`: mapa `{posicion: [direccion, ...]}` (outputs por input).

- `invariantes.sub_coalgebra_segura` (opcional): lista de estados FSM
  cuyo cierre bajo transiciones permanece en la sub-coalgebra — materializa
  la "sub-coalgebra de safety cerrada" de Part IV del ICAS-BoK.

Ejemplo minimo:

```yaml
artefacto:
  plan:
    estado_inicial: "S-START"
    estado_terminal: "S-END"
    estados: [...]
    fsm:
      inicial: "S-START"
      terminales: ["S-END", "S-ABORT"]
      transiciones:
        "S-START": ["S-WORK", "S-ABORT"]
        "S-WORK": ["S-END", "S-ABORT"]
        "S-END": []
        "S-ABORT": []
  interfaz:
    herramientas: [...]
    polinomio:
      posiciones: ["read", "write", "ask"]
      direcciones:
        read: ["content", "not-found"]
        write: ["ok", "conflict"]
        ask: ["answer"]
  invariantes:
    sub_coalgebra_segura: ["S-START", "S-WORK", "S-END"]
```

El check `coalgebra-conformance` (§13) verifica termination del FSM
cuando `plan.fsm` esta declarado; no hace nada si el campo esta ausente
(opcional por compatibilidad con shape v1.0).

Estos campos son **opcionales en v1.1** y **obligatorios** para
artefactos que declaren `extensions.kora.verificacion_coalgebraica: true`.

#### 3.5.1 API observable (Yoneda operativo)

Un artefacto **PUEDE** declarar `artefacto.interfaz.api_observable` como el
perfil representable minimo que un caller externo observa del artefacto —
materializa la identidad-como-relacion de Yoneda (`04-identidad-es-relacion`).

```yaml
artefacto:
  interfaz:
    api_observable:
      entradas:
        - nombre: consulta
          tipo: texto
          obligatorio: true
      salidas:
        - nombre: respuesta
          tipo: texto-estructurado
      invariantes_io:
        - "respuesta.urns_referenciados ⊆ conocimiento_permitido"
        - "respuesta.tiempo_generacion_ms <= contexto.qa_budget.latency.max_ms"
```

Dos artefactos con el mismo `api_observable` son **indistinguibles por
cualquier caller**; su diferencia queda en implementacion (plan, dominio,
narrativa del perfil), no en contrato externo.

Campo opcional en v1.1. Recomendado cuando el artefacto participa en
composicion con otros (`componible_con` no vacio).

#### 3.5.2 Budget de calidad (opcional)

Un artefacto **PUEDE** declarar `artefacto.contexto.qa_budget` para fijar pisos
y cotas operativas sobre calidad. Este campo es **serializacion**, no ontologia:
su semantica la gobierna `qa-spec`, no `autoria-spec`.

Forma canonica recomendada:

```yaml
artefacto:
  contexto:
    qa_budget:
      sigma_min: [0.67, 0.33, 0.67, 0.67, 0.33]
      latency:
        max_ms: 2000
      availability:
        min: 0.99
        window: "30d"
      mttr:
        max_s: 600
      cost:
        max_usd_per_turn: 0.05
```

Reglas:

1. `qa_budget` **PUEDE** omitirse en cualquier forma material.
2. Si se declara, **DEBERIA** usar la forma canonica anterior.
3. `qa_budget` **NO DEBE** contradecir `extensions.kora.vector_ontologico.sigma`;
   solo puede igualarlo o estrecharlo segun `qa-spec`.

#### 3.5.3 Risk register (opcional)

Un artefacto **PUEDE** declarar `artefacto.contexto.risk_register` para
materializar riesgos, mitigaciones y riesgo residual. Este campo es
**serializacion**; su semantica la gobierna `risk-register-spec`.

Forma canonica recomendada:

```yaml
artefacto:
  contexto:
    risk_register:
      - risk_id: qa-fallback-01
        category: quality
        source: fallback-chain
        trigger: "modelo primario indisponible"
        likelihood: 0.35
        impact: 0.40
        sigma_exposure: [0.0, 0.0, 0.1, 0.2, 0.0]
        mitigation: "forzar fallback con sigma_min intacto"
        residual_sigma_floor: [0.67, 0.33, 0.67, 0.67, 0.33]
        owner: runtime
        status: mitigated
```

Reglas:

1. `risk_register` **PUEDE** omitirse en cualquier forma material.
2. Si se declara, cada entrada **DEBERIA** ajustarse a la forma anterior.
3. `risk_register` **NO DEBE** reemplazar `compromisos_eticos`; documenta
   amenaza y mitigacion, no compromiso normativo.

## 4. Los tres atlas y el vector ontologico

### 4.1 Vector ontologico (autoritativo)

Definido por `harness-spec §3`. Seis ejes:

- `pi` ∈ {0..3} — Plan (monada libre).
- `mu` ∈ {0..3} — Materia (comonada libre).
- `xi` ∈ {0..4} — Interaccion.
- `lambda` ∈ {0..3} — Nivel sociotecnico.
- `phi` ∈ {0..4} — Acoplamiento humano.
- `sigma` ∈ [v1..v5], vᵢ ∈ {0..3} — Vector etico.

Ver `harness-spec §3.1-3.2` para la semantica de cada valor. Las leyes
inter-eje (§4.1 de harness-spec) aplican sin excepcion.

### 4.2 Atlas A — Arnes categorico

Pregunta que responde: **¿que clase de artefacto es estructuralmente?**

Enum cerrado (siete valores canonicos, slugs lowercase):

| Slug | Vector tipico | Descripcion |
|------|---------------|-------------|
| `utilidad` | Π=1, Μ=0, Ξ=1, Λ=0, Φ=1 | Funcion pura portable. |
| `disciplina` | Π=2, Μ=0, Ξ=1-2, Λ=0, Φ=1 | Cuerpo de conocimiento procedural. |
| `delegado` | Π=2, Μ=1, Ξ=2, Λ=0, Φ=1 | Scratchpad intra-invocacion. |
| `persona` | Π=2-3, Μ=2, Ξ=2-3, Λ=0-1, Φ=2 | Agente con identidad y estilo. |
| `orquestador` | Π=2-3, Μ=2, Ξ=4, Λ=1-2, Φ=2 | Coordina sub-agentes via operad dinamica. |
| `servicio` | Π=2, Μ=3, Ξ=3-4, Λ=1-2, Φ=1-2 | Agente always-on con materia ambiental. |
| `arquetipo` | meta | Meta-arnes: plantilla de familia de artefactos. |

`arquetipo` es **meta-arnes** — no se realiza directamente en un runtime,
sino que genera otros artefactos. Las runtime-extensions no lo listan
como soportado.

### 4.3 Atlas B — Forma material

Pregunta que responde: **¿como se materializa operacionalmente?**

Enum cerrado (cuatro valores canonicos):

| Slug | Descripcion |
|------|-------------|
| `habilidad` | Pieza portable, empaquetada, sin workspace propio. |
| `subagente` | Artefacto invocado por otro artefacto (no por humano). |
| `agente-propiamente-tal` | Artefacto con workspace productivo, ciclo propio. |
| `agente-plataforma` | Artefacto always-on en infraestructura de plataforma. |

Ver §5 para las reglas detalladas por forma material.

Una runtime-extension **PUEDE** declarar extensiones al atlas B (ej.
`subagente-task` como refinamiento de `subagente` para Claude Code). Estas
extensiones **DEBEN** declararse en la runtime-extension correspondiente
como "extension de atlas" — no pueden introducirse ad-hoc en artefactos.

### 4.4 Atlas C — Metafora relacional (HCAI)

Pregunta que responde: **¿como se relaciona con el humano?**

Enum (lectura Shneiderman, opcional):

| Slug | Vector (V, H) | Descripcion |
|------|---------------|-------------|
| `supertool` | (baja, alta) | Herramienta poderosa, humano al mando. |
| `telebot` | (alta, baja) | Agente autonomo, humano indirecto. |
| `electrodomestico-activo` | (baja, baja) | Dispositivo simple que sirve. |
| `centro-de-control` | (alta, alta) | Panel integrado con alta observabilidad. |

Los cuatro slugs son representantes canonicos de regiones; combinaciones
(V, H) no cubiertas son validas pero sin metafora nombrada.

### 4.5 Ortogonalidad de los tres atlas

Los tres atlas son **ejes independientes**: un mismo arnes categorico
puede materializarse en formas distintas, y cualquiera de ellas puede
llevar una metafora relacional distinta.

Ejemplos validos:

```yaml
# Delegado como habilidad
{ arnes_categorico: delegado, forma_material: habilidad, metafora_relacional: supertool }

# Delegado como subagente (mismo arnes, otra forma)
{ arnes_categorico: delegado, forma_material: subagente, metafora_relacional: supertool }

# Persona como subagente
{ arnes_categorico: persona, forma_material: subagente, metafora_relacional: centro-de-control }

# Persona como agente-propiamente-tal
{ arnes_categorico: persona, forma_material: agente-propiamente-tal, metafora_relacional: centro-de-control }

# Servicio — solo como agente-plataforma
{ arnes_categorico: servicio, forma_material: agente-plataforma, metafora_relacional: centro-de-control }
```

No todas las combinaciones son realizables en todos los runtimes; la
matriz de realizabilidad la gobierna cada runtime-extension (ver §12).

## 5. Las cuatro formas materiales

Cada forma material **DEBE** cumplir requisitos especificos de shape,
topologia y validacion. Las reglas se aplican condicionalmente segun el
valor de `atlas.forma_material`.

### 5.1 `habilidad` — Pieza portable

Dominio de proyeccion valido:
- Π ∈ {1, 2}
- Μ ∈ {0, 1}
- Ξ ∈ {1, 2}
- Λ = 0
- Φ = 1

Requisitos de shape:

- **DEBE** declarar `nivel_prescripcion` (alto, medio, bajo).
- **DEBE** seguir *progressive disclosure*: metadata en contexto,
  body lazy-load, recursos auxiliares bajo demanda.
- Body **≤ 500 lineas**. Si excede, separar en `referencias/`.
- `descripcion` **DEBE** ser clara y comprensiva (el runtime la usa para
  decidir activacion).
- `artefacto.composicion` **NO APLICA** (vector fuera de Ξ=4).
- `artefacto.contexto.memoria_config` **NO APLICA** (Μ=0-1).

Topologia:

```
{ns}/{nombre}/                      # con namespace
  SKILL.md                           # obligatorio, punto de entrada
  scripts/                           # opcional, automatizacion determinista
  referencias/                       # opcional, documentacion lazy-load
  recursos/                          # opcional, plantillas de salida
```

Subdirs opcionales (tres canonicos): `scripts/`, `referencias/`,
`recursos/`. Cualquier subdir adicional es invalido en `status: activo`.

El body **DEBE** tener seccion `## Recursos` si usa subdirs. Ver §5.5
para la proyeccion fiel a agentskills.io (que exige nombres en ingles
en el paquete publicado).

Ubicaciones validas:
- `artifacts/skills/{nombre}/SKILL.md` — top-level sin namespace.
- `artifacts/skills/{namespace}/{nombre}/SKILL.md` — con namespace.

Staging:
- `artifacts/skills/_TALLER/INBOX/{nombre}/` — pre-categorial.
- `artifacts/skills/_TALLER/REVIEW/{nombre}/` — con URN provisional.

### 5.2 `subagente` — Invocado por otro artefacto

Dominio de proyeccion valido:
- Π ∈ {1, 2, 3}
- Μ ∈ {0, 1, 2}
- Ξ ∈ {1, 2, 3}
- Λ = 0-1
- Φ ∈ {1, 2}

Requisitos de shape:

- **DEBE** declarar `artefacto.perfil.disparadores` (cuando lo invoca el
  padre).
- **DEBE** declarar `artefacto.interfaz` (contrato de invocacion).
- `artefacto.contexto.agente_padre` cuando aplica.
- `artefacto.composicion` **NO APLICA** (subagentes no orquestan).

Topologia:

```
artifacts/agents/{ns}/{nombre}/
  AGENT.md                           # obligatorio
  memoria/                           # opcional, si Μ≥2
  _BUILD/{target}/                   # gitignored, regenerable
```

Un subagente **PUEDE** vivir como archivo unico `AGENT.md` sin directorio
cuando Μ=0 y no requiere recursos auxiliares.

### 5.3 `agente-propiamente-tal` — Workspace productivo

Dominio de proyeccion valido:
- Π ∈ {2, 3}
- Μ ∈ {2, 3}
- Ξ ∈ {2, 3, 4}
- Λ ∈ {0, 1, 2}
- Φ ∈ {1, 2, 3}

Requisitos de shape:

- **DEBE** declarar las 6 dimensiones de `artefacto.*` (salvo
  `composicion` si Ξ<4).
- **DEBE** tener workspace productivo en `artifacts/agents/{ns}/{nombre}/`.
- `artefacto.invariantes` **DEBE** declarar `compromisos_eticos`.
- `artefacto.contexto.memoria_config` **DEBE** declararse si Μ≥2.

Topologia:

```
artifacts/agents/{ns}/{nombre}/
  AGENT.md                           # obligatorio
  memoria/                           # obligatorio si Μ≥2
  _BUILD/{target}/                   # gitignored
  _transmutation.yml                 # proof-carrying (por target)
```

Staging: `artifacts/agents/_FRAGUA/{INBOX,REVIEW}/`.

### 5.4 `agente-plataforma` — Always-on en infraestructura

Dominio de proyeccion valido:
- Π ∈ {2, 3}
- Μ = 3 (ambiental, obligatorio)
- Ξ ∈ {3, 4}
- Λ ∈ {1, 2, 3}
- Φ ∈ {1, 2, 3}

Requisitos de shape:

- **DEBE** declarar `extensions.{plataforma}.*` (ej. `openclaw`).
- **DEBE** declarar materia ambiental persistente (archivos
  `MEMORY.md`, `HEARTBEAT.md` u equivalentes segun runtime).
- `artefacto.composicion` **RECOMENDADO** si interactua con otros
  agentes de la plataforma.
- Entorno objetivo **DEBE** incluir al menos un runtime capaz de Μ=3
  (actualmente: solo `openclaw`).

Topologia: gobernada por el runtime de plataforma. Ver
`openclaw-runtime-extension` para el caso OpenClaw.

### 5.5 Proyeccion fiel a agentskills.io (solo `habilidad`)

Los artefactos con `forma_material: habilidad` **DEBEN** ser
transmutables byte-identical a paquetes agentskills.io-compatibles.

La transmutacion renombra:

| Campo KORA (es) | Campo agentskills.io (en) |
|------------------|----------------------------|
| `nombre` | `name` |
| `descripcion` | `description` |
| `entornos_objetivo` | `allowed-tools` (parcial) |
| `## Recursos` (body section) | `## Resources` |
| `referencias/` | `references/` |
| `recursos/` | `assets/` |
| `nivel_prescripcion` | (removido; es overlay KORA) |

Esta proyeccion es functorial y se ejecuta por:

```bash
python3 toolchain/kora transmute --agent ns/nombre --target agentskills
```

Check `fidelidad-agentskills`: genera paquete agentskills.io candidato y
verifica que es sintacticamente valido conforme al estandar externo. Si
falla, la habilidad no cumple la invariante de interop — es bug.

## 6. Validacion condicional por forma material

Matriz de aplicabilidad: que campos requiere o prohibe cada forma
material. Los checks correspondientes se resuelven al momento de
validar.

| Campo / regla | `habilidad` | `subagente` | `agente-propiamente-tal` | `agente-plataforma` |
|---------------|-------------|-------------|--------------------------|---------------------|
| `vector_ontologico` | requiere | requiere | requiere | requiere |
| `atlas.arnes_categorico` | {utilidad, disciplina, delegado} | {delegado, persona} | {persona, orquestador} | {orquestador, servicio} |
| `nivel_prescripcion` | requiere | no requiere | no requiere | no requiere |
| `artefacto.perfil` | requiere | requiere | requiere | requiere |
| `artefacto.plan` | condicional (Π≥1) | requiere | requiere | requiere |
| `artefacto.interfaz` | requiere | requiere | requiere | requiere |
| `artefacto.contexto.memoria_config` | prohibe (Μ≤1) | condicional (Μ≥2) | requiere si Μ≥2 | requiere (Μ=3) |
| `artefacto.contexto.qa_budget` | opcional | opcional | opcional | opcional |
| `artefacto.contexto.risk_register` | opcional | opcional | opcional | opcional |
| `artefacto.contexto.agente_padre` | no aplica | opcional | no aplica | no aplica |
| `artefacto.composicion` | prohibe | prohibe | condicional (Ξ=4) | opcional |
| `artefacto.invariantes.compromisos_eticos` | opcional | opcional | requiere | requiere |
| Workspace productivo | prohibe | opcional | requiere | requiere |
| Materia ambiental (`MEMORY.md` etc.) | prohibe | prohibe | condicional | requiere |
| `extensions.{plataforma}` | opcional | opcional | opcional | requiere al menos uno |
| Body en `SKILL.md` formato agentskills | requiere | no aplica | no aplica | no aplica |
| Seccion `## Recursos` si hay subdirs | requiere | no aplica | opcional | opcional |

Las runtime-extensions pueden agregar columnas y filas si extienden el
atlas B con slugs adicionales; esas extensiones **DEBEN** declararse
explicitamente.

## 7. Cuerpo Markdown

El body del archivo (`SKILL.md` para `habilidad`, `AGENT.md` para las
otras tres formas) es refinamiento legible del frontmatter. Reglas:

1. El body **NO DEBE** contradecir el frontmatter. Si hay conflicto,
   el frontmatter prevalece.
2. El body **PUEDE** agregar detalle operativo (workflow, ejemplos,
   disclaimers) que no cabe en YAML.
3. Las secciones estructurales (`## Recursos`, `## Plan`, `## Interfaz`,
   `## Invariantes`) son opcionales pero recomendadas para legibilidad.
4. El body **DEBE** estar en el idioma declarado en `lang`.
5. Referencias a archivos auxiliares **DEBERIAN** usar path relativo.

### 7.1 Secciones canonicas por forma material

| Seccion | `habilidad` | `subagente` | `agente-propiamente-tal` | `agente-plataforma` |
|---------|-------------|-------------|--------------------------|---------------------|
| `## Objetivo` | si | si | si | si |
| `## Cuando Usar` | si | si | si | si |
| `## Workflow` | si | si | si | si |
| `## Recursos` | si (si hay subdirs) | no | opcional | opcional |
| `## Plan` | opcional | si | si | si |
| `## Interfaz` | opcional | si | si | si |
| `## Invariantes` | opcional | si | si | si |
| `## Composicion` | no | no | si (Ξ=4) | opcional |
| `## Memoria` | no | si (Μ≥2) | si (Μ≥2) | si |
| `## Salida Esperada` | si | opcional | opcional | opcional |

## 8. Promocion entre formas materiales

Un artefacto **PUEDE** promoverse a una forma material superior en la
siguiente cadena:

```
habilidad → subagente → agente-propiamente-tal → agente-plataforma
```

### 8.1 Reglas de promocion

1. La promocion **DEBE** preservar el URN (`_manifest.urn`).
2. La promocion **DEBE** bumpear version **major** (cambio de `forma_material` es cambio incompatible del dominio de proyeccion, conforme a §10.3).
3. El nuevo `vector_ontologico` **DEBE** ser compatible con el dominio
   de la nueva forma material (§5).
4. Los campos del shape **DEBEN** expandirse para cumplir los requisitos
   de la nueva forma.
5. La topologia **DEBE** reorganizarse segun la nueva forma (ej.
   `artifacts/skills/{nombre}/` → `artifacts/agents/{ns}/{nombre}/`).
6. El artefacto **DEBE** declarar el evento de promocion en
   `provenance.source` o en historial de versiones.

### 8.2 Democion (descenso)

La democion (ir hacia una forma material inferior en la cadena) **NO
ESTA PERMITIDA**. Si un artefacto deja de necesitar su forma actual, se
**deprecia** y se emite uno nuevo con la forma deseada y URN distinto
que referencia al anterior via `supersedes`.

Razon: descender perderia estructura (memoria, composicion, workspace)
de forma no functorial, rompiendo trazabilidad.

### 8.3 Procedimiento de promocion

No hay CLI productiva para cambiar forma material. La promocion entre formas es
un cambio mayor de IR y se hace como procedimiento revisado:

1. crear rama o staging en `_FRAGUA/REVIEW/` o `_TALLER/REVIEW/`,
2. preservar `_manifest.urn`,
3. bumpear version major,
4. expandir el shape hasta satisfacer la matriz de §6,
5. correr `python3 toolchain/kora check --strict`,
6. documentar la promocion en `provenance.source` o historial de version.

El comando `python3 toolchain/kora promote` vigente aplica al pipeline de
knowledge `_SCRIPTORIUM`; **NO** promueve forma material de artefactos
agenticos.

## 9. Composicion (`componible_con`)

Un artefacto **PUEDE** declarar artefactos con los que se compone:

```yaml
extensions:
  kora:
    componible_con:
      - "urn:kora:artefacto:atomizar"
      - "urn:kora:artefacto:cat-thinking"
```

### 9.1 Semantica categorica

La composicion es **categorica**, no anidamiento fisico:

- Composicion Kleisli cuando los artefactos comparten monada de efectos.
- Composicion de profunctores cuando tienen interfaces compatibles.
- Composicion operadica cuando un orquestador compone sub-artefactos
  (Ξ=4).

Ver `harness-spec §6` y el corpus categorico para fundamentos.

### 9.2 Resolucion de conflictos

Cuando dos artefactos componibles tienen reglas conflictivas (ej. ambos
declaran `invariantes.reglas_duras` incompatibles), la resolucion es:

1. El artefacto de nivel superior (ej. orquestador) prevalece.
2. Si ambos son del mismo nivel, prevalece el que se invoca primero.
3. Si coinciden en timing, el toolchain emite error y exige declaracion
   explicita de prioridad.

## 10. Identidad URN y versionado

### 10.1 Regimen unificado

Todo artefacto agentico usa **un solo regimen URN**:

```
urn:{namespace}:artefacto:{id}
```

- El URN **NO** lleva version embebida.
- La version se declara en el campo `version` del frontmatter.
- Referencias a artefactos usan el URN sin version para apuntar al
  "ultimo activo", y con `@version` para fijar.

Este regimen reemplaza los regimenes previos `urn:{ns}:agent:{id}` (de
agentfile) y `urn:{ns}:skill:{id}:{version}` (de skill-overlay), que
eran divergentes.

### 10.2 Migracion del regimen (una sola pasada)

Artefactos bajo los regimenes anteriores se migran con:

```bash
python3 toolchain/kora migrate --perfil a-autoria
```

El toolchain:
1. Renombra `agent:` → `artefacto:` y `skill:` → `artefacto:` en URNs.
2. Si el URN tenia `:{version}` embebida, la extrae al campo `version`.
3. Reemite URN canonico `urn:{ns}:artefacto:{id}` sin pointer de
   compatibilidad. El URN anterior deja de resolver.
4. Reescribe referencias cruzadas (`componible_con`,
   `conocimiento_permitido`, etc.) al URN nuevo.

El tooling **NO** mantiene aliasing dual: tras la migracion, el URN
anterior es invalido. Quien necesite trazabilidad historica consulta
`git log` del artefacto, no el catalogo vivo.

### 10.3 Bump semantico

- **Patch** (X.Y.Z): correccion de redaccion, fix en scripts.
- **Minor** (X.Y): nueva capacidad compatible, expansion de
  `componible_con`.
- **Major** (X): cambio en dominio de proyeccion, cambio de
  `arnes_categorico`, cambio de `forma_material`.

## 11. Ciclo de vida

Delegado a `gobernanza §5`. Estados:

```
borrador → activo → deprecado → retirado
```

Las transiciones inversas son **invalidas**. Un artefacto retirado no es
reactivable — se emite uno nuevo con `supersedes`.

## 12. Relacion con runtime-extensions

Cada runtime-extension declara una **matriz de realizabilidad** sobre el
espacio `(arnes_categorico, forma_material)`. Ejemplos:

| Runtime | `habilidad` | `subagente` | `agente-propiamente-tal` | `agente-plataforma` |
|---------|-------------|-------------|--------------------------|---------------------|
| Claude Code | fiel | fiel | fiel | no soportado |
| Codex | fiel | fiel (budget) | parcial | no soportado |
| Gemini | fiel | fiel (budget) | parcial | no soportado |
| OpenCode | fiel | fiel | parcial | no soportado |
| OpenClaw | fiel | fiel | fiel | fiel (unico) |

`fiel` = dominio de preservacion completa. `parcial` = proyeccion con
perdida declarada en `_transmutation.yml`. `no soportado` = el runtime
rechaza la combinacion.

Las runtime-extensions **DEBEN** declarar esta matriz en su §3 y mantener
coherencia con `autoria-spec §5` (dominio de proyeccion por forma
material).

## 13. Ruptura y migracion forzada

### 13.1 Ruptura normativa

Esta spec es la **unica fuente** de autoria de artefactos agenticos
productivos. Sus antecesoras `agentfile-spec` y `skill-overlay-spec`
estan **retiradas** — no estan en las capas normativas vigentes, no
tienen URN resoluble.

Nuevos artefactos **NO PUEDEN** nacer en ninguna forma que no sea la
de esta spec. No se acepta declaracion implicita de ontologia, no se
acepta shape de seis componentes legacy, no se acepta URN de regimenes
anteriores.

### 13.2 Migracion en una sola pasada

Todo artefacto pre-existente se migra con:

```bash
python3 toolchain/kora migrate --perfil a-autoria
```

La migracion es **una pasada unica**: re-emite URN canonico, re-escribe
frontmatter al shape unificado, re-ubica archivos segun `forma_material`,
borra scaffolds legacy del workspace (`SOUL.md`, `IDENTITY.md`,
`USER.md`, `TOOLS.md`, `config.json` del formato v1 agentfile).

Tras la migracion, el workspace contiene solo:

- `AGENT.md` o `SKILL.md` conforme a esta spec.
- Subdirs canonicos (`memoria/`, `referencias/`, `recursos/`, `scripts/`).
- `_BUILD/` para outputs de transmutacion (gitignored).
- `_transmutation.yml` para agentes con dominio proyectable.

Archivos pre-existentes fuera de esa lista **se eliminan**. Su contenido,
si tiene valor historico, vive en `git log`.

### 13.3 Excepcion: `AGENTS.md` de OpenClaw

El unico archivo legacy que sobrevive es `AGENTS.md` (plural) cuando
pertenece al runtime OpenClaw. No es shape de autoria — es archivo de
runtime, regulado por `openclaw-runtime-extension` y emitido por
`kora transmute --target openclaw`. Nunca es fuente primaria; siempre
es derivado del shape unificado.

No debe confundirse con el `AGENTS.md` del formato v1 de agentfile, que
esta **retirado** junto al resto.

### 13.4 Plazo

La migracion forzada se completa antes de que se emita cualquier
artefacto agentico nuevo. No hay convivencia transitoria. El toolchain
`kora check --strict` **rechaza** cualquier artefacto que no cumpla esta
spec desde su adopcion.

## 14. Validacion estructural

Checks canonicos sobre artefactos conformes a esta spec:

| Check | Condicion | Severidad | Enforcement | Aplicabilidad |
|-------|-----------|-----------|-------------|---------------|
| `envelope-valido` | Frontmatter cumple §3. | alta | schema | toda forma |
| `manifest-type-artefacto` | `_manifest.type = artefacto`. | alta | schema | toda forma |
| `vector-ontologico-presente` | `extensions.kora.vector_ontologico` declarado. | alta | schema | toda forma |
| `vector-rango-valido` | Valores cumplen rangos de `harness-spec §3.1`. | alta | schema | toda forma |
| `leyes-inter-eje` | Vector cumple `harness-spec §4.1`. | alta | lint | toda forma |
| `forma-material-declarada` | `atlas.forma_material` es slug canonico. | alta | schema | toda forma |
| `dominio-forma-material` | Vector cumple dominio de §5 para la forma. | alta | lint | toda forma |
| `arnes-compatible-con-forma` | Par `(arnes, forma)` esta en tabla §6. | alta | lint | toda forma |
| `shape-condicional` | Campos de `artefacto.*` cumplen §6. | alta | lint | toda forma |
| `topologia-valida` | Ubicacion fisica coincide con §5. | media | lint | toda forma |
| `recursos-documentados` | Si hay subdirs, body tiene `## Recursos`. | media | lint | `habilidad` |
| `progressive-disclosure` | Body ≤ 500 lineas. | media | lint | `habilidad` |
| `fidelidad-agentskills` | Transmute a agentskills.io produce paquete valido. | alta | runtime | `habilidad` |
| `fidelidad-mastra` | Dry-run a Mastra cae en dominio declarado y conserva perdida explicita. | alta | runtime | `subagente`, `agente-propiamente-tal`, `agente-plataforma` |
| `memoria-declarada` | Si Μ≥2, `contexto.memoria_config` presente. | media | lint | `subagente` y superiores |
| `compromisos-eticos` | `invariantes.compromisos_eticos` declarado. | alta | lint | `agente-propiamente-tal`, `agente-plataforma` |
| `extension-runtime-plataforma` | Al menos un `extensions.{plataforma}` declarado. | alta | schema | `agente-plataforma` |
| `sigma-consistencia` | Σ en vector coincide con `compromisos_eticos` expandido. | media | manual | toda forma |
| `body-subordinado` | Body no contradice frontmatter. | media | manual | toda forma |
| `referencias-resolubles` | URNs en `componible_con`, `conocimiento_permitido` existen; excepcion: `supersedes` hacia URNs retirados permitido. | baja | lint | toda forma |
| `entornos-objetivo-soportan` | Cada runtime en `entornos_objetivo` soporta `(arnes, forma)`. | alta | lint | toda forma |

## 15. Glosario de identificadores

Los identificadores YAML y de topologia usan castellano descriptivo.
Esta tabla es la fuente canonica:

### 15.1 Frontmatter

| Identificador | Tipo | Proposito |
|---------------|------|-----------|
| `nombre` | string | Identificador humano del artefacto. |
| `descripcion` | string | Disparador y uso, una linea. |
| `vector_ontologico` | objeto | Los 6 ejes PMI × LFS. |
| `presentacion` | enum | `estado-primario` o `accion-primaria`. |
| `atlas.arnes_categorico` | slug | Clase estructural (atlas A). |
| `atlas.forma_material` | slug | Materializacion operacional (atlas B). |
| `atlas.metafora_relacional` | slug | Lectura HCAI (atlas C, opcional). |
| `entornos_objetivo` | lista | Runtimes soportados. |
| `nivel_prescripcion` | enum | `alto`, `medio`, `bajo` (solo `habilidad`). |
| `conocimiento_permitido` | lista | URNs de KB referenciables. |
| `componible_con` | lista | URNs de artefactos componibles. |
| `risk_register` | lista | Ledger opcional de riesgos tipados y mitigaciones. |

### 15.2 Shape del artefacto

| Identificador | Equivalente v1 | Proposito |
|---------------|-----------------|-----------|
| `artefacto.perfil` | `agent.profile` | Descripcion operativa. |
| `artefacto.plan` | `agent.plan` | FSM del artefacto. |
| `artefacto.interfaz` | `agent.interface` | Contrato de herramientas. |
| `artefacto.contexto` | `agent.context` | Memoria, operador, KB refs. |
| `artefacto.composicion` | `agent.composition` | Sub-artefactos. |
| `artefacto.invariantes` | `agent.invariants` | Reglas, guardrails, etica. |

### 15.3 Topologia

| Identificador | Equivalente previo |
|---------------|---------------------|
| `referencias/` | `references/` |
| `recursos/` | `assets/` |
| `scripts/` | `scripts/` (sin cambio, es internacional) |
| `memoria/` | `memory/` |
| `_BUILD/` | `_BUILD/` (sin cambio, marcador de salida) |
| `_transmutation.yml` | sin cambio |
| `artifacts/agents/_FRAGUA/` | sin cambio |
| `artifacts/skills/_TALLER/` | sin cambio |

## 16. Ejemplos completos

### 16.1 Habilidad de Utilidad (atomizar)

```yaml
---
_manifest:
  urn: "urn:kora:artefacto:atomizar"
  type: artefacto
  provenance:
    created_by: "FS"
    created_at: "2026-04-17"
    source: "Productor canonico familia atomic (knowledge-spec §12)."
version: "1.0.0"
status: activo
nombre: atomizar
descripcion: "Extrae proposiciones atomicas de carpetas de documentos y emite artefactos KORA/MD de familia atomic."
tags: [atomizacion, knowledge, productor]
lang: es
extensions:
  kora:
    vector_ontologico:
      pi: 2
      mu: 0
      xi: 1
      lambda: 0
      phi: 1
      sigma: [1,1,3,1,0]
    presentacion: estado-primario
    atlas:
      arnes_categorico: utilidad
      forma_material: habilidad
      metafora_relacional: supertool
    entornos_objetivo: [claude-code, codex, gemini, mastra, opencode, openclaw]
    nivel_prescripcion: medio
    conocimiento_permitido:
      - "urn:kora:kb:md-spec"
      - "urn:kora:kb:knowledge-spec"
    componible_con: []
---

# Atomizar

Use esta habilidad cuando el usuario necesite extraer proposiciones
atomicas de un corpus.

## Objetivo

Producir artefactos KORA/MD familia `atomic` conformes a md-spec §12.

## Cuando Usar

- Usar cuando el corpus es denso y RAG no es practico.
- No usar cuando el corpus es pequeno (<10 paginas).

## Workflow

1. Inspeccionar la estructura del corpus.
2. Segmentar el texto en unidades de 5K chars o 200 proposiciones.
3. Extraer proposiciones con tipo (requirement, definition, rule, ...).
4. Deduplicar multi-source con tension declarada en conflictos.
5. Emitir archivos en `artifacts/knowledge/_SCRIPTORIUM/REVIEW/`.

## Recursos

### Scripts
Usa archivos bajo `scripts/` para segmentacion y extraccion.

### Referencias
Usa archivos bajo `referencias/` para tipos canonicos de proposiciones.

## Salida Esperada

Archivos `.md` con frontmatter familia `atomic` y body con proposiciones
enumeradas.
```

### 16.2 Agente-propiamente-tal de Persona (goreologo)

```yaml
---
_manifest:
  urn: "urn:gn:artefacto:goreologo"
  type: artefacto
  provenance:
    created_by: "FS"
    created_at: "2026-04-17"
    source: "Agente persona del dominio GORE, workspace productivo."
version: "2.0.0"
status: activo
nombre: goreologo
descripcion: "Agente especialista en gobierno regional — normativa, presupuesto, politicas publicas."
tags: [persona, gore, gobierno-regional]
lang: es
extensions:
  kora:
    vector_ontologico:
      pi: 2
      mu: 2
      xi: 2
      lambda: 1
      phi: 2
      sigma: [2,2,2,2,1]
    presentacion: estado-primario
    atlas:
      arnes_categorico: persona
      forma_material: agente-propiamente-tal
      metafora_relacional: centro-de-control
    entornos_objetivo: [claude-code, openclaw]
    conocimiento_permitido:
      - "urn:gn:kb:normativa-gore"
      - "urn:gn:kb:presupuesto-publico"
    componible_con: []
  claude_code:
    model: opus
    color: blue
    max_turns: 20
    memory: user
  openclaw:
    bot_handler: telegram
    acp_compliant: true
artefacto:
  perfil:
    dominio: [gore, gobierno-regional, politicas-publicas]
    disparadores: [consulta-normativa, analisis-presupuesto]
    salidas: [analisis, recomendacion, resumen]
  plan:
    estado_inicial: recibir-consulta
    estado_terminal: entregar-analisis
    estados: [comprension, investigacion, analisis, sintesis]
  interfaz:
    herramientas: [Read, Grep, Glob, WebFetch]
    permisos: lectura-corpus
  contexto:
    memoria_config:
      tipo: persistente
      ambito: usuario
    perfil_operador: tecnico-gore
  invariantes:
    reglas_duras:
      - "No inventar cifras presupuestarias; citar fuente."
    compromisos_eticos:
      safety_norm: "Alta; dominio sensible a politicas publicas."
      fairness: "Media-alta; balance ideologico."
      transparency: "Alta; citar normativa."
      accountability: "Media; user en control."
      sustainability: "Baja; no aplica directamente."
---

# Goreologo

Agente persona especializado en gobierno regional de Chile.

## Objetivo
...
```

### 16.3 Agente-plataforma de Servicio (clawforge)

```yaml
---
_manifest:
  urn: "urn:kora:artefacto:clawforge"
  type: artefacto
  provenance:
    created_by: "FS"
    created_at: "2026-04-17"
    source: "Agente-plataforma always-on de gestion de flotas OpenClaw."
version: "1.0.0"
status: activo
nombre: clawforge
descripcion: "Servicio OpenClaw de gestion de flotas — spawns, doctoring, lifecycle de agentes."
tags: [servicio, openclaw, gestion-flota]
lang: es
extensions:
  kora:
    vector_ontologico:
      pi: 2
      mu: 3
      xi: 3
      lambda: 2
      phi: 2
      sigma: [3,2,3,3,2]
    presentacion: accion-primaria
    atlas:
      arnes_categorico: servicio
      forma_material: agente-plataforma
      metafora_relacional: centro-de-control
    entornos_objetivo: [openclaw]
    conocimiento_permitido:
      - "urn:kora:kb:openclaw-runtime-extension"
  openclaw:
    bot_handler: telegram
    acp_compliant: true
    persistencia: ambiental
    always_on: true
artefacto:
  perfil:
    dominio: [openclaw, fleet-management]
  plan:
    estado_inicial: escuchar
    estados: [escuchar, spawn, doctor, lifecycle]
  interfaz:
    herramientas: [systemctl, openclaw-cli]
  contexto:
    memoria_config:
      tipo: ambiental
      archivos: [MEMORY.md, HEARTBEAT.md]
  composicion:
    sub_agentes: [korvo, kora-salubrista, digitrans]
    ruteo_eventos: telegram-intent-routing
  invariantes:
    compromisos_eticos:
      safety_norm: "Alta; gestiona infraestructura productiva."
      accountability: "Alta; requiere audit log."
      transparency: "Alta; decisions logged."
---

# Clawforge

Servicio OpenClaw de gestion de flota de agentes.

## Objetivo
...
```
