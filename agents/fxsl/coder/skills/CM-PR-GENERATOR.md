---
_manifest:
  urn: "urn:fxsl:skill:coder-pr-generator:1.0.0"
  type: "lazy_load_endofunctor"
version: "1.0.0"
status: published
lang: es
---
# CM-PR-GENERATOR

## Proposito
Genera un Pull Request completo con descripcion, contexto y checklist de verificacion.

## Procedimiento
1. Verificar pre-condiciones:
   - [ ] Todos los tests pasan.
   - [ ] Lint pasa sin errores ni warnings.
   - [ ] Type check pasa (tsc --noEmit / mypy).
   - Si alguno falla: volver a S-IMPLEMENTAR. NO generar PR con checks rojos.
2. Generar titulo del PR:
   - < 70 caracteres.
   - Formato: `tipo(scope): descripcion` (feat, fix, refactor, test).
3. Generar cuerpo del PR con secciones:
   - **What:** Que cambia este PR (1-3 lineas).
   - **Why:** Historia asociada (Who/What/Why). Link a historia si existe.
   - **How:** Approach tecnico (decisiones clave, patterns usados).
   - **Tests:** Tests agregados/modificados. Cobertura de ACs.
   - **Checklist:**
     - [ ] Tests pasan
     - [ ] Lint limpio
     - [ ] Types verificados
     - [ ] ACs cubiertos por tests
     - [ ] CONVENTIONS.md respetado
     - [ ] Sin `any`
     - [ ] Inputs validados
4. Listar archivos modificados con resumen de cambio por archivo.
5. Si la historia es destructiva: marcar PR como requiere aprobacion humana.

## Output
PR: {titulo, cuerpo_markdown, archivos_modificados[], checklist_status, requiere_aprobacion: bool}.
