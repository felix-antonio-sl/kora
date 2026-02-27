---
_manifest:
  urn: "urn:dev:agent-bootstrap:tester-user:1.0.0"
  type: "bootstrap_user"
---

## Perfil

- Operador: Felix Sanhueza (operador solitario, sombrero Operador cuando interactua con el tester)
- Contexto: Desarrolla proyectos de software asistido por enjambre LLM. Necesita verificacion independiente de aceptacion e integracion mas alla del TDD del coder
- Nivel tecnico: Avanzado
- Idioma: Espanol (es-CL)
- Fase actual: Transicion Fase 2→3 del bootstrap path

## Rutinas

- Generar tests de aceptacion por cada historia antes de merge (DoD paso 2)
- Generar tests de integracion por cada epic cuando hay boundaries nuevos
- Ejecutar suite completa antes de merge (pre-aprobacion humana)
- Reporte de cobertura por AC al final de cada Pulse
- Validar que todo AC del backlog tiene test asociado

## Preferencias de Output

- Tests en bloques con lenguaje especificado (TypeScript/Python)
- Formato DADO/CUANDO/ENTONCES para aceptacion
- Resultados de ejecucion en tablas con pass/fail
- Reporte de cobertura en tablas con gaps destacados
- Stack traces completos en caso de fallo
- Sin explicaciones largas — la evidencia habla
