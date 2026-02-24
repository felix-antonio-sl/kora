---
_manifest:
  urn: "urn:fxsl:agent-bootstrap:ingeniero-sistemas-composicional-cm-work-system-analyzer:1.0.0"
  type: "lazy_load_endofunctor"
---

## Proposito

Analizar sistema usando Work System Perspective (Alter). Mapear 9 elementos del sistema de trabajo y 17 facetas de trabajo para comprension integral.

## Input/Output

- **Input:** Dominio o sistema existente desde cualquier estado que requiera analisis WS
- **Output:** Work System Snapshot con 9 elementos y facetas relevantes

## Procedimiento

1. Mapear 9 elementos del Work System:
   - PARTICIPANTES: Quienes realizan actividades?
   - PROCESOS: Que actividades se realizan?
   - INFORMACION: Que informacion se usa/produce?
   - TECNOLOGIAS: Que herramientas se usan?
   - CLIENTES: Quienes reciben productos/servicios?
   - PRODUCTOS/SERVICIOS: Que se produce?
   - ENTORNO: Que factores externos influyen?
   - INFRAESTRUCTURA: Que recursos compartidos se usan?
   - ESTRATEGIAS: Que estrategias guian el sistema?
2. Identificar facetas de trabajo relevantes:
   Tomar decisiones, Comunicarse, Procesar informacion, Pensar, Representar realidad, Proveer informacion, Aplicar conocimiento, Aprender, Planificar, Controlar, Improvisar, Coordinar, Trabajo fisico, Trabajo soporte, Interaccion social, Proveer servicios, Crear valor, Seguridad
3. Evaluar balance sociotecnico
4. Identificar workarounds existentes o probables

## Signature Output

```
## Work System Snapshot
| Elemento | Descripcion |
|----------|-------------|
| Participantes | {quienes} |
| Procesos | {que hacen} |
| Informacion | {que datos} |
| Tecnologias | {que herramientas} |
| Clientes | {quienes reciben} |
| Productos/Servicios | {que producen} |
| Entorno | {factores externos} |
| Infraestructura | {recursos compartidos} |
| Estrategias | {guias} |

### Facetas Dominantes
{facetas de trabajo mas relevantes}

### Balance Sociotecnico
{evaluacion}
```
