---
_manifest:
  urn: "urn:gn:skill:goreologo-intake:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-INTAKE

## Proposito
Diagnosticar, clasificar y posicionar toda consulta entrante al Goreologo: tema, dimension institucional, alcance y nivel de complejidad requerido.

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
5. Posicionar respuesta: confirmar interpretacion antes de derivar a S-ANALISIS.

## Output
Clasificacion confirmada: [Dimension institucional] + [Tipo consulta] + [Complejidad]. Si ambigua: tabla de opciones presentada al usuario. Derivacion a S-ANALISIS con posicionamiento claro.
