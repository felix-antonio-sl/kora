---
_manifest:
  urn: "urn:pro:skill:abogado-legislacion-medica-kb-guidance:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Routing de consultas juridicas a artefactos KB especificos. Mapea categoria de consulta a URN de conocimiento correspondiente.

## I/O

- **Input:** Consulta juridica clasificada por categoria tematica
- **Output:** URN del artefacto KB que contiene la respuesta normativa

## Procedimiento

1. Clasificar consulta por categoria tematica
2. Buscar en routing map la categoria correspondiente
3. Resolver URN via catalogo (SOURCE_OF_TRUTH)
4. Si catalogo tiene el URN -> usar file path del catalogo
5. Si no -> usar routing map como fallback
6. Retornar contenido de la fuente correcta

Routing map:
- Que ley aplica, jerarquia normativa, estatutos, fuentes del derecho -> urn:legal:kb:intro-estatutos
- Derechos, deberes, prohibiciones, incompatibilidades -> urn:legal:kb:deberes-prohibiciones
- Ingreso, concursos, carrera funcionaria, nombramientos -> urn:legal:kb:ingreso-carrera
- Jornada, horarios, turnos, calificaciones, evaluaciones -> urn:legal:kb:jornada-calificaciones
- Sueldos, asignaciones, bonos, remuneraciones -> urn:legal:kb:remuneraciones
- Acoso laboral, acoso sexual, mobbing, Ley Karin -> urn:legal:kb:acoso-laboral
- Sumarios, investigaciones, responsabilidad administrativa -> urn:legal:kb:responsabilidad-admin
- Despido, renuncia, termino, cesacion funciones -> urn:legal:kb:terminacion
- Confianza legitima, no renovacion contratas, continuidad vinculo -> urn:legal:kb:confianza-legitima
- Embarazo, prenatal, postnatal, fuero maternal -> urn:legal:kb:maternidad
- Contratas, honorarios, licitaciones, contratacion publica -> urn:legal:kb:contratacion-publica
- Vacaciones, feriados, permisos, licencias, comisiones -> urn:legal:kb:feriados-permisos
- Liberacion guardia nocturna, incentivo retiro, jubilacion -> urn:legal:kb:derechos-especiales
- Becas, especializacion, PAO, comisiones de estudio -> urn:legal:kb:formacion-especialistas
- Definiciones de leyes, instituciones, conceptos globales -> urn:legal:kb:index

## Signature Output

URN resuelto + file path del artefacto KB correspondiente.
