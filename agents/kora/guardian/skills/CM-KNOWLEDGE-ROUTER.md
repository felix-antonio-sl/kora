---
_manifest:
  urn: "urn:kora:skill:guardian-knowledge-router:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-KNOWLEDGE-ROUTER

## Proposito

Enrutar consultas de conocimiento a la fuente autoritativa correcta: catalogo interno KORA o busqueda externa, garantizando respuestas con precision y trazabilidad.

## Procedimiento

1. Recibir consulta y clasificar dominio: domain (dentro del ecosistema KORA) | external (fuera del ecosistema)
2. Si domain: resolver URN via catalog_resolve → identificar KB correspondiente → extraer respuesta con cita oficial
3. Si external: ejecutar web_search con terminos precisos → citar fuente con nombre oficial y URL
4. Si ambiguo: priorizar fuente interna KORA; si no existe, complementar con externa
5. Formular respuesta con nivel de autoridad explícito: "Segun KORA/Spec §X..." o "Segun [fuente externa]..."
6. Verificar que no se exponen IDs internos ni jargon de implementacion

## Output

Respuesta con cita autoritativa (fuente KORA + seccion, o fuente externa + URL). Nivel de confianza implicito en la formulacion.
