---
_manifest:
  urn: "urn:kora:skill:forgemaster-agent-surgeon:2.0.0"
  type: "lazy_load_endofunctor"
version: "2.0.0"
status: published
lang: es
---
# CM-AGENT-SURGEON

## Proposito
Diagnostica y repara agentes KORA con precision quirurgica: minima modificacion, preservar invariantes, no romper otros componentes.

## I/O

- **Input:** agent_path: string (ruta al workspace), problema: string (descripcion del problema reportado)
- **Output:** SurgicalReport (ver Signature Output)

## Procedimiento
1. DIAGNOSTICO: Leer workspace completo del agente afectado (workspace_read).
2. IDENTIFICAR PROBLEMA: Clasificar tipo — violacion segregacion, FSM rota, URNs invalidos, co-induccion ausente, config inconsistente, skill mal formado.
3. LOCALIZAR COMPONENTE: Determinar exactamente que archivo(s) y que seccion(es) estan afectados.
4. CLASIFICAR SEVERIDAD: CRITICAL(agente no funciona), HIGH(funciona mal), MEDIUM(suboptimo), LOW(cosmetico).
5. PLANIFICAR FIX: Describir cambio minimo necesario. Verificar que el fix no rompe otros componentes (efecto colateral).
6. APLICAR FIX: Modificar solo lo necesario. Preservar frontmatter, URNs existentes, estructura general.
7. VERIFICAR POST-FIX: Re-ejecutar CM-AGENT-VALIDATOR en el componente modificado. Confirmar que el fix resuelve el problema sin introducir nuevos issues.
8. DOCUMENTAR: Registrar que se cambio, por que, y que se verifico.

## Signature Output

| Campo | Tipo | Descripcion |
|-------|------|-------------|
| agente | string | Nombre del agente intervenido |
| problema | string | Problema diagnosticado |
| severidad | enum(CRITICAL\|HIGH\|MEDIUM\|LOW) | Severidad del problema |
| componente_afectado | string | Archivo(s) modificado(s) |
| fix_aplicado | string | Descripcion del fix |
| verificacion_post | enum(PASS\|FAIL) | Resultado de re-validacion |
