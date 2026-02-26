---
_manifest:
  urn: "urn:kora:skill:custodio-estructura-auditor:1.0.0"
  type: "lazy_load_endofunctor"
version: "1.0.0"
status: published
lang: es
---
# CM-ESTRUCTURA-AUDITOR

## Proposito
Audita la estructura del monorepo KORA: verifica directorios esperados, convenciones de naming, archivos huerfanos, workspaces incompletos, frontmatter valido.

## I/O

- **Input:** scope: string | null (ruta o namespace a auditar, null=monorepo completo)
- **Output:** StructureAuditReport (ver Signature Output)

## Procedimiento
1. Verificar directorios raiz esperados: inbox/, source/, drafts/, specs/, knowledge/, agents/, catalog/, skills/, scripts/, docs/.
2. Verificar namespaces en knowledge/: gn/, fxsl/, kora/, tde/, legal/, gov/, orko/, mgmt/.
3. Verificar namespaces en agents/: kora/, fxsl/, gn/, ops/, tde/, orko/, korvo/.
4. Para cada workspace en agents/: verificar 5 archivos esenciales (AGENTS.md, SOUL.md, USER.md, TOOLS.md, config.json) + directorio skills/.
5. Detectar directorios vacios o huerfanos (sin archivos utiles).
6. Verificar convenciones naming: minusculas, guiones, sin espacios, sin caracteres especiales.
7. Muestrear frontmatter de artefactos: verificar _manifest.urn presente y formato valido.
8. Reporte con hallazgos clasificados: ERROR(falta componente esencial), WARNING(convencion rota, huerfano), OK(conforme).

## Signature Output

| Campo | Tipo | Descripcion |
|-------|------|-------------|
| hallazgos | {hallazgo, severidad, ruta, accion_recomendada}[] | Lista de hallazgos clasificados |
| conteo | {error: int, warning: int, ok: int} | Conteo por severidad |
