---
_manifest:
  urn: urn:gn:skill:goreologo-intake:2.0.0
  type: lazy_load_endofunctor
---

# CM-INTAKE

## Proposito
Diagnosticar, clasificar y posicionar toda consulta entrante al Goreologo: tema, dimension institucional, alcance y nivel de complejidad requerido.

## Input/Output
- **Input:** Consulta entrante del usuario al Goreologo
- **Output:** Clasificacion estructurada: {dimension, tipo, complejidad, dominios_involucrados, alcance}

## Procedimiento
1. Recibir la consulta del usuario y extraer el tema central.
2. Clasificar la dimension institucional involucrada:
   - Estructura/competencias GORE → marco LOC 19.175
   - Gestion financiera/inversiones → FNDR, FRPD, FRIL, ISAR
   - Procesos operativos → IPR, rendiciones, procedimientos
   - Transformacion digital → Ley 21.180, TDE, modernizacion
   - Contexto Nuble → datos especificos, ERD, organigrama, gobernanza
3. Evaluar nivel de complejidad: consulta puntual, analisis multidimensional o ambiguedad que requiere clarificacion.
4. Si ambigua: presentar tabla de opciones y preguntar antes de desarrollar.
5. Contar dominios involucrados y determinar alcance:
   - Si la consulta cae en un solo dominio cubierto por un especialista → alcance: single_domain.
   - Si la consulta cruza 2+ dominios o requiere vision panoramica → alcance: cross_domain.
6. Posicionar respuesta: confirmar interpretacion y clasificacion.

## Signature Output
| Campo | Tipo | Descripcion |
|-------|------|-------------|
| dimension | string | Dimension institucional principal |
| tipo | string | Tipo de consulta (puntual, analisis, comparativa) |
| complejidad | string | Nivel: puntual, multidimensional, ambigua |
| dominios_involucrados | string[] | Lista de dominios detectados |
| alcance | single_domain \| cross_domain | Cantidad de dominios involucrados |
