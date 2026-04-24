# Workflow Map

## Mapa de implementación

Esta skill productiva implementa, para la ruta `knowledge + KB normal`, lo que
el agente `curator` distribuye entre varias skills legacy internas.

| Fase en `knowledge-curator` | Base en `curator` | Función | Output visible |
|---|---|---|---|
| `validar-handoff` | `CM-INTENT-CLASSIFIER` | aceptar contrato de ruta o reconstruir diagnóstico mínimo | route status |
| `disenar-draft` | `CM-ARTIFACT-DESIGNER` | definir namespace, URN, familia, headings y staging path | draft plan |
| `koraficar-o-reparar` | `CM-KORAFICATOR` + `CM-ARTIFACT-EDITOR` + `CM-ARTIFACT-SURGEON` | transformar fuente descriptiva o reparar draft existente | draft KORA/MD |
| `auditar-borrador` | `CM-ARTIFACT-AUDITOR` | verificar shape, referencias, fidelidad y readiness | audit report |
| `consolidar-review` | `CM-LIFECYCLE-ORCHESTRATOR` | consolidar entregables y pendientes sin gobernar la FSM | review package |

## Alcance

1. Implementa solo la ruta descriptiva `KB normal`.
2. No absorbe el régimen `spec`.
3. No absorbe el productor `atomic`.
4. No publica directo a productivo.

## Outcomes permitidos

| Outcome | Cuándo aplica |
|---|---|
| `processing` | el draft existe y sigue en trabajo activo |
| `needs_repair` | la auditoría detectó fallas reales o faltan correcciones visibles |
| `ready_to_promote` | el draft descriptivo está completo, auditado y listo para gate final |
| `rerouted_to_spec` | el material quedó fuera de scope descriptivo |
| `pending` | falta diagnóstico o contrato suficiente para afirmar `KB normal` |
