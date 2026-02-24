---
_manifest:
  urn: "urn:fxsl:agent-bootstrap:arquitecto-categorico-cm-migration-engine:2.0.0"
  type: "lazy_load_endofuntor"
---

## Proposito

Disenar migraciones de esquemas via adjunciones Δ/Σ/Π. Principio: Migracion = adjuncion, no script. Trigger: S-CATEGORICAL-MODELING(migracion).

## Input/Output

- **Input:** Schema fuente S₁, schema target S₂, morfismo de esquema F: S₁ → S₂
- **Output:** Estrategia de migracion formalizada con operador Δ/Σ/Π y SQL analogos

## Procedimiento

1. **Identificar morfismo de esquema** F: S₁ → S₂ que describe la transformacion estructural
2. **Clasificar intencion** — ¿Reestructurar (Δ)? ¿Unificar (Σ)? ¿Restringir (Π)?
3. **Seleccionar operador** de la cadena Σ_F ⊣ Δ_F ⊣ Π_F
4. **Formalizar migracion** con SQL analogos concretos
5. **Verificar preservacion** — que propiedades se conservan y cuales se pierden
6. **Componer** si la migracion es multi-paso: Σ_G ∘ Δ_F o similares

### Operadores

**Δ_F (Pullback / Restriction)**
- Condicion: Reestructurar sin cambiar cardinalidad
- SQL: SELECT alias, duplicar columnas, renombrar tablas
- Preserva: Estructura fuente exactamente
- Uso: Renombrar, reordenar, adaptar vistas

**Σ_F (Left Pushforward / Fusion)**
- Condicion: Unificar, agregar, generalizar
- SQL: UNION, INSERT INTO SELECT, merge tables
- Preserva: Puede perder informacion (colimite)
- Uso: Fusionar tablas, consolidar esquemas, deduplicar

**Π_F (Right Pushforward / Restriction)**
- Condicion: Restringir, filtrar, especializar
- SQL: JOIN, WHERE, productos cartesianos filtrados
- Preserva: Via productos (toda fila cumple restriccion)
- Uso: Filtrar datos, crear subconjuntos, especializar

### Cadena de Adjuncion

```
Σ_F ⊣ Δ_F ⊣ Π_F
(left)   (mid)   (right)

Σ_F: fusion/generalizacion (pierde info)
Δ_F: reestructuracion (preserva todo)
Π_F: restriccion/especializacion (descarta)
```

### Decision Guide

| Intencion | Operador | Riesgo |
|-----------|----------|--------|
| Renombrar/reestructurar | Δ_F | Bajo — preserva estructura |
| Fusionar/agregar | Σ_F | Medio — posible perdida por colimite |
| Filtrar/restringir | Π_F | Medio — descarta filas no-matching |
| Multi-paso complejo | Composicion Σ∘Δ o Π∘Δ | Alto — verificar conmutatividad |

### Verificacion

- Diagrama conmuta: F ∘ Δ_F = Δ_F ∘ F (consistencia)
- Adjuncion: Hom(Σ_F(I), J) ≅ Hom(I, Δ_F(J)) (universal)
- Constraint preservation: restricciones de S₁ preservadas en S₂

## Signature Output

```
## Migracion: S₁ → S₂
Morfismo: F: S₁ → S₂ = {mapeo objetos y morfismos}
Operador: {Δ_F | Σ_F | Π_F | composicion}
SQL: {DDL/DML concreto}
Preserva: {propiedades conservadas}
Pierde: {propiedades perdidas, si aplica}
Verificacion: {conmutatividad, adjuncion}
```
