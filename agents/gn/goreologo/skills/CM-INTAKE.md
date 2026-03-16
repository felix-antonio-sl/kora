---
_manifest:
  urn: urn:gn:skill:goreologo-intake:2.0.0
  type: lazy_load_endofunctor
version: 2.0.0
status: published
lang: es
---

# CM-INTAKE

## Proposito
Diagnosticar, clasificar y posicionar toda consulta entrante al Goreologo: tema, dimension institucional, alcance y nivel de complejidad requerido.

## Input/Output
- **Input:** Consulta entrante del usuario al Goreologo
- **Output:** Clasificacion confirmada: [Dimension institucional] + [Tipo consulta] + [Complejidad]

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
5. **Routing decision:** Tras clasificar dimension/tipo/complejidad, determinar:
   - ROUTE_TO_SPECIALIST: si la consulta cae en un solo dominio cubierto por un especialista → derivar via CM-SPECIALIST-ROUTER a S-ROUTING.
   - SYNTHESIZE_CROSS_DOMAIN: si la consulta cruza 2+ dominios o requiere vision panoramica → retener en goreologo, derivar a S-SINTESIS.
6. Posicionar respuesta: confirmar interpretacion y routing decision.

## Signature Output
Clasificacion confirmada: [Dimension institucional] + [Tipo consulta] + [Complejidad] + [Routing: SPECIALIST|CROSS_DOMAIN]. Si ambigua: tabla de opciones presentada al usuario. Derivacion a S-ROUTING o S-SINTESIS segun decision.
