---
_manifest:
  urn: urn:kora:skill:forgemaster-equivalence-checker:1.0.0
  type: lazy_load_endofunctor
---

# CM-EQUIVALENCE-CHECKER

## Proposito
Valida que los artefactos derivados preservan equivalencia comportamental con el agente KORA fuente, segun criterios de runtime-spec-md §6.

## Input/Output
- **Input:** source_analysis: WorkspaceAnalysis, derived_artifacts: TransmutedArtifact[], platform: string
- **Output:** EquivalenceReport (ver Signature Output)

## Procedimiento
1. VERIFICAR PRESERVACION FSM:
   - Todos los estados del agente fuente DEBEN estar representados en el artefacto derivado.
   - Todas las transiciones con sus prioridades DEBEN preservarse.
   - S-DISPATCHER y S-END DEBEN existir.
   - Determinismo de transiciones preservado.
2. VERIFICAR PRESERVACION TOOLS:
   - Toda herramienta declarada en TOOLS.md fuente DEBE tener mapeo en artefacto derivado.
   - Si plataforma no soporta herramienta → documentar limitacion, no omitir silenciosamente.
3. VERIFICAR PRESERVACION CONSTRAINTS:
   - Reglas duras del agente fuente DEBEN estar presentes en artefacto derivado.
   - config.json sandbox/tools/limits DEBEN mapearse a mecanismo equivalente de plataforma.
4. VERIFICAR SEGREGACION:
   - Identidad (SOUL.md) NO mezclada con behavior (AGENTS.md) en output.
   - Config (config.json) NO inyectada como texto rector al LLM.
5. VERIFICAR FORMATO PLATAFORMA:
   - Artefactos cumplen formato nativo de plataforma target.
   - Sin frontmatter KORA residual.
   - Estructura de directorios correcta para la plataforma.
6. Generar reporte PASS|FAIL con tabla de checks:
   ```
   | Check | Estado | Detalle |
   |-------|--------|---------|
   | FSM   | PASS   | 6/6 estados, 12/12 transiciones |
   | Tools | WARN   | diff_compute sin equivalente nativo |
   | ...   | ...    | ... |
   ```

## Signature Output
| Campo | Tipo | Descripcion |
|-------|------|-------------|
| result | enum | PASS, FAIL |
| checks | CheckEntry[] | Lista de verificaciones con estado y detalle |
| warnings | string[] | Limitaciones documentadas (no bloquean PASS) |
| failures | string[] | Violaciones que causan FAIL |
| recommendations | string[] | Mejoras sugeridas |
