# Mapa UI de turno

## Regla general

Pensar la UI asi:

1. `DAU` = episodio actual
2. `SGH` = historia hospitalaria
3. `LIS` = resultado duro de laboratorio
4. `HCC` / `OSIRIS` = longitudinal ambulatorio y compartido

## Pantallas clave

### Board DAU

Sirve para:

- pacientes activos
- `atencion_id`
- box/camilla
- categoria
- servicio
- tratante

Abrirlo cuando la pregunta sea operativa ahora.

### Episodio DAU

Pantalla pivote del caso actual.

Sirve para:

- validar sujeto
- entrar al resto de submodulos

### Triage / ingreso

Sirve para:

- motivo de consulta
- antecedentes resumidos
- alergias
- categoria
- derivacion

Fuente primaria para triage y parte del presenting inicial.

### Atencion medica

Sirve para:

- anamnesis
- examen fisico
- hipotesis
- CIE10
- GES / sospecha GES cuando exista

Fuente primaria para el nucleo clinico del episodio actual.

### Solicitudes y procedimientos

Sirve para:

- laboratorio pedido
- imagen solicitada
- indicaciones
- ejecucion
- procedimientos de box

No todo aqui es medicacion.
Parte es workflow, parte es clinica.

### Observaciones densas

Sirve para:

- observaciones de enfermeria
- soporte
- procedimientos menores
- resultados embebidos
- informes radiologicos inline

Abrirla si sospechas hueco importante en imagenologia o evolucion fina.

### Signos vitales

Sirve para:

- ultimos controles
- series
- tendencia

Abrirla cuando la pregunta dependa de evolucion, no solo de snapshot.

### Indicaciones de alta / plan

Sirve para:

- destino
- manejo consolidado
- plan de hospitalizacion o egreso

### SGH

Sirve para:

- hospitalizaciones previas
- evoluciones
- epicrisis

### LIS

Sirve para:

- resultado cuantitativo exacto
- confirmacion dura del laboratorio

### HCC / OSIRIS

Sirve para:

- preatencion
- longitudinalidad
- atenciones previas ambulatorias o compartidas

## Jerarquia de verdad

### Para episodio activo

- DAU actual primero
- observaciones densas si el caso esta vivo o raro
- signos vitales para evolucion
- solicitudes/procedimientos para pendientes

### Para laboratorio exacto

- LIS

### Para historia hospitalaria

- SGH

### Para longitudinalidad ambulatoria

- HCC / OSIRIS

## Regla de navegacion

Si el brief no responde bien la pregunta, mandar al humano a la pantalla que
es fuente primaria para esa clase de verdad.

## Fuentes de origen

> **DECOMMISSION 2026-06-22**: los repos `~/projects/hsc` y `~/projects/hsc-cli`
> fueron dados de baja y los binarios `hv2` + `hsc-agent` archivados (fuera del
> PATH). Las rutas de abajo apuntan a un repo MUERTO y se conservan solo como
> procedencia histórica. NO son referencia viva.
>
> **Sucesor**: `hsc-agent-cli` (binario `hsc-agent-cli`), la vitrina clínica
> autónoma (DAU/SGH/LIS/HCC, JSON puro, comandos cerrados). Para el mapa de
> superficies y la navegación vigentes, ver:
> - Referencia upstream absorbida (mapas UI→endpoint, manuales DAU/SGH):
>   `~/projects/hsc-agent-cli/docs/reference/`
> - Manual canónico del agente (KORA, fuente única por URN):
>   `urn:salud:kb:manual-agente-hsc-agent-cli`
>   (`~/kora-pneuma/artefactos/conocimiento/salud/manual-agente-hsc-agent-cli.md`)

Destilado desde (rutas históricas, repo decommissioned 2026-06-22):

- `/home/felix/projects/hsc/cli/docs/hv2/urgent-care-direct-platform-manual-2026-04-15.md`
- `/home/felix/projects/hsc/cli/docs/architecture/dau-active-care-coverage-matrix-2026-04-15.md`
- `/home/felix/projects/hsc/docs/go-live-checklist-urgent-agent-2026-04-19.md`
