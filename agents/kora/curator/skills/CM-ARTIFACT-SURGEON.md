---
_manifest:
  urn: "urn:kora:skill:curator-artifact-surgeon:2.0.0"
  type: "lazy_load_endofunctor"
version: "2.0.0"
status: published
lang: es
---
# CM-ARTIFACT-SURGEON

## Proposito
Diagnostica y repara artefactos de conocimiento rotos o no conformes. Aplica fixes quirurgicos con minima modificacion, preservando invariantes y sin romper referencias.

## I/O

- **Input:** artefacto: path | URN (artefacto con problemas detectados)
- **Output:** SurgicalReport (ver Signature Output)

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

## Signature Output

| Campo | Tipo | Descripcion |
|-------|------|-------------|
| artefacto_reparado | string | Artefacto con fixes aplicados |
| issues_diagnosticados | {severidad, componente, descripcion}[] | Issues encontrados |
| fixes_aplicados | {antes, despues, justificacion}[] | Fixes realizados |
| version_anterior | string | Version antes de reparacion |
| version_nueva | string | Version despues de reparacion |
| pendientes | string[] | Issues no resueltos (si aplica) |
