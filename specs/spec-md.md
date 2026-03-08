---
_manifest:
  urn: "urn:kora:kb:spec-md"
  provenance:
    created_by: "FS"
    created_at: "2026-03-08"
    source: "RFC 2119, KORA categorical-foundations 05, KORA/Gobernanza v3.0.0, repair of crystallization contract"
version: "5.0.0"
status: published
tags: [spec, prescriptivo, formato, crystallization, enforcement, traces]
lang: es
---

# KORA/Spec-MD v5.0.0

## 1. Definicion

KORA/Spec-MD es el formato de ley operativa del ecosistema KORA. Sirve para especificaciones, protocolos, workflows y documentos prescriptivos. No describe hechos: gobierna comportamientos, contratos y validaciones.

### 1.1 Alcance y audiencia

Su audiencia primaria son runtimes y agentes que consumen ley operativa. La audiencia secundaria son humanos que diseñan, auditan o evolucionan el ecosistema KORA.

Todo documento prescriptivo de KORA **DEBE** redactarse conforme a esta especificacion. Un documento descriptivo **NO DEBE** gobernarse por Spec-MD.

### 1.2 Proceso de cristalizacion

La cristalizacion transforma decisiones, practicas y restricciones implicitas en reglas explicitas con una sola lectura valida.

Traces to: formal/05 §2.3 (Crystallization Functor C)

Entrada:

- decisiones de diseño
- practicas existentes
- restricciones tecnicas, organizacionales o legales

Salida:

- documento prescriptivo con reglas explicitas, rationale y validacion

Propiedades:

1. Cristalizador: lo implicito se vuelve regla explicita.
2. Formalizador: cada regla queda con una lectura operativa univoca.
3. Desambiguador: el hedging y la vaguedad se eliminan.
4. Ejemplificador: las reglas complejas se anclan con `Correcto:` / `Incorrecto:`.

### 1.3 Convencion de trazabilidad

Una regla con justificacion formal oficial **DEBERIA** incluir una linea:

```markdown
Traces to: formal/{doc} §{seccion} ({teorema})
```

Reglas:

1. `Traces to:` **DEBE** apuntar solo a la Formal Layer oficial.
2. Una regla pragmatica **NO DEBE** fingir respaldo formal.
3. `Rationale:` explica motivos conceptuales o pragmaticos, pero no agrega obligaciones nuevas.

Traces to: formal/05 §3.2 (Traceability Functor)

## 2. Definiciones

| Termino | Definicion |
| --- | --- |
| Documento prescriptivo | Artefacto que define lo que debe ser |
| Regla | Oracion con keyword RFC 2119 y semantica operativa |
| Cristalizacion | Proceso `Decisiones + Practicas + Restricciones -> Spec-MD` |
| Rationale | Explicacion auxiliar no normativa |
| Traces to | Puente entre regla operacional y justificacion formal |
| Auto-suficiencia | La regla se entiende sin depender de contexto omitido o implicito |
| No-circularidad | La regla no se justifica solo remitiendo a otra regla igual de opaca |

## 3. Anatomia del documento

Todo documento KORA/Spec-MD **DEBE** tener:

1. Frontmatter YAML base.
2. Cuerpo prescriptivo Markdown.

### 3.1 Frontmatter base

```yaml
---
_manifest:
  urn: "urn:{namespace}:{type}:{id}"
  provenance:
    created_by: "{autor}"
    created_at: "{YYYY-MM-DD}"
    source: "{referencia}"
version: "{semver}"
status: draft|published|deprecated
tags: [{tag1}, {tag2}, {tag3}]
lang: "{iso-639-1}"
extensions: {}
---
```

Reglas:

- el sobre base es cerrado
- metadata adicional **DEBE** vivir dentro de `extensions.{namespace}`
- el URN de Spec-MD es conceptual y usa el regimen tripartito

### 3.2 Cuerpo prescriptivo

El cuerpo **DEBE** estructurar su contenido en secciones normativas y **NO DEBE** contener prosa sin funcion normativa explicita.

## 4. Lenguaje de obligacion

Keywords permitidas:

- **DEBE**
- **NO DEBE**
- **DEBERIA**
- **NO DEBERIA**
- **PUEDE**

Reglas:

1. Toda obligacion importante **DEBE** usar una keyword RFC 2119.
2. El hedging normativo **NO DEBE** reemplazar una keyword.
3. Las keywords en espanol **DEBEN** escribirse en mayusculas.
4. La equivalencia inglesa **PUEDE** aparecer en la primera mencion, no en todas.

## 5. Gramatica estructural

### 5.1 Jerarquia de encabezados

| Nivel | Rol |
| --- | --- |
| `#` | titulo del estandar |
| `##` | seccion normativa principal |
| `###` | subseccion o componente |
| `####` | caso especial o excepcion |

