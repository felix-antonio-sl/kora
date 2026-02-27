---
_manifest:
  urn: "urn:dev:agent-bootstrap:reviewer-user:1.0.0"
  type: "bootstrap_user"
---

## Perfil

- Operador: Felix Sanhueza (operador solitario, sombrero Operador cuando interactua con el reviewer)
- Contexto: Revisa PRs generados por fxsl/coder. Garantiza calidad, seguridad y conformidad antes de merge
- Nivel tecnico: Avanzado
- Idioma: Espanol (es-CL)
- Fase actual: Transicion Fase 2→3 del bootstrap path

## Rutinas

- Cada PR generado por fxsl/coder DEBE pasar por review
- Verificar diversidad de modelo antes de cada review
- Review sigue flujo: calidad → seguridad → evals → veredicto
- Hallazgos CRITICOS bloquean merge inmediatamente
- Veredicto siempre con evidencia especifica

## Preferencias de Output

- Hallazgos en tabla con severidad, ubicacion, descripcion, sugerencia
- Veredicto al final del reporte (evidencia primero)
- Codigo problematico citado en bloques diff
- Resumen ejecutivo de 1-2 lineas al inicio
- Sin falsos positivos: cada hallazgo verificado contra el codigo real
