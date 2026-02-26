---
_manifest:
  urn: "urn:fxsl:skill:ingeniero-sistemas-composicional-requirements-engineer:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Especificar requisitos funcionales y no funcionales verificables desde el modelo de sistema. Mantener trazabilidad con FBS/PBS.

## Input/Output

- **Input:** Breakdown structures (FBS/PBS) desde S-REQUIREMENTS
- **Output:** Requisitos FR/NFR con formato estandar, verificabilidad y trazabilidad

## Procedimiento

1. Derivar FR (funcionales) desde FBS — que debe hacer
2. Identificar NFR (no funcionales) por categorias:
   - Availability (A): Accesibilidad del sistema
   - Performance (PE): Rendimiento bajo condiciones
   - Security (SE): Proteccion de datos y acceso
   - Maintainability (MN): Facilidad de mantenimiento
   - Portability (PO): Transferibilidad entre entornos
   - Usability (US): Facilidad de uso
3. Formato requisito: `[When C] val(O.P) in D`
4. Verificar completitud, consistencia, verificabilidad
5. Generar matriz trazabilidad FBS→Requisitos→PBS

## Signature Output

```
## Requisitos Funcionales
| ID | Requisito | FBS Ref | Verificacion |
|----|-----------|---------|--------------|

## Requisitos No Funcionales
| ID | Categoria | Requisito | Verificacion |
|----|-----------|-----------|--------------|

## Matriz de Trazabilidad
| Requisito | FBS | PBS | Test |
|-----------|-----|-----|------|
```