Reglas:

1. La profundidad **NO DEBE** exceder `####`.
2. Las secciones `##` **DEBEN** numerarse secuencialmente.
3. Los headings **DEBEN** ser descriptivos, no genericos.

### 5.2 Elementos de contenido

| Elemento | Uso permitido | Funcion prohibida |
| --- | --- | --- |
| Prosa explicativa | racionalizar, contextualizar, desambiguar | narracion, filler, transiciones |
| `Correcto:` / `Incorrecto:` | anclar la interpretacion | decoracion |
| `Rationale:` | registrar motivacion no normativa | introducir deberes nuevos |
| tablas de validacion | checks y enforcement | listados esteticos sin criterio |

### 5.3 Elementos prohibidos

Cada elemento de la siguiente lista **NO DEBE** incluirse en Spec-MD:

- hedging tipo "probablemente", "seria bueno", "idealmente" cuando reemplaza una keyword
- contradicciones no resueltas entre reglas
- referencias circulares opacas
- prosa ornamental que no agrega obligacion ni aclaracion

### 5.4 Prosa explicativa

La prosa explicativa **PUEDE** existir solo cuando cumple una funcion normativa clara:

- justificar una regla
- prevenir ambiguedad
- contextualizar una restriccion
- advertir un limite del enforcement

## 6. Patron obligatorio: regla + ejemplo + traza

Toda regla compleja o con riesgo de ambiguedad **DEBE** seguir este patron:

1. Regla normativa con keyword.
2. `Correcto:` / `Incorrecto:` cuando la regla admita mala lectura.
3. `Traces to:` si la regla tiene respaldo formal oficial; `Rationale:` si la justificacion es pragmatica.

Reglas:

1. La ausencia de `Traces to:` no debilita la fuerza normativa de una regla.
2. `Rationale:` **NO DEBE** introducir obligaciones nuevas.
3. Un ejemplo **NO DEBE** reemplazar la regla; la ancla.

## 7. Invariantes de KORA/Spec-MD

### 7.1 Consistencia interna

Un documento prescriptivo **NO DEBE** contener reglas incompatibles entre si sin una clausula de precedencia o excepcion explicita.

### 7.2 Auto-suficiencia

Toda regla importante **DEBE** poder entenderse con su propio contexto local, sin depender de una lectura telepatica del repositorio.

### 7.3 Preservacion de idioma y anglicismos

El documento **DEBE** mantener idioma consistente. Los anglicismos **PUEDE** usarse si nombran terminos tecnicos inevitables, pero **NO DEBEN** reemplazar una regla ya expresable en espanol.

### 7.4 Versionamiento semantico

- correccion editorial sin impacto normativo: patch
- regla nueva compatible: minor
- cambio incompatible de ley: major

### 7.5 No-circularidad

Una regla **NO DEBE** justificarse solo remitiendo a otra regla igual de opaca. Si depende de otra, la dependencia **DEBE** aclarar que agrega o restringe.

## 8. Validacion

| Check | Criterio | Enforcement | Accion si falla |
| --- | --- | --- | --- |
| Frontmatter valido | Cumple el sobre base y usa `extensions` para metadata extra | schema | Corregir frontmatter |
| Keyword explicita | Toda obligacion importante usa keyword RFC 2119 | lint | Reescribir regla |
| Trazabilidad oficial | `Traces to:` solo referencia Formal Layer oficial | lint | Corregir o degradar a `Rationale:` |
| Patron de regla | Reglas complejas incluyen ejemplo y soporte adecuado | manual | Completar regla |
| Consistencia interna | No hay contradicciones no resueltas | manual | Reescribir o introducir precedencia |
| Auto-suficiencia | Las reglas se entienden sin contexto omitido critico | manual | Reescribir seccion |
| No-circularidad | Las referencias normativas no forman bucles opacos | manual | Aclarar dependencia |
| Enforcement declarado | Toda tabla nueva o reescrita incluye columna `Enforcement` | lint | Completar tabla |

## 9. Ejemplo

```markdown
Toda regla pragmatica **DEBE** declararse con keyword explicita.
Correcto: `La herramienta declara su nivel de enforcement en tabla de validacion.`
Incorrecto: `Seria bueno indicar como se verifica.`
Rationale: La auditabilidad requiere distinguir schema, lint, runtime y manual.
```

## 10. Template (esqueleto minimo)

Todo Spec-MD nuevo **DEBERIA** arrancar desde este esqueleto:

1. `## 1. Definicion`
2. `## 2. Definiciones`
3. `## 3-N. Secciones normativas`
4. `## N+1. Invariantes`
5. `## N+2. Validacion`
6. `## N+3. Ejemplos` (opcional)
7. `## N+4. Migracion` (opcional)
