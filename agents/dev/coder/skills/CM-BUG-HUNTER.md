---
_manifest:
  urn: "urn:dev:skill:coder-bug-hunter:1.0.0"
  type: "lazy_load_endofunctor"
version: "1.0.0"
status: published
lang: es
---
# CM-BUG-HUNTER

## Proposito
Diagnostica y corrige bugs con disciplina TDD: reproducir con test, diagnosticar, fix minimo, test de regresion.

## Procedimiento
1. Leer reporte de bug o test fallando.
2. **Reproducir:** Escribir test que reproduce el bug.
   - El test DEBE fallar (confirma que el bug existe).
   - Si no se puede reproducir con test: investigar mas, pedir mas contexto.
3. **Diagnosticar:** Identificar causa raiz.
   - Leer codigo afectado.
   - Trazar flujo de datos.
   - Identificar la linea/funcion/condicion que causa el fallo.
   - Documentar diagnostico: "El bug ocurre porque [causa] en [archivo:linea]."
4. **Fix minimo:** Aplicar la correccion mas pequena posible.
   - NO refactorizar alrededor del bug. Solo corregir el defecto.
   - Verificar que el test de reproduccion ahora pasa (green).
   - Verificar que tests existentes siguen pasando.
5. **Test de regresion:** El test de reproduccion SE QUEDA en el suite.
   - Es el test de regresion: previene que el bug vuelva.
   - Nombrarlo descriptivamente: `test_should_not_[bug_description]`.
6. Si el fix requiere cambio arquitectonico: NO aplicar. Reportar al Operador con diagnostico y propuesta.
7. Generar PR de bugfix via CM-PR-GENERATOR.

## Output
Fix: {diagnostico, causa_raiz, test_reproduccion, fix_aplicado, tests_pasan: bool, requiere_cambio_arquitectonico: bool}.
