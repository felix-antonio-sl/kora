---
_manifest:
  urn: "urn:kora:skill:smith-ftcf-analyzer:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-FTCF-ANALYZER

## Proposito
Elicita y estructura los cuatro ejes FTCF (Funcion, Tono, Conocimiento, Fronteras) de un nuevo agente, produciendo el perfil base para la fase de arquitectura.

## Procedimiento
1. Preguntar o inferir FUNCION: que hace el agente, que problema resuelve, a quien sirve, que outputs produce.
2. Preguntar o inferir TONO: como se comunica (formal/casual/tecnico/pedagogico), longitud de respuestas, uso de markdown, idioma.
3. Preguntar o inferir CONOCIMIENTO: fuentes requeridas (KBs curadas, web en tiempo real, razonamiento LLM), dominios de expertise, artefactos necesarios.
4. Preguntar o inferir FRONTERAS: que NO hace el agente, a que otros agentes derivar (kora/transformer, ops/tester), temas prohibidos.
5. Validar completitud: los 4 ejes deben tener respuesta. Si falta alguno, preguntar especificamente.
6. Documentar boundaries como lista de restricciones explicitas para uso en Guard Set.

## Output
Documento FTCF estructurado con 4 secciones. Cada eje tiene: descripcion, ejemplos concretos, restricciones derivadas. Lista de boundaries lista para alimentar CM-GUARD-CONFIGURATOR.
