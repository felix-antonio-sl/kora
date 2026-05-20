---
_manifest:
  urn: "urn:kora:kb:spec-md"
  provenance:
    created_by: "Claude Opus 4.7"
    created_at: "2026-05-20"
    source: "KORA v9 (HITL 2026-05-20, urn:kora:kb:adr-kora-v9-separacion-descriptivo-prescriptivo-y-arnes): extraccion del perfil prescriptivo desde md-spec v10 (§5.6.1.1-§5.6.1.9, §7.6, 9 filas spec en §9) a una spec dedicada. La URN urn:kora:kb:spec-md regresa al canon despues de haber sido absorbida por md-spec v8.0 (2026-04-16)."
version: "1.0.0"
status: publicado
tags: [spec, prescriptivo, rfc2119, cristalizacion, traces-to, normativo]
lang: es
extensions:
  kora:
    family: spec
relations:
  depends:
    - "urn:kora:kb:gobernanza"
    - "urn:kora:kb:md-spec"
  cites:
    - "urn:kora:kb:05-governance-lattice"
    - "urn:kora:kb:adr-kora-v9-separacion-descriptivo-prescriptivo-y-arnes"
---

# KORA/Spec-MD v1.0.0

## 1. Definicion

Esta spec define el **perfil prescriptivo** del formato KORA/MD. Un
documento `spec` es un artefacto KORA/MD descriptivo (gobernado por
`md-spec`) **mas** los invariantes prescriptivos de esta spec.

KORA distingue dos regimenes pragmaticos:

- **Descriptivo**: artefactos que describen hechos, procedimientos o
  referencias. Gobernado por `md-spec`.
- **Prescriptivo**: artefactos que gobiernan comportamientos, contratos
  y validaciones (specs, protocolos, workflows normativos). Gobernado
  por **esta spec** mas el envelope de `md-spec`.

Todo documento de familia `spec` (declarada via
`extensions.{namespace}.family: spec`) **DEBE** cumplir tanto los
invariantes generales de `md-spec` como los invariantes prescriptivos
de esta spec.

### 1.1 Alcance

Gobierna:

1. Lenguaje de obligacion (RFC 2119) en documentos normativos.
2. Convencion de trazabilidad (`Traces to:` / `Rationale:`).
3. Elementos retoricos normativos.
4. Patron obligatorio regla + ejemplo + traza.
5. Invariantes prescriptivos (consistencia interna, auto-suficiencia,
   no-circularidad, idioma, enforcement declarado).
6. Template esqueleto minimo.
7. Invariante de auto-declaracion de precedencia.

### 1.2 Lo que NO gobierna esta spec

- **Envelope, gramatica y familias descriptivas**: gobernado por
  `md-spec`.
- **Pipeline de curacion, lifecycle, identidad URN conceptual**:
  gobernado por `knowledge-spec`.
- **Shape de artefactos agenticos (skills, agents)**: gobernado por
  `autoria-spec`.

### 1.3 Audiencia

Audiencia primaria: editores y agentes que producen specs canonicas
(`governance/`, `ontology/`, `serialization/`, `runtime/`).

Audiencia secundaria: consumidores que necesitan distinguir reglas
prescriptivas de prosa descriptiva.

### 1.4 Precedencia

Esta spec vive en capa de **serializacion** (`gobernanza §3`). Cuando
tensiona con otra spec:

1. `gobernanza` decide precedencia constitucional.
2. `md-spec` define el envelope y gramatica base; esta spec **NO DEBE**
   relajar el contrato de md-spec.
3. Esta spec define el perfil prescriptivo encima del envelope.

## 2. Definiciones

| Termino | Definicion |
|---------|------------|
| Documento `spec` | Artefacto KORA/MD con `family: spec` que define lo que debe ser (reglas, contratos, validaciones). |
| Keyword (RFC 2119) | Palabra reservada que fija fuerza normativa: DEBE, NO DEBE, DEBERIA, NO DEBERIA, PUEDE. Enum cerrado. |
| Regla | Oracion con keyword RFC 2119 y semantica operativa univoca. |
| Cristalizacion | Proceso `Decisiones + Practicas + Restricciones → regla explicita con una sola lectura valida`. |
| Rationale | Explicacion auxiliar no normativa sobre motivacion; no introduce obligaciones. |
| Traces to | Puente entre una regla operacional y su justificacion en la Formal Layer oficial. |
| Auto-suficiencia | Propiedad de una regla que puede entenderse con su propio contexto local. |
| No-circularidad | Propiedad de una regla que no se justifica solo remitiendo a otra regla igual de opaca. |

## 3. Proceso de cristalizacion

La cristalizacion transforma decisiones, practicas y restricciones
implicitas en reglas explicitas con una sola lectura valida.

Traces to: `urn:kora:kb:05-governance-lattice` §2.3 (Crystallization Functor C)

Entrada:

- decisiones de diseño
- practicas existentes
- restricciones tecnicas, organizacionales o legales

Salida:

