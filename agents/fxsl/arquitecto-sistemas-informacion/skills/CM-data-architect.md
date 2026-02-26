---
_manifest:
  urn: "urn:fxsl:skill:arquitecto-sistemas-informacion-data-architect:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Modelar datos como categoria y derivar esquemas concretos. Formalizar entidades, relaciones, atributos y restricciones como objetos y morfismos categoricos, luego traducir a formato target.

## I/O

- **Input:** Funciones IS y dominio desde S-DATA-MODELING
- **Output:** Modelo datos en 3 niveles (conceptual, categorico, fisico) con traducciones target

## Procedimiento

1. Identificar ENTIDADES: objetos/conceptos del dominio
2. Definir ATRIBUTOS: propiedades observables de cada entidad
3. Establecer RELACIONES: morfismos entre entidades (cardinalidad, direccion)
4. Formalizar RESTRICCIONES: ecuaciones que deben satisfacerse
5. Construir ESQUEMA CATEGORICO: Categoria C con obj=entidades, morph=relaciones
6. Definir INSTANCIA: Funtor I: C → Set asigna conjuntos a entidades
7. Traducir a formato target via funtores:

### Target Mappings

| Formato | Entidad | Morfismo | Atributo |
|---------|---------|----------|----------|
| SQL | CREATE TABLE | FOREIGN KEY REFERENCES | column TYPE |
| GraphQL | type | field returning type | scalar field |
| JSON Schema | object schema | $ref | property |

### Modelo Categorico

- Schema: Categoria C con objetos = entidades, morfismos = relaciones
- Instance: Funtor I: C → Set asigna conjuntos a entidades
- Query: Bimodule Q: C x D → Set para consultas

## Signature Output

```
## Modelo Conceptual (ERD)
{Diagrama ER en Mermaid}

## Esquema Categorico
Objetos: {entidades}
Morfismos: {relaciones tipadas}
Atributos: {observables a tipos base}

## Modelo Fisico ({target})
{DDL/SDL/Schema en formato target}
```
