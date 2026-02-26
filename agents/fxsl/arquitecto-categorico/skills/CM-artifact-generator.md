---
_manifest:
  urn: "urn:fxsl:skill:arquitecto-categorico-artifact-generator:2.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Generar artefactos ejecutables desde modelos categoricos. Cada formato target es un funtor F: CategoricalModel → TargetLanguage. Trigger: S-ARTIFACT-GENERATION.

## Input/Output

- **Input:** Modelo categorico formalizado (objetos, morfismos, construcciones universales) desde S-ARTIFACT-DESIGN
- **Output:** Artefacto en formato target con trazabilidad categorica

## Procedimiento

1. **Confirmar formato destino** con usuario
2. **Aplicar mapeos categoricos** del formato seleccionado
3. **Generar sintaxis valida** en el lenguaje target
4. **Agregar trazabilidad** — comentarios que mapean cada elemento al modelo categorico
5. **Validar coherencia** — artefacto preserva estructura del modelo

### Mapeos Categoricos por Formato

**SQL (PostgreSQL DDL)**

| Categorico | SQL |
|-----------|-----|
| Objeto | CREATE TABLE |
| Morfismo | FK REFERENCES |
| Limite (Pullback) | JOIN ON |
| Colimite (Coproduct) | UNION ALL |
| Equalizer | WHERE f=g / CHECK |
| Identidad | PRIMARY KEY |
| Composicion | FK chains |

Trazabilidad: `-- Cat: C_{nombre}, Funtor: C→PostgreSQL -- Obj: {nombre}`

**GraphQL SDL**

| Categorico | GraphQL |
|-----------|---------|
| Objeto | type |
| Morfismo | field → type |
| Limite (nested) | nested type / field resolver |
| Colimite | union type |
| Identidad | id: ID! |

Trazabilidad: `# Cat: Obj({nombre}), Morph({f}:{A}→{B})`

**OpenAPI 3.x**

| Categorico | OpenAPI |
|-----------|---------|
| Objeto | schema component |
| Morfismo | $ref |
| Limite | allOf (interseccion) |
| Colimite | oneOf (union) |
| Identidad | required id property |

**JSON Schema**

| Categorico | JSON Schema |
|-----------|-------------|
| Objeto | object type + properties |
| Morfismo | $ref |
| Limite | allOf |
| Colimite | oneOf |
| Restriccion | pattern, enum, const |

**Prisma Schema**

| Categorico | Prisma |
|-----------|--------|
| Objeto | model |
| Morfismo | @relation |
| Identidad | @id |
| Limite | compound unique (@@unique) |

**Mermaid (Diagramas)**

| Categorico | Mermaid |
|-----------|---------|
| Objeto | Entity en erDiagram, Node en graph |
| Morfismo | Relacion/edge |
| Composicion | Path through nodes |

**PlantUML**

| Categorico | PlantUML |
|-----------|----------|
| Objeto | class / entity |
| Morfismo | arrow (-->, ..|>) |
| Herencia | generalization |

**SPARQL**

| Categorico | SPARQL |
|-----------|--------|
| Objeto | rdf:type / owl:Class |
| Morfismo | owl:ObjectProperty |
| Instancia | Individual |

### Validacion

- F(id) = id — identidades preservadas
- F(g∘f) = F(g)∘F(f) — composicion preservada
- Sintaxis valida del target (parseable)
- Trazabilidad completa (todo elemento tiene comentario categorico)

## Signature Output

```
## Artefacto: {formato}
Funtor: C_{dominio} → {TargetLanguage}

{codigo generado con trazabilidad inline}

Verificacion:
- Objetos: {n} mapeados
- Morfismos: {m} preservados
- Construcciones: {lista}
- Sintaxis: valida
```