- documento prescriptivo con reglas explicitas, rationale y validacion

Propiedades del funtor de cristalizacion:

1. **Cristalizador** — lo implicito se vuelve regla explicita.
2. **Formalizador** — cada regla queda con una lectura operativa univoca.
3. **Desambiguador** — el hedging y la vaguedad se eliminan.
4. **Ejemplificador** — las reglas complejas se anclan con
   `Correcto:` / `Incorrecto:`.

## 4. Lenguaje de obligacion (RFC 2119)

Keywords normativas permitidas (enum cerrado):

- **DEBE**
- **NO DEBE**
- **DEBERIA**
- **NO DEBERIA**
- **PUEDE**

Reglas:

1. Toda obligacion importante en un documento `spec` **DEBE** usar una
   keyword RFC 2119.
2. El hedging normativo ("probablemente", "seria bueno", "idealmente")
   **NO DEBE** reemplazar una keyword.
3. Las keywords en español **DEBEN** escribirse en mayusculas.
4. La equivalencia inglesa (MUST, MUST NOT, SHOULD, SHOULD NOT, MAY)
   **PUEDE** aparecer en la primera mencion, no en todas.

## 5. Convencion de trazabilidad

Una regla con justificacion formal oficial **DEBERIA** incluir una linea:

```markdown
Traces to: `urn:kora:kb:{slug}` §{seccion} ({teorema})
```

Reglas:

1. `Traces to:` **DEBE** apuntar solo a la Formal Layer oficial
   (`artifacts/knowledge/kora/categorical-foundations/`), usando el URN
   canonico del artefacto formal (`urn:kora:kb:{slug}`) seguido del
   numero de seccion y, opcionalmente, el nombre del teorema.
2. No se admite path relativo (`formal/05`) ni alias no resolubles: la
   identidad del artefacto formal se expresa por URN (`gobernanza §4.3`).
3. Una regla pragmatica **NO DEBE** fingir respaldo formal: si la
   justificacion es pragmatica, se usa `Rationale:`.
4. `Rationale:` **PUEDE** explicar motivos conceptuales o pragmaticos,
   pero **NO DEBE** introducir obligaciones nuevas.
5. La ausencia de `Traces to:` no debilita la fuerza normativa de una
   regla.

Traces to: `urn:kora:kb:05-governance-lattice` §3.2 (Traceability Functor)

Rationale: el URN canonico es identidad estable (Yoneda); los paths
relativos mezclan identidad con ubicacion fisica y se rompen al
reorganizar la Formal Layer.

## 6. Elementos retoricos normativos

El perfil `spec` admite tres elementos retoricos normativos adicionales
a los tipograficos de `md-spec §5.2`:

| Elemento | Uso permitido | Funcion prohibida |
|----------|---------------|---------------------|
| `Correcto:` / `Incorrecto:` | anclar la interpretacion de una regla | decoracion |
| `Rationale:` | registrar motivacion no normativa | introducir deberes nuevos |
| Tabla de validacion | checks y enforcement declarativo | listado estetico sin criterio |

## 7. Prosa explicativa admisible

La prosa explicativa en un documento `spec` **PUEDE** existir solo
cuando cumple una de estas cuatro funciones normativas (lista
exhaustiva):

1. justificar una regla
2. prevenir ambiguedad
3. contextualizar una restriccion
4. advertir un limite del enforcement

Prosa que no satisface ninguna de estas cuatro funciones es grasa y
**DEBE** eliminarse conforme a `md-spec §5.3`.

## 8. Patron obligatorio: regla + ejemplo + traza

Toda regla con mas de una condicion, alcance no obvio, o riesgo de
interpretacion divergente **DEBE** seguir este patron:

1. Regla normativa con keyword RFC 2119.
2. `Correcto:` / `Incorrecto:` cuando la regla admita mala lectura.
3. `Traces to:` si la regla tiene respaldo formal oficial; `Rationale:`
   si la justificacion es pragmatica.

Reglas:

1. La ausencia de `Traces to:` no debilita la fuerza normativa.
2. `Rationale:` **NO DEBE** introducir obligaciones nuevas.
3. Un ejemplo **NO DEBE** reemplazar la regla; la ancla.

Ejemplo:

```markdown
Toda regla pragmatica **DEBE** declararse con keyword explicita.

Correcto: `La herramienta declara su nivel de enforcement en tabla de validacion.`
Incorrecto: `Seria bueno indicar como se verifica.`
Rationale: La auditabilidad requiere distinguir schema, lint, runtime y manual.
```

## 9. Invariantes prescriptivos

Ademas de los invariantes generales de `md-spec §7`, un documento
`spec` **DEBE** cumplir:

1. **Consistencia interna** — no contiene reglas incompatibles entre si
   sin una clausula de precedencia o excepcion explicita.
2. **Auto-suficiencia de la regla** — toda regla importante puede
   entenderse con su propio contexto local, sin depender de una lectura
   telepatica del repositorio.
