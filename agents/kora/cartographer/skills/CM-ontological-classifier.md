---
_manifest:
  urn: "urn:kora:agent-bootstrap:cartographer-cm-ontological-classifier:1.0.0"
  type: "lazy_load_endofuntor"
---

## Proposito

Clasificar cada elemento del dominio segun su naturaleza ontologica: entidad, evento, clasificador, relacion o medicion.

## Input/Output

- **Input:** Elementos inventariados y patrones detectados desde S-MAPEAR
- **Output:** Clasificacion ontologica de cada elemento con test aplicado

## Procedimiento

1. Para cada elemento, aplicar test de clasificacion:
   - **ENTIDAD:** ¿Tiene identidad propia? ¿Persiste en tiempo? → Ej: IPR, Convenio, Funcionario, Documento
   - **EVENTO:** ¿Ocurre en un momento? ¿Cambia estado de algo? → Ej: Aprobacion, Pago, Rendicion, Auditoria
   - **CLASIFICADOR:** ¿Sirve para categorizar otras cosas? → Ej: TipoFondo, EstadoIPR, Dominio, Rol
   - **RELACION:** ¿Conecta dos cosas con semantica propia? → Ej: Asignacion(persona-cargo), Membresia, Participacion
   - **MEDICION:** ¿Es valor numerico/cualitativo sobre algo? → Ej: MontoEjecutado, PorcentajeAvance, NivelRiesgo
2. Documentar test aplicado y justificacion
3. Si ambiguo → marcar para resolucion de tension en fase CRISTALIZAR

## Signature Output

```
**Clasificacion Ontologica**:
| Elemento | Naturaleza | Test | Justificacion |
|----------|-----------|------|---------------|
| [nombre] | [ENTIDAD/EVENTO/CLASIFICADOR/RELACION/MEDICION] | [test] | [razon] |
```
