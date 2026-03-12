---
_manifest:
  urn: urn:kora:skill:curator-artifact-auditor:2.0.0
  type: lazy_load_endofunctor
version: 2.0.0
status: published
lang: es
extensions:
  kora:
    skill:
      form: extended
      allowed_tools:
        - artifact_read
        - artifact_validate
        - spec_consult
        - catalog_resolve
      requires: []
      scripts:
        - scripts/audit_artifact.py
      references:
        - references/audit-stack.md
      assets:
        - assets/audit-report-template.md
---

# CM-ARTIFACT-AUDITOR

## Proposito
Valida artefactos de conocimiento existentes contra la spec correspondiente. Genera reporte PASS|FAIL con correcciones detalladas por check, apoyandose en el stack determinista del repo cuando conviene ejecutar verificacion mecanica reproducible.

## Input/Output
- **Input:** artefacto: path | URN (artefacto a auditar)
- **Output:** AuditReport (ver Signature Output)

## Procedimiento
1. Cargar el baseline desde `references/audit-stack.md` para fijar spec rectora, pipeline y soporte mecanico disponible.
2. Si la auditoria requiere comprobacion mecanica reproducible sobre un path local, usar `scripts/audit_artifact.py` como envoltorio del stack en `scripts/kora_lib/validation.py`.
3. **Leer y Clasificar**
   - Leer artefacto completo (frontmatter + cuerpo).
   - Clasificar tipo: descriptivo(KORA/MD) o prescriptivo(KORA/Spec-MD).
   - Determinar spec rectora: md-spec §9 o spec-md §8.
4. **Checklist KORA/MD (md-spec §9, si descriptivo)**
   - Frontmatter valido
   - URN registrado
   - URN sin version
   - Sin grasa
   - Idioma preservado
   - Independencia chunk RAG
   - Sin duplicacion
   - Referencias validas
   - Fidelidad
   - Estructuras preservadas
   - Tags
   - Compresion razonable
   - Calidad de superficie
   - Heading recuperable
   - Resumen obligatorio
   - Catalogo derivado
5. **Checklist KORA/Spec-MD (spec-md §8, si prescriptivo)**
   - Frontmatter valido
   - Numeracion secuencial
   - Keywords RFC 2119 explicitas
   - Headings descriptivos
   - Sin ambiguedad
   - Ejemplos presentes
   - Sin prosa innecesaria
   - Consistencia interna
   - No-circularidad
   - Definiciones completas
   - Anglicismos controlados
   - Referencias validas
   - Auto-suficiencia
   - Enforcement declarado
6. Calcular metricas cuando aplique:
   - FS (Fidelity Score): % informacion fuente representada en output. Objetivo: 100%.
   - CR (Compression Ratio): caracteres_original / caracteres_kora. Objetivo: >1.5 o justificacion explicita por alta densidad.
   - Calidad de superficie: PASS cuando la salida conserva legibilidad tecnica y evita serializacion de campos.
7. Generar reporte siguiendo `assets/audit-report-template.md`, consolidando checks fallidos por familia operativa: fidelidad, ssot, conformidad, catalogo o superficie.
8. Si el resultado es FAIL, identificar `causa_principal` segun la familia que define el reingreso minimo del workflow.

## Signature Output
| Campo | Tipo | Descripcion |
|-------|------|-------------|
| resultado | enum(PASS\|FAIL) | Resultado global de auditoria |
| tipo | enum(descriptivo\|prescriptivo) | Tipo clasificado |
| causa_principal | enum(fidelidad\|ssot\|conformidad\|catalogo\|superficie) \| null | Familia dominante de falla para reingreso del workflow |
| checks | {nombre, status, detalle, correccion}[] | Checklist con resultado por item |
| metricas | {FS: number, CR: number} \| null | Metricas de fidelidad y compresion (si aplica) |
| resumen | string | Resumen ejecutivo del reporte |
