# Protocolo kv_inbox / kv_outbox — 2026-03-31

## Definicion

Cada agente de 3a generacion tiene dos carpetas en su workspace:

- `kv_inbox_{{nombre-agente}}/` — documentos que entran al espacio de trabajo del agente
- `kv_outbox_{{nombre-agente}}/` — documentos que salen del agente

## Reglas

1. **No indexadas.** Estas carpetas NO se indexan en memory search. Son transporte de documentos, no memoria.
2. **El agente lee su inbox** para recibir documentos depositados por el operador u otros agentes.
3. **El agente escribe en su outbox** para entregar artefactos al operador u otros agentes.
4. **Sin procesamiento automatico.** Los documentos no se inyectan en bootstrap ni se cargan automaticamente. El agente los lee explicitamente cuando se le indica.
5. **Naming libre.** Los archivos dentro de inbox/outbox pueden tener cualquier nombre y formato.
6. **Limpieza manual.** El operador o el agente limpian las carpetas cuando los documentos ya no son necesarios.

## Mapa de carpetas

| Agente | Workspace | Inbox | Outbox |
|---|---|---|---|
| main | ~/.openclaw/workspace | kv_inbox_main/ | kv_outbox_main/ |
| mente-omega | ~/.openclaw/workspace-mente-omega | kv_inbox_mente-omega/ | kv_outbox_mente-omega/ |
| salubrista | ~/.openclaw/workspace-salubrista | kv_inbox_salubrista/ | kv_outbox_salubrista/ |
| steipete | ~/.openclaw/workspace-steipete | kv_inbox_steipete/ | kv_outbox_steipete/ |
| gtd-integral | ~/.openclaw/workspace-gtd-integral | kv_inbox_gtd-integral/ | kv_outbox_gtd-integral/ |
| allan-kelly | ~/.openclaw/workspace-allan-kelly | kv_inbox_allan-kelly/ | kv_outbox_allan-kelly/ |

## kv_commons — espacio compartido

Ruta: `~/.openclaw/kv_commons/`

| Carpeta | Uso |
|---|---|
| `inbox/` | Documentos depositados por el operador para todos los agentes |
| `outbox/` | Documentos producidos por cualquier agente para consumo comun |

Reglas:
- Accesible por los 6 agentes (ruta absoluta fuera de workspaces individuales).
- No indexado. No inyectado en bootstrap.
- Cualquier agente puede leer y escribir en ambas carpetas.
- Para documentos dirigidos a un agente especifico, usar el kv_inbox individual.
- Para documentos de interes comun o colaborativo, usar kv_commons.

## Uso cross-agente

- **Individual**: inbox/outbox dentro del workspace de cada agente.
- **Compartido**: `~/.openclaw/kv_commons/inbox` y `outbox`.
- **Directo**: si ambos agentes tienen acceso fs completo, pueden escribir directamente en el inbox del otro.
