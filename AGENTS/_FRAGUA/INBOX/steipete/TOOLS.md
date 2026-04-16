---
_manifest:
  urn: "urn:dev:agent-bootstrap:steipete-tools:1.6.0"
  type: "bootstrap_tools"
---

## dispatch_worker

- **Firma:** `package: WorkPackage -> WorkerHandle`
- **Parametros:** `package` contiene: archivos target, intencion en lenguaje natural, blast radius estimado, close-the-loop criteria, CLI preferido (claude-code/codex/gemini-cli/opencode), modelo especifico
- **Cuando usar:** Cuando un paquete de trabajo esta listo para ejecucion.
- **Cuando NO usar:** Para preguntas o consultas.
- **Descripcion funcional:** Envia paquete a obrero de codigo via exec. El obrero recibe la intencion, lee el codebase, ejecuta el ciclo (types -> tests -> code -> lint -> commit), y reporta resultado.
- **Notas:** Mapea a `exec: claude -p "..."`, `exec: codex --task "..."`, `exec: gemini -p "..."`, o `exec: opencode -p "..."` segun CLI seleccionado.

## monitor_workers

- **Firma:** `filter?: WorkerFilter -> WorkerStatus[]`
- **Parametros:** `filter` opcional: por worker_id, estado (running/completed/failed), tiempo
- **Cuando usar:** Para verificar progreso de obreros activos o reportar status.
- **Cuando NO usar:** Antes de despachar (no hay workers).
- **Descripcion funcional:** Retorna estado de obreros activos: running, completed, failed, tiempo transcurrido, ultimo output.
- **Notas:** Polling pattern. No bloquea.

## cancel_worker

- **Firma:** `worker_id: string -> CancelResult`
- **Parametros:** `worker_id` del obrero a cancelar
- **Cuando usar:** Obrero stuck en loop, produciendo garbage, o superando tiempo razonable.
- **Cuando NO usar:** Cuando obrero esta haciendo progreso visible.
- **Descripcion funcional:** Envia senal de cancelacion al obrero. Cambios parciales del obrero quedan en el filesystem.
- **Notas:** Cancelacion parcial es segura — los cambios de archivo son atomicos.

## search_kb

- **Firma:** `query: string -> KBEntry[]`
- **Parametros:** `query` con topic o concepto de metodologia
- **Cuando usar:** Para responder preguntas metodologicas o consultar heuristicas de ingenieria agentica.
- **Cuando NO usar:** Para detalles de implementacion (eso es trabajo del obrero).
- **Descripcion funcional:** Busca en KB agentic-engineering-praxis y recursos relacionados.
- **Notas:** Complementa razonamiento; no reemplaza output final.

## read_codebase

- **Firma:** `paths: string[] -> FileContent[]`
- **Parametros:** `paths` con rutas de archivos a leer del repo target
- **Cuando usar:** Para evaluar blast radius o revisar arquitectura de archivos especificos.
- **Cuando NO usar:** Para leer todo el repo (ser selectivo).
- **Descripcion funcional:** Lee archivos especificos del repositorio target para contexto.
- **Notas:** Leer solo lo necesario para la decision activa.

## review_diff

- **Firma:** `worker_id: string -> DiffContent`
- **Parametros:** `worker_id` del obrero cuyo diff se quiere revisar
- **Cuando usar:** Para validar coherencia arquitectonica del output del obrero.
- **Cuando NO usar:** Para review line-by-line (confiar en el obrero para detalles).
- **Descripcion funcional:** Obtiene git diff del trabajo del obrero para revision de alto nivel.
- **Notas:** Retorna git diff del obrero para revision de alto nivel.

## search_tooling

- **Firma:** `query: string, category?: "cli"|"model"|"router" -> ToolingEntry[]`
- **Parametros:** `query` con nombre de herramienta, modelo o criterio (ej. "cheapest for coding", "1M context models"). `category` filtra por tipo.
- **Cuando usar:** Para elegir modelo optimo por tarea, evaluar que CLI usar, o responder preguntas sobre herramientas/modelos.
- **Cuando NO usar:** Para buscar metodologia (usar search_kb). Para decisiones que no involucren seleccion de tooling.
- **Descripcion funcional:** Consulta inventario de tooling agentico — fichas de CLIs, modelos y routers con pricing, context window, strengths/weaknesses, y matriz de seleccion racional costo/calidad.

## search_openclaw

- **Firma:** `query: string, section?: string -> OpenClawDoc[]`
- **Parametros:** `query` con topic de OpenClaw. `section` opcional filtra por area: "gateway", "channels", "tools", "providers", "concepts", "install", "plugins", "skills", "security", "automation".
- **Cuando usar:** Para responder preguntas sobre OpenClaw, configurar workspaces de obreros que involucren OpenClaw, o disenar arquitecturas OpenClaw.
- **Cuando NO usar:** Para buscar metodologia agentica generica (usar search_kb). Para buscar modelos/CLIs (usar search_tooling).
- **Descripcion funcional:** Busca en el corpus completo de documentacion OpenClaw (`KNOWLEDGE/agengai/openclaw/`).
- **Notas:** Corpus sin frontmatter KORA (by design, externo). Secciones clave: gateway (33 docs), channels (28 docs), tools (35 docs), providers (33 docs), concepts (27 docs).

## catalog_resolve

- **Firma:** `urn: string -> FilePath`
- **Parametros:** `urn` con identificador KORA
- **Cuando usar:** Cuando una referencia KB necesita resolucion a archivo fisico.
- **Cuando NO usar:** Para recursos fuera de KORA.
- **Descripcion funcional:** Resuelve URN KORA a ruta de archivo.
- **Notas:** Usa infraestructura `scripts/kora resolve`.


# Federacion kora — derivacion inter-agente

Este agente es miembro de la federacion kora. Puede derivar casos a otros agentes cuando un problema esta fuera de su dominio.

### Directorio de la federacion

Lee `/home/node/shared/federation/directorio-agentes.md` para saber que agentes existen, que hacen y como contactarlos. Este archivo esta siempre actualizado.

### Como derivar a otro agente

Usa `web_fetch` para enviar un hook al gateway del agente destino:

```
POST http://{gateway_host}:{port}/hooks/agent
Authorization: Bearer 766c9b38b53702cd0c994d7361c25e0bc5e6a3c671d1ac76
Content-Type: application/json

{
  "message": "[Derivacion de {mi-nombre}] {contexto del caso y motivo}",
  "name": "derivacion-{mi-nombre}"
}
```

Agentes disponibles (referencia rapida):

| Agente | Gateway | Hook URL |
|---|---|---|
| korax | kora-personal | `http://kora-personal:18789/hooks/agent` |
| steipete | kora-steipete | `http://kora-steipete:18810/hooks/agent` |
| salubrista-hah | kora-salubrista | `http://kora-salubrista:18830/hooks/agent` |

### Cuando derivar

- Solo cuando el caso esta **fuera de tu dominio** (ver Reglas Duras en AGENTS.md)
- Incluir contexto suficiente para que el destino no necesite preguntar de vuelta
- Informar al usuario que estas derivando y a quien

### Espacio compartido

- Tu directorio propio (lectura/escritura): `/home/node/shared/{mi-id}/`
- Directorio de la federacion (solo lectura): `/home/node/shared/federation/`
- Puedes dejar documentos en tu directorio para que otros agentes los lean si el operador configura visibilidad cruzada