3. **No-circularidad** — una regla **NO DEBE** justificarse solo
   remitiendo a otra regla igual de opaca. Si depende de otra, la
   dependencia **DEBE** aclarar que agrega o restringe.
4. **Preservacion de idioma y anglicismos** — el documento mantiene
   idioma consistente. Los anglicismos **PUEDEN** usarse si nombran
   terminos tecnicos inevitables, pero **NO DEBEN** reemplazar una regla
   ya expresable en español.
5. **Enforcement declarado** — toda tabla de validacion **DEBE** incluir
   columna `Enforcement` con valor de `gobernanza §7` (`schema`, `lint`,
   `runtime`, `eval`, `manual`).
6. **Integridad del perfil prescriptivo** — los invariantes anteriores
   son constitutivos del perfil; violarlos invalida el caracter
   prescriptivo del documento.

## 10. Template esqueleto minimo

Todo documento `spec` nuevo **DEBERIA** arrancar desde este esqueleto.
Las sub-reglas marcadas con **DEBE** dentro del esqueleto son
obligatorias independientemente del caracter recomendatorio del
template:

1. `## 1. Definicion` (incluye alcance y audiencia).
2. `## 2. Definiciones` de terminos usados normativamente.
3. `## 3-N. Secciones normativas` numeradas secuencialmente.
4. `## N+1. Invariantes`.
5. `## N+2. Validacion` (tabla con `Enforcement` obligatoria).
6. `## N+3. Ejemplos` (opcional).
7. `## N+4. Migracion` — **DEBE** incluirse en major bumps; opcional en
   minor/patch. En major bumps documenta: (1) que cambio, (2) que
   migrar, (3) que se depreca.

## 11. Invariante de auto-declaracion

El propio documento `spec` **DEBE** declarar al inicio su
**precedencia** en la jerarquia de specs, conforme a `gobernanza §3.4`
(regla de especializacion). La declaracion **PUEDE** ser el frontmatter
`relations.depends` o una seccion `## Precedencia` explicita.

## 12. Validacion

| Check | Criterio | Enforcement | Spec ref |
| --- | --- | --- | --- |
| Keyword explicita | Toda obligacion importante usa keyword RFC 2119 | lint | §4 |
| Trazabilidad oficial | `Traces to:` referencia solo Formal Layer oficial | lint | §5 |
| Patron de regla | Reglas complejas que admitan mala lectura incluyen `Correcto:/Incorrecto:`; toda regla con justificacion disponible incluye `Traces to:` o `Rationale:` | manual | §8 |
| Consistencia interna | No hay contradicciones no resueltas | manual | §9 r1 |
| Auto-suficiencia de regla | Reglas se entienden sin contexto omitido critico | manual | §9 r2 |
| No-circularidad | Referencias normativas no forman bucles opacos | manual | §9 r3 |
| Enforcement declarado | Toda tabla de validacion incluye columna `Enforcement` | lint | §9 r5 |
| Template prescriptivo | Documento sigue esqueleto §10 | manual | §10 |
| Migracion en major | Major bumps incluyen seccion `## Migracion` | lint | §10 r7 |

## 13. Migracion

### 13.0 Contrato vigente v1

Esta spec **regresa al canon** despues de haber sido absorbida por
`md-spec v8.0` (2026-04-16). La directiva HITL del operador (2026-05-20,
`urn:kora:kb:adr-kora-v9-separacion-descriptivo-prescriptivo-y-arnes`)
restaura la separacion entre regimen descriptivo y prescriptivo.

Cambios respecto a la absorcion previa:

- El contenido prescriptivo de `md-spec §5.6.1.1-§5.6.1.9` migra a esta
  spec como §3-§11.
- `md-spec §7.6` (integridad perfil prescriptivo) migra a esta spec
  como §9 r6.
- 9 filas de validacion en `md-spec §9` (Keyword explicita,
  Trazabilidad oficial, Patron de regla, Consistencia interna,
  Auto-suficiencia, No-circularidad, Enforcement declarado, Template
  prescriptivo, Migracion en major) migran a §12 de esta spec.
- URN `urn:kora:kb:spec-md` regresa al catalogo activo. Refs
  historicas a este URN (que apuntaban a versiones pre-v8) resuelven
  ahora a esta v1.0; no es retro-compatibilidad estricta, es
  reactivacion.

### 13.1 Que migrar

- Refs cruzadas a `md-spec §5.6.1.X` (perfil spec) reapuntan a
  `spec-md §X` correspondiente.
- Refs cruzadas a `md-spec §7.6` reapuntan a `spec-md §9 r6`.
- Refs cruzadas a checks `Keyword explicita (spec)`, `Trazabilidad
  oficial (spec)`, etc. reapuntan a `spec-md §12`.

### 13.2 Que se depreca

- Nada. La separacion no depreca contenido; solo lo relocaliza.
- El URN `urn:kora:kb:spec-md` deja de ser nodo deprecado/retirado y se
  vuelve nodo activo.
