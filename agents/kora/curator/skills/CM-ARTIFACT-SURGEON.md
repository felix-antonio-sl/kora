---
_manifest:
  urn: "urn:kora:skill:curator-artifact-surgeon:1.0.0"
  type: "skill"
version: "1.0.0"
status: published
lang: es
---
# CM-ARTIFACT-SURGEON

## Proposito
Diagnostica y repara artefactos de conocimiento rotos o no conformes. Aplica fixes quirurgicos con minima modificacion, preservando invariantes y sin romper referencias.

## Procedimiento
1. DIAGNOSTICAR:
   - Leer artefacto completo.
   - Clasificar tipo (descriptivo/prescriptivo).
   - Ejecutar checklist correspondiente (CM-ARTIFACT-AUDITOR).
   - Identificar cada issue: componente afectado, severidad(critica|alta|media|baja).
2. CLASIFICAR SEVERIDAD:
   - Critica: frontmatter invalido (no parsea), URN malformado, archivo corrupto.
   - Alta: perdida de fidelidad (info faltante), violacion SSOT, referencia rota.
   - Media: grasa presente, headings no telegraficos, independencia chunk violada.
   - Baja: tags insuficientes, formato suboptimo, anglicismo sin controlar.
3. PLANIFICAR FIX:
   - Priorizar por severidad (critica primero).
   - Cada fix: minima modificacion necesaria.
   - Verificar que fix no rompe otros componentes del artefacto.
   - Verificar que fix no rompe referencias de otros artefactos.
4. APLICAR FIX:
   - Uno por uno, verificando despues de cada uno.
   - Preservar contenido informativo/normativo existente.
   - Bump version: Patch si fix no cambia contenido, Minor si agrega info restaurada.
5. DOCUMENTAR: lista de cambios con {severidad, componente, antes, despues, justificacion}.

## Output
Artefacto reparado. Reporte quirurgico: {issues_diagnosticados: [{severidad, componente, descripcion}], fixes_aplicados: [{antes, despues, justificacion}], version_anterior, version_nueva, pendientes: []}.
