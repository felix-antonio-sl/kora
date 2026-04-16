# Memory — steipete

## Regla de uso

Clasificar cada dato importante antes de usarlo:
- `estado_vivo` — verificado contra repo, runtime o configuracion actual
- `memoria_operativa` — convenciones locales utiles para ejecutar
- `legado` — contexto historico; no decidir con esto sin validacion presente

Si hay conflicto entre categorias, manda `estado_vivo`.

## Estado vivo

- steipete es el agente operativo actual del workspace
- fuente viva de producto para OPModel: `/home/felix/projects/opmodel`
- fuente viva de metodologia OPM/ISO: `/home/felix/kora/KNOWLEDGE/fxsl/opm/`

## Memoria operativa

- entrada de composicion Steinberg: `reference/steinberg-index.md`
- para coding agents: preferir ACP via `sessions_spawn(runtime: "acp", agentId: ...)` cuando el runtime lo soporte
- `claude` CLI no se usa como agente de coding local
- `cwd` de ejecucion debe ser un repo real cuando se despachan agentes de coding
- produccion documental en `output/` si aplica; cross-agent via path absoluto
- `hsc-cli` se trabaja en modo `hv2-only` salvo bug critico de seguridad en `h`
- reentrada rapida de `hsc-cli`: `README.md`, `docs/hv2/START-HERE.md`, `docs/hv2/WORKSET.md`
- `scripts/dev/{build,test,smoke}.sh` de `hsc-cli` son `hv2-first`
- `hv2` ya expone superficies operativas `board`, `current`, `timeline` y `pending`
- `hv2 pending` separa `pending` y `completed`, con `workflow_state` y enlace heuristico a resultados observacionales
- `hv2 conditions` ya hidrata desde `DAU + SGH + HCC + OSIRIS` sin construir una problem list sintetica
- `hv2 observations` mejora parsing LIS: filtra metadata espuria, soporta mejor resultados con comparadores y expone `triage-category` + fallback de SV desde triage
- `hv2 observations` ahora soporta filtrado `--series` por analito/codigo y orden cronologico, manteniendo la semantica de observaciones atomicas
- `hv2 components` extrae triage `motivo/antecedentes/alergias` con parser mas robusto
- `hv2 timeline` ya tiene tests directos para orden, warnings y agregacion multi-fuente
- `hv2 service-requests` ya incluye DAU actual + examenes/interconsultas de `HCC primary`
- `hv2 medication-requests` ya incluye DAU actual + prescripciones de `HCC primary` filtradas contra no-medicacion obvia
- `hv2 current` y `hv2 pending` siguen siendo superficies del encounter DAU activo, aunque los record surfaces subyacentes tengan mas longitudinalidad
- la frontera de `hv2` quedo explicitada: sesiones de consulta, turnos y revisiones de caseload viven en una capa superior; `hv2` solo extrae/normaliza/proviene ladrillos
- `hsc-agent` ya tiene artefactos base para esa capa superior: README, overview de session layer, contrato de ingestión desde `hv2`, reglas de reconcile y schema SQL mínimo en `db/schema/001_session_layer.sql`

## Legado

- `reference/legacy-steipete/` y `reference/opmodel/legacy-steipete/` son memoria y contexto, no estado vivo
- el steipe antiguo es antecedente historico util; steipete actual es sucesor, no copia
- si un dato viene de memorias o sesiones antiguas, marcarlo como legado hasta validarlo contra el presente
